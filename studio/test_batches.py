import base64
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, Mock
import httpx
from PIL import Image
from . import batches, provider as ai, storage as store
from .test_studio import fixture


def seed_ui_demo(data_dir):
    """Synthetic browser fixture, restricted to our isolated temporary QA directory."""
    path = Path(data_dir).resolve()
    if not path.name.startswith('auraly-qa-') or path.parent != Path(tempfile.gettempdir()).resolve():
        raise ValueError('Only isolated QA directory allowed.')
    with patch.object(store, 'DATA', path):
        p = store.create('TESTE ISOLADO · referência fictícia', 'Avatar de teste', '')
        folder = store.folder(p['id'])
        Image.new('RGB', (90,160), 'gray').save(folder/'anchor.png')
        analysis = {'summary':'Dados sintéticos para testar a interface; não é análise real.', 'hero':'Carta de teste',
            'hero_evidence':[0.2], 'beats':[{'start':0,'end':3,'label':'HOOK','visual':'Carta','change':'Abre','props':'Carta'}],
            'ambiguity':False, 'continuity':'Teste', 'source_reuse':'Teste'}
        store.write_json(folder/'ANALISE.json',analysis)
        (folder/'source.mp4').touch()
        (folder/'sources.md').write_text('Synthetic QA only')
        store.change(p['id'],analysis=analysis,transcript=[],status='analysis_approved',duration=3)
        return p['id']


class BatchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.data = patch.object(store, 'DATA', Path(self.temp.name))
        self.data.start()
        ai.configure('FAKE', kie_key='', gemini_key='', text_provider='auto')
        self.source = store.create('Source', 'Original', '')['id']
        folder = store.folder(self.source)
        for name in ('source.mp4', 'sources.md', 'ANALISE.json'):
            (folder/name).write_text('{}')
        anchor = folder/'anchor.png'
        Image.new('RGB',(30,50),'red').save(anchor)
        self.registry = {'a':('A',anchor),'b':('B',anchor)}
        store.change(self.source, status='analysis_approved', analysis={'hero':'Card'}, transcript=[])

    def tearDown(self):
        ai.configure('', kie_key='', gemini_key='', text_provider='auto')
        self.data.stop()
        self.temp.cleanup()

    def test_batch_reuses_analysis_not_script_and_is_idempotent(self):
        ids = batches.create(self.source, ['a','b'], self.registry, 3, 'id')
        self.assertEqual(ids, batches.create(self.source,['a','b'],self.registry,3,'id'))
        self.assertEqual(len(store.all_projects()),3)
        for pid in ids:
            p=store.get(pid)
            self.assertEqual(p['analysis'],{'hero':'Card'})
            self.assertNotIn('script',p)
            self.assertEqual(p['calls'],[])
            self.assertTrue((store.folder(pid)/'anchor.png').is_file())
        self.assertNotEqual(store.get(ids[0])['avatar'],store.get(ids[1])['avatar'])

    def test_batch_requires_approved_analysis(self):
        store.change(self.source,status='analysis_ready')
        with self.assertRaises(ValueError):
            batches.create(self.source,['a'],self.registry,1,'id')

    def test_enqueue_does_not_duplicate_busy_jobs(self):
        ids=batches.create(self.source,['a'],self.registry,1,'id')
        pool=Mock()
        batches.enqueue(ids,pool)
        batches.enqueue(ids,pool)
        self.assertEqual(pool.submit.call_count,1)

    def test_prepare_stops_before_approval(self):
        pid=batches.create(self.source,['a'],self.registry,1,'id')[0]
        with patch.object(batches.engine,'script',side_effect=lambda p: store.change(p,status='script_ready',script=fixture()[0])), patch.object(batches.engine,'hooks') as hooks:
            batches.advance(pid)
            hooks.assert_not_called()
        self.assertEqual(store.get(pid)['status'],'script_ready')

    def test_authorized_pipeline_and_no_repeat_when_complete(self):
        pid=batches.create(self.source,['a'],self.registry,1,'id')[0]
        store.change(pid,status='script_ready',script=fixture()[0])
        with patch.object(batches.engine,'hooks',side_effect=lambda p:store.change(p,status='hooks_ready',hooks=[{'id':'H1'}])), patch.object(batches.engine,'plan',side_effect=lambda p:store.change(p,status='plan_ready')), patch.object(batches.engine,'generate',side_effect=lambda p:store.change(p,status='complete')) as generate:
            batches.advance(pid,True)
            batches.advance(pid,True)
            self.assertEqual(generate.call_count,1)
        self.assertEqual(store.get(pid)['selected'],['H1'])

    def test_sticky_fallback_skips_openai_on_next_chunk(self):
        ai.configure(gemini_key='FAKE')
        with patch.object(ai,'_openai_think',side_effect=ai.ProviderError('quota',429)) as openai, patch.object(ai,'_gemini_think',return_value={}):
            ai.think(self.source,'',{})
            ai.think(self.source,'',{})
            self.assertEqual(openai.call_count,1)

    def test_retry_pause_and_budget_stop_new_request(self):
        ai.configure('',gemini_key='FAKE')
        with patch.object(ai,'_gemini_think',side_effect=ai.ProviderError('busy',503)) as call, patch.object(ai,'retry_wait',side_effect=lambda *args:store.change(self.source,pause_requested=True)):
            with self.assertRaises(ValueError):ai.think(self.source,'',{})
            self.assertEqual(call.call_count,1)

    def test_kie_text_payload_and_json_response(self):
        ai.configure('',kie_key='FAKE',text_provider='kie')
        response=httpx.Response(200,json={'choices':[{'finish_reason':'stop','message':{'content':'{"ok":true}'}}]})
        with patch.object(ai.httpx,'Client') as factory:
            client=factory.return_value.__enter__.return_value
            client.post.return_value=response
            self.assertTrue(ai.think(self.source,'JSON',{},[store.folder(self.source)/'anchor.png'])['ok'])
            kwargs=client.post.call_args.kwargs
            self.assertEqual(kwargs['json']['model'],'gemini-3-5-flash-thinking')
            url=kwargs['json']['messages'][1]['content'][-1]['image_url']['url']
            self.assertTrue(url.startswith('data:image/jpeg;base64,'))
            self.assertLessEqual(len(url),ai.KIE_INLINE_BUDGET)
        self.assertEqual(store.get(self.source)['calls'][0]['route'],'kie/text')

    def test_kie_compression_keeps_native_resolution(self):
        source=store.folder(self.source)/'anchor.png'
        with Image.open(source) as im:size=im.size
        raw=base64.b64decode(ai._compress_for_kie(source).split(',',1)[1])
        with Image.open(io.BytesIO(raw)) as out:
            self.assertEqual(out.size,size)
            self.assertEqual(out.format,'JPEG')
