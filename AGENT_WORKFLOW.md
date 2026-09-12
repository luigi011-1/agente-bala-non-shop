# AGENT_WORKFLOW.md
## Auraly Studio — session bootstrap

Read this file first. Then read canonical state. Then load only what the current stage requires.

**Never reconstruct production state from chat when canonical files exist.**
**During EXECUTE, do not reload creative context unless execution fails because a required artifact is missing.**

---

## Two phases — strict separation

| Phase | Who | What it may read |
|-------|-----|-----------------|
| THINK / PREPARE | CLI | Video, transcripts, copy docs, Graphify, creative context |
| EXECUTE | CLI → Chrome extension | Canonical state + execution plan ONLY |

A session that enters EXECUTE must not reload MP4, transcriptions, copy docs, or Graphify.
The plan contains everything the executor needs.

---

## Canonical files (single source of truth)

| File | Purpose |
|------|---------|
| `producao/<slug>/status.json` | Avatar/asset state |
| `producao/<slug>/execution_plan.json` | Immutable batch plan (write once, read by executor) |
| `producao/<slug>/execution_state.json` | Batch tracking (batch_id, idempotency key) |
| `studio/queue-state.json` | Browser queue (jobs, preflights, batches) |

---

## PREPARE steps (may read creative context)

1. After script approval, propose 10 visual hooks; the user may select any quantity. This rule applies only to new productions and never rewrites an already approved hook selection.
2. Load `status.json` — identify `current_avatar_id` and stage
3. Verify all N+2 assets have `eligible_for_execution=True`
4. `from studio.orchestrator import build_plan, validate_plan, status`
5. `build_plan(root)` — resolves all prompts, refs, output paths into `execution_plan.json`
6. `validate_plan(root)` — must return `[]` before any EXECUTE step

## EXECUTE steps (canonical state + plan only)

6. `from studio.orchestrator import execute_avatar`
7. `execute_avatar(root)` — single call; handles steps 7–12 below:
   - Verify plan integrity (sha256)
   - Fail-fast on any validation error — zero browser actions if invalid
   - ensure_bridge() — auto-starts headless FastAPI on port 8765
   - sync_prepared_assets — materialize queue jobs (idempotent)
   - authorize_batch — one batch for all N+2 assets simultaneously
   - dispatch_batch — create preflight_requests for the extension
8. Poll `GET /api/browser/queue` until all N+2 preflights are `valid`
9. Extension fills, submits, downloads (per job in the wave)
10. `reconcile_materialized_jobs` — update canonical state
11. Human review → approve/reject

---

## Fail-fast rule

```
load plan → verify sha256 → validate_execution_plan
→ any error: raise ValueError, zero browser actions
```

ensure_bridge(), authorize_batch(), dispatch_batch() are never called on an invalid plan.

---

## Asset independence (N+2 simultaneous)

- K01–K03: hooks
- K04: body
- K05: CTA — **no dependency on K04**

All enter the same batch. References per asset: `[avatar_anchor, shared_card_reference]`.

Concurrency: `effective = min(len(assets), MAX_BROWSER_CONCURRENCY)`
Default cap: 8 (env `MAX_BROWSER_CONCURRENCY`). All assets pre-materialized regardless of cap.
With 3 hooks: desired=5, effective=5, n_waves=1.

---

## Idempotency

`execute_avatar` saves `execution_state.json` with `{plan_sha256, batch_id}`.
A repeated call with the same plan reuses the batch — no duplicate jobs, preflights, or submissions.

## Direct ChatGPT image-generation recovery

When the practical Chrome workflow is used, every retry stays in the **same tab and same conversation** for that asset:

1. If ChatGPT reports a recoverable generation failure — including “Não consegui gerar a imagem”, “Something went wrong”, rate-limit language such as “Você está solicitando muitas gerações de imagem”, or a stalled generation — first inspect the visible page.
2. If a dismiss/close button is present for a warning or pop-up, close it.
3. Attach the corresponding avatar anchor **again** in that same conversation.
4. Paste the exact approved prompt for that asset and submit it once.
5. Never open a replacement tab just because one generation failed.

---

## Entry point (same for Claude Code and Codex)

```python
from studio.orchestrator import build_plan, validate_plan, execute_avatar, status
```

No behavior lives in prompts. Both agents call the same functions, same files, same results.

---

## Environment

```bash
# Install dependencies (both environments)
pip install -r requirements.txt
.venv/Scripts/pip install -r requirements.txt

# PREPARE
python -m studio.execution_plan producao/sexta_pessoa
python -m studio.execution_plan producao/sexta_pessoa --validate

# TESTS (zero skips expected)
python -m unittest studio.test_pipeline_state studio.test_pipeline_browser_bridge \
    studio.test_batch_authorization studio.test_execution_plan \
    studio.test_bridge studio.test_orchestrator -v
node --test studio/chrome-extension/background.test.cjs studio/chrome-extension/content.test.cjs
```
