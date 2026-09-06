import io
import json
import zipfile
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest.mock import patch
from fastapi.testclient import TestClient
from PIL import Image
from . import browser_queue as q, storage as store
from .app import app, TOKEN
from .test_studio import fixture


class BrowserQueueTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.patches = [patch.object(store, 'DATA', self.root / 'data'),
                        patch.object(q, 'DOWNLOADS', self.root / 'Downloads')]
        for p in self.patches:
            p.start()
        self.client = TestClient(app)
        self.headers = {'x-studio-token': TOKEN}

    def tearDown(self):
        self.client.close()
        for p in self.patches:
            p.stop()
        self.temp.cleanup()

    def project(self, avatars=('Robin', 'Casey')):
        store.DATA.mkdir(exist_ok=True)
        p = store.create('Pilot', '')
        script, imageset = fixture()
        folder = store.folder(p['id'])
        (folder / 'avatars').mkdir()
        rows = []
        for i, name in enumerate(avatars, 1):
            aid = f'av{i:02}'
            Image.new('RGB', (512, 768), 'white').save(folder / 'avatars' / f'{aid}.png')
            rows.append({'id': aid, 'name': name, 'file': f'avatars/{aid}.png'})
        store.change(p['id'], status='imageset_ready', script=script, imageset=imageset,
                     selected=['H1'], hooks=[{'id': 'H1', 'action': 'She opens the envelope.'}],
                     avatars=rows)
        return p['id']

    def image(self, color='red', fmt='PNG'):
        b = io.BytesIO()
        Image.new('RGB', (512, 768), color).save(b, format=fmt)
        return b.getvalue()

    def drive_all(self, pid, fmt='JPEG'):
        """Enqueue, then send every job and receive an image for it."""
        q.enqueue([pid])
        q.control(True, 4)
        jobs = []
        while (job := q.claim()):
            q.update(job['id'], 'submitting', tab_id=100)
            q.update(job['id'], 'generating')
            q.receive(job['id'], self.image(fmt=fmt))
            jobs.append(job)
        return jobs

    def test_enqueue_fans_over_avatars_and_is_idempotent(self):
        pid = self.project()
        s = q.enqueue([pid])
        self.assertEqual(len(s['jobs']), 6)  # 2 avatars x 3 frames
        self.assertEqual({j['frame'] for j in s['jobs']}, {'K01', 'BODY', 'CTA'})
        self.assertEqual({j['avatar'] for j in s['jobs']}, {'Robin', 'Casey'})
        self.assertEqual(len(q.enqueue([pid])['jobs']), 6)
        robin = next(j for j in s['jobs'] if j['avatar'] == 'Robin')
        self.assertEqual(q.anchor(robin['id']), store.folder(pid) / 'avatars/av01.png')

    def test_downloads_layout_one_run_folder_with_avatar_subfolders(self):
        pid = self.project()
        s = q.enqueue([pid])
        dirs = {Path(j['destination_dir']) for j in s['jobs']}
        # every avatar folder shares one dated run folder, itself under "Auraly Studio"
        self.assertEqual({d.parent for d in dirs}, {self.root / 'Downloads' / 'Auraly Studio' /
                                                    f'{__import__("datetime").date.today():%Y-%m-%d}_Pilot_{pid[:8]}'})
        self.assertEqual({d.name for d in dirs}, {'Robin', 'Casey'})

    def test_receive_writes_veo_video_prompts_beside_the_images(self):
        pid = self.project()
        jobs = self.drive_all(pid)
        dest = Path(next(j for j in jobs if j['avatar_id'] == 'av01')['destination_dir'])
        text = (dest / 'PROMPTS_VIDEO_VEO.txt').read_text(encoding='utf-8')
        self.assertIn('Veo 3.1', text)
        self.assertIn('Robin', text)
        for take in store.get(pid)['script']['takes']:
            self.assertIn(take['speech'], text)

    def test_claim_never_duplicates_or_mixes_avatar(self):
        pid = self.project()
        q.enqueue([pid])
        q.control(True, 4)
        with ThreadPoolExecutor(max_workers=8) as pool:
            jobs = [j for j in pool.map(lambda _: q.claim(), range(8)) if j]
        self.assertEqual(len(jobs), 2)
        self.assertEqual({j['avatar_key'] for j in jobs}, {f'{pid[:8]}:av01', f'{pid[:8]}:av02'})

    def test_attention_blocks_only_its_avatar(self):
        pid = self.project()
        q.enqueue([pid])
        q.control(True, 1)
        job = q.claim()
        q.update(job['id'], 'attention', error='limit')
        other = q.claim()
        self.assertIsNotNone(other)
        self.assertNotEqual(other['avatar_id'], job['avatar_id'])
        self.assertIsNone(q.claim())

    def test_pause_blocks_new_send_but_preserves_pending_receipt(self):
        pid = self.project(('Robin',))
        q.enqueue([pid])
        q.control(True)
        job = q.claim()
        q.update(job['id'], 'submitting', tab_id=100)
        q.update(job['id'], 'generating')
        q.control(False)
        self.assertIsNone(q.claim())
        self.assertEqual(q.receive(job['id'], self.image())['status'], 'done')

    def test_restart_does_not_resend_and_retains_tab(self):
        pid = self.project(('Robin',))
        q.enqueue([pid])
        q.control(True)
        job = q.claim()
        q.update(job['id'], 'submitting', tab_id=100)
        q.update(job['id'], 'generating')
        q.recover()
        self.assertFalse(q.load()['running'])
        self.assertEqual(q.get_job(job['id'])['tab_id'], 100)
        q.control(True)
        self.assertIsNone(q.claim())

    def test_receipt_is_idempotent_and_keeps_actual_file_type(self):
        pid = self.project(('Robin',))
        q.enqueue([pid])
        q.control(True)
        job = q.claim()
        q.update(job['id'], 'submitting', tab_id=100)
        q.update(job['id'], 'generating')
        raw = self.image(fmt='JPEG')
        done = q.receive(job['id'], raw)
        self.assertTrue(done['file'].endswith('.jpg'))
        self.assertEqual(q.receive(job['id'], raw)['file'], done['file'])
        with self.assertRaises(ValueError):
            q.receive(job['id'], self.image('blue'))
        self.assertTrue((Path(done['file']).parent / 'manifest.json').is_file())

    def test_changed_anchor_rejected_for_that_avatar_only(self):
        pid = self.project()
        s = q.enqueue([pid])
        robin = next(j for j in s['jobs'] if j['avatar'] == 'Robin')
        casey = next(j for j in s['jobs'] if j['avatar'] == 'Casey')
        (store.folder(pid) / 'avatars/av01.png').write_bytes(self.image('blue'))
        with self.assertRaises(ValueError):
            q.anchor(robin['id'])
        self.assertEqual(q.anchor(casey['id']), store.folder(pid) / 'avatars/av02.png')

    def test_has_jobs_and_extension_bridge_auth(self):
        pid = self.project(('Robin',))
        self.assertFalse(q.has_jobs(pid))
        q.enqueue([pid])
        self.assertTrue(q.has_jobs(pid))
        path = '/api/browser/agent/state'
        self.assertEqual(self.client.get(path).status_code, 403)
        secret = q.token()
        headers = {'x-auraly-browser-token': secret, 'Origin': 'chrome-extension://' + 'a' * 32}
        self.assertEqual(self.client.get(path, headers=headers).status_code, 200)
        headers['Origin'] = 'https://chatgpt.com'
        self.assertEqual(self.client.get(path, headers=headers).status_code, 403)

    def test_pause_between_prepare_and_submit(self):
        pid = self.project(('Robin',))
        q.enqueue([pid])
        q.control(True)
        job = q.claim()
        q.control(False)
        with self.assertRaises(ValueError):
            q.update(job['id'], 'submitting')

    def test_export_requires_every_frame_approved_for_the_avatar(self):
        pid = self.project()
        jobs = self.drive_all(pid)
        robin = [j for j in jobs if j['avatar_id'] == 'av01']
        with self.assertRaisesRegex(ValueError, 'aprove'):
            q.export_package(pid, 'av01')
        for job in robin[:-1]:
            q.review(job['id'], 'approve')
        with self.assertRaisesRegex(ValueError, 'aprove'):
            q.export_package(pid, 'av01')
        self.assertFalse((store.folder(pid) / 'auraly-chrome-robin.zip').exists())

    def test_approved_export_has_real_format_speech_and_avatar(self):
        pid = self.project()
        jobs = self.drive_all(pid)
        for job in (j for j in jobs if j['avatar_id'] == 'av01'):
            q.review(job['id'], 'approve')
        with zipfile.ZipFile(q.export_package(pid, 'av01')) as z:
            self.assertIn('imagens/K01.jpg', z.namelist())
            self.assertIn('imagens/CTA.jpg', z.namelist())
            self.assertEqual(z.read('imagens/K01.jpg'), self.image(fmt='JPEG'))
            manifest = json.loads(z.read('manifest.json'))
            self.assertEqual(manifest['source'], 'chatgpt-chrome')
            self.assertIsNone(manifest['model'])
            self.assertEqual(manifest['avatar'], 'Robin')
            self.assertEqual(len(manifest['clips']), 3)
            flow = z.read('PROMPTS_VIDEO_VEO.txt').decode()
            self.assertIn('Veo 3.1', flow)
            for take in store.get(pid)['script']['takes']:
                self.assertIn(take['speech'], flow)
            self.assertIn('She opens the envelope.', flow)

    def test_review_retry_rebuilds_only_that_avatar_scene(self):
        pid = self.project()
        jobs = self.drive_all(pid)
        target = next(j for j in jobs if j['avatar_id'] == 'av01' and j['frame'] == 'K01')
        q.control(False)
        state = q.review(target['id'], 'retry')
        fresh = [j for j in state['jobs'] if j['status'] == 'queued']
        self.assertEqual(len(fresh), 1)
        self.assertEqual((fresh[0]['avatar_id'], fresh[0]['frame']), ('av01', 'K01'))
        self.assertEqual(fresh[0]['retry_of'], target['id'])
        self.assertEqual(next(j for j in state['jobs'] if j['id'] == target['id'])['status'], 'cancelled')

    def test_review_and_export_routes_require_local_authorization(self):
        pid = self.project()
        jobs = self.drive_all(pid)
        route = f"/api/browser/jobs/{jobs[0]['id']}/review"
        self.assertEqual(self.client.post(route, json={'decision': 'approve'}).status_code, 403)
        for job in (j for j in jobs if j['avatar_id'] == 'av01'):
            r = self.client.post(f"/api/browser/jobs/{job['id']}/review",
                                 json={'decision': 'approve'}, headers=self.headers)
            self.assertEqual(r.status_code, 200, r.text)
        path = f'/api/browser/projects/{pid}/avatars/av01/export'
        self.assertEqual(self.client.post(path).status_code, 403)
        r = self.client.post(path, headers=self.headers)
        self.assertEqual(r.status_code, 200, r.text[:200])
        self.assertTrue(zipfile.is_zipfile(io.BytesIO(r.content)))


if __name__ == '__main__':
    unittest.main()
