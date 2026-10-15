#!/usr/bin/env bash
# Prepara a pos-producao (skills edicao, anuncio-app e manifesto) em HyperFrames.
# Roda em segundo plano no SessionStart da nuvem e pode rodar na mao num Mac/Linux.
# Pede Node 22+ e FFmpeg, que a nuvem ja traz. Instala:
#   - CLI hyperframes (cache do npx) e o Chrome Headless Shell de render
#   - whisper-cli (whisper.cpp) e os modelos ggml-small.en / ggml-small, para tempo por palavra
# Idempotente: o que ja existe e pulado. Log em ${TMPDIR:-/tmp}/preparar_hyperframes.log.
set -uo pipefail
HF_VERSION="${HF_VERSION:-0.8.153}"  # a versao que acabamento.py e legendas_hf.py chamam (evita baixar no meio da edicao)
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

# Repo heygen-com/hyperframes, como no Mac do Luigi (pedido dele, 2026-10-15): clone em ~/ferramentas/hyperframes
# e as skills dele no usuario (npx skills add heygen-com/hyperframes -g), que a edicao consulta primeiro.
HF_REPO_DIR="${HF_REPO_DIR:-$HOME/ferramentas/hyperframes}"
[ -d "$HF_REPO_DIR/.git" ] || git clone -q --depth 1 https://github.com/heygen-com/hyperframes.git "$HF_REPO_DIR"
[ -d "$HOME/.agents/skills/hyperframes" ] || npx -y skills add heygen-com/hyperframes -g -y

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
# Editor (skill edicao) igual ao do Mac: WhisperX (alinhamento palavra por palavra) e OpenCV (zoom nos picos) num
# .venv-operacao que o editar.py usa sozinho. Torch so de CPU (a roda CUDA do PyPI e gigante e nao serve aqui).
# Sem isto o editor da nuvem cortava pelo metodo antigo e parava no zoom (2026-10-15).
repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
venv="$repo/.venv-operacao"
if ! "$venv/bin/python" -c "import whisperx, cv2" 2>/dev/null; then
  python3 -m venv --system-site-packages "$venv" \
    && "$venv/bin/python" -m pip install -q --index-url https://download.pytorch.org/whl/cpu \
         --extra-index-url https://pypi.org/simple torch==2.8.0 torchaudio==2.8.0 whisperx==3.8.6 opencv-python-headless
fi
# Modelo do alinhador (360 MB): o proxy ja cortou o download no meio e o arquivo truncado derrubava o alinhamento
# em silencio. Baixa aqui, confere abrindo e baixa de novo se vier quebrado.
for tentativa in 1 2 3; do
  "$venv/bin/python" -c "import whisperx; whisperx.load_align_model(language_code='en', device='cpu')" && break
  rm -f "$HOME/.cache/torch/hub/checkpoints/wav2vec2_fairseq_base_ls960_asr_ls960.pth"
done
# O alinhador separa frases com o punkt_tab do NLTK; o NLTK recusa baixar atras do proxy da nuvem sem este opt-in
# (o proxy e o da propria sessao) e o alinhamento falhava em todos os takes.
[ -d "$HOME/nltk_data/tokenizers/punkt_tab" ] || NLTK_ALLOW_PROXIED_URLOPEN=1 "$venv/bin/python" -c "import nltk; nltk.download('punkt_tab', quiet=True)"
echo "HyperFrames $HF_VERSION pronto; modelos whisper em $WHISPER_HOME/models; editor com WhisperX em $venv"
