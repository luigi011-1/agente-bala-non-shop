#!/usr/bin/env bash
# macOS/Linux entry point; .venv-operacao is prepared by scripts/preparar_operacao.py.
set -euo pipefail
if [ "$#" -lt 1 ]; then
  echo "Uso: bash run_watch.sh VIDEO.mp4 [--alignment whisperx] [opcoes]" >&2
  exit 2
fi
watch_scripts="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
watch_root="$(cd "$watch_scripts/../../../.." && pwd -P)"
watch_principal="$watch_root"
if watch_common="$(git -C "$watch_root" rev-parse --path-format=absolute --git-common-dir 2>/dev/null)"; then
  watch_principal="$(dirname "$watch_common")"
fi
watch_python=""
if [ -n "${BALA_PYTHON:-}" ]; then
  watch_python="$BALA_PYTHON"
else
  for watch_candidate in "$watch_root/.venv-operacao/bin/python" "$watch_principal/.venv-operacao/bin/python" "$watch_root/.venv/bin/python" "$watch_principal/.venv/bin/python"; do
    if [ -x "$watch_candidate" ]; then watch_python="$watch_candidate"; break; fi
  done
fi
# Keep the existing cloud setup compatible, without mistaking the old macOS Python for a ready runtime.
if [ -z "$watch_python" ] && command -v python3 >/dev/null 2>&1 && python3 -c 'import PIL, faster_whisper' >/dev/null 2>&1; then
  watch_python="$(command -v python3)"
fi
if [ -z "$watch_python" ]; then
  echo "Ambiente ausente. Execute python3 scripts/preparar_operacao.py no checkout." >&2
  exit 2
fi
watch_video="$1"
shift
exec "$watch_python" "$watch_scripts/watch_pipeline.py" --video "$watch_video" "$@"
