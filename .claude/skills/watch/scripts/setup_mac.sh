#!/usr/bin/env bash
# setup_mac.sh · prepara a skill /watch no macOS (2026-09-24), equivalente ao setup_windows.ps1.
# Instala ffmpeg pelo Homebrew se faltar, cria a .venv-operacao na raiz do repo e instala as versoes
# validadas de requirements.txt. Uso, da raiz do repo:  bash .claude/skills/watch/scripts/setup_mac.sh
set -euo pipefail

aqui="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
raiz="$(cd "$aqui/../../../.." && pwd)"

if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v ffprobe >/dev/null 2>&1; then
    if command -v brew >/dev/null 2>&1; then
        echo "Instalando ffmpeg pelo Homebrew..."
        brew install ffmpeg
    else
        echo "ERRO: ffmpeg nao encontrado e o Homebrew nao esta instalado." >&2
        echo "      Instalar o Homebrew (https://brew.sh) e rodar de novo." >&2
        exit 1
    fi
fi

# O python3 que vem no macOS e o 3.9, velho demais para as versoes fixadas (Pillow 12 pede 3.10+).
# A .venv-operacao validada em 2026-09-24 usa o python@3.12 do Homebrew.
py=""
for cand in python3.12 /opt/homebrew/bin/python3.12 /usr/local/bin/python3.12; do
    if command -v "$cand" >/dev/null 2>&1; then py="$(command -v "$cand")"; break; fi
done
if [ -z "$py" ]; then
    if command -v brew >/dev/null 2>&1; then
        echo "Instalando python@3.12 pelo Homebrew..."
        brew install python@3.12
        py="$(brew --prefix python@3.12)/bin/python3.12"
    else
        echo "ERRO: Python 3.12 nao encontrado e o Homebrew nao esta instalado." >&2
        exit 1
    fi
fi

if [ ! -x "$raiz/.venv-operacao/bin/python" ]; then
    echo "Criando a .venv-operacao em $raiz/.venv-operacao com $py ..."
    "$py" -m venv "$raiz/.venv-operacao"
fi

"$raiz/.venv-operacao/bin/python" -m pip install --upgrade pip >/dev/null
"$raiz/.venv-operacao/bin/python" -m pip install -r "$aqui/../requirements.txt"
"$raiz/.venv-operacao/bin/python" -c "import faster_whisper, PIL, av; print('watch pronto: faster-whisper, Pillow e av instalados')"
