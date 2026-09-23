import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from PIL import Image

from . import browser_queue as queue, pipeline_browser_bridge as bridge, pipeline_state as state, storage as store


def ready_state(root: Path):
    script = root / "ROTEIRO.md"; script.write_text("script", encoding="utf-8")
    selection = "selected-hooks-hash"
    ids = ("K01_hook_card_pull_camera", "K02_hook_salt_circle_closing", "K03_hook_honey_over_card", "K04_body_reading_t2_t4", "K05_cta_stories_t5")
    metadata = {"version": 2, "source_script": {"sha256": state.sha256_file(script)}, "hook_selection": {"sha256": selection}}
    package = root / "PROMPTS.v2.md"
    package.write_text("```json\n" + json.dumps(metadata) + "\n```\n" + "\n".join(
        f"## {asset_id} · TEST\n```json\n{{\"shot_id\": \"{asset_id}\"}}\n```" for asset_id in ids), encoding="utf-8")
    anchor = root / "casey.jpeg"; anchor.write_bytes(b"anchor-a")
    card = root / "REF-CARTA.png"; card.write_bytes(b"card-a")
    payload = {
        "schema_version": 1, "pipeline": "auraly_soulmate", "angle": 3,
        "production": {"id": "sexta_pessoa", "title": "Test", "root": str(root), "created_at": None, "updated_at": None},
        "workflow": {"stage": "image_prompts_ready", "next_action": "prepare_current_avatar", "current_avatar_id": "casey_harrisson", "blocked_by": None},
        "inputs": {"video": {}, "avatars": []},
        "artifacts": {
            "script": {"path": "ROTEIRO.md", "exists": True, "sha256": state.sha256_file(script)},
            "image_prompts_current": {"path": "PROMPTS.v2.md", "exists": True, "sha256": state.sha256_file(package), "version": 2, "hook_selection_sha256": selection},
            "shared_card_reference": {"path": "REF-CARTA.png", "exists": True, "sha256": state.sha256_file(card)},
        },
        "approvals": {"shared_card_reference": {"status": "approved", "approved_sha256": state.sha256_file(card)}},
        "hooks": {"status": "unknown", "selected_ids": [], "no_hooks_explicitly_authorized": False},
        "avatar_queue": {"order": ["casey_harrisson"], "current_index": 0},
        "avatars": {"casey_harrisson": {"name": "Casey", "stage": "queued", "anchor_path": str(anchor), "anchor_sha256": state.sha256_file(anchor), "assets": {}}},
        "unknowns": [], "inconsistencies": [], "history": [],
    }
    state.save(payload, root)
    state.prepare_current_avatar(root)


class PipelineBrowserBridgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.root = Path(self.temp.name) / "sexta_pessoa"; self.root.mkdir()
        self.patch = patch.object(store, "DATA", self.root / "isolated-queue"); self.patch.start(); ready_state(self.root)

    def tearDown(self):
        self.patch.stop(); self.temp.cleanup()

    def sync(self):
        return bridge.sync_prepared_assets(self.root)

    def image(self):
        raw = io.BytesIO(); Image.new("RGB", (512, 768), "red").save(raw, format="PNG"); return raw.getvalue()

    def preflight(self, job, **changes):
        report = {"job_id": job["id"], "canonical_asset_fingerprint": job["canonical_asset_fingerprint"],
                  "tab_id": 101, "window_id": 11, "url": "https://chatgpt.com/",
                  "extension_session_id": "session-0000000001", "nonce": "nonce-00000000001",
                  "content_script_ready": True, "composer_ready": True, "upload_ready": True,
                  "draft_empty": True, "generation_idle": True, "modal_clear": True, "conversation_clean": True}
        report.update(changes); return report

    def test_sync_is_idempotent_and_materializes_k01_to_k05(self):
        first = self.sync(); second = self.sync()
        self.assertEqual(len(first["contracts"]), 5)
        self.assertEqual(len(first["queue"]["jobs"]), 5)
        self.assertEqual(len(second["queue"]["jobs"]), 5)
        self.assertEqual({j["asset_id"] for j in second["queue"]["jobs"]}, {
            "K01_hook_card_pull_camera", "K02_hook_salt_circle_closing", "K03_hook_honey_over_card",
            "K04_body_reading_t2_t4", "K05_cta_stories_t5"})
        self.assertTrue(all(not j["execution_ready"] for j in second["queue"]["jobs"]))
        self.assertIsNone(queue.claim())

    def test_materialized_contract_uses_declared_references_not_historical_asset_id(self):
        contract = self.sync()["contracts"][0]
        anchor_only = dict(contract)
        anchor_only["references"] = [ref for ref in contract["references"] if ref["role"] == "avatar_anchor"]
        # K01's legacy name must not silently impose REF-CARTA on a newer contract.
        queue.enqueue_materialized([anchor_only])
        self.assertEqual(len(queue.load()["jobs"]), 5)

    def test_dependency_specific_fingerprints(self):
        self.sync(); before = queue.load()["jobs"][:]
        status = state.load(self.root); assets = status["avatars"]["casey_harrisson"]["assets"]
        package = self.root / "PROMPTS.v2.md"; text = package.read_text(encoding="utf-8").replace('"K02_hook_salt_circle_closing"', '"K02 revised"')
        package.write_text(text, encoding="utf-8")
        _, sections = state._prompt_package_metadata_and_sections(package)
        assets["K02_hook_salt_circle_closing"]["prompt_sha256"] = hashlib.sha256(sections["K02_hook_salt_circle_closing"].encode()).hexdigest()
        assets["K02_hook_salt_circle_closing"]["status"] = "pending"; state.save(status, self.root)
        self.sync(); after = queue.load()["jobs"]
        self.assertEqual(len(after), len(before) + 1)
        self.assertEqual(after[-1]["asset_id"], "K02_hook_salt_circle_closing")

    def test_anchor_and_card_changes_affect_only_registered_dependencies(self):
        self.sync(); status = state.load(self.root); avatar = status["avatars"]["casey_harrisson"]
        Path(avatar["anchor_path"]).write_bytes(b"anchor-b"); new_anchor = state.sha256_file(Path(avatar["anchor_path"]))
        for asset in avatar["assets"].values(): asset.update(anchor_sha256=new_anchor, status="pending")
        state.save(status, self.root); self.sync(); self.assertEqual(len(queue.load()["jobs"]), 10)
        status = state.load(self.root); avatar = status["avatars"]["casey_harrisson"]; card = self.root / "REF-CARTA.png"; card.write_bytes(b"card-b"); new_card = state.sha256_file(card)
        for asset in avatar["assets"].values():
            if asset.get("shared_card_reference_sha256"):
                asset.update(shared_card_reference_sha256=new_card, status="pending")
        state.save(status, self.root); self.sync(); jobs = queue.load()["jobs"]
        self.assertEqual(len(jobs), 15)  # K01–K05 all have card dependency

    def test_queue_status_reconciliation_never_approves_without_review_and_is_idempotent(self):
        result = self.sync(); jobs = result["queue"]["jobs"]
        for queue_status in ("queued", "generating", "attention"):
            row = dict(jobs[0], status=queue_status, review_status="pending")
            reconciled = state.reconcile_materialized_jobs(self.root, [row])
            asset = reconciled["avatars"]["casey_harrisson"]["assets"][row["asset_id"]]
            self.assertNotEqual(asset["status"], "approved")
        body_file = self.root / "body.png"; body_file.write_bytes(b"body")
        body_hash = state.sha256_file(body_file)
        row = dict(jobs[3], status="done", review_status="approved", image_sha256=body_hash, local_file=str(body_file))
        one = state.reconcile_materialized_jobs(self.root, [row]); two = state.reconcile_materialized_jobs(self.root, [row])
        cta = two["avatars"]["casey_harrisson"]["assets"]["K05_cta_stories_t5"]
        self.assertTrue(cta["eligible_for_execution"])
        self.assertNotIn("parent_required_result_sha256", cta)
        cta_contract = next(c for c in bridge.build_materialized_jobs(self.root) if c["asset_id"] == "K05_cta_stories_t5")
        self.assertIsNone(cta_contract.get("parent_dependency"))
        self.assertEqual({r["role"] for r in cta_contract["references"]}, {"avatar_anchor", "shared_card_reference"})

    def test_legacy_enqueue_contract_remains_unchanged(self):
        store.DATA.mkdir(parents=True, exist_ok=True)
        project = store.create("Legacy", "")
        folder = store.folder(project["id"]); (folder / "avatars").mkdir()
        Image.new("RGB", (320, 480), "white").save(folder / "avatars" / "legacy.png")
        store.change(project["id"], imageset={"frames": [{"id": "K01", "title": "Legacy", "prompt": "legacy", "takes": []}]},
                     avatars=[{"id": "av01", "name": "Legacy", "file": "avatars/legacy.png"}])
        queued = queue.enqueue([project["id"]])
        job = queued["jobs"][0]
        self.assertNotIn("job_kind", job)
        self.assertEqual(job["frame"], "K01")
        self.assertEqual(len(queue.enqueue([project["id"]])["jobs"]), 1)

    def test_active_materialized_job_after_restart_is_preserved_not_resent(self):
        self.sync()
        snapshot = queue.load(); snapshot["running"] = True; snapshot["jobs"][0]["status"] = "generating"
        queue.save(snapshot)
        queue.recover()
        recovered = queue.load()
        self.assertFalse(recovered["running"])
        self.assertEqual(recovered["jobs"][0]["status"], "generating")
        bridge.sync_prepared_assets(self.root)
        self.assertEqual(len(queue.load()["jobs"]), 5)
        self.assertIsNone(queue.claim())

    def test_materialized_queue_operations_are_safe_and_review_requires_explicit_decision(self):
        self.sync(); job = queue.load()["jobs"][0]
        with self.assertRaisesRegex(ValueError, "não está habilitado"):
            queue.update(job["id"], "preparing")
        with self.assertRaisesRegex(ValueError, "não está habilitado"):
            queue.reference(job["id"], "avatar_anchor")
        with self.assertRaisesRegex(ValueError, "não está habilitado"):
            queue.receive(job["id"], self.image())
        snapshot = queue.load(); target = next(j for j in snapshot["jobs"] if j["id"] == job["id"])
        target.update(execution_ready=True, activation_preflight_id="receipt", tab_id=77, window_id=7,
                      preflight_url="https://chatgpt.com/", authorized_extension_session_id="session",
                      authorized_target={"tab_id": 77, "window_id": 7, "url": "https://chatgpt.com/", "extension_session_id": "session", "preflight_id": "receipt"})
        queue.save(snapshot); queue.control(True)
        claimed = queue.claim(); self.assertEqual(claimed["id"], job["id"])
        queue.update(job["id"], "attention", tab_id=77, error="interrupted")
        queue.recover_job(job["id"], "inspect")
        done = queue.receive(job["id"], self.image())
        self.assertEqual(done["status"], "done"); self.assertEqual(done["review_status"], "pending")
        approved = queue.review(job["id"], "approve")
        self.assertEqual(next(j for j in approved["jobs"] if j["id"] == job["id"])["review_status"], "approved")

    def test_legacy_and_materialized_jobs_coexist_and_clear_by_scope(self):
        self.sync(); store.DATA.mkdir(parents=True, exist_ok=True); project = store.create("Legacy coexist", "")
        folder = store.folder(project["id"]); (folder / "avatars").mkdir()
        Image.new("RGB", (320, 480), "white").save(folder / "avatars" / "legacy.png")
        store.change(project["id"], imageset={"frames": [{"id": "K01", "title": "Legacy", "prompt": "legacy", "takes": []}]},
                     avatars=[{"id": "av01", "name": "Legacy", "file": "avatars/legacy.png"}])
        queue.enqueue([project["id"]]); self.assertTrue(queue.has_jobs(project["id"])); self.assertTrue(queue.has_jobs("sexta_pessoa"))
        self.assertEqual(len(queue.load()["jobs"]), 6)
        queue.clear("sexta_pessoa")
        remaining = queue.load()["jobs"]
        self.assertEqual(len(remaining), 1); self.assertEqual(remaining[0]["project"], project["id"])

    def test_single_asset_sync_and_activation_require_exact_job_and_fingerprint(self):
        result = bridge.sync_one_asset(self.root, "K01_hook_card_pull_camera")
        self.assertEqual(len(result["queue"]["jobs"]), 1)
        job = result["queue"]["jobs"][0]
        self.assertFalse(job["execution_ready"])
        with self.assertRaisesRegex(ValueError, "Fingerprint mudou"):
            queue.activate_materialized(job["id"], "wrong", "missing", {})
        receipt = queue.register_preflight(self.preflight(job))
        activated = queue.activate_materialized(job["id"], job["canonical_asset_fingerprint"], receipt["preflight_id"], self.preflight(job))
        active = activated["jobs"][0]
        self.assertTrue(active["execution_ready"])
        self.assertEqual(active["activation_fingerprint"], job["canonical_asset_fingerprint"])
        self.assertEqual(active["authorized_target"]["preflight_id"], receipt["preflight_id"])
        self.assertEqual(next(p for p in activated["preflights"] if p["preflight_id"] == receipt["preflight_id"])["status"], "consumed")
        self.assertEqual({j["asset_id"] for j in activated["jobs"]}, {"K01_hook_card_pull_camera"})

    def test_preflight_is_bound_to_exact_tab_session_fingerprint_and_single_use(self):
        job = bridge.sync_one_asset(self.root, "K01_hook_card_pull_camera")["queue"]["jobs"][0]
        receipt = queue.register_preflight(self.preflight(job))
        wrong_tab = self.preflight(job, tab_id=102)
        with self.assertRaisesRegex(ValueError, "não corresponde"):
            queue.activate_materialized(job["id"], job["canonical_asset_fingerprint"], receipt["preflight_id"], wrong_tab)
        self.assertEqual(queue.load()["jobs"][0]["execution_ready"], False)
        self.assertEqual(queue.load()["preflights"][0]["status"], "invalidated")

    def test_preflight_revalidation_rejects_dirty_tab_and_session_restart(self):
        job = bridge.sync_one_asset(self.root, "K01_hook_card_pull_camera")["queue"]["jobs"][0]
        receipt = queue.register_preflight(self.preflight(job))
        with self.assertRaisesRegex(ValueError, "falhou"):
            queue.activate_materialized(job["id"], job["canonical_asset_fingerprint"], receipt["preflight_id"], self.preflight(job, draft_empty=False))
        self.assertFalse(queue.load()["jobs"][0]["execution_ready"])
        receipt = queue.register_preflight(self.preflight(job))
        queue.heartbeat("session-0000000002")
        with self.assertRaisesRegex(ValueError, "não utilizável"):
            queue.activate_materialized(job["id"], job["canonical_asset_fingerprint"], receipt["preflight_id"], self.preflight(job))

    def test_preflight_fingerprint_change_and_consumed_receipt_cannot_activate_again(self):
        job = bridge.sync_one_asset(self.root, "K01_hook_card_pull_camera")["queue"]["jobs"][0]
        receipt = queue.register_preflight(self.preflight(job))
        with self.assertRaisesRegex(ValueError, "Fingerprint mudou"):
            queue.activate_materialized(job["id"], "0" * 64, receipt["preflight_id"], self.preflight(job, canonical_asset_fingerprint="0" * 64))
        receipt = queue.register_preflight(self.preflight(job))
        queue.activate_materialized(job["id"], job["canonical_asset_fingerprint"], receipt["preflight_id"], self.preflight(job))
        with self.assertRaisesRegex(ValueError, "novo e não ativado"):
            queue.activate_materialized(job["id"], job["canonical_asset_fingerprint"], receipt["preflight_id"], self.preflight(job))

    def test_preflight_request_is_idempotent_and_never_enables_or_claims_job(self):
        job = bridge.sync_one_asset(self.root, "K01_hook_card_pull_camera")["queue"]["jobs"][0]
        first = queue.request_preflight(job["id"], job["canonical_asset_fingerprint"])
        second = queue.request_preflight(job["id"], job["canonical_asset_fingerprint"])
        self.assertEqual(first["request_id"], second["request_id"])
        self.assertEqual(first["status"], "requested")
        self.assertFalse(queue.get_job(job["id"])["execution_ready"])
        queue.control(True); self.assertIsNone(queue.claim())

    def test_preflight_request_success_and_failure_do_not_change_execution_state(self):
        job = bridge.sync_one_asset(self.root, "K01_hook_card_pull_camera")["queue"]["jobs"][0]
        request = queue.request_preflight(job["id"], job["canonical_asset_fingerprint"])
        queue.mark_preflight_checking(request["request_id"], job["id"], job["canonical_asset_fingerprint"], "session-0000000001")
        receipt = queue.register_preflight(self.preflight(job))
        row = next(r for r in queue.load()["preflight_requests"] if r["request_id"] == request["request_id"])
        self.assertEqual(row["status"], "ready"); self.assertEqual(row["preflight_id"], receipt["preflight_id"])
        self.assertFalse(queue.get_job(job["id"])["execution_ready"])
        state_snapshot = queue.load(); state_snapshot["preflight_requests"][0]["status"] = "expired"; queue.save(state_snapshot)
        failed = queue.request_preflight(job["id"], job["canonical_asset_fingerprint"])
        queue.mark_preflight_checking(failed["request_id"], job["id"], job["canonical_asset_fingerprint"], "session-0000000001")
        queue.fail_preflight_request(failed["request_id"], "session-0000000001", "ambiguidade de abas")
        self.assertEqual(next(r for r in queue.load()["preflight_requests"] if r["request_id"] == failed["request_id"])["status"], "failed")
        self.assertFalse(queue.get_job(job["id"])["execution_ready"])

    def test_preflight_request_fingerprint_change_expires_old_request_and_session_restart_expires_ready(self):
        job = bridge.sync_one_asset(self.root, "K01_hook_card_pull_camera")["queue"]["jobs"][0]
        request = queue.request_preflight(job["id"], job["canonical_asset_fingerprint"])
        queue.mark_preflight_checking(request["request_id"], job["id"], job["canonical_asset_fingerprint"], "session-0000000001")
        queue.register_preflight(self.preflight(job))
        queue.heartbeat("session-0000000002")
        row = next(r for r in queue.load()["preflight_requests"] if r["request_id"] == request["request_id"])
        self.assertEqual(row["status"], "expired")
        with self.assertRaisesRegex(ValueError, "Fingerprint mudou"):
            queue.request_preflight(job["id"], "0" * 64)
        self.assertFalse(queue.get_job(job["id"])["execution_ready"])

    def test_extension_restart_requeues_same_interrupted_preflight_request(self):
        job = bridge.sync_one_asset(self.root, "K01_hook_card_pull_camera")["queue"]["jobs"][0]
        request = queue.request_preflight(job["id"], job["canonical_asset_fingerprint"])
        queue.mark_preflight_checking(request["request_id"], job["id"], job["canonical_asset_fingerprint"], "session-0000000001")
        queue.heartbeat("session-0000000002")
        row = next(r for r in queue.load()["preflight_requests"] if r["request_id"] == request["request_id"])
        self.assertEqual(row["status"], "requested")
        self.assertEqual(row["request_id"], request["request_id"])
        self.assertFalse(queue.get_job(job["id"])["execution_ready"])


if __name__ == "__main__":
    unittest.main()
