#!/usr/bin/env bash
# Prepara a nuvem para o /watch: dependencias Python + modelo Whisper em cache.
# Idempotente e barato quando ja esta pronto. Usado pelo hook SessionStart e
# pode ser colado no "Setup script" do ambiente (ai o cache fica no snapshot).
# Uso: preparar_nuvem.sh [modelo]   (padrao: small.en)
# SO_DEPS=1 instala so as dependencias (rapido, sincrono no hook).
MODEL="${1:-small.en}"
DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG="${TMPDIR:-/tmp}/preparar_nuvem.log"

# 1) dependencias: so instala se faltar alguma
if ! python3 -c "import faster_whisper, PIL, av" >/dev/null 2>&1; then
  pip install -q -r "$DIR/requirements.txt" >>"$LOG" 2>&1
fi

[ "$SO_DEPS" = "1" ] && exit 0

# 2) modelo Whisper: so baixa se nao estiver no cache; falha de rede nao derruba nada
python3 - >>"$LOG" 2>&1 <<PY
import os
os.environ.setdefault("HF_HUB_ETAG_TIMEOUT", "10")
os.environ.setdefault("HF_HUB_DOWNLOAD_TIMEOUT", "30")
from faster_whisper.utils import download_model
try:
    download_model("$MODEL", local_files_only=True)
    print("whisper $MODEL ja em cache")
except Exception:
    try:
        download_model("$MODEL")
        print("whisper $MODEL baixado")
    except Exception as e:
        print("whisper $MODEL NAO baixou (rede bloqueada?):", type(e).__name__)
PY
exit 0
