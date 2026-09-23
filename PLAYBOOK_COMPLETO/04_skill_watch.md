# 04 — A Skill `/watch` (nossa ferramenta de decomposição)

> **Lembrete:** a `/watch` serve para decompor vídeos modelo que serão clonados com **avatares de IA — pessoas que não existem**.

Este documento conta **por que** criamos a `/watch`, **como** ela foi construída, **o que** ela faz por baixo, **quais programas** foram instalados, **como usá-la**, e **quais são suas limitações honestas**. O usuário pediu especificamente para registrar todo esse processo.

---

## 1. Por que a `/watch` existe (o problema que ela resolve)

A etapa mais crítica e mais fácil de fazer mal feito é a **decomposição** do vídeo modelo (Fase 2 do processo — ver documento 05). O método antigo era **extrair frames esparsos** (por exemplo, 1 frame por segundo) e montar grades de miniaturas minúsculas.

Esse método antigo tinha uma falha grave: **ele perdia reveals que acontecem dentro de um take.**

Exemplo real: num vídeo de "canela dissolve o açúcar", o avatar despejava líquido na barriga de uma pessoa deitada (pessoa de IA, não real), a "gordura" de cristais derretia e revelava que embaixo havia gomos de abdômen. Esse reveal — o momento em que os gomos aparecem — **durava uma fração de segundo**. Com extração a 1 frame por segundo, você pegava o frame *antes* e o frame *depois*, mas **pulava o instante do reveal**. Resultado: a decomposição não registrava que existia uma transformação ali, e o clone saía sem o close da barriga — matando o herói do vídeo.

Além disso, as miniaturas minúsculas (240 pixels de largura) escondiam detalhe. "Gomos aparecendo sob cristais derretendo" é invisível numa miniatura daquele tamanho.

**A conclusão importante:** o erro não era falta de áudio nem falta de "assistir de verdade". O erro era **amostragem esparsa** e **miniaturas pequenas demais**. A `/watch` conserta exatamente esses dois problemas.

---

## 2. A conversa honesta sobre "assistir o vídeo de verdade"

O pedido inicial foi: *"quero que você assista o vídeo com áudio de verdade, não só extraia frames."*

A resposta honesta é: **nenhuma IA assiste um vídeo continuamente com olhos e ouvidos.** Quando qualquer IA "entende um vídeo", por baixo dos panos ela está **amostrando frames** (pegando quadros e olhando as imagens). O áudio, então, não é processado nativamente de jeito nenhum — precisa ser transcrito por um modelo de voz separado.

Então a `/watch` não é mágica. Ela é a **melhor aproximação real possível**:
- Amostragem de frames **tão densa** (a cada 0,2 segundo no vídeo inteiro) que nenhum reveal se perde.
- Detecção de **todos os cortes de cena** para nunca pular um take.
- Visualização em **resolução cheia** dos momentos-chave, não em miniatura.
- **Transcrição do áudio** com um modelo de voz (Whisper), com timestamps.

O resultado é idêntico, na prática, ao que "assistir de verdade" entregaria — mas pela via que realmente funciona.

---

## 3. Os programas instalados (a stack)

Para a `/watch` funcionar, foram instalados no computador (Windows):

| Programa | Versão | Papel |
|---|---|---|
| **Python** | 3.12.10 | Roda o script do pipeline |
| **ffmpeg / ffprobe** | 9.0 (Gyan) | Extrai frames e áudio; sonda o vídeo |
| **faster-whisper** | 1.2.1 | Transcreve o áudio na CPU (mais leve/rápido que o Whisper original) |
| **modelo `small.en`** | — | Modelo de transcrição em inglês, baixado no primeiro uso |
| **Pillow** | 12.3 | Monta as grades legíveis com rótulos de tempo |

### Comandos de instalação exatos (Windows / PowerShell)

```powershell
# Python 3.12 em escopo de usuário
winget install --id Python.Python.3.12 -e --scope user --silent --accept-package-agreements --accept-source-agreements

# ffmpeg (build completo do Gyan)
winget install --id Gyan.FFmpeg -e --silent --accept-package-agreements --accept-source-agreements

# bibliotecas Python
python -m pip install faster-whisper Pillow
```

O modelo `small.en` foi pré-baixado uma vez para o primeiro `/watch` já sair rápido, rodando:

```powershell
python -c "from faster_whisper import WhisperModel; m = WhisperModel('small.en', device='cpu', compute_type='int8'); print('modelo pronto')"
```

> **Se for reinstalar em outra máquina:** os mesmos comandos acima resolvem. Se não houver `winget`, instale o Python pelo site python.org e o ffmpeg baixando o build estático (zip) e apontando o PATH para a pasta `bin`.

---

## 4. Como a `/watch` foi construída (o processo)

A construção seguiu esta sequência:

1. **Verificação do ambiente** — descobrimos que a máquina não tinha `ffmpeg`, nem Python de verdade (só um atalho vazio da Microsoft Store), nem `pip`. Mas tinha `winget`.
2. **Instalação da stack** — Python, ffmpeg, faster-whisper, Pillow (comandos acima).
3. **Escrita do script do pipeline** (`watch_pipeline.py`) — o coração da ferramenta.
4. **Escrita de um wrapper** (`run_watch.ps1`) — que recarrega o PATH e chama o script.
5. **Escrita do `SKILL.md`** — o documento de instruções que a IA segue ao rodar `/watch`, amarrando o pipeline técnico à disciplina de análise (frame a frame, sem pattern-matching, confirmar o herói).
6. **Teste com vídeo sintético** — geramos um vídeo de teste com ffmpeg e rodamos o pipeline, corrigindo dois bugs no caminho:
   - `-vsync` foi removido no ffmpeg 9.0 → trocado por `-fps_mode`.
   - O `:` do caminho do Windows (`C:/...`) era interpretado como separador dentro do filtergraph do ffmpeg → resolvido rodando o ffmpeg com o diretório de trabalho na pasta de saída e usando nomes relativos.
7. **Refinamento** — inicialmente a extração densa era só no hook (0,2s) e o resto da timeline mais esparso (0,5s). O usuário pediu **densidade uniforme de 0,2s no vídeo inteiro** (para pegar reveals no corpo e no CTA também), e o script foi ajustado.

---

## 5. O que a `/watch` faz (o pipeline)

A partir de um `.mp4`, numa única execução:

1. **Sonda o vídeo** (ffprobe): duração, fps, resolução, se tem áudio.
2. **Detecta cada corte de cena**: extrai um frame em cada mudança de take → o mapa de takes.
3. **Extrai a timeline inteira densa**: 5 frames por segundo (1 a cada 0,2 segundo) no vídeo **completo** — pega reveals dentro de qualquer take (hook, corpo, CTA).
4. **Transcreve o áudio** com faster-whisper, com timestamps por segmento.
5. **Monta grades legíveis** (Pillow): tiles grandes (360px) com o rótulo de tempo (ex.: `t=3.40s`) em cada quadro. Timeline em folhas de 20 tiles.
6. **Escreve** `manifest.json` (índice de tudo) + `transcript.txt` e `transcript.json`.

### Estrutura de saída

Tudo vai para `<pasta_do_video>/<nome>_watch/`:

```
<nome>_watch/
├── frames/
│   ├── scenes/      → 1 frame por corte de cena (scene_t0002.00.png, ...)
│   └── timeline/    → vídeo inteiro a 0,2s (tl_t0000.00.png, tl_t0000.20.png, ...)
├── audio/
│   ├── audio.wav
│   ├── transcript.txt   → fala com timestamps, legível
│   └── transcript.json
├── overview/
│   ├── overview_scenes_01.png     → grade do mapa de cenas
│   └── overview_timeline_01.png…  → grades densas da timeline inteira
└── manifest.json    → índice de tudo, com timestamps
```

Os nomes dos frames trazem o timestamp embutido (ex.: `tl_t0003.40.png` = o frame de t=3,40s), o que torna trivial referenciar "o frame em t=3,4s".

---

## 6. Como usar a `/watch`

Comando básico:

```
powershell -File ".claude/skills/watch/scripts/run_watch.ps1" -Video "CAMINHO_DO_VIDEO.mp4"
```

Ou apontando uma pasta de saída específica:

```
powershell -File ".claude/skills/watch/scripts/run_watch.ps1" -Video "CAMINHO.mp4" -OutDir "entradas/nome_do_video_watch"
```

**Opções úteis** (passadas via `-Extra`):
- `--model medium.en` → transcrição mais precisa (mais lenta na CPU).
- `--timeline-fps 10` → densidade ainda maior (0,1s por frame) para vídeos com reveals muito rápidos.
- `--scene-threshold 0.15` → detecta cortes de cena mais sutis.
- `--no-audio` → pula a transcrição.

### O fluxo de análise depois de rodar (o que a IA faz com a saída)

1. Lê a **transcrição** (`audio/transcript.txt`) — a fala beat a beat com tempo.
2. Lê as **grades de visão geral** em resolução cheia, nesta ordem:
   - `overview_scenes_*` → entende o arco/estrutura (quantos takes, o que é cada um).
   - `overview_timeline_*` → varre o vídeo inteiro em sequência (0,2s por frame), com **atenção máxima aos primeiros 6-8 segundos (o hook)**, mas varrendo também corpo e CTA procurando **mudanças dentro de um mesmo take**.
3. Dá **zoom em resolução cheia** nos frames individuais de qualquer reveal suspeito.
4. Se precisar de mais densidade num intervalo, re-extrai só aquela janela a 15 fps:
   ```
   ffmpeg -ss 3.0 -t 1.5 -i "VIDEO.mp4" -vf "fps=15" -qscale:v 2 "SAIDA/zoom_%03d.png"
   ```
5. Monta a **decomposição beat a beat** e **confirma o herói do hook** antes de gerar qualquer prompt.

---

## 7. Os arquivos da skill

A skill vive em `.claude/skills/watch/` e tem três arquivos:

- **`SKILL.md`** — as instruções que a IA segue ao rodar `/watch` (inclui a disciplina de análise: ler grades → zoom nos reveals → decompor → confirmar o herói).
- **`scripts/watch_pipeline.py`** — o pipeline Python (código completo abaixo).
- **`scripts/run_watch.ps1`** — o wrapper PowerShell que recarrega o PATH e chama o Python.

### 7.1. `run_watch.ps1` (o wrapper)

```powershell
param(
    [Parameter(Mandatory=$true)][string]$Video,
    [string]$OutDir = "",
    [string]$Extra = ""
)
$ErrorActionPreference = "Stop"

# PATH atualizado (Machine + User) para achar ffmpeg/ffprobe/python
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" +
            [System.Environment]::GetEnvironmentVariable("Path","User")

$py = "C:\Users\luigi\AppData\Local\Programs\Python\Python312\python.exe"
if (-not (Test-Path $py)) {
    $py = (Get-Command python -ErrorAction SilentlyContinue |
           Where-Object { $_.Source -notlike "*WindowsApps*" } |
           Select-Object -First 1).Source
}
if (-not $py) { throw "Python nao encontrado." }

$script = Join-Path $PSScriptRoot "watch_pipeline.py"

$args = @("--video", $Video)
if ($OutDir -ne "") { $args += @("--outdir", $OutDir) }
if ($Extra -ne "")  { $args += $Extra.Split(" ") }

& $py $script @args
exit $LASTEXITCODE
```

### 7.2. `watch_pipeline.py` (o pipeline — código completo)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
watch_pipeline.py — pipeline do /watch
Transforma um .mp4 numa decomposicao completa para analise frame-a-frame + audio.
"""
import argparse, json, os, re, shutil, subprocess, sys
from pathlib import Path

WINGET_LINKS = Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "WinGet" / "Links"

def find_bin(name):
    p = shutil.which(name)
    if p:
        return p
    cand = WINGET_LINKS / f"{name}.exe"
    if cand.exists():
        return str(cand)
    raise SystemExit(f"[ERRO] nao encontrei '{name}'. Instale ou ajuste o PATH.")

FFMPEG = find_bin("ffmpeg")
FFPROBE = find_bin("ffprobe")

def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", **kw)

def probe(video):
    cmd = [FFPROBE, "-v", "error", "-print_format", "json",
           "-show_format", "-show_streams", str(video)]
    r = run(cmd)
    if r.returncode != 0:
        raise SystemExit(f"[ERRO] ffprobe falhou:\n{r.stderr}")
    data = json.loads(r.stdout)
    v = next((s for s in data["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in data["streams"] if s["codec_type"] == "audio"), None)
    if not v:
        raise SystemExit("[ERRO] o arquivo nao tem stream de video.")
    fps = 0.0
    if v.get("avg_frame_rate", "0/0") not in ("0/0", "0"):
        num, den = v["avg_frame_rate"].split("/")
        fps = float(num) / float(den) if float(den) else 0.0
    dur = float(data["format"].get("duration") or v.get("duration") or 0.0)
    return {"duration": round(dur, 3), "fps": round(fps, 3),
            "width": int(v.get("width", 0)), "height": int(v.get("height", 0)),
            "has_audio": a is not None}

def extract_fps(video, outdir, fps, prefix, start=None, dur=None):
    if outdir.exists():
        for old in outdir.glob(f"{prefix}_*.png"):
            old.unlink()
    outdir.mkdir(parents=True, exist_ok=True)
    cmd = [FFMPEG, "-hide_banner", "-y"]
    if start is not None:
        cmd += ["-ss", str(start)]
    if dur is not None:
        cmd += ["-t", str(dur)]
    cmd += ["-i", str(video), "-vf", f"fps={fps}", "-qscale:v", "2",
            str(outdir / f"{prefix}_%04d.png")]
    r = run(cmd)
    if r.returncode != 0:
        print(f"[aviso] extracao {prefix} retornou {r.returncode}:\n{r.stderr[-500:]}")
    base = start or 0.0
    frames = sorted(outdir.glob(f"{prefix}_[0-9]*.png"))
    result = []
    for i, f in enumerate(frames):
        t = round(base + i / fps, 2)
        new = outdir / f"{prefix}_t{t:07.2f}.png"
        if f != new:
            f.rename(new)
        result.append({"file": new.name, "t": t})
    return result

def extract_scenes(video, outdir, threshold):
    if outdir.exists():
        for old in outdir.glob("scene_*.png"):
            old.unlink()
    outdir.mkdir(parents=True, exist_ok=True)
    meta = outdir / "_scene_meta.txt"
    cmd = [FFMPEG, "-hide_banner", "-y", "-i", str(video),
           "-vf", f"select='gt(scene,{threshold})',metadata=print:file=_scene_meta.txt",
           "-fps_mode", "vfr", "-qscale:v", "2", "scene_%04d.png"]
    r = run(cmd, cwd=str(outdir))
    if r.returncode != 0:
        print(f"[aviso] deteccao de cena retornou {r.returncode}:\n{r.stderr[-500:]}")
    times = []
    if meta.exists():
        for line in meta.read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.search(r"pts_time:([0-9.]+)", line)
            if m:
                times.append(float(m.group(1)))
    frames = sorted(outdir.glob("scene_[0-9]*.png"))
    result = []
    for i, f in enumerate(frames):
        t = round(times[i], 2) if i < len(times) else round(i, 2)
        new = outdir / f"scene_t{t:07.2f}.png"
        if f != new:
            f.rename(new)
        result.append({"file": new.name, "t": t})
    if meta.exists():
        meta.unlink()
    return result

def transcribe(video, outdir, model_name):
    outdir.mkdir(parents=True, exist_ok=True)
    wav = outdir / "audio.wav"
    cmd = [FFMPEG, "-hide_banner", "-y", "-i", str(video),
           "-vn", "-ac", "1", "-ar", "16000", str(wav)]
    r = run(cmd)
    if r.returncode != 0 or not wav.exists():
        print(f"[aviso] extracao de audio falhou:\n{r.stderr[-400:]}")
        return None
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("[aviso] faster-whisper nao instalado; pulando transcricao.")
        return None
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    segments, info = model.transcribe(str(wav), language="en", beam_size=5,
                                      vad_filter=True)
    segs, lines = [], []
    for s in segments:
        segs.append({"start": round(s.start, 2), "end": round(s.end, 2),
                     "text": s.text.strip()})
        lines.append(f"[{s.start:6.2f} -> {s.end:6.2f}] {s.text.strip()}")
    (outdir / "transcript.json").write_text(
        json.dumps(segs, ensure_ascii=False, indent=2), encoding="utf-8")
    (outdir / "transcript.txt").write_text("\n".join(lines), encoding="utf-8")
    return {"segments": segs, "text": " ".join(s["text"] for s in segs)}

def make_montages(frames_meta, frames_dir, out_dir, label, cols=4, tile_w=360, per_sheet=12):
    from PIL import Image, ImageDraw, ImageFont
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except Exception:
        font = ImageFont.load_default()
    bar = 26
    sheets = []
    chunks = [frames_meta[i:i + per_sheet] for i in range(0, len(frames_meta), per_sheet)]
    for si, chunk in enumerate(chunks, 1):
        thumbs = []
        for fm in chunk:
            img = Image.open(frames_dir / fm["file"]).convert("RGB")
            w, h = img.size
            tile_h = int(h * tile_w / w)
            img = img.resize((tile_w, tile_h))
            canvas = Image.new("RGB", (tile_w, tile_h + bar), (15, 15, 15))
            canvas.paste(img, (0, bar))
            d = ImageDraw.Draw(canvas)
            d.text((6, 3), f"t={fm['t']:.2f}s", fill=(255, 220, 0), font=font)
            thumbs.append(canvas)
        tw, th = thumbs[0].size
        rows = (len(thumbs) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * tw, rows * th), (0, 0, 0))
        for idx, t in enumerate(thumbs):
            r_, c_ = divmod(idx, cols)
            sheet.paste(t, (c_ * tw, r_ * th))
        name = f"overview_{label}_{si:02d}.png"
        sheet.save(out_dir / name)
        sheets.append(name)
    return sheets

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", required=True)
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--timeline-fps", type=float, default=5.0)
    ap.add_argument("--scene-threshold", type=float, default=0.2)
    ap.add_argument("--model", default="small.en")
    ap.add_argument("--no-audio", action="store_true")
    args = ap.parse_args()

    video = Path(args.video).resolve()
    if not video.exists():
        raise SystemExit(f"[ERRO] video nao encontrado: {video}")
    outdir = Path(args.outdir).resolve() if args.outdir else \
        video.parent / f"{video.stem}_watch"
    outdir.mkdir(parents=True, exist_ok=True)

    print(f"[1/5] sondando {video.name} ...")
    info = probe(video)

    print("[2/5] detectando cortes de cena ...")
    scenes = extract_scenes(video, outdir / "frames" / "scenes", args.scene_threshold)

    print(f"[3/5] extraindo timeline densa COMPLETA (@ {args.timeline_fps}fps) ...")
    timeline = extract_fps(video, outdir / "frames" / "timeline", args.timeline_fps, "tl")

    transcript = None
    if not args.no_audio and info["has_audio"]:
        print(f"[4/5] transcrevendo audio (modelo {args.model}) ...")
        transcript = transcribe(video, outdir / "audio", args.model)
    else:
        print("[4/5] audio pulado.")

    print("[5/5] gerando grades de visao geral ...")
    ov = outdir / "overview"
    m_scenes = make_montages(scenes, outdir / "frames" / "scenes", ov, "scenes") if scenes else []
    m_tl = make_montages(timeline, outdir / "frames" / "timeline", ov, "timeline",
                         cols=5, per_sheet=20) if timeline else []

    manifest = {
        "video": str(video), "outdir": str(outdir), "info": info,
        "params": {"timeline_fps": args.timeline_fps,
                   "scene_threshold": args.scene_threshold, "model": args.model},
        "scenes": scenes, "timeline": timeline,
        "overview": {"scenes": m_scenes, "timeline": m_tl},
        "transcript": bool(transcript),
    }
    (outdir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n=== PRONTO ===")

if __name__ == "__main__":
    main()
```

---

## 8. Limitações honestas da `/watch`

- **Não é "assistir" contínuo com olhos e ouvidos** — é amostragem densa de frames + transcrição de áudio. É o máximo real possível, e mata os erros do método antigo.
- **A transcrição é conferência, não substitui a análise visual do herói.** O texto ajuda a amarrar cada beat, mas quem identifica o herói do hook é o olho sobre os frames.
- **Escala:** um vídeo de ~45s a 0,2s gera ~225 frames = ~12 grades para varrer. É mais pesado que o método antigo, mas é a completude necessária para não perder reveals.
- **Vídeos muito longos** podem gerar muitas grades; nesses casos, foca-se a atenção no hook e nos pontos de reveal identificados pela varredura.

---

## 9. Custo de tempo por vídeo (referência real)

Num vídeo de ~60 segundos, 720p-1440p:
- Extração de frames: segundos.
- Transcrição com `small.en` na CPU: um a poucos minutos.
- Geração das grades: segundos.
- Total: normalmente poucos minutos por vídeo.

Próximo documento: **05 — O Processo de Produção**, que encaixa a `/watch` no fluxo completo das 7 fases.
