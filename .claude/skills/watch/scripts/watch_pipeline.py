#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
watch_pipeline.py — pipeline do /watch

Transforma um .mp4 numa decomposicao completa para analise frame-a-frame + audio:
  1. Sonda o video (ffprobe): duracao, fps, resolucao, se tem audio.
  2. Extrai um frame em cada CORTE DE CENA (mapa de takes).
  3. Extrai a TIMELINE inteira densa (padrao: 5 fps = 1 frame/0,2s no video
     COMPLETO) -> pega reveals dentro de qualquer take (hook, corpo E cta),
     ex.: cristais derretendo e revelando os gomos da barriga.
  4. Extrai o audio e transcreve com faster-whisper (timestamps por segmento).
  5. Gera GRADES (montages) em tamanho legivel para visao geral rapida.
  6. Escreve manifest.json + transcript.txt/json.

Uso:
  python watch_pipeline.py --video "CAMINHO.mp4" [opcoes]

Opcoes principais:
  --outdir DIR          (padrao: <pasta_do_video>/<nome>_watch)
  --timeline-fps 5      (densidade no video inteiro; 0,2s por frame)
  --scene-threshold 0.2
  --model small.en      (modelo faster-whisper; use medium.en p/ +precisao)
  --no-audio            pula a transcricao
"""

import argparse, json, os, platform, re, shutil, subprocess, sys
from pathlib import Path

# ---- localizar binarios (PATH pode estar "stale" em shell novo no Windows) ----
IS_WINDOWS = platform.system() == "Windows"
WINGET_LINKS = Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "WinGet" / "Links"

def find_bin(name):
    p = shutil.which(name)
    if p:
        return p
    if IS_WINDOWS:
        cand = WINGET_LINKS / f"{name}.exe"
        if cand.exists():
            return str(cand)
    raise SystemExit(f"[ERRO] nao encontrei '{name}'. Instale ou ajuste o PATH.")

FFMPEG = find_bin("ffmpeg")
FFPROBE = find_bin("ffprobe")

def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", **kw)

# ---------------------------- sonda ----------------------------
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
    return {
        "duration": round(dur, 3),
        "fps": round(fps, 3),
        "width": int(v.get("width", 0)),
        "height": int(v.get("height", 0)),
        "has_audio": a is not None,
    }

# ---------------------- extracao por fps fixo ----------------------
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
    # renomear com timestamp
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

# ------------------------- deteccao de cena -------------------------
def extract_scenes(video, outdir, threshold):
    if outdir.exists():
        for old in outdir.glob("scene_*.png"):
            old.unlink()
    outdir.mkdir(parents=True, exist_ok=True)
    meta = outdir / "_scene_meta.txt"
    # roda com cwd=outdir e nomes relativos: evita o ':' do caminho Windows
    # ser interpretado como separador dentro do filtergraph do ffmpeg.
    cmd = [FFMPEG, "-hide_banner", "-y", "-i", str(video),
           "-vf", f"select='gt(scene,{threshold})',metadata=print:file=_scene_meta.txt",
           "-fps_mode", "vfr", "-qscale:v", "2", "scene_%04d.png"]
    r = run(cmd, cwd=str(outdir))
    if r.returncode != 0:
        print(f"[aviso] deteccao de cena retornou {r.returncode}:\n{r.stderr[-500:]}")
    # parse dos pts_time
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

# --------------------------- transcricao ---------------------------
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
    segs = []
    lines = []
    for s in segments:
        segs.append({"start": round(s.start, 2), "end": round(s.end, 2),
                     "text": s.text.strip()})
        lines.append(f"[{s.start:6.2f} -> {s.end:6.2f}] {s.text.strip()}")
    (outdir / "transcript.json").write_text(
        json.dumps(segs, ensure_ascii=False, indent=2), encoding="utf-8")
    (outdir / "transcript.txt").write_text("\n".join(lines), encoding="utf-8")
    return {"segments": segs, "text": " ".join(s["text"] for s in segs)}

# ----------------------------- montages -----------------------------
def make_montages(frames_meta, frames_dir, out_dir, label, cols=4, tile_w=360,
                  per_sheet=12):
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

# ------------------------------- main -------------------------------
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
    print(f"      duracao={info['duration']}s fps={info['fps']} "
          f"{info['width']}x{info['height']} audio={info['has_audio']}")

    print("[2/5] detectando cortes de cena ...")
    scenes = extract_scenes(video, outdir / "frames" / "scenes",
                            args.scene_threshold)
    print(f"      {len(scenes)} cenas.")

    print(f"[3/5] extraindo timeline densa COMPLETA "
          f"(@ {args.timeline_fps}fps = 1 frame/{1/args.timeline_fps:.2f}s) ...")
    timeline = extract_fps(video, outdir / "frames" / "timeline",
                           args.timeline_fps, "tl")
    print(f"      {len(timeline)} frames (vídeo inteiro na densidade do hook).")

    transcript = None
    if not args.no_audio and info["has_audio"]:
        print(f"[4/5] transcrevendo audio (modelo {args.model}) ...")
        transcript = transcribe(video, outdir / "audio", args.model)
        if transcript:
            print(f"      {len(transcript['segments'])} segmentos.")
    else:
        print("[4/5] audio pulado.")

    print("[5/5] gerando grades de visao geral ...")
    ov = outdir / "overview"
    m_scenes = make_montages(scenes, outdir / "frames" / "scenes", ov, "scenes") if scenes else []
    m_tl = make_montages(timeline, outdir / "frames" / "timeline", ov, "timeline",
                         cols=5, per_sheet=20) if timeline else []

    manifest = {
        "video": str(video),
        "outdir": str(outdir),
        "environment": {
            "os": platform.platform(),
            "architecture": platform.machine(),
            "python": sys.version.split()[0],
            "ffmpeg": FFMPEG,
            "ffprobe": FFPROBE,
        },
        "info": info,
        "params": {
            "timeline_fps": args.timeline_fps,
            "scene_threshold": args.scene_threshold, "model": args.model,
        },
        "scenes": scenes,
        "timeline": timeline,
        "overview": {"scenes": m_scenes, "timeline": m_tl},
        "transcript": bool(transcript),
    }
    (outdir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n=== PRONTO ===")
    print(f"saida: {outdir}")
    print(f"grades: {ov}")
    print(f"manifest: {outdir / 'manifest.json'}")
    if transcript:
        print(f"transcricao: {outdir / 'audio' / 'transcript.txt'}")

if __name__ == "__main__":
    main()
