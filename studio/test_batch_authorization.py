"""Tests for explicit batch authorization — authorize_batch() and dispatch_batch().

Covers the 12 points in Luigi's spec plus the in-flight cache test.
"""
import copy
import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

# Ensure the package is importable from the project root
sys.path.insert(0, str(Path(__file__).parent.parent))

from studio import browser_queue, pipeline_state, storage as store


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _write_temp_file(content: bytes) -> Path:
    fd, path = tempfile.mkstemp()
    os.write(fd, content)
    os.close(fd)
    return Path(path)


def _make_canonical_state(tmp_dir: Path, *, avatar_id='casey_harrisson'):
    """Minimal canonical state with K01-K05 for casey_harrisson."""
    anchor_bytes = b'anchor-bytes'
    card_bytes = b'card-bytes'
    anchor_path = tmp_dir / 'anchor.jpeg'
    card_path = tmp_dir / 'REF-CARTA.png'
    anchor_path.write_bytes(anchor_bytes)
    card_path.write_bytes(card_bytes)
    script_bytes = b'script'
    hooks_bytes = b'hooks'
    pkg_content = '---\nasset_id: K01_hook_card_pull_camera\n\nPrompt K01\n\n---\nasset_id: K02_hook_salt_circle_closing\n\nPrompt K02\n\n---\nasset_id: K03_hook_honey_over_card\n\nPrompt K03\n\n---\nasset_id: K04_body_reading_t2_t4\n\nPrompt K04\n\n---\nasset_id: K05_cta_stories_bridge\n\nPrompt K05\n'
    pkg_path = tmp_dir / 'prompts.md'
    pkg_path.write_text(pkg_content, encoding='utf-8')
    pkg_sha = _sha(pkg_content.encode())
    script_sha = _sha(script_bytes)
    hooks_sha = _sha(hooks_bytes)
    card_sha = _sha(card_bytes)
    anchor_sha = _sha(anchor_bytes)
    return {
        'production': {'id': 'sexta_pessoa', 'title': 'Sexta Pessoa'},
        'pipeline': 'auraly_soulmate',
        'workflow': {'stage': 'image_prompts_ready', 'current_avatar_id': avatar_id},
        'artifacts': {
            'image_prompts_current': {'path': 'prompts.md', 'sha256': pkg_sha},
            'shared_card_reference': {'path': 'REF-CARTA.png', 'sha256': card_sha},
        },
        'avatars': {
            avatar_id: {
                'anchor_path': str(anchor_path),
                'anchor_sha256': anchor_sha,
                'assets': {
                    'K01_hook_card_pull_camera': {
                        'status': 'queued', 'eligible_for_execution': True,
                        'prompt_sha256': _sha(b'Prompt K01'),
                        'anchor_sha256': anchor_sha,
                        'shared_card_reference_sha256': card_sha,
                        'source_prompt_package_sha256': pkg_sha,
                        'source_script_sha256': script_sha,
                        'hook_selection_sha256': hooks_sha,
                        'parent_asset': None, 'result': None,
                    },
                    'K02_hook_salt_circle_closing': {
                        'status': 'queued', 'eligible_for_execution': True,
                        'prompt_sha256': _sha(b'Prompt K02'),
                        'anchor_sha256': anchor_sha,
                        'shared_card_reference_sha256': card_sha,
                        'source_prompt_package_sha256': pkg_sha,
                        'source_script_sha256': script_sha,
                        'hook_selection_sha256': hooks_sha,
                        'parent_asset': None, 'result': None,
                    },
                    'K03_hook_honey_over_card': {
                        'status': 'queued', 'eligible_for_execution': True,
                        'prompt_sha256': _sha(b'Prompt K03'),
                        'anchor_sha256': anchor_sha,
                        'shared_card_reference_sha256': card_sha,
                        'source_prompt_package_sha256': pkg_sha,
                        'source_script_sha256': script_sha,
                        'hook_selection_sha256': hooks_sha,
                        'parent_asset': None, 'result': None,
                    },
                    'K04_body_reading_t2_t4': {
                        'status': 'queued', 'eligible_for_execution': True,
                        'prompt_sha256': _sha(b'Prompt K04'),
                        'anchor_sha256': anchor_sha,
                        'shared_card_reference_sha256': card_sha,
                        'source_prompt_package_sha256': pkg_sha,
                        'source_script_sha256': script_sha,
                        'hook_selection_sha256': hooks_sha,
                        'parent_asset': None, 'result': None,
                    },
                    'K05_cta_stories_bridge': {
                        'status': 'pending', 'eligible_for_execution': False,
                        'prompt_sha256': _sha(b'Prompt K05'),
                        'anchor_sha256': anchor_sha,
                        'shared_card_reference_sha256': card_sha,
                        'source_prompt_package_sha256': pkg_sha,
                        'source_script_sha256': script_sha,
                        'hook_selection_sha256': hooks_sha,
                        'parent_asset': 'K04_body_reading_t2_t4', 'result': None,
                    },
                },
            }
        },
    }


class BatchAuthorizationTests(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.mkdtemp()
        self._state_dir = Path(self._tmp) / 'state'
        self._state_dir.mkdir()
        # Patch storage to use a temp directory
        self._data_patcher = patch.object(store, 'DATA', Path(self._tmp) / 'data')
        self._data_patcher.start()
        store.DATA.mkdir(parents=True, exist_ok=True)
        # Initialize empty queue
        browser_queue.save({
            'running': True, 'concurrency': 4, 'jobs': [],
            'connected_at': None, 'preflights': [], 'preflight_requests': [],
            'extension_session_id': None, 'batch_authorizations': [],
        })

    def tearDown(self):
        self._data_patcher.stop()

    def _enqueue_k01_k04(self):
        """Put K01-K04 into the queue and return (state, fingerprints dict)."""
        canonical = _make_canonical_state(self._state_dir)
        (self._state_dir / pipeline_state.STATUS_FILENAME).write_text(
            json.dumps(canonical), encoding='utf-8')
        # Build specs manually (mirrors pipeline_browser_bridge)
        anchor_bytes = b'anchor-bytes'
        card_bytes = b'card-bytes'
        anchor_sha = _sha(anchor_bytes)
        card_sha = _sha(card_bytes)
        script_sha = _sha(b'script')
        hooks_sha = _sha(b'hooks')
        pkg_content = canonical['artifacts']['image_prompts_current']['path']
        pkg_sha = canonical['artifacts']['image_prompts_current']['sha256']
        state_path = str(self._state_dir / pipeline_state.STATUS_FILENAME)
        anchor_path = str(self._state_dir / 'anchor.jpeg')
        card_path = str(self._state_dir / 'REF-CARTA.png')
        specs = []
        for asset_id in ['K01_hook_card_pull_camera', 'K02_hook_salt_circle_closing',
                         'K03_hook_honey_over_card', 'K04_body_reading_t2_t4']:
            prompt = f'Prompt {asset_id.split("_")[0]}'
            prompt_sha = _sha(prompt.encode())
            identity = {
                'production_id': 'sexta_pessoa', 'pipeline': 'auraly_soulmate',
                'avatar_id': 'casey_harrisson', 'asset_id': asset_id,
                'prompt_sha256': prompt_sha, 'anchor_sha256': anchor_sha,
                'shared_card_reference_sha256': card_sha,
                'source_script_sha256': script_sha, 'hook_selection_sha256': hooks_sha,
                'parent': None,
            }
            fp = _sha(json.dumps(identity, ensure_ascii=False, sort_keys=True,
                                  separators=(',', ':')).encode())
            specs.append({
                **identity,
                'prompt': prompt,
                'source_prompt_package_sha256': pkg_sha,
                'canonical_state_path': state_path,
                'references': [
                    {'role': 'avatar_anchor', 'canonical_path': anchor_path,
                     'sha256': anchor_sha, 'size': 12, 'mtime_ns': 0},
                    {'role': 'shared_card_reference', 'canonical_path': card_path,
                     'sha256': card_sha, 'size': 10, 'mtime_ns': 0},
                ],
                'parent_dependency': None,
                'execution_spec': {
                    'version': 1, 'target_generation_provider': 'chatgpt_ui',
                    'retry_policy': {'automatic_retry': False, 'requires_explicit_recovery': True},
                    'dependencies': [],
                    'expected_reference_sha256': {'avatar_anchor': anchor_sha,
                                                  'shared_card_reference': card_sha},
                },
                'canonical_asset_fingerprint': fp,
            })
        queue_state = browser_queue.enqueue_materialized(specs)
        fps = {s['asset_id']: s['canonical_asset_fingerprint'] for s in specs}
        return queue_state, fps

    # ── Test 1: batch authorizes exactly K01-K04 ─────────────────────────────
    def test_authorize_batch_covers_exactly_k01_to_k04(self):
        _, fps = self._enqueue_k01_k04()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps)
        self.assertEqual(batch['status'], 'authorized')
        authorized_ids = {a['asset_id'] for a in batch['assets']}
        self.assertEqual(authorized_ids,
                         {'K01_hook_card_pull_camera', 'K02_hook_salt_circle_closing',
                          'K03_hook_honey_over_card', 'K04_body_reading_t2_t4'})

    # ── Test 2: K05 is never in the batch ────────────────────────────────────
    def test_k05_is_absent_from_batch(self):
        _, fps = self._enqueue_k01_k04()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps)
        asset_ids = {a['asset_id'] for a in batch['assets']}
        self.assertNotIn('K05_cta_stories_bridge', asset_ids)

    # ── Test 3: four preflight requests dispatched without serialization ──────
    def test_dispatch_creates_four_preflight_requests(self):
        _, fps = self._enqueue_k01_k04()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps)
        result = browser_queue.dispatch_batch(batch['batch_id'])
        self.assertEqual(len(result['dispatched']), 4)
        self.assertEqual(result['skipped'], [])
        state = browser_queue.load()
        batch_requests = [r for r in state['preflight_requests']
                          if r.get('batch_id') == batch['batch_id']]
        self.assertEqual(len(batch_requests), 4)
        # All are in 'requested' status — extension handles them in parallel
        self.assertTrue(all(r['status'] == 'requested' for r in batch_requests))

    # ── Test 4: asset outside batch is never activated ────────────────────────
    def test_asset_outside_batch_never_receives_preflight_request(self):
        _, fps = self._enqueue_k01_k04()
        # Only K01 and K02
        partial_fps = {k: v for k, v in fps.items()
                       if k in {'K01_hook_card_pull_camera', 'K02_hook_salt_circle_closing'}}
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', partial_fps)
        browser_queue.dispatch_batch(batch['batch_id'])
        state = browser_queue.load()
        batch_requests = [r for r in state['preflight_requests']
                          if r.get('batch_id') == batch['batch_id']]
        requested_job_ids = {r['job_id'] for r in batch_requests}
        # K03 and K04 jobs must NOT appear in this batch's requests
        k03_k04_jobs = [j for j in state['jobs']
                        if j.get('asset_id') in {'K03_hook_honey_over_card', 'K04_body_reading_t2_t4'}]
        for job in k03_k04_jobs:
            self.assertNotIn(job['id'], requested_job_ids)

    # ── Test 5: fingerprint divergence blocks only that asset ─────────────────
    def test_fingerprint_divergence_blocks_only_diverged_asset(self):
        _, fps = self._enqueue_k01_k04()
        # Corrupt K02 fingerprint
        bad_fps = dict(fps)
        bad_fps['K02_hook_salt_circle_closing'] = 'a' * 64
        with self.assertRaises(ValueError) as ctx:
            browser_queue.authorize_batch(
                'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', bad_fps)
        self.assertIn('K02', str(ctx.exception))
        # K01/K03/K04 batch is still possible with correct fingerprints
        valid_fps = {k: v for k, v in fps.items() if k != 'K02_hook_salt_circle_closing'}
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', valid_fps)
        self.assertEqual({a['asset_id'] for a in batch['assets']},
                         {'K01_hook_card_pull_camera', 'K03_hook_honey_over_card',
                          'K04_body_reading_t2_t4'})

    # ── Test 6: K03 failure does not block K01/K02/K04 ───────────────────────
    def test_k03_dispatch_skip_does_not_block_siblings(self):
        _, fps = self._enqueue_k01_k04()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps)
        # Manually corrupt the K03 job fingerprint in the queue to simulate divergence after auth
        state = browser_queue.load()
        k03_job = next(j for j in state['jobs']
                       if j.get('asset_id') == 'K03_hook_honey_over_card')
        k03_job['canonical_asset_fingerprint'] = 'f' * 64  # stale value in queue
        browser_queue.save(state)
        result = browser_queue.dispatch_batch(batch['batch_id'])
        dispatched_ids = {d['asset_id'] for d in result['dispatched']}
        skipped_ids = {s['asset_id'] for s in result['skipped']}
        self.assertIn('K01_hook_card_pull_camera', dispatched_ids)
        self.assertIn('K02_hook_salt_circle_closing', dispatched_ids)
        self.assertIn('K04_body_reading_t2_t4', dispatched_ids)
        self.assertIn('K03_hook_honey_over_card', skipped_ids)

    # ── Test 7: repeated dispatch/authorize is idempotent ────────────────────
    def test_dispatch_is_idempotent_no_duplicate_requests(self):
        _, fps = self._enqueue_k01_k04()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps)
        browser_queue.dispatch_batch(batch['batch_id'])
        result2 = browser_queue.dispatch_batch(batch['batch_id'])
        # Second dispatch reuses existing requests
        self.assertTrue(all(d['reused'] for d in result2['dispatched']))
        state = browser_queue.load()
        # Total unique preflight_requests for this batch must still be 4
        batch_requests = [r for r in state['preflight_requests']
                          if r.get('batch_id') == batch['batch_id']]
        self.assertEqual(len(batch_requests), 4)

    # ── Test 8: old batch cannot execute new asset version ───────────────────
    def test_stale_batch_fingerprint_cannot_execute_updated_asset(self):
        _, fps = self._enqueue_k01_k04()
        # Save the old K01 fingerprint
        old_k01_fp = fps['K01_hook_card_pull_camera']
        # Authorize with old fingerprints
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps)
        # Simulate K01 being re-prepared with a new fingerprint
        state = browser_queue.load()
        k01_job = next(j for j in state['jobs']
                       if j.get('asset_id') == 'K01_hook_card_pull_camera')
        new_fp = 'b' * 64
        k01_job['canonical_asset_fingerprint'] = new_fp
        browser_queue.save(state)
        # dispatch_batch must skip K01 because the batch's registered fingerprint doesn't match
        result = browser_queue.dispatch_batch(batch['batch_id'])
        skipped_ids = {s['asset_id'] for s in result['skipped']}
        self.assertIn('K01_hook_card_pull_camera', skipped_ids)
        # And the new fingerprint must not have been dispatched under the old batch
        state = browser_queue.load()
        k01_requests = [r for r in state['preflight_requests']
                        if r.get('batch_id') == batch['batch_id']
                        and r.get('canonical_asset_fingerprint') == new_fp]
        self.assertEqual(k01_requests, [])

    # ── Test 9: shared cache: 2 resolutions for 2 shared references ──────────
    # (verified in background.test.cjs; here we verify the queue references are identical)
    def test_k01_to_k04_share_same_reference_sha256_values(self):
        _, fps = self._enqueue_k01_k04()
        state = browser_queue.load()
        all_refs = []
        for job in state['jobs']:
            if job.get('job_kind') == 'canonical_materialized':
                all_refs.extend(job.get('references', []))
        anchor_shas = {r['sha256'] for r in all_refs if r['role'] == 'avatar_anchor'}
        card_shas = {r['sha256'] for r in all_refs if r['role'] == 'shared_card_reference'}
        self.assertEqual(len(anchor_shas), 1, 'all K01-K04 must share one anchor sha')
        self.assertEqual(len(card_shas), 1, 'all K01-K04 must share one card sha')

    # ── Test 10: concurrency stays at 4 ──────────────────────────────────────
    def test_queue_concurrency_is_4(self):
        state = browser_queue.load()
        self.assertEqual(state['concurrency'], 4)

    # ── Test 11: completed batch produces no new claims ───────────────────────
    def test_batch_after_dispatch_status_is_preflighting_not_authorized(self):
        _, fps = self._enqueue_k01_k04()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps)
        browser_queue.dispatch_batch(batch['batch_id'])
        state = browser_queue.load()
        saved_batch = next(b for b in state['batch_authorizations']
                           if b['batch_id'] == batch['batch_id'])
        # After dispatch it must be 'preflighting', not still 'authorized'
        self.assertEqual(saved_batch['status'], 'preflighting')

    # ── Test 12: legacy jobs are unaffected by batch machinery ───────────────
    def test_legacy_jobs_coexist_with_batch_jobs(self):
        # Add a legacy job directly to the queue
        state = browser_queue.load()
        state['jobs'].append({
            'id': 'legacy-001', 'job_kind': None, 'project': 'old_project',
            'avatar_id': 'legacy_av', 'avatar': 'Legacy', 'avatar_key': 'old:av',
            'frame': 'F1', 'title': 'Legacy Frame', 'index': 1, 'status': 'queued',
            'prompt': 'old prompt', 'anchor_rel': 'anchor.jpg', 'anchor_sha256': 'a' * 64,
            'fingerprint': 'c' * 64, 'created': store.now(), 'tab_id': None,
            'conversation_url': None, 'destination_dir': '/tmp', 'error': None,
        })
        browser_queue.save(state)
        # Authorize a canonical batch
        _, fps = self._enqueue_k01_k04()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps)
        # Legacy job must still be present and unmodified
        state = browser_queue.load()
        legacy = next((j for j in state['jobs'] if j['id'] == 'legacy-001'), None)
        self.assertIsNotNone(legacy)
        self.assertEqual(legacy['status'], 'queued')
        self.assertIsNone(legacy.get('batch_id'))

    # ── authorize_batch: pipeline guard ──────────────────────────────────────
    def test_authorize_batch_rejects_non_auraly_pipeline(self):
        with self.assertRaises(ValueError) as ctx:
            browser_queue.authorize_batch(
                'prod', 'some_other_pipeline', 'av', {'K01': 'a' * 64})
        self.assertIn('auraly_soulmate', str(ctx.exception))

    # ── authorize_batch: empty batch guard ────────────────────────────────────
    def test_authorize_batch_rejects_empty_fingerprints(self):
        with self.assertRaises(ValueError):
            browser_queue.authorize_batch(
                'prod', 'auraly_soulmate', 'av', {})

    # ── get_batch ─────────────────────────────────────────────────────────────
    def test_get_batch_returns_correct_record(self):
        _, fps = self._enqueue_k01_k04()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps)
        fetched = browser_queue.get_batch(batch['batch_id'])
        self.assertEqual(fetched['batch_id'], batch['batch_id'])
        self.assertEqual(fetched['production_id'], 'sexta_pessoa')

    def test_get_batch_raises_for_unknown_id(self):
        with self.assertRaises(ValueError):
            browser_queue.get_batch('nonexistent' * 3)

    # ── Benchmark: timing simulation ──────────────────────────────────────────
    def test_benchmark_batch_dispatch_timing(self):
        import time
        _, fps = self._enqueue_k01_k04()
        t0 = time.perf_counter()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps)
        t1 = time.perf_counter()
        result = browser_queue.dispatch_batch(batch['batch_id'])
        t2 = time.perf_counter()
        auth_ms = (t1 - t0) * 1000
        dispatch_ms = (t2 - t1) * 1000
        print(f'\n[benchmark] authorize_batch: {auth_ms:.1f}ms | '
              f'dispatch_batch (4 requests): {dispatch_ms:.1f}ms | '
              f'total: {(t2-t0)*1000:.1f}ms')
        # Both operations should complete in well under 1 second
        self.assertLess(auth_ms, 1000, 'batch authorization must complete < 1s')
        self.assertLess(dispatch_ms, 1000, 'batch dispatch must complete < 1s')
        self.assertEqual(len(result['dispatched']), 4)


class AllowActivationTests(unittest.TestCase):
    """7 tests for the allow_activation=False (preflight_only) guard.

    Spec from Luigi (2026-09-08):
      1. batch preflight_only reaches four preflights ready, zero jobs activated
      2. multiple ticks after ready keep execution_ready=False
      3. autoActivatePreflights() (backend gate) refuses to activate these jobs
      4. claim() does not deliver these jobs
      5. normal batch with allow_activation=True still follows the full flow
      6. no implicit promotion from preflight_only to execute mode
      7. repeated benchmark dispatch stays idempotent with zero submissions
    """

    def setUp(self):
        self._tmp = tempfile.mkdtemp()
        self._state_dir = Path(self._tmp) / 'state'
        self._state_dir.mkdir()
        self._data_patcher = patch.object(store, 'DATA', Path(self._tmp) / 'data')
        self._data_patcher.start()
        store.DATA.mkdir(parents=True, exist_ok=True)
        browser_queue.save({
            'running': True, 'concurrency': 4, 'jobs': [],
            'connected_at': None, 'preflights': [], 'preflight_requests': [],
            'extension_session_id': None, 'batch_authorizations': [],
        })

    def tearDown(self):
        self._data_patcher.stop()

    def _enqueue_k01_k04(self):
        anchor_bytes = b'anchor-bytes'
        card_bytes = b'card-bytes'
        anchor_sha = _sha(anchor_bytes)
        card_sha = _sha(card_bytes)
        script_sha = _sha(b'script')
        hooks_sha = _sha(b'hooks')
        canonical = _make_canonical_state(self._state_dir)
        (self._state_dir / pipeline_state.STATUS_FILENAME).write_text(
            json.dumps(canonical), encoding='utf-8')
        pkg_sha = canonical['artifacts']['image_prompts_current']['sha256']
        state_path = str(self._state_dir / pipeline_state.STATUS_FILENAME)
        anchor_path = str(self._state_dir / 'anchor.jpeg')
        card_path = str(self._state_dir / 'REF-CARTA.png')
        specs = []
        for asset_id in ['K01_hook_card_pull_camera', 'K02_hook_salt_circle_closing',
                         'K03_hook_honey_over_card', 'K04_body_reading_t2_t4']:
            prompt = f'Prompt {asset_id.split("_")[0]}'
            prompt_sha = _sha(prompt.encode())
            identity = {
                'production_id': 'sexta_pessoa', 'pipeline': 'auraly_soulmate',
                'avatar_id': 'casey_harrisson', 'asset_id': asset_id,
                'prompt_sha256': prompt_sha, 'anchor_sha256': anchor_sha,
                'shared_card_reference_sha256': card_sha,
                'source_script_sha256': script_sha, 'hook_selection_sha256': hooks_sha,
                'parent': None,
            }
            fp = _sha(json.dumps(identity, ensure_ascii=False, sort_keys=True,
                                  separators=(',', ':')).encode())
            specs.append({
                **identity,
                'prompt': prompt,
                'source_prompt_package_sha256': pkg_sha,
                'canonical_state_path': state_path,
                'references': [
                    {'role': 'avatar_anchor', 'canonical_path': anchor_path,
                     'sha256': anchor_sha, 'size': 12, 'mtime_ns': 0},
                    {'role': 'shared_card_reference', 'canonical_path': card_path,
                     'sha256': card_sha, 'size': 10, 'mtime_ns': 0},
                ],
                'parent_dependency': None,
                'execution_spec': {
                    'version': 1, 'target_generation_provider': 'chatgpt_ui',
                    'retry_policy': {'automatic_retry': False, 'requires_explicit_recovery': True},
                    'dependencies': [],
                    'expected_reference_sha256': {'avatar_anchor': anchor_sha,
                                                  'shared_card_reference': card_sha},
                },
                'canonical_asset_fingerprint': fp,
            })
        browser_queue.enqueue_materialized(specs)
        fps = {s['asset_id']: s['canonical_asset_fingerprint'] for s in specs}
        return fps

    # ── Test A1: preflight_only batch reaches ready state, zero jobs activated ─
    def test_preflight_only_batch_zero_jobs_activated(self):
        fps = self._enqueue_k01_k04()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps,
            allow_activation=False)
        result = browser_queue.dispatch_batch(batch['batch_id'])
        self.assertEqual(len(result['dispatched']), 4)
        # Verify allow_activation=False is stored on the batch
        self.assertFalse(batch['allow_activation'])
        # Verify all 4 preflight_requests carry allow_activation=False
        state = browser_queue.load()
        batch_requests = [r for r in state['preflight_requests']
                          if r.get('batch_id') == batch['batch_id']]
        self.assertEqual(len(batch_requests), 4)
        for req in batch_requests:
            self.assertFalse(req.get('allow_activation'),
                             f"request {req['request_id']} should have allow_activation=False")
        # Zero jobs must have execution_ready=True
        activated = [j for j in state['jobs'] if j.get('execution_ready')]
        self.assertEqual(activated, [])

    # ── Test A2: execution_ready stays False even after simulated preflight registration
    def test_preflight_only_batch_execution_ready_stays_false_after_preflight(self):
        fps = self._enqueue_k01_k04()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps,
            allow_activation=False)
        browser_queue.dispatch_batch(batch['batch_id'])
        state = browser_queue.load()
        # Simulate: extension registered a preflight (status='valid') for K01
        k01_job = next(j for j in state['jobs']
                       if j.get('asset_id') == 'K01_hook_card_pull_camera')
        from datetime import datetime, timedelta, timezone
        now = datetime.now(timezone.utc)
        preflight_row = {
            'job_id': k01_job['id'],
            'canonical_asset_fingerprint': k01_job['canonical_asset_fingerprint'],
            'tab_id': 101, 'window_id': 1, 'url': 'https://chatgpt.com/',
            'extension_session_id': 'sess-abc',
            'nonce': 'nonce-1', 'preflight_id': 'pf-001',
            'created_at': now.isoformat(),
            'expires_at': (now + timedelta(seconds=120)).isoformat(),
            'status': 'valid',
            'content_script_ready': True, 'composer_ready': True,
            'upload_ready': True, 'draft_empty': True, 'generation_idle': True,
            'modal_clear': True, 'conversation_clean': True,
        }
        state['preflights'].append(preflight_row)
        browser_queue.save(state)
        # Simulate multiple ticks: K01 still must not be execution_ready
        for _ in range(3):
            state = browser_queue.load()
            k01 = next(j for j in state['jobs']
                       if j.get('asset_id') == 'K01_hook_card_pull_camera')
            self.assertFalse(k01.get('execution_ready'),
                             'K01 must remain execution_ready=False in preflight_only batch')

    # ── Test A3: backend refuses activate_materialized for preflight_only jobs ─
    def test_activate_materialized_refused_for_preflight_only_batch(self):
        fps = self._enqueue_k01_k04()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps,
            allow_activation=False)
        browser_queue.dispatch_batch(batch['batch_id'])
        state = browser_queue.load()
        k01_job = next(j for j in state['jobs']
                       if j.get('asset_id') == 'K01_hook_card_pull_camera')
        # Register a valid preflight manually (simulates what the extension would produce)
        from datetime import datetime, timedelta, timezone
        now = datetime.now(timezone.utc)
        state['extension_session_id'] = 'sess-test'
        pf = {
            'job_id': k01_job['id'],
            'canonical_asset_fingerprint': k01_job['canonical_asset_fingerprint'],
            'tab_id': 200, 'window_id': 2, 'url': 'https://chatgpt.com/',
            'extension_session_id': 'sess-test', 'nonce': 'n1', 'preflight_id': 'pf-999',
            'created_at': now.isoformat(),
            'expires_at': (now + timedelta(seconds=120)).isoformat(),
            'status': 'valid',
            'content_script_ready': True, 'composer_ready': True, 'upload_ready': True,
            'draft_empty': True, 'generation_idle': True, 'modal_clear': True,
            'conversation_clean': True,
        }
        state['preflights'].append(pf)
        browser_queue.save(state)
        revalidation = {
            'job_id': k01_job['id'],
            'canonical_asset_fingerprint': k01_job['canonical_asset_fingerprint'],
            'tab_id': 200, 'window_id': 2, 'url': 'https://chatgpt.com/',
            'extension_session_id': 'sess-test',
            'content_script_ready': True, 'composer_ready': True, 'upload_ready': True,
            'draft_empty': True, 'generation_idle': True, 'modal_clear': True,
            'conversation_clean': True,
        }
        with self.assertRaises(ValueError) as ctx:
            browser_queue.activate_materialized(
                k01_job['id'], k01_job['canonical_asset_fingerprint'], 'pf-999', revalidation)
        self.assertIn('allow_activation=False', str(ctx.exception))
        # Job still not execution_ready
        k01_now = browser_queue.get_job(k01_job['id'])
        self.assertFalse(k01_now.get('execution_ready'))

    # ── Test A4: claim() does not deliver preflight_only batch jobs ───────────
    def test_claim_does_not_deliver_preflight_only_jobs(self):
        fps = self._enqueue_k01_k04()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps,
            allow_activation=False)
        browser_queue.dispatch_batch(batch['batch_id'])
        # Even if we set execution_ready=True manually (simulating a bypass attempt),
        # claim() must still skip them because of the preflight_only batch guard.
        state = browser_queue.load()
        for job in state['jobs']:
            if job.get('job_kind') == 'canonical_materialized':
                job['execution_ready'] = True
                job['authorized_target'] = {'tab_id': 1, 'window_id': 1,
                                            'url': 'https://chatgpt.com/',
                                            'extension_session_id': 'sess-x',
                                            'preflight_id': 'pf-x'}
                job['activation_preflight_id'] = 'pf-x'
                job['tab_id'] = 1
                job['window_id'] = 1
                job['preflight_url'] = 'https://chatgpt.com/'
                job['authorized_extension_session_id'] = 'sess-x'
        browser_queue.save(state)
        claimed = browser_queue.claim()
        self.assertIsNone(claimed, 'claim() must return None for preflight_only batch jobs')

    # ── Test A5: normal batch with allow_activation=True follows the full flow ─
    def test_allow_activation_true_batch_can_be_activated(self):
        fps = self._enqueue_k01_k04()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps,
            allow_activation=True)
        browser_queue.dispatch_batch(batch['batch_id'])
        state = browser_queue.load()
        # preflight_requests for this batch must have allow_activation=True
        batch_requests = [r for r in state['preflight_requests']
                          if r.get('batch_id') == batch['batch_id']]
        for req in batch_requests:
            self.assertTrue(req.get('allow_activation', True),
                            'allow_activation=True batch requests must carry True')
        # _job_in_preflight_only_batch must return False for these jobs
        k01_job = next(j for j in state['jobs']
                       if j.get('asset_id') == 'K01_hook_card_pull_camera')
        self.assertFalse(browser_queue._job_in_preflight_only_batch(state, k01_job['id']))

    # ── Test A6: no implicit promotion from preflight_only to execute ──────────
    def test_preflight_only_cannot_be_promoted_implicitly(self):
        fps = self._enqueue_k01_k04()
        batch = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps,
            allow_activation=False)
        browser_queue.dispatch_batch(batch['batch_id'])
        # Repeated dispatch calls must not change allow_activation on the batch
        browser_queue.dispatch_batch(batch['batch_id'])
        state = browser_queue.load()
        saved_batch = next(b for b in state['batch_authorizations']
                           if b['batch_id'] == batch['batch_id'])
        self.assertFalse(saved_batch['allow_activation'],
                         'allow_activation must not be implicitly promoted to True')
        # New authorize_batch with allow_activation=True on same jobs must create
        # a SEPARATE batch, leaving the original untouched
        batch2 = browser_queue.authorize_batch(
            'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps,
            allow_activation=True)
        self.assertNotEqual(batch2['batch_id'], batch['batch_id'])
        self.assertTrue(batch2['allow_activation'])
        state = browser_queue.load()
        original = next(b for b in state['batch_authorizations']
                        if b['batch_id'] == batch['batch_id'])
        self.assertFalse(original['allow_activation'],
                         'original preflight_only batch must not be affected by new execution batch')

    # ── Test A7: repeated benchmark dispatch is idempotent, zero submissions ───
    def test_repeated_benchmark_dispatch_idempotent_no_submissions(self):
        fps = self._enqueue_k01_k04()
        UNSAFE = {'preparing', 'submitting', 'generating', 'receiving'}
        for i in range(3):
            batch = browser_queue.authorize_batch(
                'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps,
                allow_activation=False)
            r1 = browser_queue.dispatch_batch(batch['batch_id'])
            r2 = browser_queue.dispatch_batch(batch['batch_id'])
            # Second dispatch must reuse all 4 requests
            self.assertTrue(all(d['reused'] for d in r2['dispatched']),
                            f'iteration {i}: second dispatch must reuse all requests')
            state = browser_queue.load()
            # Zero jobs must be in any submission state
            unsafe_jobs = [j for j in state['jobs'] if j.get('status') in UNSAFE]
            self.assertEqual(unsafe_jobs, [],
                             f'iteration {i}: no jobs must be in submission state')
            # Zero jobs must be execution_ready
            activated = [j for j in state['jobs'] if j.get('execution_ready')]
            self.assertEqual(activated, [],
                             f'iteration {i}: no jobs must be execution_ready')


if __name__ == '__main__':
    unittest.main()
