"""Ficha do frame e placar de cada K (Luigi, 2026-09-25, todos os angulos).

Existe porque o K01 de `fitywell_growth_modelo_intestino` passou no linter com 0 falha e saiu outro
gancho: a forma do heroi estava generica, a camera longe e havia props inventados. O prompt tinha as
palavras certas ("very close to the lens"), mas nao tinha a MEDIDA do frame do modelo. Regra e fonte:
`GATE_VISUAL.md` Parte 6.

O que esta verificacao garante, lendo so do disco:
- toda producao nova tem `FICHA_FRAMES.md`, com uma secao por K e o frame do modelo que a sustenta;
- os termos de forma do heroi escritos na ficha aparecem literalmente no K;
- o placar F1-F6 (fidelidade ao frame) e G1-G8 (gate anti cara de IA) esta completo, e cada OK traz
  a evidencia entre aspas, que tem que existir literalmente no texto do K, em todos os avatares;
- a composicao do K tem medida (quanto do quadro e a que distancia da lente), nunca so adjetivo;
- a camera do K diz a lente e a altura.

O que NAO garante: que a ficha descreve o frame corretamente, e que a imagem gerada saiu igual. Isso
e leitura humana: o frame fica anexado na ficha, e o K do gancho e conferido contra o resultado real.

Producoes anteriores a regra estao em `controle/ficha_legado.json` e nao sao cobradas.
"""
import json
import os
import re
import unicodedata

LEGADO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "controle", "ficha_legado.json")

ITENS = {
    "F1": "forma do heroi",
    "F2": "quanto do quadro",
    "F3": "distancia da lente",
    "F4": "camera",
    "F5": "pose do avatar",
    "F6": "lista fechada",
    "G1": "luz neutra",
    "G2": "ceu ou janela",
    "G3": "foco",
    "G4": "realismo",
    "G5": "sem tom quente",
    "G6": "sem texto",
    "G7": "bandeira",
    "G8": "boca no K de fala",
}
# Itens que nunca podem ser N/A: sem eles o K nao tem heroi medido nem acabamento do gate.
SEM_NA = {"F1", "F2", "F3", "F4", "G1", "G3", "G4", "G5", "G6"}

RE_SECAO = re.compile(r"^##\s+(K\d+[A-Z]?)\b", re.M)
RE_ASPAS = re.compile(r'"([^"]+)"')
RE_LINHA_ITEM = re.compile(r"^\|\s*([FG]\d)\b[^|]*\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|\s*$", re.M)

RE_QUADRO = re.compile(
    r"\b\d{1,3}\s*(%|percent)|\b(ten|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)\s+percent"
    r"|\b(half|a third|two thirds|a quarter|three quarters) of the frame|edge to edge|fills? the (whole )?frame",
    re.I)
RE_DISTANCIA = re.compile(
    r"\b(\d+|a few|few|one|two|three|four|five|six)\s+(inch(es)?|centimet\w+|cm)\b|touching the lens", re.I)
RE_LENTE = re.compile(r"\b(0\.5x|1x|2x|ultra-?wide|wide(-angle)?|lens)\b", re.I)
RE_ALTURA = re.compile(r"\b(counter|table|chest|eye|floor|ground|waist|knee|shoulder|overhead|top-down|"
                       r"straight above|above|below|rim|low|high|desk|island)\b", re.I)


def _norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = s.replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", s).strip()


def legado():
    try:
        with open(LEGADO_PATH, encoding="utf-8") as f:
            return set(json.load(f).get("producoes", []))
    except (OSError, ValueError):
        return set()


def parse_ficha(texto):
    """{K: {"frame": str, "termos": [..], "placar": {item: (status, evidencias, bruto)}, "linha": n}}"""
    out = {}
    ms = list(RE_SECAO.finditer(texto))
    for i, m in enumerate(ms):
        fim = ms[i + 1].start() if i + 1 < len(ms) else len(texto)
        corpo = texto[m.start():fim]
        frame = re.search(r"^Frame:\s*`?([^`\n]+?)`?\s*$", corpo, re.M)
        termos = re.search(r"^Termos de forma:\s*(.+)$", corpo, re.M)
        placar = {}
        for it in RE_LINHA_ITEM.finditer(corpo):
            status = it.group(2).strip().upper().replace(" ", "")
            placar[it.group(1)] = (status, RE_ASPAS.findall(it.group(3)), it.group(3).strip())
        out[m.group(1)] = {
            "frame": frame.group(1).strip() if frame else None,
            "termos": RE_ASPAS.findall(termos.group(1)) if termos else [],
            "placar": placar,
            "linha": texto.count("\n", 0, m.start()) + 1,
        }
    return out


def _campo(k_texto, nome):
    """Valor de um campo do JSON do K (composition, camera...). Aceita o K como JSON ou texto."""
    try:
        d = json.loads(k_texto)
        return str(d.get(nome, ""))
    except (ValueError, TypeError):
        m = re.search(r'"%s"\s*:\s*"((?:[^"\\]|\\.)*)"' % nome, k_texto or "")
        return m.group(1) if m else ""


def validar_ficha(pasta, ks_por_arquivo):
    """ks_por_arquivo: {nome_do_arquivo: {K: texto_do_K}}. Devolve [(nivel, check, msg, loc)]."""
    issues = []
    add = lambda nivel, msg, loc="FICHA_FRAMES.md": issues.append((nivel, "ficha-frame", msg, loc))
    nome = os.path.basename(os.path.normpath(pasta))
    if nome in legado():
        return [("OK", "ficha-frame", "producao anterior a regra da ficha (controle/ficha_legado.json)", None)]
    todos_k = sorted({k for ks in ks_por_arquivo.values() for k in ks if k.startswith("K")})
    if not todos_k:
        return issues
    caminho = os.path.join(pasta, "FICHA_FRAMES.md")
    if not os.path.exists(caminho):
        add("FALHA", "FICHA_FRAMES.md nao existe. Todo K parte da ficha do frame do modelo, com o placar "
                     "F1-F6 e G1-G8 e a evidencia citada (GATE_VISUAL.md Parte 6)")
        return issues
    with open(caminho, encoding="utf-8") as f:
        ficha = parse_ficha(f.read())
    ruim = False
    for k in todos_k:
        sec = ficha.get(k)
        loc = "FICHA_FRAMES.md:%d" % sec["linha"] if sec else "FICHA_FRAMES.md"
        if not sec:
            add("FALHA", "%s nao tem secao na ficha do frame" % k)
            ruim = True
            continue
        if not sec["frame"] or not os.path.exists(os.path.join(pasta, sec["frame"])):
            add("FALHA", "%s: linha 'Frame:' ausente ou o arquivo do frame do modelo nao existe (%s)"
                % (k, sec["frame"]), loc)
            ruim = True
        if not sec["termos"]:
            add("FALHA", "%s: 'Termos de forma:' sem nenhum termo entre aspas. A forma do heroi vem do frame, "
                         "nunca de vocabulario generico" % k, loc)
            ruim = True
        for item in ITENS:
            if item not in sec["placar"]:
                add("FALHA", "%s: placar sem o item %s (%s)" % (k, item, ITENS[item]), loc)
                ruim = True
                continue
            status, evid, bruto = sec["placar"][item]
            if status in ("N/A", "NA"):
                if item in SEM_NA:
                    add("FALHA", "%s: %s (%s) nao pode ser N/A" % (k, item, ITENS[item]), loc)
                    ruim = True
                elif not bruto.strip():
                    add("FALHA", "%s: %s marcado N/A sem motivo" % (k, item), loc)
                    ruim = True
                continue
            if status != "OK":
                add("FALHA", "%s: %s (%s) esta '%s'. Item reprovado nao sai" % (k, item, ITENS[item], status), loc)
                ruim = True
                continue
            if not evid:
                add("FALHA", "%s: %s marcado OK sem evidencia entre aspas" % (k, item), loc)
                ruim = True
        # evidencia e termos de forma existem LITERALMENTE no K de cada arquivo (cada avatar)
        for arq, ks in ks_por_arquivo.items():
            texto = ks.get(k)
            if texto is None:
                continue
            alvo = _norm(texto)
            for termo in sec["termos"]:
                if _norm(termo) not in alvo:
                    add("FALHA", "%s em %s nao usa o termo de forma da ficha \"%s\"" % (k, arq, termo), loc)
                    ruim = True
            for item, (status, evid, _) in sec["placar"].items():
                if status != "OK":
                    continue
                for e in evid:
                    if _norm(e) not in alvo:
                        add("FALHA", "%s em %s: a evidencia do %s \"%s\" nao esta no prompt. Placar sem a "
                                     "frase no K e autodeclaracao" % (k, arq, item, e), loc)
                        ruim = True
            comp = _campo(texto, "composition")
            cam = _campo(texto, "camera")
            if not RE_QUADRO.search(comp):
                add("FALHA", "%s em %s: a composicao nao diz QUANTO do quadro o heroi ocupa (porcentagem, "
                             "metade, edge to edge). Adjetivo nao e medida" % (k, arq), loc)
                ruim = True
            if not (RE_DISTANCIA.search(comp) or RE_DISTANCIA.search(cam)):
                add("FALHA", "%s em %s: sem a distancia do heroi ate a lente (inches, centimeters, touching "
                             "the lens)" % (k, arq), loc)
                ruim = True
            if not (RE_LENTE.search(cam) and RE_ALTURA.search(cam)):
                add("FALHA", "%s em %s: a camera tem que dizer a lente e a altura (ex.: 'ultra-wide 0.5x "
                             "lens', 'at counter level')" % (k, arq), loc)
                ruim = True
    extras = sorted(set(ficha) - set(todos_k))
    if extras:
        add("AVISO", "a ficha tem secoes sem K correspondente: %s" % ", ".join(extras))
    if not ruim:
        issues.append(("OK", "ficha-frame", "%d K com ficha, placar 14/14 e evidencia no prompt em %d arquivo(s)"
                       % (len(todos_k), len(ks_por_arquivo)), None))
    return issues
