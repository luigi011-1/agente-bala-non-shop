"""Gera os pacotes por avatar da producao auraly_venda_familiar_corredor (Auraly, growth, avatar IA, validacao).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Identidade e roupa: os CHARACTER
SHEETS (producao/_ancoras/character_sheets/, regra so Auraly de 2026-10-04). Cenario e angulo de camera: os do
VIDEO MODELO, quase 100% fieis (corredor, camera no chao e depois selfie de perto). Medidas: FICHA_FRAMES.md.
Prompt de imagem em JSON. Mapa K/V: K01 -> V01 (gancho mudo com cortes internos), K02 -> V02 a V15 (corpo).

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
assert TAKES == ["T%d" % i for i in range(1, 16)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES) - {"T1"}, FALAS.keys()
PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$", ROTEIRO.split("## Tradução completa (Português)")[1].split("\n## ")[0], re.M))
assert set(PT) == set(TAKES), PT

MAPA = {"V01": "K01", **{"V%02d" % i: "K02" for i in range(2, 16)}}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
CENA = ("The ordinary American hallway of the reference video: cream-painted walls, white baseboards, red-oak plank "
        "flooring, a six-panel wooden door at the far end of the hallway and another wooden door set into the right "
        "wall. On the left wall near the far door hangs a small American flag, discreet but visible and in focus.")
LUZ = ("Neutral overcast daylight coming in from a window just out of frame, cool and even, the ceiling lights switched "
       "off, soft even light on the face and hands with no harsh shadows.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no studio, no grey studio background, no "
       "plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no blur, "
       "no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no "
       "golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic "
       "lighting, no second person in frame, no figure or silhouette in any doorway, no shoes, no socks, no tarot "
       "cards, no candles")
FILEIRA = ("a thin straight line of coarse white salt with dried leaves mixed into the salt, laid along the oak floor "
           "from the avatar's knees in a dead-straight line all the way to the far door")
RESTOS = ("the remains of a thin line of coarse white salt with dried leaves mixed into the salt, a pale streak with "
          "small leaf shapes on the oak floor")

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
    "T2": "baixa e solene, como quem traz uma mensagem delicada", "T3": "em voz mais baixa, quase em segredo",
    "T4": "calma e próxima", "T5": "serena e esperançosa", "T6": "firme e acolhedora", "T7": "direta e convidativa",
    "T8": "séria, em tom de aviso", "T9": "intensa e solene", "T10": "firme e tranquilizadora",
    "T11": "urgente e próxima", "T12": "rápida e prática", "T13": "calorosa e firme", "T14": "séria e baixa",
    "T15": "próxima e acolhedora",
}
MASC = {"baixa": "baixo", "solene": "solene", "calma": "calmo", "próxima": "próximo", "serena": "sereno",
        "esperançosa": "esperançoso", "firme": "firme", "acolhedora": "acolhedor", "direta": "direto",
        "convidativa": "convidativo", "séria": "sério", "intensa": "intenso", "tranquilizadora": "tranquilizador",
        "urgente": "urgente", "rápida": "rápido", "prática": "prático", "calorosa": "caloroso"}
ACAO = {
    "T7": "{n} olha de relance para baixo, para onde ficam os comentários, e volta o olhar para a lente.",
    "T12": "{n} baixa o olhar por um instante, para a tela, em \"press save\" e em \"tap the screen\", e volta a olhar para a lente.",
}
ACAO_PADRAO = "{n} fala olhando para a lente, com pequenas inclinações naturais da cabeça, sem nenhuma mão visível."
TITULOS = {"K01": "gancho mudo, fileira de sal e folhas no chão do corredor, câmera no chão",
           "K02": "corpo, selfie de perto agachado no corredor, restos da fileira de sal no canto"}

CAMERA = {
    "K01": ("phone resting on the hallway floor, lens at floor level about four feet from the near end of the line of salt, "
            "0.5x lens, looking along the hallway toward the far door, fixed"),
    "K02": ("selfie angle, phone held at chest height in an outstretched hand just out of frame, about 18 inches from the "
            "face, 1x front lens, pointing slightly upward, fixed"),
}


def keyframes(a):
    n, p = a["nome"], a["pos"]
    ref = (f"Use the first attached image (character sheet) only for {n}'s exact identity (face, skin, hair, body) and "
           f"wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the "
           f"reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.")
    k01 = {
        "prop": (f"The only object is {FILEIRA}, still unlit except for a tiny flame at its near end, where {n} holds a "
                 f"small plain lighter in {a['maos']}. The floor around the line is empty and clean."),
        "posture": (f"{n} kneels on the hallway floor at the left of the frame, sitting back on {p} heels, body turned toward "
                    f"the line of salt, both hands together at its near end holding the lighter, eyes on the flame, mouth "
                    f"closed."),
        "composition": (f"The thin straight line of coarse white salt runs from the bottom center of the frame straight to the "
                        f"six-panel door at the far end, about 20 percent of the frame, its near end about 48 inches from the "
                        f"lens, closer to the camera than {p} face, which is about 60 inches from the lens, nothing else "
                        f"competing with it. {n} is framed from the top of the head down to the knees on the left side of "
                        f"the frame. Nothing else is in the foreground. The background is reduced by framing, never by blur."),
        "state": f"Start frame: {n} has just lit the lighter at the near end of the line, a tiny flame, mouth closed.",
        "negative": NEG + ", no fire running along the line yet, no open door, no smoke, no salt circle, no jar",
    }
    k02 = {
        "prop": (f"In the lower right corner of the frame, on the oak floor, lie {RESTOS}. No hands and no other objects "
                 f"are in frame."),
        "posture": (f"{n} crouches in the hallway facing the lens, {p} left shoulder closer to the camera, looking straight "
                    f"into the lens with a calm intimate expression."),
        "composition": (f"{p.capitalize()} face and shoulders fill the center of the frame, about 60 percent of the frame, "
                        f"about 18 inches from the lens, the face in the upper middle with a little headroom, framed from the "
                        f"top of the head to the chest; the remains of the line of salt in the lower right corner, about 20 "
                        f"inches from the lens, about 10 percent of the frame; the hallway recedes sharply behind {p} head "
                        f"toward the far door. Nothing else is in the foreground. The background is reduced by framing, "
                        f"never by blur."),
        "state": f"Start frame: {n} looks straight into the lens, caught mid-sentence, lips naturally parted, calm intimate expression.",
        "negative": NEG + ", no smoke, no flames, no ash, no hands in frame",
    }
    out = []
    for cod, d, take in (("K01", k01, "T1"), ("K02", k02, "T2 a T15")):
        j = {"shot_id": f"{cod}_{a['arquivo'].lower()}", "fiction_note": FICCAO, "reference_use": ref,
             "identity_main": a["identidade"], "wardrobe": a["roupa"], "scene": CENA, "prop": d["prop"],
             "posture": d["posture"], "composition": d["composition"], "camera": CAMERA[cod], "lighting": LUZ,
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
                   f"o que acontece no vídeo: plano 1, {n} de joelhos no chão do corredor acende com um isqueiro a ponta da "
                   f"fileira fina de sal e folhas secas e a primeira chama sobe, bem na frente da lente; corte seco para o "
                   f"plano 2, plano aberto do corredor sem ninguém em quadro, o fogo corre pela fileira até o fundo, deixa "
                   f"cinzas e brasas no piso e perde força perto da porta de madeira; corte seco para o plano 3, a porta do "
                   f"fundo abre sozinha, devagar, para um cômodo escuro e a fumaça branca sai e rola pelo chão em direção à "
                   f"lente; corte seco para o plano 4, {n} volta ao quadro pela esquerda, ainda de joelhos, e olha para a "
                   f"lente.\n\n"
                   "câmera: fixa no chão, olhando ao longo do corredor, com três cortes secos internos ao clipe, sem movimento\n\n"
                   "som ambiente: corredor silencioso, o clique do isqueiro, o fogo estalando e a porta rangendo, sem música")
            if h:
                txt = txt.replace("de joelhos", "de joelhos")
        else:
            txt = (f"{art} {n}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, em tom de "
                   f"conversa de selfie, {emocao(t, h)}, voz autêntica, como se exigisse ser {ouvido}, a seguinte frase: "
                   f"\"{FALAS[t]}\"\n\n"
                   f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
                   f"sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
                   f"o que acontece no vídeo: {ACAO.get(t, ACAO_PADRAO).format(n=n)}\n\n"
                   "câmera: selfie de perto, fixa, sem movimento\n\n"
                   "som ambiente: corredor silencioso, sem música")
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
        "1. Clipes numerados na ordem: V01 a V15.",
        "2. V01 (gancho mudo): usar ~4,5 s, até ela olhar para a lente, que é a transição para o V02. Sem tarja no topo: o "
        "modelo não tem.",
        "3. V02 a V15: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / "
        "Keep Vocal. Todos saem do mesmo frame (K02), então a troca de clipe fica no mesmo enquadramento, como no modelo.",
        "4. Do V02 ao V15, legenda branca karaokê no meio do quadro, a palavra falada em amarelo.",
        "5. Sem seta para a foto de perfil: o CTA é follow. O `222` do V07 (antes da metade) pode levar um sinal de comentário "
        "pequeno na legenda.",
        "6. Sem Voice Changer: a voz vem do prompt de cada V.",
        "7. Música baixa por baixo da fala a partir do V02, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "8. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS.get(t, '(sem fala)')} | {PT[t]} |")
    return L


INDICE = [("T1", "K01"), ("T2 a T15", "K02")]


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    up = a["nome"].upper()
    L = [f"# {a['nome']} | Auraly Venda Familiar Corredor | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `producao/auraly_venda_familiar_corredor/input/modelo.mp4` (105,7 s, avatar IA)", "",
         f"Character sheet: `{a['sheet']}`", "",
         "Funil: growth, `222` no T7 (antes da metade) + save + toque na tela + follow. Rodada de validação, cenário e ângulo do modelo.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    L += [f"| {t} | {k} | CHARACTER SHEET {up} + FRAME DO MODELO ({k}) | GERAR DO ZERO |" for t, k in INDICE]
    L += ["", "## Trava de identidade e continuidade", "",
          f"- Identidade (character sheet): {a['identidade']}", f"- Roupa (character sheet, descalço): {a['roupa']}",
          f"- Cenário (do vídeo modelo): {CENA}", f"- Luz: {LUZ}",
          f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.", "- Sem 2ª pessoa.", "",
          "## Trava do prop herói", "", f"- A fileira: {FILEIRA}.", f"- Os restos: {RESTOS}.", "",
          "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "", "## Prompts de imagem", ""]
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


CHECKLIST = ("Checklist de envio: 32/32 aprovados (N/A: A1, A2, A7, A9 fiéis ao modelo, gancho mudo; A10 growth sem "
             "produto; C3 a C7 sem segunda pessoa, selfie na mão fora de quadro, frase curta repetida, cena atuada ou "
             "motion control)")
FICHA = "Ficha: 2/2 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)"


def entrega(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Venda Familiar Corredor", "",
         "Produção `auraly_venda_familiar_corredor` · Ângulo 3 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY", "",
         f"## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v{VERSAO})", "",
         "Colar inteiro na memória do agente antes do primeiro K.", "", "```text", BLOCO_FLOW, "```", "",
         CHECKLIST, "", FICHA, "", "## Anexos e mapa", "",
         f"- **Character sheet {a['nome']}:** `{a['sheet']}` no K01 e no K02 (identidade e roupa).",
         "- **Frame do modelo** do mesmo código: `input/frames_modelo/K01_modelo.png` no K01 e `K02_modelo.png` no K02 "
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
