"""Build an immutable, versioned execution plan for a production batch.

All N+2 assets (hooks + body + CTA) are resolved before Chrome opens.
No creative decisions happen after build(); execution is purely deterministic.

Usage:
    python -m studio.execution_plan producao/sexta_pessoa
    python -m studio.execution_plan producao/sexta_pessoa --dry-run
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

from . import pipeline_browser_bridge as bridge, pipeline_state as state

PLAN_FILENAME = "execution_plan.json"
PLAN_VERSION = 1
MAX_BROWSER_CONCURRENCY = int(os.environ.get("MAX_BROWSER_CONCURRENCY", "8"))

REQUIRED_ASSET_FIELDS = (
    "production_id", "pipeline", "avatar_id", "asset_id", "asset_type",
    "prompt", "prompt_sha256", "references", "output_path", "eligible",
    "wave", "canonical_asset_fingerprint", "execution_spec",
)
# asset_type in the plan = role in canonical state ("hook", "body", "cta")

REQUIRED_EXECUTION_SPEC_FIELDS = (
    "version", "target_generation_provider", "retry_policy",
    "dependencies", "expected_reference_sha256",
)


def _sha256(obj: Any) -> str:
    return hashlib.sha256(
        json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def _output_path(root: Path, avatar_id: str, asset_id: str) -> str:
    return str(root / "pacote_browser" / avatar_id / f"{asset_id}.png")


def build(path_or_root: str | Path, dry_run: bool = False,
          max_concurrency: int | None = None) -> dict:
    """Build an immutable execution plan for all eligible assets of the current avatar.

    Computes wave assignments so the executor can work in batches when concurrency
    is capped below the total asset count. All assets are prepared regardless of cap.

    Writes execution_plan.json unless dry_run=True. Returns the plan dict.
    """
    root = Path(path_or_root)
    if root.name == state.STATUS_FILENAME:
        root = root.parent

    current_state = state.load(root)
    avatar_id = current_state["workflow"].get("current_avatar_id")
    if not avatar_id:
        raise ValueError("No current_avatar_id in workflow state.")

    assets_meta = current_state["avatars"][avatar_id].get("assets", {})

    ineligible = [k for k, v in assets_meta.items() if not v.get("eligible_for_execution")]
    if ineligible:
        raise ValueError(f"Assets not eligible for execution: {ineligible}. Run prepare_current_avatar first.")

    contracts = bridge.build_materialized_jobs(root)
    if not contracts:
        raise ValueError("No contracts built — check asset status (must be 'pending' or 'queued').")

    cap = max_concurrency if max_concurrency is not None else MAX_BROWSER_CONCURRENCY
    desired_concurrency = len(contracts)
    effective_concurrency = min(desired_concurrency, cap)
    n_waves = (desired_concurrency + effective_concurrency - 1) // effective_concurrency

    production_id = current_state["production"]["id"]
    pipeline = current_state["pipeline"]

    plan_assets = []
    for i, c in enumerate(contracts):
        plan_assets.append({
            "production_id": production_id,
            "pipeline": pipeline,
            "avatar_id": avatar_id,
            "asset_id": c["asset_id"],
            "asset_type": assets_meta[c["asset_id"]].get("role"),
            "prompt": c["prompt"],
            "prompt_sha256": c["prompt_sha256"],
            "references": c["references"],
            "output_path": _output_path(root, avatar_id, c["asset_id"]),
            "eligible": True,
            "wave": i // effective_concurrency,
            "canonical_asset_fingerprint": c["canonical_asset_fingerprint"],
            "execution_spec": c["execution_spec"],
        })

    plan_body: dict = {
        "plan_version": PLAN_VERSION,
        "created_at": int(time.time()),
        "production_id": production_id,
        "pipeline": pipeline,
        "avatar_id": avatar_id,
        "desired_concurrency": desired_concurrency,
        "effective_concurrency": effective_concurrency,
        "max_browser_concurrency": cap,
        "n_waves": n_waves,
        "assets": plan_assets,
    }
    plan_body["plan_sha256"] = _sha256({k: v for k, v in plan_body.items()})

    if not dry_run:
        out = root / PLAN_FILENAME
        out.write_text(json.dumps(plan_body, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[execution_plan] Written: {out}")
        print(f"[execution_plan] plan_sha256: {plan_body['plan_sha256'][:16]}...")
        print(f"[execution_plan] assets ({len(plan_assets)}): {[a['asset_id'] for a in plan_assets]}")
        print(f"[execution_plan] concurrency: {effective_concurrency}/{desired_concurrency} cap={cap}, waves={n_waves}")

    return plan_body


def load(path_or_root: str | Path) -> dict:
    """Load and integrity-check an existing execution plan."""
    root = Path(path_or_root)
    if root.name == state.STATUS_FILENAME:
        root = root.parent
    plan_path = root / PLAN_FILENAME
    if not plan_path.exists():
        raise FileNotFoundError(f"No execution plan at {plan_path}. Run build() first.")
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    stored_sha = plan.get("plan_sha256")
    body = {k: v for k, v in plan.items() if k != "plan_sha256"}
    computed = _sha256(body)
    if stored_sha != computed:
        raise ValueError(
            f"execution_plan.json integrity check failed: "
            f"stored={stored_sha[:16] if stored_sha else 'None'}, computed={computed[:16]}"
        )
    return plan


def validate_execution_plan(plan: dict) -> list[str]:
    """Validate an execution plan before any browser execution.

    Returns a list of error strings. Empty list = valid and safe to proceed.
    An invalid plan must produce zero browser tabs, zero submissions.
    """
    errors: list[str] = []

    # 1. Plan-level integrity
    stored_sha = plan.get("plan_sha256")
    body = {k: v for k, v in plan.items() if k != "plan_sha256"}
    if _sha256(body) != stored_sha:
        errors.append("plan_sha256 integrity check failed")

    assets = plan.get("assets", [])
    if not assets:
        errors.append("plan has no assets")
        return errors

    # 2. No duplicate asset_ids
    asset_ids = [a.get("asset_id") for a in assets]
    if len(asset_ids) != len(set(asset_ids)):
        errors.append(f"duplicate asset_ids: {asset_ids}")

    seen_fps: dict[str, str] = {}
    for asset in assets:
        aid = asset.get("asset_id", "<missing>")

        # 3. Required fields present and non-None
        for field in REQUIRED_ASSET_FIELDS:
            if field not in asset or asset[field] is None:
                errors.append(f"{aid}: missing required field '{field}'")

        # 4. Prompt not empty
        prompt = asset.get("prompt", "")
        if not (prompt and prompt.strip()):
            errors.append(f"{aid}: prompt is empty")

        # 5. Prompt sha256 matches content
        expected_hash = asset.get("prompt_sha256")
        if prompt and expected_hash:
            actual = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
            if actual != expected_hash:
                errors.append(f"{aid}: prompt_sha256 mismatch (content changed after plan was built)")

        # 6. References: files must exist and hashes must match
        for ref in asset.get("references", []):
            role = ref.get("role", "?")
            path = ref.get("canonical_path")
            ref_sha = ref.get("sha256")
            if not path:
                errors.append(f"{aid}/{role}: canonical_path missing")
                continue
            p = Path(path)
            if not p.exists():
                errors.append(f"{aid}/{role}: file not found: {path}")
                continue
            if ref_sha:
                actual_ref = state.sha256_file(p)
                if actual_ref != ref_sha:
                    errors.append(
                        f"{aid}/{role}: file hash mismatch "
                        f"(expected {ref_sha[:8]}, got {actual_ref[:8]})"
                    )

        # 7. Output path must have an extension (file need not exist yet)
        output_path = asset.get("output_path", "")
        if output_path and not Path(output_path).suffix:
            errors.append(f"{aid}: output_path has no extension: {output_path}")

        # 8. ExecutionSpec completeness
        spec = asset.get("execution_spec") or {}
        for sf in REQUIRED_EXECUTION_SPEC_FIELDS:
            if sf not in spec:
                errors.append(f"{aid}: execution_spec missing '{sf}'")

        # 9. Fingerprint uniqueness across assets
        fp = asset.get("canonical_asset_fingerprint")
        if fp:
            if fp in seen_fps:
                errors.append(
                    f"{aid}: canonical_asset_fingerprint collision with {seen_fps[fp]}"
                )
            seen_fps[fp] = aid

    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build execution plan for a production batch.")
    parser.add_argument("root", help="Production root (e.g. producao/sexta_pessoa)")
    parser.add_argument("--dry-run", action="store_true", help="Build but do not write to disk")
    parser.add_argument("--validate", action="store_true", help="Validate existing plan")
    args = parser.parse_args()

    try:
        if args.validate:
            plan = load(args.root)
            errs = validate_execution_plan(plan)
            if errs:
                for e in errs:
                    print(f"  ERROR: {e}", file=sys.stderr)
                sys.exit(1)
            print("[execution_plan] valid — zero errors")
        else:
            plan = build(args.root, dry_run=args.dry_run)
            if args.dry_run:
                print(json.dumps(plan, indent=2, ensure_ascii=False))
    except (ValueError, FileNotFoundError) as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)
