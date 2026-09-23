"""Neutral entry point for Claude Code and Codex — same code, same sequence.

Both agents call these functions instead of re-inventing the sequence per conversation.
All state lives in files; nothing is passed through conversation history.

THINK phase may read creative sources (scripts, copy docs, Graphify).
EXECUTE phase reads canonical state + execution plan ONLY.
Never reconstruct production state from chat when canonical files exist.
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from . import browser_queue, execution_plan as ep, pipeline_browser_bridge as bridge, pipeline_state as state
from .bridge import ensure_bridge

EXECUTION_STATE_FILENAME = "execution_state.json"


# ── status ────────────────────────────────────────────────────────────────────

def status(root: str | Path) -> dict[str, Any]:
    """Read current production status. Cheap — no file-tree walk, no creative context."""
    root = Path(root)
    if root.name == state.STATUS_FILENAME:
        root = root.parent

    canonical = state.load(root)
    wf = canonical["workflow"]
    avatar_id = wf.get("current_avatar_id")
    avatar_assets = (
        canonical["avatars"].get(avatar_id, {}).get("assets", {}) if avatar_id else {}
    )
    statuses = [v.get("status") for v in avatar_assets.values()]

    plan_version = plan_sha256 = plan_valid = None
    plan_path = root / ep.PLAN_FILENAME
    if plan_path.exists():
        try:
            plan = ep.load(root)
            plan_version = plan.get("plan_version")
            plan_sha256 = (plan.get("plan_sha256") or "")[:16]
            plan_valid = len(ep.validate_execution_plan(plan)) == 0
        except (ValueError, FileNotFoundError):
            plan_valid = False

    q = browser_queue.load()
    return {
        "production": canonical["production"]["id"],
        "current_stage": wf.get("stage"),
        "current_avatar": avatar_id,
        "next_action": wf.get("next_action"),
        "plan_version": plan_version,
        "plan_sha256": plan_sha256,
        "plan_valid": plan_valid,
        "assets_total": len(avatar_assets),
        "assets_pending": statuses.count("pending"),
        "assets_queued": statuses.count("queued"),
        "assets_running": sum(1 for s in statuses if s in ("preparing", "submitting", "generating")),
        "assets_received": statuses.count("done"),
        "assets_approved": statuses.count("approved"),
        "queue_jobs": len(q.get("jobs", [])),
    }


# ── prepare ───────────────────────────────────────────────────────────────────

def build_plan(root: str | Path, max_concurrency: int | None = None) -> dict:
    """PREPARE: Build immutable execution plan for the current avatar.

    Writes execution_plan.json. Raises if any asset is not yet eligible.
    """
    return ep.build(root, max_concurrency=max_concurrency)


def validate_plan(root: str | Path) -> list[str]:
    """PREPARE: Load and validate existing execution_plan.json.

    Returns list of error strings. Empty = safe to proceed.
    Zero browser tabs must open when this returns non-empty.
    """
    plan = ep.load(root)
    return ep.validate_execution_plan(plan)


# ── execute ───────────────────────────────────────────────────────────────────

def execute_avatar(
    root: str | Path,
    avatar_id: str | None = None,
) -> dict:
    """EXECUTE: Run the full pre-Chrome preparation cycle for one avatar.

    Steps:
      1. Load execution_plan.json and verify plan_sha256 integrity.
      2. validate_execution_plan — abort immediately if ANY error.
      3. Confirm the requested avatar matches the plan.
      4. Confirm hooks + body + CTA are all present.
      5. Read effective_concurrency from the plan.
      6. Idempotency check: if same plan_sha256 + batch still valid, resume.
      7. ensure_bridge() — auto-starts headless server.
      8. sync_prepared_assets — materialize queue jobs (idempotent).
      9. browser_queue.control — set concurrency.
     10. authorize_batch — one batch for ALL N+2 assets simultaneously.
     11. dispatch_batch — create preflight_requests for the extension.
     12. Save execution_state.json + return tracking dict.

    Returns a dict with batch_id, asset list, concurrency, dispatch result.
    Idempotent: repeated calls with the same plan reuse the existing batch.
    """
    root = Path(root)
    if root.name == state.STATUS_FILENAME:
        root = root.parent

    # ── 1. Load plan + verify integrity (raises ValueError on tamper) ──────────
    plan = ep.load(root)

    # ── 2. Validate — FAIL-FAST: abort before any browser action ──────────────
    errors = ep.validate_execution_plan(plan)
    if errors:
        raise ValueError(
            f"Execution plan invalid — {len(errors)} error(s), aborting before bridge. "
            f"First: {errors[0]}"
        )

    # ── 3. Select avatar ───────────────────────────────────────────────────────
    target_avatar = avatar_id or plan["avatar_id"]
    if target_avatar != plan["avatar_id"]:
        raise ValueError(
            f"Requested avatar '{target_avatar}' does not match plan avatar "
            f"'{plan['avatar_id']}'. Rebuild plan for the correct avatar."
        )

    plan_assets = plan["assets"]

    # ── 4. Confirm hooks + body + CTA ─────────────────────────────────────────
    roles = {a["asset_type"] for a in plan_assets}
    missing = {"hook", "body", "cta"} - roles
    if missing:
        raise ValueError(f"Plan missing required asset roles: {missing}")

    # ── 5. Effective concurrency (resolved at build time) ─────────────────────
    effective_concurrency = plan["effective_concurrency"]

    # ── 6. Idempotency: reuse existing batch when plan is unchanged ────────────
    exec_state_path = root / EXECUTION_STATE_FILENAME
    exec_state: dict = {}
    if exec_state_path.exists():
        exec_state = json.loads(exec_state_path.read_text(encoding="utf-8"))

    if exec_state.get("plan_sha256") == plan["plan_sha256"]:
        existing_batch_id = exec_state.get("batch_id")
        if existing_batch_id:
            try:
                browser_queue.get_batch(existing_batch_id)
                # Batch still valid — dispatch is idempotent, picks up any skipped assets
                dispatch_result = browser_queue.dispatch_batch(existing_batch_id)
                return {
                    "batch_id": existing_batch_id,
                    "avatar_id": target_avatar,
                    "plan_sha256": plan["plan_sha256"],
                    "assets": [a["asset_id"] for a in plan_assets],
                    "effective_concurrency": effective_concurrency,
                    "dispatch_result": dispatch_result,
                    "resumed": True,
                }
            except ValueError:
                pass  # batch gone — fall through to create new

    # ── 7–11. First run: start bridge, sync, authorize, dispatch ──────────────
    ensure_bridge()

    bridge.sync_prepared_assets(root)

    browser_queue.control(True, effective_concurrency)

    fingerprints = {
        a["asset_id"]: a["canonical_asset_fingerprint"] for a in plan_assets
    }
    batch = browser_queue.authorize_batch(
        production_id=plan["production_id"],
        pipeline=plan["pipeline"],
        avatar_id=target_avatar,
        asset_fingerprints=fingerprints,
    )
    batch_id = batch["batch_id"]

    dispatch_result = browser_queue.dispatch_batch(batch_id)

    # ── 12. Persist execution state for idempotent resume ─────────────────────
    exec_state_path.write_text(
        json.dumps({
            "plan_sha256": plan["plan_sha256"],
            "batch_id": batch_id,
            "avatar_id": target_avatar,
            "dispatched_at": int(time.time()),
        }, indent=2),
        encoding="utf-8",
    )

    return {
        "batch_id": batch_id,
        "avatar_id": target_avatar,
        "plan_sha256": plan["plan_sha256"],
        "assets": [a["asset_id"] for a in plan_assets],
        "effective_concurrency": effective_concurrency,
        "dispatch_result": dispatch_result,
        "resumed": False,
    }


def start_bridge() -> str:
    """EXECUTE: Ensure the headless bridge is running. Returns its base URL."""
    return ensure_bridge()


def retry_asset(root: str | Path, asset_id: str) -> None:
    """EXECUTE: Retry a single failed or interrupted asset.

    Not yet implemented — browser execution phase is pending.
    """
    raise NotImplementedError(
        f"retry_asset({asset_id!r}) not yet implemented. "
        "Reset asset status in canonical state and re-run execute_avatar()."
    )
