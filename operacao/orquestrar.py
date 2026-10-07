"""Prepara contexto verificável e registra revisão; não executa nem aprova produção."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]

def digest(path: Path) -> str:
    sha = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            sha.update(block)
    return sha.hexdigest()

def load_angles():
    return json.loads((ROOT / "operacao/angulos.json").read_text(encoding="utf-8"))["angles"]

def resolve_angle(value):
    key = value.casefold().strip()
    for angle in load_angles():
        if key in [str(x).casefold() for x in [angle["id"], angle["slug"], angle["name"], *angle["aliases"]]]:
            return angle
        if key in [x.casefold() for x in angle.get("historical_aliases", [])]:
            raise ValueError(f"{value} é histórico. Declare a oferta atual ou uma análise histórica explícita.")
    raise ValueError("Ângulo desconhecido. Use sea-moss, fitwell, auraly ou body-hacks.")

def production_snapshot(production: Path | None):
    if production is None:
        return {}
    return {
        str(p.resolve()): digest(p)
        for p in sorted(production.rglob("*"))
        if p.is_file()
        and not any(part.startswith(".") or part in {"storage", "__pycache__"}
                    for part in p.relative_to(production).parts)
    }

def checkpoint_fields(path):
    text = path.read_text(encoding="utf-8")
    result = {}
    for key in ("Angle", "Current stage", "Next action", "Objective", "Round", "Source"):
        match = re.search(r"^\s*" + re.escape(key) + r":\s*(.+)$", text, re.M | re.I)
        if match:
            result[key] = match.group(1).strip()
    return result

def prepare(angle_value, task, production=None, out=None, artifacts=None):
    angle = resolve_angle(angle_value)
    prod = None
    if production:
        prod = Path(production).expanduser()
        prod = (prod if prod.is_absolute() else ROOT / prod).resolve()
        if not prod.is_dir():
            raise ValueError(f"Pasta de produção ausente: {prod}")
        if not prod.is_relative_to((ROOT / "producao").resolve()) or prod == (ROOT / "producao").resolve():
            raise ValueError("A produção deve ser uma pasta individual em producao/.")
    cp = prod / "CHECKPOINT.md" if prod else None
    state = checkpoint_fields(cp) if cp and cp.is_file() else {}
    if state:
        declared = re.search(r"\b([1-4])\b", state.get("Angle", ""))
        if declared and declared.group(1) != angle["id"]:
            raise ValueError("O ângulo informado conflita com o CHECKPOINT. Não misture produções.")
        if not state.get("Current stage") or not state.get("Next action"):
            raise ValueError("CHECKPOINT sem Current stage/Next action: regularize os fatos antes de executar.")
    if angle["id"] == "3" and prod and not state:
        raise ValueError("Produção Auraly sem CHECKPOINT: registre o intake primeiro, sem inventar aprovações.")
    sources = [ROOT / "AGENTS.md", ROOT / angle["canonical_router"], ROOT / "operacao/schema_revisao.json",
               ROOT / "operacao/angulos.json", ROOT / ".agents/skills/revisar-producao/SKILL.md",
               ROOT / ".codex/agents/bala-revisor.toml"]
    if task in {"adaptar", "revisar"}:
        sources += [ROOT / path for path in angle["doctrine"]]
        sources += [ROOT / "GATE_VISUAL.md", ROOT / "PERFIL_ORGANICO.md",
                    ROOT / "producao/_flow/INSTRUCOES_AGENTE_FLOW.md"]
    if cp and cp.is_file():
        sources.append(cp)
    # Mantém os caminhos, não despeja todos os playbooks em cada subagente.
    sources = list(dict.fromkeys(sources))
    missing = [str(p) for p in sources if not p.is_file()]
    if missing:
        raise ValueError("Fontes canônicas ausentes: " + ", ".join(missing))
    deliverables = [Path(p).expanduser().resolve() for p in (artifacts or [])]
    if any(not p.is_file() for p in deliverables):
        raise ValueError("Todo --artifact deve apontar para um arquivo existente.")
    task_id = str(uuid.uuid4())
    target = Path(out).expanduser().resolve() if out else ROOT / "operacao/execucoes" / (
        datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + angle["slug"] + "-" + task_id[:8])
    if target.exists() and any(target.iterdir()):
        raise ValueError(f"Saída ocupada: {target}. Use pasta nova para preservar a execução anterior.")
    target.mkdir(parents=True, exist_ok=True)
    role = "bala-pesquisador" if task in {"minerar", "watch"} else "bala-produtor"
    if task == "revisar":
        role = "bala-revisor"
    pack = {
        "version": 1, "task_id": task_id, "created_at": datetime.now(timezone.utc).isoformat(),
        "repo_root": str(ROOT), "angle": angle, "task": task, "worker": role,
        "reviewer": "bala-revisor", "production": str(prod) if prod else None,
        "current_stage": state.get("Current stage"), "next_action": state.get("Next action"),
        "checkpoint": str(cp) if cp and cp.is_file() else None,
        "routing_state": "READY" if task in {"minerar", "revisar"} or state else "NEEDS_INTAKE",
        "reference_fingerprints": {str(p): digest(p) for p in sources},
        "production_fingerprints": production_snapshot(prod),
        "deliverable_fingerprints": {str(p): digest(p) for p in deliverables},
        "review_schema": str(ROOT / "operacao/schema_revisao.json"),
        "approval_boundary": "Revisão técnica não aprova roteiro, seleção, publicação ou merge.",
    }
    (target / "TASK.json").write_text(json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    instructions = (
        f"# Execução {task_id}\n\nÂngulo: {angle['name']}\nTarefa: {task}\n"
        f"Especialista: {role}\nRevisor independente: bala-revisor\n\n"
        "Leia AGENTS.md e siga o roteador canônico. Abra somente os artefatos necessários à etapa.\n"
        f"Current stage: {pack['current_stage'] or 'não registrado'}\n"
        f"Next action: {pack['next_action'] or 'registrar entradas e estado antes de adaptar'}\n\n"
        "Use as ferramentas do Codex para delegar; este CLI prepara contexto, não chama um modelo.\n"
        "Depois da autoria, prepare TASK novo para revisar a versão final. O revisor recebe as fontes e\n"
        "a entrega, avalia os fatos e retorna JSON conforme o schema, sem editar os arquivos.\n"
        "O orquestrador registra o JSON com registrar-revisao e confere a cobertura antes de entregar.\n"
        "Se houver falha, corrigir e revisar novamente os arquivos finais; jamais reutilizar parecer stale.\n"
        "A aprovação de roteiro permanece com Luigi. Nenhuma ação no Flow é executada por este CLI.\n"
    )
    (target / "DISPATCH.md").write_text(instructions, encoding="utf-8")
    return target / "TASK.json"

def register_review(task_path, review_path, out=None):
    task_path, review_path = Path(task_path).resolve(), Path(review_path).resolve()
    pack = json.loads(task_path.read_text(encoding="utf-8"))
    review = json.loads(review_path.read_text(encoding="utf-8"))
    if review.get("task_id") != pack["task_id"] or review.get("reviewer") != "bala-revisor" or review.get("independent") is not True:
        raise ValueError("Parecer não identifica esta tarefa e um revisor independente.")
    status = review.get("status")
    if status not in {"APPROVED", "CHANGES_REQUIRED", "INCOMPLETE"}:
        raise ValueError("Status de revisão inválido.")
    checks, findings = review.get("checks"), review.get("findings")
    if not isinstance(checks, list) or not checks or not isinstance(findings, list):
        raise ValueError("Parecer exige checks com evidência e findings.")
    for check in checks:
        if not isinstance(check, dict) or check.get("result") not in {"PASS", "FAIL", "UNKNOWN", "NOT_APPLICABLE"} or not check.get("name") or not check.get("evidence"):
            raise ValueError("Check sem resultado/evidência verificável.")
    for finding in findings:
        if not isinstance(finding, dict) or finding.get("severity") not in {"BLOCKER", "WARNING"} or not finding.get("message") or not finding.get("evidence"):
            raise ValueError("Achado sem severidade/mensagem/evidência.")
    if status == "APPROVED" and (any(c["result"] in {"FAIL", "UNKNOWN"} for c in checks) or any(f["severity"] == "BLOCKER" for f in findings)):
        raise ValueError("APPROVED conflita com falha, incerteza ou achado bloqueante.")
    if status == "APPROVED" and not pack["production_fingerprints"] and not pack.get("deliverable_fingerprints"):
        raise ValueError("Sem artefatos da entrega. Prepare a revisão final com --production ou --artifact.")
    for path, original in pack["reference_fingerprints"].items():
        if not Path(path).is_file() or digest(Path(path)) != original:
            raise ValueError(f"Fonte mudou desde o preparo. Refaça a revisão: {path}")
    current = production_snapshot(Path(pack["production"]) if pack.get("production") else None)
    if current != pack["production_fingerprints"]:
        raise ValueError("Artefatos mudaram desde o preparo. Refaça a revisão da versão final.")
    for path, original in pack.get("deliverable_fingerprints", {}).items():
        if not Path(path).is_file() or digest(Path(path)) != original:
            raise ValueError(f"Entrega mudou desde o preparo. Refaça a revisão: {path}")
    target = Path(out).resolve() if out else task_path.parent / "REVISAO_REGISTRADA.json"
    if target.exists():
        raise ValueError("Parecer já registrado nesse destino. Preserve o histórico usando tarefa nova.")
    record = dict(review, registered_at=datetime.now(timezone.utc).isoformat(), taskpack_sha256=digest(task_path),
                  artifacts_unchanged=True, user_script_approval_granted=False)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return target, status

def preflight():
    packages = ["faster-whisper", "whisperx", "torch", "torchaudio", "Pillow", "av", "crawlee", "httpx2"]
    versions = {}
    missing = []
    for package in packages:
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            missing.append(package)
    binaries = {x: shutil.which(x) for x in ("ffmpeg", "ffprobe")}
    missing += [key for key, val in binaries.items() if not val]
    result = {"status": "READY" if not missing else "MISSING_DEPENDENCIES", "python": sys.version.split()[0],
              "runtime": sys.executable, "versions": versions, "binaries": binaries, "missing": missing,
              "models": "Faster-Whisper small.en e alinhador inglês são baixados/cacheados no primeiro uso.",
              "coverage": "Verifica dependências instaladas; a execução real é validada pelo /watch e pelo Crawlee."}
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("preparar")
    prep.add_argument("--angle", required=True)
    prep.add_argument("--task", required=True, choices=["minerar", "watch", "adaptar", "revisar"])
    prep.add_argument("--production")
    prep.add_argument("--out")
    prep.add_argument("--artifact", action="append", default=[], help="Entrega a revisar; repetível, aceita imagem/manifest/relatório.")
    sub.add_parser("preflight")
    rev = sub.add_parser("registrar-revisao")
    rev.add_argument("--taskpack", required=True)
    rev.add_argument("--review", required=True)
    rev.add_argument("--out")
    args = parser.parse_args()
    try:
        if args.command == "preparar":
            print(prepare(args.angle, args.task, args.production, args.out, args.artifact))
        elif args.command == "registrar-revisao":
            path, status = register_review(args.taskpack, args.review, args.out)
            print(json.dumps({"path": str(path), "status": status}, ensure_ascii=False))
            return 0 if status == "APPROVED" else 1
        else:
            result = preflight()
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0 if result["status"] == "READY" else 2
    except (ValueError, KeyError, OSError, TypeError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        return 2
    return 0

if __name__ == "__main__":
    sys.exit(main())
