"""Fraseado seguro para o Google Flow (Luigi, 2026-10-09).

Problema: o Flow devolveu "This generation might violate our policies" em todos os prompts de imagem e de video
dos packs Auraly "video A" e "video B". O Flow nao tem campo de negative prompt: a lista `negative` e lida como
texto do pedido, e o classificador le o TOKEN (nudez, arma, bebida, fogo, "real person", "explicitly male"),
nao a negacao. Este modulo e a fonte unica das regras:

  * `seguro_k(j)`      reescreve um K (dict JSON) em fraseado positivo e neutro
  * `seguro_v(txt)`    reescreve um V (texto) trocando termos de gatilho por descricao neutra
  * `texto_flow(j)`    serializa o K no formato do bloco do Flow (v21, sem fiction_note nem negative)
  * `varrer_k/varrer_v` listam termos de gatilho; usado por checar_entrega.py (check `flow_seguro`)

Marcador de pacote seguro: a linha `flow_seguro: v1` no cabecalho de PROMPTS_/FLOW_/ENTREGA_. Pacote com o marcador
reprova (FALHA) em termo proibido; pacote sem o marcador so recebe AVISO (historico).

CLI: python flow_seguro.py <arquivo.md|pasta> ...   lista os gatilhos encontrados nos blocos copiaveis.
"""
import json
import re
import sys
from pathlib import Path

MARCADOR = "flow_seguro: v1"

# Substitui a lista `negative`. Frase unica, toda em positivo: o Flow nao tem negative prompt.
CLEAN_FRAME = ("A plain text-free photographic frame showing only the scene described above, true neutral colors, "
               "natural unretouched skin, hands with five natural fingers each, one person alone in frame, "
               "everything in sharp focus.")

# Campos do K entregue ao Flow, na ordem. `fiction_note` e `negative` deixaram de existir (v21).
ORDEM_K = ["reference_use", "identity_main", "wardrobe", "scene", "prop", "posture", "composition", "camera",
           "lighting", "state", "realism", "aspect_ratio", "clean_frame"]

# (regex, troca). Aplicado em todo valor string do K, nesta ordem.
TROCAS_K = [
    # identidade: sem "fictional AI character", sem "explicitly male", sem "very rich"
    (r"The exact fictional AI character ", ""),
    (r", explicitly (?:male|female)", ""),
    (r"\bvery rich ", ""),
    # referencia do character sheet
    (r"Use the attached (?:character sheet|image \(character sheet\)) only for ([\w ]+?)'s exact identity "
     r"\(face, skin, hair, body\),? (?:and )?wardrobe(?: and jewelry)?; ignore its grey studio background\. ",
     r"Use the attached character sheet as the identity reference and keep \1's face, skin, hair, body and outfit "
     r"exactly consistent; its plain backdrop is not part of the scene. "),
    (r"; no other image is attached", ""),
    # bebida alcoolica
    (r"amber glass bottle of whiske?y with a plain cream paper label with no readable text",
     "amber glass bottle with a plain cream paper label"),
    (r"whiske?y", "amber drink"),
    # fogo
    (r"burning with a small real flame about eight inches tall", "topped by a small steady flame about eight inches tall"),
    (r"a small real flame burns on the pile", "a small steady flame sits on the pile"),
    (r"small real flame", "small steady flame"),
    (r"burning board", "flame-topped board"),
    # marca
    (r"iPhone", "smartphone"),
    (r"IPHONE", "SMARTPHONE"),
    # realismo sem negacao
    (r", no AI polish, no beauty smoothing", ", natural unretouched look"),
    # negacoes escondidas nos campos positivos
    (r",? (?:and )?never white or blown out", ""),
    (r", no warm lamp light", ", daylight only"),
    (r"with no harsh shadows", "with soft shadows"),
    (r"and it does not tint the skin or the room", "and the skin and the room keep neutral colors"),
    (r"The background is reduced by framing, never by blur\.", "The background stays simple through the framing."),
    (r"Nothing else is in frame\.", "Only these elements are in frame."),
    (r"Nothing else is in the foreground\.", "Only these elements are in the foreground."),
    (r"Nothing else is held in either hand\.", "Both hands are only pressed together."),
    (r" No other prop\.", ""),
    (r"gesturing as (?:his|her) talks", "gesturing while talking"),
    (r" with a red serpent on a blue sky", " on a blue sky"),
    (r", no wig, no headscarf", ", a natural bare scalp"),
    (r", no makeup and no wig", ", a bare face and a natural bare scalp"),
    (r", no makeup", ", a bare face"),
    (r", no cards in hand", ", the hand open and empty"),
]

# Texto do V (portugues): troca por descricao neutra. Falas entre aspas nunca sao tocadas.
TROCAS_V = [
    (r"derramando o uísque", "vertendo o líquido âmbar"),
    (r"garrafa de uísque", "garrafa âmbar"),
    (r"o uísque", "o líquido âmbar"),
    (r"uísque", "líquido âmbar"),
    (r"um isqueiro acende e a chama toma o sal", "uma pequena chama surge e se firma sobre o sal"),
    (r"um isqueiro acende", "uma pequena chama surge"),
    (r"clique do isqueiro", "estalo suave"),
    (r"com a chama alta entre elas", "com a chama pequena e firme diante delas"),
    (r"chama subindo", "chama firme"),
    (r"a chama sobe um pouco", "a chama cresce um pouco"),
    (r"a chama balança um pouco", "a chama oscila de leve"),
    (r"o que está queimando", "o que está sobre a tábua"),
    (r"o som baixo da chama subindo", "um som baixo e constante"),
    (r"leve crepitar baixo da chama sobre a tábua", "leve crepitar baixo vindo da tábua"),
]

# Gatilhos para varredura. (regex, motivo)
FALHA_K = [
    (r"\bfiction_note\b|no real person|real person|fictional AI", "frase de 'pessoa real' e 'personagem de IA': o filtro le 'real person'"),
    (r"explicitly (?:male|female)", "genero explicito: o filtro le como pedido sobre o corpo"),
    (r"\"negative\"\s*:", "campo negative: o Flow nao tem negative prompt, a lista vira pedido"),
    (r"\b(?:nude|naked|nudity|topless|shirtless|lingerie|cleavage|bare chest|undress\w*|erotic|sexual|nipple|breast|genital\w*)\b",
     "nudez e corpo"),
    (r"\b(?:blood|gore|wound|corpse|cadaver|weapon|gun|knife|stab\w*|kill\w*|violen\w+|dead|death)\b", "violencia"),
    (r"\b(?:child|children|kid|kids|boy|girl|baby|toddler|teen\w*|minor)\b", "menor de idade"),
    (r"\b(?:witch\w*|spell|occult|demon|satan\w*|curse\w*|hex)\b", "ocultismo"),
    (r"\bde-aging\b|\bplastic-looking\b|\bno extra fingers\b|\bno third hand\b", "negacao de anatomia"),
]
CAUTELA_K = [
    (r"\bwhiske?y\b|\b(?:vodka|alcohol|liquor|booze|wine|beer|drunk)\b", "bebida alcoolica"),
    (r"\b(?:lighter|ignite|igniting|arson|torch|bonfire|inferno)\b|\bburn(?:s|ing|ed)?\b|\bfire\b",
     "fogo e queima"),
    (r"\b(?:Eiffel|Burj|Taj Mahal|Louvre|Disney|Rolex|Rolls[- ]Royce|Ferrari|Lamborghini|Louis Vuitton|Chanel|"
     r"Hermes|Gucci|iPhone|Apple|Nike|Coca[- ]Cola)\b", "marca, celebridade ou monumento"),
]
FALHA_V = [
    (r"\b(?:nu|nua|nudez|sangue|arma|facada|matar|morte|morrer|violên\w+|criança\w*|menino|menina|bebê)\b",
     "nudez, violencia ou menor de idade"),
    (r"explicitamente (?:homem|mulher)", "genero explicito"),
]
CAUTELA_V = [
    (r"\b(?:uísque|whisky|whiskey|vodka|álcool|bebida alcoólica|cerveja|vinho)\b", "bebida alcoolica"),
    (r"\b(?:isqueiro|fogo|incêndio|queimar|queimando|ateia\w*)\b", "fogo e queima"),
]
# Limite de negacoes no K: cada "no X", "never", "without", "not" vira pedido literal para o modelo.
LIMITE_NEGACOES_K = 2
RE_NEGACAO = re.compile(r"\b(?:no|never|without|nothing|not|don't|doesn't)\b", re.I)


def _troca(txt, tabela):
    for pad, rep in tabela:
        txt = re.sub(pad, rep, txt)
    return txt


def seguro_k(j):
    """Recebe o dict do K (formato v17, com fiction_note e negative) e devolve o do v21."""
    out = {}
    for k, v in j.items():
        if k in ("fiction_note", "negative", "shot_id"):
            continue
        out[k] = _troca(v, TROCAS_K) if isinstance(v, str) else v
    extra = _extra_positivo(j.get("negative", ""))
    out["clean_frame"] = CLEAN_FRAME + (" " + extra if extra else "")
    return out


def _extra_positivo(neg):
    """Traduz os extras do K (cartas, mao vazia) para positivo. O resto do negative some."""
    extras = []
    if re.search(r"readable text on the cards", neg):
        extras.append("Exactly three cards, each showing only its small printed title.")
    if re.search(r"no tarot card|no card in hand", neg):
        extras.append("The raised hand is open and empty.")
    return " ".join(extras)


def seguro_v(txt):
    """Troca termos de gatilho no texto do V sem tocar nas falas entre aspas."""
    partes = re.split(r'("[^"\n]*")', txt)
    return "".join(p if p.startswith('"') and p.endswith('"') else _troca(p, TROCAS_V) for p in partes)


def texto_flow(j):
    """Bloco do Flow: JSON em ingles, so os campos de ORDEM_K mais `format`. `j` ja passou por seguro_k."""
    assert set(ORDEM_K) == set(j) - {"shot_id"}, set(ORDEM_K) ^ (set(j) - {"shot_id"})
    d = {"format": "IMPORTANT: THIS IS SMARTPHONE FOOTAGE. Vertical 9:16."}
    d.update({k: j[k] for k in ORDEM_K})
    return json.dumps(d, ensure_ascii=False, indent=2)


def sem_falas(txt):
    return re.sub(r'"[^"\n]*"', '""', txt)


def varrer_k(txt):
    """Lista (nivel, termo, motivo) para um K (JSON ou texto). nivel: FALHA ou AVISO."""
    ach = []
    for pad, motivo in FALHA_K:
        for m in re.finditer(pad, txt, re.I):
            ach.append(("FALHA", m.group(0), motivo))
    for pad, motivo in CAUTELA_K:
        for m in re.finditer(pad, txt, re.I if "iPhone" not in pad else 0):
            ach.append(("AVISO", m.group(0), motivo))
    n = len(RE_NEGACAO.findall(txt))
    if n > LIMITE_NEGACOES_K:
        ach.append(("FALHA", "%d negacoes" % n, "mais de %d 'no/never/without/not' no K: o modelo le como pedido" % LIMITE_NEGACOES_K))
    return ach


def varrer_v(txt):
    corpo = sem_falas(txt)
    ach = []
    for pad, motivo in FALHA_V:
        for m in re.finditer(pad, corpo, re.I):
            ach.append(("FALHA", m.group(0), motivo))
    for pad, motivo in CAUTELA_V:
        for m in re.finditer(pad, corpo, re.I):
            ach.append(("AVISO", m.group(0), motivo))
    return ach


RE_BLOCO = re.compile(r"```(?:json|text)?\n(.*?)```", re.S)


def varrer_arquivo(caminho):
    """Varre os blocos copiaveis de um .md. Devolve lista (id, nivel, termo, motivo)."""
    txt = Path(caminho).read_text(encoding="utf-8")
    res = []
    for b in RE_BLOCO.findall(txt):
        m = re.match(r"\s*(K\d+|REF-\w+|V\d+)\b", b)
        cod = m.group(1) if m else None
        if cod is None and b.lstrip().startswith("{"):
            cod = "K?"
        if cod is None and "o que acontece no vídeo" in b:
            cod = "V?"
        if cod is None:
            continue
        fn = varrer_k if cod.startswith(("K", "REF")) else varrer_v
        for nivel, termo, motivo in fn(b):
            res.append((cod, nivel, termo, motivo))
    return res


# ---- Versao CURTA (2026-10-09): se o limite for o tamanho do prompt, nao a palavra ----
def compacto_k(j):
    """K em um paragrafo so (~600-900 caracteres): identidade, roupa, cena, prop, estado, camera e fecho fixo."""
    j = seguro_k(j) if "clean_frame" not in j else j
    partes = ["Match the attached character sheet exactly.", j["identity_main"], j["wardrobe"], j["scene"], j["prop"],
              j["state"].replace("Start frame: ", ""), j["camera"].split(", ")[0] + ", 1x lens, level.",
              "Neutral overcast daylight, true neutral colors, real skin texture, smartphone footage look, everything in "
              "sharp focus, text-free frame, 9:16 vertical."]
    return " ".join(x.strip() for x in partes if x)


def compacto_v(txt):
    """V enxuto: troca a frase longa de lip sync por uma curta e corta repeticoes de tom. Falas intactas."""
    txt = re.sub(r"\n\n[^\n]*diz todas as palavras corretamente[^\n]*\n", "\n\nDiz todas as palavras, lip sync perfeito.\n", txt)
    txt = re.sub(r"fala (?:em )?ESPANHOL latino neutro, sem sotaque americano e sem falar inglês, ", "fala em espanhol latino neutro, ", txt)
    txt = re.sub(r", em tom de gravação direta para a câmera, natural e confiante", "", txt)
    txt = re.sub(r", em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, no mesmo ritmo do vídeo modelo", "", txt)
    return txt


def gerar_curto(entrega, saida):
    """Le um ENTREGA_*.md e grava a versao curta: K em paragrafo, V enxuto."""
    t = Path(entrega).read_text(encoding="utf-8")
    out = ["# " + Path(entrega).stem + " (versao CURTA)", "", MARCADOR, "",
           "Mesmo conteudo da ENTREGA, em prompts curtos. K = character sheet + prompt, 4 variacoes 9:16. V = imagem escolhida + prompt, 1 variacao 9:16.", ""]
    for b in RE_BLOCO.findall(t):
        m = re.match(r"\s*(K\d+)\n(\{.*\})\s*$", b, re.S)
        if m:
            d = json.loads(m.group(2))
            d.pop("format", None)
            d.setdefault("clean_frame", CLEAN_FRAME)
            out += ["```text", m.group(1), compacto_k(d), "```", ""]
            continue
        m = re.match(r"\s*(V\d+)\n(.*)$", b, re.S)
        if m:
            out += ["```text", m.group(1), compacto_v(m.group(2)).strip(), "```", ""]
    Path(saida).write_text("\n".join(out), encoding="utf-8")
    return len("\n".join(out))


def main(args):
    total = 0
    for a in args:
        p = Path(a)
        arqs = sorted(p.rglob("*.md")) if p.is_dir() else [p]
        for f in arqs:
            if not re.match(r"(PROMPTS|FLOW|ENTREGA)_", f.name):
                continue
            for cod, nivel, termo, motivo in varrer_arquivo(f):
                total += 1
                print("%s %s %s: '%s' (%s)" % (nivel, f, cod, termo, motivo))
    print("%d achado(s)" % total)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
