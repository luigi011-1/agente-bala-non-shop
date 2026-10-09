"""Navegador real: metadados JS, robots e bloqueios, sem acessar redes sociais."""
import asyncio
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
from pathlib import Path
import threading
import unittest

from operacao.coleta_browser import crawl_browser


@unittest.skipUnless(importlib.util.find_spec('playwright') and Path('/Applications/Google Chrome.app').exists(), 'Chrome/Playwright opcional ausente')
class BrowserCollection(unittest.TestCase):
    def test_javascript_robots_and_login_are_observed(self):
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/robots.txt':
                    body = 'User-agent: *\nDisallow: /reel/denied/\n'
                elif self.path == '/reel/js/':
                    video = {'@type': 'VideoObject', 'url': base + '/reel/js/', 'uploadDate': '2026-10-06T12:00:00Z',
                             'interactionStatistic': {'interactionType': 'https://schema.org/WatchAction', 'userInteractionCount': 910000}}
                    body = '<html><title>Health</title><script>let s=document.createElement("script");s.type="application/ld+json";s.textContent=' + json.dumps(json.dumps(video)) + ';document.head.appendChild(s)</script></html>'
                else:
                    body = '<html><title>Log in to Instagram</title>Log in to continue</html>'
                self.send_response(200)
                self.end_headers()
                self.wfile.write(body.encode())
            def log_message(self, *args):
                pass
        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        base = f'http://127.0.0.1:{server.server_port}'
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        pages, errors, limited, scheduled = asyncio.run(crawl_browser(
            [base + '/reel/js/', base + '/reel/login/', base + '/reel/denied/'],
            max_pages=3, max_seconds=30, concurrency=1, allow_local_fixtures=True))
        self.assertEqual(pages[base + '/reel/js/']['evidence']['views'][0]['value'], 910000)
        self.assertTrue(pages[base + '/reel/js/']['rendered_with_browser'])
        self.assertTrue(pages[base + '/reel/login/']['blocked'])
        self.assertNotIn(base + '/reel/denied/', pages)
        self.assertTrue(any(e['reason'] == 'LOGIN_OR_CHALLENGE' for e in errors))
        self.assertTrue(any(e['reason'] == 'NOT_FETCHED_OR_ROBOTS_DENIED' for e in errors))

    def test_refuses_personal_profile_and_outside_domains_before_network(self):
        with self.assertRaises(ValueError):
            asyncio.run(crawl_browser(['https://example.com/'], max_pages=1, max_seconds=2, concurrency=1))
        with self.assertRaises(ValueError):
            asyncio.run(crawl_browser(['https://www.instagram.com/reel/x/'], max_pages=1, max_seconds=2, concurrency=1,
                                     browser_profile='/tmp/personal-profile'))
