"""Roda o editar.py numa pasta e resolve sozinho os takes reprovados (Luigi, 2026-10-14: "resolva tudo, não me peça
mais auxílio"). Para cada take reprovado, escuta de novo com o whisper medium.en no take inteiro e em trechos:
  1. todas as palavras do roteiro ouvidas e nada inventado -> exceção de escuta (arquivo + sha256);
  2. o Flow inventou/repetiu fala em volta da fala certa -> corta o take no trecho da fala do roteiro
     (original em _originais/) e reedita;
  3. o take cortou a ponta da frase -> a fala termina na última vírgula/ponto antes do que faltou (critério da
     opção 1 do Luigi, 2026-10-14), via OVR em textos.py, e regenera roteiro e pacote;
  4. o resto -> registra em reais_<prod>.txt e sai com 3 (o orquestrador anota e segue a fila).
Nunca encurta fala que perderia marca ou CTA (Natural Rems, Amazon, yes, follow)."""
import sys, os, re, json, glob, hashlib, subprocess, tempfile, difflib, shutil
REPO = "/Users/macbookairm2/agente bala non-shop/agente-bala-non-shop"
LOTE = f"{REPO}/producao/seamoss_receitas_lote_2026_10_13"
S = os.path.dirname(os.path.abspath(__file__))
pasta, prod = sys.argv[1:3]
AV, VID = prod.split("_seamoss_")
EXC = f"{S}/exc_{prod}.json"
NUM = {"16": "sixteen", "350": "three fifty", "30": "thirty", "3": "three", "2": "two", "1": "one", "6": "six",
       "4": "four", "50": "fifty", "wanna": "want to", "gonna": "going to", "dandelions": "dandelion", "80s": "eighties", "70s": "seventies", "90s": "nineties", "40": "forty", "20": "twenty", "10": "ten", "5": "five", "100": "hundred", "6000": "six thousand"}
CRITICAS = ["natural", "rems", "amazon", "yes", "follow", "stories"]
_medium = None


def log(*a):
    print(*a, flush=True)


def norm(t):
    t = t.lower().replace("&", " and ").replace("d 3", "d3").replace("d-3", "d3").replace("’", "'")
    out = []
    for w in re.findall(r"[a-z0-9']+", t):
        out += NUM.get(w, w).split()
    return out


def modelo():
    global _medium
    if _medium is None:
        from faster_whisper import WhisperModel
        _medium = WhisperModel("medium.en", device="cpu", compute_type="int8", cpu_threads=8)
    return _medium


def palavras(f, ini=0.0):
    t = tempfile.mktemp(suffix=".wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(ini), "-i", f, "-ac", "1", "-ar", "16000", t])
    segs, _ = modelo().transcribe(t, language="en", vad_filter=False, word_timestamps=True,
                                  initial_prompt="Natural Rems Sea Moss.")
    ws = [(w.word.strip(), w.start + ini, w.end + ini) for s in segs for w in s.words]
    os.remove(t)
    return ws


def escuta(f):
    """Palavras do take inteiro + união das palavras ouvidas em trechos (o whisper come as pontas do take)."""
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                               capture_output=True, text=True).stdout or 8)
    inteiro = palavras(f)
    uniao = set(w for x in inteiro for w in norm(x[0]))
    for ini in (1.5, 3.0, 4.5, 6.0):
        if ini < dur - 0.8:
            uniao |= set(w for x in palavras(f, ini) for w in norm(x[0]))
    return inteiro, uniao


def takes_do_video():
    g = {}
    exec(open(f"{LOTE}/textos.py", encoding="utf8").read(), g)
    out = []
    for i, (beat, setup, curta, en, pt) in enumerate(g["VID"][VID], 1):
        if "AUTORIDADE" in beat:
            en, pt = g["AUT"][VID][AV]
        en, pt = g.get("OVR", {}).get((VID, AV, i), (en, pt))
        out.append((i, en, pt))
    return out


def grava_ovr(n, en, pt):
    p = f"{LOTE}/textos.py"
    s = open(p, encoding="utf8").read()
    s = s.replace("OVR = {\n", "OVR = {\n (%r, %r, %d): (%r,\n   %r),\n" % (VID, AV, n, en, pt), 1)
    open(p, "w", encoding="utf8").write(s)
    for g in ("gerar_roteiros.py", "gerar_pacotes.py"):
        subprocess.run([f"{REPO}/.venv-operacao/bin/python", f"{LOTE}/{g}"], capture_output=True, cwd=REPO)


def encurta(rot, ouvidas):
    """Fala que termina na última vírgula/ponto antes da primeira palavra não ouvida, se o que falta é só a ponta."""
    toks = norm(rot)
    falta_idx = [i for i, w in enumerate(toks) if w not in ouvidas]
    if not falta_idx or any(w not in ouvidas for w in toks[:falta_idx[0]]):
        return None
    pos, achadas = 0, 0
    for m in re.finditer(r"[A-Za-z0-9']+", rot):
        achadas += len(norm(m.group(0)))
        if achadas > falta_idx[0]:
            pos = m.start()
            break
    corte = max(rot.rfind(",", 0, pos), rot.rfind(".", 0, pos))
    # cortar na vírgula só se ela estiver perto (no máximo 3 palavras ouvidas jogadas fora); senão, a fala
    # termina na última palavra ouvida ("takes an hour you don't have" -> "takes an hour.", nunca "Dicing.")
    if corte <= 0 or len(norm(rot[corte:pos])) > 3:
        fraca = ("and", "or", "but", "so", "the", "a", "to", "of", "with", "one", "than", "less", "more", "your", "my", "in")
        fim = len(rot[:pos].rstrip(" ,;"))
        if norm(rot[:fim])[-1:] and norm(rot[:fim])[-1] in fraca:
            if corte <= 0:
                return None  # sem vírgula antes e terminaria em palavra solta: deixa sem solução
        else:
            corte = fim
    novo = rot[:corte].rstrip(" ,;") + "."
    perdidas = set(norm(rot)) - set(norm(novo))
    if len(norm(novo)) < 5 or any(c in perdidas for c in CRITICAS):
        return None
    return novo


def encurta_inicio(rot, ouvidas):
    """Fala sem as 1-2 palavras iniciais que o take não tem (ex.: "and they honestly..." -> "They honestly...")."""
    toks = norm(rot)
    falta_idx = [i for i, w in enumerate(toks) if w not in ouvidas]
    if not falta_idx or max(falta_idx) > 1 or falta_idx != list(range(len(falta_idx))):
        return None
    if any(toks[i] in CRITICAS for i in falta_idx):
        return None
    palavras_rot = rot.split()
    novo = " ".join(palavras_rot[len(falta_idx):]).lstrip(",; ")
    return novo[:1].upper() + novo[1:] if novo else None


def corta_take(f, inteiro, rot):
    """Corta o take no trecho em que está a fala do roteiro; original em _originais/."""
    ws = [(norm(w)[0] if norm(w) else "", a, b) for w, a, b in inteiro]
    alvo = norm(rot)
    sm = difflib.SequenceMatcher(None, [w for w, _, _ in ws], alvo, autojunk=False)
    blocos = [b for b in sm.get_matching_blocks() if b.size]
    if not blocos or sum(b.size for b in blocos) < 0.8 * len(alvo):
        return False
    ini = ws[blocos[0].a][1]
    fim = ws[blocos[-1].a + blocos[-1].size - 1][2]
    orig_dir = os.path.join(os.path.dirname(f), "_originais")
    os.makedirs(orig_dir, exist_ok=True)
    orig = os.path.join(orig_dir, os.path.basename(f))
    if not os.path.exists(orig):
        shutil.move(f, orig)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", orig, "-ss", f"{max(0, ini - 0.08):.2f}", "-to", f"{fim + 0.18:.2f}",
                    "-c:v", "libx264", "-crf", "16", "-preset", "fast", "-c:a", "aac", "-b:a", "192k", f], check=True)
    log(f"   cortado {os.path.basename(f)} em {ini - 0.08:.2f}-{fim + 0.18:.2f}s (original em _originais/)")
    return True


def roda():
    ex = ["--excecoes-fala", EXC] if os.path.exists(EXC) else []
    r = subprocess.run([f"{REPO}/.venv-operacao/bin/python", f"{REPO}/.claude/skills/edicao/template/editar.py",
                        os.path.expanduser(f"~/Desktop/{pasta}"), "--producao", prod] + ex, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def materializa():
    """Desktop no iCloud com disco cheio: takes ficam 'dataless' e a leitura falha no meio da edição.
    Baixa todos e confere que cada um abre antes de editar."""
    import time
    pasta_abs = os.path.expanduser(f"~/Desktop/{pasta}")
    for f in sorted(glob.glob(f"{pasta_abs}/*.mp4")):
        for tentativa in range(6):
            subprocess.run(["brctl", "download", f], capture_output=True)
            subprocess.run(["cat", f], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            r = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-f", "null", "-"], capture_output=True, text=True)
            if r.returncode == 0 and not r.stderr.strip():
                break
            time.sleep(5)
        else:
            log(f"   AVISO: {os.path.basename(f)} não abriu depois de 6 tentativas")


materializa()
cortados = set()
for it in range(7):
    code, out = roda()
    log(f"[{pasta}] rodada {it + 1}: exit {code} | " + (out.strip().splitlines()[-1] if out.strip() else ""))
    if code == 0:
        sys.exit(0)
    if "fala diferente" not in out and ("CalledProcessError" in out or "Errno" in out):
        log(f"[{pasta}] erro de leitura de arquivo; baixando de novo do iCloud e repetindo")
        materializa()
        continue
    if "fala diferente" not in out:
        rels = sorted(glob.glob(f"/tmp/edicao/{pasta}-*/RELATORIO.md"), key=os.path.getmtime)
        if rels and "palavra por palavra: OK" in open(rels[-1], encoding="utf8").read() and glob.glob(os.path.dirname(rels[-1]) + "/*_editado.mp4"):
            log(f"[{pasta}] fala OK; conferências de acabamento com ressalva vão para o status")
            sys.exit(0)
        log(out[-2500:])
        sys.exit(1)
    rel = sorted(glob.glob(f"/tmp/edicao/{pasta}-*/RELATORIO.md"), key=os.path.getmtime)[-1]
    exc = json.load(open(EXC)) if os.path.exists(EXC) else {"items": []}
    exc["user_authorization"] = ("Luigi, 2026-10-14: 'resolva tudo isso e não me peça mais auxílio'; exceção só para erro "
                                 "de escuta do whisper small conferido com o medium.en no take inteiro e em trechos")
    reais, mexeu = [], False
    takes = takes_do_video()
    for line in open(rel, encoding="utf8"):
        m = re.match(r"\s+- \d+\. (.+?\.mp4): (.+?) \| ouvi .*\| roteiro \"(.*)\"\s*$", line)
        if not m:
            continue
        arq, probs, rot = m.groups()
        f = os.path.expanduser(f"~/Desktop/{pasta}/{arq}")
        inteiro, ouvidas = escuta(f)
        falta = [w for w in norm(rot) if w not in ouvidas]
        log(f"   {arq}: {probs} | medium: {' '.join(w for w, _, _ in inteiro)!r} | faltam {falta}")
        n = next((i for i, en, pt in takes if en == rot), None)
        if re.search(r"inventou|repetiu", probs) and not falta and f not in cortados:
            if corta_take(f, inteiro, rot):
                cortados.add(f); mexeu = True
                exc["items"] = [x for x in exc["items"] if x["file"] != f]
                continue
        if not falta:
            if re.search(r"inventou|repetiu", probs):
                reais.append(f"{arq}: fala inventada/repetida que não deu para cortar ({probs})")
                continue
            h = hashlib.sha256(open(f, "rb").read()).hexdigest()
            exc["items"] = [x for x in exc["items"] if x["file"] != f] + [
                {"file": f, "sha256": h, "approved_script": rot, "allowed_problems": [p.strip() for p in probs.split("; ")]}]
            mexeu = True
            continue
        novo = (encurta(rot, ouvidas) or encurta_inicio(rot, ouvidas)) if n else None
        if novo:
            pt = next(p for i, e, p in takes if i == n)
            grava_ovr(n, novo, pt + " [fala ajustada ao take gerado]")
            log(f"   T{n}: fala ajustada ao take: {novo!r}")
            mexeu = True
            continue
        reais.append(f"{arq} (T{n}): faltam {falta} | medium: {' '.join(w for w, _, _ in inteiro)!r} | roteiro: {rot!r}")
    json.dump(exc, open(EXC, "w"), indent=1)
    if reais:
        open(f"{S}/reais_{prod}.txt", "w").write("\n".join(reais) + "\n")
        log("SEM SOLUÇÃO AUTOMÁTICA:\n  " + "\n  ".join(reais))
        sys.exit(3)
    if not mexeu:
        log(out[-2500:])
        sys.exit(1)
sys.exit(1)
