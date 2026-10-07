"""Regressões dos limites de contexto, estado e parecer independente."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from operacao import orquestrar as op


class Orchestration(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for source in ("AGENTS.md", "CLAUDE.md", "WORKFLOW_AURALY.md", "GATE_VISUAL.md", "PERFIL_ORGANICO.md",
                       "producao/_flow/INSTRUCOES_AGENTE_FLOW.md", ".agents/skills/revisar-producao/SKILL.md",
                       ".codex/agents/bala-revisor.toml", "operacao/schema_revisao.json"):
            path = self.root / source
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("Fixture: " + source)
        (self.root / "operacao/angulos.json").write_text((op.ROOT / "operacao/angulos.json").read_text())
        for angle in op.load_angles():
            for source in angle["doctrine"]:
                path = self.root / source
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("Fixture doctrine")
        self.root_patch = patch.object(op, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.production = self.root / "producao/example"
        self.production.mkdir(parents=True)

    def checkpoint(self, angle="3"):
        path = self.production / "CHECKPOINT.md"
        path.write_text(f"Angle: {angle}\nCurrent stage: WAITING_SCRIPT_APPROVAL\nNext action: Wait for Luigi.\n")
        return path

    def review(self, pack, **overrides):
        task = json.loads(pack.read_text())
        data = {"task_id": task["task_id"], "reviewer": "bala-revisor", "independent": True,
                "status": "APPROVED", "checks": [{"name": "Fixture check", "result": "PASS", "evidence": "example.txt:1"}], "findings": []}
        data.update(overrides)
        path = pack.parent / "parecer.json"
        path.write_text(json.dumps(data))
        return path

    def test_angles_aliases_and_historical_offer(self):
        self.assertEqual(op.resolve_angle("FityWell")["id"], "2")
        self.assertEqual(op.resolve_angle("sea moss gummies")["id"], "1")
        self.assertEqual(op.resolve_angle("body-hacks")["id"], "4")
        with self.assertRaisesRegex(ValueError, "histórico"):
            op.resolve_angle("Korella")

    def test_never_advances_waiting_checkpoint(self):
        cp = self.checkpoint()
        original = cp.read_bytes()
        pack = op.prepare("auraly", "adaptar", str(self.production))
        self.assertEqual(json.loads(pack.read_text())["current_stage"], "WAITING_SCRIPT_APPROVAL")
        op.register_review(pack, self.review(pack))
        self.assertEqual(cp.read_bytes(), original)
        record = json.loads((pack.parent / "REVISAO_REGISTRADA.json").read_text())
        self.assertFalse(record["user_script_approval_granted"])

    def test_rejects_missing_checkpoint_cross_angle_and_broad_folder(self):
        with self.assertRaisesRegex(ValueError, "sem CHECKPOINT"):
            op.prepare("auraly", "adaptar", str(self.production))
        self.checkpoint()
        with self.assertRaisesRegex(ValueError, "conflita"):
            op.prepare("sea-moss", "adaptar", str(self.production))
        with self.assertRaisesRegex(ValueError, "individual"):
            op.prepare("auraly", "revisar", str(self.production.parent))

    def test_changed_added_or_removed_artifacts_invalidate_review(self):
        for mutation in ("change", "add", "remove"):
            with self.subTest(mutation=mutation):
                cp = self.checkpoint()
                pack = op.prepare("auraly", "revisar", str(self.production))
                review = self.review(pack)
                if mutation == "change":
                    cp.write_text(cp.read_text() + "Alterado\n")
                elif mutation == "add":
                    (self.production / "ROTEIRO.md").write_text("Novo artefato")
                else:
                    cp.unlink()
                with self.assertRaises(ValueError):
                    op.register_review(pack, review)
                for file in self.production.iterdir():
                    file.unlink()

    def test_mining_report_fingerprint_is_required_and_checked(self):
        pack = op.prepare("sea-moss", "minerar")
        with self.assertRaisesRegex(ValueError, "Sem artefatos"):
            op.register_review(pack, self.review(pack))
        deliverable = self.root / "relatorio.json"
        deliverable.write_text('{"approved":[]}')
        pack = op.prepare("sea-moss", "revisar", artifacts=[str(deliverable)])
        review = self.review(pack)
        deliverable.write_text('{"approved":["inventado"]}')
        with self.assertRaisesRegex(ValueError, "Entrega mudou"):
            op.register_review(pack, review)

    def test_visual_media_changes_invalidate_review_too(self):
        self.checkpoint()
        image = self.production / "avatar.png"
        image.write_bytes(b"fixture image before")
        pack = op.prepare("auraly", "revisar", str(self.production))
        review = self.review(pack)
        image.write_bytes(b"fixture image after")
        with self.assertRaisesRegex(ValueError, "Artefatos mudaram"):
            op.register_review(pack, review)

    def test_wrong_agent_and_unknown_check_cannot_approve(self):
        self.checkpoint()
        for override in ({"reviewer": "bala-produtor"}, {"independent": False},
                         {"checks": [{"name": "País", "result": "UNKNOWN", "evidence": "Oculto"}]},
                         {"findings": [{"severity": "BLOCKER", "message": "Sem prova", "evidence": "ref:1"}]}):
            with self.subTest(override=override):
                pack = op.prepare("auraly", "revisar", str(self.production))
                with self.assertRaises(ValueError):
                    op.register_review(pack, self.review(pack, **override))


if __name__ == "__main__":
    unittest.main()
