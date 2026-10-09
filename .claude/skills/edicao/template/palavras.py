# Tempo por palavra com faster-whisper (já instalado na nuvem pelo SessionStart).
# Uso: python3 palavras.py saida.json take1.mp4 take2.mp4 ...  → {"1": [[palavra, ini, fim], ...], ...}
#      python3 palavras.py saida.json base.wav --flat           → [[palavra, ini, fim], ...]
import sys, json, re
from faster_whisper import WhisperModel
out, files = sys.argv[1], [f for f in sys.argv[2:] if f != "--flat"]
m = WhisperModel("small.en", device="cpu", compute_type="int8")
def words(f):
    segs, _ = m.transcribe(f, language="en", word_timestamps=True)
    return [[w.word.strip(), round(w.start, 3), round(w.end, 3)] for s in segs for w in s.words]
res = words(files[0]) if "--flat" in sys.argv else {str(int(re.search(r"t(\d+)\.mp4$", f).group(1))): words(f) for f in files}
json.dump(res, open(out, "w"))
