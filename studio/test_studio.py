import copy
import json
import tempfile
import subprocess
import unittest
import zipfile
import httpx
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient
from PIL import Image

from . import engine, provider, storage
from .app import TOKEN, app
from .rules import validate_analysis, validate_plan, validate_script, video_prompt


def fixture():
    speech = [
        "What have you been thinking about today? Take a moment and notice who came to mind.",
        "Comment two two two to save this reflection, then follow me and check my stories for more.",
        "Keep this thought with you today, and come back whenever you want a moment for yourself."]
    script = {'takes': [{'id': f'T{i+1}', 'speech': s, 'beat': 'Beat', 'translation': 'Tradução',
                          'action': 'Ela olha para a lente.', 'setup': ['A','B','C'][i]}
                         for i,s in enumerate(speech)], 'notes': 'Fixture', 'identity_lock': 'Identity', 'continuity': 'Same room'}
    prompt = {'scene': 'A United States flag in the room', 'state': 'Initial state',
              'negative': 'no captions, no subtitles', 'realism': 'natural'}
    plan = {'notes': 'Test', 'frames': [
        {'id':'REF-CARTA','title':'Reference','role':'reference','parent':None,'takes':[], 'hook_id':None,'prompt':prompt},
        {'id':'K01','title':'Hook','role':'hook','parent':None,'takes':['T1'], 'hook_id':'H1','prompt':prompt},
        {'id':'K02','title':'Body','role':'body','parent':None,'takes':['T2'], 'hook_id':None,'prompt':prompt},
        {'id':'K03','title':'CTA','role':'cta','parent':'K02','takes':['T3'], 'hook_id':None,'prompt':prompt}]}
    return script, plan


class StudioTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.data_patch = patch.object(storage, 'DATA', Path(self.temp.name))
        self.data_patch.start()
        provider.configure('', 'gpt-5.4', kie_key='', gemini_key='', allow_temp_upload=False, text_provider='auto')
        self.client = TestClient(app)
        self.headers = {'X-Studio-Token':TOKEN}
        self.p = storage.create('Test', 'Shelby', '')
        self.pid = self.p['id']

    def tearDown(self):
        self.client.close()
        self.data_patch.stop()
        self.temp.cleanup()

    def ready(self):
        script, plan = fixture()
        Image.new('RGB',(120,200),'white').save(storage.folder(self.pid)/'anchor.png')
        storage.write_json(storage.folder(self.pid)/'ANALISE.json', {'hero':'Test'})
        storage.change(self.pid, script=script, plan=plan, selected=['H1'], sources=[],
                       hooks=[{'id':'H1','action':'Ela abre o envelope.'}], max_attempts=2, status='plan_ready')
        return script, plan

    def test_csrf_and_origin(self):
        self.assertEqual(self.client.post('/api/config',json={'api_key':'secret'}).status_code,403)
        self.assertEqual(self.client.post('/api/config',json={'api_key':'secret'},headers={**self.headers,'Origin':'https://evil.example'}).status_code,403)
        r=self.client.post('/api/config',json={'api_key':'secret-test'},headers=self.headers)
        self.assertEqual(r.status_code,200)
        self.assertNotIn('secret-test',r.text)
        self.assertNotIn('secret-test',self.client.get('/api/config').text)

    def test_browser_upload_with_empty_optional_anchor(self):
        anchor = storage.folder(self.pid) / 'registered.png'
        Image.new('RGB', (120, 200), 'white').save(anchor)
        probe = subprocess.CompletedProcess([], 0, json.dumps({
            'streams': [{'codec_type': 'video'}], 'format': {'duration': '29'}}), '')
        with patch('studio.app.AVATARS', {'shelby': ('Shelby', anchor)}), \
             patch('studio.app.subprocess.run', return_value=probe), \
             patch('studio.app.snapshot', return_value=[]):
            r = self.client.post('/api/projects', headers=self.headers,
                data={'title': 'Browser upload', 'avatar': 'shelby'},
                files={'video': ('test.mp4', b'local-test', 'video/mp4'),
                       'anchor': ('', b'', 'application/octet-stream')})
        self.assertEqual(r.status_code, 200, r.text)
        self.assertEqual(r.json()['status'], 'uploaded')

    def test_no_path_escape(self):
        with self.assertRaises(ValueError): storage.artifact(self.pid,'../studio.sqlite3')
        with self.assertRaises(ValueError): storage.folder('../')

    def test_script_gate_and_exact_speech(self):
        script,_=fixture()
        validate_script(script)
        for t in script['takes']: self.assertIn('"'+t['speech']+'"',video_prompt(t,t['action']))
        bad=copy.deepcopy(script);bad['takes'][0]['speech']='Short.'
        with self.assertRaises(ValueError): validate_script(bad)
        bad=copy.deepcopy(script);bad['takes'][1]['speech']=bad['takes'][1]['speech'].replace('two two two','yes')
        with self.assertRaises(ValueError): validate_script(bad)

    def test_dependency_and_take_coverage(self):
        script,plan=fixture();validate_plan(plan,['H1'],script)
        bad=copy.deepcopy(plan);bad['frames'][-1]['parent']='K99'
        with self.assertRaises(ValueError): validate_plan(bad,['H1'],script)
        bad=copy.deepcopy(plan);bad['frames'][-1]['takes']=['T2']
        with self.assertRaises(ValueError): validate_plan(bad,['H1'],script)

    def test_approval_gates_and_key_requirement(self):
        r=self.client.post(f'/api/projects/{self.pid}/run/generate',json={},headers=self.headers)
        self.assertEqual(r.status_code,400)
        storage.change(self.pid,status='analysis_ready',analysis={'ambiguity':True})
        r=self.client.post(f'/api/projects/{self.pid}/approve/analysis',json={},headers=self.headers)
        self.assertEqual(r.status_code,400)
        r=self.client.post(f'/api/projects/{self.pid}/approve/analysis',json={'clarification':'O envelope é o herói.'},headers=self.headers)
        self.assertEqual(r.status_code,200)
        r=self.client.post(f'/api/projects/{self.pid}/run/script',json={},headers=self.headers)
        self.assertEqual(r.status_code,400)
        self.assertFalse(storage.get(self.pid)['busy'])

    def test_generate_export_resume_no_duplicate(self):
        script,plan=self.ready()
        provider.configure('test')
        def image(pid,prompt,refs,dest):
            dest.parent.mkdir(exist_ok=True)
            Image.new('RGB',(120,200),'white').save(dest)
        review={'pass':True,'issues':[], 'checks':{k:True for k in ['identity','hands','prop','initial_state','composition','kit','text']}}
        with patch.object(provider,'image',side_effect=image) as generator, patch.object(provider,'think',return_value=review):
            engine.generate(self.pid)
            self.assertEqual(generator.call_count,4)
            engine.generate(self.pid)
            self.assertEqual(generator.call_count,4)
        p=storage.get(self.pid)
        self.assertEqual(p['status'],'complete')
        with zipfile.ZipFile(storage.folder(self.pid)/'auraly-flow.zip') as z:
            self.assertIn('hook/K01.png',z.namelist())
            self.assertIn('cta/K03.png',z.namelist())
            self.assertIn('FLOW_PROMPTS.txt',z.namelist())
            manifest=json.loads(z.read('manifest.json'))
            for clip in manifest['clips']:
                t=next(t for t in script['takes'] if t['id']==clip['take'])
                self.assertIn('"'+t['speech']+'"',clip['prompt'])

    def test_received_image_not_regenerated_after_reviewer_failure(self):
        self.ready();provider.configure('test')
        def image(pid,prompt,refs,dest):
            dest.parent.mkdir(exist_ok=True);Image.new('RGB',(120,200),'white').save(dest)
        with patch.object(provider,'image',side_effect=image) as generator, patch.object(provider,'think',side_effect=ValueError('review unavailable')):
            with self.assertRaises(ValueError): engine.generate(self.pid)
            self.assertEqual(storage.get(self.pid)['assets']['REF-CARTA']['status'],'review_pending')
            with self.assertRaises(ValueError): engine.generate(self.pid)
            self.assertEqual(generator.call_count,1)

    def test_interrupted_image_requires_explicit_retry(self):
        self.ready();provider.configure('test')
        storage.change(self.pid,assets={'REF-CARTA':{'status':'generating','attempts':[{'status':'generating'}]}})
        with patch.object(provider,'image') as generator:
            with self.assertRaises(ValueError): engine.generate(self.pid)
            generator.assert_not_called()

    def test_retry_limit_only_applies_to_selected_image(self):
        self.ready()
        attempts = [{'status': 'rejected'}, {'status': 'rejected'}]
        storage.change(self.pid, assets={'REF-CARTA': {'status': 'rejected', 'attempts': attempts}})
        r = self.client.post(f'/api/projects/{self.pid}/assets/REF-CARTA/review',
                             json={'decision': 'retry'}, headers=self.headers)
        self.assertEqual(r.status_code, 200)
        p = storage.get(self.pid)
        self.assertEqual(p['max_attempts'], 2)
        self.assertEqual(p['retry_limits'], {'REF-CARTA': 3})

    def test_reference_cannot_contain_spoken_takes(self):
        script, plan = fixture()
        plan['frames'][0]['takes'] = ['T1']
        with self.assertRaises(ValueError): validate_plan(plan, ['H1'], script)

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
        storage.change(self.pid, call_limits={'text': 1, 'image': 1}, calls=[{'route': 'responses'}])
        with patch('studio.provider.httpx.Client') as client:
            with self.assertRaises(ValueError): provider.request(self.pid, 'responses', json={})
            client.assert_not_called()
        self.assertEqual(len(storage.get(self.pid)['calls']), 1)

    def test_pause_preserves_asset_state_before_next_call(self):
        self.ready(); provider.configure('test')
        storage.change(self.pid, pause_requested=True)
        with patch.object(provider, 'image') as image:
            with self.assertRaises(ValueError): engine.generate(self.pid)
            image.assert_not_called()
        self.assertEqual(storage.get(self.pid)['assets'], {})

    def test_verify_access_only_consults_catalog(self):
        provider.configure('test', 'gpt-6-astra', 'medium')
        with patch('studio.provider.httpx.Client') as client:
            connection = client.return_value.__enter__.return_value
            connection.get.side_effect = [httpx.Response(200, json={'id': 'gpt-6-astra'}),
                                          httpx.Response(200, json={'id': 'gpt-image-2'})]
            result = provider.verify_access()
            connection.post.assert_not_called()
            self.assertEqual(connection.get.call_count, 2)
        self.assertEqual(result['kind'], 'catalog_only')
        self.assertEqual(storage.get(self.pid)['calls'], [])

    def test_directed_correction_and_original_anchor_in_derived_edits(self):
        self.ready(); provider.configure('test')
        folder = storage.folder(self.pid)
        Image.new('RGB', (120, 200), 'white').save(folder / 'ref.png')
        Image.new('RGB', (120, 200), 'white').save(folder / 'rejected.png')
        storage.change(self.pid, assets={
            'REF-CARTA': {'status': 'approved', 'file': 'ref.png', 'attempts': []},
            'K01': {'status': 'rejected', 'file': 'rejected.png', 'correction': 'Fix only the hand.',
                    'feedback': [{'text': 'Fix only the hand.'}], 'attempts': [{'status': 'rejected'}]}})
        def image(pid, prompt, refs, dest):
            dest.parent.mkdir(exist_ok=True); Image.new('RGB', (120, 200), 'white').save(dest)
        review = {'pass': True, 'issues': [], 'checks': {k: True for k in
            ['identity','hands','prop','initial_state','composition','kit','text']}}
        with patch.object(provider, 'image', side_effect=image) as generator, \
             patch.object(provider, 'think', return_value=review):
            engine.generate(self.pid)
        first = generator.call_args_list[0]
        self.assertIn('Fix only the hand.', first.args[1])
        self.assertEqual(first.args[2][0], folder / 'rejected.png')
        self.assertIn(folder / 'anchor.png', generator.call_args_list[-1].args[2])
        self.assertEqual(storage.get(self.pid)['assets']['K01']['feedback'][0]['text'], 'Fix only the hand.')

    def test_analysis_rejects_gaps_and_fake_timestamps(self):
        analysis = {'hero': 'Card', 'hero_evidence': [.2], 'ambiguity': False,
            'beats': [{'start': 0, 'end': 3, 'visual': 'Card', 'type': 'TALKING',
                       'label': 'HOOK', 'change': 'Reveals card'}]}
        validate_analysis(analysis, 3)
        bad = copy.deepcopy(analysis); bad['hero_evidence'] = [float('nan')]
        with self.assertRaises(ValueError): validate_analysis(bad, 3)
        bad = copy.deepcopy(analysis); bad['beats'][0]['end'] = 1
        with self.assertRaises(ValueError): validate_analysis(bad, 3)


if __name__ == '__main__': unittest.main()
