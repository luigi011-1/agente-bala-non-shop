# -*- coding: utf-8 -*-
"""
checar_entrega.py - Gate mecanico da entrega de producao.

Le os arquivos de producao/<avatar>_<slug>/ DO DISCO e checa as regras do CLAUDE.md
que podem ser verificadas por maquina. Nao depende de nada estar carregado em contexto.

Uso:
    python checar_entrega.py producao/kendra_selos
    python checar_entrega.py --todos

Existe porque regra lembrada e regra esquecida. Criado em 2026-08-26.
"""
from __future__ import annotations
import sys, os, re, json, io, glob

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FALHAS, AVISOS, OKS = [], [], []


def falha(check, msg, loc=""):
    FALHAS.append((check, msg, loc))


def aviso(check, msg, loc=""):
    AVISOS.append((check, msg, loc))


def ok(check, msg=""):
    OKS.append((check, msg))


def ler(path):
    if not os.path.exists(path):
        return None
    return io.open(path, encoding="utf-8").read()


def linha_de(texto, idx):
    return texto.count("\n", 0, idx) + 1


# ---------------------------------------------------------------- normalizacao
ASPAS = dict.fromkeys(map(ord, "“”„″"), '"')
APOST = dict.fromkeys(map(ord, "‘’ʼ"), "'")


def norm_fala(s):
    s = s.translate(ASPAS).translate(APOST)
    s = re.sub(r"\s+", " ", s).strip().strip('"').strip()
    return s


def palavras(s):
    return [w for w in re.split(r"\s+", norm_fala(s)) if re.search(r"[A-Za-z0-9]", w)]


# ---------------------------------------------------------------- parsers
RE_TAKE = re.compile(r"^###\s+(T\d+)\s*[·|]\s*(.*)$", re.M)
# Aceita rotulo de locutor nos videos de dialogo: > MULHER: "..." / > HOMEM IDOSO: "..."
RE_FALA_ROT = re.compile(r'^>\s*(?:[A-ZÀ-Ú][A-ZÀ-Ú0-9 ª\.]{1,24}:\s*)?"(.+?)"\s*$', re.M | re.S)


def parse_takes(roteiro):
    """Retorna a lista de takes na ordem do arquivo."""
    out = []
    ms = list(RE_TAKE.finditer(roteiro))
    for i, m in enumerate(ms):
        fim = ms[i + 1].start() if i + 1 < len(ms) else len(roteiro)
        corpo = roteiro[m.start():fim]
        head = m.group(2)
        mudo = bool(re.search(r"B-ROLL|MUDO|SEM FALA", head, re.I))
        fm = RE_FALA_ROT.search(corpo)
        out.append({
            "id": m.group(1),
            "head": head.strip(),
            "fala": norm_fala(fm.group(1)) if fm else None,
            "mudo": mudo,
            "linha": linha_de(roteiro, m.start()),
        })
    return out


RE_BLOCO_JSON = re.compile(r"```json\s*\n(.*?)\n```", re.S)
RE_BLOCO_TXT = re.compile(r"```(?:text)?\s*\n(.*?)\n```", re.S)
RE_H_KEY = re.compile(r"^##\s+(REF-[A-Z0-9\-]+|K\d+[A-Z]?)\s*(?:[·|].*)?$", re.M)
RE_H_VID = re.compile(
    r"^###\s+(V\d+[A-Z]?)\s*[·|]\s*(T\d+)\s*[·|]\s*usa\s+(K\d+[A-Z]?)", re.M | re.I)


def parse_keyframes(prompts):
    """Casa cada heading K__/REF-__ com o proximo bloco json."""
    out = []
    hs = list(RE_H_KEY.finditer(prompts))
    for i, m in enumerate(hs):
        fim = hs[i + 1].start() if i + 1 < len(hs) else len(prompts)
        corpo = prompts[m.start():fim]
        jm = RE_BLOCO_JSON.search(corpo)
        quebra = prompts.find("\n", m.start())
        out.append({
            "id": m.group(1),
            "head": prompts[m.start():quebra if quebra > 0 else len(prompts)].strip(),
            "json_raw": jm.group(1) if jm else None,
            "linha": linha_de(prompts, m.start()),
        })
    return out


def parse_videos(prompts):
    out = []
    hs = list(RE_H_VID.finditer(prompts))
    for i, m in enumerate(hs):
        fim = hs[i + 1].start() if i + 1 < len(hs) else len(prompts)
        corpo = prompts[m.start():fim]
        bm = RE_BLOCO_TXT.search(corpo)
        out.append({
            "id": m.group(1), "take": m.group(2), "usa": m.group(3),
            "bloco": bm.group(1) if bm else None,
            "linha": linha_de(prompts, m.start()),
        })
    return out


def fala_do_bloco(bloco):
    """Extrai a fala entre aspas do prompt de video. Segundo retorno diz se e take mudo."""
    if bloco is None:
        return None, False
    if re.search(r"sem fala no take|voz-?over|voz off", bloco, re.I):
        return None, True
    m = re.search(r'a seguinte frase:\s*"(.+?)"', bloco, re.S)
    if not m:
        m = re.search(r'"(.{15,})"', bloco, re.S)
    return (norm_fala(m.group(1)) if m else None), False


NEGADORES = (r"nunca|nenhum\w*|jamais|sem\s|n[aã]o\s|nada de|proibid\w+|evitar|"
             r"\bno\b|do not|don't|avoid|never")


def em_negacao(texto, idx, janela=110):
    """True se o trecho em torno de idx estiver numa frase de PROIBICAO.

    As notas de compliance listam os termos proibidos de proposito
    ('Nunca dizer one-time', 'Nenhum prompt diz feitico, bruxa'). Sem isto
    o linter acusa justamente quem esta obedecendo a regra.
    """
    ini = texto.rfind("\n", 0, idx) + 1
    ini_frase = max(ini, idx - janela)
    for sep in (". ", "! ", "? ", "**", ": "):
        pos = texto.rfind(sep, ini_frase, idx)
        if pos > ini_frase:
            ini_frase = max(ini_frase, pos + len(sep))
    return bool(re.search(NEGADORES, texto[ini_frase:idx], re.I))


# ---------------------------------------------------------------- checagens
def detectar_angulo(roteiro, prompts):
    txt = (roteiro or "") + (prompts or "")
    m = re.search(r"[ÂA]ngulo\s*([123])", txt)
    return int(m.group(1)) if m else None


def c_travessao(arquivos, takes):
    """Em dash na COPY e falha. Em titulo ou nota de producao e so aviso.

    A copy vai pro ar, o titulo nao. O proprio gabarito (brandon_angle2) tem
    em dash num heading, entao tratar heading como falha reprovaria a referencia.
    """
    falas = {t["fala"] for t in takes if t["fala"]}
    achou = False
    for nome, txt in arquivos.items():
        linhas = txt.split("\n")
        for m in re.finditer("—", txt):
            achou = True
            ln = linha_de(txt, m.start())
            linha = linhas[ln - 1]
            trecho = linha.strip()[:90]
            copy = (linha.lstrip().startswith(">")
                    or any(f[:40] in linha for f in falas if len(f) > 40)
                    or nome == "DM.md" and not linha.lstrip().startswith("#"))
            (falha if copy else aviso)(
                "travessao", "travessao (em dash) %s: %s"
                % ("na COPY" if copy else "em titulo/nota", trecho), "%s:%d" % (nome, ln))
    if not achou:
        ok("travessao", "nenhum em dash nos arquivos")


def c_keyword(angulo, arquivos, takes):
    """A keyword errada so conta se estiver na FALA de um take.

    As notas de producao citam o modelo dos outros angulos de proposito
    ('Modelo do Angulo 2: Comment yes and I will send you the quiz'), e isso
    e referencia, nao CTA.
    """
    if angulo is None:
        aviso("keyword", "angulo nao detectado, checagem pulada")
        return
    esperada, proibida = ("222", "yes") if angulo == 3 else ("yes", "222")
    txt = "\n".join(arquivos.values())
    if re.search(r'["\'`]%s["\'`]|\b%s\b' % (esperada, esperada), txt, re.I):
        ok("keyword", "keyword '%s' presente (angulo %d)" % (esperada, angulo))
    else:
        falha("keyword", "keyword '%s' do angulo %d nao aparece em lugar nenhum" % (esperada, angulo))
    for t in takes:
        if not t["fala"]:
            continue
        if re.search(r'(?:comment|type|write)\s+["\'`]?%s\b' % proibida, t["fala"], re.I):
            falha("keyword", "%s usa a keyword ERRADA '%s' (angulo %d exige '%s')"
                  % (t["id"], proibida, angulo, esperada), "ROTEIRO.md:%d" % t["linha"])


def c_palavras_por_take(takes):
    ruim = False
    for t in takes:
        if t["fala"] is None:
            if not t["mudo"]:
                falha("palavras", "%s nao tem fala e nao esta marcado como B-ROLL/MUDO" % t["id"],
                      "ROTEIRO.md:%d" % t["linha"])
                ruim = True
            continue
        n = len(palavras(t["fala"]))
        if n < 13 or n > 29:
            falha("palavras",
                  "%s tem %d palavras (faixa 13 a 29). Quebrar em fim de frase, nunca inventar filler."
                  % (t["id"], n), "ROTEIRO.md:%d" % t["linha"])
            ruim = True
    if not ruim and takes:
        ok("palavras", "%d takes falados, todos dentro de 13 a 29 palavras"
           % len([t for t in takes if t["fala"]]))


def c_fala_literal(takes, videos):
    mapa = {t["id"]: t for t in takes}
    ruim = False
    for v in videos:
        t = mapa.get(v["take"])
        if t is None:
            falha("fala-literal", "%s aponta pro take %s, que nao existe no ROTEIRO.md"
                  % (v["id"], v["take"]), "PROMPTS_PRODUCAO.md:%d" % v["linha"])
            ruim = True
            continue
        fala_v, mudo_v = fala_do_bloco(v["bloco"])
        if mudo_v or t["mudo"]:
            continue
        if fala_v is None:
            falha("fala-literal", "%s nao tem fala entre aspas no bloco" % v["id"],
                  "PROMPTS_PRODUCAO.md:%d" % v["linha"])
            ruim = True
            continue
        if fala_v != t["fala"]:
            falha("fala-literal",
                  "%s NAO e copia literal de %s.\n           roteiro: %s\n           prompt : %s"
                  % (v["id"], t["id"], t["fala"], fala_v), "PROMPTS_PRODUCAO.md:%d" % v["linha"])
            ruim = True
    if not ruim and videos:
        ok("fala-literal", "%d prompts de video batem palavra por palavra com o roteiro" % len(videos))


def c_json_valido(kfs):
    ruim = False
    for k in kfs:
        if k["json_raw"] is None:
            falha("json", "%s nao tem bloco json" % k["id"], "PROMPTS_PRODUCAO.md:%d" % k["linha"])
            ruim = True
            continue
        try:
            json.loads(k["json_raw"])
        except Exception as e:
            falha("json", "%s tem JSON invalido: %s" % (k["id"], e),
                  "PROMPTS_PRODUCAO.md:%d" % k["linha"])
            ruim = True
    if not ruim and kfs:
        ok("json", "%d prompts de imagem com JSON valido" % len(kfs))


def c_bandeira(kfs):
    ruim = False
    for k in kfs:
        if k["id"].startswith("REF-"):
            continue  # excecao: prop isolado nao tem cenario
        if not k["json_raw"]:
            continue
        try:
            d = json.loads(k["json_raw"])
        except Exception:
            continue
        blob = " ".join(str(v) for v in d.values())
        if not re.search(r"\bflag\b|american flag|stars and stripes", blob, re.I):
            falha("bandeira",
                  "%s nao tem bandeira dos EUA no cenario (obrigatoria, discreta porem visivel, no campo scene)"
                  % k["id"], "PROMPTS_PRODUCAO.md:%d" % k["linha"])
            ruim = True
        elif not re.search(r"\bflag\b|american flag", str(d.get("scene", "")), re.I):
            # em prompt EDITAR a bandeira vive em keep_identical, e isso e o correto
            if not re.search(r"EDITAR do", k["head"], re.I):
                aviso("bandeira", "%s cita bandeira fora do campo 'scene'" % k["id"],
                      "PROMPTS_PRODUCAO.md:%d" % k["linha"])
    if not ruim and kfs:
        ok("bandeira", "bandeira dos EUA presente em todos os keyframes com cenario")


TERMOS_SENSIVEIS = [
    "penis", "erectile", "erection", "genital", "breast", "nipple", "gore",
    "wound", "naked", "nude", "sexual", "witch", "spell", "occult", "demon", "satan",
]


def c_negative(kfs):
    ruim = False
    for k in kfs:
        if not k["json_raw"]:
            continue
        try:
            d = json.loads(k["json_raw"])
        except Exception:
            continue
        neg = str(d.get("negative", ""))
        loc = "PROMPTS_PRODUCAO.md:%d" % k["linha"]
        if not neg:
            falha("negative", "%s nao tem campo 'negative'" % k["id"], loc)
            ruim = True
            continue
        if re.search(r"\bno text\b", neg, re.I):
            falha("negative",
                  "%s usa 'no text' seco. Correto: 'no captions, no subtitles, no words overlaid on the image'"
                  % k["id"], loc)
            ruim = True
        if "no captions" not in neg.lower():
            falha("negative", "%s nao tem 'no captions' no negative" % k["id"], loc)
            ruim = True
        for termo in TERMOS_SENSIVEIS:
            if re.search(r"\b%s\b" % termo, neg, re.I):
                falha("negative",
                      "%s lista termo sensivel '%s' no negative. O classificador le o token, nao a negacao."
                      % (k["id"], termo), loc)
                ruim = True
    if not ruim and kfs:
        ok("negative", "negatives corretos, sem 'no text' seco e sem termo sensivel")


def c_nomenclatura(prompts, roteiro):
    ruim = False
    for nome, txt in (("PROMPTS_PRODUCAO.md", prompts), ("ROTEIRO.md", roteiro)):
        if not txt:
            continue
        for m in re.finditer(r"^#{2,4}\s+([A-Z]{1,4})(\d+)", txt, re.M):
            if m.group(1) not in ("T", "K", "V", "REF"):
                falha("nomenclatura", "prefixo '%s%s' fora do padrao T/K/V/REF"
                      % (m.group(1), m.group(2)), "%s:%d" % (nome, linha_de(txt, m.start())))
                ruim = True
    if not ruim:
        ok("nomenclatura", "prefixos T/K/V/REF consistentes")


SECOES_ROTEIRO = [
    (r"Esqueleto preservado", "tabela de esqueleto preservado"),
    (r"Setups? de cena", "setups de cena"),
    (r"Roteiro cena a cena", "roteiro cena a cena"),
    (r"s[oó]-fala", "roteiro so-fala"),
    (r"Notas de produ", "notas de producao"),
]
SECOES_PROMPTS = [
    (r"[ÍI]ndice de gera", "indice de geracao"),
    (r"Trava de identidade", "trava de identidade e continuidade"),
    (r"Bloco global", "bloco global de video"),
    (r"Mapa de [âa]ncoras", "mapa de ancoras"),
    (r"CapCut", "montagem no CapCut"),
    (r"Gates? de qualidade", "gates de qualidade"),
]


def c_secoes(roteiro, prompts):
    for txt, specs, nome in ((roteiro, SECOES_ROTEIRO, "ROTEIRO.md"),
                             (prompts, SECOES_PROMPTS, "PROMPTS_PRODUCAO.md")):
        if txt is None:
            continue
        faltando, pos = [], []
        for pat, label in specs:
            m = re.search(r"^#{1,4}.*%s" % pat, txt, re.M | re.I)
            if m:
                pos.append((m.start(), label))
            else:
                faltando.append(label)
        if faltando:
            falha("secoes", "%s sem as secoes: %s" % (nome, ", ".join(faltando)))
        elif [l for _, l in sorted(pos)] != [l for _, l in pos]:
            falha("secoes", "%s tem as secoes fora da ordem do CLAUDE.md" % nome)
        else:
            ok("secoes", "%s com todas as secoes, na ordem" % nome)


def c_gerar_do_zero(kfs):
    zeros = [k["id"] for k in kfs if re.search(r"GERAR DO ZERO", k["head"], re.I)]
    edits = [k["id"] for k in kfs if re.search(r"EDITAR do", k["head"], re.I)]
    sem = [k["id"] for k in kfs
           if k["id"] not in zeros and k["id"] not in edits and not k["id"].startswith("REF-")]
    if sem:
        falha("gerar-do-zero",
              "keyframes sem acao declarada no titulo (GERAR DO ZERO ou EDITAR do K__): %s"
              % ", ".join(sem))
    if kfs:
        aviso("gerar-do-zero",
              "GERAR DO ZERO: %s  |  EDITAR: %s  (conferir a olho: um zero por SETUP, nunca por take)"
              % (", ".join(zeros) or "-", ", ".join(edits) or "-"))


def c_ref_maiuscula(prompts):
    ruim = False
    for m in re.finditer(r"^##+\s+(K\d+[A-Z]?|REF-[A-Z0-9\-]+)\s*[·|](.*)$", prompts, re.M):
        titulo = m.group(2)
        for ref in re.finditer(r"[âa]ncora\s+(\w+)|ref-(\w+)", titulo, re.I):
            achado = (ref.group(1) or ref.group(2))
            if achado and achado != achado.upper():
                falha("ref-caixa-alta", "referencia '%s' no titulo de %s nao esta em CAIXA ALTA"
                      % (achado, m.group(1)), "PROMPTS_PRODUCAO.md:%d" % linha_de(prompts, m.start()))
                ruim = True
    if not ruim:
        ok("ref-caixa-alta", "referencias nos titulos em caixa alta")


PRODUTO_PAT = (r"\bapp\b|\bquiz\b|smartphone|phone screen|app screenshot|mockup"
               r"|\bbottle\b|supplement|frasco")


def c_sem_produto(angulo, kfs):
    if angulo not in (2, 3):
        return
    ruim = False
    for k in kfs:
        if not k["json_raw"]:
            continue
        try:
            d = json.loads(k["json_raw"])
        except Exception:
            continue
        # o negative e onde o produto DEVE ser proibido, entao nao conta
        corpo = " ".join(str(v) for campo, v in d.items()
                         if campo not in ("negative", "reference_use"))
        for m in re.finditer(PRODUTO_PAT, corpo, re.I):
            ctx = corpo[max(0, m.start() - 45):m.start() + 45]
            if em_negacao(corpo, m.start(), janela=60):
                continue
            falha("sem-produto", "angulo %d nao mostra produto, mas %s cita '%s': ...%s..."
                  % (angulo, k["id"], m.group(0), ctx), "PROMPTS_PRODUCAO.md:%d" % k["linha"])
            ruim = True
    if not ruim and kfs:
        ok("sem-produto", "angulo %d sem produto em quadro" % angulo)


def c_blocos_video(videos):
    ruim = False
    for v in videos:
        if v["bloco"] is None:
            falha("blocos-video", "%s nao tem bloco de prompt" % v["id"],
                  "PROMPTS_PRODUCAO.md:%d" % v["linha"])
            ruim = True
            continue
        b = v["bloco"]
        loc = "PROMPTS_PRODUCAO.md:%d" % v["linha"]
        if not re.search(r"^c[âa]mera:", b, re.M | re.I):
            falha("blocos-video", "%s sem o bloco 'camera:'" % v["id"], loc)
            ruim = True
        if not re.search(r"^som ambiente:", b, re.M | re.I):
            falha("blocos-video", "%s sem o bloco 'som ambiente:'" % v["id"], loc)
            ruim = True
        elif not re.search(r"sem m[uú]sica", b, re.I):
            falha("blocos-video", "%s: som ambiente sem 'sem musica'" % v["id"], loc)
            ruim = True
        if not re.search(r"o que acontece no v[ií]deo:", b, re.I):
            falha("blocos-video", "%s sem o bloco 'o que acontece no video:'" % v["id"], loc)
            ruim = True
        _, mudo = fala_do_bloco(b)
        if not mudo and not re.search(r"lip sync", b, re.I):
            falha("blocos-video", "%s sem a trava de lip sync" % v["id"], loc)
            ruim = True
        # so vale dentro de "o que acontece no video". Na linha "camera:" falar de
        # enquadramento e legitimo ("fixa no enquadramento" = camera estavel), e o
        # proprio gabarito faz isso.
        acao = re.search(r"o que acontece no v[ií]deo:(.*?)(?=^c[âa]mera:|\Z)", b, re.S | re.M | re.I)
        if acao and re.search(r"composi[cç][aã]o|aspect ratio|9:16|plano m[eé]dio|close-?up", acao.group(1), re.I):
            falha("blocos-video",
                  "%s descreve enquadramento/composicao na acao. Isso e da IMAGEM, nunca do video." % v["id"], loc)
            ruim = True
    if not ruim and videos:
        ok("blocos-video", "%d prompts de video com os 5 blocos corretos" % len(videos))


def c_patch(arquivos):
    ruim = False
    pats = [r"adicione .{0,40}em todos os prompts", r"acrescente .{0,40}em (todos|cada)",
            r"troque .{0,30}em todos", r"basta (adicionar|trocar|colar)"]
    for nome, txt in arquivos.items():
        for pat in pats:
            for m in re.finditer(pat, txt, re.I):
                falha("prompt-completo",
                      "instrucao de patch: '%s'. Prompt entregue e prompt COMPLETO."
                      % txt[m.start():m.end()][:70], "%s:%d" % (nome, linha_de(txt, m.start())))
                ruim = True
    if not ruim:
        ok("prompt-completo", "nenhuma instrucao de patch, prompts entregues inteiros")


def c_angulo3(angulo, arquivos, kfs):
    if angulo != 3:
        return
    antes = len([f for f in FALHAS if f[0] == "angulo3"])
    if "DM.md" not in arquivos:
        falha("angulo3", "angulo 3 exige TRES arquivos: falta o DM.md")
    else:
        dm = arquivos["DM.md"]
        for pat, msg in ((r"one[- ]time", "'one-time' e trava de copy proibida"),
                         (r"pagamento [uú]nico", "'pagamento unico' e trava de copy proibida")):
            for m in re.finditer(pat, dm, re.I):
                if em_negacao(dm, m.start()):
                    continue  # e a propria nota de proibicao
                falha("angulo3", msg + " (o checkout renova a $29/mes)",
                      "DM.md:%d" % linha_de(dm, m.start()))
    for nome, txt in arquivos.items():
        for m in re.finditer(r"\bwitch\w*|\bspell\b|circle of protection|feiti[cç]o|bruxa", txt, re.I):
            if em_negacao(txt, m.start()):
                continue  # nota de compliance listando o que NAO se diz
            falha("angulo3", "registro OCULTO detectado ('%s'). A lei e: divino, nunca oculto."
                  % m.group(0), "%s:%d" % (nome, linha_de(txt, m.start())))
    for k in kfs:
        if not k["json_raw"]:
            continue
        j = k["json_raw"]
        # "portrait orientation" e formato de carta, nao retrato de rosto
        # "his/her face" e o rosto da PROPRIA avatar, e "face turned toward the camera"
        # e a face da CARTA. Nenhum dos dois e o rosto da alma gemea.
        if re.search(r"\bportrait of\b|\bpolaroid\b|photograph of a (man|person|face)"
                     r"|drawing of a face|soulmate'?s face|face of (the|her) (soulmate|man)", j, re.I):
            if not re.search(r"obscur|out of focus|frosted|silhouett|fog|mist|ice|partial"
                             r"|unreadable|not visible|hidden", j, re.I):
                falha("angulo3",
                      "%s mostra retrato/rosto sem obscurecimento. O rosto NUNCA e revelado no video."
                      % k["id"], "PROMPTS_PRODUCAO.md:%d" % k["linha"])
    if len([f for f in FALHAS if f[0] == "angulo3"]) == antes:
        ok("angulo3", "travas do angulo 3 respeitadas")


# ---------------------------------------------------------------- runner
def checar(pasta):
    global FALHAS, AVISOS, OKS
    FALHAS, AVISOS, OKS = [], [], []
    roteiro = ler(os.path.join(pasta, "ROTEIRO.md"))
    prompts = ler(os.path.join(pasta, "PROMPTS_PRODUCAO.md"))
    if roteiro is None:
        falha("arquivos", "ROTEIRO.md nao existe")
    if prompts is None:
        falha("arquivos", "PROMPTS_PRODUCAO.md nao existe")

    arquivos = {}
    for nome in ("ROTEIRO.md", "PROMPTS_PRODUCAO.md", "DM.md", "GANCHOS.md"):
        t = ler(os.path.join(pasta, nome))
        if t is not None:
            arquivos[nome] = t

    angulo = detectar_angulo(roteiro or "", prompts or "")
    takes = parse_takes(roteiro) if roteiro else []
    kfs = parse_keyframes(prompts) if prompts else []
    videos = parse_videos(prompts) if prompts else []

    c_travessao(arquivos, takes)
    c_keyword(angulo, arquivos, takes)
    c_palavras_por_take(takes)
    c_fala_literal(takes, videos)
    c_json_valido(kfs)
    c_bandeira(kfs)
    c_negative(kfs)
    c_nomenclatura(prompts or "", roteiro or "")
    c_secoes(roteiro, prompts)
    c_gerar_do_zero(kfs)
    c_ref_maiuscula(prompts or "")
    c_sem_produto(angulo, kfs)
    c_blocos_video(videos)
    c_patch(arquivos)
    c_angulo3(angulo, arquivos, kfs)

    print("=" * 82)
    print("  %s   (angulo %s | %d takes | %d keyframes | %d clipes)"
          % (pasta, angulo if angulo else "?", len(takes), len(kfs), len(videos)))
    print("=" * 82)
    for c, m in OKS:
        print("  [OK]     %-16s %s" % (c, m))
    for c, m, loc in AVISOS:
        print("  [AVISO]  %-16s %s%s" % (c, m, ("  (%s)" % loc) if loc else ""))
    for c, m, loc in FALHAS:
        print("  [FALHA]  %-16s %s%s" % (c, m, ("\n           -> %s" % loc) if loc else ""))
    print("-" * 82)
    print("  %d ok, %d avisos, %d FALHAS" % (len(OKS), len(AVISOS), len(FALHAS)))
    print()
    return len(FALHAS)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args[0] == "--todos":
        alvos = sorted(d for d in glob.glob("producao/*")
                       if os.path.isdir(d) and os.path.exists(os.path.join(d, "ROTEIRO.md")))
    else:
        alvos = args
    total = sum(checar(a.rstrip("/\\")) for a in alvos)
    print("TOTAL: %d falhas em %d pasta(s)" % (total, len(alvos)))
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
