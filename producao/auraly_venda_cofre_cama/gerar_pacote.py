"""Gera os pacotes por avatar da producao auraly_venda_cofre_cama (Auraly, GROWTH, dinheiro, avatar IA, validacao).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Identidade e roupa: os CHARACTER
SHEETS (producao/_ancoras/character_sheets/, regra so Auraly de 2026-10-04). Cenario e angulo de camera: os do
VIDEO MODELO, quase 100% fieis (quarto com cama de bau, escada escondida, cofre). Medidas: FICHA_FRAMES.md.
Prompt de imagem em JSON. Mapa K/V: K01 -> V01 (gancho), K02 -> V02 (descida e cofre, cortes internos),
K03 -> V03 a V11 (corpo, plano unico).

Saidas por avatar: PROMPTS_<AVATAR>.md, FLOW_<AVATAR>.md e ENTREGA_<AVATAR>.md.
Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")
INSTR = (AQUI.parent / "_flow" / "INSTRUCOES_AGENTE_FLOW.md").read_text(encoding="utf-8")
VERSAO = re.search(r"^Versao (\d+)", INSTR, re.M).group(1)
BLOCO_FLOW = re.search(r"## Bloco para a memoria do executor\n\n(.*?)\n## Historico resumido", INSTR, re.S).group(1).rstrip()

HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 12)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES) - {"T1", "T2"}, FALAS.keys()
PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$", ROTEIRO.split("## Tradução completa (Português)")[1].split("\n## ")[0], re.M))
assert set(PT) == set(TAKES), PT

MAPA = {"V01": "K01", "V02": "K02", **{"V%02d" % i: "K03" for i in range(3, 12)}}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
BANDEIRA = "a small American flag (discreet but visible and in focus)"
CENA_QUARTO = ("The ordinary American master bedroom of the reference video: a charcoal-grey upholstered storage bed with a "
               "tufted headboard, made with a light grey-white duvet, a dark wooden nightstand on each side of the bed with "
               "a table lamp switched off, cream-beige walls and wall-to-wall beige carpet. On the right nightstand, next to "
               "the lamp, " + BANDEIRA + " stands in a small glass.")
CENA_ESCADA = ("The hidden cellar shaft of the reference video, seen from the bedroom above: a narrow wooden staircase of plain "
               "plank treads going down between rough brown earth walls held by dark wooden beams, with a bare white bulb "
               "hanging below and, at the top, the underside of the lifted grey bed platform with its wooden slats. On a "
               "wooden beam beside the stairs, " + BANDEIRA + " is pinned.")
CENA_COFRE = ("The underground cellar vault of the reference video: rough brown earth walls, dark wooden posts and ceiling "
              "beams, a string of bare white bulbs hanging overhead, and behind the person plain wooden shelves holding "
              "stacks of hundred-dollar bills. On the wooden post at the left, " + BANDEIRA + " is pinned.")
LUZ_QUARTO = ("Neutral overcast daylight coming in from a window just out of frame on the left, cool and even, the bedside "
              "lamps switched off, soft even light on the face and body with no harsh shadows.")
LUZ_COFRE = ("Neutral cool white light as flat and even as overcast daylight, from the bare bulbs overhead and from the open hatch above, no orange "
             "or amber glow on the walls or the skin, soft even light on the face with no harsh shadows.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no studio, no grey studio background, no "
       "plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no glowing "
       "objects, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no "
       "golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no "
       "cinematic lighting, no second person in frame, no tarot cards, no candles")
PILHA = ("a stack of hundred-dollar bills, thick, held together by an orange-tan paper strap around the middle, the top "
         "bill showing a portrait and the number 100")
AVATARES = [
    dict(nome="Avery Knox", arquivo="AVERY_KNOX", genero="mulher", pos="her",
         sheet="producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg",
         identidade=("The exact fictional AI character Avery Knox: white American woman around fifty-six, voluminous shaggy "
                     "layered platinum-blonde hair with visible darker roots, brown eyes, fair skin with crow's feet and "
                     "fine lines, everyday makeup with defined brows, mascara and pink lipstick."),
         roupa=("White long-sleeve button-up shirt with a chest pocket and the cuffs rolled, medium-blue bootcut jeans, "
                "barefoot, a large turquoise and silver squash-blossom necklace, several big turquoise rings and silver "
                "cuff bracelets set with turquoise on both wrists."),
         maos="her fair hands with big turquoise rings",
         sotaque="texano carregado",
         voz="voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos"),
    dict(nome="Devon Price", arquivo="DEVON_PRICE", genero="mulher", pos="her",
         sheet="producao/_ancoras/character_sheets/devon_price_character_sheet.jpg",
         identidade=("The exact fictional AI character Devon Price: white American woman around fifty-two, closely shaved "
                     "head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined "
                     "jaw, fine lines and no makeup."),
         roupa=("Light-wash denim shirt worn open with the cuffs rolled over a fitted black crew-neck T-shirt, dark blue "
                "jeans, barefoot, large silver hoop earrings, a thin silver chain necklace and black-framed reading "
                "glasses hanging from the T-shirt collar."),
         maos="her freckled fair hands with bare fingers",
         sotaque="de Chicago",
         voz="voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago"),
    dict(nome="Jordan Vale", arquivo="JORDAN_VALE", genero="homem", pos="his",
         sheet="producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg",
         identidade=("The exact fictional AI character Jordan Vale, explicitly male: white American man around fifty-eight, "
                     "long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, "
                     "sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded "
                     "traditional American tattoos with no lettering, a swallow and a red rose on the left forearm."),
         roupa="Black leather vest over a heather grey crew-neck T-shirt, dark blue straight jeans, barefoot.",
         maos="his weathered hands with faded tattoos on the forearms",
         sotaque="do Tennessee",
         voz="voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee"),
]


EMOCAO = {
    "T3": "baixa, séria e conspiratória", "T4": "convicta e intensa", "T5": "urgente e direta", "T6": "firme e reveladora",
    "T7": "solene e intensa", "T8": "séria, em tom de aviso", "T9": "rápida e prática", "T10": "calma e confiante",
    "T11": "próxima e urgente",
}
MASC = {"baixa": "baixo", "séria": "sério", "conspiratória": "conspiratório", "convicta": "convicto", "intensa": "intenso",
        "direta": "direto", "firme": "firme", "reveladora": "revelador", "solene": "solene", "rápida": "rápido",
        "prática": "prático", "calma": "calmo", "confiante": "confiante", "próxima": "próximo"}
ACAO = {
    "T3": "{n} fala olhando fixo para a lente, com um pequeno aceno de cabeça.",
    "T4": "{n} balança a cabeça devagar, olhando fixo para a lente.",
    "T5": "{n} aponta para baixo com a mão livre, para os comentários, e depois para a lente.",
    "T8": "{n} ergue o dedo indicador da mão livre, como quem pede atenção.",
    "T9": "{n} conta nos dedos da mão livre, um, dois, três, enquanto fala.",
    "T10": "{n} fala devagar, com um pequeno aceno de cabeça.",
    "T11": "{n} se inclina um pouco para a lente e aponta para ela com a mão livre.",
}
ACAO_PADRAO = "{n} fala olhando para a lente, com pequenos gestos naturais da mão livre."
TITULOS = {
    "K01": "gancho mudo, a cama de baú estofada colada na lente e o avatar prestes a levantá-la",
    "K02": "descida, a escada de tábuas escondida vista de costas entre paredes de terra",
    "K03": "corpo, o avatar de pé no cofre segurando um maço de notas de 100 dólares na lente",
}
CAMERA = {
    "K01": ("phone fixed on a tripod about four feet above the carpet, about eight feet from the bed, 1x lens, pointing "
            "level, fixed"),
    "K02": ("phone held above and behind the person at the top of the stairs, about five feet above the carpet, 1x lens, "
            "pointing down the staircase, fixed"),
    "K03": ("phone fixed on a small stand about five feet above the floor of the vault, about three feet from the person, "
            "1x lens, pointing level, fixed"),
}


def keyframes(a):
    n, p = a["nome"], a["pos"]
    ref = (f"Use the first attached image (character sheet) only for {n}'s exact identity (face, skin, hair, body) and "
           f"wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the "
           f"reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.")
    k01 = {
        "scene": CENA_QUARTO, "lighting": LUZ_QUARTO,
        "prop": (f"The only object is the charcoal-grey upholstered storage bed, closed and made, with nothing visible "
                 f"underneath it. {n} rests one of {a['maos']} on the edge of the duvet; the other hand hangs at {p} side."),
        "posture": (f"{n} stands upright beside the bed on the right side, one hand resting on the edge of the duvet, "
                    f"looking at the lens, mouth closed, about to lift the bed."),
        "composition": (f"The charcoal-grey upholstered storage bed with its tufted headboard is very close to the lens in "
                        f"the lower left foreground, about 40 percent of the frame, its near corner about 30 inches from "
                        f"the lens, closer to the camera than {p} face, nothing else competing with it. {n} is framed from "
                        f"the top of the head to the feet. Nothing else is in the foreground. The background is reduced by "
                        f"framing, never by blur."),
        "state": f"Start frame: {n} stands with one hand on the duvet, the bed still closed, mouth closed.",
        "negative": NEG + ", no open hatch, no staircase yet, no money, no shoes, no socks",
    }
    k02 = {
        "scene": CENA_ESCADA, "lighting": LUZ_QUARTO,
        "prop": (f"The only object is the narrow wooden staircase going down between rough brown earth walls into the "
                 f"cellar shaft. {n} is already on it, seen from behind, one of {a['maos']} on the wooden beam beside the "
                 f"stairs."),
        "posture": (f"{n} descends the staircase with {p} back to the lens, one foot already on a lower tread, the "
                    f"other hand reaching back toward the lifted bed platform, {p} head slightly turned down the stairs."),
        "composition": (f"The narrow wooden staircase fills the lower half of the frame, about 50 percent of the frame, its "
                        f"top tread about 24 inches from the lens, closer to the camera than {p} back, nothing else "
                        f"competing with it. {n} is framed from the top of the head to the hips, from behind. Nothing else is "
                        f"in the foreground. The background is reduced by framing, never by blur."),
        "state": f"Start frame: {n} one step down the stairs, seen from behind, mid-stride.",
        "negative": NEG + ", no money yet, no face visible, no shoes, no socks, no smoke",
    }
    k03 = {
        "scene": CENA_COFRE, "lighting": LUZ_COFRE,
        "prop": (f"The only object is {PILHA}, held up in one of {a['maos']} toward the lens at chest height; the other "
                 f"hand hangs at {p} side."),
        "posture": (f"{n} stands inside the cellar vault facing the lens, holding the stack of bills up at chest height on "
                    f"the left of the frame, looking straight into the lens."),
        "composition": (f"The stack of hundred-dollar bills is very close to the lens in the lower left of the frame, about "
                        f"15 percent of the frame, about 16 inches from the lens, closer to the camera than {p} face, "
                        f"nothing else competing with it. {n} is framed from the top of the head to the waist, {p} face in "
                        f"the upper half. Nothing else is in the foreground. The background is reduced by framing, never "
                        f"by blur."),
        "state": f"Start frame: {n} caught mid-sentence, lips naturally parted, serious expression, the stack held still.",
        "negative": NEG + ", no money on the floor, no bills in the other hand, no shoes, no socks",
    }
    out = []
    for cod, d, take in (("K01", k01, "T1"), ("K02", k02, "T2"), ("K03", k03, "T3 a T11")):
        j = {"shot_id": f"{cod}_{a['arquivo'].lower()}", "fiction_note": FICCAO, "reference_use": ref,
             "identity_main": a["identidade"], "wardrobe": a["roupa"], "scene": d["scene"], "prop": d["prop"],
             "posture": d["posture"], "composition": d["composition"], "camera": CAMERA[cod], "lighting": d["lighting"],
             "state": d["state"], "realism": REALISMO, "aspect_ratio": "9:16 vertical", "negative": d["negative"]}
        out.append(dict(codigo=cod, take=take, titulo=TITULOS[cod], j=j))
    return out


def emocao(t, homem):
    e = EMOCAO[t]
    return re.sub(r"\w+", lambda m: MASC.get(m.group(0), m.group(0)), e) if homem else e


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art = "o avatar" if h else "a avatar"
    ouvido = "ouvido" if h else "ouvida"
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        if t == "T1":
            txt = (f"(sem fala no take: gancho mudo, {art} fica em silêncio o clipe inteiro, boca fechada)\n\n"
                   f"o que acontece no vídeo: {n} aperta a borda do colchão com as duas mãos e levanta a plataforma da cama "
                   f"de baú, que sobe devagar com um pistão e abre por baixo um poço retangular com uma escada de tábuas "
                   f"e uma lâmpada acesa lá no fundo; {n} segura a plataforma erguida com uma mão, olha para a lente e "
                   f"passa uma perna para dentro do poço.\n\n"
                   "câmera: fixa, sem movimento, um plano só, sem cortes\n\n"
                   "som ambiente: quarto silencioso, o pistão da cama subindo e o ranger leve da madeira, sem música")
        elif t == "T2":
            txt = (f"(sem fala no take: {art} fica em silêncio o clipe inteiro, boca fechada)\n\n"
                   f"o que acontece no vídeo: plano 1, {n} de costas desce a escada de tábuas entre as paredes de terra; "
                   f"corte seco para o plano 2, o cofre subterrâneo aberto, {n} de costas no pé da escada com uma mão na "
                   f"parede, com prateleiras de madeira cheias de pilhas de notas de 100 dólares e um fio de lâmpadas "
                   f"brancas; corte seco para o plano 3, macro das pilhas de notas de 100 dólares com cinta de papel "
                   f"laranja, colado na lente; corte seco para o plano 4, de costas, a mão de {n} pega um maço da "
                   f"prateleira e {n} se vira para a lente segurando o maço no peito.\n\n"
                   "câmera: fixa, com três cortes secos internos ao clipe, sem movimento\n\n"
                   "som ambiente: passos na madeira, o eco leve do cofre e o papel das notas, sem música")
        else:
            txt = (f"{art} {n}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
                   f"{emocao(t, h)}, voz autêntica, como se exigisse ser {ouvido}, a seguinte frase: \"{FALAS[t]}\"\n\n"
                   f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
                   f"sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
                   f"o que acontece no vídeo: {ACAO.get(t, ACAO_PADRAO).format(n=n)} O maço de notas continua erguido na "
                   f"outra mão e o cofre atrás não muda.\n\n"
                   "câmera: fixa, sem movimento\n\n"
                   "som ambiente: cofre subterrâneo silencioso, um eco leve, sem música")
        vs.append((cod, t, MAPA[cod], txt))
    return vs


def texto_flow(j):
    ordem = ["fiction_note", "reference_use", "identity_main", "wardrobe", "scene", "prop", "posture",
             "composition", "camera", "lighting", "state", "realism", "aspect_ratio", "negative"]
    assert set(ordem) == set(j) - {"shot_id"}, set(j) ^ set(ordem)
    d = {"format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."}
    d.update({k: j[k] for k in ordem})
    return json.dumps(d, ensure_ascii=False, indent=2)


def mapa_kv():
    return ["MAPA K/V"] + [f"{v}: {k}" for v, k in MAPA.items()]


def capcut():
    return [
        "1. Clipes numerados na ordem: V01 a V11.",
        "2. V01 e V02 (gancho mudo): usar ~5,2 s do V01 e ~4,3 s do V02, emendados no corte da descida, como o modelo "
        "(~9,5 s no total). Texto no topo, duas linhas: \"I see wealth coming into your life.\" / \"Not a single soul.\".",
        "3. V03 a V11: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / "
        "Keep Vocal. Todos saem do mesmo frame (K03), então a troca de clipe fica no mesmo enquadramento, como no modelo.",
        "4. Do V03 ao V11, legenda karaokê branca com a palavra falada em amarelo, no meio do quadro, como o modelo.",
        "5. No V11, seta vermelha para baixo no canto inferior esquerdo. Sem seta para a foto de perfil: o CTA é follow.",
        "6. Sem Voice Changer: a voz vem do prompt de cada V.",
        "7. Som ambiente baixo no V01 e no V02 (pistão, passos); sem música por baixo da fala.",
        "8. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS.get(t, '(sem fala)')} | {PT[t]} |")
    return L


INDICE = [("T1", "K01"), ("T2", "K02"), ("T3 a T11", "K03")]


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    up = a["nome"].upper()
    L = [f"# {a['nome']} | Auraly Venda Cofre Cama (growth) | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `producao/auraly_venda_cofre_cama/input/modelo.mp4` (87,7 s, avatar IA)", "",
         f"Character sheet: `{a['sheet']}`", "",
         "Funil: growth, `222` no T5 + like + save + envio + follow. Rodada de validação, cenário e ângulo do modelo.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    L += [f"| {t} | {k} | CHARACTER SHEET {up} + FRAME DO MODELO ({k}) | GERAR DO ZERO |" for t, k in INDICE]
    L += ["", "## Trava de identidade e continuidade", "",
          f"- Identidade (character sheet): {a['identidade']}", f"- Roupa (character sheet, descalço como no modelo): {a['roupa']}",
          f"- Cenário (do vídeo modelo), quarto: {CENA_QUARTO}", f"- Cenário, escada: {CENA_ESCADA}", f"- Cenário, cofre: {CENA_COFRE}",
          f"- Luz do quarto: {LUZ_QUARTO}", f"- Luz do cofre: {LUZ_COFRE}",
          f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.", "- Sem 2ª pessoa.", "",
          "## Trava do prop herói", "", "- A cama: charcoal-grey upholstered storage bed with a tufted headboard.",
          f"- O maço: {PILHA}.", "", "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "",
          "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · CHARACTER SHEET {up} + FRAME DO MODELO", "",
              "> ### 📎 ANEXAR: **2 IMAGENS**", f"> **1️⃣ CHARACTER SHEET {up}** `{a['sheet']}`",
              f"> **2️⃣ FRAME DO MODELO, cenário e ângulo** `input/frames_modelo/{k['codigo']}_modelo.png`", ">",
              "> ### 🆕 GERAR DO ZERO", "", f"Cena: {k['titulo']}.", "", "```json",
              json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Montagem no CapCut", ""] + capcut() + [""]
    flow = [f"# Blocos limpos para o Google Flow | {a['nome']}", "", f"Fonte interna: `PROMPTS_{a['arquivo']}.md`", "",
            "```text"] + mapa_kv() + ["```", "", "## BLOCO DE IMAGEM", "", "```text"]
    for k in ks:
        flow += [k["codigo"], texto_flow(k["j"]), ""]
    flow += ["```", "", "## BLOCO DE VÍDEO", "", "```text"]
    for cod, _, _, txt in vs:
        flow += [cod, txt, ""]
    flow += ["```", "", "## Transcrição final por take", ""] + transcricao()
    return "\n".join(L) + "\n", "\n".join(flow) + "\n"


CHECKLIST = ("Checklist de envio: 32/32 aprovados (N/A: A1, A2, A4, A9 fiéis ao modelo; A10 growth sem produto; "
             "C3 a C7 sem segunda pessoa, selfie, frase curta repetida, cena atuada ou motion control)")
FICHA = "Ficha: 3/3 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)"


def entrega(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Venda Cofre Cama (growth)", "",
         "Produção `auraly_venda_cofre_cama` · Ângulo 3 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY", "",
         f"## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v{VERSAO})", "",
         "Colar inteiro na memória do agente antes do primeiro K.", "", "```text", BLOCO_FLOW, "```", "",
         CHECKLIST, "", FICHA, "", "## Anexos e mapa", "",
         f"- **Character sheet {a['nome']}:** `{a['sheet']}` no K01, K02 e K03 (identidade e roupa).",
         "- **Frame do modelo** do mesmo código: `input/frames_modelo/K01_modelo.png`, `K02_modelo.png` e `K03_modelo.png` "
         "(cenário, ângulo e enquadramento).",
         "", "```text"] + mapa_kv() + ["```", "", "## 2. PROMPTS DE IMAGEM", ""]
    for k in ks:
        L += [f"### {k['codigo']} · {k['take']}, {k['titulo']} · anexar CHARACTER SHEET + FRAME DO MODELO", "",
              "```text", k["codigo"], texto_flow(k["j"]), "```", ""]
    L += ["## 3. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · frame inicial = a imagem escolhida do {kcod}", "", "```text", cod, txt, "```", ""]
    L += ["## 4. Montagem no CapCut", ""] + capcut()
    L += ["", "## 5. Transcrição final por take", ""] + transcricao()
    L += ["", "## 6. Roteiro final em inglês", ""]
    for i, t in enumerate(TAKES, 1):
        L.append(f"{i}. {FALAS.get(t, '(sem fala: gancho mudo)')}")
    L += ["", " ".join(FALAS[t] for t in TAKES if t in FALAS), ""]
    return "\n".join(L)


def main():
    for a in AVATARES:
        p, f = pacote(a)
        (AQUI / f"PROMPTS_{a['arquivo']}.md").write_text(p, encoding="utf-8")
        (AQUI / f"FLOW_{a['arquivo']}.md").write_text(f, encoding="utf-8")
        (AQUI / f"ENTREGA_{a['arquivo']}.md").write_text(entrega(a), encoding="utf-8")
    print("ok: %d avatares, Flow v%s" % (len(AVATARES), VERSAO))


if __name__ == "__main__":
    main()
