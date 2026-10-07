"""Conservative filters and a real Crawlee HTTP run against local fixtures."""
import argparse
import asyncio
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
from pathlib import Path
import tempfile
import threading
import time
import unittest

from operacao.mineracao import (
    classify_video, crawl_pages, extract_page, load_seeds, main, mine,
    normalize_url, render_report,
)

HAS_BS4 = importlib.util.find_spec("bs4") is not None
HAS_CRAWLEE = importlib.util.find_spec("crawlee") is not None and importlib.util.find_spec("httpx2") is not None


def jsonld(value):
    return '<html><title>Public health video</title><script type="application/ld+json">' + json.dumps(value) + "</script></html>"


class Scope(unittest.TestCase):
    def test_domain_is_exact_and_credentials_and_insecure_urls_rejected(self):
        for url in (
            "https://instagram.com.evil.example/reel/a/", "https://notinstagram.com/reel/a/",
            "https://facebook.com@evil.example/watch/?v=1", "http://www.instagram.com/reel/a/",
            "https://user:password@www.instagram.com/reel/a/", "https://www.instagram.com:444/reel/a/",
            "http://127.0.0.1:1234/reel/a/", "https://l.facebook.com/l.php?u=https://evil.example",
        ):
            with self.subTest(url=url), self.assertRaises(ValueError):
                normalize_url(url)

    def test_tracking_removed_without_losing_facebook_video(self):
        self.assertEqual(normalize_url("https://m.facebook.com/watch?v=123&utm_campaign=ignored"), "https://www.facebook.com/watch/?v=123")
        self.assertEqual(normalize_url("https://instagram.com/reel/ABC/?igsh=tracking#fragment"), "https://www.instagram.com/reel/ABC/")

    def test_fixture_requires_explicit_flag_and_is_loopback_only(self):
        self.assertEqual(normalize_url("http://127.0.0.1:1234/reel/a/", allow_local_fixtures=True), "http://127.0.0.1:1234/reel/a/")
        with self.assertRaises(ValueError):
            normalize_url("http://192.168.1.2/reel/a/", allow_local_fixtures=True)

    def test_audit_requires_coverage_and_angle_not_an_ai_bio_guess(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "seeds.json"
            audit = {"subject_url": "https://www.instagram.com/profile/", "source_url": "https://www.instagram.com/profile/",
                     "observed_at": datetime.now(timezone.utc).isoformat(), "field": "profile_ai_only", "value": True,
                     "method": "visual_audit", "scope": "bio_only", "verified": True, "note": "bio says AI"}
            path.write_text(json.dumps({"urls": ["https://www.instagram.com/reel/a/"], "observations": [audit]}))
            with self.assertRaisesRegex(ValueError, "auditoria"):
                load_seeds(path)
            audit.update(field="niche_match", method="content_audit", scope="profile_content")
            path.write_text(json.dumps({"urls": ["https://www.instagram.com/reel/a/"], "observations": [audit]}))
            with self.assertRaisesRegex(ValueError, "angle"):
                load_seeds(path)


@unittest.skipUnless(HAS_BS4, "Runtime opcional de mineração não instalado")
class EvidenceFilters(unittest.TestCase):
    def setUp(self):
        self.now = datetime.now(timezone.utc)
        self.url = "https://www.instagram.com/reel/ABC/"
        self.profile = "https://www.instagram.com/healthcreator/"
        self.filters = {"timezone": "UTC", "today": self.now.date().isoformat(), "lookback_days": 2, "min_views": 800000, "max_profile_age_days": 30}

    def video(self, views=900000, posted_at=None):
        return extract_page(jsonld({"@type": "VideoObject", "url": self.url, "uploadDate": posted_at or self.now.isoformat(),
                                    "interactionStatistic": {"interactionType": "https://schema.org/WatchAction", "userInteractionCount": views},
                                    "author": {"@type": "Person", "url": self.profile}}), self.url, self.now.isoformat())

    def test_every_criterion_requires_evidence_instead_of_inference(self):
        video = self.video()
        result = classify_video(video, {}, [], self.filters, self.now)
        self.assertEqual(result["status"], "candidate")
        self.assertEqual(result["criteria"]["views"]["status"], "confirmed")
        self.assertIn("profile_created_at", result["missing"])
        self.assertIn("profile_country", result["missing"])
        self.assertIn("profile_ai_only", result["missing"])

    def test_strict_more_than_800k_old_dates_and_rounded_counts(self):
        self.assertEqual(classify_video(self.video(800000), {}, [], self.filters, self.now)["status"], "rejected")
        self.assertEqual(classify_video(self.video(posted_at=(self.now - timedelta(days=3)).isoformat()), {}, [], self.filters, self.now)["status"], "rejected")
        self.assertEqual(classify_video(self.video("900K"), {}, [], self.filters, self.now)["criteria"]["views"]["status"], "unknown")
        self.assertEqual(classify_video(self.video(posted_at=self.now.date().isoformat()), {}, [], self.filters, self.now)["criteria"]["posted_at"]["status"], "unknown")

    def test_post_date_never_becomes_profile_creation(self):
        page = extract_page(jsonld({"@type": "Person", "url": self.profile, "datePublished": self.now.isoformat(),
                                    "foundingDate": self.now.isoformat(), "description": "US health AI avatar"}), self.profile, self.now.isoformat())
        self.assertNotIn("profile_created_at", page["evidence"])
        self.assertNotIn("profile_country", page["evidence"])
        self.assertNotIn("profile_ai_only", page["evidence"])

    def test_unrelated_recommended_video_does_not_supply_views(self):
        html = jsonld({"@type": "VideoObject", "url": "https://www.instagram.com/reel/OTHER/", "uploadDate": self.now.isoformat(),
                       "interactionStatistic": {"interactionType": "WatchAction", "userInteractionCount": 9999999}})
        page = extract_page(html, self.url, self.now.isoformat())
        self.assertFalse(page["evidence"])

    def test_unidentified_itemlist_recommendation_never_supplies_current_metrics(self):
        html = jsonld({"@type": "ItemList", "itemListElement": [{"@type": "VideoObject", "uploadDate": self.now.isoformat(),
                      "interactionStatistic": {"interactionType": "WatchAction", "userInteractionCount": 9999999},
                      "author": {"url": "https://www.instagram.com/someoneelse/"}}]})
        html = html.replace("<html>", '<html><meta property="og:url" content="' + self.url + '">')
        page = extract_page(html, self.url, self.now.isoformat())
        self.assertFalse(page["evidence"])
        self.assertIsNone(page["profile_url"])

    def test_identityless_root_video_requires_matching_canonical_url(self):
        obj = {"@type": "VideoObject", "uploadDate": self.now.isoformat(),
               "interactionStatistic": {"interactionType": "WatchAction", "userInteractionCount": 900001}}
        page = extract_page(jsonld(obj), self.url, self.now.isoformat())
        self.assertFalse(page["evidence"])
        html = jsonld(obj).replace("<html>", '<html><meta property="og:url" content="' + self.url + '">')
        page = extract_page(html, self.url, self.now.isoformat())
        self.assertEqual(page["evidence"]["views"][0]["value"], 900001)

    def test_instagram_photo_route_alone_never_proves_video(self):
        photo = {"url": "https://www.instagram.com/p/PHOTO/", "evidence": {}}
        result = classify_video(photo, {}, [], self.filters, self.now)
        self.assertEqual(result["criteria"]["media_type"]["status"], "unknown")

    def test_conflicting_evidence_cannot_approve(self):
        video = self.video()
        video["evidence"]["views"].append(dict(video["evidence"]["views"][0], value=700000))
        result = classify_video(video, {}, [], self.filters, self.now)
        self.assertEqual(result["criteria"]["views"]["status"], "conflict")
        self.assertEqual(result["status"], "candidate")


@unittest.skipUnless(HAS_CRAWLEE, "Crawlee[beautifulsoup,httpx] não instalado")
class RealCrawler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hits = []
        cls.now = datetime.now(timezone.utc)
        parent = cls

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                parent.hits.append(self.path)
                if self.path == "/redirect/":
                    self.send_response(302)
                    self.send_header("Location", "https://example.com/never-fetch")
                    self.end_headers()
                    return
                if self.path == "/reel/slow/":
                    time.sleep(2)
                if self.path == "/robots.txt":
                    content = "User-agent: *\nAllow: /\nDisallow: /reel/denied/\n"
                elif self.path == "/reel/good/":
                    content = jsonld({"@type": "VideoObject", "url": parent.base + self.path, "uploadDate": parent.now.isoformat(),
                                      "interactionStatistic": {"interactionType": "WatchAction", "userInteractionCount": 900001},
                                      "author": {"@type": "Person", "url": parent.base + "/profile/"}})
                elif self.path == "/profile/":
                    content = jsonld({"@type": "SocialMediaAccount", "url": parent.base + "/profile/",
                                      "dateCreated": (parent.now - timedelta(days=10)).isoformat(), "location": {"addressCountry": "US"}})
                elif self.path == "/reel/login/":
                    content = '<html><title>Log in to Instagram</title><form action="/login"><input type="password"></form></html>'
                elif self.path == "/farm/":
                    content = "<html><title>Public profile</title>" + "".join(f'<a href="/reel/{index}/">Video</a>' for index in range(10)) + "</html>"
                else:
                    content = "<html><title>Public metadata unavailable</title><p>English wellness content</p></html>"
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                try:
                    self.wfile.write(content.encode())
                except BrokenPipeError:
                    pass

            def log_message(self, *args):
                pass

        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.base = "http://127.0.0.1:" + str(cls.server.server_port)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def options(self, directory, urls, observations=None):
        seeds = Path(directory) / "seeds.json"
        seeds.write_text(json.dumps({"urls": urls, "observations": observations or []}))
        return argparse.Namespace(angle="sea-moss", seeds=seeds, out=Path(directory) / "out", timezone="UTC", today=None,
                                  min_views=None, lookback_days=None, max_profile_age_days=None, max_pages=4,
                                  max_seconds=15, concurrency=1, allow_local_fixtures=True)

    def audits(self):
        common = {"subject_url": self.base + "/profile/", "source_url": self.base + "/profile/", "observed_at": self.now.isoformat(), "value": True, "verified": True}
        return [common | {"field": "profile_ai_only", "method": "visual_audit", "scope": "all_public_posts", "note": "Fixture: os três posts públicos têm avatar IA, auditados visualmente."},
                common | {"field": "niche_match", "method": "content_audit", "scope": "profile_content", "angle": "sea-moss", "note": "Fixture: conteúdo de saúde e sea moss; nenhum ângulo misturado."}]

    def test_complete_verified_fixture_real_crawlee_and_report_schema(self):
        with tempfile.TemporaryDirectory() as directory:
            args = self.options(directory, [self.base + "/reel/good/"], self.audits())
            result = asyncio.run(mine(args))
            self.assertEqual(result["status"], "COMPLETE", result)
            self.assertEqual(len(result["approved"]), 1)
            self.assertEqual(result["counts"]["pages"], 2)
            self.assertTrue(result["test_fixture_mode"])
            self.assertIn(self.base + "/reel/good/", render_report(result))
            self.assertIn("visual_audit", render_report(result))
            try:
                from jsonschema import Draft202012Validator
            except ImportError:
                return
            schema = json.loads(Path("operacao/schema_mineracao.json").read_text())
            Draft202012Validator({"$ref": "#/$defs/result", "$defs": schema["$defs"]}).validate(result)

    def test_ai_policy_missing_keeps_candidate_even_with_country_date_views(self):
        with tempfile.TemporaryDirectory() as directory:
            result = asyncio.run(mine(self.options(directory, [self.base + "/reel/good/"])))
            self.assertEqual(result["status"], "PARTIAL")
            self.assertFalse(result["approved"])
            self.assertEqual(result["candidates"][0]["missing"], ["profile_ai_only", "niche_match"])

    def test_login_and_robots_disallow_do_not_become_empty_success(self):
        for path in ("/reel/login/", "/reel/denied/"):
            with self.subTest(path=path), tempfile.TemporaryDirectory() as directory:
                result = asyncio.run(mine(self.options(directory, [self.base + path])))
                self.assertEqual(result["status"], "BLOCKED", result)
                self.assertTrue(result["errors"])
                self.assertFalse(result["approved"])

    def test_page_limit_bounds_discovered_links(self):
        pages, errors, limits, scheduled = asyncio.run(crawl_pages([self.base + "/farm/"], max_pages=3, max_seconds=15, concurrency=2, allow_local_fixtures=True))
        self.assertLessEqual(len(pages), 3)
        self.assertEqual(len(scheduled), 3)
        self.assertTrue(limits)

    def test_cross_domain_redirect_is_blocked_before_external_request(self):
        pages, errors, limits, scheduled = asyncio.run(crawl_pages([self.base + "/redirect/"], max_pages=2, max_seconds=15, concurrency=1, allow_local_fixtures=True))
        self.assertFalse(pages)
        self.assertTrue(any("instagram.com" in error.get("detail", "") for error in errors), errors)

    def test_timeout_is_reported(self):
        pages, errors, limits, scheduled = asyncio.run(crawl_pages([self.base + "/reel/slow/"], max_pages=2, max_seconds=0.3, concurrency=1, allow_local_fixtures=True))
        self.assertTrue(limits)
        self.assertTrue(any(error["reason"] == "TIME_LIMIT" or "Timeout" in error["reason"] for error in errors), errors)

    def test_cli_partial_exit_and_saved_proofs(self):
        with tempfile.TemporaryDirectory() as directory:
            args = self.options(directory, [self.base + "/reel/login/"])
            exit_code = main(["--angle", "auraly", "--seeds", str(args.seeds), "--out", str(args.out), "--allow-local-fixtures", "--max-seconds", "15"])
            self.assertEqual(exit_code, 2)
            self.assertTrue((args.out / "resultados.json").exists())
            self.assertTrue((args.out / "relatorio.md").exists())


if __name__ == "__main__":
    unittest.main()
