"""Canonical-state to browser-queue contract bridge (Phase A: no browser execution)."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Callable

from . import browser_queue, pipeline_state


def _fingerprint(payload: dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()


def _root(path_or_root: str | Path) -> Path:
    value = Path(path_or_root)
    return (value.parent if value.name == pipeline_state.STATUS_FILENAME else value).resolve()


def build_materialized_jobs(path_or_root: str | Path, only_asset_id: str | None = None) -> list[dict[str, Any]]:
    """Build, but do not enqueue, contracts for currently eligible canonical assets."""
    root = _root(path_or_root)
    state = pipeline_state.load(root)
    avatar_id = state["workflow"].get("current_avatar_id")
    avatar = state["avatars"][avatar_id]
    package = state["artifacts"]["image_prompts_current"]
    _, sections = pipeline_state._prompt_package_metadata_and_sections(root / package["path"])
    card = state.get("artifacts", {}).get("shared_card_reference", {})
    contracts = []
    for asset_id, asset in avatar.get("assets", {}).items():
        if only_asset_id is not None and asset_id != only_asset_id:
            continue
        if not asset.get("eligible_for_execution") or asset.get("status") not in {"pending", "queued"}:
            continue
        prompt = sections[asset_id]
        prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
        if prompt_hash != asset["prompt_sha256"]:
            raise pipeline_state.PipelineStateError(f"Prompt do asset não corresponde ao hash preparado: {asset_id}.")
        def reference(role: str, path: str, sha256: str) -> dict[str, Any]:
            stat = Path(path).stat()
            return {"role": role, "canonical_path": path, "sha256": sha256,
                    "size": stat.st_size, "mtime_ns": stat.st_mtime_ns}
        references = [reference("avatar_anchor", avatar["anchor_path"], asset["anchor_sha256"])]
        if asset.get("shared_card_reference_sha256"):
            if not card.get("path"):
                raise pipeline_state.PipelineStateError(
                    f"{asset_id} exige shared_card_reference, mas ela não está declarada no estado."
                )
            references.append(reference("shared_card_reference", str(root / card["path"]), asset["shared_card_reference_sha256"]))
        parent = None
        if asset.get("parent_asset"):
            parent_asset = avatar["assets"][asset["parent_asset"]]
            parent_hash = parent_asset.get("result", {}).get("image_sha256")
            parent_path = parent_asset.get("result", {}).get("local_file")
            if parent_asset.get("status") != "approved" or not parent_hash or not parent_path:
                continue
            parent = {"asset_id": asset["parent_asset"], "approved_result_sha256": parent_hash,
                      "canonical_path": parent_path}
            references.append(reference("parent_approved_result", parent_path, parent_hash))
        identity = {
            "production_id": state["production"]["id"], "pipeline": state["pipeline"],
            "avatar_id": avatar_id, "asset_id": asset_id, "prompt_sha256": prompt_hash,
            "anchor_sha256": asset["anchor_sha256"],
            "shared_card_reference_sha256": asset.get("shared_card_reference_sha256"),
            "source_script_sha256": asset["source_script_sha256"],
            "hook_selection_sha256": asset["hook_selection_sha256"],
            "parent": parent,
        }
        contracts.append({
            **identity,
            "prompt": prompt,
            "source_prompt_package_sha256": asset["source_prompt_package_sha256"],
            "canonical_state_path": str(root / pipeline_state.STATUS_FILENAME),
            "references": references,
            "parent_dependency": parent,
            "execution_spec": {
                "version": 1, "target_generation_provider": "chatgpt_ui",
                "retry_policy": {"automatic_retry": False, "requires_explicit_recovery": True},
                "dependencies": [parent] if parent else [],
                "expected_reference_sha256": {r["role"]: r["sha256"] for r in references},
            },
            "canonical_asset_fingerprint": _fingerprint(identity),
        })
    return contracts


def sync_prepared_assets(path_or_root: str | Path,
                         enqueue: Callable[[list[dict[str, Any]]], dict[str, Any]] = browser_queue.enqueue_materialized,
                         only_asset_id: str | None = None) -> dict[str, Any]:
    """Persist eligible contracts into the existing queue and reflect only queued facts back."""
    root = _root(path_or_root)
    contracts = build_materialized_jobs(root, only_asset_id=only_asset_id)
    queue_state = enqueue(contracts)
    jobs = {job.get("canonical_asset_fingerprint"): job for job in queue_state["jobs"]
            if job.get("job_kind") == "canonical_materialized"}
    state = pipeline_state.load(root)
    avatar = state["avatars"][state["workflow"]["current_avatar_id"]]
    changed = False
    for contract in contracts:
        asset = avatar["assets"][contract["asset_id"]]
        job = jobs[contract["canonical_asset_fingerprint"]]
        if asset.get("canonical_asset_fingerprint") != contract["canonical_asset_fingerprint"]:
            asset["canonical_asset_fingerprint"] = contract["canonical_asset_fingerprint"]
            changed = True
        if asset.get("queue_job_id") != job["id"] or asset.get("status") == "pending":
            asset.update(queue_job_id=job["id"], queue_status=job["status"], status="queued")
            changed = True
    if changed:
        pipeline_state.save(state, root)
    return {"contracts": contracts, "queue": queue_state, "state": state}


def sync_one_asset(path_or_root: str | Path, asset_id: str,
                   enqueue: Callable[[list[dict[str, Any]]], dict[str, Any]] = browser_queue.enqueue_materialized) -> dict[str, Any]:
    """Materialize one explicitly named eligible asset; never fans out to siblings."""
    if not asset_id:
        raise ValueError("asset_id explícito é obrigatório.")
    result = sync_prepared_assets(path_or_root, enqueue=enqueue, only_asset_id=asset_id)
    if len(result["contracts"]) != 1 or result["contracts"][0]["asset_id"] != asset_id:
        raise pipeline_state.PipelineStateError("O asset explícito não está elegível para materialização.")
    return result
