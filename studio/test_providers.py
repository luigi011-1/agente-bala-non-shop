import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import httpx
from . import provider as ai, storage as store, credentials


class ProviderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.data = patch.object(store, 'DATA', Path(self.temp.name))
        self.data.start()
        ai.configure('', gemini_key='', text_provider='auto')
        self.pid = store.create('Test', '')['id']

    def tearDown(self):
        ai.configure('', gemini_key='')
        self.data.stop()
        self.temp.cleanup()

    def test_dpapi_roundtrip_and_legacy_migration(self):
        values = {'openai_key': 'FAKE_OPENAI', 'gemini_key': 'FAKE_GOOGLE'}
        store.write_json(store.DATA / 'preferences.json', values)
        ai.load_preferences()
        saved = (store.DATA / 'preferences.json').read_text()
        for value in values.values():
            self.assertNotIn(value, saved)
        self.assertEqual(json.loads(credentials.unprotect(json.loads(saved)['protected_credentials'])), values)
        ai.configure('', gemini_key='')
        ai.save_preferences()
        ai.load_preferences()
        self.assertFalse(ai.settings()['configured'])
        self.assertFalse(ai.settings()['gemini_configured'])

    def test_text_call_limit_counts_every_route(self):
        with self.assertRaises(ValueError):
            ai.check_call_allowed({'calls': [{'route': 'responses'}], 'call_limits': {'text': 1}})

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

    def test_invalid_text_provider_rejected(self):
        with self.assertRaises(ValueError):
            ai.configure(text_provider='kie')


if __name__ == '__main__':
    unittest.main()
