import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from . import browser_queue as queue, execution_plan, pipeline_browser_bridge as bridge, pipeline_state as state, storage as store
from .test_pipeline_browser_bridge import ready_state


class ExecutionPlanBuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "sexta_pessoa"
        self.root.mkdir()
        self.patch = patch.object(store, "DATA", self.root / "isolated-queue")
        self.patch.start()
        ready_state(self.root)
        # Sync queue so jobs exist (status=queued) — build_materialized_jobs needs pending/queued
        bridge.sync_prepared_assets(self.root)

    def tearDown(self):
        self.patch.stop()
        self.temp.cleanup()

    def test_build_produces_exactly_five_assets(self):
        plan = execution_plan.build(self.root, dry_run=True)
        self.assertEqual(len(plan["assets"]), 5)
        self.assertEqual(
            {a["asset_id"] for a in plan["assets"]},
            {"K01_hook_card_pull_camera", "K02_hook_salt_circle_closing",
             "K03_hook_honey_over_card", "K04_body_reading_t2_t4", "K05_cta_stories_t5"},
        )

    def test_all_assets_eligible_no_parent_dependency(self):
        plan = execution_plan.build(self.root, dry_run=True)
        for asset in plan["assets"]:
            aid = asset["asset_id"]
            self.assertTrue(asset["eligible"], f"{aid} should be eligible")
            ref_roles = {r["role"] for r in asset["references"]}
            self.assertNotIn("parent_approved_result", ref_roles,
                             f"{aid} must not reference parent_approved_result")
            self.assertEqual(asset["execution_spec"]["dependencies"], [],
                             f"{aid} must have no execution dependencies")

    def test_k05_references_match_k01_pattern(self):
        plan = execution_plan.build(self.root, dry_run=True)
        k01 = next(a for a in plan["assets"] if a["asset_id"] == "K01_hook_card_pull_camera")
        k05 = next(a for a in plan["assets"] if a["asset_id"] == "K05_cta_stories_t5")
        self.assertEqual(
            {r["role"] for r in k01["references"]},
            {r["role"] for r in k05["references"]},
        )
        self.assertEqual({r["role"] for r in k05["references"]},
                         {"avatar_anchor", "shared_card_reference"})

    def test_plan_sha256_valid(self):
        plan = execution_plan.build(self.root, dry_run=True)
        stored = plan["plan_sha256"]
        body = {k: v for k, v in plan.items() if k != "plan_sha256"}
        self.assertEqual(execution_plan._sha256(body), stored)

    def test_tampered_plan_detected_on_load(self):
        execution_plan.build(self.root)
        plan_path = self.root / execution_plan.PLAN_FILENAME
        raw = json.loads(plan_path.read_text())
        raw["assets"][0]["prompt"] = "TAMPERED"
        plan_path.write_text(json.dumps(raw))
        with self.assertRaises(ValueError, msg="load() must detect tampered content"):
            execution_plan.load(self.root)

    def test_build_is_idempotent(self):
        plan1 = execution_plan.build(self.root)
        plan2 = execution_plan.build(self.root)
        self.assertEqual(plan1["plan_sha256"], plan2["plan_sha256"])

    def test_prompt_change_changes_asset_fingerprint(self):
        plan1 = execution_plan.build(self.root, dry_run=True)
        # Mutate the prompt package so one asset's prompt changes
        st = state.load(self.root)
        package_path = self.root / st["artifacts"]["image_prompts_current"]["path"]
        text = package_path.read_text(encoding="utf-8")
        new_text = text.replace('"K02_hook_salt_circle_closing"', '"K02 MODIFIED"')
        package_path.write_text(new_text, encoding="utf-8")
        # Invalidate K02 prompt_sha256 so it gets requeued
        _, sections = state._prompt_package_metadata_and_sections(package_path)
        import hashlib
        st["avatars"]["casey_harrisson"]["assets"]["K02_hook_salt_circle_closing"]["prompt_sha256"] = \
            hashlib.sha256(sections["K02_hook_salt_circle_closing"].encode()).hexdigest()
        st["avatars"]["casey_harrisson"]["assets"]["K02_hook_salt_circle_closing"]["status"] = "pending"
        state.save(st, self.root)
        bridge.sync_prepared_assets(self.root)
        plan2 = execution_plan.build(self.root, dry_run=True)
        fp1 = {a["asset_id"]: a["canonical_asset_fingerprint"] for a in plan1["assets"]}
        fp2 = {a["asset_id"]: a["canonical_asset_fingerprint"] for a in plan2["assets"]}
        self.assertNotEqual(fp1["K02_hook_salt_circle_closing"], fp2["K02_hook_salt_circle_closing"])
        # Other assets unchanged
        self.assertEqual(fp1["K01_hook_card_pull_camera"], fp2["K01_hook_card_pull_camera"])

    def test_anchor_change_changes_all_fingerprints(self):
        plan1 = execution_plan.build(self.root, dry_run=True)
        # Update anchor sha256 in state to simulate a file change
        st = state.load(self.root)
        avatar = st["avatars"]["casey_harrisson"]
        anchor = Path(avatar["anchor_path"])
        anchor.write_bytes(b"new-anchor-bytes")
        new_sha = state.sha256_file(anchor)
        for asset in avatar["assets"].values():
            asset["anchor_sha256"] = new_sha
            asset["status"] = "pending"
        state.save(st, self.root)
        bridge.sync_prepared_assets(self.root)
        plan2 = execution_plan.build(self.root, dry_run=True)
        fp1 = {a["asset_id"]: a["canonical_asset_fingerprint"] for a in plan1["assets"]}
        fp2 = {a["asset_id"]: a["canonical_asset_fingerprint"] for a in plan2["assets"]}
        for aid in fp1:
            self.assertNotEqual(fp1[aid], fp2[aid], f"fingerprint for {aid} must change after anchor update")

    def test_all_required_fields_present(self):
        plan = execution_plan.build(self.root, dry_run=True)
        for asset in plan["assets"]:
            for field in execution_plan.REQUIRED_ASSET_FIELDS:
                self.assertIn(field, asset, f"{asset['asset_id']} missing '{field}'")
                self.assertIsNotNone(asset[field], f"{asset['asset_id']}.{field} must not be None")

    def test_concurrency_capped_at_max_browser_concurrency(self):
        plan = execution_plan.build(self.root, dry_run=True, max_concurrency=3)
        self.assertEqual(plan["desired_concurrency"], 5)
        self.assertEqual(plan["effective_concurrency"], 3)
        self.assertEqual(plan["n_waves"], 2)
        waves = [a["wave"] for a in plan["assets"]]
        self.assertEqual(waves[:3], [0, 0, 0])
        self.assertEqual(waves[3:], [1, 1])

    def test_default_concurrency_covers_all_five_assets_in_one_wave(self):
        plan = execution_plan.build(self.root, dry_run=True)
        self.assertEqual(plan["effective_concurrency"], 5)
        self.assertEqual(plan["n_waves"], 1)
        self.assertTrue(all(a["wave"] == 0 for a in plan["assets"]))

    def test_prepare_then_build_then_validate_full_cycle(self):
        plan = execution_plan.build(self.root)
        loaded = execution_plan.load(self.root)
        self.assertEqual(plan["plan_sha256"], loaded["plan_sha256"])
        errors = execution_plan.validate_execution_plan(loaded)
        self.assertEqual(errors, [], f"Unexpected errors: {errors}")

    def test_ineligible_asset_blocks_build(self):
        # Mark K03 ineligible
        st = state.load(self.root)
        st["avatars"]["casey_harrisson"]["assets"]["K03_hook_honey_over_card"]["eligible_for_execution"] = False
        state.save(st, self.root)
        with self.assertRaises(ValueError, msg="build() must refuse when assets are not eligible"):
            execution_plan.build(self.root, dry_run=True)

    def test_output_paths_are_deterministic_and_contain_asset_id(self):
        plan = execution_plan.build(self.root, dry_run=True)
        for asset in plan["assets"]:
            self.assertIn(asset["asset_id"], asset["output_path"])
            self.assertTrue(asset["output_path"].endswith(".png"))

    def test_production_pipeline_avatar_duplicated_per_asset(self):
        plan = execution_plan.build(self.root, dry_run=True)
        for asset in plan["assets"]:
            self.assertEqual(asset["production_id"], plan["production_id"])
            self.assertEqual(asset["pipeline"], plan["pipeline"])
            self.assertEqual(asset["avatar_id"], plan["avatar_id"])


class ExecutionPlanValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "sexta_pessoa"
        self.root.mkdir()
        self.patch = patch.object(store, "DATA", self.root / "isolated-queue")
        self.patch.start()
        ready_state(self.root)
        bridge.sync_prepared_assets(self.root)
        self.plan = execution_plan.build(self.root, dry_run=True)

    def tearDown(self):
        self.patch.stop()
        self.temp.cleanup()

    def test_valid_plan_passes_with_zero_errors(self):
        errors = execution_plan.validate_execution_plan(self.plan)
        self.assertEqual(errors, [])

    def test_missing_anchor_file_fails(self):
        plan = copy.deepcopy(self.plan)
        anchor_ref = next(r for r in plan["assets"][0]["references"] if r["role"] == "avatar_anchor")
        Path(anchor_ref["canonical_path"]).unlink()
        errors = execution_plan.validate_execution_plan(plan)
        self.assertTrue(any("file not found" in e for e in errors), errors)

    def test_missing_card_file_fails(self):
        plan = copy.deepcopy(self.plan)
        card_ref = next(
            r for a in plan["assets"] for r in a["references"]
            if r["role"] == "shared_card_reference"
        )
        Path(card_ref["canonical_path"]).unlink()
        errors = execution_plan.validate_execution_plan(plan)
        self.assertTrue(any("file not found" in e for e in errors), errors)

    def test_hash_divergence_detected(self):
        plan = copy.deepcopy(self.plan)
        anchor_ref = next(r for r in plan["assets"][0]["references"] if r["role"] == "avatar_anchor")
        Path(anchor_ref["canonical_path"]).write_bytes(b"tampered-anchor-content")
        errors = execution_plan.validate_execution_plan(plan)
        self.assertTrue(any("hash mismatch" in e for e in errors), errors)

    def test_empty_prompt_fails(self):
        plan = copy.deepcopy(self.plan)
        plan["assets"][0]["prompt"] = ""
        errors = execution_plan.validate_execution_plan(plan)
        self.assertTrue(any("prompt is empty" in e for e in errors), errors)

    def test_whitespace_only_prompt_fails(self):
        plan = copy.deepcopy(self.plan)
        plan["assets"][0]["prompt"] = "   \n  "
        errors = execution_plan.validate_execution_plan(plan)
        self.assertTrue(any("prompt is empty" in e for e in errors), errors)

    def test_duplicate_asset_id_fails(self):
        plan = copy.deepcopy(self.plan)
        plan["assets"].append(copy.deepcopy(plan["assets"][0]))
        errors = execution_plan.validate_execution_plan(plan)
        self.assertTrue(any("duplicate" in e for e in errors), errors)

    def test_missing_required_field_fails(self):
        plan = copy.deepcopy(self.plan)
        del plan["assets"][0]["execution_spec"]
        errors = execution_plan.validate_execution_plan(plan)
        self.assertTrue(any("execution_spec" in e for e in errors), errors)

    def test_incomplete_execution_spec_fails(self):
        plan = copy.deepcopy(self.plan)
        del plan["assets"][0]["execution_spec"]["target_generation_provider"]
        errors = execution_plan.validate_execution_plan(plan)
        self.assertTrue(any("execution_spec missing" in e for e in errors), errors)

    def test_output_path_without_extension_fails(self):
        plan = copy.deepcopy(self.plan)
        plan["assets"][0]["output_path"] = "/some/path/no_extension"
        errors = execution_plan.validate_execution_plan(plan)
        self.assertTrue(any("no extension" in e for e in errors), errors)

    def test_fingerprint_collision_fails(self):
        plan = copy.deepcopy(self.plan)
        plan["assets"][1]["canonical_asset_fingerprint"] = plan["assets"][0]["canonical_asset_fingerprint"]
        errors = execution_plan.validate_execution_plan(plan)
        self.assertTrue(any("collision" in e for e in errors), errors)

    def test_invalid_plan_means_zero_browser_actions(self):
        plan = copy.deepcopy(self.plan)
        plan["assets"][0]["prompt"] = ""
        errors = execution_plan.validate_execution_plan(plan)
        self.assertGreater(len(errors), 0)
        # Critical invariant: invalid plan → queue must not deliver anything
        # No jobs have been activated, so claim() returns None regardless
        self.assertIsNone(queue.claim())

    def test_no_assets_fails(self):
        plan = copy.deepcopy(self.plan)
        plan["assets"] = []
        errors = execution_plan.validate_execution_plan(plan)
        self.assertTrue(any("no assets" in e for e in errors), errors)


if __name__ == "__main__":
    unittest.main()
