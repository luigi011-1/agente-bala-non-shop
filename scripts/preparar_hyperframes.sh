#!/usr/bin/env bash
# Prepara a pos-producao (skills edicao, anuncio-app e manifesto) em HyperFrames.
# Roda em segundo plano no SessionStart da nuvem e pode rodar na mao num Mac/Linux.
# Pede Node 22+ e FFmpeg, que a nuvem ja traz. Instala:
#   - CLI hyperframes (cache do npx) e o Chrome Headless Shell de render
#   - whisper-cli (whisper.cpp) e os modelos ggml-small.en / ggml-small, para tempo por palavra
# Idempotente: o que ja existe e pulado. Log em ${TMPDIR:-/tmp}/preparar_hyperframes.log.
set -uo pipefail
HF_VERSION="${HF_VERSION:-0.8.143}"
WHISPER_TAG="${WHISPER_TAG:-v1.9.5}"
WHISPER_HOME="${WHISPER_HOME:-$HOME/.cache/whisper-cpp}"
log="${TMPDIR:-/tmp}/preparar_hyperframes.log"
exec >>"$log" 2>&1
echo "== $(date -u +%FT%TZ) preparar_hyperframes"

node_major="$(node -p 'process.versions.node.split(".")[0]' 2>/dev/null || echo 0)"
if [ "$node_major" -lt 22 ]; then echo "Node 22+ ausente (achei $node_major)"; exit 0; fi
command -v ffmpeg >/dev/null || { echo "FFmpeg ausente"; exit 0; }

npx -y "hyperframes@$HF_VERSION" --version
npx -y "hyperframes@$HF_VERSION" browser ensure

if ! command -v whisper-cli >/dev/null; then
  src="$WHISPER_HOME/src"
  [ -d "$src/.git" ] || git clone -q --depth 1 --branch "$WHISPER_TAG" https://github.com/ggml-org/whisper.cpp.git "$src"
  cmake -S "$src" -B "$src/build" -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DWHISPER_BUILD_TESTS=OFF \
    && cmake --build "$src/build" -j --target whisper-cli \
    && install -m 755 "$src/build/bin/whisper-cli" "${WHISPER_BIN_DIR:-/usr/local/bin}/whisper-cli"
fi

mkdir -p "$WHISPER_HOME/models"
for m in small.en small; do
  f="$WHISPER_HOME/models/ggml-$m.bin"
  if [ ! -s "$f" ]; then
    curl -fsSL -o "$f.part" "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-$m.bin" && mv "$f.part" "$f"
  fi
done
echo "HyperFrames $HF_VERSION pronto; modelos whisper em $WHISPER_HOME/models"
