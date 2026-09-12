import json
import tempfile
import unittest
from pathlib import Path

from . import pipeline_state as state


def base_state(root: Path):
    return {
        "schema_version": 1,
        "pipeline": "auraly_soulmate",
        "angle": 3,
        "production": {"id": "test", "title": "Test", "root": str(root), "created_at": None, "updated_at": None},
        "workflow": {"stage": "hooks_awaiting_choice", "next_action": "await_hook_selection", "current_avatar_id": "casey", "blocked_by": None},
        "inputs": {"video": {"path": None, "sha256": None}, "avatars": []},
        "artifacts": {},
        "approvals": {},
        "hooks": {"status": "unknown", "selected_ids": [], "no_hooks_explicitly_authorized": False},
        "avatar_queue": {"order": ["casey"], "current_index": 0},
        "avatars": {"casey": {"stage": "queued", "assets": {}}},
        "unknowns": [],
        "inconsistencies": [],
        "history": [],
    }


class PipelineStateTests(unittest.TestCase):
    def _ready_casey_state(self, root: Path):
        script = root / "ROTEIRO.md"
        script.write_text("current script", encoding="utf-8")
        package_file = root / "PROMPTS.v2.md"
        selection_hash = "selection-hash"
        sections = []
        for asset_id in (
            "K01_hook_card_pull_camera", "K02_hook_salt_circle_closing",
            "K03_hook_honey_over_card", "K04_body_reading_t2_t4", "K05_cta_stories_t5",
        ):
            sections.append(f"## {asset_id} · test\n```json\n{{\"shot_id\": \"{asset_id}\"}}\n```")
        metadata = {
            "version": 2,
            "source_script": {"sha256": state.sha256_file(script)},
            "hook_selection": {"sha256": selection_hash},
        }
        package_file.write_text(
            "```json\n" + json.dumps(metadata) + "\n```\n\n" + "\n\n".join(sections),
            encoding="utf-8",
        )
        anchor = root / "casey.jpeg"
        anchor.write_bytes(b"casey anchor")
        card = root / "REF-CARTA.png"
        card.write_bytes(b"approved card")
        payload = base_state(root)
        payload["workflow"].update({"stage": "image_prompts_ready", "next_action": "prepare_current_avatar"})
        payload["artifacts"].update({
            "script": {"path": "ROTEIRO.md", "exists": True, "sha256": state.sha256_file(script), "kind": "script"},
            "image_prompts_current": {
                "path": "PROMPTS.v2.md", "exists": True, "sha256": state.sha256_file(package_file),
                "kind": "image_prompt_package", "version": 2, "hook_selection_sha256": selection_hash,
            },
            "shared_card_reference": {"path": "REF-CARTA.png", "exists": True, "sha256": state.sha256_file(card), "kind": "reference"},
        })
        payload["approvals"]["shared_card_reference"] = {
            "status": "approved", "approved_sha256": state.sha256_file(card),
        }
        payload["avatars"]["casey"].update({
            "anchor_path": str(anchor), "anchor_sha256": state.sha256_file(anchor),
        })
        return payload

    def test_status_round_trip_and_next_action(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            payload = base_state(root)
            state.save(payload, root)
            loaded = state.load(root)
            self.assertEqual(loaded["pipeline"], "auraly_soulmate")
            self.assertEqual(state.next_action(loaded), "await_hook_selection")

    def test_hooks_require_one_selection_only_when_approved(self):
        with tempfile.TemporaryDirectory() as temp:
            payload = base_state(Path(temp))
            payload["hooks"]["status"] = "approved"
            with self.assertRaises(state.PipelineStateError):
                state.validate(payload)
            payload["hooks"]["selected_ids"] = ["H99"]
            state.validate(payload)
            payload["hooks"]["selected_ids"] = list(range(100))
            state.validate(payload)

    def test_user_explicit_hook_can_have_no_original_option_id(self):
        with tempfile.TemporaryDirectory() as temp:
            payload = base_state(Path(temp))
            payload["hooks"] = {
                "status": "approved",
                "selected_ids": ["user_explicit_card_pull"],
                "selected_hooks": [{
                    "selection_id": "user_explicit_card_pull",
                    "title": "Carta puxada rapidamente para a câmera.",
                    "origin": "user_explicit",
                    "original_option_id": None,
                    "original_option_title": None,
                }],
                "no_hooks_explicitly_authorized": False,
            }
            state.validate(payload)
            payload["workflow"]["stage"] = "hooks_approved"
            self.assertEqual(state.next_action(payload), "build_image_prompts")

    def test_ready_image_prompts_prepare_the_current_avatar(self):
        with tempfile.TemporaryDirectory() as temp:
            payload = base_state(Path(temp))
            payload["workflow"]["stage"] = "image_prompts_ready"
            self.assertEqual(state.next_action(payload), "prepare_current_avatar")

    def test_reconcile_blocks_hash_mismatch_without_guessing_stage(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            artifact = root / "ROTEIRO.md"
            artifact.write_text("v1", encoding="utf-8")
            payload = base_state(root)
            payload["artifacts"]["script"] = {
                "path": "ROTEIRO.md", "exists": True,
                "sha256": state.sha256_file(artifact), "kind": "script",
            }
            state.save(payload, root)
            artifact.write_text("v2", encoding="utf-8")
            reconciled = state.reconcile(root)
            self.assertEqual(reconciled["workflow"]["stage"], "hooks_awaiting_choice")
            self.assertEqual(reconciled["workflow"]["next_action"], "resolve_inconsistency")
            self.assertEqual(reconciled["inconsistencies"][0]["code"], "artifact_hash_mismatch")

    def test_shared_card_approval_is_invalidated_when_its_hash_changes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            card = root / "REF-CARTA.png"
            card.write_bytes(b"hash A")
            approved_hash = state.sha256_file(card)
            payload = base_state(root)
            payload["workflow"].update({
                "stage": "image_prompts_ready",
                "next_action": "prepare_current_avatar",
            })
            payload["artifacts"]["shared_card_reference"] = {
                "path": "REF-CARTA.png", "exists": True,
                "sha256": approved_hash, "kind": "reference",
                "approval_status": "approved",
                "approved_sha256": approved_hash,
            }
            payload["approvals"]["shared_card_reference"] = {
                "status": "approved",
                "approved_sha256": approved_hash,
                "valid_only_if_artifact_sha256_matches": True,
            }
            state.save(payload, root)

            card.write_bytes(b"hash B")
            self.assertNotEqual(approved_hash, state.sha256_file(card))

            reconciled = state.reconcile(root)
            approval = reconciled["approvals"]["shared_card_reference"]
            self.assertEqual(approval["status"], "invalidated_hash_mismatch")
            self.assertEqual(reconciled["artifacts"]["shared_card_reference"]["approval_status"], "invalidated_hash_mismatch")
            self.assertEqual(reconciled["workflow"]["stage"], "image_prompts_ready")
            self.assertEqual(reconciled["workflow"]["blocked_by"], "shared_card_reference_approval_hash_mismatch")
            self.assertEqual(reconciled["workflow"]["next_action"], "await_shared_card_reference_reapproval")

    def test_prepare_current_avatar_records_five_assets_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            payload = self._ready_casey_state(root)
            state.save(payload, root)

            prepared = state.prepare_current_avatar(root)
            assets = prepared["avatars"]["casey"]["assets"]
            self.assertEqual(prepared["avatars"]["casey"]["stage"], "preparing_images")
            self.assertEqual(prepared["workflow"]["stage"], "processing_avatar_queue")
            self.assertEqual(prepared["workflow"]["next_action"], "execute_eligible_current_avatar_assets")
            self.assertEqual(set(assets), {
                "K01_hook_card_pull_camera", "K02_hook_salt_circle_closing",
                "K03_hook_honey_over_card", "K04_body_reading_t2_t4", "K05_cta_stories_t5",
            })
            self.assertTrue(all(assets[key]["eligible_for_execution"] for key in assets))
            self.assertIsNone(assets["K05_cta_stories_t5"]["parent_asset"])
            self.assertIsNone(assets["K05_cta_stories_t5"]["parent_required_status"])
            self.assertTrue(all(asset["status"] == "pending" and asset["attempt_count"] == 0 for asset in assets.values()))

            history_count = len(prepared["history"])
            repeated = state.prepare_current_avatar(root)
            self.assertEqual(repeated["avatars"]["casey"]["assets"], assets)
            self.assertEqual(len(repeated["history"]), history_count)

    def test_prepare_reads_declared_n_plus_two_assets_without_card_reference(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            script = root / "ROTEIRO.md"
            script.write_text("script", encoding="utf-8")
            anchor = root / "anchor.jpeg"
            anchor.write_bytes(b"anchor")
            definitions = [
                {"asset_id": f"K0{i}_hook_{i}", "role": "hook", "reference_roles": ["avatar_anchor"]}
                for i in range(1, 6)
            ] + [
                {"asset_id": "K06_body", "role": "body", "reference_roles": ["avatar_anchor"]},
                {"asset_id": "K07_cta", "role": "cta", "reference_roles": ["avatar_anchor"]},
            ]
            selection_hash = "selected-five-hooks"
            metadata = {
                "version": 3,
                "source_script": {"sha256": state.sha256_file(script)},
                "hook_selection": {"sha256": selection_hash},
                "assets": definitions,
            }
            package = root / "PROMPTS.md"
            sections = [f"## {row['asset_id']} · test\n```json\n{{\"shot_id\": \"{row['asset_id']}\"}}\n```" for row in definitions]
            package.write_text("```json\n" + json.dumps(metadata) + "\n```\n\n" + "\n\n".join(sections), encoding="utf-8")
            payload = base_state(root)
            payload["workflow"].update({"stage": "image_prompts_ready", "next_action": "prepare_current_avatar"})
            payload["artifacts"].update({
                "script": {"path": "ROTEIRO.md", "exists": True, "sha256": state.sha256_file(script), "kind": "script"},
                "image_prompts_current": {"path": "PROMPTS.md", "exists": True, "sha256": state.sha256_file(package), "kind": "image_prompt_package", "version": 3, "hook_selection_sha256": selection_hash},
            })
            payload["avatars"]["casey"].update({"anchor_path": str(anchor), "anchor_sha256": state.sha256_file(anchor)})
            state.save(payload, root)

            prepared = state.prepare_current_avatar(root)
            assets = prepared["avatars"]["casey"]["assets"]
            self.assertEqual(set(assets), {row["asset_id"] for row in definitions})
            self.assertTrue(all(asset["shared_card_reference_sha256"] is None for asset in assets.values()))
            self.assertTrue(all(asset["eligible_for_execution"] for asset in assets.values()))

    def test_reconcile_marks_only_prepared_avatar_assets_stale_when_anchor_changes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            payload = self._ready_casey_state(root)
            state.save(payload, root)
            state.prepare_current_avatar(root)
            anchor = Path(payload["avatars"]["casey"]["anchor_path"])
            anchor.write_bytes(b"changed anchor")

            reconciled = state.reconcile(root)
            assets = reconciled["avatars"]["casey"]["assets"]
            self.assertTrue(all(asset["status"] == "stale" for asset in assets.values()))
            self.assertTrue(all("anchor_sha256_mismatch" in asset["stale_reasons"] for asset in assets.values()))
            self.assertEqual(reconciled["workflow"]["blocked_by"], "prepared_assets_stale")
            self.assertEqual(reconciled["workflow"]["next_action"], "reprepare_current_avatar")

    def test_migration_keeps_unknown_decisions_unknown(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "sexta_pessoa"
            (root / "watch").mkdir(parents=True)
            (root / "pacote_browser" / "casey_harrisson").mkdir(parents=True)
            for avatar in ("kris_walker", "shelby_turner", "kelly_bennett", "robin_matthews"):
                (root / "pacote_browser" / avatar).mkdir(parents=True)
            (root / "watch" / "manifest.json").write_text("{}", encoding="utf-8")
            (root / "watch" / "transcript.txt").write_text("hello", encoding="utf-8")
            (root / "ROTEIRO.md").write_text("pipeline: auraly", encoding="utf-8")
            (root / "GANCHOS_VISUAIS.md").write_text("Roteiro aprovado.", encoding="utf-8")
            (root / "PROMPTS_IMAGEM.md").write_text("draft", encoding="utf-8")
            (root / "pacote_browser" / "_LEIA_PRIMEIRO.md").write_text(
                "Escolher o primeiro avatar (`casey_harrisson`). Repetir para `kris_walker`, `shelby_turner`, `kelly_bennett`, `robin_matthews`.",
                encoding="utf-8",
            )
            migrated = state.migrate_sexta_pessoa(root)
            self.assertEqual(migrated["workflow"]["stage"], "hooks_awaiting_choice")
            self.assertEqual(migrated["workflow"]["current_avatar_id"], "casey_harrisson")
            self.assertEqual(migrated["avatar_queue"]["order"], ["casey_harrisson", "kris_walker", "shelby_turner", "kelly_bennett", "robin_matthews"])
            self.assertEqual(migrated["hooks"]["status"], "unknown")
            self.assertEqual(migrated["avatars"]["casey_harrisson"]["assets"], {})
            self.assertTrue((root / state.STATUS_FILENAME).is_file())


if __name__ == "__main__":
    unittest.main()
