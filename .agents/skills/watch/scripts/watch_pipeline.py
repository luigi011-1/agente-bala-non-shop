#!/usr/bin/env python3
"""Canonical /watch: dense visual evidence, Faster-Whisper ASR, optional WhisperX alignment.

Exit 0 means requested extraction succeeded; it never means the video was visually reviewed.
Exit 2 means failed/partial processing. Each run replaces its own generated artifacts so an
old transcript cannot be mistaken for the result of a failed rerun.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
import importlib.metadata
import json
import math
import numbers
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import time
import uuid


class PipelineError(RuntimeError):
    pass


def find_bin(name):
    """Resolve at execution time; importing this module does not require FFmpeg."""
    found = shutil.which(name)
    if found:
        return found
    candidates = []
    if platform.system() == "Windows":
        local = os.environ.get("LOCALAPPDATA")
        if local:
            candidates.append(Path(local) / "Microsoft/WinGet/Links" / (name + ".exe"))
    elif platform.system() == "Darwin":
        candidates = [Path(d) / name for d in ("/opt/homebrew/bin", "/usr/local/bin")]
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    raise PipelineError(f"{name} nao encontrado. Prepare o ambiente da operacao e confira o PATH.")


def run(cmd, timeout=300, **kwargs):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                                errors="replace", timeout=timeout, **kwargs)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise PipelineError(f"{Path(cmd[0]).name}: {exc}") from exc
    if result.returncode:
        raise PipelineError(f"{Path(cmd[0]).name} retornou {result.returncode}: {result.stderr[-1500:]}")
    return result


def json_compatible(value):
    """WhisperX/Pandas produce NumPy scalars; preserve absent/non-finite times as null."""
    if value is None or isinstance(value, (str, bool)):
        return value
    if isinstance(value, numbers.Integral):
        return int(value)
    if isinstance(value, numbers.Real):
        return float(value) if math.isfinite(value) else None
    if isinstance(value, dict):
        return {key: json_compatible(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_compatible(item) for item in value]
    return value


def write_json(path, data):
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(json_compatible(data), ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8")
    temporary.replace(path)


def probe(video, ffprobe=None, timeout=300):
    result = run([ffprobe or find_bin("ffprobe"), "-v", "error", "-print_format", "json",
                  "-show_format", "-show_streams", str(video)], timeout=timeout)
    try:
        data = json.loads(result.stdout)
        stream = next(s for s in data.get("streams", []) if s.get("codec_type") == "video")
        numerator, denominator = stream.get("avg_frame_rate", "0/1").split("/")
        fps = float(numerator) / float(denominator) if float(denominator) else 0
        duration = float(data.get("format", {}).get("duration") or stream.get("duration") or 0)
        if not math.isfinite(duration) or duration <= 0:
            raise ValueError("duracao invalida")
        return {"duration": round(duration, 6), "fps": round(fps, 6),
                "width": int(stream.get("width", 0)), "height": int(stream.get("height", 0)),
                "has_audio": any(s.get("codec_type") == "audio" for s in data.get("streams", []))}
    except (StopIteration, ValueError, KeyError, TypeError) as exc:
        raise PipelineError(f"Arquivo sem video utilizavel: {exc}") from exc


def extract_frames(video, scenes_dir, timeline_dir, threshold, fps, ffmpeg=None, timeout=300):
    """Decode once; include the first frame plus cuts. Timeline labels are the FPS sampling grid."""
    scenes_dir.mkdir(parents=True)
    timeline_dir.mkdir(parents=True)
    metadata = scenes_dir / "_scene_meta.txt"
    timeline_output = os.path.relpath(timeline_dir / "tl_%06d.png", scenes_dir)
    graph = (f"[0:v]split=2[a][b];"
             f"[a]select='eq(n,0)+gt(scene,{threshold})',metadata=print:file=_scene_meta.txt[s];"
             f"[b]fps={fps}[t]")
    run([ffmpeg or find_bin("ffmpeg"), "-hide_banner", "-y", "-i", str(video),
         "-filter_complex", graph, "-map", "[s]", "-fps_mode", "vfr", "scene_%06d.png",
         "-map", "[t]", timeline_output], timeout=timeout, cwd=str(scenes_dir))
    times = [float(match.group(1)) for line in metadata.read_text(encoding="utf-8").splitlines()
             if (match := re.search(r"pts_time:([-+0-9.eE]+)", line))]
    scene_files = sorted(scenes_dir.glob("scene_[0-9]*.png"))
    if len(times) != len(scene_files):
        raise PipelineError("Contagem de cenas diverge dos timestamps do FFmpeg; nenhum tempo sera inventado.")
    scenes = []
    for index, (frame, timestamp) in enumerate(zip(scene_files, times), 1):
        name = f"scene_t{timestamp:010.4f}_{index:06d}.png"
        frame.rename(scenes_dir / name)
        scenes.append({"file": name, "t": round(timestamp, 6)})
    metadata.unlink()
    timeline = []
    for index, frame in enumerate(sorted(timeline_dir.glob("tl_[0-9]*.png"))):
        timestamp = index / fps
        name = f"tl_t{timestamp:010.4f}_{index + 1:06d}.png"
        frame.rename(timeline_dir / name)
        timeline.append({"file": name, "t": round(timestamp, 6)})
    if not scenes or not timeline:
        raise PipelineError("FFmpeg nao produziu a timeline e o frame inicial esperados.")
    return scenes, timeline


def faster_transcription(wav, args):
    from faster_whisper import WhisperModel
    model = WhisperModel(args.model, device=args.device, compute_type=args.compute_type,
                         cpu_threads=args.cpu_threads)
    segments, info = model.transcribe(str(wav), language=None if args.language == "auto" else args.language,
                                      beam_size=5, vad_filter=True,
                                      word_timestamps=args.word_timestamps and args.alignment == "none")
    output = []
    for segment in segments:  # faster-whisper performs inference lazily here.
        record = {"start": round(float(segment.start), 4), "end": round(float(segment.end), 4),
                  "text": segment.text.strip()}
        if args.word_timestamps and args.alignment == "none":
            record["words"] = [{"word": word.word, "start": round(float(word.start), 4),
                                "end": round(float(word.end), 4), "probability": float(word.probability)}
                               for word in (segment.words or [])]
        output.append(record)
    return output, info.language


def align_words(segments, wav, language, device, model_name=None):
    """Use existing ASR text; do not load WhisperX ASR, VAD or diarization."""
    import whisperx
    model, metadata = whisperx.load_align_model(language_code=language, device=device,
                                               model_name=model_name)
    result = whisperx.align(segments, model, metadata, str(wav), device,
                           return_char_alignments=False, interpolate_method="ignore")
    words = result.get("word_segments") or [word for segment in result.get("segments", [])
                                             for word in segment.get("words", [])]
    # Missing timestamps remain missing. Never borrow a neighbor's timing or fill with zero.
    timed = sum(isinstance(word.get("start"), (int, float))
                and isinstance(word.get("end"), (int, float))
                and math.isfinite(word["start"]) and math.isfinite(word["end"])
                and 0 <= word["start"] <= word["end"] for word in words)
    expected = sum(len(segment["text"]) if language in ("ja", "zh") else len(segment["text"].split())
                   for segment in segments)
    status = "SUCCEEDED" if words and timed == len(words) == expected else "PARTIAL" if words else "FAILED"
    return {"status": status, "backend": "whisperx", "language": language,
            "word_count": len(words), "expected_word_count": expected, "timed_word_count": timed,
            "unaligned_word_count": max(expected, len(words)) - timed, "segments": result.get("segments", []),
            "words": words}


def transcribe(video, outdir, args, ffmpeg=None):
    outdir.mkdir(parents=True, exist_ok=True)
    audio = {"status": "FAILED", "backend": "faster-whisper", "language": None,
             "segments": [], "text": ""}
    alignment = {"status": "NOT_REQUESTED", "backend": None}
    wav = outdir / "audio.wav"
    try:
        run([ffmpeg or find_bin("ffmpeg"), "-hide_banner", "-y", "-i", str(video),
             "-vn", "-ac", "1", "-ar", "16000", str(wav)], timeout=args.command_timeout)
        segments, language = faster_transcription(wav, args)
        audio.update(status="SUCCEEDED" if segments else "NO_SPEECH_DETECTED", language=language,
                     segments=segments, text=" ".join(segment["text"] for segment in segments))
        write_json(outdir / "transcript.json", segments)
        (outdir / "transcript.txt").write_text("\n".join(
            f"[{segment['start']:7.3f} -> {segment['end']:7.3f}] {segment['text']}"
            for segment in segments), encoding="utf-8")
        if args.alignment == "whisperx":
            if not segments:
                alignment = {"status": "NOT_APPLICABLE", "backend": "whisperx", "reason": "no_speech_detected"}
            else:
                # Free the ASR model before loading the alignment model (function scope ended).
                try:
                    alignment = align_words(segments, wav, language, args.device, args.align_model)
                    write_json(outdir / "alignment.json", alignment)
                    write_json(outdir / "words.json", alignment["words"])
                except Exception as exc:
                    alignment = {"status": "FAILED", "backend": "whisperx",
                                 "error": f"{type(exc).__name__}: {exc}"}
    except Exception as exc:
        audio["error"] = f"{type(exc).__name__}: {exc}"
        if args.alignment == "whisperx":
            alignment = {"status": "FAILED", "backend": "whisperx", "reason": "transcription_failed"}
    return audio, alignment


def make_sheet(job):
    from PIL import Image, ImageDraw, ImageFont
    chunk, frames_dir, output, cols, tile_width = job
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except OSError:
        font = ImageFont.load_default()
    thumbs = []
    for record in chunk:
        with Image.open(frames_dir / record["file"]) as source:
            height = max(1, round(source.height * tile_width / source.width))
            image = source.convert("RGB").resize((tile_width, height))
        canvas = Image.new("RGB", (tile_width, height + 26), (15, 15, 15))
        canvas.paste(image, (0, 26))
        ImageDraw.Draw(canvas).text((6, 3), f"t={record['t']:.3f}s", fill=(255, 220, 0), font=font)
        thumbs.append(canvas)
    width, height = thumbs[0].size
    sheet = Image.new("RGB", (cols * width, math.ceil(len(thumbs) / cols) * height))
    for index, thumb in enumerate(thumbs):
        sheet.paste(thumb, (index % cols * width, index // cols * height))
    sheet.save(output)
    return output.name


def montage_jobs(frames, frames_dir, output_dir, label, cols, per_sheet):
    output_dir.mkdir(parents=True, exist_ok=True)
    return [(frames[index:index + per_sheet], frames_dir,
             output_dir / f"overview_{label}_{index // per_sheet + 1:02d}.png", cols, 360)
            for index in range(0, len(frames), per_sheet)]


@contextmanager
def output_lock(outdir):
    outdir.mkdir(parents=True, exist_ok=True)
    lock = outdir / ".watch.lock"
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise PipelineError(f"Outro /watch possui {lock}. Confira se o processo terminou antes de remover a trava.") from exc
    try:
        with os.fdopen(fd, "w") as file:
            file.write(f"pid={os.getpid()}\n")
        yield
    finally:
        lock.unlink(missing_ok=True)


def check_output_ownership(outdir):
    reserved = ("frames", "audio", "overview", "manifest.json")
    if not any((outdir / name).exists() for name in reserved):
        return
    try:
        old = json.loads((outdir / "manifest.json").read_text(encoding="utf-8"))
        owned = old.get("pipeline") == "watch" or all(
            key in old for key in ("video", "info", "scenes", "timeline", "overview"))
    except (ValueError, OSError, AttributeError):
        owned = False
    if not owned:
        raise PipelineError("A pasta de saida contem artefatos sem manifest do /watch. Use outra pasta; nenhum arquivo foi substituido.")
    if any((outdir / name).is_symlink() for name in reserved):
        raise PipelineError("A pasta de saida contem symlink em caminho reservado; use outra pasta.")


def publish(staging, outdir):
    # Only these generated directories belong to /watch. Other production artifacts stay intact.
    for name in ("frames", "audio", "overview"):
        current = outdir / name
        if current.exists():
            if current.is_dir():
                shutil.rmtree(current)
            else:
                current.unlink()
        fresh = staging / name
        if fresh.exists():
            fresh.replace(current)


def package_versions():
    versions = {}
    for package in ("faster-whisper", "whisperx", "ctranslate2", "Pillow", "av", "torch", "torchaudio"):
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = None
    return versions


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--video", required=True)
    parser.add_argument("--outdir")
    parser.add_argument("--timeline-fps", type=float, default=5)
    parser.add_argument("--scene-threshold", type=float, default=0.2)
    parser.add_argument("--model", default="small.en")
    parser.add_argument("--language", default="en", help="ISO language code, or auto; .en models support English only")
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--compute-type", default="int8")
    parser.add_argument("--cpu-threads", type=int, default=4)
    parser.add_argument("--jobs", type=int, default=min(4, os.cpu_count() or 1))
    parser.add_argument("--alignment", choices=("none", "whisperx"), default="none")
    parser.add_argument("--align-model", help="Optional explicit WhisperX alignment model")
    parser.add_argument("--word-timestamps", action="store_true", help="Faster-Whisper words when alignment=none")
    parser.add_argument("--no-audio", action="store_true", help="Explicitly skip transcription (e.g. silent paid reference)")
    parser.add_argument("--allow-no-audio", action="store_true", help="Allow a missing audio stream; transcribe if present")
    parser.add_argument("--max-frames", type=int, default=20000, help="Fail instead of truncating above this sampling budget")
    parser.add_argument("--command-timeout", type=float, default=300)
    return parser


def validate_args(parser, args):
    if not math.isfinite(args.timeline_fps) or not 0 < args.timeline_fps <= 60:
        parser.error("--timeline-fps deve estar entre 0 (exclusivo) e 60")
    if not math.isfinite(args.scene_threshold) or not 0 <= args.scene_threshold <= 1:
        parser.error("--scene-threshold deve estar entre 0 e 1")
    if args.jobs < 1 or args.cpu_threads < 1 or args.max_frames < 1:
        parser.error("--jobs, --cpu-threads e --max-frames devem ser positivos")
    if not math.isfinite(args.command_timeout) or args.command_timeout <= 0:
        parser.error("--command-timeout deve ser positivo")
    if args.no_audio and args.alignment != "none":
        parser.error("--no-audio nao combina com alinhamento solicitado")
    if args.align_model and args.alignment != "whisperx":
        parser.error("--align-model exige --alignment whisperx")
    if args.model.endswith(".en") and args.language not in ("en", "auto"):
        parser.error("Modelo .en suporta apenas ingles; use --model small para outro idioma")


def process(args):
    video = Path(args.video).expanduser().resolve()
    if not video.is_file():
        raise PipelineError(f"Video nao encontrado: {video}")
    outdir = Path(args.outdir).expanduser().resolve() if args.outdir else video.parent / (video.stem + "_watch")
    if outdir == video or outdir in video.parents:
        raise PipelineError("Use uma pasta de saida que nao contenha o video de entrada.")
    check_output_ownership(outdir)
    started = time.perf_counter()
    manifest = {"schema_version": 2, "pipeline": "watch", "run_id": str(uuid.uuid4()),
                "status": "RUNNING", "analysis_status": "PENDING_VISUAL_REVIEW", "video": str(video),
                "outdir": str(outdir), "info": None, "scenes": [], "timeline": [],
                "overview": {"scenes": [], "timeline": []}, "transcript": False,
                "audio": {"status": "PENDING"}, "alignment": {"status": "NOT_REQUESTED"},
                "params": {key: value for key, value in vars(args).items() if key not in ("video", "outdir")},
                "environment": {"os": platform.platform(), "architecture": platform.machine(),
                                "python": sys.version.split()[0], "packages": package_versions()}, "errors": []}
    with output_lock(outdir):
        write_json(outdir / "manifest.json", manifest)
        with tempfile.TemporaryDirectory(prefix=".watch-run-", dir=outdir.parent) as temporary:
            staging = Path(temporary)
            audio_future = None
            with ThreadPoolExecutor(max_workers=1) as audio_pool:
                try:
                    ffmpeg, ffprobe = find_bin("ffmpeg"), find_bin("ffprobe")
                    manifest["environment"].update(ffmpeg=ffmpeg, ffprobe=ffprobe)
                    info = probe(video, ffprobe, args.command_timeout)
                    manifest["info"] = info
                    if math.ceil(info["duration"] * args.timeline_fps) > args.max_frames:
                        raise PipelineError("Timeline excede --max-frames. Aumente o limite se necessario; o video nao sera truncado.")
                    if args.no_audio:
                        manifest["audio"] = {"status": "SKIPPED_BY_REQUEST"}
                    elif not info["has_audio"]:
                        manifest["audio"] = {"status": "NO_AUDIO_STREAM", "allowed": args.allow_no_audio}
                        if args.alignment == "whisperx":
                            manifest["alignment"] = {"status": "NOT_APPLICABLE", "backend": "whisperx", "reason": "no_audio_stream"}
                        if not args.allow_no_audio:
                            manifest["errors"].append("Audio ausente sem modo mudo explicito (--no-audio ou --allow-no-audio).")
                    else:
                        audio_future = audio_pool.submit(transcribe, video, staging / "audio", args, ffmpeg)
                    print(f"Extraindo video completo: {info['duration']}s, {args.timeline_fps}fps ...", flush=True)
                    scenes, timeline = extract_frames(video, staging / "frames/scenes", staging / "frames/timeline",
                                                      args.scene_threshold, args.timeline_fps, ffmpeg, args.command_timeout)
                    manifest.update(scenes=scenes, timeline=timeline)
                    if len(timeline) > args.max_frames:
                        raise PipelineError("FFmpeg excedeu o limite de frames; a execucao nao sera marcada completa.")
                    manifest["coverage"] = {"source_duration_s": info["duration"], "sample_interval_s": 1 / args.timeline_fps,
                                            "timeline_count": len(timeline), "timestamp_basis": "fps_filter_sampling_grid",
                                            "visual_review_performed": False}
                    jobs = (montage_jobs(scenes, staging / "frames/scenes", staging / "overview", "scenes", 4, 12)
                            + montage_jobs(timeline, staging / "frames/timeline", staging / "overview", "timeline", 5, 20))
                    with ThreadPoolExecutor(max_workers=args.jobs) as montage_pool:
                        sheets = list(montage_pool.map(make_sheet, jobs))
                    manifest["overview"] = {label: [name for name in sheets if name.startswith("overview_" + label + "_")]
                                            for label in ("scenes", "timeline")}
                    manifest["status"] = "COMPLETE" if not manifest["errors"] else "PARTIAL"
                except Exception as exc:
                    manifest["status"] = "FAILED"
                    manifest["errors"].append(f"{type(exc).__name__}: {exc}")
                if audio_future:
                    try:
                        audio, alignment = audio_future.result()
                        manifest.update(audio=audio, alignment=alignment, transcript=audio["status"] in ("SUCCEEDED", "NO_SPEECH_DETECTED"))
                        if audio["status"] == "FAILED":
                            manifest["errors"].append("Transcricao: " + audio.get("error", "falhou"))
                        if alignment["status"] in ("FAILED", "PARTIAL"):
                            manifest["errors"].append("Alinhamento: " + alignment.get("error", alignment["status"]))
                        if manifest["errors"] and manifest["status"] == "COMPLETE":
                            manifest["status"] = "PARTIAL"
                    except Exception as exc:
                        manifest["audio"] = {"status": "FAILED", "error": str(exc)}
                        manifest["errors"].append(f"Transcricao: {exc}")
                        if manifest["status"] == "COMPLETE":
                            manifest["status"] = "PARTIAL"
            publish(staging, outdir)
            manifest["elapsed_seconds"] = round(time.perf_counter() - started, 3)
            write_json(outdir / "manifest.json", manifest)
    return manifest


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    validate_args(parser, args)
    try:
        manifest = process(args)
    except (PipelineError, OSError, ValueError) as exc:
        print(f"[ERRO] {exc}", file=sys.stderr)
        return 2
    print(f"{manifest['status']}: {manifest['outdir']} ({manifest['elapsed_seconds']}s)")
    print("A extracao aguarda leitura visual das grades e frames pelo analista.")
    for error in manifest["errors"]:
        print(f"[ERRO] {error}", file=sys.stderr)
    return 0 if manifest["status"] == "COMPLETE" else 2


if __name__ == "__main__":
    raise SystemExit(main())
