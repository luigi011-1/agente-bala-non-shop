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

Desde 2026-10-05 as etapas independentes rodam AO MESMO TEMPO (a saida e a
mesma de antes, arquivo por arquivo): cenas, timeline e transcricao em
paralelo, e as grades em varios processos enquanto o Whisper ainda roda.

Uso:
  python watch_pipeline.py --video "CAMINHO.mp4" [opcoes]

Opcoes principais:
  --outdir DIR          (padrao: <pasta_do_video>/<nome>_watch)
  --timeline-fps 5      (densidade no video inteiro; 0,2s por frame)
  --scene-threshold 0.2
  --model small.en      (modelo faster-whisper; use medium.en p/ +precisao)
  --no-audio            pula a transcricao
  --jobs N              processos para as grades (padrao: todos os nucleos)
"""

import argparse, json, os, platform, re, shutil, subprocess, sys, time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

# ---- localizar binarios (PATH pode estar "stale" em shell novo no Windows/macOS) ----
IS_WINDOWS = platform.system() == "Windows"
IS_MACOS = platform.system() == "Darwin"
WINGET_LINKS = Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "WinGet" / "Links"
# Homebrew: /opt/homebrew em chip Apple, /usr/local em Intel
BREW_BINS = [Path("/opt/homebrew/bin"), Path("/usr/local/bin")]

def find_bin(name):
    p = shutil.which(name)
    if p:
        return p
    if IS_WINDOWS:
        cand = WINGET_LINKS / f"{name}.exe"
        if cand.exists():
            return str(cand)
    if IS_MACOS:
        for d in BREW_BINS:
            cand = d / name
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

# ------------------- cenas + timeline numa passada -------------------
def extract_frames(video, scenes_dir, timeline_dir, threshold, fps):
    """Mesmo resultado de extract_scenes + extract_fps, decodificando o video
    UMA vez so (split no filtergraph). Os PNGs saem byte a byte iguais."""
    for d, pat in ((scenes_dir, "scene_*.png"), (timeline_dir, "tl_*.png")):
        if d.exists():
            for old in d.glob(pat):
                old.unlink()
        d.mkdir(parents=True, exist_ok=True)
    meta = scenes_dir / "_scene_meta.txt"
    # cwd=scenes_dir e nomes relativos dentro do filtro: evita o ':' do
    # caminho Windows virar separador no filtergraph (mesma trava de antes).
    tl_out = os.path.relpath(timeline_dir / "tl_%04d.png", scenes_dir)
    graph = (f"[0:v]split=2[a][b];"
             f"[a]select='gt(scene,{threshold})',metadata=print:file=_scene_meta.txt[s];"
             f"[b]fps={fps}[t]")
    cmd = [FFMPEG, "-hide_banner", "-y", "-i", str(video),
           "-filter_complex", graph,
           "-map", "[s]", "-fps_mode", "vfr", "-qscale:v", "2", "scene_%04d.png",
           "-map", "[t]", "-qscale:v", "2", tl_out]
    r = run(cmd, cwd=str(scenes_dir))
    if r.returncode != 0:
        print(f"[aviso] extracao de frames retornou {r.returncode}:\n{r.stderr[-500:]}")
    times = []
    if meta.exists():
        for line in meta.read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.search(r"pts_time:([0-9.]+)", line)
            if m:
                times.append(float(m.group(1)))
        meta.unlink()
    scenes = []
    for i, f in enumerate(sorted(scenes_dir.glob("scene_[0-9]*.png"))):
        t = round(times[i], 2) if i < len(times) else round(i, 2)
        new = scenes_dir / f"scene_t{t:07.2f}.png"
        if f != new:
            f.rename(new)
        scenes.append({"file": new.name, "t": t})
    timeline = []
    for i, f in enumerate(sorted(timeline_dir.glob("tl_[0-9]*.png"))):
        t = round(i / fps, 2)
        new = timeline_dir / f"tl_t{t:07.2f}.png"
        if f != new:
            f.rename(new)
        timeline.append({"file": new.name, "t": t})
    return scenes, timeline

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
    # Falha do Whisper (modelo que nao baixa, rede bloqueada) nao derruba
    # o resto do /watch: frames, grades e manifest saem do mesmo jeito.
    try:
        model = WhisperModel(model_name, device="cpu", compute_type="int8")
        segments, info = model.transcribe(str(wav), language="en", beam_size=5,
                                          vad_filter=True)
        segs = []
        lines = []
        for s in segments:
            segs.append({"start": round(s.start, 2), "end": round(s.end, 2),
                         "text": s.text.strip()})
            lines.append(f"[{s.start:6.2f} -> {s.end:6.2f}] {s.text.strip()}")
    except Exception as e:
        print(f"[aviso] transcricao falhou ({type(e).__name__}: {e}); "
              f"frames e grades seguem normalmente.")
        return None
    (outdir / "transcript.json").write_text(
        json.dumps(segs, ensure_ascii=False, indent=2), encoding="utf-8")
    (outdir / "transcript.txt").write_text("\n".join(lines), encoding="utf-8")
    return {"segments": segs, "text": " ".join(s["text"] for s in segs)}

# ----------------------------- montages -----------------------------
def _load_font():
    from PIL import ImageFont
    try:
        return ImageFont.truetype("arial.ttf", 20)
    except Exception:
        return ImageFont.load_default()

def _make_sheet(job):
    """Monta UMA grade. Roda num processo separado, entao recebe tudo pronto."""
    from PIL import Image, ImageDraw
    chunk, frames_dir, out_path, cols, tile_w = job
    font = _load_font()
    bar = 26
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
    sheet.save(out_path)
    return out_path.name

def montage_jobs(frames_meta, frames_dir, out_dir, label, cols=4, tile_w=360,
                 per_sheet=12):
    out_dir.mkdir(parents=True, exist_ok=True)
    chunks = [frames_meta[i:i + per_sheet] for i in range(0, len(frames_meta), per_sheet)]
    return [(chunk, frames_dir, out_dir / f"overview_{label}_{si:02d}.png", cols, tile_w)
            for si, chunk in enumerate(chunks, 1)]

def make_montages(frames_meta, frames_dir, out_dir, label, cols=4, tile_w=360,
                  per_sheet=12, pool=None):
    jobs = montage_jobs(frames_meta, frames_dir, out_dir, label, cols, tile_w, per_sheet)
    if pool is None:
        return [_make_sheet(j) for j in jobs]
    return list(pool.map(_make_sheet, jobs))

# ------------------------------- main -------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", required=True)
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--timeline-fps", type=float, default=5.0)
    ap.add_argument("--scene-threshold", type=float, default=0.2)
    ap.add_argument("--model", default="small.en")
    ap.add_argument("--no-audio", action="store_true")
    ap.add_argument("--jobs", type=int, default=0,
                    help="processos para as grades (padrao: todos os nucleos)")
    args = ap.parse_args()

    video = Path(args.video).resolve()
    if not video.exists():
        raise SystemExit(f"[ERRO] video nao encontrado: {video}")
    outdir = Path(args.outdir).resolve() if args.outdir else \
        video.parent / f"{video.stem}_watch"
    outdir.mkdir(parents=True, exist_ok=True)

    t0 = time.perf_counter()
    print(f"[1/5] sondando {video.name} ...")
    info = probe(video)
    print(f"      duracao={info['duration']}s fps={info['fps']} "
          f"{info['width']}x{info['height']} audio={info['has_audio']}")

    # A transcricao vai para um processo proprio e roda enquanto o ffmpeg
    # tira cenas e timeline numa passada so, e enquanto as grades sao montadas.
    jobs = args.jobs or os.cpu_count() or 2
    do_audio = not args.no_audio and info["has_audio"]
    audio_pool = ProcessPoolExecutor(max_workers=1) if do_audio else None
    if do_audio:
        print(f"[4/5] transcrevendo audio (modelo {args.model}) em paralelo ...")
        fut_tr = audio_pool.submit(transcribe, video, outdir / "audio", args.model)
    else:
        print("[4/5] audio pulado.")
    print("[2/5] detectando cortes de cena ...")
    print(f"[3/5] extraindo timeline densa COMPLETA "
          f"(@ {args.timeline_fps}fps = 1 frame/{1/args.timeline_fps:.2f}s) ...")
    scenes, timeline = extract_frames(video, outdir / "frames" / "scenes",
                                      outdir / "frames" / "timeline",
                                      args.scene_threshold, args.timeline_fps)
    print(f"      {len(scenes)} cenas.")
    print(f"      {len(timeline)} frames (vídeo inteiro na densidade do hook).")
    t_frames = time.perf_counter() - t0

    print("[5/5] gerando grades de visao geral ...")
    ov = outdir / "overview"
    with ProcessPoolExecutor(max_workers=jobs) as mpool:
        m_scenes = make_montages(scenes, outdir / "frames" / "scenes", ov, "scenes",
                                 pool=mpool) if scenes else []
        m_tl = make_montages(timeline, outdir / "frames" / "timeline", ov, "timeline",
                             cols=5, per_sheet=20, pool=mpool) if timeline else []
    t_grades = time.perf_counter() - t0

    transcript = None
    if do_audio:
        transcript = fut_tr.result()
        audio_pool.shutdown()
        if transcript:
            print(f"      {len(transcript['segments'])} segmentos.")
    t_total = time.perf_counter() - t0
    print(f"      tempos: frames {t_frames:.1f}s · grades {t_grades:.1f}s · "
          f"total {t_total:.1f}s")

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
