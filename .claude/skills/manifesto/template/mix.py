# mistura a locução de timing.json com o whoosh nas trocas de fundo e reconstrói o index.html
import json, re, subprocess
subprocess.run(["node", "build.mjs"], check=True)
h = open("index.html").read()
W = [float(x) for x in re.findall(r'clipPath: "circle\(120% at 50% 38%\)", duration: 0\.65, ease: "power3\.inOut" \}, ([\d.]+)\)', h)]
d = json.load(open("timing.json")); src = d.get("voice_only", d["audio"])
args = ["ffmpeg", "-y", "-loglevel", "error", "-i", src]; filt = ""
for i, t in enumerate(W, 1):
    args += ["-i", "assets/whoosh.wav"]; filt += f"[{i}:a]adelay={int((t - 0.1) * 1000)}:all=1[w{i}];"
filt += "[0:a]" + "".join(f"[w{i}]" for i in range(1, len(W) + 1)) + f"amix=inputs={len(W) + 1}:normalize=0[o]"
outp = src.replace(".wav", "_sfx.wav")
subprocess.run(args + ["-filter_complex", filt, "-map", "[o]", "-ar", "44100", "-ac", "1", outp], check=True)
d["voice_only"] = src; d["audio"] = outp; json.dump(d, open("timing.json", "w"), indent=2)
subprocess.run(["node", "build.mjs"], check=True)
print("mix ok", outp, len(W), "whooshes")
