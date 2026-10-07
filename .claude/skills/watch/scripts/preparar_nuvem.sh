#!/usr/bin/env bash
# Existing SessionStart hook: prepare the canonical /watch baseline and cache its ASR model.
# WhisperX is prepared by scripts/preparar_operacao.py, not downloaded on every cloud session.
set -euo pipefail
watch_model="${1:-small.en}"
watch_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
watch_log="${TMPDIR:-/tmp}/preparar_nuvem.log"
watch_python="${BALA_PYTHON:-python3}"
if [ -z "${BALA_PYTHON:-}" ] && [ -x "$watch_root/.venv-operacao/bin/python" ]; then
  watch_python="$watch_root/.venv-operacao/bin/python"
fi
if ! "$watch_python" - "$watch_root/.agents/skills/watch/requirements.txt" <<'CHECK_DEPS'
import importlib.metadata as metadata
from pathlib import Path
import sys
try:
    for row in Path(sys.argv[1]).read_text().splitlines():
        if row.strip() and not row.startswith("#"):
            package, expected = row.split("==", 1)
            if metadata.version(package) != expected:
                raise ValueError("Versao diferente: " + package)
except (metadata.PackageNotFoundError, ValueError):
    sys.exit(1)
CHECK_DEPS
then
  "$watch_python" -m pip install -q -r "$watch_root/.agents/skills/watch/requirements.txt" >>"$watch_log" 2>&1
fi
if [ "${SO_DEPS:-0}" = "1" ]; then exit 0; fi
"$watch_python" - "$watch_model" >>"$watch_log" 2>&1 <<'WATCH_PY'
import os
import sys
os.environ.setdefault("HF_HUB_ETAG_TIMEOUT", "10")
os.environ.setdefault("HF_HUB_DOWNLOAD_TIMEOUT", "30")
from faster_whisper.utils import download_model
model = sys.argv[1]
try:
    download_model(model, local_files_only=True)
except Exception:
    download_model(model)
print(f"Whisper {model} pronto no cache")
WATCH_PY
