"""Passive real benchmark: authorize K01-K04, dispatch preflight requests, wait for all
four to reach 'ready' state. Stops before any upload/fill/submit.

Run while the Studio server is live and the Chrome extension is connected:

    python -m studio.benchmark_batch_preflight

Reads canonical state from producao/sexta_pessoa/status.json.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

# Allow running as a script from the project root
sys.path.insert(0, str(Path(__file__).parent.parent))

from studio import browser_queue, pipeline_state, pipeline_browser_bridge

PRODUCTION_ROOT = Path(__file__).parent.parent / 'producao' / 'sexta_pessoa'
STATUS_FILE = PRODUCTION_ROOT / pipeline_state.STATUS_FILENAME
REQUIRED_CAPS = {
    'canonical_materialized_jobs', 'multiple_references', 'preflight_handshake',
    'preflight_polling', 'batch_preflight', 'dedicated_tab_creation',
}
BATCH_ASSETS = [
    'K01_hook_card_pull_camera',
    'K02_hook_salt_circle_closing',
    'K03_hook_honey_over_card',
    'K04_body_reading_t2_t4',
]
POLL_INTERVAL = 0.15  # seconds between queue reads (150ms for finer benchmark resolution)
TIMEOUT = 180         # seconds before giving up


def _ms(t0: float) -> int:
    return int((time.perf_counter() - t0) * 1000)


def _check_extension() -> dict:
    """Verify that the loaded service worker reports the required capabilities."""
    q = browser_queue.load()
    version = q.get('agent_protocol_version', '<not reported>')
    caps = set(q.get('agent_capabilities') or [])
    missing = REQUIRED_CAPS - caps
    print(f'\n[capabilities] agent_protocol_version : {version}')
    print(f'[capabilities] reported                : {sorted(caps) or "(none yet)"}')
    if missing:
        print(f'[capabilities] MISSING                 : {sorted(missing)}')
        print('\nextension_reload_required=true')
        print('Reload the extension at chrome://extensions and run again.')
        sys.exit(1)
    print(f'[capabilities] ALL REQUIRED PRESENT')
    return {'version': version, 'capabilities': sorted(caps)}


def _build_fingerprints() -> dict[str, str]:
    """Build materialized jobs (idempotent) and return the current fingerprints."""
    result = pipeline_browser_bridge.sync_prepared_assets(STATUS_FILE)
    state = browser_queue.load()
    fps: dict[str, str] = {}
    for job in state['jobs']:
        if (job.get('production_id') == 'sexta_pessoa'
                and job.get('avatar_id') == 'casey_harrisson'
                and job.get('job_kind') == 'canonical_materialized'
                and job.get('asset_id') in BATCH_ASSETS
                and job.get('status') != 'cancelled'):
            fps[job['asset_id']] = job['canonical_asset_fingerprint']
    missing = set(BATCH_ASSETS) - set(fps)
    if missing:
        print(f'\n[ERROR] Missing queued jobs for: {sorted(missing)}')
        print('Run pipeline_browser_bridge.sync_prepared_assets first.')
        sys.exit(1)
    return fps


def _asset_timings(request_ids: list[str]) -> dict[str, dict]:
    """Return per-asset timing data keyed by request_id."""
    return {r: {} for r in request_ids}


def run():
    wall0 = time.perf_counter()
    print('=' * 64)
    print(' AURALY STUDIO — Batch Preflight Benchmark (passive)')
    print('=' * 64)

    # ── 1. Extension capability check ────────────────────────────────────────
    ext_info = _check_extension()

    # ── 2. Build / sync materialized jobs ────────────────────────────────────
    print('\n[sync] Building materialized jobs from canonical state...')
    fps = _build_fingerprints()
    print(f'[sync] Fingerprints:')
    for asset_id in BATCH_ASSETS:
        print(f'       {asset_id}: {fps[asset_id][:16]}...')

    # ── 3. Authorize batch ────────────────────────────────────────────────────
    t_auth_start = time.perf_counter()
    batch = browser_queue.authorize_batch(
        'sexta_pessoa', 'auraly_soulmate', 'casey_harrisson', fps,
        allow_activation=False)
    t_auth_end = time.perf_counter()
    batch_id = batch['batch_id']
    auth_ms = int((t_auth_end - t_auth_start) * 1000)
    print(f'\n[T0] batch authorized  batch_id={batch_id}  ({auth_ms} ms)')

    # ── 4. Dispatch batch ────────────────────────────────────────────────────
    t_dispatch_start = time.perf_counter()
    dispatch_result = browser_queue.dispatch_batch(batch_id)
    t1 = time.perf_counter()
    dispatch_ms = int((t1 - t_dispatch_start) * 1000)

    if dispatch_result['skipped']:
        print(f'\n[WARN] Skipped assets: {dispatch_result["skipped"]}')

    dispatched = dispatch_result['dispatched']
    req_by_asset = {d['asset_id']: d['request_id'] for d in dispatched}
    print(f'[T1] preflight requests persisted  ({dispatch_ms} ms)')
    for asset_id in BATCH_ASSETS:
        rid = req_by_asset.get(asset_id, 'SKIPPED')
        print(f'     {asset_id}: request_id={rid}')

    if not dispatched:
        print('\n[ERROR] No preflight requests were dispatched. Aborting.')
        sys.exit(1)

    # ── 5. Poll until all four preflights are ready ───────────────────────────
    print(f'\n[poll] Waiting for extension to create tabs and register preflights...')
    print(f'       (poll every {POLL_INTERVAL}s, timeout {TIMEOUT}s)\n')

    asset_events: dict[str, dict] = {aid: {} for aid in BATCH_ASSETS}
    request_ids = set(req_by_asset.values())
    t_poll_start = time.perf_counter()

    prev_statuses: dict[str, str] = {}

    while True:
        elapsed = time.perf_counter() - t_poll_start
        if elapsed > TIMEOUT:
            print(f'\n[TIMEOUT] {TIMEOUT}s elapsed without all preflights becoming ready.')
            break

        state = browser_queue.load()

        # Track preflight_request transitions
        for req in state.get('preflight_requests', []):
            rid = req.get('request_id')
            if rid not in request_ids:
                continue
            asset_id = next((a for a, r in req_by_asset.items() if r == rid), None)
            if not asset_id:
                continue
            status = req.get('status')
            if status != prev_statuses.get(rid):
                prev_statuses[rid] = status
                now_ms = _ms(wall0)
                print(f'  [{now_ms:6d}ms] {asset_id.split("_")[0]} → preflight_request.{status}')
                asset_events[asset_id][f'request_{status}_ms'] = now_ms
                if status == 'failed':
                    asset_events[asset_id]['error'] = req.get('error', '')

        # Track preflights (tab creation + content_script readiness)
        for pf in state.get('preflights', []):
            jid = pf.get('job_id')
            job = next((j for j in state['jobs'] if j['id'] == jid), None)
            if not job or job.get('asset_id') not in BATCH_ASSETS:
                continue
            asset_id = job['asset_id']
            pf_status = pf.get('status')
            key = f'preflight_{pf_status}_ms'
            if key not in asset_events[asset_id]:
                now_ms = _ms(wall0)
                print(f'  [{now_ms:6d}ms] {asset_id.split("_")[0]} → preflight.{pf_status}'
                      f'  tab_id={pf.get("tab_id")}')
                asset_events[asset_id][key] = now_ms
                asset_events[asset_id]['tab_id'] = pf.get('tab_id')
                asset_events[asset_id]['window_id'] = pf.get('window_id')

        # Done when all dispatched assets have a 'valid' preflight
        valid_count = sum(
            1 for aid in BATCH_ASSETS
            if f'preflight_valid_ms' in asset_events[aid])
        failed_count = sum(
            1 for aid in BATCH_ASSETS
            if 'error' in asset_events[aid])

        if valid_count + failed_count == len(dispatched):
            break

        time.sleep(POLL_INTERVAL)

    t_end = time.perf_counter()
    total_ms = int((t_end - wall0) * 1000)

    # ── 6. Report ─────────────────────────────────────────────────────────────
    print('\n' + '=' * 64)
    print(' RESULTS')
    print('=' * 64)
    print(f'\nextension.agent_protocol_version : {ext_info["version"]}')
    print(f'extension.capabilities           : {ext_info["capabilities"]}')
    print(f'\nbatch_id                         : {batch_id}')
    print(f'batch_authorization_ms           : {auth_ms}')
    print(f'dispatch_ms                      : {dispatch_ms}')

    tab_ids = {}
    for aid in BATCH_ASSETS:
        ev = asset_events[aid]
        print(f'\n  {aid}')
        print(f'    request_id        : {req_by_asset.get(aid, "SKIPPED")}')
        print(f'    tab_id            : {ev.get("tab_id", "?")}')
        print(f'    window_id         : {ev.get("window_id", "?")}')
        for k, v in sorted(ev.items()):
            if k.endswith('_ms'):
                print(f'    {k:<30}: {v} ms')
        if 'error' in ev:
            print(f'    ERROR             : {ev["error"]}')
        if ev.get('tab_id'):
            tab_ids[aid] = ev['tab_id']

    # Aggregate metrics
    valid_assets = [a for a in BATCH_ASSETS if f'preflight_valid_ms' in asset_events[a]]
    if valid_assets:
        first_pf = min(asset_events[a]['preflight_valid_ms'] for a in valid_assets)
        last_pf = max(asset_events[a]['preflight_valid_ms'] for a in valid_assets)
        print(f'\nfirst_preflight_ready_ms         : {first_pf}')
        print(f'all_preflights_ready_ms          : {last_pf}')

    # Parallelism evidence: compare tab creation start times
    request_checking_times = {a: asset_events[a].get('request_checking_ms')
                               for a in BATCH_ASSETS
                               if asset_events[a].get('request_checking_ms')}
    if len(request_checking_times) >= 2:
        times = sorted(request_checking_times.values())
        spread = times[-1] - times[0]
        print(f'\nparallelism — tab creation spread : {spread} ms'
              f'  (0 = perfectly simultaneous, <2000 = overlapping)')
        print(f'parallelism — times per asset    :')
        for aid, t in sorted(request_checking_times.items(), key=lambda x: x[1]):
            print(f'  {aid.split("_")[0]}: {t} ms')
        if spread < 2000:
            print('  -> PARALLEL confirmed (spread < 2s)')
        else:
            print('  -> SEQUENTIAL detected (spread >= 2s)')

    # Over-1s phases
    print(f'\ntotal_ms                         : {total_ms}')
    print('\nPhases > 1000ms:')
    slow = []
    for aid in BATCH_ASSETS:
        ev = asset_events[aid]
        checking = ev.get('request_checking_ms', 0)
        valid = ev.get('preflight_valid_ms', 0)
        if checking and valid:
            tab_creation_ms = valid - checking
            if tab_creation_ms > 1000:
                slow.append((aid, 'tab_creation', tab_creation_ms))
    if slow:
        for aid, phase, ms in slow:
            print(f'  {aid.split("_")[0]} {phase}: {ms} ms')
    else:
        print('  (none detected)')

    # Safety confirmation
    state_final = browser_queue.load()
    unsafe = [j for j in state_final['jobs']
              if j.get('asset_id') in BATCH_ASSETS
              and j.get('status') in {'preparing', 'submitting', 'generating', 'receiving'}]
    print(f'\nZero uploads / prompts / submissions : '
          f'{"CONFIRMED" if not unsafe else "VIOLATED — " + str([j["asset_id"] for j in unsafe])}')

    if not valid_assets:
        print('\n[OUTCOME] No preflights reached ready. Check extension connection and reload.')
    elif len(valid_assets) < len(dispatched):
        failed = [a for a in BATCH_ASSETS if 'error' in asset_events[a]]
        print(f'\n[OUTCOME] Partial: {len(valid_assets)} ready, {len(failed)} failed: {failed}')
    else:
        print(f'\n[OUTCOME] All {len(valid_assets)} preflights ready. Batch is primed for submission.')
        print('          Call dispatch/execute when ready. No submission has occurred.')


if __name__ == '__main__':
    run()
