#!/usr/bin/env bash
# run_watch.sh · roda o pipeline do /watch no macOS/Linux (2026-09-24), equivalente ao run_watch.ps1.
# Uso:  bash .claude/skills/watch/scripts/run_watch.sh "CAMINHO/DO/VIDEO.mp4" [--outdir PASTA] [opcoes extras]
set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Uso: bash run_watch.sh VIDEO.mp4 [--outdir PASTA] [--model medium.en] [...]" >&2
    exit 1
fi

aqui="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
raiz="$(cd "$aqui/../../../.." && pwd)"
# Numa worktree a .venv mora no checkout principal.
if comum="$(git -C "$raiz" rev-parse --path-format=absolute --git-common-dir 2>/dev/null)"; then
    principal="$(dirname "$comum")"
else
    principal="$raiz"
fi

py=""
for cand in "$raiz/.venv/bin/python" "$principal/.venv/bin/python"; do
    if [ -x "$cand" ]; then py="$cand"; break; fi
done
# Na nuvem (claude.ai/code) nao ha .venv: o SessionStart instala as
# dependencias no Python do sistema, entao usar ele direto.
if [ -z "$py" ] && command -v python3 >/dev/null 2>&1 \
        && python3 -c "import PIL" >/dev/null 2>&1; then
    py="$(command -v python3)"
fi
if [ -z "$py" ]; then
    echo "ERRO: .venv nao encontrada. Rodar antes: bash .claude/skills/watch/scripts/setup_mac.sh" >&2
    exit 1
fi
for bin in ffmpeg ffprobe; do
    command -v "$bin" >/dev/null 2>&1 || { echo "ERRO: $bin nao encontrado. Rodar setup_mac.sh." >&2; exit 1; }
done

video="$1"; shift
exec "$py" "$aqui/watch_pipeline.py" --video "$video" "$@"
