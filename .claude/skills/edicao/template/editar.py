#!/usr/bin/env python3
"""Edição automática de takes do Flow, num comando só (estilo v3 aprovado pelo Luigi em 2026-10-09).

    python3 editar.py <pasta_dos_takes> [--producao <nome ou pasta>] [--musica <nome>] [--insert 2.5] [--estilo auraly] [--ritmo 3.8] [--ramp 1] [--leaks 2,4] [--up 1]

Faz, em ordem, e para no primeiro problema:
  1. transcreve cada take (faster-whisper, modelo carregado uma vez);
  2. acha sozinho o roteiro da produção comparando a fala com os roteiros do repo e das entregas;
  3. confere cada take PALAVRA POR PALAVRA; o que o Flow inventou ou repetiu é cortado em qualquer ponto;\n     palavra que faltou ou foi trocada para a edição (o take volta para o Flow);
  4. ordena pelo número do take (T__) do pacote; insert mudo entra só com a janela da ação;
     corta pelos silêncios reais e monta a base com os trechos EM PARALELO (minterpolate por trecho);
  5. legenda (tempo do whisper no vídeo cortado, texto do roteiro), light leak, música a -25 dB da voz;
  6. lint e render no HyperFrames, recompressão para caber na pasta do Mac (< 30 MB);
  7. conferências automáticas (silêncio, quadro fantasma, contagem de palavras) + contact sheets,
     e escreve RELATORIO.md com passa/falha.
Regras e porquês: docs/pos-producao-edicao-regras.md. Nada aqui muda o estilo aprovado.
"""
import argparse, concurrent.futures as cf, difflib, glob, hashlib, json, os, re, shutil, subprocess, sys, time

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "../../../.."))
# nuvem: /mnt/project-files; Mac: edicao/musicas do repo (teste no Mac, 2026-10-09: ficava sem achar a faixa)
MUSICAS = os.environ.get("EDICAO_MUSICAS") or next(
    (p for p in ("/mnt/project-files/edicao/musicas", os.path.join(REPO, "edicao/musicas")) if glob.glob(f"{p}/*.mp3")),
    os.path.join(REPO, "edicao/musicas"))
ENTREGAS = "/mnt/project-files/entregas"

SP, GAP, PAD_IN, PAD_OUT, MIN_ISLAND, JUNTA, W, H, FPS = 1.12, 0.15, 0.05, 0.11, 0.4, 0.05, 1080, 1920, 30
INSERT = 2.5  # segundos do insert mudo (antes da aceleração); --insert 0 = inteiro
MUSICA_DB = -25  # Luigi, 2026-10-09: música sempre 25 dB abaixo da voz (-10 atrapalhou a fala)


def sh(cmd, **kw):
    return subprocess.run(cmd, shell=isinstance(cmd, str), check=True, capture_output=True, text=True, **kw).stdout


def sh_err(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stderr


_rms = {}
def rms_janelas(f):
    """Volume médio (dB) de cada janela de 50 ms do áudio do take."""
    if f not in _rms:
        e = sh_err(f'ffmpeg -hide_banner -i "{f}" -vn -af "aresample=16000,asetnsamples=800,astats=metadata=1:reset=1,'
                   f'ametadata=print:key=lavfi.astats.Overall.RMS_level" -f null -')
        _rms[f] = [float(x) if x != "-inf" else -120.0 for x in re.findall(r"RMS_level=(-?[\d.]+|-inf)", e)]
    return _rms[f]

_limiar = {}
def limiar(f):
    """Volume abaixo do qual o take está "em silêncio", medido no próprio take (Luigi, 2026-10-10: o Flow às vezes
    gera intervalo longo entre duas falas do mesmo take, e todo silêncio no meio do take sai). Com -35 dB fixo, a
    pausa com som de ambiente ou chiado do Flow não era cortada. Agora: fundo do take (5% mais baixo) + 6 dB,
    nunca acima da fala - 12 dB, nunca abaixo de -35 dB."""
    if f not in _limiar:
        v = sorted(rms_janelas(f))
        if len(v) < 20: _limiar[f] = -35.0
        else:
            fundo, fala = v[len(v) // 20], v[len(v) * 7 // 10]
            # piso -35: mais baixo, o ruído de sala das pausas virava "som" e as pausas ficavam (2026-10-10).
            # Palavra dita baixinho é protegida em `ilhas`, pelo tempo da palavra, não pelo limiar.
            _limiar[f] = round(max(-35.0, min(fundo + 6, fala - 12)), 1)
    return _limiar[f]

def silencio_rms(f, minimo):
    """Trechos [início, fim] com volume médio abaixo do limiar do take por pelo menos `minimo` s. Mede pela média
    de cada janela, como o limiar: o silencedetect olha o pico, e com chiado nenhum trecho virava silêncio."""
    thr, v, out, st = limiar(f), rms_janelas(f), [], None
    for i, x in enumerate(v + [0.0]):
        if x < thr and i < len(v):
            if st is None: st = i
        elif st is not None:
            if (i - st) * 0.05 >= minimo: out.append([st * 0.05, min(i * 0.05, dur(f))])
            st = None
    return out

def dur(f):
    return float(sh(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))


NUMEROS = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()

def norm(t):
    # o whisper escreve "2 cups" onde o roteiro diz "two cups": número vira palavra antes de comparar
    ws = re.sub(r"[^a-z0-9' ]", " ", t.lower().replace("’", "'")).split()
    return [NUMEROS[int(w)] if w.isdigit() and int(w) <= 20 else w for w in ws]


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


# ---------- 1. transcrição ----------
_modelo = None
def palavras(f):
    global _modelo
    if not sh(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", f]).strip():
        return []  # sem trilha de áudio: take mudo
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

def numeros_take(arq):
    """{fala: número do take} pelos blocos V__ do pacote. Sem isso o take falado é numerado entre as FALAS
    e o mudo pelo TAKE, e o insert cai no lugar errado (teste v04 no Mac, 2026-10-09: limão depois do Boil)."""
    txt = open(arq, encoding="utf8", errors="ignore").read()
    tn = {}
    for m in re.finditer(r"^V(\d+)[ \t]*\n(.*?)^```", txt, re.M | re.S):
        f = FALA.search(m.group(2))
        if f: tn.setdefault(f.group(1).strip(), int(m.group(1)))
    return tn

def falas_tabela(arq):
    """{número do take: texto} da tabela do roteiro (| T7 | and a pinch of black pepper, | ... |)."""
    txt = open(arq, encoding="utf8", errors="ignore").read()
    return {int(m.group(1)): m.group(2).strip() for m in re.finditer(r"^\|\s*T(\d+)\s*\|\s*([^|]*?)\s*\|", txt, re.M)}

def parecido(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()

def achar_roteiro(ditos, forcada=None):
    """ditos: {take: texto ouvido} (só takes com fala). Devolve (pasta, arquivo, {take: fala}, nota, linhas)."""
    melhor = None
    forcada = os.path.basename(os.path.normpath(forcada)) if forcada else None  # nome ou caminho
    for pasta, arqs in falas_por_producao().items():
        if forcada and os.path.basename(pasta.rstrip("/")) != forcada and pasta != forcada:
            continue
        for arq, linhas in arqs.items():
            esc = {k: max(linhas, key=lambda l: parecido(t, l)) for k, t in ditos.items()}
            nota = sum(parecido(ditos[k], esc[k]) for k in ditos) / len(ditos)
            if not melhor or nota > melhor[3]:
                melhor = (pasta, arq, esc, nota, list(dict.fromkeys(linhas)))
    return melhor


CONTRACOES = {"it's": "it is", "don't": "do not", "doesn't": "does not", "isn't": "is not", "you're": "you are",
              "i'm": "i am", "that's": "that is", "can't": "cannot", "won't": "will not", "we're": "we are",
              "they're": "they are", "i'll": "i will", "you'll": "you will", "here's": "here is", "what's": "what is"}

# palavra curta trocada por outra curta é escuta do whisper ("drop the spoonful" por "drop a spoonful")
PEQUENAS = {"a", "an", "the", "and", "in", "on", "of", "to", "at", "for", "is", "it", "this", "that", "your", "you",
            "oh", "no", "so", "now"}

def escuta_ok(h, r):
    """Tokens ouvidos `h` contra os do roteiro `r` (mesmo tamanho): iguais ou erro de escuta do whisper."""
    return len(h) == len(r) and all(a == b or (a in PEQUENAS and b in PEQUENAS)
                                    or difflib.SequenceMatcher(None, a, b).ratio() >= 0.6 for a, b in zip(h, r))

def conferir_fala(ws, fala, sobra=None):
    """Confere o take PALAVRA POR PALAVRA contra a fala do roteiro (Luigi, 2026-10-09: o Flow inventa, remove e
    repete falas no mesmo take; nota de semelhança deixava passar). Devolve (problemas, escutas).
    problemas = faltou / inventou / repetiu / trocou. escutas = palavra quase igual (erro do whisper,
    "kimchee" por "kimchi", "it's" por "it is"): só avisam, porque a legenda usa o texto do roteiro.
    `sobra` (set), se passado, recebe o índice em `ws` de cada palavra inventada ou repetida."""
    hw, dono = [], []
    for n, (w, _, _) in enumerate(ws):
        for t in norm(w): hw.append(t); dono.append(n)
    rt = norm(fala)
    probs, escutas = [], []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, hw, rt, autojunk=False).get_opcodes():
        h, r = " ".join(hw[i1:i2]), " ".join(rt[j1:j2])
        if op == "equal": continue
        if op == "replace" and (i2 - i1) > (j2 - j1):
            # sobra colada numa escuta ("meant for you oh" no lugar de "no"): a ponta que casa com o roteiro é
            # escuta, o resto é sobra que se corta (teste 2026-10-10: sem isso virava "trocou" e travava)
            n = j2 - j1
            for ini, fim in ((i2 - n, i2), (i1, i1 + n)):
                if escuta_ok(hw[ini:fim], rt[j1:j2]):
                    extra = list(range(i1, ini)) + list(range(fim, i2))
                    e = [hw[x] for x in extra]
                    rep = e == hw[i2:i2 + len(e)] or e == hw[max(0, i1 - len(e)):i1]
                    probs.append(f'{"repetiu" if rep else "inventou"} "{" ".join(e)}"')
                    if sobra is not None: sobra.update(dono[x] for x in extra)
                    if hw[ini:fim] != rt[j1:j2]: escutas.append(f'"{" ".join(hw[ini:fim])}" no lugar de "{r}"')
                    break
            else:
                probs.append(f'trocou "{r}" por "{h}"')
            continue
        if op == "replace":
            exp = lambda x: " ".join(CONTRACOES.get(t, t) for t in x.split())
            if exp(h) == exp(r) or (h in PEQUENAS and r in PEQUENAS) or (i2 - i1 == j2 - j1 and all(
                    difflib.SequenceMatcher(None, a, b).ratio() >= 0.6 for a, b in zip(hw[i1:i2], rt[j1:j2]))) \
                    or difflib.SequenceMatcher(None, h.replace(" ", ""), r.replace(" ", "")).ratio() >= 0.85:
                escutas.append(f'"{h}" no lugar de "{r}"')
            else:
                probs.append(f'trocou "{r}" por "{h}"')
        elif op == "delete":
            e = hw[i1:i2]; n = len(e)
            rep = e == hw[i2:i2 + n] or e == hw[max(0, i1 - n):i1]
            probs.append(f'{"repetiu" if rep else "inventou"} "{h}"')
            if sobra is not None: sobra.update(dono[i1:i2])
        else:
            probs.append(f'faltou "{r}"')
    return probs, escutas

def ouvir_trecho(f, a, b, tmp):
    """Transcreve um trecho sozinho e devolve as palavras com tempo absoluto: isolado, o whisper escreve o que
    foi dito (no take inteiro ele suprime a fala repetida)."""
    t = f"{tmp}/trecho_{hashlib.md5(f'{f}{a}{b}'.encode()).hexdigest()[:8]}.wav"
    sh(["ffmpeg", "-loglevel", "error", "-y", "-i", f, "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-vn", "-ar", "16000", "-ac", "1", t])
    return [[w, x + a, y + a] for w, x, y in palavras(t)]

def fala_sem_texto(f, ws, tmp, minimo=0.35):
    """Fala que está no áudio e não está na transcrição. O whisper SUPRIME fala repetida (teste 2026-10-09:
    "...from the store, bought black pepper from the store, drop..." saiu sem a repetição em todas as
    configurações) e esconde ela de dois jeitos: um trecho com som e sem palavra, ou uma palavra ESTICADA por
    cima dela ("store" durando 2,1s). Cada suspeito é transcrito sozinho; só vira corte se tiver palavra.
    Devolve [[início, fim, texto]]."""
    d = dur(f)
    sil = silencio_rms(f, GAP)
    som, pos = [], 0.0
    for a, b in sil:
        if a > pos: som.append([pos, a])
        pos = b
    if d > pos: som.append([pos, d])
    teto = lambda w: 0.45 + 0.09 * len(re.sub(r"[^a-z0-9]", "", w.lower()))  # duração plausível da palavra
    # som sem palavra usa o tempo REAL de cada palavra: com o teto aqui, o fim de um "Why?" falado devagar virava
    # "fala escondida" e o corte comia a palavra (V01 temperos, 2026-10-10). Palavra longa demais é o caso 2.
    cobre = sorted([max(0, a - 0.08), b + 0.08] for w, a, b in ws)
    achados = []
    for a, b in som:  # 1) som sem palavra
        x = a
        for c0, c1 in cobre:
            if c1 <= x or c0 >= b: continue
            if c0 > x and c0 - x >= minimo: achados.append([x, c0])
            x = max(x, c1)
        if b - x >= minimo: achados.append([x, b])
    for w, a, b in ws:  # 2) palavra esticada por cima de outra fala
        if b - a > teto(w) + minimo:
            achados.append([a, b, w])
    cortes = []
    for ach in achados:
        a, b = ach[0], ach[1]
        ouvido = ouvir_trecho(f, max(0, a - 0.02), min(d, b + 0.02), tmp)
        if len(ach) == 3:  # esticada: a primeira palavra ouvida é a própria; o resto é sobra
            resto = [o for o in ouvido if norm(o[0]) != norm(ach[2])][1:] if ouvido and norm(ouvido[0][0]) != norm(ach[2]) else ouvido[1:]
            if resto: cortes.append([max(a, resto[0][1] - 0.05), b, " ".join(o[0] for o in resto)])
        elif ouvido:
            cortes.append([a, b, " ".join(o[0] for o in ouvido)])
    junto = []  # o mesmo trecho achado pelos dois jeitos vira um corte só, com o texto mais longo
    for a, b, t in sorted((float(a), float(b), t) for a, b, t in cortes):
        if junto and a <= junto[-1][1]:
            junto[-1][1] = max(junto[-1][1], b)
            if len(t) > len(junto[-1][2]): junto[-1][2] = t
        else: junto.append([a, b, t])
    return junto

def limpar(f, ws, fala, tmp, k):
    """Corta do take o que o Flow inventou ou repetiu, em QUALQUER ponto (começo, meio ou fim; Luigi, 2026-10-09:
    "é só cortar a parte que ele inventou, repetiu ou ficou em silêncio"). Os silêncios saem depois, no corte normal.
    Palavra que FALTOU ou foi TROCADA não tem conserto na edição: devolve None e o take volta para o Flow.
    Devolve (arquivo, [trechos tirados])."""
    sobra = set()
    probs, _ = conferir_fala(ws, fala, sobra)
    if any(not p.startswith(("inventou", "repetiu")) for p in probs): return None
    if any(len(norm(ws[n][0])) > 1 for n in sobra): return None  # palavra só em parte sobra: não corta ao meio
    mudos = [m for m in fala_sem_texto(f, ws, tmp) if not any(ws[n][1] - 0.1 <= m[0] and m[1] <= ws[n][2] + 0.1 for n in sobra)]
    if not sobra and not mudos: return None
    d, faixas, i = dur(f), [], 0
    while i < len(ws):
        if i in sobra: i += 1; continue
        j = i
        while j + 1 < len(ws) and j + 1 not in sobra: j += 1
        a = 0.0 if i == 0 else max(ws[i - 1][2], ws[i][1] - 0.05)
        b = d if j + 1 == len(ws) else min(ws[j + 1][1], ws[j][2] + 0.15)
        faixas.append([a, b]); i = j + 1
    for m0, m1, _ in mudos:  # tira de dentro das faixas a fala que o whisper não escreveu
        nova = []
        for a, b in faixas:
            if m1 <= a or m0 >= b: nova.append([a, b]); continue
            if m0 > a: nova.append([a, m0])
            if m1 < b: nova.append([m1, b])
        faixas = [x for x in nova if x[1] - x[0] > 0.04]
    if not faixas: return None
    filt = "".join(f"[0:v]trim=start={a:.3f}:end={b:.3f},setpts=PTS-STARTPTS[v{n}];"
                   f"[0:a]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS[a{n}];" for n, (a, b) in enumerate(faixas))
    filt += "".join(f"[v{n}][a{n}]" for n in range(len(faixas))) + f"concat=n={len(faixas)}:v=1:a=1[v][a]"
    saida = f"{tmp}/limpo_t{k:02d}.mp4"
    sh(["ffmpeg", "-loglevel", "error", "-y", "-i", f, "-filter_complex", filt, "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-crf", "16", "-preset", "fast", "-c:a", "aac", "-b:a", "192k", saida])
    tirados, atual = [], []
    for n, (w, _, _) in enumerate(ws):
        if n in sobra: atual.append(w)
        elif atual: tirados.append(" ".join(atual)); atual = []
    if atual: tirados.append(" ".join(atual))
    tirados += [f"{txt} ({a:.1f}-{b:.1f}s, fala que o whisper tinha escondido)" for a, b, txt in mudos]
    return saida, tirados


# ---------- 4. cortes ----------
def ilhas(f, ws):
    d = dur(f)
    sil = silencio_rms(f, GAP)
    isl, pos = [], 0.0
    for a, b in sil:
        if a - pos > 0.02: isl.append([pos, a])
        pos = b
    if d - pos > 0.02: isl.append([pos, d])
    isl = [i for i in isl if any(wb > i[0] + 0.03 and wa < i[1] - 0.03 for _, wa, wb in ws)]  # ruído cai
    # palavra ouvida nunca vira silêncio: o trecho dela (até a duração plausível, para não proteger pausa
    # esticada pelo whisper) entra nas ilhas mesmo com volume baixo (V01 temperos: o "one." final sumia)
    teto = lambda w: 0.45 + 0.09 * len(re.sub(r"[^a-z0-9]", "", w.lower()))
    # só nas PONTAS do take: a voz do Flow cai no fim (o "one." baixinho). No meio, o whisper às vezes começa
    # a palavra cedo demais ("because" 0,5s antes do som) e a proteção engolia a pausa.
    ini0 = isl[0][0] if isl else 0.0
    fim0 = isl[-1][1] if isl else d
    for w, wa, wb in ws:
        if not (wa >= fim0 - 0.1 or wb <= ini0 + 0.1):
            continue
        a2, b2 = wa, min(wb, wa + teto(w))
        dentro = sum(max(0.0, min(b2, i[1]) - max(a2, i[0])) for i in isl)
        if dentro < 0.5 * (b2 - a2):  # só a palavra que o corte perdeu; esticada pelo whisper já está coberta
            isl.append([a2, b2])
    isl.sort()
    junto = []
    for i in isl:
        if junto and i[0] <= junto[-1][1] + 0.02: junto[-1][1] = max(junto[-1][1], i[1])
        else: junto.append(list(i))
    isl = junto
    # ilha curta (< 0,4s) junta com a vizinha só se estiverem COLADAS (até 0,25s): sem essa trava, um estalo depois
    # de uma pausa longa "juntava" e a pausa inteira ficava no vídeo (teste 2026-10-10: 1,5s de pausa mantida)
    merged = []
    for i in isl:
        if merged and i[0] - merged[-1][1] <= 0.25 and (i[1] - i[0] < MIN_ISLAND or merged[-1][1] - merged[-1][0] < MIN_ISLAND):
            merged[-1][1] = i[1]
        else: merged.append(list(i))
    merged = [m for m in merged if m[1] - m[0] >= 0.12]  # estalo isolado cai
    sp = []
    for a, b in merged:
        x = [max(0, a - PAD_IN), min(d, b + PAD_OUT)]
        if sp and x[0] - sp[-1][1] < JUNTA: sp[-1][1] = x[1]
        else: sp.append(x)
    return sp

def janela_insert(f, maximo):
    """Insert mudo entra só com a janela de `maximo` s de mais movimento (a ação). Inteiro, ele alongava o vídeo
    em ~7s por insert (teste v04 no Mac, 2026-10-09; no v04 aprovado foram encurtados à mão para 2,5s)."""
    d = dur(f)
    if not maximo or d <= maximo: return [[0.0, d]]
    t = sh_err(f'ffmpeg -hide_banner -i "{f}" -vf "scale=96:-2,tblend=all_mode=difference,signalstats,'
               f'metadata=print:key=lavfi.signalstats.YAVG" -an -f null -')
    ts = [float(x) for x in re.findall(r"pts_time:([\d.]+)", t)]
    ys = [float(x) for x in re.findall(r"YAVG=([\d.]+)", t)]
    if not ts or len(ts) != len(ys): return [[0.0, maximo]]
    ini = max((x for x in ts if x + maximo <= d), default=0.0,
              key=lambda x: sum(y for u, y in zip(ts, ys) if x <= u < x + maximo))
    return [[ini, ini + maximo]]

def segmentos(takes, words, ramp):
    segs = []
    for k, f in takes:
        sp = ilhas(f, words[k]) if words[k] else janela_insert(f, INSERT)  # take mudo: só a ação
        for j, (a, b) in enumerate(sp):
            segs.append(dict(k=k, a=a, b=b, sp=SP))
            if k in ramp and j + 1 < len(sp) and sp[j + 1][0] > b:
                segs.append(dict(k=k, a=b, b=sp[j + 1][0], sp=ramp[k], mute=True))
        if not words[k]:
            segs[-1]["mute"] = True
    o = 0.0
    for s in segs:
        s["o"] = o; s["d"] = (s["b"] - s["a"]) / s["sp"]; o += s["d"]
    return segs

def um_trecho(arg):
    i, s, src, tmp = arg
    out = f"{tmp}/seg{i:03d}.mkv"
    fixo = f"{tmp}/segf{i:03d}.mkv"
    chave = json.dumps([s.get("a"), s.get("b"), s.get("sp"), s.get("mute"), src, FPS, W, H])
    if os.path.exists(fixo) and os.path.exists(f"{fixo}.key") and open(f"{fixo}.key").read() == chave:
        # rodada repetida na mesma pasta de trabalho: reaproveita o trecho já montado
        return fixo, int(sh(["ffprobe", "-v", "error", "-count_packets", "-select_streams", "v:0", "-show_entries",
                             "stream=nb_read_packets", "-of", "csv=p=0", fixo]).strip())
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
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", out, "-c:v", "copy", "-af", f"apad,atrim=end={n / FPS:.6f}",
        "-c:a", "pcm_s16le", fixo])
    open(f"{fixo}.key", "w").write(chave)
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
def alinhar(heard, roteiro_palavras, max_dif=0.08):
    """Tempo de cada palavra do roteiro a partir do que o whisper ouviu, mesmo com contagem diferente
    ("gut-friendly" ouvido como "gut friendly", palavra engolida). None se divergir demais."""
    h = [" ".join(norm(w)) for w, _, _ in heard]; r = [" ".join(norm(w)) for w in roteiro_palavras]
    ops = difflib.SequenceMatcher(None, h, r, autojunk=False).get_opcodes()
    dif = sum(max(i2 - i1, j2 - j1) for op, i1, i2, j1, j2 in ops if op != "equal")
    if dif > max_dif * max(len(r), 1):
        return None
    t = [None] * len(r)
    for op, i1, i2, j1, j2 in ops:
        if op == "equal":
            for d in range(j2 - j1): t[j1 + d] = heard[i1 + d][1]
        elif op == "replace" or op == "insert":
            a = heard[i1][1] if i1 < len(heard) else (heard[-1][2] if heard else 0.0)
            b = heard[i2 - 1][2] if op == "replace" else a
            for d in range(j2 - j1): t[j1 + d] = a + (b - a) * d / max(j2 - j1, 1)
    for i in range(1, len(t)):  # nunca volta no tempo
        t[i] = max(t[i], t[i - 1])
    return t


# palavra que pesa na frase (Auraly): número, dinheiro, tempo, ação forte
FORTES = {"money", "cash", "rich", "call", "found", "never", "always", "everything", "nothing", "today", "tonight",
          "now", "next", "week", "blessing", "seal", "stories", "soulmate", "face", "name", "love", "isn't", "can't",
          "won't", "don't", "stop", "change", "changes", "dark", "light", "open", "closed", "warning", "chosen", "you"}
VAZIAS = {"the", "a", "an", "and", "or", "but", "of", "to", "in", "on", "at", "for", "with", "that", "this", "it", "is",
          "was", "be", "are", "your", "my", "i", "me", "so", "if", "just", "what", "when", "they", "she", "he", "we"}

def palavra_chave(p, n):
    """Índice da palavra que fica grande na página, ou None (referência do Luigi: ~metade das páginas)."""
    limpa = [re.sub(r"[^a-z0-9']", "", w["w"].lower()) for w in p]
    for i, w in enumerate(limpa):
        if re.search(r"\d", w): return i
    for i, w in enumerate(limpa):
        if w in FORTES and len(p) > 1: return i
    cand = [(len(w), i) for i, w in enumerate(limpa) if w not in VAZIAS and len(w) >= 5]
    return max(cand)[1] if cand and n % 2 == 0 else None

def juntar_curtas(pages, minimo=0.15):
    """Página que dura menos de `minimo` s se junta à seguinte. Duas palavras no mesmo instante ("Why?" e
    "Papaya") geravam página de duração ZERO, e o HyperFrames deixa clipe de duração zero na tela muito
    depois (V01 temperos, 2026-10-10: o "why" do T3 apareceu em cima do T5)."""
    out = []
    for i, p in enumerate(pages):
        if out and out[-1] is not None and i < len(pages) and p[0]["t"] - out[-1][0]["t"] < minimo:
            out[-1] = out[-1] + p
        else:
            out.append(list(p))
    return out

def legenda_auraly(ws, segs, total, inserts):
    """Estilo Auraly da referência do Luigi (2026-10-09): a página se monta palavra por palavra no tempo da fala,
    empilha até 3 linhas curtas, uma palavra-chave bem maior; troca no ponto, na vírgula e na troca de take."""
    pages, cur = [], []
    for i, w in enumerate(ws):
        cur.append(w); nx = ws[i + 1] if i + 1 < len(ws) else None
        if (not nx or len(cur) >= 4 or re.search(r"[.!?]$", w["w"]) or (re.search(r",$", w["w"]) and len(cur) >= 2)
                or nx["k"] != w["k"]):
            pages.append(cur); cur = []
    pages = juntar_curtas(pages)
    html, js = [], []
    for n, p in enumerate(pages):
        st = 0 if n == 0 else p[0]["t"]; en = pages[n + 1][0]["t"] if n < len(pages) - 1 else total
        en = min([en] + [s["o"] for s in segs if s["k"] in inserts and s["o"] > st + 0.01])
        big = palavra_chave(p, n)
        spans = []
        for j, w in enumerate(p):
            txt = re.sub(r"[.,!?;:]$", "", w["w"]).lower()
            spans.append(f'<span class="w{" big" if j == big else ""}" id="w{n}_{j}">{txt}</span>')
            t = max(st, w["t"] - 0.03)
            js.append(f'tl.fromTo("#w{n}_{j}", {{ opacity: 0, scale: {0.7 if j == big else 0.9} }}, '
                      f'{{ opacity: 1, scale: 1, duration: {0.12 if j == big else 0.06}, ease: "back.out(2)" }}, {t:.3f});')
        html.append(f'<div class="clip capa" id="cp{n}" data-start="{st:.3f}" data-duration="{en - st:.3f}" '
                    f'data-track-index="{2 + n % 2}"><div class="linhas">{"".join(spans)}</div></div>')
    return html, js, len(pages)

def selos_auraly(total):
    """Selos fixos do canal em TODO vídeo Auraly (Luigi, 2026-10-10): 777 à direita na altura do rosto, 222 à
    esquerda na altura do peito."""
    return [f'<div class="clip selo" id="selo777" style="top: 420px; right: 56px;" data-start="0" data-duration="{total:.3f}" '
            f'data-track-index="6">🇺🇸777🇺🇸</div>',
            f'<div class="clip selo" id="selo222" style="top: 1310px; left: 56px;" data-start="0" data-duration="{total:.3f}" '
            f'data-track-index="7">🔮222🔮</div>']

def legenda_html(segs, heard, roteiro_palavras, total, leaks, up, estilo="fitwell"):
    def seg_at(t):
        return next((s for s in segs if s["o"] <= t < s["o"] + s["d"]), segs[-1])
    tempos = alinhar(heard, roteiro_palavras)
    usa_roteiro = tempos is not None
    if usa_roteiro:
        ws = [dict(w=w, t=a, k=seg_at(a + 0.05)["k"]) for w, a in zip(roteiro_palavras, tempos)]
    else:
        ws = [dict(w=w, t=a, k=seg_at(a + 0.05)["k"]) for w, a, _ in heard]
    pages, cur = [], []
    for i, w in enumerate(ws):
        cur.append(w); nx = ws[i + 1] if i + 1 < len(ws) else None
        if (not nx or len(cur) >= 3 or re.search(r"[.!?]$", w["w"]) or (re.search(r",$", w["w"]) and len(cur) >= 2)
                or nx["k"] != w["k"]):
            pages.append(cur); cur = []
    pages = juntar_curtas(pages)
    html, js = [], []
    # insert mudo = take sem nenhum trecho falado; a legenda some quando ele entra (teste v04 no Mac,
    # 2026-10-09: "of ginger" ficou em cima da mão espremendo o limão nos dois inserts)
    inserts = {s["k"] for s in segs} - {s["k"] for s in segs if not s.get("mute")}
    if estilo == "auraly":
        html, js, npag = legenda_auraly(ws, segs, total, inserts)
        html += selos_auraly(total)
        pages = [None] * npag
    for n, p in enumerate(pages if estilo != "auraly" else []):
        st = 0 if n == 0 else p[0]["t"]; en = pages[n + 1][0]["t"] if n < len(pages) - 1 else total
        en = min([en] + [s["o"] for s in segs if s["k"] in inserts and s["o"] > st + 0.01])
        txt = " ".join(re.sub(r"[.,!?]$", "", w["w"]) for w in p).lower()
        cls = " up" if p[0]["k"] in up else ""
        html.append(f'<div class="clip cap{cls}" id="cp{n}" data-start="{st:.3f}" data-duration="{en - st:.3f}" '
                    f'data-track-index="{2 + n % 2}"><div class="capin">{txt}</div></div>')
    efeito = "flash" if estilo == "auraly" else "leak"  # Auraly: flash claro; FitWell: sem efeito por padrão
    for i, s in enumerate(segs):
        if i > 0 and segs[i - 1]["k"] != s["k"] and s["k"] in leaks:
            t = max(0, s["o"] - 0.12)
            html.append(f'<div class="clip {efeito}" id="lk{i}" data-start="{t:.3f}" data-duration="0.5" data-track-index="5"></div>')
            js.append(f'tl.fromTo("#lk{i}", {{ opacity: 0 }}, {{ opacity: 0.85, duration: 0.14, ease: "power2.out" }}, {t:.3f});')
            js.append(f'tl.to("#lk{i}", {{ opacity: 0, duration: 0.34, ease: "power2.in" }}, {t + 0.16:.3f});')
    return html, js, usa_roteiro, len(pages)

PAGINA = open(os.path.join(AQUI, "pagina_v3.html"), encoding="utf8").read()

def escolher_musica(nome, chave):
    faixas = sorted(glob.glob(f"{MUSICAS}/*.mp3"))
    if not faixas: sys.exit(f"Nenhuma música em {MUSICAS}. Aponte EDICAO_MUSICAS ou rode com --sem-musica.")
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
    # voz já em -14 LUFS; música normalizada em -14 LUFS e baixada 25 dB = 25 dB abaixo da voz, sempre
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", voz, "-ss", f"{ini:.2f}", "-i", musica, "-filter_complex",
        f"[1:a]loudnorm=I=-14:TP=-2:LRA=11,volume={MUSICA_DB}dB,aformat=sample_rates=44100:channel_layouts=mono,"
        f"atrim=0:{total:.3f},afade=t=in:d=0.3,afade=t=out:st={total - 0.8:.2f}:d=0.8[m];"
        f"[0:a][m]amix=inputs=2:normalize=0,atrim=0:{total:.3f},alimiter=limit=0.95[o]",
        "-map", "[o]", "-ar", "44100", "-ac", "1", saida])
    return ini


# ---------- 7. conferências ----------
def quadros(video, ini, n, larg=64):
    """n quadros a partir do quadro ini. Busca com -ss antes do -i (preciso ao decodificar) para não varrer o vídeo inteiro a cada corte."""
    import numpy as np
    alt = int(larg * H / W)
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", f"{ini / FPS:.4f}", "-i", video, "-frames:v", str(n),
                          "-vf", f"scale={larg}:{alt},format=gray", "-f", "rawvideo", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, alt, larg).astype(np.float32)

def fantasmas(video, cortes_q):
    """Quadro misturado: parecido com os DOIS vizinhos de um corte de cena. Corte limpo tem um lado ~igual."""
    achados = []
    for c in cortes_q:
        ini = max(0, c - 3)
        try:
            f = quadros(video, ini, 7)
        except Exception:
            continue
        for j in range(1, len(f) - 1):
            ac = abs(f[j - 1] - f[j + 1]).mean(); ab = abs(f[j - 1] - f[j]).mean(); bc = abs(f[j] - f[j + 1]).mean()
            if ac > 12 and ab > 0.25 * ac and bc > 0.25 * ac:
                achados.append(round((ini + j) / FPS, 2))
    return sorted(set(achados))

def silencios(video, d=0.25):
    return [tuple(x) for x in silencio_rms(video, d)]

def sheet(video, tempos, saida, cols=12, larg=120):
    expr = "+".join(f"between(t,{t - 0.1:.2f},{t + 0.1:.2f})" for t in tempos)
    sh(["ffmpeg", "-loglevel", "error", "-y", "-i", video, "-vf", f"select='{expr}',scale={larg}:-1,tile={cols}x{-(-len(tempos) * 7 // cols)}",
        "-frames:v", "1", saida])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pasta"); ap.add_argument("--producao"); ap.add_argument("--musica"); ap.add_argument("--sem-musica", action="store_true")
    ap.add_argument("--ramp", default="1", help="takes-herói (pausa acelerada 5x em vez de cortada)")
    ap.add_argument("--leaks", default=None, help="takes com efeito na entrada (padrão: FitWell nenhum; Auraly o 2, saída do gancho)")
    ap.add_argument("--estilo", choices=["fitwell", "auraly"], default=None, help="padrão: auraly se a produção for Auraly")
    ap.add_argument("--ritmo", type=float, default=None, help="palavras/s alvo (padrão: 3,8 FitWell, 4,0 Auraly)")
    ap.add_argument("--up", default="1", help="takes com legenda mais alta")
    ap.add_argument("--nome", default=None); ap.add_argument("--trabalho", default=None)
    ap.add_argument("--nota-minima", type=float, default=0.85)
    ap.add_argument("--insert", type=float, default=INSERT, help="segundos de cada insert mudo, na ação (0 = inteiro)")
    a = ap.parse_args()
    globals()["INSERT"] = a.insert
    t0 = time.time(); rel = []
    # qualquer nome de arquivo serve: a ORDEM vem da fala comparada com o roteiro (passo 2)
    arquivos = sorted(os.path.abspath(f) for f in glob.glob(f"{a.pasta}/*.mp4") if "_editado" not in os.path.basename(f))
    if not arquivos: sys.exit("Nenhum .mp4 na pasta")
    def numero(f):
        m = re.search(r"(\d+)", os.path.splitext(os.path.basename(f))[0])
        return int(m.group(1)) if m else None
    nome = a.nome or os.path.basename(os.path.abspath(a.pasta).rstrip("/"))
    # pasta de trabalho única por pasta de takes: duas sessões editando pastas de mesmo nome em paralelo
    # escreveriam no mesmo lugar (2026-10-09); a mesma pasta de takes continua reaproveitando os trechos
    tag = hashlib.md5(os.path.abspath(a.pasta).encode()).hexdigest()[:8]
    tmp = a.trabalho or f"/tmp/edicao/{nome}-{tag}"
    os.makedirs(f"{tmp}/assets", exist_ok=True); shutil.copytree(os.path.join(AQUI, "fonts"), f"{tmp}/fonts", dirs_exist_ok=True)

    log(f"1/7 transcrevendo {len(arquivos)} takes")
    w_arq = {f: palavras(f) for f in arquivos}
    d_arq = {f: " ".join(w for w, _, _ in w_arq[f]) for f in arquivos}
    falantes = {f: t for f, t in d_arq.items() if len(norm(t)) >= 2}
    if not falantes: sys.exit("Nenhum take com fala")

    log("2/7 achando o roteiro e a ordem dos takes pela fala")
    achado = achar_roteiro(falantes, a.producao)
    if not achado: sys.exit("Nenhum roteiro encontrado")
    pasta, arq, falas_arq, nota, linhas = achado
    # posição de cada take = número do take (T__) da frase dele no pacote; mudo usa o número do nome do arquivo.
    # Os dois na MESMA numeração: sem os blocos V__, a frase só tem a posição entre as falas.
    tn = numeros_take(arq)
    pos = {f: tn.get(falas_arq[f], linhas.index(falas_arq[f]) + 1) for f in falantes}
    avisos = []
    mudos = [f for f in arquivos if f not in falantes]
    if mudos and not tn:
        avisos.append("Pacote sem blocos V__: a posição dos takes mudos não é confiável, conferir no cortes.png")
    teto = max(tn.values()) if tn else len(arquivos)
    for f in mudos:
        if numero(f) is not None and not 1 <= numero(f) <= teto:
            sys.exit(f"Take mudo {os.path.basename(f)}: o número no nome ({numero(f)}) não é um take do roteiro "
                     f"(1 a {teto}); provavelmente é o horário do Flow. Renomeie com o número do take (ex.: t07_pimenta.mp4).")
        voz = falas_tabela(arq).get(numero(f), "")
        if re.search(r"[A-Za-z]{3}", voz) and not re.search(r"mudo|no speech|sem fala", voz, re.I):
            avisos.append(f"{os.path.basename(f)} é mudo mas o T{numero(f)} do roteiro tem fala (\"{voz}\"): essa fala NÃO "
                          "entra no vídeo. Regra desde 2026-10-09: take com fala é sempre falado, mudo só sem voz-over")
        if numero(f) in pos.values():
            avisos.append(f"{os.path.basename(f)} é mudo mas o T{numero(f)} do roteiro tem fala: conferir no cortes.png")
    repetidas = {p for p in pos.values() if list(pos.values()).count(p) > 1}
    if repetidas:
        avisos.append("Dois takes com a mesma frase do roteiro: " + ", ".join(
            os.path.basename(f) for f in pos if pos[f] in repetidas) + " (desempate pelo nome do arquivo)")
    for f in arquivos:
        if f not in falantes:
            if numero(f) is None:
                sys.exit(f"Take mudo sem número no nome: {os.path.basename(f)}. Renomeie com a posição (ex.: t03.mp4).")
            pos[f] = numero(f) - 0.5  # mudo entra antes do take falado de mesmo número
            avisos.append(f"{os.path.basename(f)} é mudo: posição pelo nome ({numero(f)}), conferir no cortes.png")
    ordem = sorted(arquivos, key=lambda f: (pos[f], numero(f) or 0, f))
    for i, f in enumerate(ordem, 1):
        if f in falantes and numero(f) is not None and numero(f) <= teto and numero(f) != i:  # horário no nome não é aviso
            avisos.append(f"{os.path.basename(f)} foi para a posição {i} pela fala (o nome dizia {numero(f)})")
    takes = [(i, f) for i, f in enumerate(ordem, 1)]
    # take mudo nunca passa pelo corte de fala: ruído que o whisper "ouve" no insert virava um trecho de 0,6s
    # (teste v04 no Mac, 2026-10-09: a pimenta sumiu e a legenda anterior ficou em cima dela)
    words = {i: (w_arq[f] if f in falantes else []) for i, f in takes}
    ditos = {i: d_arq[f] for i, f in takes}
    falas = {i: falas_arq[f] for i, f in takes if f in falantes}
    rel.append("- Ordem dos takes (pela fala): " + " → ".join(
        f"{i}. {os.path.basename(f)} (T{int(pos[f] + 0.5)})" for i, f in takes))
    rel += [f"  - aviso: {x}" for x in avisos]
    rel.append(f"- Produção: `{os.path.basename(pasta)}` (`{arq.replace(REPO + '/', '').replace('/mnt/project-files/', '')}`), semelhança {nota:.0%}")
    if nota < a.nota_minima: sys.exit(f"Roteiro incerto ({nota:.0%} < {a.nota_minima:.0%}): {arq}. Rode com --producao.")

    log("3/7 conferindo a fala de cada take, palavra por palavra")
    erros_fala, aparados, avisos_escuta = [], [], []
    for k in sorted(falas):
        f = dict(takes)[k]
        probs, esc = conferir_fala(words[k], falas[k])
        if probs or fala_sem_texto(f, words[k], tmp):
            ap = limpar(f, words[k], falas[k], tmp, k)
            if ap:
                novo, tirados = ap
                fora = " / ".join(tirados)
                w2 = palavras(novo)
                probs2, esc2 = conferir_fala(w2, falas[k])
                if probs2:
                    probs += [f"depois do corte ainda: {p}" for p in probs2]
                else:
                    words[k], ditos[k], esc = w2, " ".join(w for w, _, _ in w2), esc2
                    takes = [(i, novo if i == k else g) for i, g in takes]
                    aparados.append(f"{k}. {os.path.basename(f)}: cortado o que o Flow inventou ou repetiu: \"{fora}\"; ouvir a emenda")
                    probs = []
        if probs:
            erros_fala.append(f"{k}. {os.path.basename(f)}: " + "; ".join(probs) + f' | ouvi "{ditos[k]}" | roteiro "{falas[k]}"')
        avisos_escuta += [f"{k}. escuta do whisper, conferir no vídeo: {e}" for e in esc]
    rel.append(f"- Fala dos takes contra o roteiro, palavra por palavra: {'OK' if not erros_fala else 'FALHA'}")
    rel += [f"  - aparado: {x}" for x in aparados]
    rel += [f"  - aviso: {x}" for x in avisos_escuta]
    rel += [f"  - {e}" for e in erros_fala]
    if erros_fala: open(f"{tmp}/RELATORIO.md", "w").write("\n".join(rel)); sys.exit("Take com fala diferente do roteiro; ver RELATORIO.md")

    n = len(takes)
    # estilo pela produção: Auraly tem legenda e efeitos próprios (referências do Luigi, docs/pos-producao-referencias-luigi.md)
    auraly = "auraly" in pasta.lower() or any("pipeline: auraly" in open(x, encoding="utf8", errors="ignore").read()
                                              for x in glob.glob(f"{pasta}/*.md"))
    estilo = a.estilo or ("auraly" if auraly else "fitwell")
    alvo = a.ritmo or (4.0 if estilo == "auraly" else 3.8)
    ramp = {int(x): 5 for x in a.ramp.split(",") if x}
    # sem light leak no FitWell (Luigi, 2026-10-10); no Auraly um flash só na saída do gancho
    leaks = [int(x) for x in a.leaks.split(",")] if a.leaks else ([2] if estilo == "auraly" and n >= 2 else [])
    up = [int(x) for x in a.up.split(",") if x]
    src = dict(takes)

    log("4/7 cortando e montando a base em paralelo")
    segs = segmentos(takes, words, ramp)
    # ritmo dopaminérgico (Luigi, 2026-10-10): velocidade calculada por vídeo para chegar ao alvo de palavras/s das
    # referências dele (3,8 FitWell, 4,0 Auraly), entre 1,0x e 1,25x; a rampa do take-herói não muda
    nw = sum(len(norm(falas[k])) for k in falas)
    vel = [s for s in segs if s["sp"] == SP]
    fixo = sum((s["b"] - s["a"]) / s["sp"] for s in segs if s["sp"] != SP)
    sp = min(1.25, max(1.0, sum(s["b"] - s["a"] for s in vel) / max(0.1, nw / alvo - fixo)))
    o = 0.0
    for s in segs:
        if s in vel: s["sp"] = round(sp, 3)
        s["o"] = o; s["d"] = (s["b"] - s["a"]) / s["sp"]; o += s["d"]
    total = montar_base(segs, src, tmp)
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{tmp}/junto.mkv", "-an", "-c:v", "copy", f"{tmp}/assets/base.mp4"])
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{tmp}/junto.mkv", "-vn", "-af", "loudnorm=I=-14:TP=-1.2,aresample=44100",
        "-ar", "44100", "-ac", "1", f"{tmp}/voz.wav"])
    json.dump(segs, open(f"{tmp}/segs.json", "w"), indent=1)

    log("5/7 legenda, leak e música")
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{tmp}/voz.wav", "-ar", "16000", "-ac", "1", f"{tmp}/voz16.wav"])
    heard = palavras(f"{tmp}/voz16.wav")
    rot_pal = " ".join(falas[k] for k in sorted(falas)).split()
    html, js, usa_rot, npag = legenda_html(segs, heard, rot_pal, total, leaks, up, estilo)
    musica = None if a.sem_musica else escolher_musica(a.musica, os.path.basename(pasta))
    ini = mixar(f"{tmp}/voz.wav", musica, total, f"{tmp}/assets/mix.wav")
    open(f"{tmp}/index.html", "w", encoding="utf8").write(
        PAGINA.replace("{{TOTAL}}", f"{total:.3f}").replace("{{CLIPS}}", "\n".join(html)).replace("{{JS}}", "\n".join(js)))

    log("6/7 lint e render")
    lint = subprocess.run("npx -y hyperframes@0.8.143 lint .", shell=True, cwd=tmp, capture_output=True, text=True).stdout
    nerr = re.search(r"(\d+) error", lint)
    sh(f"npx -y hyperframes@0.8.143 render . -o renders/final.mp4 --quality high --quiet", cwd=tmp)
    saida = f"{tmp}/{nome}_editado.mp4"
    for crf in (19, 22, 24, 25, 26, 28):  # sobe o crf até caber na cópia para o Mac (limite de 25 MB)
        sh(["ffmpeg", "-loglevel", "error", "-y", "-i", f"{tmp}/renders/final.mp4", "-c:v", "libx264", "-crf", str(crf), "-preset", "slow",
            "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-c:a", "aac", "-b:a", "192k", saida])
        if os.path.getsize(saida) < 24.5e6: break

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
        "Nenhuma legenda com menos de 0,1s": not re.search(r'data-duration="0\.0\d\d"', "\n".join(h for h in html if "cap" in h)),
        "Arquivo abaixo de 25 MB": mb < 25,
    }
    rel += [f"- {k}: {'OK' if v else 'FALHA'}" for k, v in ok.items()]
    if sil: rel.append(f"  - silêncios: {sil}")
    if fant: rel.append(f"  - quadro fantasma em: {fant}s")
    rel += [f"- Duração {total:.1f}s · {len(heard) / total:.2f} palavras/s · {len(segs)} trechos ({sum(1 for s in segs if s.get('mute'))} rampas) · {npag} legendas",
            f"- Música: {os.path.basename(musica) + f' (a partir de {ini:.1f}s, {MUSICA_DB} dB da voz)' if musica else 'sem música'}",
            f"- Estilo {estilo} · fala a {sp:.2f}x (alvo {alvo} palavras/s) · {'flash' if estilo == 'auraly' else 'light leak'} na entrada dos takes {leaks or 'nenhum'}; rampa nos takes {sorted(ramp)}" + (f"; legenda alta nos takes {up}" if estilo != "auraly" else "; selos 777/222"),
            f"- Arquivo: `{saida}` ({mb:.1f} MB) · tempo total {time.time() - t0:.0f}s",
            "- Olhar antes de entregar: `cortes.png` (pulo) e `legendas.png` (nada sobre rosto ou herói)"]
    open(f"{tmp}/RELATORIO.md", "w").write(f"# Relatório de edição · {nome}\n\n" + "\n".join(rel) + "\n")
    print("\n".join(rel))
    sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
