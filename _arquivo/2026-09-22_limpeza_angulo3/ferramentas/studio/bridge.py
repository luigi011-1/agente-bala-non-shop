"""Headless FastAPI bridge — only /api/browser/* routes.

Started automatically by ensure_bridge(). No UI, no static files, no /app routes.
All endpoints delegate to browser_queue; no logic is duplicated here.

The FastAPI server portion requires: pip install fastapi uvicorn httpx
ensure_bridge() itself only requires httpx (and subprocess/socket from stdlib).

Usage:
    python -m studio.bridge               # direct start (port 8765)
    from studio.bridge import ensure_bridge; url = ensure_bridge()
"""
from __future__ import annotations

import os
import socket
import subprocess
import sys
import time
from pathlib import Path

import httpx

BRIDGE_PORT = int(os.environ.get("STUDIO_BRIDGE_PORT", "8765"))
BRIDGE_URL = f"http://127.0.0.1:{BRIDGE_PORT}"
HEALTH_PATH = "/api/browser/queue"

# ── FastAPI server (optional — only needed when running as the bridge subprocess) ─

try:
    from fastapi import FastAPI, HTTPException, Request
    from fastapi.responses import FileResponse
    _FASTAPI_AVAILABLE = True
except ImportError:
    _FASTAPI_AVAILABLE = False

if _FASTAPI_AVAILABLE:
    from . import browser_queue as bq

    app = FastAPI(title="Auraly Studio Bridge", docs_url=None, redoc_url=None)

    @app.get("/api/browser/queue")
    def get_queue():
        return bq.load()

    @app.post("/api/browser/control")
    def control(body: dict):
        return bq.control(body.get("enabled", True), body.get("concurrency"))

    @app.post("/api/browser/authorize-batch")
    def authorize_batch(body: dict):
        try:
            return bq.authorize_batch(
                production_id=body["production_id"],
                pipeline=body["pipeline"],
                avatar_id=body["avatar_id"],
                asset_fingerprints=body["asset_fingerprints"],
                allow_activation=body.get("allow_activation", True),
            )
        except (KeyError, ValueError) as e:
            raise HTTPException(status_code=400, detail=str(e))

    @app.post("/api/browser/dispatch-batch/{batch_id}")
    def dispatch_batch(batch_id: str):
        try:
            return bq.dispatch_batch(batch_id)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @app.get("/api/browser/batch/{batch_id}")
    def get_batch(batch_id: str):
        try:
            return bq.get_batch(batch_id)
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    @app.post("/api/browser/claim")
    def claim():
        return bq.claim() or {}

    @app.post("/api/browser/activate-materialized")
    def activate_materialized(body: dict):
        try:
            return bq.activate_materialized(
                job_id=body["job_id"],
                canonical_asset_fingerprint=body["canonical_asset_fingerprint"],
                preflight_id=body["preflight_id"],
                preflight_report=body["preflight_report"],
            )
        except (KeyError, ValueError) as e:
            raise HTTPException(status_code=400, detail=str(e))

    @app.post("/api/browser/update/{job_id}")
    def update_job(job_id: str, body: dict):
        try:
            return bq.update(job_id, body["status"],
                             **{k: v for k, v in body.items() if k != "status"})
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @app.post("/api/browser/receive/{job_id}")
    async def receive(job_id: str, request: Request):
        body = await request.body()
        try:
            return bq.receive(job_id, body)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @app.post("/api/browser/reference/{job_id}")
    def reference(job_id: str, body: dict):
        try:
            return bq.reference(job_id, body["role"])
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @app.post("/api/browser/review/{job_id}")
    def review_job(job_id: str, body: dict):
        try:
            return bq.review(job_id, body["decision"])
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @app.get("/api/browser/download/{job_id}")
    def download(job_id: str):
        job = bq.get_job(job_id)
        path = job.get("local_file") if job else None
        if not path or not Path(path).exists():
            raise HTTPException(status_code=404, detail="file not found")
        return FileResponse(path)

    @app.post("/api/browser/preflight/register")
    def register_preflight(body: dict):
        try:
            return bq.register_preflight(body)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @app.post("/api/browser/preflight/request")
    def request_preflight(body: dict):
        try:
            return bq.request_preflight(body["job_id"], body["canonical_asset_fingerprint"])
        except (KeyError, ValueError) as e:
            raise HTTPException(status_code=400, detail=str(e))

    @app.post("/api/browser/heartbeat")
    def heartbeat(body: dict):
        return bq.heartbeat(body.get("session_id", ""))

    # Agent compatibility surface: the extension uses this narrow contract directly.
    @app.post("/api/browser/agent/state")
    def agent_state(body: dict):
        return bq.heartbeat(body.get("extension_session_id"), body.get("agent_protocol_version"), body.get("agent_capabilities"))

    @app.post("/api/browser/agent/preflight")
    def agent_preflight(body: dict):
        return bq.register_preflight(body)

    @app.post("/api/browser/agent/preflight-requests/checking")
    def agent_preflight_checking(body: dict):
        return bq.mark_preflight_checking(body["request_id"], body["job_id"], body["canonical_asset_fingerprint"], body["extension_session_id"])

    @app.post("/api/browser/agent/preflight-requests/failed")
    def agent_preflight_failed(body: dict):
        return bq.fail_preflight_request(body["request_id"], body["extension_session_id"], body["error"])

    @app.post("/api/browser/agent/jobs/{job_id}/activate")
    def agent_activate(job_id: str, body: dict):
        return bq.activate_materialized(job_id, body["canonical_asset_fingerprint"], body["preflight_id"], body["revalidation"])

    @app.post("/api/browser/agent/claim")
    def agent_claim():
        return {"job": bq.claim()}

    @app.post("/api/browser/agent/jobs/{job_id}")
    def agent_update(job_id: str, body: dict):
        return bq.update(job_id, body["status"], tab_id=body.get("tab_id"), conversation_url=body.get("conversation_url"), error=body.get("error"))

    @app.get("/api/browser/agent/jobs/{job_id}/references/{role}")
    def agent_reference(job_id: str, role: str):
        return FileResponse(bq.reference(job_id, role), media_type="application/octet-stream")

    @app.post("/api/browser/agent/jobs/{job_id}/image")
    async def agent_image(job_id: str, request: Request):
        return bq.receive(job_id, await request.body())

else:
    app = None


# ── Process management (no fastapi dependency) ─────────────────────────────────

def _port_occupied_by_other(port: int) -> bool:
    """True when port is in use but does NOT respond to our health check."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        in_use = s.connect_ex(("127.0.0.1", port)) == 0
    if not in_use:
        return False
    try:
        httpx.get(f"http://127.0.0.1:{port}{HEALTH_PATH}", timeout=1.0)
        return False  # our bridge is responding
    except Exception:
        return True   # something else holds the port


def ensure_bridge(timeout: float = 10.0) -> str:
    """Start bridge subprocess if not running. Returns base URL.

    Idempotent: if the bridge is already healthy, returns immediately without
    spawning a second process.
    Raises RuntimeError if the bridge does not become healthy within `timeout` seconds.
    Raises RuntimeError immediately if the port is occupied by an incompatible process.
    """
    try:
        httpx.get(f"{BRIDGE_URL}{HEALTH_PATH}", timeout=1.0)
        return BRIDGE_URL
    except Exception:
        pass

    if _port_occupied_by_other(BRIDGE_PORT):
        raise RuntimeError(
            f"Port {BRIDGE_PORT} is occupied by an incompatible process. "
            "Set STUDIO_BRIDGE_PORT to a free port and retry."
        )

    env = {**os.environ, "STUDIO_BRIDGE_PORT": str(BRIDGE_PORT)}
    subprocess.Popen(
        [sys.executable, "-m", "studio.bridge"],
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            httpx.get(f"{BRIDGE_URL}{HEALTH_PATH}", timeout=1.0)
            return BRIDGE_URL
        except Exception:
            time.sleep(0.2)

    raise RuntimeError(
        f"Bridge did not become healthy within {timeout}s on port {BRIDGE_PORT}. "
        "Check STUDIO_BRIDGE_PORT and that 'fastapi' and 'uvicorn' are installed."
    )


if __name__ == "__main__":
    if not _FASTAPI_AVAILABLE:
        print("ERROR: fastapi and uvicorn are required to run the bridge server.", file=sys.stderr)
        print("Run: pip install fastapi uvicorn", file=sys.stderr)
        sys.exit(1)
    import uvicorn
    uvicorn.run("studio.bridge:app", host="127.0.0.1", port=BRIDGE_PORT, log_level="warning")
