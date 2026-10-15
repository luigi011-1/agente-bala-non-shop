#!/usr/bin/env python3
"""Mede uma referência editada sem confundir áudio misturado com stems de música.

python scripts/analisar_edicao_referencia.py VIDEO WATCH_DIR --output METRICAS.json
Usar após /watch; não certifica leitura visual, silêncio de voz ou emoção musical.
"""
import argparse
import hashlib
import json
import math
import re
import subprocess
from pathlib import Path

import numpy as np


def medir(video, watch_dir):
    video, watch_dir = Path(video), Path(watch_dir)
    manifest = json.loads((watch_dir / 'manifest.json').read_text())
    if manifest['status'] != 'COMPLETE' or not manifest.get('transcript'):
        raise ValueError('Exige /watch COMPLETE com transcrição')
    source_hash = hashlib.sha256(video.read_bytes()).hexdigest()
    probe = json.loads(subprocess.check_output([
        'ffprobe', '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(video)]))
    duration = float(probe['format']['duration'])
    transcript = json.loads((watch_dir / 'audio/transcript.json').read_text())
    words = [w for s in transcript for w in s.get('words', [])]
    tokens = re.findall(r"\b[\w]+(?:['’][\w]+)*\b", ' '.join(s['text'] for s in transcript))
    gaps = []
    prev = 0.0
    for w in sorted(words, key=lambda x: x['start']):
        if w['start'] - prev >= 0.15:
            gaps.append({'start': round(prev, 3), 'end': round(w['start'], 3)})
        prev = max(prev, w['end'])
    if duration - prev >= 0.15:
        gaps.append({'start': round(prev, 3), 'end': round(duration, 3)})
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', str(video), '-vn',
        '-ar', '16000', '-ac', '1', '-f', 'f32le', '-'])
    pcm = np.frombuffer(raw, dtype='<f4')
    windows = []
    for i in range(0, len(pcm), 16000):
        samples = pcm[i:i + 16000]
        rms = float(np.sqrt(np.mean(samples.astype(float) ** 2)))
        windows.append({'start': round(i / 16000, 3), 'rms_dbfs': round(20 * math.log10(max(rms, 1e-6)), 2)})
    loudness = subprocess.run(['ffmpeg', '-hide_banner', '-i', str(video), '-vn',
        '-af', 'loudnorm=I=-14:TP=-1.2:LRA=11:print_format=json', '-f', 'null', '-'],
        capture_output=True, text=True, check=True).stderr
    blocks = re.findall(r'\{\s*"input_i".*?\}', loudness, re.S)
    measured = json.loads(blocks[-1]) if blocks else None
    visual = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    return {'source': str(video), 'source_sha256': source_hash, 'duration_seconds': duration,
        'width': visual['width'], 'height': visual['height'], 'fps': visual['avg_frame_rate'],
        'word_count_asr_regex': len(tokens), 'asr_word_units': len(words),
        'words_per_second_full_clip': round(len(tokens) / duration, 3),
        'first_asr_word_seconds': words[0]['start'] if words else None,
        'last_asr_word_seconds': words[-1]['end'] if words else None,
        'scene_detector_candidates': [s['t'] for s in manifest['scenes']],
        'asr_gaps_not_proven_silence': gaps, 'mixed_audio_rms_1s': windows,
        'mixed_audio_loudnorm_measurement': measured,
        'limitations': ['ASR tem erros e pode esticar tempos de palavras.',
            'Detector de cenas pode perder jump cuts e disparar com legendas.',
            'RMS e LUFS são do mix; não medem relação música/voz nem gênero, emoção ou BPM.',
            'Sem escuta perceptiva e sem stems separados; emoção da trilha não certificada.']}


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('video'); ap.add_argument('watch_dir'); ap.add_argument('--output', required=True)
    args = ap.parse_args()
    Path(args.output).write_text(json.dumps(medir(args.video, args.watch_dir), indent=2, ensure_ascii=False) + '\n')
