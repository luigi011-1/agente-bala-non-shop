#!/usr/bin/env python3
"""Edição automática de takes do Flow, num comando só (estilo v3 aprovado pelo Luigi em 2026-10-09).

    python3 editar.py <pasta_dos_takes> [--producao <pasta>] [--musica <nome>] [--ramp 1] [--leaks 2,4] [--up 1]

Faz, em ordem, e para no primeiro problema:
  1. transcreve cada take (faster-whisper, modelo carregado uma vez);
  2. acha sozinho o roteiro da produção comparando a fala com os roteiros do repo e das entregas;
  3. confere se cada take falou a frase do roteiro;
  4. corta pelos silêncios reais e monta a base com os trechos EM PARALELO (minterpolate por trecho);
  5. legenda (tempo do whisper no vídeo cortado, texto do roteiro), light leak, música a -10 dB da voz;
  6. lint e render no HyperFrames, recompressão para caber na pasta do Mac (< 30 MB);
  7. conferências automáticas (silêncio, quadro fantasma, contagem de palavras) + contact sheets,
     e escreve RELATORIO.md com passa/falha.
Regras e porquês: docs/pos-producao-edicao-regras.md. Nada aqui muda o estilo aprovado.
"""
import argparse, concurrent.futures as cf, difflib, glob, hashlib, json, os, re, shutil, subprocess, sys, time

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "../../../.."))
MUSICAS = os.environ.get("EDICAO_MUSICAS", "/mnt/project-files/edicao/musicas")
ENTREGAS = "/mnt/project-files/entregas"

SP, GAP, PAD_IN, PAD_OUT, MIN_ISLAND, JUNTA, W, H, FPS = 1.12, 0.15, 0.05, 0.11, 0.4, 0.05, 1080, 1920, 30
MUSICA_DB = -10  # Luigi, 2026-10-09: música sempre 10 dB abaixo da voz


def sh(cmd, **kw):
    return subprocess.run(cmd, shell=isinstance(cmd, str), check=True, capture_output=True, text=True, **kw).stdout


def sh_err(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stderr


def dur(f):
    return float(sh(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))


def norm(t):
    return re.sub(r"[^a-z0-9' ]", " ", t.lower().replace("’", "'")).split()


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


# ---------- 1. transcrição ----------
_modelo = None
def palavras(f):
    global _modelo
    if _modelo is None:
        from faster_whisper import WhisperModel
        _modelo = WhisperModel("small.en", device="cpu", compute_type="int8")
    segs, _ = _modelo.transcribe(f, language="en", word_timestamps=True)
    return [[w.word.strip(), round(w.start, 3), round(w.end, 3)] for s in segs for w in s.words]


# ---------- 2. achar o roteiro ----------
FALA = re.compile(r'(?:speaks|frase|says|line)[^"\n]{0,140}?:\s*"([^"]{12,})"', re.I)

def falas_por_producao():
    fontes = glob.glob(f"{REPO}/producao/*/**/*.md", recursive=True) + glob.glob(f"{ENTREGAS}/**/*.md", recursive=True)
    prod = {}
    for f in fontes:
        if "/_" in f.replace(REPO, "").replace(ENTREGAS, ""):
            continue
        try:
            txt = open(f, encoding="utf8", errors="ignore").read()
        except OSError:
            continue
        linhas = [m.group(1).strip() for m in FALA.finditer(txt)]
        if linhas:
            prod.setdefault(os.path.dirname(f), {}).setdefault(f, linhas)
    return prod

def parecido(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()

def achar_roteiro(ditos, forcada=None):
    """ditos: {take: texto ouvido}. Devolve (pasta, arquivo, {take: fala}, nota)."""
    melhor = None
    for pasta, arqs in falas_por_producao().items():
        if forcada and os.path.basename(pasta.rstrip("/")) != forcada and pasta != forcada:
            continue
        for arq, linhas in arqs.items():
            esc = {k: max(linhas, key=lambda l: parecido(t, l)) for k, t in ditos.items()}
            nota = sum(parecido(ditos[k], esc[k]) for k in ditos) / len(ditos)
            if not melhor or nota > melhor[3]:
                melhor = (pasta, arq, esc, nota)
    return melhor


# ---------- 4. cortes ----------
def ilhas(f, ws):
    d = dur(f)
    log_ = sh_err(f'ffmpeg -hide_banner -i "{f}" -af silencedetect=noise=-35dB:d={GAP} -f null -')
    sil, st = [], None
    for m in re.finditer(r"silence_(start|end): ([\d.]+)", log_):
        if m.group(1) == "start": st = float(m.group(2))
        else: sil.append([st, float(m.group(2))]); st = None
    if st is not None: sil.append([st, d])
    isl, pos = [], 0.0
    for a, b in sil:
        if a - pos > 0.02: isl.append([pos, a])
        pos = b
    if d - pos > 0.02: isl.append([pos, d])
    isl = [i for i in isl if any(wb > i[0] + 0.03 and wa < i[1] - 0.03 for _, wa, wb in ws)]  # ruído cai
    merged = []
    for i in isl:
        if merged and (i[1] - i[0] < MIN_ISLAND or merged[-1][1] - merged[-1][0] < MIN_ISLAND): merged[-1][1] = i[1]
        else: merged.append(list(i))
    sp = []
    for a, b in merged:
        x = [max(0, a - PAD_IN), min(d, b + PAD_OUT)]
        if sp and x[0] - sp[-1][1] < JUNTA: sp[-1][1] = x[1]
        else: sp.append(x)
    return sp

def segmentos(takes, words, ramp):
    segs = []
    for k, f in takes:
        sp = ilhas(f, words[k])
        for j, (a, b) in enumerate(sp):
            segs.append(dict(k=k, a=a, b=b, sp=SP))
            if k in ramp and j + 1 < len(sp) and sp[j + 1][0] > b:
                segs.append(dict(k=k, a=b, b=sp[j + 1][0], sp=ramp[k], mute=True))
    o = 0.0
    for s in segs:
        s["o"] = o; s["d"] = (s["b"] - s["a"]) / s["sp"]; o += s["d"]
    return segs

def um_trecho(arg):
    i, s, src, tmp = arg
    out = f"{tmp}/seg{i:03d}.mkv"
    v = (f"[0:v]trim=start={s['a']:.3f}:end={s['b']:.3f},setpts=(PTS-STARTPTS)/{s['sp']},"
         f"minterpolate=fps={FPS}:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1:scd=none,"
         f"scale={W}:{H}:flags=lanczos,setsar=1,"
         # o minterpolate engole os últimos quadros do trecho: completa clonando o último (como a v3 aprovada)
         f"tpad=stop_mode=clone:stop_duration=0.3,trim=end_frame={max(1, round(s['d'] * FPS))},setpts=N/({FPS}*TB)[v]")
    if s.get("mute"):
        a = f"aevalsrc=0:d={s['d']:.4f}:s=44100,aformat=sample_rates=44100:channel_layouts=mono[a0]"
    else:
        a = (f"[0:a]atrim=start={s['a']:.3f}:end={s['b']:.3f},asetpts=PTS-STARTPTS,atempo={s['sp']},"
             f"aformat=sample_rates=44100:channel_layouts=mono,afade=t=in:d=0.012,"
             f"afade=t=out:st={max(0, s['d'] - 0.02):.3f}:d=0.02[a0]")
    sh(["ffmpeg", "-y", "-loglevel", "error", "-threads", "1", "-i", src, "-filter_complex", f"{v};{a}",
        "-map", "[v]", "-map", "[a0]", "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p",
        "-g", "15", "-r", str(FPS), "-c:a", "pcm_s16le", out])
    # áudio do trecho com a duração exata do vídeo do trecho (quadros inteiros): sem deriva de lábio ao juntar
    n = int(sh(["ffprobe", "-v", "error", "-count_packets", "-select_streams", "v:0", "-show_entries",
                "stream=nb_read_packets", "-of", "csv=p=0", out]).strip())
    fixo = f"{tmp}/segf{i:03d}.mkv"
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", out, "-c:v", "copy", "-af", f"apad,atrim=end={n / FPS:.6f}",
        "-c:a", "pcm_s16le", fixo])
    return fixo, n

def montar_base(segs, src, tmp):
    trabalhos = [(i, s, src[s["k"]], tmp) for i, s in enumerate(segs)]
    with cf.ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as ex:
        res = list(ex.map(um_trecho, trabalhos))
    with open(f"{tmp}/lista.txt", "w") as fh:
        fh.writelines(f"file '{f}'\n" for f, _ in res)
    sh(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{tmp}/lista.txt", "-c", "copy", f"{tmp}/junto.mkv"])
    # tempos reais de cada trecho (quadros inteiros) para legenda, leak e conferência
    o = 0.0
    for s, (_, n) in zip(segs, res):
        s["o"] = o; s["d"] = n / FPS; o += s["d"]
    return o


# ---------- 5. legenda, leak, música ----------
def legenda_html(segs, heard, roteiro_palavras, total, leaks, up):
    def seg_at(t):
        return next((s for s in segs if s["o"] <= t < s["o"] + s["d"]), segs[-1])
    usa_roteiro = len(heard) == len(roteiro_palavras)
    ws = [dict(w=roteiro_palavras[i] if usa_roteiro else w, t=a, k=seg_at(a + 0.05)["k"]) for i, (w, a, _) in enumerate(heard)]
    pages, cur = [], []
    for i, w in enumerate(ws):
        cur.append(w); nx = ws[i + 1] if i + 1 < len(ws) else None
        if (not nx or len(cur) >= 3 or re.search(r"[.!?]$", w["w"]) or (re.search(r",$", w["w"]) and len(cur) >= 2)
                or nx["k"] != w["k"]):
            pages.append(cur); cur = []
    html, js = [], []
    for n, p in enumerate(pages):
        st = 0 if n == 0 else p[0]["t"]; en = pages[n + 1][0]["t"] if n < len(pages) - 1 else total
        txt = " ".join(re.sub(r"[.,!?]$", "", w["w"]) for w in p).lower()
        cls = " up" if p[0]["k"] in up else ""
        html.append(f'<div class="clip cap{cls}" id="cp{n}" data-start="{st:.3f}" data-duration="{en - st:.3f}" '
                    f'data-track-index="{2 + n % 2}"><div class="capin">{txt}</div></div>')
    for i, s in enumerate(segs):
        if i > 0 and segs[i - 1]["k"] != s["k"] and s["k"] in leaks:
            t = max(0, s["o"] - 0.12)
            html.append(f'<div class="clip leak" id="lk{i}" data-start="{t:.3f}" data-duration="0.5" data-track-index="5"></div>')
            js.append(f'tl.fromTo("#lk{i}", {{ opacity: 0 }}, {{ opacity: 0.85, duration: 0.14, ease: "power2.out" }}, {t:.3f});')
            js.append(f'tl.to("#lk{i}", {{ opacity: 0, duration: 0.34, ease: "power2.in" }}, {t + 0.16:.3f});')
    return html, js, usa_roteiro, len(pages)

PAGINA = open(os.path.join(AQUI, "pagina_v3.html"), encoding="utf8").read()

def escolher_musica(nome, chave):
    faixas = sorted(glob.glob(f"{MUSICAS}/*.mp3"))
    if not faixas: return None
    if nome:
        c = [f for f in faixas if nome.lower() in os.path.basename(f).lower()]
        if not c: sys.exit(f"Música '{nome}' não encontrada em {MUSICAS}")
        return c[0]
    return faixas[int(hashlib.md5(chave.encode()).hexdigest(), 16) % len(faixas)]  # fixa por produção

def mixar(voz, musica, total, saida):
    if not musica:
        shutil.copy(voz, saida); return 0.0
    log_ = sh_err(f'ffmpeg -hide_banner -t 40 -i "{musica}" -af silencedetect=noise=-40dB:d=0.3 -f null -')
    m = re.search(r"silence_start: 0(?:\.0+)?\s.*?silence_end: ([\d.]+)", log_, re.S)
    ini = float(m.group(1)) if m else 0.0  # pula silêncio de abertura da faixa
    # voz já em -14 LUFS; música normalizada em -14 LUFS e baixada 10 dB = 10 dB abaixo da voz, sempre
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", voz, "-ss", f"{ini:.2f}", "-i", musica, "-filter_complex",
        f"[1:a]loudnorm=I=-14:TP=-2:LRA=11,volume={MUSICA_DB}dB,aformat=sample_rates=44100:channel_layouts=mono,"
        f"atrim=0:{total:.3f},afade=t=in:d=0.3,afade=t=out:st={total - 0.8:.2f}:d=0.8[m];"
        f"[0:a][m]amix=inputs=2:normalize=0,atrim=0:{total:.3f},alimiter=limit=0.95[o]",
        "-map", "[o]", "-ar", "44100", "-ac", "1", saida])
    return ini


# ---------- 7. conferências ----------
def quadros(video, tempos, larg=64):
    import numpy as np
    alt = int(larg * H / W)
    expr = "+".join(f"eq(n\\,{n})" for n in tempos)
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", video, "-vf", f"select='{expr}',scale={larg}:{alt},format=gray",
                          "-fps_mode", "passthrough", "-f", "rawvideo", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, alt, larg).astype(np.float32)

def fantasmas(video, cortes_q):
    """Quadro misturado: parecido com os DOIS vizinhos de um corte de cena. Corte limpo tem um lado ~igual."""
    achados = []
    for c in cortes_q:
        ns = list(range(max(0, c - 3), c + 4))
        try:
            f = quadros(video, ns)
        except Exception:
            continue
        for j in range(1, len(f) - 1):
            ac = abs(f[j - 1] - f[j + 1]).mean(); ab = abs(f[j - 1] - f[j]).mean(); bc = abs(f[j] - f[j + 1]).mean()
            if ac > 12 and ab > 0.25 * ac and bc > 0.25 * ac:
                achados.append(round((ns[j]) / FPS, 2))
    return sorted(set(achados))

def silencios(video, d=0.25):
    log_ = sh_err(f'ffmpeg -hide_banner -i "{video}" -af silencedetect=noise=-35dB:d={d} -f null -')
    ini = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log_)]
    fim = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log_)]
    return list(zip(ini, fim))

def sheet(video, tempos, saida, cols=12, larg=120):
    expr = "+".join(f"between(t,{t - 0.1:.2f},{t + 0.1:.2f})" for t in tempos)
    sh(["ffmpeg", "-loglevel", "error", "-y", "-i", video, "-vf", f"select='{expr}',scale={larg}:-1,tile={cols}x{-(-len(tempos) * 7 // cols)}",
        "-frames:v", "1", saida])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pasta"); ap.add_argument("--producao"); ap.add_argument("--musica"); ap.add_argument("--sem-musica", action="store_true")
    ap.add_argument("--ramp", default="1", help="takes-herói (pausa acelerada 5x em vez de cortada)")
    ap.add_argument("--leaks", default=None, help="takes com light leak na entrada (padrão: 2 e o do meio)")
    ap.add_argument("--up", default="1", help="takes com legenda mais alta")
    ap.add_argument("--nome", default=None); ap.add_argument("--trabalho", default=None)
    ap.add_argument("--nota-minima", type=float, default=0.85)
    a = ap.parse_args()
    t0 = time.time(); rel = []
    takes = sorted((int(m.group(1)), os.path.abspath(f)) for f in glob.glob(f"{a.pasta}/*.mp4")
                   if (m := re.match(r"t(\d+)\.mp4$", os.path.basename(f))))
    if not takes: sys.exit("Nenhum tNN.mp4 na pasta")
    nome = a.nome or os.path.basename(os.path.abspath(a.pasta).rstrip("/"))
    tmp = a.trabalho or f"/tmp/edicao/{nome}"
    os.makedirs(f"{tmp}/assets", exist_ok=True); shutil.copytree(os.path.join(AQUI, "fonts"), f"{tmp}/fonts", dirs_exist_ok=True)

    log(f"1/7 transcrevendo {len(takes)} takes")
    words = {k: palavras(f) for k, f in takes}
    ditos = {k: " ".join(w for w, _, _ in words[k]) for k in words}

    log("2/7 achando o roteiro")
    achado = achar_roteiro(ditos, a.producao)
    if not achado: sys.exit("Nenhum roteiro encontrado")
    pasta, arq, falas, nota = achado
    rel.append(f"- Produção: `{os.path.basename(pasta)}` (`{arq.replace(REPO + '/', '').replace('/mnt/project-files/', '')}`), semelhança {nota:.0%}")
    if nota < a.nota_minima: sys.exit(f"Roteiro incerto ({nota:.0%} < {a.nota_minima:.0%}): {arq}. Rode com --producao.")

    log("3/7 conferindo a fala de cada take")
    erros_fala = []
    for k in sorted(falas):
        r = parecido(ditos[k], falas[k])
        if r < 0.9: erros_fala.append(f"T{k}: ouvi \"{ditos[k]}\" | roteiro \"{falas[k]}\" ({r:.0%})")
    rel.append(f"- Fala dos takes contra o roteiro: {'OK' if not erros_fala else 'FALHA'}")
    rel += [f"  - {e}" for e in erros_fala]
    if erros_fala: open(f"{tmp}/RELATORIO.md", "w").write("\n".join(rel)); sys.exit("Take com fala diferente do roteiro; ver RELATORIO.md")

    n = len(takes)
    ramp = {int(x): 5 for x in a.ramp.split(",") if x}
    leaks = [int(x) for x in a.leaks.split(",")] if a.leaks else sorted({2, n // 2 + 2} & set(range(2, n + 1)))
    up = [int(x) for x in a.up.split(",") if x]
    src = dict(takes)

    log("4/7 cortando e montando a base em paralelo")
    segs = segmentos(takes, words, ramp)
    total = montar_base(segs, src, tmp)
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{tmp}/junto.mkv", "-an", "-c:v", "copy", f"{tmp}/assets/base.mp4"])
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{tmp}/junto.mkv", "-vn", "-af", "loudnorm=I=-14:TP=-1.2,aresample=44100",
        "-ar", "44100", "-ac", "1", f"{tmp}/voz.wav"])
    json.dump(segs, open(f"{tmp}/segs.json", "w"), indent=1)

    log("5/7 legenda, leak e música")
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{tmp}/voz.wav", "-ar", "16000", "-ac", "1", f"{tmp}/voz16.wav"])
    heard = palavras(f"{tmp}/voz16.wav")
    rot_pal = " ".join(falas[k] for k in sorted(falas)).split()
    html, js, usa_rot, npag = legenda_html(segs, heard, rot_pal, total, leaks, up)
    musica = None if a.sem_musica else escolher_musica(a.musica, os.path.basename(pasta))
    ini = mixar(f"{tmp}/voz.wav", musica, total, f"{tmp}/assets/mix.wav")
    open(f"{tmp}/index.html", "w", encoding="utf8").write(
        PAGINA.replace("{{TOTAL}}", f"{total:.3f}").replace("{{CLIPS}}", "\n".join(html)).replace("{{JS}}", "\n".join(js)))

    log("6/7 lint e render")
    lint = subprocess.run("npx -y hyperframes@0.8.143 lint .", shell=True, cwd=tmp, capture_output=True, text=True).stdout
    nerr = re.search(r"(\d+) error", lint)
    sh(f"npx -y hyperframes@0.8.143 render . -o renders/final.mp4 --quality high --quiet", cwd=tmp)
    saida = f"{tmp}/{nome}_editado.mp4"
    sh(["ffmpeg", "-loglevel", "error", "-y", "-i", f"{tmp}/renders/final.mp4", "-c:v", "libx264", "-crf", "19", "-preset", "slow",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-c:a", "aac", "-b:a", "192k", saida])

    log("7/7 conferências")
    cortes = [s["o"] for s in segs[1:]]
    fant = fantasmas(f"{tmp}/assets/base.mp4", [round(c * FPS) for c in cortes])
    sil = [x for x in silencios(f"{tmp}/voz.wav") if not any(s.get("mute") and s["o"] - 0.2 <= x[0] <= s["o"] + s["d"] for s in segs)]
    mb = os.path.getsize(saida) / 1e6
    sheet(f"{tmp}/assets/base.mp4", cortes, f"{tmp}/cortes.png")
    sh(["ffmpeg", "-loglevel", "error", "-y", "-i", saida, "-vf", "fps=0.7,scale=216:-1,tile=6x3", "-frames:v", "1", f"{tmp}/legendas.png"])
    ok = {
        "Lint sem erro": bool(nerr) and nerr.group(1) == "0",
        "Sem silêncio fora da rampa": not sil,
        "Sem quadro fantasma nos cortes": not fant,
        "Legenda com o texto do roteiro (contagem bateu)": usa_rot,
        "Arquivo abaixo de 30 MB": mb < 30,
    }
    rel += [f"- {k}: {'OK' if v else 'FALHA'}" for k, v in ok.items()]
    if sil: rel.append(f"  - silêncios: {sil}")
    if fant: rel.append(f"  - quadro fantasma em: {fant}s")
    rel += [f"- Duração {total:.1f}s · {len(heard) / total:.2f} palavras/s · {len(segs)} trechos ({sum(1 for s in segs if s.get('mute'))} rampas) · {npag} legendas",
            f"- Música: {os.path.basename(musica) + f' (a partir de {ini:.1f}s, {MUSICA_DB} dB da voz)' if musica else 'sem música'}",
            f"- Light leak na entrada dos takes {leaks}; rampa nos takes {sorted(ramp)}; legenda alta nos takes {up}",
            f"- Arquivo: `{saida}` ({mb:.1f} MB) · tempo total {time.time() - t0:.0f}s",
            "- Olhar antes de entregar: `cortes.png` (pulo) e `legendas.png` (nada sobre rosto ou herói)"]
    open(f"{tmp}/RELATORIO.md", "w").write(f"# Relatório de edição · {nome}\n\n" + "\n".join(rel) + "\n")
    print("\n".join(rel))
    sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
