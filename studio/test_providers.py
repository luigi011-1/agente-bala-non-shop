import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import httpx
from PIL import Image
from . import provider as ai, storage as store, credentials


class ProviderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.data = patch.object(store, 'DATA', Path(self.temp.name))
        self.data.start()
        ai.configure('', kie_key='', gemini_key='', allow_temp_upload=False, text_provider='auto')
        self.pid = store.create('Test', 'Shelby', '')['id']

    def tearDown(self):
        ai.configure('', kie_key='', gemini_key='', allow_temp_upload=False)
        self.data.stop()
        self.temp.cleanup()

    def test_dpapi_roundtrip_and_legacy_migration(self):
        values = {'openai_key': 'FAKE_OPENAI', 'kie_key': 'FAKE_KIE', 'gemini_key': 'FAKE_GOOGLE'}
        store.write_json(store.DATA / 'preferences.json', values)
        ai.load_preferences()
        saved = (store.DATA / 'preferences.json').read_text()
        for value in values.values():
            self.assertNotIn(value, saved)
        self.assertEqual(json.loads(credentials.unprotect(json.loads(saved)['protected_credentials'])), values)
        ai.configure('', kie_key='', gemini_key='')
        ai.save_preferences()
        ai.load_preferences()
        self.assertFalse(ai.settings()['configured'])
        self.assertFalse(ai.settings()['kie_configured'])
        self.assertFalse(ai.settings()['gemini_configured'])

    def test_kie_counts_as_image(self):
        with self.assertRaises(ValueError):
            ai.check_call_allowed({'calls': [{'route': 'kie/images'}], 'call_limits': {'image': 1}}, 'images/edits')

    def test_gemini_only_routes_without_openai(self):
        ai.configure(gemini_key='FAKE')
        with patch.object(ai, '_gemini_think', return_value={}) as gemini, patch.object(ai, '_openai_think') as openai:
            ai.think(self.pid, '', {})
            gemini.assert_called_once()
            openai.assert_not_called()

    def test_fallback_only_on_typed_429(self):
        ai.configure('FAKE', gemini_key='FAKE')
        with patch.object(ai, '_gemini_think', return_value={}) as fallback:
            for error in [ValueError('429 text'), ai.ProviderError('missing model', 404)]:
                with patch.object(ai, '_openai_think', side_effect=error), self.assertRaises(ValueError):
                    ai.think(self.pid, '', {})
            fallback.assert_not_called()
            with patch.object(ai, '_openai_think', side_effect=ai.ProviderError('rate limit', 429)):
                ai.think(self.pid, '', {})
            fallback.assert_called_once()

    def test_upload_requires_consent_and_unpaused_project(self):
        ai.configure(kie_key='FAKE')
        with patch.object(ai, '_upload_temp') as upload:
            with self.assertRaises(ValueError):
                ai._kie_image(self.pid, '', [Path('anchor.png')], store.folder(self.pid) / 'x.png')
            ai.configure(allow_temp_upload=True)
            store.change(self.pid, pause_requested=True)
            with self.assertRaises(ValueError):
                ai._kie_image(self.pid, '', [Path('anchor.png')], store.folder(self.pid) / 'x.png')
            upload.assert_not_called()

    def test_gemini_503_retries_are_counted(self):
        ai.configure(gemini_key='FAKE')
        with patch.object(ai.httpx, 'Client') as factory, patch.object(ai, 'retry_wait'):
            client = factory.return_value.__enter__.return_value
            client.post.return_value = httpx.Response(503, json={'error': {'message': 'busy'}})
            with self.assertRaises(ValueError):
                ai.think(self.pid, '', {})
            self.assertEqual(client.post.call_count, 3)
        self.assertEqual(len(store.get(self.pid)['calls']), 3)
        self.assertEqual(store.get(self.pid)['calls'][0]['status'], 'failed')

    def test_kie_task_persisted_before_poll_and_recovered_without_post(self):
        ai.configure(kie_key='FAKE')
        destination = store.folder(self.pid) / 'image.png'
        with patch.object(ai.httpx, 'Client') as factory, patch.object(ai.time, 'sleep'):
            client = factory.return_value.__enter__.return_value
            client.post.return_value = httpx.Response(200, json={'code': 200, 'data': {'taskId': 'task-test'}})
            def interrupt(*args, **kwargs):
                self.assertEqual(store.get(self.pid)['calls'][0]['task_id'], 'task-test')
                raise httpx.ReadTimeout('interrupted')
            client.get.side_effect = interrupt
            with self.assertRaises(ValueError):
                ai.image(self.pid, 'prompt', [], destination)
            self.assertEqual(client.post.call_count, 1)
        output = io.BytesIO()
        Image.new('RGB', (20, 30)).save(output, format='PNG')
        store.change(self.pid, call_limits={'image': 1})
        with patch.object(ai.httpx, 'Client') as factory, patch.object(ai.time, 'sleep'):
            client = factory.return_value.__enter__.return_value
            client.get.side_effect = [httpx.Response(200, json={'data': {'state': 'success',
                'resultJson': json.dumps({'resultUrls': ['https://example.test/result.png']})}}),
                httpx.Response(200, content=output.getvalue())]
            self.assertTrue(ai.recover_image(self.pid, 'image.png'))
            client.post.assert_not_called()
        self.assertTrue(destination.is_file())
        self.assertEqual(len(store.get(self.pid)['calls']), 1)
