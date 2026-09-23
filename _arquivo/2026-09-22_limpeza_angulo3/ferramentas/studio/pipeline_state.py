"""Canonical operational state for the Angle 3 Auraly soulmate pipeline.

This module intentionally has no copy, hook-generation, browser, SQLite, or provider logic.
It owns only schema validation, atomic persistence, hashes, safe reconciliation, transitions,
and migration of filesystem evidence into a portable project status file.
"""

from __future__ import annotations

import hashlib
import json
import re
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


PIPELINE = "auraly_soulmate"
ANGLE = 3
STATUS_FILENAME = "status_pipeline_auraly_soulmate.json"

WORKFLOW_STAGES = {
    "received", "transcribing", "transcribed", "analyzing", "writing_script",
    "script_awaiting_approval", "script_approved", "generating_hook_options",
    "hooks_awaiting_choice", "hooks_approved", "building_image_prompts",
    "image_prompts_ready", "processing_avatar_queue", "completed", "failed",
}
AVATAR_STAGES = {
    "queued", "preparing_images", "generating_images", "reviewing_images",
    "awaiting_corrections", "organizing_files", "generating_video_prompts",
    "completed", "failed",
}
ASSET_STAGES = {
    "pending", "submitted", "generating", "downloaded", "review_pending",
    "approved", "rejected", "retrying", "failed", "unknown", "stale",
    "queued", "result_received", "attention",
}


class PipelineStateError(ValueError):
    """Raised when a state file is malformed or violates a hard pipeline invariant."""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _relative(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def _artifact(root: Path, path: Path | None, kind: str) -> dict[str, Any]:
    if path is None or not path.is_file():
        return {"path": None, "exists": False, "sha256": None, "kind": kind}
    return {
        "path": _relative(root, path),
        "exists": True,
        "sha256": sha256_file(path),
        "kind": kind,
        "observed_at": utc_now(),
    }


def _state_path(root: Path) -> Path:
    return root / STATUS_FILENAME


def _append_unique(records: list[dict[str, Any]], record: dict[str, Any]) -> None:
    key = (record.get("code"), record.get("path"), record.get("message"))
    if not any((item.get("code"), item.get("path"), item.get("message")) == key for item in records):
        records.append(record)


def validate(state: dict[str, Any]) -> None:
    if not isinstance(state, dict):
        raise PipelineStateError("O estado precisa ser um objeto JSON.")
    if state.get("pipeline") != PIPELINE or state.get("angle") != ANGLE:
        raise PipelineStateError("Este arquivo aceita somente angle=3 e pipeline=auraly_soulmate.")
    if state.get("schema_version") != 1:
        raise PipelineStateError("Versão de schema não suportada.")

    workflow = state.get("workflow")
    if not isinstance(workflow, dict) or workflow.get("stage") not in WORKFLOW_STAGES:
        raise PipelineStateError("workflow.stage inválido.")

    avatars = state.get("avatars")
    queue = state.get("avatar_queue")
    if not isinstance(avatars, dict) or not isinstance(queue, dict):
        raise PipelineStateError("avatars e avatar_queue são obrigatórios.")
    order = queue.get("order")
    if not isinstance(order, list) or len(order) != len(set(order)):
        raise PipelineStateError("avatar_queue.order precisa conter IDs únicos.")
    if any(avatar_id not in avatars for avatar_id in order):
        raise PipelineStateError("A fila referencia avatar inexistente.")
    current = workflow.get("current_avatar_id")
    if current is not None and current not in avatars:
        raise PipelineStateError("workflow.current_avatar_id referencia avatar inexistente.")

    for avatar_id, avatar in avatars.items():
        if avatar.get("stage") not in AVATAR_STAGES:
            raise PipelineStateError(f"Estágio inválido para avatar {avatar_id}.")
        for asset_id, asset in avatar.get("assets", {}).items():
            if asset.get("status") not in ASSET_STAGES:
                raise PipelineStateError(f"Status inválido para asset {avatar_id}/{asset_id}.")

    hooks = state.get("hooks", {})
    if hooks.get("status") == "approved":
        selected = hooks.get("selected_ids", [])
        selections = hooks.get("selected_hooks", [])
        no_hooks = hooks.get("no_hooks_explicitly_authorized", False)
        if not selected and not no_hooks:
            raise PipelineStateError("hooks aprovados exigem ao menos um hook, salvo autorização explícita sem hooks.")
        if selections:
            if not isinstance(selections, list):
                raise PipelineStateError("hooks.selected_hooks precisa ser uma lista.")
            selection_ids = [item.get("selection_id") for item in selections if isinstance(item, dict)]
            if len(selection_ids) != len(selections) or any(not item for item in selection_ids):
                raise PipelineStateError("Cada hook selecionado precisa de um selection_id operacional.")
            if len(selection_ids) != len(set(selection_ids)):
                raise PipelineStateError("hooks.selected_hooks possui selection_id duplicado.")
            if any(item.get("origin") not in {"artifact_option", "user_explicit"} for item in selections):
                raise PipelineStateError("A origem de cada hook precisa ser artifact_option ou user_explicit.")
            if set(selected) != set(selection_ids):
                raise PipelineStateError("selected_ids precisa refletir os selection_id de selected_hooks.")


def load(path_or_root: str | Path) -> dict[str, Any]:
    candidate = Path(path_or_root)
    path = candidate if candidate.name == STATUS_FILENAME else _state_path(candidate)
    if not path.is_file():
        raise FileNotFoundError(path)
    state = json.loads(path.read_text(encoding="utf-8"))
    validate(state)
    return state


def save(state: dict[str, Any], path_or_root: str | Path) -> Path:
    validate(state)
    candidate = Path(path_or_root)
    path = candidate if candidate.name == STATUS_FILENAME else _state_path(candidate)
    state["production"]["updated_at"] = utc_now()
    payload = json.dumps(state, ensure_ascii=False, indent=2) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)
    return path


def next_action(state: dict[str, Any]) -> str:
    if state["workflow"].get("blocked_by") == "shared_card_reference_approval_hash_mismatch":
        return "await_shared_card_reference_reapproval"
    if state["workflow"].get("blocked_by") == "prepared_assets_stale":
        return "reprepare_current_avatar"
    if state.get("inconsistencies"):
        return "resolve_inconsistency"
    stage = state["workflow"]["stage"]
    if stage == "script_awaiting_approval":
        return "await_script_approval"
    if stage == "hooks_awaiting_choice":
        return "await_hook_selection"
    if stage == "hooks_approved":
        return "build_image_prompts"
    if stage == "image_prompts_ready":
        return "prepare_current_avatar"
    if stage == "processing_avatar_queue":
        current = state["workflow"].get("current_avatar_id")
        if current is None:
            return "select_current_avatar"
        avatar = state["avatars"][current]
        if avatar["stage"] == "preparing_images":
            return "execute_eligible_current_avatar_assets"
        if avatar["stage"] == "awaiting_corrections":
            return "await_avatar_correction_decision"
        if avatar["stage"] == "reviewing_images":
            return "review_current_avatar_assets"
        return "continue_current_avatar"
    if stage == "completed":
        return "none"
    return "continue_pipeline"


def _prompt_package_metadata_and_sections(path: Path) -> tuple[dict[str, Any], dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    metadata_match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.S)
    if not metadata_match:
        raise PipelineStateError("Pacote atual de prompts não contém metadados JSON válidos.")
    metadata = json.loads(metadata_match.group(1))
    sections: dict[str, str] = {}
    pattern = re.compile(r"^## (K\d+_[^·\n]+).*?```json\s*(\{.*?\})\s*```", re.M | re.S)
    for match in pattern.finditer(text):
        asset_id = match.group(1).strip()
        sections[asset_id] = match.group(2).strip()
    return metadata, sections


def _prepared_asset_is_current(asset: dict[str, Any], expected: dict[str, Any]) -> bool:
    fields = (
        "role", "prompt_reference", "prompt_sha256", "anchor_sha256",
        "shared_card_reference_sha256", "source_prompt_package_sha256",
        "source_prompt_package_version", "source_script_sha256",
        "hook_selection_sha256", "parent_asset", "parent_required_status", "reference_roles",
    )
    return all(asset.get(field) == expected.get(field) for field in fields)


def _asset_definitions(metadata: dict[str, Any]) -> tuple[tuple[str, str, tuple[str, ...], str | None], ...]:
    """Read declared assets; packages without a manifest retain the legacy five-asset contract."""
    declared = metadata.get("assets")
    if declared is None:
        return (
            ("K01_hook_card_pull_camera", "hook", ("avatar_anchor", "shared_card_reference"), None),
            ("K02_hook_salt_circle_closing", "hook", ("avatar_anchor", "shared_card_reference"), None),
            ("K03_hook_honey_over_card", "hook", ("avatar_anchor", "shared_card_reference"), None),
            ("K04_body_reading_t2_t4", "body", ("avatar_anchor", "shared_card_reference"), None),
            ("K05_cta_stories_t5", "cta", ("avatar_anchor", "shared_card_reference"), None),
        )
    if not isinstance(declared, list) or not declared:
        raise PipelineStateError("O manifesto de assets do pacote de prompts é inválido.")
    definitions, seen = [], set()
    for item in declared:
        if not isinstance(item, dict):
            raise PipelineStateError("Cada asset declarado precisa ser um objeto.")
        asset_id, role = item.get("asset_id"), item.get("role")
        roles, parent = item.get("reference_roles", ["avatar_anchor"]), item.get("parent_asset")
        if not isinstance(asset_id, str) or not asset_id or asset_id in seen:
            raise PipelineStateError("Cada asset declarado exige asset_id único.")
        if role not in {"hook", "body", "cta"}:
            raise PipelineStateError(f"Papel inválido no manifesto de assets: {asset_id}.")
        if not isinstance(roles, list) or "avatar_anchor" not in roles or len(roles) != len(set(roles)):
            raise PipelineStateError(f"{asset_id} exige reference_roles únicos incluindo avatar_anchor.")
        if any(ref not in {"avatar_anchor", "shared_card_reference", "parent_approved_result"} for ref in roles):
            raise PipelineStateError(f"{asset_id} declara papel de referência inválido.")
        seen.add(asset_id)
        definitions.append((asset_id, role, tuple(roles), parent))
    return tuple(definitions)


def _refresh_prepared_asset_staleness(state: dict[str, Any], root: Path) -> bool:
    """Mark only assets whose recorded source hashes no longer match their inputs."""
    package = state.get("artifacts", {}).get("image_prompts_current", {})
    package_path = root / (package.get("path") or "")
    package_hash = sha256_file(package_path) if package_path.is_file() else None
    script = state.get("artifacts", {}).get("script", {})
    script_path = root / (script.get("path") or "")
    script_hash = sha256_file(script_path) if script_path.is_file() else None
    card = state.get("artifacts", {}).get("shared_card_reference", {})
    card_path = root / (card.get("path") or "")
    card_hash = sha256_file(card_path) if card_path.is_file() else None
    changed = False
    for avatar in state.get("avatars", {}).values():
        anchor_path = Path(avatar.get("anchor_path") or "")
        anchor_hash = sha256_file(anchor_path) if anchor_path.is_file() else None
        for asset in avatar.get("assets", {}).values():
            reasons = []
            if asset.get("source_prompt_package_sha256") != package_hash:
                reasons.append("source_prompt_package_sha256_mismatch")
            if asset.get("source_script_sha256") != script_hash:
                reasons.append("source_script_sha256_mismatch")
            if asset.get("hook_selection_sha256") != package.get("hook_selection_sha256"):
                reasons.append("hook_selection_sha256_mismatch")
            if asset.get("anchor_sha256") != anchor_hash:
                reasons.append("anchor_sha256_mismatch")
            if asset.get("shared_card_reference_sha256") is not None and asset.get("shared_card_reference_sha256") != card_hash:
                reasons.append("shared_card_reference_sha256_mismatch")
            parent_id = asset.get("parent_asset")
            parent = avatar.get("assets", {}).get(parent_id) if parent_id else None
            if parent and parent.get("status") == "stale":
                reasons.append("parent_asset_stale")
            if reasons:
                asset["status"] = "stale"
                asset["eligible_for_execution"] = False
                asset["stale_reasons"] = reasons
                changed = True
    return changed


def prepare_current_avatar(path_or_root: str | Path) -> dict[str, Any]:
    """Prepare deterministic image assets for the active avatar without generating media.

    This records only verified inputs and asset dependencies. Repeating the call with unchanged
    inputs returns the already-valid preparation without rewriting or duplicating it.
    """
    candidate = Path(path_or_root)
    root = candidate.parent if candidate.name == STATUS_FILENAME else candidate
    state = load(candidate)
    workflow = state["workflow"]
    if workflow.get("stage") not in {"image_prompts_ready", "processing_avatar_queue"}:
        raise PipelineStateError("prepare_current_avatar exige prompts de imagem prontos.")
    if workflow.get("blocked_by") and workflow.get("blocked_by") != "prepared_assets_stale":
        raise PipelineStateError("prepare_current_avatar não pode rodar enquanto o workflow estiver bloqueado.")
    avatar_id = workflow.get("current_avatar_id")
    if not avatar_id:
        raise PipelineStateError("Não há avatar atual para preparar.")
    avatar = state["avatars"][avatar_id]
    package = state.get("artifacts", {}).get("image_prompts_current", {})
    package_path = root / package.get("path", "")
    if not package_path.is_file() or sha256_file(package_path) != package.get("sha256"):
        raise PipelineStateError("Pacote atual de prompts não está verificável.")
    metadata, sections = _prompt_package_metadata_and_sections(package_path)
    if metadata.get("source_script", {}).get("sha256") != state["artifacts"]["script"].get("sha256"):
        raise PipelineStateError("Pacote de prompts não corresponde ao hash do roteiro atual.")
    if metadata.get("hook_selection", {}).get("sha256") != package.get("hook_selection_sha256"):
        raise PipelineStateError("Pacote de prompts não corresponde à seleção atual de hooks.")
    anchor_path = Path(avatar.get("anchor_path") or "")
    if not anchor_path.is_file() or sha256_file(anchor_path) != avatar.get("anchor_sha256"):
        raise PipelineStateError("Âncora do avatar atual não está verificável.")
    definitions = _asset_definitions(metadata)
    card = state["artifacts"].get("shared_card_reference", {})
    card_path = root / card.get("path", "")
    card_approval = state.get("approvals", {}).get("shared_card_reference", {})
    if any("shared_card_reference" in roles for _, _, roles, _ in definitions):
        if (not card_path.is_file() or sha256_file(card_path) != card.get("sha256")
                or card_approval.get("status") != "approved"
                or card_approval.get("approved_sha256") != card.get("sha256")):
            raise PipelineStateError("REF-CARTA aprovada não está verificável.")
    expected_assets: dict[str, dict[str, Any]] = {}
    for asset_id, role, reference_roles, parent in definitions:
        prompt = sections.get(asset_id)
        if prompt is None:
            raise PipelineStateError(f"Prompt ausente no pacote atual: {asset_id}.")
        expected_assets[asset_id] = {
            "asset_id": asset_id,
            "role": role,
            "prompt_reference": {"path": package["path"], "section": asset_id},
            "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
            "anchor_sha256": avatar["anchor_sha256"],
            "shared_card_reference_sha256": card["sha256"] if "shared_card_reference" in reference_roles else None,
            "source_prompt_package_sha256": package["sha256"],
            "source_prompt_package_version": package.get("version"),
            "source_script_sha256": state["artifacts"]["script"]["sha256"],
            "hook_selection_sha256": package["hook_selection_sha256"],
            "parent_asset": parent,
            "parent_required_status": "approved" if parent else None,
            "reference_roles": list(reference_roles),
        }

    existing = avatar.get("assets", {})
    if set(existing) == set(expected_assets) and all(
        _prepared_asset_is_current(existing[asset_id], expected)
        for asset_id, expected in expected_assets.items()
    ):
        return state

    avatar["assets"] = {
        asset_id: {
            **expected,
            "status": "pending",
            "attempt_count": 0,
            "current_error": None,
            "result": None,
            "local_file": None,
            "review": {"status": "pending", "reviewed_at": None},
            "eligible_for_execution": parent is None,
        }
        for asset_id, expected in expected_assets.items()
        for parent in (expected["parent_asset"],)
    }
    avatar["assets_evidence"] = "prepared_from_current_prompt_package"
    avatar["stage"] = "preparing_images"
    workflow["stage"] = "processing_avatar_queue"
    workflow["blocked_by"] = None
    workflow["next_action"] = next_action(state)
    state["history"].append({
        "at": utc_now(), "type": "avatar_prepared",
        "message": f"{avatar_id} preparado com cinco assets do pacote atual; nenhuma mídia foi gerada.",
    })
    save(state, root)
    return state


def reconcile_materialized_jobs(path_or_root: str | Path, jobs: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Reflect queue facts in canonical assets; queue statuses never imply approval by themselves."""
    candidate = Path(path_or_root)
    root = candidate.parent if candidate.name == STATUS_FILENAME else candidate
    state = load(candidate)
    changed = False
    by_fingerprint = {job.get("canonical_asset_fingerprint"): job for job in jobs
                      if job.get("job_kind") == "canonical_materialized"}
    for avatar in state.get("avatars", {}).values():
        for asset in avatar.get("assets", {}).values():
            job = by_fingerprint.get(asset.get("canonical_asset_fingerprint"))
            if not job:
                continue
            queue_status = job.get("status")
            review_status = job.get("review_status")
            if queue_status == "queued":
                target = "queued"
            elif queue_status in {"preparing", "submitting", "generating", "receiving"}:
                target = "generating"
            elif queue_status == "attention":
                target = "attention"
            elif queue_status == "done" and review_status == "approved":
                target = "approved"
            elif queue_status == "done" and review_status == "rejected":
                target = "rejected"
            elif queue_status == "done":
                target = "result_received"
            elif queue_status == "failed":
                target = "failed"
            else:
                continue
            update = {
                "queue_job_id": job.get("id"), "queue_status": queue_status,
                "status": target,
                "review": {"status": review_status or "pending", "reviewed_at": job.get("reviewed_at")},
            }
            if job.get("image_sha256"):
                update["result"] = {"image_sha256": job["image_sha256"], "job_id": job.get("id"),
                                    "local_file": job.get("local_file")}
            if any(asset.get(key) != value for key, value in update.items()):
                asset.update(update)
                changed = True
    if changed:
        state["workflow"]["next_action"] = next_action(state)
        save(state, root)
    return state


def reconcile(path_or_root: str | Path, artifact_keys: Iterable[str] | None = None) -> dict[str, Any]:
    """Safely reconcile referenced files. Ambiguity becomes a blocking inconsistency.

    This function never guesses approvals, generation state, current avatar, or a missing file's
    replacement. It only detects deterministic filesystem mismatches and recalculates next_action.
    """
    candidate = Path(path_or_root)
    root = candidate.parent if candidate.name == STATUS_FILENAME else candidate
    state = load(candidate)
    keys = set(artifact_keys) if artifact_keys is not None else set(state.get("artifacts", {}))
    state["inconsistencies"] = []

    for key in keys:
        artifact = state.get("artifacts", {}).get(key)
        if not artifact or not artifact.get("exists"):
            continue
        relative = artifact.get("path")
        if not relative:
            _append_unique(state["inconsistencies"], {
                "code": "artifact_path_missing", "path": None,
                "message": f"Artefato {key} está marcado como existente sem caminho verificável.",
            })
            continue
        target = (root / relative).resolve()
        try:
            target.relative_to(root.resolve())
        except ValueError:
            _append_unique(state["inconsistencies"], {
                "code": "artifact_path_escape", "path": relative,
                "message": f"Artefato {key} aponta fora da produção.",
            })
            continue
        if not target.is_file():
            _append_unique(state["inconsistencies"], {
                "code": "artifact_missing", "path": relative,
                "message": f"Artefato esperado não foi encontrado: {key}.",
            })
            continue
        actual = sha256_file(target)
        expected = artifact.get("sha256")
        if expected is not None and actual != expected:
            _append_unique(state["inconsistencies"], {
                "code": "artifact_hash_mismatch", "path": relative,
                "message": f"O conteúdo de {key} mudou desde a última observação.",
            })
            if key == "shared_card_reference":
                approval = state.get("approvals", {}).get("shared_card_reference")
                if isinstance(approval, dict) and approval.get("status") == "approved":
                    approval["status"] = "invalidated_hash_mismatch"
                    approval["invalidated_at"] = utc_now()
                    approval["invalidation_evidence"] = "artifact_sha256_mismatch"
                    artifact["approval_status"] = "invalidated_hash_mismatch"

    prepared_assets_stale = _refresh_prepared_asset_staleness(state, root)
    shared_card_approval = state.get("approvals", {}).get("shared_card_reference", {})
    if shared_card_approval.get("status") == "invalidated_hash_mismatch":
        state["workflow"]["blocked_by"] = "shared_card_reference_approval_hash_mismatch"
    elif prepared_assets_stale:
        state["workflow"]["blocked_by"] = "prepared_assets_stale"
    elif state["inconsistencies"]:
        state["workflow"]["blocked_by"] = "inconsistency"
    state["workflow"]["next_action"] = next_action(state)
    save(state, root)
    return state


def _parse_execution_order(readme: Path) -> list[str] | None:
    if not readme.is_file():
        return None
    text = readme.read_text(encoding="utf-8")
    match = re.search(r"Escolher o primeiro avatar \(`([^`]+)`\).*?Repetir para `([^`]+)`, `([^`]+)`, `([^`]+)`, `([^`]+)`", text, re.S)
    if not match:
        return None
    return list(match.groups())


def migrate_sexta_pessoa(root: str | Path) -> dict[str, Any]:
    """Create a conservative status for the existing sexta_pessoa production.

    It records only filesystem evidence and the caller's explicit current-avatar instruction.
    Generated browser images and hook selections are deliberately left unknown unless a project
    artifact proves their exact provenance.
    """
    root = Path(root).resolve()
    if root.name != "sexta_pessoa":
        raise PipelineStateError("O migrador MVP é limitado à produção sexta_pessoa.")

    source_readme = root / "pacote_browser" / "_LEIA_PRIMEIRO.md"
    order = _parse_execution_order(source_readme)
    if not order:
        raise PipelineStateError("A ordem de avatares não pôde ser comprovada no pacote_browser.")

    roster = {
        "casey_harrisson": "Casey Harrisson",
        "kris_walker": "Kris Walker",
        "shelby_turner": "Shelby Turner",
        "kelly_bennett": "Kelly Bennett",
        "robin_matthews": "Robin Matthews",
    }
    missing = [avatar_id for avatar_id in order if avatar_id not in roster]
    if missing:
        raise PipelineStateError(f"Avatar sem nome comprovado: {missing}")

    artifacts = {
        "watch_manifest": _artifact(root, root / "watch" / "manifest.json", "watch_manifest"),
        "transcript": _artifact(root, root / "watch" / "transcript.txt", "transcript"),
        "script": _artifact(root, root / "ROTEIRO.md", "script"),
        "hook_options": _artifact(root, root / "GANCHOS_VISUAIS.md", "hook_options"),
        "image_prompts": _artifact(root, root / "PROMPTS_IMAGEM.md", "image_prompts"),
        "shared_card_reference": _artifact(root, root / "pacote_browser" / "_compartilhado" / "REF-CARTA.png", "reference"),
    }

    avatars: dict[str, Any] = {}
    for position, avatar_id in enumerate(order, start=1):
        prompt_dir = root / "pacote_browser" / avatar_id
        prompt_files = sorted(path.name for path in prompt_dir.glob("*.md") if path.name[:2].isdigit())
        avatars[avatar_id] = {
            "name": roster[avatar_id],
            "position": position,
            "stage": "queued",
            "anchor_path": None,
            "anchor_sha256": None,
            "anchor_evidence": "unknown",
            "prompt_files": prompt_files,
            "assets": {},
            "assets_evidence": "unknown",
            "video_prompts": {"status": "unknown", "path": None},
            "completed_at": None,
        }

    # Casey as active avatar is an explicit instruction in the current migration request.
    avatars["casey_harrisson"]["stage"] = "queued"
    script_evidence = root / "GANCHOS_VISUAIS.md"
    script_text = script_evidence.read_text(encoding="utf-8") if script_evidence.is_file() else ""
    script_approval = "confirmed_by_artifact" if "Roteiro aprovado." in script_text else "unknown"

    state: dict[str, Any] = {
        "schema_version": 1,
        "pipeline": PIPELINE,
        "angle": ANGLE,
        "production": {
            "id": "sexta_pessoa",
            "title": "A sexta pessoa",
            "root": str(root),
            "created_at": None,
            "migrated_at": utc_now(),
            "updated_at": utc_now(),
        },
        "workflow": {
            "stage": "hooks_awaiting_choice",
            "next_action": "await_hook_selection",
            "current_avatar_id": "casey_harrisson",
            "current_avatar_evidence": "explicit_user_confirmation",
            "blocked_by": "hook_selection_unknown",
        },
        "inputs": {
            "video": {"path": None, "sha256": None, "evidence": "watch_manifest_references_external_video"},
            "avatars": [
                {"id": avatar_id, "name": roster[avatar_id], "position": i,
                 "anchor_path": None, "anchor_sha256": None, "evidence": "prompt_package_only"}
                for i, avatar_id in enumerate(order, start=1)
            ],
        },
        "artifacts": artifacts,
        "approvals": {
            "script": {
                "status": script_approval,
                "approved_at": None,
                "evidence_path": "GANCHOS_VISUAIS.md" if script_approval != "unknown" else None,
                "artifact_sha256": artifacts["script"]["sha256"],
            },
            "hooks": {
                "status": "unknown",
                "selected_ids": [],
                "selected_titles": [],
                "source_script_sha256": artifacts["script"]["sha256"],
                "approved_at": None,
                "no_hooks_explicitly_authorized": False,
                "evidence": "No project artifact proves the current selected hook set.",
            },
        },
        "hooks": {
            "status": "unknown",
            "options_path": artifacts["hook_options"]["path"],
            "options_sha256": artifacts["hook_options"]["sha256"],
            "selected_ids": [],
            "selected_titles": [],
            "source_script_sha256": artifacts["script"]["sha256"],
            "no_hooks_explicitly_authorized": False,
        },
        "avatar_queue": {"order": order, "current_index": 0, "evidence_path": "pacote_browser/_LEIA_PRIMEIRO.md"},
        "avatars": avatars,
        "unknowns": [
            {
                "code": "hook_selection_unknown",
                "message": "Há opções e prompts de imagem, mas nenhum artefato prova qual conjunto de hooks está aprovado para a produção atual.",
            },
            {
                "code": "browser_asset_provenance_unknown",
                "message": "Não há imagens nomeadas e vinculadas por artefato aos assets da Casey; nenhum asset foi marcado como concluído.",
            },
            {
                "code": "avatar_anchor_provenance_unknown",
                "message": "Os pacotes citam âncoras, mas a produção não contém um registro canônico com caminho e hash de cada arquivo de origem.",
            },
        ],
        "inconsistencies": [],
        "history": [
            {
                "at": utc_now(),
                "type": "migration",
                "message": "Estado MVP migrado somente a partir de artefatos locais e confirmação explícita do avatar atual.",
            }
        ],
    }
    validate(state)
    save(state, root)
    return reconcile(root)
