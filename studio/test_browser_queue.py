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
        self.patches = [patch.object(store,'DATA',self.root/'data'), patch.object(q,'DOWNLOADS',self.root/'Downloads')]
        for p in self.patches: p.start()
        self.client = TestClient(app)
        self.headers = {'x-studio-token':TOKEN}

    def tearDown(self):
        self.client.close()
        for p in self.patches: p.stop()
        self.temp.cleanup()

    def project(self, avatar='Robin'):
        store.DATA.mkdir(exist_ok=True)
        p=store.create('Pilot',avatar,'')
        Image.new('RGB',(512,768),'white').save(store.folder(p['id'])/'anchor.png')
        store.change(p['id'],status='plan_ready',plan={'frames':[
            {'id':'REF-CARTA','role':'reference','prompt':{'scene':'Foil card'}},
            {'id':'K01','role':'hook','parent':None,'prompt':{'scene':'Kitchen','composition':'Chest height'}},
            {'id':'K02','role':'hook','parent':'K01','prompt':{'scene':'Same as K01, with honey'}}]})
        return p['id']

    def image(self,color='red',fmt='PNG'):
        b=io.BytesIO();Image.new('RGB',(512,768),color).save(b,format=fmt);return b.getvalue()

    def sent(self,pid):
        q.enqueue([pid]);q.control(True);job=q.claim()
        q.update(job['id'],'submitting',tab_id=100)
        q.update(job['id'],'generating',conversation_url='https://chatgpt.com/c/test-123')
        return job

    def test_anchor_only_parent_text_and_idempotent_enqueue(self):
        pid=self.project();s=q.enqueue([pid]);self.assertEqual(len(s['jobs']),2)
        self.assertIn('Kitchen',s['jobs'][1]['prompt'])
        self.assertIn('Foil card',s['jobs'][1]['prompt'])
        self.assertEqual(len(q.enqueue([pid])['jobs']),2)
        self.assertEqual(q.anchor(s['jobs'][0]['id']),store.folder(pid)/'anchor.png')

    def test_concurrent_claim_never_duplicates_or_mixes_avatar(self):
        a=self.project();b=self.project('Casey');c=self.project('Robin')
        q.enqueue([a,b,c]);q.control(True,4)
        with ThreadPoolExecutor(max_workers=8) as pool:
            jobs=[j for j in pool.map(lambda _:q.claim(),range(8)) if j]
        self.assertEqual(len(jobs),2);self.assertEqual({j['avatar'] for j in jobs},{'Robin','Casey'})

    def test_pause_blocks_new_send_but_preserves_pending_receipt(self):
        job=self.sent(self.project());q.control(False)
        self.assertIsNone(q.claim());done=q.receive(job['id'],self.image())
        self.assertEqual(done['status'],'done')

    def test_restart_does_not_resend_and_retains_tab(self):
        job=self.sent(self.project());q.recover()
        self.assertFalse(q.load()['running']);self.assertEqual(q.get_job(job['id'])['tab_id'],100)
        q.control(True);self.assertIsNone(q.claim())

    def test_receipt_is_idempotent_and_keeps_actual_file_type(self):
        job=self.sent(self.project());raw=self.image(fmt='JPEG')
        done=q.receive(job['id'],raw);self.assertTrue(done['file'].endswith('.jpg'))
        self.assertEqual(q.receive(job['id'],raw)['file'],done['file'])
        with self.assertRaises(ValueError):q.receive(job['id'],self.image('blue'))
        self.assertEqual(Path(done['file']).read_bytes(),raw)
        self.assertTrue((Path(done['file']).parent/'manifest.json').is_file())

    def test_changed_anchor_and_malformed_image_rejected(self):
        pid=self.project();job=self.sent(pid)
        (store.folder(pid)/'anchor.png').write_bytes(self.image('blue'))
        with self.assertRaises(ValueError):q.anchor(job['id'])
        with self.assertRaises(ValueError):q.receive(job['id'],b'not image')

    def test_attention_blocks_only_its_avatar(self):
        a=self.project();b=self.project('Casey');q.enqueue([a,b]);q.control(True)
        job=q.claim();q.update(job['id'],'attention',error='limit')
        self.assertEqual(q.claim()['avatar'],'Casey');self.assertIsNone(q.claim())

    def test_extension_requires_token_and_web_origins_cannot_use_bridge(self):
        path='/api/browser/agent/state'
        self.assertEqual(self.client.get(path).status_code,403)
        secret=q.token();headers={'x-auraly-browser-token':secret,'Origin':'chrome-extension://'+'a'*32}
        self.assertEqual(self.client.get(path,headers=headers).status_code,200)
        headers['Origin']='https://chatgpt.com'
        self.assertEqual(self.client.get(path,headers=headers).status_code,403)
        self.assertEqual(self.client.post('/api/browser/control',json={'running':True}).status_code,403)

    def test_pause_between_prepare_and_submit(self):
        q.enqueue([self.project()]);q.control(True);job=q.claim();q.control(False)
        with self.assertRaises(ValueError):q.update(job['id'],'submitting')

    def ready_for_export(self):
        pid = self.project()
        script, plan = fixture()
        store.change(pid, script=script, plan=plan, selected=['H1'],
                     hooks=[{'id':'H1','action':'She opens the envelope.'}])
        q.enqueue([pid]); q.control(True)
        jobs = []
        while job := q.claim():
            q.update(job['id'], 'submitting', tab_id=100)
            q.update(job['id'], 'generating')
            q.receive(job['id'], self.image(fmt='JPEG'))
            jobs.append(job)
        return pid, jobs

    def test_export_requires_all_scenes_and_manual_review(self):
        pid, jobs = self.ready_for_export()
        with self.assertRaisesRegex(ValueError, 'aprove'): q.export_package(pid)
        for job in jobs[:-1]: q.review(job['id'], 'approve')
        with self.assertRaisesRegex(ValueError, 'K03'): q.export_package(pid)
        self.assertFalse((store.folder(pid)/'auraly-chrome-flow.zip').exists())

    def test_approved_chrome_export_preserves_format_speech_and_skips_reference(self):
        pid, jobs = self.ready_for_export()
        for job in jobs: q.review(job['id'], 'approve')
        with zipfile.ZipFile(q.export_package(pid)) as z:
            self.assertIn('imagens/K01.jpg', z.namelist())
            self.assertFalse(any('REF-CARTA' in n for n in z.namelist()))
            self.assertEqual(z.read('imagens/K01.jpg'), self.image(fmt='JPEG'))
            manifest = json.loads(z.read('manifest.json'))
            self.assertEqual(manifest['source'], 'chatgpt-chrome')
            self.assertIsNone(manifest['model'])
            self.assertEqual(len(manifest['clips']), 3)
            for take in store.get(pid)['script']['takes']:
                self.assertIn(take['speech'], z.read('FLOW_PROMPTS.txt').decode())
            self.assertIn('She opens the envelope.', z.read('FLOW_PROMPTS.txt').decode())

    def test_legacy_reference_prompt_shape_can_be_reviewed(self):
        pid, jobs = self.ready_for_export()
        state = q.load()
        target = next(j for j in state['jobs'] if j['id'] == jobs[1]['id'])
        payload = json.loads(target['prompt'])
        prop = payload['prop_description'][0]
        payload['prop_description'] = [{
            'scene': prop['design'], 'realism': prop['material'], 'reference_use': 'legacy'}]
        target['prompt'] = json.dumps(payload, ensure_ascii=False, indent=2)
        q.save(state)
        self.assertEqual(q.review(jobs[1]['id'], 'approve')['jobs'][1]['review_status'], 'approved')

    def test_changed_plan_or_anchor_invalidates_approved_export(self):
        pid, jobs = self.ready_for_export()
        for job in jobs: q.review(job['id'], 'approve')
        p = store.get(pid)
        p['plan']['frames'][1]['prompt']['scene'] += ' Changed'
        store.save(p)
        with self.assertRaisesRegex(ValueError, 'plano mudou'): q.export_package(pid)
        p['plan']['frames'][1]['prompt']['scene'] = fixture()[1]['frames'][1]['prompt']['scene']
        store.save(p)
        (store.folder(pid)/'anchor.png').write_bytes(self.image('blue'))
        with self.assertRaisesRegex(ValueError, 'alterada'): q.export_package(pid)

    def test_modified_image_cannot_be_reviewed_or_exported(self):
        pid, jobs = self.ready_for_export()
        for job in jobs: q.review(job['id'], 'approve')
        Path(q.get_job(jobs[0]['id'])['local_file']).write_bytes(self.image('blue'))
        with self.assertRaisesRegex(ValueError, 'alterada'): q.review(jobs[0]['id'], 'approve')
        with self.assertRaisesRegex(ValueError, 'alterada'): q.export_package(pid)

    def test_review_retry_preserves_result_and_does_not_expand_pilot(self):
        pid = self.project()
        q.enqueue([pid], limit=1); q.control(True)
        job = q.claim(); q.update(job['id'], 'submitting'); q.update(job['id'], 'generating')
        done = q.receive(job['id'], self.image())
        q.control(False)
        state = q.review(job['id'], 'retry')
        self.assertEqual(len(state['jobs']), 2)
        self.assertEqual(state['jobs'][0]['status'], 'cancelled')
        self.assertEqual(state['jobs'][1]['retry_of'], job['id'])
        self.assertEqual(state['jobs'][1]['frame'], 'K01')
        self.assertEqual(Path(done['local_file']).read_bytes(), self.image())
        self.assertFalse(state['running'])

    def test_review_and_export_routes_require_local_authorization(self):
        pid, jobs = self.ready_for_export()
        route = f"/api/browser/jobs/{jobs[0]['id']}/review"
        self.assertEqual(self.client.post(route,json={'decision':'approve'}).status_code,403)
        self.assertEqual(self.client.get(f"/api/browser/jobs/{jobs[0]['id']}/result").status_code,200)
        for job in jobs:
            response = self.client.post(f"/api/browser/jobs/{job['id']}/review",
                json={'decision':'approve'},headers=self.headers)
            self.assertEqual(response.status_code,200,response.text)
        path = f'/api/browser/projects/{pid}/export'
        self.assertEqual(self.client.post(path).status_code,403)
        response = self.client.post(path, headers=self.headers)
        self.assertEqual(response.status_code,200,response.text[:100] if response.status_code != 200 else '')
        self.assertEqual(response.headers['content-type'], 'application/zip')
        self.assertTrue(zipfile.is_zipfile(io.BytesIO(response.content)))


if __name__=='__main__':unittest.main()
