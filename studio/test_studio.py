import copy
import json
import tempfile
import subprocess
import unittest
import httpx
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient
from PIL import Image

from . import engine, provider, storage
from .app import TOKEN, app
from .rules import validate_analysis, validate_imageset, validate_script, video_prompt


def fixture():
    speech = [
        "What have you been thinking about today? Take a moment and notice who came to mind.",
        "Comment two two two to save this reflection, then follow me and check my stories for more.",
        "Keep this thought with you today, and come back whenever you want a moment for yourself."]
    script = {'takes': [{'id': f'T{i+1}', 'speech': s, 'beat': 'Beat', 'translation': 'Tradução',
                         'action': 'Ela olha para a lente.', 'setup': ['A', 'B', 'C'][i]}
                        for i, s in enumerate(speech)],
              'notes': 'Fixture', 'continuity': 'Mesma sala e figurino em todos os takes.'}
    prompt = {'scene': 'A United States flag on the wall behind the table', 'composition': 'chest-up',
              'state': 'Initial state before the action', 'lighting': 'neutral daylight',
              'realism': 'natural skin', 'negative': 'no captions, no subtitles'}
    imageset = {'notes': 'Test', 'frames': [
        {'id': 'K01', 'title': 'Hook', 'role': 'hook', 'hook_id': 'H1', 'takes': ['T1'], 'prompt': prompt},
        {'id': 'BODY', 'title': 'Body', 'role': 'body', 'hook_id': None, 'takes': ['T2'], 'prompt': prompt},
        {'id': 'CTA', 'title': 'CTA', 'role': 'cta', 'hook_id': None, 'takes': ['T3'], 'prompt': prompt}]}
    return script, imageset


class StudioTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.data_patch = patch.object(storage, 'DATA', Path(self.temp.name))
        self.data_patch.start()
        provider.configure('', 'gpt-5.4', gemini_key='', text_provider='auto')
        self.client = TestClient(app)
        self.headers = {'X-Studio-Token': TOKEN}
        self.p = storage.create('Test', '')
        self.pid = self.p['id']

    def tearDown(self):
        self.client.close()
        self.data_patch.stop()
        self.temp.cleanup()

    def ready_imageset(self):
        script, imageset = fixture()
        folder = storage.folder(self.pid)
        (folder / 'avatars').mkdir()
        avatars = []
        for aid in ('a1b2c3d4', 'e5f6a7b8'):
            Image.new('RGB', (120, 200), 'white').save(folder / 'avatars' / f'{aid}.png')
            avatars.append({'id': aid, 'name': f'Avatar {aid}', 'file': f'avatars/{aid}.png'})
        storage.change(self.pid, script=script, imageset=imageset, selected=['H1'],
                       hooks=[{'id': 'H1', 'action': 'Ela abre o envelope.'}],
                       avatars=avatars, status='imageset_ready')
        return script, imageset

    def test_csrf_and_origin(self):
        self.assertEqual(self.client.post('/api/config', json={'api_key': 'secret'}).status_code, 403)
        self.assertEqual(self.client.post('/api/config', json={'api_key': 'secret'},
            headers={**self.headers, 'Origin': 'https://evil.example'}).status_code, 403)
        r = self.client.post('/api/config', json={'api_key': 'secret-test'}, headers=self.headers)
        self.assertEqual(r.status_code, 200)
        self.assertNotIn('secret-test', r.text)
        self.assertNotIn('secret-test', self.client.get('/api/config').text)

    def test_upload_needs_only_a_video(self):
        probe = subprocess.CompletedProcess([], 0, json.dumps({
            'streams': [{'codec_type': 'video'}], 'format': {'duration': '29'}}), '')
        with patch('studio.app.subprocess.run', return_value=probe), \
             patch('studio.app.snapshot', return_value=[]):
            r = self.client.post('/api/projects', headers=self.headers,
                data={'title': 'Video only'},
                files={'video': ('test.mp4', b'local-test', 'video/mp4')})
        self.assertEqual(r.status_code, 200, r.text)
        self.assertEqual(r.json()['status'], 'uploaded')
        self.assertEqual(r.json()['avatars'], [])

    def test_no_path_escape(self):
        with self.assertRaises(ValueError): storage.artifact(self.pid, '../studio.sqlite3')
        with self.assertRaises(ValueError): storage.folder('../')

    def test_script_gate_and_exact_speech(self):
        script, _ = fixture()
        validate_script(script)
        for t in script['takes']:
            self.assertIn('"' + t['speech'] + '"', video_prompt(t, t['action']))
        bad = copy.deepcopy(script); bad['takes'][0]['speech'] = 'Short.'
        with self.assertRaises(ValueError): validate_script(bad)
        bad = copy.deepcopy(script)
        bad['takes'][1]['speech'] = bad['takes'][1]['speech'].replace('two two two', 'yes')
        with self.assertRaises(ValueError): validate_script(bad)

    def test_imageset_gate(self):
        script, imageset = fixture()
        validate_imageset(imageset, ['H1'], script)
        bad = copy.deepcopy(imageset); bad['frames'][0]['hook_id'] = 'H9'
        with self.assertRaises(ValueError): validate_imageset(bad, ['H1'], script)
        bad = copy.deepcopy(imageset); bad['frames'][1]['takes'] = ['T3']
        with self.assertRaises(ValueError): validate_imageset(bad, ['H1'], script)
        bad = copy.deepcopy(imageset); bad['frames'][0]['parent'] = 'K00'
        with self.assertRaises(ValueError): validate_imageset(bad, ['H1'], script)
        bad = copy.deepcopy(imageset); bad['frames'][2]['prompt'] = dict(bad['frames'][2]['prompt'], negative='')
        with self.assertRaises(ValueError): validate_imageset(bad, ['H1'], script)

    def test_run_imageset_blocked_before_hook_selection(self):
        r = self.client.post(f'/api/projects/{self.pid}/run/imageset', json={}, headers=self.headers)
        self.assertEqual(r.status_code, 400)
        storage.change(self.pid, status='analysis_ready', analysis={'ambiguity': True})
        r = self.client.post(f'/api/projects/{self.pid}/approve/analysis', json={}, headers=self.headers)
        self.assertEqual(r.status_code, 400)
        r = self.client.post(f'/api/projects/{self.pid}/approve/analysis',
            json={'clarification': 'O envelope é o herói.'}, headers=self.headers)
        self.assertEqual(r.status_code, 200)
        r = self.client.post(f'/api/projects/{self.pid}/run/script', json={}, headers=self.headers)
        self.assertEqual(r.status_code, 400)  # no think key configured
        self.assertFalse(storage.get(self.pid)['busy'])

    def test_script_stage_is_avatar_agnostic(self):
        provider.configure('test')
        storage.change(self.pid, status='analysis_approved', analysis={'hero': 'Envelope'},
                       transcript=[{'start': 0, 'text': 'x'}], direction='')
        script, _ = fixture()
        with patch.object(provider, 'think', return_value=script) as thinker:
            engine.script(self.pid)
        self.assertEqual(thinker.call_args.args[3] if len(thinker.call_args.args) > 3 else (), ())
        self.assertNotIn('avatar', thinker.call_args.args[2])
        self.assertEqual(storage.get(self.pid)['status'], 'script_ready')

    def test_imageset_stage_builds_frames_from_selected_hooks(self):
        provider.configure('test')
        script, imageset = fixture()
        storage.change(self.pid, status='hooks_selected', script=script, selected=['H1'],
                       hooks=[{'id': 'H1', 'action': 'a', 'title': 't'}])
        with patch.object(provider, 'think', return_value=imageset):
            engine.imageset(self.pid)
        p = storage.get(self.pid)
        self.assertEqual(p['status'], 'imageset_ready')
        self.assertEqual([f['id'] for f in p['imageset']['frames']], ['K01', 'BODY', 'CTA'])

    def test_add_and_remove_avatars(self):
        script, imageset = fixture()
        storage.change(self.pid, status='imageset_ready', script=script, imageset=imageset,
                       selected=['H1'], hooks=[{'id': 'H1', 'action': 'a'}])
        import io
        png = io.BytesIO(); Image.new('RGB', (100, 160), 'white').save(png, format='JPEG')
        r = self.client.post(f'/api/projects/{self.pid}/avatars', headers=self.headers,
            files=[('files', ('Shelby Turner.jpeg', png.getvalue(), 'image/jpeg')),
                   ('files', ('Kris.jpeg', png.getvalue(), 'image/jpeg'))])
        self.assertEqual(r.status_code, 200, r.text)
        avatars = storage.get(self.pid)['avatars']
        self.assertEqual([a['name'] for a in avatars], ['Shelby Turner', 'Kris'])
        self.assertTrue((storage.folder(self.pid) / avatars[0]['file']).is_file())
        r = self.client.delete(f'/api/projects/{self.pid}/avatars/{avatars[0]["id"]}', headers=self.headers)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(storage.get(self.pid)['avatars']), 1)

    def test_prepare_queue_requires_avatars(self):
        script, imageset = fixture()
        storage.change(self.pid, status='imageset_ready', script=script, imageset=imageset,
                       selected=['H1'], hooks=[{'id': 'H1', 'action': 'a'}], avatars=[])
        r = self.client.post(f'/api/projects/{self.pid}/queue', json={'ids': [self.pid]}, headers=self.headers)
        self.assertEqual(r.status_code, 400)

    def test_empty_transcript_stops_extraction_gate(self):
        folder = storage.folder(self.pid) / 'watch'
        folder.mkdir()
        (folder / 'audio').mkdir()
        storage.write_json(folder / 'manifest.json', {
            'info': {'duration': 1}, 'timeline': [{}] * 5, 'transcript': True})
        storage.write_json(folder / 'audio/transcript.json', [])
        with self.assertRaises(ValueError): engine.extract(self.pid)
        self.assertNotEqual(storage.get(self.pid)['status'], 'extracted')

    def test_analyze_reads_every_sheet_and_hook_frame(self):
        provider.configure('test')
        folder = storage.folder(self.pid)
        (folder / 'watch/audio').mkdir(parents=True)
        transcript = [{'start': 0, 'end': 2, 'text': 'Original speech.'}]
        storage.write_json(folder / 'watch/audio/transcript.json', transcript)
        timeline = [{'file': f't_{i:03}.png', 't': i * .2} for i in range(10)]
        storage.change(self.pid, extraction={'info': {'duration': 2}, 'timeline': timeline,
            'overview': {'scenes': ['scene.png'], 'timeline': ['timeline1.png', 'timeline2.png']}})
        analysis = {'hero': 'Envelope', 'hero_evidence': [.2], 'beats': [{'start': 0, 'end': 2,
            'visual': 'Envelope', 'label': 'HOOK', 'type': 'TALKING', 'change': 'Abre'}], 'ambiguity': False}
        with patch.object(provider, 'think', side_effect=[
                {'peak_times': []}, {'peak_times': []}, {'peak_times': []}, {}, {}, analysis]) as thinker:
            engine.analyze(self.pid)
            self.assertEqual(thinker.call_count, 6)
            seen = [path.name for call in thinker.call_args_list for path in
                    (call.args[3] if len(call.args) > 3 else [])]
        self.assertEqual(seen, ['scene.png', 'timeline1.png', 'timeline2.png'] + [f['file'] for f in timeline])
        self.assertEqual(storage.get(self.pid)['transcript'], transcript)
        self.assertEqual(storage.get(self.pid)['status'], 'analysis_ready')

    def test_astra_medium_is_sent_in_response_request(self):
        provider.configure('test', 'gpt-6-astra', 'medium')
        result = {'status': 'completed', 'output': [{'content': [
            {'type': 'output_text', 'text': '{"ok":true}'}]}]}
        with patch.object(provider, 'request', return_value=result) as request:
            self.assertTrue(provider.think(self.pid, 'Return JSON.', {})['ok'])
        payload = request.call_args.kwargs['json']
        self.assertEqual(payload['model'], 'gpt-6-astra')
        self.assertEqual(payload['reasoning'], {'effort': 'medium'})
        self.assertIn('JSON', payload['input'][0]['content'][0]['text'])
        self.assertNotIn('temperature', payload)

    def test_preferences_persist_without_key_and_invalid_key_not_echoed(self):
        secret = 'sk-proj-TEST_ONLY_NOT_A_REAL_CREDENTIAL'
        r = self.client.post('/api/config', headers=self.headers,
            json={'api_key': secret, 'text_model': 'gpt-6-astra', 'reasoning_effort': 'medium'})
        self.assertEqual(r.status_code, 200)
        prefs = (storage.DATA / 'preferences.json').read_text(encoding='utf-8')
        self.assertNotIn(secret, prefs)
        self.assertNotIn('api_key', prefs)
        provider.configure(model='gpt-5.4', effort='low')
        provider.load_preferences()
        self.assertEqual(provider.settings()['text_model'], 'gpt-6-astra')
        self.assertEqual(provider.settings()['reasoning_effort'], 'medium')
        invalid = secret * 30
        r = self.client.post('/api/config', headers=self.headers, json={'api_key': invalid})
        self.assertEqual(r.status_code, 422)
        self.assertNotIn(secret, r.text)

    def test_provider_error_redacts_key_and_records_model(self):
        secret = 'sk-proj-TEST_ONLY_NOT_A_REAL_CREDENTIAL'
        provider.configure(secret)
        response = httpx.Response(401, json={'error': {'message': 'Incorrect API key: ' + secret}})
        with patch('studio.provider.httpx.Client') as client:
            client.return_value.__enter__.return_value.post.return_value = response
            with self.assertRaises(ValueError) as caught:
                provider.request(self.pid, 'responses', json={
                    'model': 'gpt-6-astra', 'reasoning': {'effort': 'medium'}})
        self.assertNotIn(secret, str(caught.exception))
        p = storage.get(self.pid)
        self.assertNotIn(secret, json.dumps(p))
        self.assertEqual(p['calls'][0]['reasoning_effort'], 'medium')
        self.assertEqual(p['calls'][0]['status'], 'failed')

    def test_call_limit_prevents_network_request(self):
        provider.configure('test')
        storage.change(self.pid, call_limits={'text': 1}, calls=[{'route': 'responses'}])
        with patch('studio.provider.httpx.Client') as client:
            with self.assertRaises(ValueError): provider.request(self.pid, 'responses', json={})
            client.assert_not_called()
        self.assertEqual(len(storage.get(self.pid)['calls']), 1)

    def test_verify_access_only_consults_catalog(self):
        provider.configure('test', 'gpt-6-astra', 'medium')
        with patch('studio.provider.httpx.Client') as client:
            connection = client.return_value.__enter__.return_value
            connection.get.side_effect = [httpx.Response(200, json={'id': 'gpt-6-astra'})]
            result = provider.verify_access()
            connection.post.assert_not_called()
            self.assertEqual(connection.get.call_count, 1)
        self.assertEqual(result['kind'], 'catalog_only')
        self.assertEqual(storage.get(self.pid)['calls'], [])

    def test_analysis_rejects_gaps_and_fake_timestamps(self):
        analysis = {'hero': 'Card', 'hero_evidence': [.2], 'ambiguity': False,
            'beats': [{'start': 0, 'end': 3, 'visual': 'Card', 'type': 'TALKING',
                       'label': 'HOOK', 'change': 'Reveals card'}]}
        validate_analysis(analysis, 3)
        bad = copy.deepcopy(analysis); bad['hero_evidence'] = [float('nan')]
        with self.assertRaises(ValueError): validate_analysis(bad, 3)
        bad = copy.deepcopy(analysis); bad['beats'][0]['end'] = 1
        with self.assertRaises(ValueError): validate_analysis(bad, 3)


if __name__ == '__main__':
    unittest.main()
