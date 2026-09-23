"""Tests for studio/bridge.py — ensure_bridge() and route surface."""
import unittest
from unittest.mock import MagicMock, patch, call

import httpx

from . import bridge as br

_fastapi_available = br._FASTAPI_AVAILABLE


@unittest.skipUnless(_fastapi_available, "fastapi not installed — run: pip install fastapi uvicorn")
class BridgeRoutesTests(unittest.TestCase):
    """Verify that the FastAPI app exposes exactly the /api/browser/* routes needed
    by the Chrome extension, and nothing else (no UI, no /app routes)."""

    def _paths(self):
        return {r.path for r in br.app.routes}

    def test_all_required_browser_routes_present(self):
        paths = self._paths()
        required = {
            "/api/browser/queue",
            "/api/browser/control",
            "/api/browser/authorize-batch",
            "/api/browser/dispatch-batch/{batch_id}",
            "/api/browser/batch/{batch_id}",
            "/api/browser/claim",
            "/api/browser/activate-materialized",
            "/api/browser/receive/{job_id}",
            "/api/browser/reference/{job_id}",
            "/api/browser/review/{job_id}",
            "/api/browser/download/{job_id}",
            "/api/browser/preflight/register",
            "/api/browser/preflight/request",
            "/api/browser/heartbeat",
        }
        missing = required - paths
        self.assertEqual(missing, set(), f"Missing routes: {missing}")

    def test_no_ui_routes(self):
        paths = self._paths()
        ui_prefixes = ("/app", "/static", "/ui", "/dashboard")
        bad = [p for p in paths if any(p.startswith(pfx) for pfx in ui_prefixes)]
        self.assertEqual(bad, [], f"UI routes must not be present: {bad}")

    def test_no_docs_routes(self):
        paths = self._paths()
        self.assertNotIn("/docs", paths)
        self.assertNotIn("/redoc", paths)


class EnsureBridgeTests(unittest.TestCase):
    """Tests for ensure_bridge() using mocks — zero real processes or ports."""

    def setUp(self):
        self._port = br.BRIDGE_PORT

    def _url(self):
        return f"http://127.0.0.1:{self._port}"

    @patch("studio.bridge.subprocess.Popen")
    @patch("studio.bridge.httpx.get")
    def test_bridge_starts_when_not_running(self, mock_get, mock_popen):
        # First call: not running. Second call (inside loop): healthy.
        mock_get.side_effect = [
            httpx.ConnectError("refused"),   # initial check
            MagicMock(status_code=200),      # health check after Popen
        ]
        url = br.ensure_bridge(timeout=5.0)
        self.assertEqual(url, br.BRIDGE_URL)
        mock_popen.assert_called_once()

    @patch("studio.bridge.subprocess.Popen")
    @patch("studio.bridge.httpx.get")
    def test_bridge_reused_when_already_healthy(self, mock_get, mock_popen):
        # Bridge responds immediately — no subprocess spawned.
        mock_get.return_value = MagicMock(status_code=200)
        url = br.ensure_bridge(timeout=5.0)
        self.assertEqual(url, br.BRIDGE_URL)
        mock_popen.assert_not_called()

    @patch("studio.bridge.time.sleep")
    @patch("studio.bridge.subprocess.Popen")
    @patch("studio.bridge.httpx.get")
    def test_bridge_waits_for_health_before_returning(self, mock_get, mock_popen, mock_sleep):
        # First check: not running. Next 3 checks: still starting. Then: healthy.
        mock_get.side_effect = [
            httpx.ConnectError("refused"),      # initial check
            httpx.ConnectError("still starting"),
            httpx.ConnectError("still starting"),
            MagicMock(status_code=200),         # healthy on 4th try
        ]
        url = br.ensure_bridge(timeout=10.0)
        self.assertEqual(url, br.BRIDGE_URL)
        # sleep called between health polls
        self.assertGreaterEqual(mock_sleep.call_count, 2)

    @patch("studio.bridge.time.time")
    @patch("studio.bridge.time.sleep")
    @patch("studio.bridge.subprocess.Popen")
    @patch("studio.bridge.httpx.get")
    def test_timeout_raises_clearly(self, mock_get, mock_popen, mock_sleep, mock_time):
        # Simulate: initial check fails, then time immediately runs out.
        mock_get.side_effect = httpx.ConnectError("always refused")
        # time.time(): first call sets deadline (t=0), second call is past deadline (t=999).
        mock_time.side_effect = [0.0, 999.0]
        with self.assertRaises(RuntimeError) as ctx:
            br.ensure_bridge(timeout=5.0)
        self.assertIn(str(self._port), str(ctx.exception))

    @patch("studio.bridge.subprocess.Popen")
    @patch("studio.bridge.httpx.get")
    def test_two_consecutive_calls_spawn_one_process(self, mock_get, mock_popen):
        # First call: not running, then starts. Second call: already healthy.
        call_count = [0]
        def side_effect(*args, **kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                raise httpx.ConnectError("refused")  # initial check, call 1
            return MagicMock(status_code=200)         # healthy for all subsequent calls

        mock_get.side_effect = side_effect
        br.ensure_bridge(timeout=5.0)
        br.ensure_bridge(timeout=5.0)
        # Popen called exactly once — second call found bridge healthy
        mock_popen.assert_called_once()

    @patch("studio.bridge._port_occupied_by_other")
    @patch("studio.bridge.subprocess.Popen")
    @patch("studio.bridge.httpx.get")
    def test_port_occupied_by_incompatible_process_raises_immediately(
            self, mock_get, mock_popen, mock_port_occupied):
        mock_get.side_effect = httpx.ConnectError("refused")
        mock_port_occupied.return_value = True  # port occupied, not our bridge
        with self.assertRaises(RuntimeError) as ctx:
            br.ensure_bridge(timeout=5.0)
        self.assertIn(str(self._port), str(ctx.exception))
        self.assertIn("incompatible", str(ctx.exception))
        mock_popen.assert_not_called()  # must not kill or override unknown process

    @patch("studio.bridge.subprocess.Popen")
    @patch("studio.bridge.httpx.get")
    def test_popen_called_with_correct_module(self, mock_get, mock_popen):
        mock_get.side_effect = [
            httpx.ConnectError("refused"),
            MagicMock(status_code=200),
        ]
        br.ensure_bridge(timeout=5.0)
        args = mock_popen.call_args[0][0]  # first positional arg = command list
        self.assertIn("studio.bridge", args)

    @patch("studio.bridge.subprocess.Popen")
    @patch("studio.bridge.httpx.get")
    def test_no_studio_app_dependency(self, mock_get, mock_popen):
        """Bridge must start independently — no dependency on studio.app."""
        mock_get.side_effect = [
            httpx.ConnectError("refused"),
            MagicMock(status_code=200),
        ]
        br.ensure_bridge(timeout=5.0)
        args = mock_popen.call_args[0][0]
        self.assertNotIn("studio.app", args)


class PortOccupiedByOtherTests(unittest.TestCase):
    @patch("studio.bridge.httpx.get")
    @patch("studio.bridge.socket.socket")
    def test_free_port_returns_false(self, mock_socket_cls, mock_get):
        mock_socket = MagicMock()
        mock_socket.__enter__ = lambda s: s
        mock_socket.__exit__ = MagicMock(return_value=False)
        mock_socket.connect_ex.return_value = 1  # ECONNREFUSED = port free
        mock_socket_cls.return_value = mock_socket
        result = br._port_occupied_by_other(9999)
        self.assertFalse(result)

    @patch("studio.bridge.httpx.get")
    @patch("studio.bridge.socket.socket")
    def test_our_bridge_on_port_returns_false(self, mock_socket_cls, mock_get):
        mock_socket = MagicMock()
        mock_socket.__enter__ = lambda s: s
        mock_socket.__exit__ = MagicMock(return_value=False)
        mock_socket.connect_ex.return_value = 0  # port in use
        mock_socket_cls.return_value = mock_socket
        mock_get.return_value = MagicMock(status_code=200)  # our bridge responds
        result = br._port_occupied_by_other(9999)
        self.assertFalse(result)

    @patch("studio.bridge.httpx.get")
    @patch("studio.bridge.socket.socket")
    def test_foreign_process_on_port_returns_true(self, mock_socket_cls, mock_get):
        mock_socket = MagicMock()
        mock_socket.__enter__ = lambda s: s
        mock_socket.__exit__ = MagicMock(return_value=False)
        mock_socket.connect_ex.return_value = 0  # port in use
        mock_socket_cls.return_value = mock_socket
        mock_get.side_effect = Exception("not our bridge")
        result = br._port_occupied_by_other(9999)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
