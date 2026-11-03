#!/usr/bin/env python3
"""Edição automática de takes do Flow, num comando só (estilo v3 aprovado pelo Luigi em 2026-10-09).

    python3 editar.py <pasta_dos_takes> [--producao <nome ou pasta>] [--musica <nome>] [--insert 2.5] [--estilo auraly] [--ritmo 3.8] [--ramp 1] [--leaks 2,4] [--up 1]

Faz, em ordem, e para no primeiro problema:
  1. transcreve cada take (faster-whisper, modelo carregado uma vez);
  2. acha sozinho o roteiro da produção comparando a fala com os roteiros do repo e das entregas;
  3. confere cada take PALAVRA POR PALAVRA; o que o Flow inventou ou repetiu é cortado em qualquer ponto;\n     palavra que faltou ou foi trocada para a edição (o take volta para o Flow);
  4. ordena pelo número do take (T__) do pacote; insert mudo entra só com a janela da ação;
     corta pelos silêncios reais e monta a base com os trechos EM PARALELO (minterpolate por trecho);
  5. legenda (tempo do whisper no vídeo cortado, texto do roteiro), light leak, música a -18 dB da voz;
  6. lint e render no HyperFrames, sem recompressão (teto de entrega 100 MB, Luigi 2026-10-15);
  7. conferências automáticas (silêncio, quadro fantasma, contagem de palavras) + contact sheets,
     e escreve RELATORIO.md com passa/falha.
Regras e porquês: docs/pos-producao-edicao-regras.md. Nada aqui muda o estilo aprovado.
"""
import argparse, concurrent.futures as cf, difflib, glob, hashlib, json, os, re, shutil, subprocess, sys, time

AQUI = os.path.dirname(os.path.abspath(__file__))
# motor v4 precisa de WhisperX e Pillow, que estão no .venv-operacao: se este Python não tem, roda de novo nele
_VENV = os.path.abspath(os.path.join(AQUI, "../../../..", ".venv-operacao", "bin", "python"))
try:
    import PIL, whisperx  # noqa: F401
except ImportError:
    if os.path.exists(_VENV) and os.path.realpath(sys.executable) != os.path.realpath(_VENV):
        os.execv(_VENV, [_VENV, os.path.abspath(__file__)] + sys.argv[1:])
sys.path.insert(0, AQUI)
import motor  # noqa: E402
import plano_editorial  # noqa: E402
PLANO_EDITORIAL = None  # opt-in por produção, nunca herdado pela Auraly
REPO = os.path.abspath(os.path.join(AQUI, "../../../.."))
# nuvem: /mnt/project-files; Mac: edicao/musicas do repo (teste no Mac, 2026-10-09: ficava sem achar a faixa)
MUSICAS = os.environ.get("EDICAO_MUSICAS") or next(
    (p for p in ("/mnt/project-files/edicao/musicas", os.path.join(REPO, "edicao/musicas")) if glob.glob(f"{p}/*.mp3")),
    os.path.join(REPO, "edicao/musicas"))
ENTREGAS = "/mnt/project-files/entregas"

SP, GAP, PAD_IN, PAD_OUT, MIN_ISLAND, JUNTA, W, H, FPS = 1.12, 0.15, 0.05, 0.11, 0.4, 0.05, 1080, 1920, 30
INSERT = 2.5  # segundos do insert mudo (antes da aceleração); --insert 0 = inteiro
IDIOMA = "en"
LEGENDA_DINAMICA = True  # Luigi, 2026-10-13: legenda mais dinâmica (Montserrat caixa alta, palavra ativa amarela)
MUSICA_DB = -18  # Luigi, 2026-10-10: -18 dB (cama do media-use da HyperFrames, 0,12) aprovado; -25 sumia, -10 atrapalhou a fala


def sh(cmd, **kw):
    if isinstance(cmd, list) and not kw:
        return motor._sh(cmd)  # -nostdin + fallback libx264 se o h264_videotoolbox falhar
    return subprocess.run(cmd, shell=isinstance(cmd, str), check=True, capture_output=True, text=True,
                          stdin=subprocess.DEVNULL, **kw).stdout


def sh_err(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, stdin=subprocess.DEVNULL).stderr


def _chave_arq(f):
    real = os.path.abspath(f)
    try:
        st = os.stat(real)
        return (real, st.st_mtime_ns, st.st_size)
    except OSError:
        return (real, 0, 0)


_rms = {}
def rms_janelas(f):
    """Volume médio (dB) de cada janela de 50 ms do áudio do take (reaproveita motor.rms10 para não abrir ffmpeg 2x)."""
    kf = _chave_arq(f)
    if kf not in _rms:
        import math
        r10 = motor.rms10(f)
        out = []
        for i in range(0, len(r10), 5):
            bloco = r10[i:i + 5]
            p_med = sum(10.0 ** (max(-120.0, x) / 10.0) for x in bloco) / len(bloco)
            out.append(round(10.0 * math.log10(p_med), 2) if p_med > 1e-12 else -120.0)
        _rms[kf] = out
    return _rms[kf]

_limiar = {}
def limiar(f):
    """Volume abaixo do qual o take está "em silêncio", medido no próprio take (Luigi, 2026-10-10: o Flow às vezes
    gera intervalo longo entre duas falas do mesmo take, e todo silêncio no meio do take sai). Com -35 dB fixo, a
    pausa com som de ambiente ou chiado do Flow não era cortada. Agora: fundo do take (5% mais baixo) + 6 dB,
    nunca acima da fala - 12 dB, nunca abaixo de -35 dB."""
    kf = _chave_arq(f)
    if kf not in _limiar:
        v = sorted(rms_janelas(f))
        if len(v) < 20: _limiar[kf] = -35.0
        else:
            fundo, fala = v[len(v) // 20], v[len(v) * 7 // 10]
            # piso -35: mais baixo, o ruído de sala das pausas virava "som" e as pausas ficavam (2026-10-10).
            # Palavra dita baixinho é protegida em `ilhas`, pelo tempo da palavra, não pelo limiar.
            _limiar[kf] = round(max(-35.0, min(fundo + 6, fala - 12)), 1)
    return _limiar[kf]

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

DEZENAS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()

def por_extenso(n):
    """Número como se fala na receita: 30 = thirty, 25 = twenty five, 325 = three twenty five (temperatura,
    como o roteiro escreve), 300 = three hundred. Meredith T3 e Marshall T3, 2026-10-10: o whisper escreveu
    "30" e "325" e o take certo travava como "trocou"."""
    if n <= 20: return [NUMEROS[n]]
    if n < 100: return [DEZENAS[n // 10]] + ([NUMEROS[n % 10]] if n % 10 else [])
    if n < 1000: return [NUMEROS[n // 100]] + (por_extenso(n % 100) if n % 100 else ["hundred"])
    return [str(n)]

def norm(t):
    # o whisper escreve "2 cups" onde o roteiro diz "two cups": número vira palavra antes de comparar
    texto = t.lower().replace("’", "'")
    # O CTA Auraly soletra o selo; os dois transcritores escrevem 222 em algarismos.
    texto = re.sub(r"\b222\b", "dos dos dos" if IDIOMA == "es" else "two two two", texto)
    if IDIOMA == "es":
        import unicodedata
        texto = "".join(c for c in unicodedata.normalize("NFD", texto) if not unicodedata.combining(c))
        digitos = "cero uno dos tres cuatro cinco seis siete ocho nueve".split()
        return [digitos[int(w)] if w.isdigit() and len(w) == 1 else w
                for w in re.sub(r"[^a-z0-9' ]", " ", texto).split()]
    ws = re.sub(r"[^a-z0-9' ]", " ", texto).split()
    return [x for w in ws for x in (por_extenso(int(w)) if w.isdigit() else [w])]


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


# ---------- 1. transcrição ----------
_modelo = None
_modelo_small = None
def _obter_modelo(usar_small=False):
    global _modelo, _modelo_small
    from faster_whisper import WhisperModel
    if usar_small:
        if _modelo_small is None:
            _modelo_small = WhisperModel("small.en" if IDIOMA == "en" else "small", device="cpu", compute_type="int8", cpu_threads=2)
        return _modelo_small
    if _modelo is None:
        _modelo = WhisperModel("base.en" if IDIOMA == "en" else "base", device="cpu", compute_type="int8", cpu_threads=2)
    return _modelo

def palavras(f, usar_small=False):
    cache_w = f"{f}.words{'.sm' if usar_small else ''}.json"
    try:
        st = os.stat(f)
        chave_w = f"{int(st.st_mtime)}:{st.st_size}:{IDIOMA}"
        if os.path.exists(cache_w):
            dw = json.load(open(cache_w))
            if dw.get("k") == chave_w and "out" in dw:
                return dw["out"]
    except Exception:
        chave_w = None
    wav = motor.wav16k(f)
    if not wav:
        return []  # sem trilha de áudio: take mudo
    mod = _obter_modelo(usar_small=usar_small)
    segs, _ = mod.transcribe(wav, language=IDIOMA, word_timestamps=True, beam_size=1)
    out = [[w.word.strip(), round(w.start, 3), round(w.end, 3)] for s in segs for w in s.words]
    if chave_w:
        try:
            tmp_cw = f"{cache_w}.{os.getpid()}.tmp"
            with open(tmp_cw, "w") as fh:
                json.dump({"k": chave_w, "out": out}, fh)
            os.replace(tmp_cw, cache_w)
        except Exception:
            pass
    return out


# ---------- 2. achar o roteiro ----------
FALA = re.compile(r'(?:speaks|frase|says|line)[^"\n]{0,140}?:\s*"([^"]{12,})"', re.I)

def falas_por_producao(forcada=None):
    if forcada:
        pasta_direta = os.path.join(REPO, "producao", os.path.basename(os.path.normpath(forcada)))
        if os.path.isdir(pasta_direta):
            fontes = glob.glob(f"{pasta_direta}/**/*.md", recursive=True)
        else:
            fontes = glob.glob(f"{REPO}/producao/*/**/*.md", recursive=True) + glob.glob(f"{ENTREGAS}/**/*.md", recursive=True)
    else:
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

PRODUTO_TOPO = 1300  # legenda abaixo do produto: o pote na mão fica de ~840 a ~1180 px (teste de 5 vídeos, 2026-10-15)


def takes_com_produto(pasta):
    """Números de take (T__) em que o produto está em quadro, lidos do pacote: o K__ cuja âncora é a imagem do
    produto (Mapa de âncoras) e os T__ que usam esse K__ (Índice de geração). Na venda com o pote no peito, a
    legenda do centro cobria o rótulo (Cassidy, Marshall, 2026-10-15)."""
    arq = os.path.join(pasta, "PROMPTS_PRODUCAO.md")
    if not os.path.exists(arq):
        return set()
    txt = open(arq, encoding="utf8", errors="ignore").read()
    ks = {int(m.group(1)) for m in re.finditer(r"^\|\s*K(\d+)\s*\|([^|\n]*)\|", txt, re.M)
          if re.search(r"produto|product|REF-LIVRO|frasco|bottle|jar", m.group(2), re.I)}
    return {int(m.group(1)) for m in re.finditer(r"^\|\s*T(\d+)\s*\|\s*K(\d+)\s*\|", txt, re.M) if int(m.group(2)) in ks}


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
    for pasta, arqs in falas_por_producao(forcada).items():
        if forcada and os.path.basename(pasta.rstrip("/")) != forcada and pasta != forcada:
            continue
        for arq, linhas in arqs.items():
            esc = {k: max(linhas, key=lambda l: parecido(t, l)) for k, t in ditos.items()}
            nota = sum(parecido(ditos[k], esc[k]) for k in ditos) / len(ditos)
            if not melhor or nota > melhor[3]:
                melhor = (pasta, arq, esc, nota, list(dict.fromkeys(linhas)))
    return melhor


CONTRACOES = {"it's": "it is", "don't": "do not", "doesn't": "does not", "isn't": "is not", "you're": "you are",
              "i'm": "i am", "that's": "that is", "can't": "can not", "cannot": "can not", "won't": "will not", "we're": "we are",
              "they're": "they are", "i'll": "i will", "you'll": "you will", "here's": "here is", "what's": "what is",
              "onto": "on to", "into": "in to", "everyday": "every day", "anymore": "any more",
              "20s": "twenties", "30s": "thirties", "40s": "forties", "50s": "fifties", "60s": "sixties", "70s": "seventies"}

# palavra curta trocada por outra curta é escuta do whisper ("drop the spoonful" por "drop a spoonful")
PEQUENAS = {"a", "an", "the", "and", "in", "on", "of", "to", "at", "for", "is", "it", "this", "that", "your", "you",
            "oh", "no", "so", "now"}

def escuta_ok(h, r):
    """Tokens ouvidos `h` contra os do roteiro `r` (mesmo tamanho): iguais ou erro de escuta do whisper."""
    return len(h) == len(r) and all(a == b or (a in PEQUENAS and b in PEQUENAS)
                                    or difflib.SequenceMatcher(None, a, b).ratio() >= 0.6 for a, b in zip(h, r))

def conferir_fala(ws, fala, sobra=None):
    """Comparação lexical estrita. Só números e contrações equivalentes são normalizados.
    Similaridade de grafia não prova que uma palavra foi falada; divergência exige auditoria ASR.
    `sobra`, se passado, recebe índices das palavras extras na transcrição."""
    def tokens(texto):
        return [x for t in norm(texto) for x in
                (CONTRACOES.get(t, t).split() if IDIOMA == "en" else [t])]
    hw, dono = [], []
    for n, (w, _, _) in enumerate(ws):
        for t in tokens(w): hw.append(t); dono.append(n)
    rt = tokens(fala)
    probs = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, hw, rt, autojunk=False).get_opcodes():
        h, r = " ".join(hw[i1:i2]), " ".join(rt[j1:j2])
        if op == "equal": continue
        if op == "replace":
            probs.append(f'trocou "{r}" por "{h}"')
        elif op == "delete":
            e = hw[i1:i2]; n = len(e)
            rep = e == hw[i2:i2 + n] or e == hw[max(0, i1 - n):i1]
            probs.append(f'{"repetiu" if rep else "inventou"} "{h}"')
            if sobra is not None: sobra.update(dono[i1:i2])
        else:
            probs.append(f'faltou "{r}"')
    return probs, []

def aplicar_excecoes_fala(f, problemas, fala, registro):
    """Exceções pontuais autorizadas: arquivo, hash, roteiro e divergência devem coincidir.
    Nunca enfraquece a comparação lexical geral nem permite novas divergências."""
    item = registro.get(os.path.realpath(f))
    if not item or norm(item.get("approved_script", "")) != norm(fala):
        return problemas, []
    digest = hashlib.sha256()
    with open(f, "rb") as fonte:
        for bloco in iter(lambda: fonte.read(1024 * 1024), b""):
            digest.update(bloco)
    if digest.hexdigest() != item.get("sha256"):
        return problemas, []
    permitidos = set(item.get("allowed_problems", []))
    aceitos = [p for p in problemas if p in permitidos]
    return [p for p in problemas if p not in permitidos], aceitos

def ouvir_trecho(f, a, b, tmp, com_tempos=True):
    """Transcreve um trecho sozinho e devolve as palavras com tempo absoluto: isolado, o whisper escreve o que
    foi dito (no take inteiro ele suprime a fala repetida)."""
    t = f"{tmp}/trecho_{hashlib.md5(f'{f}{a}{b}'.encode()).hexdigest()[:8]}.wav"
    wav_src = motor.wav16k(f, tmp)
    if not wav_src:
        return []
    precisa = not os.path.exists(t)
    if not precisa:
        try:
            precisa = os.path.getmtime(t) < os.path.getmtime(f) or os.path.getsize(t) <= 44
        except OSError:
            precisa = True
    if precisa:
        import wave
        with wave.open(wav_src, "rb") as wf:
            taxa = wf.getframerate()
            i0 = max(0, min(wf.getnframes(), int(round(a * taxa))))
            i1 = max(i0, min(wf.getnframes(), int(round(b * taxa))))
            wf.setpos(i0)
            fatia = wf.readframes(i1 - i0)
        t_tmp = f"{t}.{os.getpid()}.tmp.wav"
        with wave.open(t_tmp, "wb") as wf_out:
            wf_out.setnchannels(1)
            wf_out.setsampwidth(2)
            wf_out.setframerate(16000)
            wf_out.writeframes(fatia)
        os.replace(t_tmp, t)
    if not com_tempos:
        mod = _obter_modelo(usar_small=False)
        segs, _ = mod.transcribe(t, language=IDIOMA, word_timestamps=False, beam_size=1)
        return [[w.strip(), a, b] for s in segs for w in s.text.strip().split() if w.strip()]
    return [[w, x + a, y + a] for w, x, y in palavras(t)]

def palavras_por_trechos(f, tmp, pausa=0.3):
    """Transcreve o take em pedaços de voz (separados por pausas de `pausa` s) e junta com tempo absoluto. No take
    inteiro o whisper às vezes come a palavra da ponta (Cassidy T2, 2026-10-10: "baking powder" no começo e
    "then shape it into buns" no fim sumiam; ouvidos em trechos, estavam lá). Só serve de segunda escuta."""
    d = dur(f)
    som, pos = [], 0.0
    for a, b in silencio_rms(f, pausa):
        if a - pos > 0.12: som.append([max(0.0, pos - 0.05), min(d, a + 0.05)])
        pos = b
    if d - pos > 0.12: som.append([max(0.0, pos - 0.05), d])
    out = []
    for a, b in som:
        out += ouvir_trecho(f, a, b, tmp)
    return out

_cache_fst = {}
def fala_sem_texto(f, ws, tmp, minimo=0.35, so_interno=False):
    """Fala que está no áudio e não está na transcrição. O whisper SUPRIME fala repetida (teste 2026-10-09:
    "...from the store, bought black pepper from the store, drop..." saiu sem a repetição em todas as
    configurações) e esconde ela de dois jeitos: um trecho com som e sem palavra, ou uma palavra ESTICADA por
    cima dela ("store" durando 2,1s). Cada suspeito é transcrito sozinho; só vira corte se tiver palavra.
    Devolve [[início, fim, texto]]."""
    chave = (f, len(ws), minimo, so_interno)
    if chave in _cache_fst:
        return _cache_fst[chave]
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
    ini_fala = ws[0][1] if ws else 0.0
    fim_fala = ws[-1][2] if ws else d
    min_som = max(minimo, 0.55) if so_interno else minimo
    min_est = max(minimo, 0.65) if so_interno else minimo
    achados = []
    for a, b in som:  # 1) som sem palavra
        if so_interno:
            a, b = max(a, ini_fala), min(b, fim_fala)
            if b - a < min_som:
                continue
        x = a
        for c0, c1 in cobre:
            if c1 <= x or c0 >= b: continue
            if c0 > x and c0 - x >= min_som: achados.append([x, c0])
            x = max(x, c1)
        if b - x >= min_som: achados.append([x, b])
    for w, a, b in ws:  # 2) palavra esticada por cima de outra fala (só conta o tempo com som real, não silêncio colado pelo whisper)
        if b - a > teto(w) + min_est:
            som_dur = sum(max(0.0, min(b, s1) - max(a, s0)) for s0, s1 in som)
            if som_dur > teto(w) + min_est:
                achados.append([a, b, w])
    cortes = []
    for ach in achados:
        a, b = ach[0], ach[1]
        a_pad, b_pad = max(0, a - 0.02), min(d, b + 0.02)
        ouvido_rapido = ouvir_trecho(f, a_pad, b_pad, tmp, com_tempos=False)
        if len(ach) == 3:  # esticada: a primeira palavra ouvida é a própria; o resto é sobra
            resto_rap = [o for o in ouvido_rapido if norm(o[0]) != norm(ach[2])][1:] if ouvido_rapido and norm(ouvido_rapido[0][0]) != norm(ach[2]) else ouvido_rapido[1:]
            if resto_rap:
                ouvido = ouvir_trecho(f, a_pad, b_pad, tmp, com_tempos=True)
                resto = [o for o in ouvido if norm(o[0]) != norm(ach[2])][1:] if ouvido and norm(ouvido[0][0]) != norm(ach[2]) else ouvido[1:]
                if resto: cortes.append([max(a, resto[0][1] - 0.05), b, " ".join(o[0] for o in resto)])
        elif ouvido_rapido:
            cortes.append([a, b, " ".join(o[0] for o in ouvido_rapido)])
    junto = []  # o mesmo trecho achado pelos dois jeitos vira um corte só, com o texto mais longo
    for a, b, t in sorted((float(a), float(b), t) for a, b, t in cortes):
        if junto and a <= junto[-1][1]:
            junto[-1][1] = max(junto[-1][1], b)
            if len(t) > len(junto[-1][2]): junto[-1][2] = t
        else: junto.append([a, b, t])
    _cache_fst[chave] = junto
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
        a = 0.0 if i == 0 else max(ws[i - 1][2], ws[i][1] + (0.02 if (i - 1) in sobra else -0.05))
        b = d if j + 1 == len(ws) else min(ws[j + 1][1], ws[j][2] + (0.04 if (j + 1) in sobra else 0.15))
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
    v_enc = (["-c:v", "h264_videotoolbox", "-q:v", "72", "-profile:v", "high"]
             if sys.platform == "darwin" else ["-c:v", "libx264", "-crf", "16", "-preset", "fast"])
    sh(["ffmpeg", "-loglevel", "error", "-y", "-i", f, "-filter_complex", filt, "-map", "[v]", "-map", "[a]",
        *v_enc, "-c:a", "aac", "-b:a", "192k", saida])
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
    # só no FIM do take: a voz do Flow cai no fim (o "one." baixinho). No meio, o whisper às vezes começa
    # a palavra cedo demais ("because" 0,5s antes do som) e a proteção engolia a pausa.
    ini0 = isl[0][0] if isl else 0.0
    fim0 = isl[-1][1] if isl else d
    for w, wa, wb in ws:
        if wa < fim0 - 0.1:  # só a ponta FINAL: o whisper sempre começa a 1ª palavra em 0,0s e a proteção no
            continue          # início trazia o silêncio de abertura do take (V02 chips, 2026-10-10)
        a2, b2 = wa, min(wb, wa + teto(w))
        # e só até onde ainda há voz fraca (limiar - 10 dB): o whisper estica a última palavra e o silêncio
        # depois do "it." final ficava (V03 canela, 2026-10-10)
        rms, fraco = rms_janelas(f), limiar(f) - 10
        vivos = [n * 0.05 + 0.05 for n in range(int(a2 / 0.05), min(len(rms), int(b2 / 0.05) + 1)) if rms[n] >= fraco]
        if not vivos:
            continue
        b2 = min(b2, max(vivos))
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

def segmentos(takes, words, ramp, alinhado=None):
    segs = []
    alinhado = alinhado or {}
    for k, f in takes:
        if not words[k]:
            sp = janela_insert(f, INSERT)  # take mudo: só a ação
        elif alinhado.get(k):
            sp = motor.ilhas_v4(f, alinhado[k])  # motor v4: bordas reais das palavras
        else:
            sp = ilhas(f, words[k])
        if PLANO_EDITORIAL:
            if any(p["take"] == k and p["end"] - p["start"] < 2 / FPS for p in PLANO_EDITORIAL.get("protected_intervals", [])):
                raise ValueError("Proteção menor que dois frames; revisar intervalo")
            sp = plano_editorial.proteger_intervalos(sp, k, PLANO_EDITORIAL, dur(f))
        for j, (a, b) in enumerate(sp):
            segs.append(dict(k=k, a=a, b=b, sp=SP))
            if k in ramp and j + 1 < len(sp) and sp[j + 1][0] > b:
                segs.append(dict(k=k, a=b, b=sp[j + 1][0], sp=ramp[k], mute=True))
        if not words[k]:
            for trecho in segs:
                if trecho["k"] == k:
                    trecho["mute"] = True
    # trecho de menos de 2 quadros cai: a pausa curta do take-herói acelerada 5x virava trecho sem nenhum quadro
    # e a montagem quebrava (V02 chips, 2026-10-10); juntar a pausa à fala trazia a pausa de volta
    segs = [s for s in segs if (s["b"] - s["a"]) / s["sp"] >= 2.0 / FPS]
    o = 0.0
    for s in segs:
        s["o"] = o; s["d"] = (s["b"] - s["a"]) / s["sp"]; o += s["d"]
    return segs

def um_trecho(arg):
    i, s, src, tmp = arg
    fixo = f"{tmp}/segf{i:03d}.mkv"
    n = max(1, round(s["d"] * FPS))
    chave = json.dumps([s.get("a"), s.get("b"), s.get("sp"), s.get("mute"), src, FPS, W, H, "v4_fast", n])
    if os.path.exists(fixo) and os.path.exists(f"{fixo}.key") and open(f"{fixo}.key").read() == chave:
        # rodada repetida na mesma pasta de trabalho: reaproveita o trecho já montado
        return fixo, n
    # motor v4: um passe só por trecho (vídeo com end_frame=n + áudio com apad,atrim=end=n/FPS, sem deriva de lábio)
    v = motor.filtro_trecho(s["a"], s["b"], s["sp"], s["d"])
    if s.get("mute"):
        a = f"aevalsrc=0:d={n / FPS:.6f}:s=44100,aformat=sample_rates=44100:channel_layouts=mono,atrim=end={n / FPS:.6f}[a0]"
    else:
        a = (f"[0:a]atrim=start={s['a']:.3f}:end={s['b']:.3f},asetpts=PTS-STARTPTS,atempo={s['sp']},"
             f"aformat=sample_rates=44100:channel_layouts=mono,afade=t=in:d=0.012,"
             f"afade=t=out:st={max(0, s['d'] - 0.02):.3f}:d=0.02,apad,atrim=end={n / FPS:.6f}[a0]")
    usa_vt = sys.platform == "darwin"
    hw_in = ["-hwaccel", "videotoolbox"] if usa_vt else []
    v_enc = (["-c:v", "h264_videotoolbox", "-q:v", "74", "-profile:v", "high", "-bf", "0"]
             if usa_vt else ["-c:v", "libx264", "-crf", "12", "-preset", "veryfast"])
    sh(["ffmpeg", "-y", "-loglevel", "error", "-threads", "2", *hw_in, "-i", src, "-filter_complex", f"{v};{a}",
        "-map", "[v]", "-map", "[a0]", *v_enc, "-pix_fmt", "yuv420p",
        "-g", "15", "-r", str(FPS), "-c:a", "pcm_s16le", fixo])
    open(f"{fixo}.key", "w").write(chave)
    return fixo, n

def montar_base(segs, src, tmp):
    trabalhos = [(i, s, src[s["k"]], tmp) for i, s in enumerate(segs)]
    # EDICAO_WORKERS: o fila_edicao.py roda 3 vídeos juntos e limita cada um a 3 trechos (Luigi, 2026-10-15)
    with cf.ThreadPoolExecutor(max_workers=int(os.environ.get("EDICAO_WORKERS") or os.cpu_count() or 4)) as ex:
        res = list(ex.map(um_trecho, trabalhos))
    with open(f"{tmp}/lista.txt", "w") as fh:
        fh.writelines(f"file '{f}'\n" for f, _ in res)
    # Grava assets/base.mp4 e voz.wav num único comando direto do concat (sem gravar/ler junto.mkv de 60 MB)
    sh(["ffmpeg", "-y", "-loglevel", "error", "-threads", "2", "-f", "concat", "-safe", "0", "-i", f"{tmp}/lista.txt",
        "-map", "0:v", "-c:v", "copy", f"{tmp}/assets/base.mp4",
        "-map", "0:a", "-af", "loudnorm=I=-14:TP=-1.2,aresample=44100", "-ar", "44100", "-ac", "1", f"{tmp}/voz.wav"])
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

def juntar_curtas(pages, minimo=0.5):
    """Página que dura menos de `minimo` s se junta à seguinte (0,5s = regra do embedded-captions da HyperFrames,
    Luigi 2026-10-10: regras da HyperFrames têm prioridade; antes era 0,15s). Duas palavras no mesmo instante ("Why?" e
    "Papaya") geravam página de duração ZERO, e o HyperFrames deixa clipe de duração zero na tela muito
    depois (V01 temperos, 2026-10-10: o "why" do T3 apareceu em cima do T5)."""
    out = []
    for p in pages:
        if PLANO_EDITORIAL and out and p[0]["k"] != out[-1][0]["k"]:
            out.append(list(p)); continue  # não atravessar mudança de take para prolongar legenda
        if out and p[0]["t"] - out[-1][0]["t"] < minimo:
            curta = out.pop()
            # página curta que FECHA frase vai para a anterior; senão "stay. / I have" virava "stay i" (V03, 2026-10-10)
            if re.search(r"[.!?,]$", curta[-1]["w"]) and out and out[-1][-1]["k"] == curta[0]["k"]:
                out[-1] = out[-1] + curta
                out.append(list(p))
            else:
                out.append(curta + list(p))
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
        if (not nx or len(cur) >= (PLANO_EDITORIAL.get("captions", {}).get("max_words", 3) if PLANO_EDITORIAL else 3) or re.search(r"[.!?]$", w["w"]) or (re.search(r",$", w["w"]) and len(cur) >= 2)
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
    if PLANO_EDITORIAL and musica and "music" in PLANO_EDITORIAL:
        ini = plano_editorial.music_start_seconds(PLANO_EDITORIAL)
        if ini >= dur(musica):
            raise ValueError("Ponto de entrada musical fora da faixa")
        envelope = plano_editorial.filtro_musica(total, PLANO_EDITORIAL, base_db=MUSICA_DB)
        # Só a cama é repetida; atrim limita a entrada antes da normalização.
        filtro = (f"[1:a]atrim=duration={total:.6f},asetpts=PTS-STARTPTS,"
                  f"loudnorm=I=-14:TP=-2:LRA=11,{envelope},"
                  "aformat=sample_rates=44100:channel_layouts=mono[m];"
                  f"[0:a][m]amix=inputs=2:normalize=0,atrim=0:{total:.6f},alimiter=limit=0.95[o]")
        sh(["ffmpeg", "-y", "-loglevel", "error", "-i", voz,
            "-stream_loop", "-1", "-ss", str(ini), "-i", musica, "-filter_complex", filtro,
            "-map", "[o]", "-ar", "44100", "-ac", "1", saida])
        return ini
    if not musica:
        shutil.copy(voz, saida); return 0.0
    log_ = sh_err(f'ffmpeg -hide_banner -t 40 -i "{musica}" -af silencedetect=noise=-40dB:d=0.3 -f null -')
    m = re.search(r"silence_start: 0(?:\.0+)?\s.*?silence_end: ([\d.]+)", log_, re.S)
    ini = float(m.group(1)) if m else 0.0  # pula silêncio de abertura da faixa
    # voz já em -14 LUFS; música normalizada em -14 LUFS e baixada 18 dB = 18 dB abaixo da voz, sempre
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

def fantasmas(video, cortes_q, segs=None, src=None):
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
                # v4 não interpola: movimento natural também aciona o teste antigo.
                # Só dispensar se o quadro suspeito existir no take original (erro médio <=3/255).
                t = (ini + j) / FPS
                if segs and src:
                    frame_n = ini + j
                    candidatos = [s for s in segs if round(s["o"] * FPS) - 2 <= frame_n < round((s["o"] + s["d"]) * FPS) + 2]
                    corresponde = False
                    for s in candidatos:
                        origem_t = s["a"] + min(max(0, t - s["o"]), s["d"]) * s["sp"]
                        try:
                            orig = quadros(src[s["k"]], max(0, round(origem_t * FPS) - 10), 24)
                            if len(orig) and min(abs(q - f[j]).mean() for q in orig) <= 3:
                                corresponde = True
                                break
                        except Exception:
                            pass
                    if corresponde:
                        continue
                achados.append(round((ini + j) / FPS, 2))
    return sorted(set(achados))

def silencios(video, d=0.45):
    return [tuple(x) for x in silencio_rms(video, d)]

def sheet(video, tempos, saida, cols=12, larg=120):
    if not tempos:
        from PIL import Image
        Image.new("RGB", (larg, int(larg * H / W)), (0, 0, 0)).save(saida)
        return
    # Busca direta por corte (-ss antes de -i) em vez de decodificar o vídeo 1080p inteiro quadro a quadro
    hw_in = ["-hwaccel", "videotoolbox"] if sys.platform == "darwin" else []
    ins, fil = [], []
    for idx_t, t in enumerate(tempos):
        t0_c = max(0.0, t - 0.10)
        ins += [*hw_in, "-ss", f"{t0_c:.3f}", "-t", "0.22", "-i", video]
        fil.append(f"[{idx_t}:v]fps={FPS},scale={larg}:-1,trim=end_frame=7,setpts=PTS-STARTPTS[v{idx_t}]")
    n_in = len(tempos)
    rows = max(1, -(-n_in * 7 // cols))
    concat_v = "".join(f"[v{i}]" for i in range(n_in)) + f"concat=n={n_in}:v=1:a=0,tile={cols}x{rows}[out]"
    sh(["ffmpeg", "-loglevel", "error", "-y", *ins, "-filter_complex", ";".join(fil + [concat_v]),
        "-map", "[out]", "-frames:v", "1", saida])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plano-editorial", help="JSON por produção: ações protegidas, ritmo e envelope musical")
    ap.add_argument("--idioma", choices=["en", "es"], default="en", help="idioma da fala e do alinhamento (Jordan: es)")
    ap.add_argument("pasta"); ap.add_argument("--producao"); ap.add_argument("--musica"); ap.add_argument("--sem-musica", action="store_true")
    ap.add_argument("--ramp", default="1", help="takes-herói (pausa acelerada 5x em vez de cortada)")
    ap.add_argument("--leaks", default=None, help="takes com efeito na entrada (padrão: FitWell nenhum; Auraly o 2, saída do gancho)")
    ap.add_argument("--estilo", choices=["fitwell", "auraly"], default=None, help="padrão: auraly se a produção for Auraly")
    ap.add_argument("--ritmo", type=float, default=None, help="palavras/s alvo (padrão: 3,8 FitWell, 4,0 Auraly)")
    ap.add_argument("--up", default="1", help="takes com legenda mais alta")
    # 1300 (Luigi, 2026-10-15): nas duas entregas Avery aprovadas a legenda foi descida à mão de 960 para 1300 (lábios livres)
    ap.add_argument("--legenda-topo", type=int, default=1300, help="topo da legenda Auraly em pixels; ajustar após conferir rosto")
    # Luigi, 2026-10-23 (HIDRA): legenda pequena e baixa em todos os takes, nunca sobre o herói do gancho nem rosto
    ap.add_argument("--legenda-tam", type=int, default=86, help="tamanho da fonte da legenda dinâmica (padrão 86)")
    ap.add_argument("--legenda-fixa", type=int, default=None, help="topo da legenda em px em TODOS os takes (ignora --up)")
    ap.add_argument("--legenda-gancho", type=int, default=None, help="com --legenda-fixa: topo da legenda nos takes de --up (gancho), longe do herói")
    ap.add_argument("--nome", default=None); ap.add_argument("--trabalho", default=None)
    ap.add_argument("--excecoes-fala", help="JSON de exceções explícitas por arquivo/hash/roteiro; sem alterar prompts")
    ap.add_argument("--nota-minima", type=float, default=0.85)
    ap.add_argument("--insert", type=float, default=INSERT, help="segundos de cada insert mudo, na ação (0 = inteiro)")
    # acabamento HyperFrames (Luigi, 2026-10-10: priorizar o que o repositório HyperFrames oferece), ver acabamento.py
    ap.add_argument("--sem-acabamento", action="store_true", help="sem palavra atrás do avatar, zoom e SFX")
    # "auto" = rodízio entre vídeos (acabamento.CARDAPIO): cada vídeo novo sai diferente do anterior
    ap.add_argument("--legenda", default="auto", help="auto, padrao (a aprovada) ou estilo do catálogo HyperFrames (caption-highlight...)")
    ap.add_argument("--sfx", default="auto", help="auto ou pacote de SFX HyperFrames: sutil, cinema, pop, brilho, glitch, nenhum")
    ap.add_argument("--picos", default=None, help="palavras de pico (padrão: automático)")
    ap.add_argument("--fonte-pico", default="auto", help="auto, anton, serifada ou montserrat")
    ap.add_argument("--sem-zoom", action="store_true"); ap.add_argument("--grao", action="store_true")
    a = ap.parse_args()
    globals()["PLANO_EDITORIAL"] = plano_editorial.carregar_plano(a.plano_editorial) if a.plano_editorial else None
    globals()["IDIOMA"] = a.idioma
    motor.IDIOMA = a.idioma
    globals()["INSERT"] = a.insert
    t0 = time.time(); rel = []
    excecoes = {}
    if a.excecoes_fala:
        registro = json.load(open(a.excecoes_fala, encoding="utf8"))
        if not registro.get("user_authorization"):
            sys.exit("Exceções sem autorização registrada")
        excecoes = {os.path.realpath(i["file"]): i for i in registro["items"]}
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
    motor.TRABALHO = tmp

    log(f"1/7 transcrevendo {len(arquivos)} takes")
    # E1 + E3: extrai 1 único WAV 16kHz mono por take e pré-calcula rms10 em paralelo antes da transcrição
    with cf.ThreadPoolExecutor(max_workers=min(4, max(1, len(arquivos)))) as ex_w:
        list(ex_w.map(motor.rms10, arquivos))
    w_arq = {f: palavras(f) for f in arquivos}
    d_arq = {f: " ".join(w for w, _, _ in w_arq[f]) for f in arquivos}
    falantes = {f: t for f, t in d_arq.items() if len(norm(t)) >= 2}
    if not falantes: sys.exit("Nenhum take com fala")

    log("2/7 achando o roteiro e a ordem dos takes pela fala")
    achado = achar_roteiro(falantes, a.producao)
    if not achado or achado[3] < a.nota_minima:
        # Se base.en ficou abaixo da nota mínima, re-transcreve com small.en
        w_arq = {f: palavras(f, usar_small=True) for f in arquivos}
        d_arq = {f: " ".join(w for w, _, _ in w_arq[f]) for f in arquivos}
        falantes = {f: t for f, t in d_arq.items() if len(norm(t)) >= 2}
        achado = achar_roteiro(falantes, a.producao) if falantes else None
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
    t_produto = takes_com_produto(pasta)
    produto = {i for i, f in takes if (int(pos[f] + 0.5) if f in pos else numero(f)) in t_produto}
    if produto:
        rel.append(f"- Produto em quadro nos takes {sorted(t_produto)}: legenda abaixo dele (topo {PRODUTO_TOPO} px)")

    log("3/7 conferindo a fala de cada take, palavra por palavra")
    erros_fala, aparados, avisos_escuta = [], [], []
    for k in sorted(falas):
        f = dict(takes)[k]
        probs, esc = conferir_fala(words[k], falas[k])
        probs, aceitos = aplicar_excecoes_fala(f, probs, falas[k], excecoes)
        if any(p.startswith(("faltou", "trocou")) for p in probs):
            # fallback rápido para small.en no take inteiro antes de fatiar por trechos
            w_sm = palavras(f, usar_small=True)
            probs_sm, esc_sm = conferir_fala(w_sm, falas[k])
            probs_sm, aceitos_sm = aplicar_excecoes_fala(f, probs_sm, falas[k], excecoes)
            if len(probs_sm) < len(probs):
                words[k], ditos[k], probs, esc, aceitos = w_sm, " ".join(w for w, _, _ in w_sm), probs_sm, esc_sm, aceitos_sm
        if any(p.startswith(("faltou", "trocou")) for p in probs):
            # segunda escuta, por trechos: palavra "faltando" pode ser só o whisper comendo a ponta do take
            w2 = palavras_por_trechos(f, tmp)
            probs2, esc2 = conferir_fala(w2, falas[k])
            probs2, aceitos2 = aplicar_excecoes_fala(f, probs2, falas[k], excecoes)
            if len(probs2) < len(probs):
                avisos_escuta.append(f"{k}. transcrição refeita por trechos (no take inteiro o whisper perdeu: "
                                     f"{'; '.join(p for p in probs if p not in probs2)})")
                words[k], ditos[k], probs, esc, aceitos = w2, " ".join(w for w, _, _ in w2), probs2, esc2, aceitos2
        if aceitos:
            rel.append(f"- Exceção autorizada por Luigi, take {k}: {'; '.join(aceitos)}; áudio original mantido, legenda do roteiro aprovado.")
        # Não cortar para tentar resolver palavra faltante ou substituída: o original deve ser auditado.
        # Quando probs == [] (fala 100% aprovada), só procura fala escondida no meio do take (so_interno=True);
        # qualquer ruído antes da 1ª ou depois da última palavra já sai automaticamente em motor.ilhas_v4.
        if not aceitos and not any(p.startswith(("faltou", "trocou")) for p in probs) and (probs or fala_sem_texto(f, words[k], tmp, so_interno=(not probs))):
            ap = limpar(f, words[k], falas[k], tmp, k)
            if ap:
                novo, tirados = ap
                fora = " / ".join(tirados)
                w2 = palavras(novo)
                probs2, esc2 = conferir_fala(w2, falas[k])
                probs2, _ = aplicar_excecoes_fala(f, probs2, falas[k], excecoes)
                if probs2:
                    w2_sm = palavras(novo, usar_small=True)
                    probs2_sm, esc2_sm = conferir_fala(w2_sm, falas[k])
                    probs2_sm, _ = aplicar_excecoes_fala(f, probs2_sm, falas[k], excecoes)
                    if len(probs2_sm) < len(probs2):
                        w2, probs2, esc2 = w2_sm, probs2_sm, esc2_sm
                if probs2 and all(p.startswith(("inventou", "repetiu")) for p in probs2):
                    ap2 = limpar(novo, w2, falas[k], tmp, k + 100)
                    if ap2:
                        novo2, tirados2 = ap2
                        w3 = palavras(novo2)
                        probs3, esc3 = conferir_fala(w3, falas[k])
                        probs3, _ = aplicar_excecoes_fala(f, probs3, falas[k], excecoes)
                        if probs3:
                            w3_sm = palavras(novo2, usar_small=True)
                            probs3_sm, esc3_sm = conferir_fala(w3_sm, falas[k])
                            probs3_sm, _ = aplicar_excecoes_fala(f, probs3_sm, falas[k], excecoes)
                            if len(probs3_sm) < len(probs3):
                                w3, probs3, esc3 = w3_sm, probs3_sm, esc3_sm
                        if not probs3:
                            novo, w2, probs2, esc2 = novo2, w3, probs3, esc3
                            fora = " / ".join(tirados + tirados2)
                if probs2:
                    if probs:
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
    if PLANO_EDITORIAL:
        plano_editorial.validar_contexto(PLANO_EDITORIAL, auraly, estilo)
        protegidos = {p["take"] for p in PLANO_EDITORIAL.get("protected_intervals", [])}
        if any(int(x.split(".", 1)[0]) in protegidos for x in aparados):
            sys.exit("Take aparado mudou os tempos fonte; revisar intervalos protegidos do plano")
        rel.append("- Plano editorial aplicado: " + json.dumps(PLANO_EDITORIAL, ensure_ascii=False))
    alvo = a.ritmo or (4.0 if estilo == "auraly" else 3.8)
    ramp = {int(x): 5 for x in a.ramp.split(",") if x}
    # sem light leak no FitWell (Luigi, 2026-10-10); no Auraly um flash só na saída do gancho
    leaks = [int(x) for x in a.leaks.split(",")] if a.leaks else ([2] if estilo == "auraly" and n >= 2 else [])
    up = [int(x) for x in a.up.split(",") if x]

    log("4/7 alinhando as palavras do roteiro, cortando e montando a base em paralelo")
    # Libera faster-whisper ANTES de carregar WhisperX/wav2vec2 (~650 MB), evitando pico duplo na RAM
    global _modelo, _modelo_small
    _modelo = None
    _modelo_small = None
    import gc
    gc.collect()
    src = dict(takes)
    alinhado = {k: motor.alinhar_forcado(src[k], falas[k], words[k]) for k in falas}
    # Libera imediatamente ~650 MB de RAM do modelo de alinhamento (wav2vec2) antes do ffmpeg/render
    motor._al = None
    gc.collect()
    sem_al = [k for k, v in alinhado.items() if not v]
    if sem_al:
        rel.append(f"  - aviso: takes sem alinhamento forçado (corte pelo método antigo): {sem_al}")
    # Pré-calcula rms10 de todos os takes em paralelo antes de segmentos()
    with cf.ThreadPoolExecutor(max_workers=min(4, max(1, len(src)))) as ex_r:
        list(ex_r.map(motor.rms10, src.values()))
    segs = segmentos(takes, words, ramp, alinhado)
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
    if PLANO_EDITORIAL:
        segs = plano_editorial.aplicar_ritmo(segs, PLANO_EDITORIAL)
        if any((s["b"] - s["a"]) / s["sp"] < 2 / FPS for s in segs):
            raise ValueError("Plano editorial criou trecho menor que dois frames; revisar limites da proteção")
    total = montar_base(segs, src, tmp)
    if PLANO_EDITORIAL:
        json.dump(PLANO_EDITORIAL, open(f"{tmp}/plano_editorial_aplicado.json", "w"), ensure_ascii=False, indent=2)
    json.dump(segs, open(f"{tmp}/segs.json", "w"), indent=1)

    log("5/7 legenda e música")
    def saida_de(k, t):
        cand = [x for x in segs if x["k"] == k and not x.get("mute")]
        for x in cand:
            if x["a"] - 0.08 <= t <= x["b"] + 0.08:
                return x["o"] + min(max(0.0, t - x["a"]), x["b"] - x["a"]) / x["sp"]
        prox = min(cand, key=lambda x: abs(x["a"] - t)) if cand else None
        return prox["o"] if prox else 0.0
    ws = []
    for k in sorted(falas):
        fonte = alinhado.get(k) or words[k]
        ws += [dict(w=w, t=saida_de(k, a2), k=k) for w, a2, _ in fonte]
    usa_rot = all(alinhado.get(k) for k in falas)
    inserts = {x["k"] for x in segs} - {x["k"] for x in segs if not x.get("mute")}
    eventos, duracoes = [], []
    banda_leg = None
    if estilo == "auraly":
        pages, cur = [], []
        for i, w in enumerate(ws):
            cur.append(w); nx = ws[i + 1] if i + 1 < len(ws) else None
            if (not nx or len(cur) >= 4 or re.search(r"[.!?]$", w["w"]) or (re.search(r",$", w["w"]) and len(cur) >= 2)
                    or nx["k"] != w["k"]):
                pages.append(cur); cur = []
        pages = juntar_curtas(pages)
        for n, p in enumerate(pages):
            st = p[0]["t"] if PLANO_EDITORIAL else (0 if n == 0 else p[0]["t"]); en = pages[n + 1][0]["t"] if n < len(pages) - 1 else total
            en = min([en] + [x["o"] for x in segs if x["k"] in inserts and x["o"] > st + 0.01])
            if PLANO_EDITORIAL:
                en = min([en] + [x["o"] for x in segs if x["k"] != p[0]["k"] and x["o"] > st + 0.01])
            big = palavra_chave(p, n)
            pos = motor.layout_auraly([re.sub(r"[.,!?;:]$", "", w["w"]).lower() for w in p], big, topo=a.legenda_topo)
            for j in range(len(p)):
                a2 = st if j == 0 else max(st, p[j]["t"] - 0.03)
                b2 = en if j == len(p) - 1 else max(a2, p[j + 1]["t"] - 0.03)
                png = f"{tmp}/leg_{n:03d}_{j}.png"
                motor.png_auraly(pos, j + 1, png)
                eventos.append((a2, b2, png))
            duracoes.append(en - st)
    else:
        pages, cur = [], []
        for i, w in enumerate(ws):
            cur.append(w); nx = ws[i + 1] if i + 1 < len(ws) else None
            if (not nx or len(cur) >= (PLANO_EDITORIAL.get("captions", {}).get("max_words", 3) if PLANO_EDITORIAL else 3) or re.search(r"[.!?]$", w["w"]) or (re.search(r",$", w["w"]) and len(cur) >= 2)
                    or nx["k"] != w["k"]):
                pages.append(cur); cur = []
        pages = juntar_curtas(pages)
        pos_legenda = PLANO_EDITORIAL.get("captions", {}) if PLANO_EDITORIAL else {}
        topos_pag = []
        for p in pages:
            topo_leg = pos_legenda.get("hero_top", 760) if p[0]["k"] in up else pos_legenda.get("top", 880)
            if p[0]["k"] in produto:
                topo_leg = PRODUTO_TOPO
            if a.legenda_fixa:
                fixa = a.legenda_gancho if (a.legenda_gancho and p[0]["k"] in up) else a.legenda_fixa
                topo_leg = max(topo_leg, fixa) if p[0]["k"] in produto else fixa
            topos_pag.append(topo_leg)
        if topos_pag:
            y0_leg = max(0, (min(topos_pag) - 50) // 2 * 2)
            y1_leg = min(H, (max(topos_pag) + 290 + 1) // 2 * 2)
            banda_leg = (y0_leg, max(2, y1_leg - y0_leg))
        tarefas_png = []
        for n, (p, topo_leg) in enumerate(zip(pages, topos_pag)):
            st = p[0]["t"] if PLANO_EDITORIAL else (0 if n == 0 else p[0]["t"]); en = pages[n + 1][0]["t"] if n < len(pages) - 1 else total
            en = min([en] + [x["o"] for x in segs if x["k"] in inserts and x["o"] > st + 0.01])
            if PLANO_EDITORIAL:
                en = min([en] + [x["o"] for x in segs if x["k"] != p[0]["k"] and x["o"] > st + 0.01])
            txt = " ".join(re.sub(r"[.,!?]$", "", w["w"]) for w in p).lower()
            png = f"{tmp}/leg_{n:03d}.png"
            if LEGENDA_DINAMICA:  # palavra falada em amarelo, troca no tempo da fala
                pal = [re.sub(r"[.,!?;:]$", "", w["w"]) for w in p]
                for j in range(len(p)):
                    a2 = st if j == 0 else max(st, p[j]["t"] - 0.03)
                    b2 = en if j == len(p) - 1 else max(a2, p[j + 1]["t"] - 0.03)
                    pj = f"{tmp}/leg_{n:03d}_{j}.png"
                    tarefas_png.append((True, pal, j, topo_leg, pj, a.legenda_tam, banda_leg))
                    eventos.append((a2, b2, pj))
            else:
                tarefas_png.append((False, txt, 0, topo_leg, png, a.legenda_tam, banda_leg))
                eventos.append((st, en, png))
            duracoes.append(en - st)
        if tarefas_png:
            def _gerar_png(t_arg):
                din, tx_p, j_i, tp_l, cam_p, tm_l, bd_l = t_arg
                if din:
                    motor.png_dinamica(tx_p, j_i, tp_l, cam_p, tam=tm_l, banda=bd_l)
                else:
                    motor.png_fitwell(tx_p, tp_l, cam_p, banda=bd_l)
            with cf.ThreadPoolExecutor(max_workers=4) as ex_png:
                list(ex_png.map(_gerar_png, tarefas_png))
    npag = len(pages)
    lista_leg = motor.faixa_legendas(eventos, total, tmp, banda=banda_leg)
    flashes = [max(0, x["o"] - 0.12) for i, x in enumerate(segs) if i > 0 and segs[i - 1]["k"] != x["k"] and x["k"] in leaks]
    selos = None
    if estilo == "auraly":
        selos = f"{tmp}/selos.png"; motor.png_selos(selos)
    musica = None if a.sem_musica else escolher_musica(a.musica, os.path.basename(pasta))
    ini = mixar(f"{tmp}/voz.wav", musica, total, f"{tmp}/assets/mix.wav")

    json.dump(ws, open(f"{tmp}/palavras_saida.json", "w"))  # para rodar acabamento.py sozinho depois
    base_final, mix_final, camadas = f"{tmp}/assets/base.mp4", f"{tmp}/assets/mix.wav", []
    if not a.sem_acabamento:
        log("5b/7 acabamento HyperFrames (palavra atrás do avatar, zoom de pico, SFX)")
        import acabamento
        var = acabamento.variacao(f"{os.path.basename(pasta)}/{nome}")
        # Luigi, 2026-10-13 (velocidade): legenda padrão (Pillow, sem render HyperFrames) no lugar do rodízio
        a.legenda = "padrao" if a.legenda == "auto" else a.legenda
        a.sfx = "nenhum" if a.sfx == "auto" else a.sfx  # Luigi, 2026-10-13: só música de fundo
        a.fonte_pico = var["fonte_pico"] if a.fonte_pico == "auto" else a.fonte_pico
        rel.append(f"- Variação deste vídeo (rodízio): legenda {a.legenda} · SFX {a.sfx} · fonte do pico {a.fonte_pico}")
        forc = [re.sub(r"[^a-z0-9']", "", x.lower()) for x in a.picos.split(",")] if a.picos else None
        base_final, frente, mix_final, rel_ac = acabamento.aplicar(
            tmp, ws, segs, total, estilo, flashes, forc, not a.sem_zoom, a.grao, a.sfx, a.fonte_pico, log)
        rel += rel_ac
        if frente:
            camadas.append((frente, 0))
            flashes = []  # o flash do catálogo (editorial-flash-overlay) substitui o do ffmpeg
        if a.legenda != "padrao" and produto:
            # a camada do catálogo tem uma altura só para o vídeo inteiro: cobriria o produto
            rel.append(f"- Legenda {a.legenda} trocada pela padrão: o catálogo não desce abaixo do produto por take")
            a.legenda = "padrao"
        if a.legenda != "padrao":
            import legendas_hf
            picos = json.load(open(f"{tmp}/picos.json"))
            idx = [i for i, w in enumerate(ws) for p in picos if abs(w["t"] - p["t"]) < 0.01]
            camadas.append(legendas_hf.camada(a.legenda, ws, total, tmp, idx, log, centro=a.legenda_topo + 160))
            lista_leg = None
            rel.append(f"- Legenda do catálogo HyperFrames: {a.legenda}")

    log("6/7 render final (1080x1920, um passe)")
    saida = f"{tmp}/{nome}_editado.mp4"
    motor.render_final(base_final, lista_leg, mix_final, total, saida, flashes, selos, camadas,
                       leg_y=banda_leg[0] if banda_leg else 0)
    heard = ws

    log("7/7 conferências")
    cortes = [s["o"] for s in segs[1:]]
    mb = os.path.getsize(saida) / 1e6
    hw_in = ["-hwaccel", "videotoolbox"] if sys.platform == "darwin" else []
    with cf.ThreadPoolExecutor(max_workers=4) as ex_sh:
        f_fa = ex_sh.submit(fantasmas, f"{tmp}/assets/base.mp4", [round(c * FPS) for c in cortes], segs, src)
        f_si = ex_sh.submit(silencios, f"{tmp}/voz.wav")
        f_c = ex_sh.submit(sheet, f"{tmp}/assets/base.mp4", cortes, f"{tmp}/cortes.png")
        f_l = ex_sh.submit(sh, ["ffmpeg", "-loglevel", "error", *hw_in, "-skip_frame", "nokey", "-threads", "2", "-y", "-i", saida,
                                "-vf", "fps=0.7,scale=216:-1,tile=6x3", "-frames:v", "1", f"{tmp}/legendas.png"])
        fant = f_fa.result()
        sil_bruto = f_si.result()
        f_c.result(); f_l.result()
    sil = [x for x in sil_bruto if not any(s.get("mute") and s["o"] - 0.2 <= x[0] <= s["o"] + s["d"] for s in segs)]
    if PLANO_EDITORIAL:
        janelas = plano_editorial.protected_output_windows(segs, PLANO_EDITORIAL)
        # Só liberar silêncio totalmente contido na proteção; overlap parcial não basta.
        sil = plano_editorial.silencios_nao_autorizados(sil_bruto, segs, PLANO_EDITORIAL, tolerance=1 / FPS)
        rel.append(f"- Ações/pausas protegidas na saída (s): {janelas}; demais silêncios continuam bloqueantes")
    ok = {
        "Sem silêncio fora da rampa/proteção editorial" if PLANO_EDITORIAL else "Sem silêncio fora da rampa": not sil,
        "Sem quadro fantasma nos cortes": not fant,
        "Legenda com o texto do roteiro (contagem bateu)": usa_rot,
        "Nenhuma legenda com menos de 0,1s": min(duracoes or [1]) >= 0.1,
        "Vídeo em 1080x1920": sh(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                  "stream=width,height", "-of", "csv=p=0", saida]).strip() == "1080,1920",
        "Arquivo até 100 MB": mb <= 100,
    }
    rel += [f"- {k}: {'OK' if v else 'FALHA'}" for k, v in ok.items()]
    if sil: rel.append(f"  - silêncios: {sil}")
    if fant: rel.append(f"  - quadro fantasma em: {fant}s")
    rel += [f"- Duração {total:.1f}s · {len(heard) / total:.2f} palavras/s · {len(segs)} trechos ({sum(1 for s in segs if s.get('mute'))} rampas) · {npag} legendas",
            f"- Música: {os.path.basename(musica) + f' (a partir de {ini:.1f}s, cama base {MUSICA_DB} dB)' if musica else 'sem música'}" + ("; envelope editorial registrado acima" if PLANO_EDITORIAL and musica and "music" in PLANO_EDITORIAL else ""),
            f"- Estilo {estilo} · fala a {sp:.2f}x (alvo {alvo} palavras/s) · {'flash' if estilo == 'auraly' else 'light leak'} na entrada dos takes {leaks or 'nenhum'}; rampa nos takes {sorted(ramp)}" + (f"; legenda alta nos takes {up}" if estilo != "auraly" else "; selos 777/222"),
            f"- Arquivo: `{saida}` ({mb:.1f} MB) · tempo total {time.time() - t0:.0f}s",
            "- Olhar antes de entregar: `cortes.png` (pulo) e `legendas.png` (nada sobre rosto ou herói)"]
    open(f"{tmp}/RELATORIO.md", "w").write(f"# Relatório de edição · {nome}\n\n" + "\n".join(rel) + "\n")
    print("\n".join(rel))
    sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
