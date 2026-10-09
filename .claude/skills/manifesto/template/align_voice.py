# Alinha uma locução gravada fora (ElevenLabs, voz própria) ao script.json e escreve timing.json.
# Entrada: assets/vo_eleven/gabriel.mp3 + words.json (whisper-cli -ml 1 -ojf). Respiro extra só nas trocas de fundo.
import json, re, subprocess, unicodedata, difflib

SRC, WORDS, OUT_WAV = "assets/vo_eleven/gabriel.mp3", "assets/vo_eleven/words.json", "assets/vo_eleven/locucao.wav"
MIN_THEME_GAP, LEAD, TAIL = 0.6, 0.4, 2.4

def norm(w):
    w = unicodedata.normalize("NFD", w.lower())
    return re.sub(r"[^a-z0-9]", "", w)

scenes = json.load(open("script.json"))["scenes"]
spoken = [(s["text"].strip(), s["offsets"]["from"] / 1000, s["offsets"]["to"] / 1000)
          for s in json.load(open(WORDS))["transcription"] if s["text"].strip()]

disp = []  # (scene_idx, word)
for i, s in enumerate(scenes):
    for w in s["text"].replace("*", "").split():
        disp.append((i, w))

a = [norm(w) for _, w in disp]; b = [norm(w) for w, _, _ in spoken]
alias = {"pra": "para", "obraup": "obra", "upia": "upa", "20": "20"}
a2 = [alias.get(x, x) for x in a]
m = difflib.SequenceMatcher(None, a2, b, autojunk=False)
start = [None] * len(disp); end = [None] * len(disp)
for blk in m.get_matching_blocks():
    for k in range(blk.size):
        start[blk.a + k] = spoken[blk.b + k][1]; end[blk.a + k] = spoken[blk.b + k][2]
# palavras sem par: tempo do vizinho seguinte da fala (ex.: "ObraUp" = "obra UP", "UpIA" = "UP-A")
for op, i1, i2, j1, j2 in m.get_opcodes():
    if op in ("replace", "delete"):
        for k in range(i1, i2):
            j = min(j1 + (k - i1), len(spoken) - 1) if j2 > j1 else max(j1 - 1, 0)
            start[k] = spoken[j][1]; end[k] = spoken[min(j2 - 1, len(spoken) - 1)][2] if j2 > j1 else spoken[j][2]
miss = sum(1 for x in start if x is None)
assert miss == 0, f"{miss} palavras sem tempo"

# cenas no tempo da gravação original
sc = []
for i, s in enumerate(scenes):
    idx = [k for k, (si, _) in enumerate(disp) if si == i]
    sc.append({"id": s["id"], "theme": s["theme"], "a": start[idx[0]], "b": end[idx[-1]], "w": [start[k] for k in idx]})

# blocos por tema; a pausa entre blocos vira pelo menos MIN_THEME_GAP
blocks = []
for i, g in enumerate(sc):
    if not blocks or sc[i - 1]["theme"] != g["theme"]: blocks.append([])
    blocks[-1].append(g)
out = {"audio": OUT_WAV, "scenes": {}}
t = LEAD; cuts = []
for bi, bl in enumerate(blocks):
    nxt = blocks[bi + 1][0]["a"] if bi + 1 < len(blocks) else None
    frm = max(0.0, bl[0]["a"] - 0.08)
    to = (bl[-1]["b"] + nxt) / 2 if nxt else bl[-1]["b"] + 0.5
    off = t - frm
    for g in bl:
        out["scenes"][g["id"]] = {"start": round(g["a"] + off, 3), "duration": round(g["b"] - g["a"], 3),
                                  "words": [{"start": round(w - g["a"], 3)} for w in g["w"]]}
    cuts.append((frm, to, t))
    t += (to - frm) + (max(0.0, MIN_THEME_GAP - (nxt - bl[-1]["b"])) if nxt else 0)
total = t + TAIL
filt = ";".join(f"[0:a]atrim={f:.3f}:{e:.3f},asetpts=PTS-STARTPTS,afade=t=out:st={e - f - 0.03:.3f}:d=0.03,adelay={int(at * 1000)}:all=1[a{i}]"
                for i, (f, e, at) in enumerate(cuts))
filt += ";" + "".join(f"[a{i}]" for i in range(len(cuts))) + f"amix=inputs={len(cuts)}:normalize=0,apad=whole_dur={total:.2f},loudnorm=I=-16:TP=-1.5[o]"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", SRC, "-filter_complex", filt, "-map", "[o]", "-ar", "44100", "-ac", "1", OUT_WAV], check=True)
json.dump(out, open("timing.json", "w"), indent=2)
print(f"ok · {len(sc)} cenas · {len(blocks)} blocos · {total:.1f}s")
