"""Niche-first requests, weekly boundaries, content language and scoped ranking."""
import argparse
import asyncio
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import AsyncMock, patch

from operacao.mineracao import classify_video, evidence, load_seeds, mine, rank_videos
from operacao.nichos import mining_defaults, resolve_niche


class NicheCatalog(unittest.TestCase):
    def test_aliases_and_legacy_are_editorial_not_product(self):
        for alias in ('saúde e beleza', 'health and beauty', 'saude-beleza'):
            self.assertEqual(resolve_niche(alias)['slug'], 'saude-beleza')
        self.assertEqual(resolve_niche('manifestação/tarot')['slug'], 'manifestacao-tarot')
        self.assertEqual(resolve_niche(angle='sea-moss'), resolve_niche(angle='fitwell'))
        for angle in ('sea-moss', 'fitwell', 'auraly', 'body-hacks'):
            terms = ' '.join(resolve_niche(angle=angle)['search_terms_en']).lower()
            self.assertNotIn('sea moss', terms)
            self.assertNotIn('fitwell', terms)
            self.assertNotIn('auraly', terms)
        self.assertEqual(resolve_niche('manifestação/tarot', angle='sea-moss')['slug'], 'manifestacao-tarot')

    def test_custom_niche_and_defaults(self):
        custom = resolve_niche('Pets e treinamento de cães')
        self.assertTrue(custom['custom'])
        self.assertEqual(custom['search_terms_en'], [])
        self.assertEqual(mining_defaults()['lookback_days'], 7)
        self.assertEqual(mining_defaults()['language'], 'en')
        with self.assertRaises(ValueError):
            resolve_niche('')


class WeeklyAndLanguage(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 10, 7, 20, tzinfo=timezone.utc)
        self.url = 'https://www.instagram.com/reel/week/'
        self.filters = mining_defaults() | {'today': '2026-10-07'}

    def video(self, posted, language=None, country='US', views=900001):
        proof = {}
        for field, value in {'posted_at': posted, 'views': views, 'profile_country': country,
                             'profile_created_at': '2026-09-20T12:00:00Z', 'profile_ai_only': True, 'niche_match': True}.items():
            proof[field] = [evidence(value, self.url, self.now.isoformat(), 'fixture')]
        # Production never infers language from country or title. In fixtures
        # explicit evidence represents an inspected video, not profile metadata.
        if language:
            proof['language'] = [evidence(language, self.url, self.now.isoformat(), 'content_audit')]
        return {'url': self.url, 'title': 'English title', 'evidence': proof}

    def result(self, posted, **kwargs):
        return classify_video(self.video(posted, **kwargs), {}, [], self.filters, self.now)

    def test_seven_calendar_dates_in_new_york_including_today(self):
        self.assertEqual(self.result('2026-10-01T04:00:00Z', language='en')['status'], 'approved')
        self.assertEqual(self.result('2026-10-01T03:59:59Z', language='en')['criteria']['posted_at']['status'], 'rejected')
        self.assertEqual(self.result('2026-10-07T20:00:01Z', language='en')['criteria']['posted_at']['status'], 'rejected')

    def test_language_unknown_despite_us_profile_and_english_title(self):
        result = self.result('2026-10-07T12:00:00Z')
        self.assertEqual(result['status'], 'candidate')
        self.assertIn('language', result['missing'])
        self.assertEqual(self.result('2026-10-07T12:00:00Z', language='es')['status'], 'rejected')
        self.assertEqual(self.result('2026-10-07T12:00:00Z', language='en-US')['status'], 'approved')

    def test_ranking_confirmed_views_descending_unknown_last(self):
        items = [self.result('2026-10-07T12:00:00Z', views=900001), self.result('2026-10-07T12:00:00Z', views='1M'), self.result('2026-10-07T12:00:00Z', views=3000000)]
        ranked = rank_videos(items)
        self.assertEqual([v['confirmed_views'] for v in ranked], [3000000, 900001, None])

    def test_profile_language_audit_cannot_confirm_every_video(self):
        observation = {'subject_url': 'https://www.instagram.com/creator/', 'source_url': self.url, 'field': 'language', 'value': 'en', 'observed_at': self.now.isoformat(), 'method': 'content_audit', 'scope': 'video_content', 'note': 'One video inspected'}
        video = self.video('2026-10-07T12:00:00Z') | {'profile_url': observation['subject_url']}
        result = classify_video(video, {}, [observation], self.filters, self.now)
        self.assertEqual(result['criteria']['language']['status'], 'unknown')


class RequestEvidence(unittest.TestCase):
    def seeds(self, path, audit):
        path.write_text(json.dumps({'urls': ['https://www.instagram.com/reel/a/'], 'observations': [audit]}))

    def test_niche_audit_alias_normalized_language_requires_video_scope(self):
        base = {'subject_url': 'https://www.instagram.com/creator/', 'source_url': 'https://www.instagram.com/creator/', 'observed_at': '2026-10-07T12:00:00Z', 'verified': True, 'note': 'Actual content inspected'}
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'seeds.json'
            self.seeds(path, base | {'field': 'niche_match', 'value': True, 'method': 'content_audit', 'scope': 'profile_content', 'niche': 'saúde e beleza'})
            _, audits = load_seeds(path)
            self.assertEqual(audits[0]['niche'], 'saude-beleza')
            self.seeds(path, base | {'field': 'language', 'value': 'en', 'method': 'content_audit', 'scope': 'video_content'})
            with self.assertRaisesRegex(ValueError, 'vídeo específico'):
                load_seeds(path)
            self.seeds(path, base | {'subject_url': 'https://www.instagram.com/reel/a/', 'field': 'language', 'value': 'en', 'method': 'asr', 'scope': 'video_content'})
            _, audits = load_seeds(path)
            self.assertEqual(audits[0]['value'], 'en')
            try:
                from jsonschema import Draft202012Validator
            except ImportError:
                return  # Behavioral assertions above still run without optional schema QA.
            defs = json.loads(Path('operacao/schema_mineracao.json').read_text())['$defs']
            Draft202012Validator({'$ref': '#/$defs/seeds', '$defs': defs}).validate(json.loads(path.read_text()))

    def test_mine_niche_without_angle_excludes_other_niche_observations(self):
        now = datetime.now(timezone.utc)
        url = 'https://www.instagram.com/reel/a/'
        video = {'url': url, 'evidence': {'views': [evidence(900001, url, now.isoformat(), 'fixture')]}}
        audit = {'subject_url': url, 'source_url': url, 'observed_at': now.isoformat(), 'verified': True, 'note': 'Health posts inspected', 'field': 'niche_match', 'value': True, 'method': 'content_audit', 'scope': 'profile_content', 'niche': 'saúde e beleza'}
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'seeds.json'
            self.seeds(path, audit)
            args = argparse.Namespace(niche='manifestação/tarot', angle=None, seeds=path, timezone=None, today=None, min_views=None, lookback_days=None, max_profile_age_days=None, max_pages=20, max_seconds=120, concurrency=2, allow_local_fixtures=False)
            with patch('operacao.mineracao.crawl_pages', AsyncMock(return_value=({url: video}, [], False, [url]))):
                result = asyncio.run(mine(args))
            self.assertIsNone(result['angle'])
            self.assertEqual(result['filters']['lookback_days'], 7)
            self.assertEqual(result['niche']['slug'], 'manifestacao-tarot')
            self.assertEqual(result['candidates'][0]['criteria']['niche_match']['status'], 'unknown')
            self.assertEqual(result['ranking_scope'], 'among_collected_videos')
            try:
                from jsonschema import Draft202012Validator
            except ImportError:
                return  # Behavioral assertions above still run without optional schema QA.
            defs = json.loads(Path('operacao/schema_mineracao.json').read_text())['$defs']
            Draft202012Validator({'$ref': '#/$defs/result', '$defs': defs}).validate(result)

    def test_legacy_audit_kept_only_for_compatible_editorial_niche(self):
        now = datetime.now(timezone.utc)
        url = 'https://www.instagram.com/reel/a/'
        video = {'url': url, 'evidence': {'views': [evidence(900001, url, now.isoformat(), 'fixture')]}}
        audit = {'subject_url': url, 'source_url': url, 'observed_at': now.isoformat(), 'verified': True, 'note': 'Health posts inspected', 'field': 'niche_match', 'value': True, 'method': 'content_audit', 'scope': 'profile_content', 'angle': 'sea-moss'}
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'seeds.json'
            self.seeds(path, audit)
            args = argparse.Namespace(niche=None, angle='sea-moss', seeds=path, timezone=None, today=None, min_views=None, lookback_days=None, max_profile_age_days=None, max_pages=20, max_seconds=120, concurrency=2, allow_local_fixtures=False)
            with patch('operacao.mineracao.crawl_pages', AsyncMock(return_value=({url: video}, [], False, [url]))):
                compatible = asyncio.run(mine(args))
                args.niche = 'manifestação/tarot'
                incompatible = asyncio.run(mine(args))
            self.assertEqual(compatible['candidates'][0]['criteria']['niche_match']['status'], 'confirmed')
            self.assertEqual(incompatible['candidates'][0]['criteria']['niche_match']['status'], 'unknown')


if __name__ == '__main__':
    unittest.main()
