// Gera a locução cena a cena (HeyGen), junta numa faixa e escreve timing.json.
// node voice.mjs <voice_id>
import fs from "node:fs";
import { execFileSync } from "node:child_process";

const VOICE = process.argv[2];
if (!VOICE) { console.error("uso: node voice.mjs <voice_id>"); process.exit(1); }
const ROOT = process.env.HF_SKILLS ?? (process.env.HOME + "/.claude/plugins/cache/hyperframes/hyperframes/0.8.140/skills"); // ajuste a versão do plugin
const LAUNCH = ROOT + "/hyperframes/scripts/plugin-cli.mjs";
const TTS = ROOT + "/media-use/audio/scripts/heygen-tts.mjs";
const TEMPO = +(process.env.TEMPO ?? 1), GAP = +(process.env.GAP ?? 0.32), GAP_THEME = 0.8, LEAD = 0.5, TAIL = 2.4;

const { scenes } = JSON.parse(fs.readFileSync("script.json", "utf8"));
fs.mkdirSync("assets/vo", { recursive: true });

const out = { audio: `assets/vo/locucao_${TEMPO}.wav`, scenes: {} };
let t = LEAD; const parts = [];
for (const [i, s] of scenes.entries()) {
  const say = (s.say ?? s.text).replaceAll("*", "");
  const wav = `assets/vo/${s.id}.wav`, words = `assets/vo/${s.id}.words.json`;
  if (!fs.existsSync(wav)) {
    execFileSync("node", [LAUNCH, "--script", TTS, say, "-o", wav, "--words", words, "--voice", VOICE, "--lang", "pt"], { stdio: "inherit" });
  }
  const dur = +execFileSync("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", wav]).toString();
  let ws = []; try { ws = JSON.parse(fs.readFileSync(words, "utf8")); } catch {}
  // descarta silêncio inicial/final da própria fala
  const first = ws.length ? ws[0].start : 0, last = ws.length ? ws.at(-1).end : dur;
  // palavras exibidas: só usa os tempos se a contagem bater (a cena com "say" diferente cai no rateio)
  const shown = s.text.split(/\s+/).length;
  out.scenes[s.id] = { start: +(t).toFixed(3), duration: +((last - first) / TEMPO).toFixed(3),
    words: ws.length === shown ? ws.map(w => ({ start: +((w.start - first) / TEMPO).toFixed(3) })) : null };
  parts.push({ wav, ss: first, to: last, at: t });
  t += (last - first) / TEMPO + ((scenes[i + 1] && scenes[i + 1].theme !== s.theme) ? GAP_THEME : GAP);
}
// monta a faixa: cada fala posicionada no seu tempo
const total = t + TAIL;
const inputs = parts.flatMap(p => ["-i", p.wav]);
const filt = parts.map((p, i) => `[${i}:a]atrim=${p.ss}:${p.to},asetpts=PTS-STARTPTS,atempo=${TEMPO},adelay=${Math.round(p.at * 1000)}:all=1[a${i}]`).join(";")
  + ";" + parts.map((_, i) => `[a${i}]`).join("") + `amix=inputs=${parts.length}:normalize=0,apad=whole_dur=${total.toFixed(2)},loudnorm=I=-16:TP=-1.5[out]`;
execFileSync("ffmpeg", ["-y", "-loglevel", "error", ...inputs, "-filter_complex", filt, "-map", "[out]", "-ar", "44100", "-ac", "1", out.audio]);
fs.writeFileSync("timing.json", JSON.stringify(out, null, 2));
console.log(`ok · ${parts.length} falas · ${total.toFixed(1)}s → ${out.audio}`);
