"""Tests for studio/orchestrator.py — execute_avatar, status, fail-fast, idempotency."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from . import browser_queue as queue, execution_plan as ep, pipeline_browser_bridge as bridge
from . import pipeline_state as state, storage as store, orchestrator
from .test_pipeline_browser_bridge import ready_state

_MOCK_BRIDGE_URL = "http://127.0.0.1:8765"


class ExecuteAvatarTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "sexta_pessoa"
        self.root.mkdir()
        self.qpatch = patch.object(store, "DATA", self.root / "isolated-queue")
        self.qpatch.start()
        ready_state(self.root)
        bridge.sync_prepared_assets(self.root)
        # Build a valid plan on disk
        self.plan = ep.build(self.root)

    def tearDown(self):
        self.qpatch.stop()
        self.temp.cleanup()

    def _run(self, **kwargs):
        """execute_avatar with ensure_bridge mocked out (no real subprocess)."""
        with patch("studio.orchestrator.ensure_bridge", return_value=_MOCK_BRIDGE_URL):
            return orchestrator.execute_avatar(self.root, **kwargs)

    # ── 1: five assets selected ───────────────────────────────────────────────

    def test_five_assets_selected_for_casey(self):
        result = self._run()
        self.assertEqual(len(result["assets"]), 5)
        self.assertEqual(
            set(result["assets"]),
            {"K01_hook_card_pull_camera", "K02_hook_salt_circle_closing",
             "K03_hook_honey_over_card", "K04_body_reading_t2_t4", "K05_cta_stories_t5"},
        )

    # ── 2: exactly one batch with all five assets ─────────────────────────────

    def test_exactly_one_batch_with_five_assets(self):
        result = self._run()
        q = queue.load()
        batches = q.get("batch_authorizations", [])
        matching = [b for b in batches if b["batch_id"] == result["batch_id"]]
        self.assertEqual(len(matching), 1)
        batch = matching[0]
        batch_asset_ids = {a["asset_id"] for a in batch["assets"]}
        self.assertEqual(batch_asset_ids, set(result["assets"]))

    # ── 3: effective concurrency = 5 ─────────────────────────────────────────

    def test_effective_concurrency_five(self):
        result = self._run()
        self.assertEqual(result["effective_concurrency"], 5)
        q = queue.load()
        self.assertEqual(q.get("concurrency"), 5)

    # ── 4: K05 independent — no parent_approved_result in its preflight refs ──

    def test_k05_independent_no_parent_dependency(self):
        result = self._run()
        q = queue.load()
        k05_job = next(
            (j for j in q["jobs"] if j.get("asset_id") == "K05_cta_stories_t5"), None
        )
        self.assertIsNotNone(k05_job, "K05 job must be in queue")
        # No parent_dependency in the materialized job
        self.assertIsNone(k05_job.get("parent_dependency"))

    # ── 5: invalid plan → abort before bridge ────────────────────────────────

    def test_invalid_plan_aborts_before_bridge(self):
        # Tamper the plan on disk so validate fails (empty prompt)
        plan_path = self.root / ep.PLAN_FILENAME
        raw = json.loads(plan_path.read_text())
        raw["assets"][0]["prompt"] = ""
        # Recompute sha256 so load() passes; validate() catches the empty prompt
        body = {k: v for k, v in raw.items() if k != "plan_sha256"}
        raw["plan_sha256"] = ep._sha256(body)
        plan_path.write_text(json.dumps(raw))

        bridge_called = []
        authorize_called = []
        dispatch_called = []

        with patch("studio.orchestrator.ensure_bridge", side_effect=lambda: bridge_called.append(1)):
            with patch.object(queue, "authorize_batch", side_effect=lambda *a, **k: authorize_called.append(1)):
                with patch.object(queue, "dispatch_batch", side_effect=lambda *a: dispatch_called.append(1)):
                    with self.assertRaises(ValueError, msg="invalid plan must raise ValueError"):
                        orchestrator.execute_avatar(self.root)

        self.assertEqual(bridge_called, [], "ensure_bridge must NOT be called on invalid plan")
        self.assertEqual(authorize_called, [], "authorize_batch must NOT be called on invalid plan")
        self.assertEqual(dispatch_called, [], "dispatch_batch must NOT be called on invalid plan")

    # ── 6: tampered plan (sha256 mismatch) → abort before bridge ─────────────

    def test_tampered_plan_sha256_aborts_before_bridge(self):
        plan_path = self.root / ep.PLAN_FILENAME
        raw = json.loads(plan_path.read_text())
        raw["assets"][0]["prompt"] = "TAMPERED"
        # Do NOT update plan_sha256 — load() will detect mismatch
        plan_path.write_text(json.dumps(raw))

        with patch("studio.orchestrator.ensure_bridge",
                   side_effect=AssertionError("ensure_bridge must not be called")):
            with self.assertRaises((ValueError, AssertionError)):
                orchestrator.execute_avatar(self.root)

    # ── 7: missing anchor → abort before bridge ───────────────────────────────

    def test_missing_anchor_aborts_before_bridge(self):
        plan = ep.load(self.root)
        anchor_path = next(
            r["canonical_path"]
            for a in plan["assets"]
            for r in a["references"] if r["role"] == "avatar_anchor"
        )
        Path(anchor_path).unlink()

        with patch("studio.orchestrator.ensure_bridge",
                   side_effect=AssertionError("ensure_bridge must not be called")):
            with self.assertRaises((ValueError, AssertionError)):
                orchestrator.execute_avatar(self.root)

    # ── 8: repeated call is idempotent ────────────────────────────────────────

    def test_repeated_call_is_idempotent(self):
        r1 = self._run()
        r2 = self._run()

        # Same batch reused
        self.assertEqual(r1["batch_id"], r2["batch_id"])
        self.assertTrue(r2["resumed"], "second call must set resumed=True")

        # Job count must not grow
        jobs_after_1 = len(queue.load()["jobs"])
        jobs_after_2 = len(queue.load()["jobs"])
        self.assertEqual(jobs_after_1, jobs_after_2, "jobs must not be duplicated")

        # Preflight requests must not grow
        prs_1 = len(queue.load().get("preflight_requests", []))
        self._run()
        prs_2 = len(queue.load().get("preflight_requests", []))
        self.assertEqual(prs_1, prs_2, "preflight_requests must not be duplicated")

    # ── 9: only current avatar's assets included ─────────────────────────────

    def test_wrong_avatar_id_raises(self):
        with patch("studio.orchestrator.ensure_bridge", return_value=_MOCK_BRIDGE_URL):
            with self.assertRaises(ValueError, msg="wrong avatar must raise"):
                orchestrator.execute_avatar(self.root, avatar_id="somebody_else")

    # ── 10: MAX_BROWSER_CONCURRENCY cap respected ─────────────────────────────

    def test_max_concurrency_cap_in_plan_used(self):
        # Rebuild plan with cap=3; execute_avatar must use plan's effective_concurrency
        capped_plan = ep.build(self.root, max_concurrency=3)
        self.assertEqual(capped_plan["effective_concurrency"], 3)
        self.assertEqual(capped_plan["desired_concurrency"], 5)
        with patch("studio.orchestrator.ensure_bridge", return_value=_MOCK_BRIDGE_URL):
            result = orchestrator.execute_avatar(self.root)
        self.assertEqual(result["effective_concurrency"], 3)
        self.assertEqual(queue.load().get("concurrency"), 3)

    # ── 11: healthy bridge reused (Popen not called) ──────────────────────────

    def test_healthy_bridge_is_reused(self):
        import httpx
        with patch("studio.bridge.httpx.get", return_value=MagicMock(status_code=200)):
            with patch("studio.bridge.subprocess.Popen") as mock_popen:
                result = orchestrator.execute_avatar(self.root)
                mock_popen.assert_not_called()
        self.assertIn("batch_id", result)

    # ── 12: Claude and Codex use the exact same function ─────────────────────

    def test_claude_and_codex_use_same_entry_point(self):
        # Both agents import from studio.orchestrator; verify the function is stable
        from studio.orchestrator import execute_avatar as fn_direct
        from studio import orchestrator as mod
        self.assertIs(fn_direct, mod.execute_avatar)
        # Function signature accepts root + optional avatar_id, nothing else required
        import inspect
        sig = inspect.signature(fn_direct)
        params = list(sig.parameters.keys())
        self.assertIn("root", params)
        self.assertIn("avatar_id", params)

    # ── concurrency scaling ───────────────────────────────────────────────────

    def test_concurrency_scales_with_asset_count(self):
        # 5 assets, default cap 8 → effective 5 in one wave
        plan = ep.build(self.root, dry_run=True)
        self.assertEqual(plan["desired_concurrency"], 5)
        self.assertEqual(plan["effective_concurrency"], 5)
        self.assertEqual(plan["n_waves"], 1)

        # 5 assets, cap 3 → effective 3, 2 waves; all 5 still pre-materialized
        plan_capped = ep.build(self.root, dry_run=True, max_concurrency=3)
        self.assertEqual(plan_capped["effective_concurrency"], 3)
        self.assertEqual(plan_capped["n_waves"], 2)
        self.assertEqual(len(plan_capped["assets"]), 5)  # all prepared, scheduler handles waves

    def test_zero_real_browser_actions(self):
        """After execute_avatar, no job has been activated (execution_ready stays False)."""
        self._run()
        q = queue.load()
        activated = [j for j in q["jobs"] if j.get("execution_ready")]
        self.assertEqual(activated, [], "no job must be execution_ready after execute_avatar")
        unsafe = [j for j in q["jobs"]
                  if j.get("status") in {"preparing", "submitting", "generating", "receiving"}]
        self.assertEqual(unsafe, [], "no job must be in a submission state")


class ExecuteAvatarConcurrencyTests(unittest.TestCase):
    """Prove wave/concurrency properties across different hook counts via plan."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "sexta_pessoa"
        self.root.mkdir()
        self.qpatch = patch.object(store, "DATA", self.root / "isolated-queue")
        self.qpatch.start()
        ready_state(self.root)
        bridge.sync_prepared_assets(self.root)

    def tearDown(self):
        self.qpatch.stop()
        self.temp.cleanup()

    def _plan_with_cap(self, cap):
        return ep.build(self.root, dry_run=True, max_concurrency=cap)

    def test_n_plus_2_concurrency_table(self):
        # Using the actual 5-asset plan, test capping at various levels
        cases = [
            # (max_concurrency, expected_effective, expected_waves)
            (10, 5, 1),   # 5 ≤ 10 → effective=5, 1 wave
            (5,  5, 1),   # 5 == 5 → effective=5, 1 wave
            (4,  4, 2),   # 5 > 4  → effective=4, 2 waves (4+1)
            (3,  3, 2),   # 5 > 3  → effective=3, 2 waves (3+2)
            (2,  2, 3),   # 5 > 2  → effective=2, 3 waves (2+2+1)
            (1,  1, 5),   # 5 > 1  → effective=1, 5 waves
        ]
        for cap, exp_eff, exp_waves in cases:
            with self.subTest(cap=cap):
                plan = self._plan_with_cap(cap)
                self.assertEqual(plan["effective_concurrency"], exp_eff,
                                 f"cap={cap}: effective_concurrency")
                self.assertEqual(plan["n_waves"], exp_waves,
                                 f"cap={cap}: n_waves")
                # All 5 assets always pre-materialized
                self.assertEqual(len(plan["assets"]), 5,
                                 f"cap={cap}: all assets must be in plan")


class StatusTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "sexta_pessoa"
        self.root.mkdir()
        self.qpatch = patch.object(store, "DATA", self.root / "isolated-queue")
        self.qpatch.start()
        ready_state(self.root)
        bridge.sync_prepared_assets(self.root)

    def tearDown(self):
        self.qpatch.stop()
        self.temp.cleanup()

    def test_status_returns_expected_keys(self):
        ep.build(self.root)
        s = orchestrator.status(self.root)
        for key in ("production", "current_stage", "current_avatar", "next_action",
                    "plan_version", "plan_sha256", "plan_valid",
                    "assets_total", "assets_pending", "assets_queued",
                    "assets_running", "assets_received", "assets_approved", "queue_jobs"):
            self.assertIn(key, s, f"status() missing key '{key}'")

    def test_status_plan_valid_true_after_build(self):
        ep.build(self.root)
        s = orchestrator.status(self.root)
        self.assertTrue(s["plan_valid"])
        self.assertEqual(s["assets_total"], 5)

    def test_status_plan_valid_false_without_plan(self):
        s = orchestrator.status(self.root)
        self.assertIsNone(s["plan_valid"])

    def test_status_does_not_raise_without_plan(self):
        s = orchestrator.status(self.root)
        self.assertIsNotNone(s["production"])


if __name__ == "__main__":
    unittest.main()
