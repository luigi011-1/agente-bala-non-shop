"""Gera os pacotes por avatar da producao auraly_venda_video_a (Auraly, venda, carreira/dinheiro, validacao, origem ORGANICA).

Fonte da fala: ROTEIRO.md (Avery e Devon, ingles) e ../auraly_venda_video_a_jordan_es/ROTEIRO.md (Jordan, espanhol), lidos do disco.
O pacote do Jordan sai na pasta auraly_venda_video_a_jordan_es (a fala em espanhol precisa do proprio ROTEIRO.md para o linter).
Regra do Luigi de 2026-10-06: K so com o character sheet do avatar; V so com a imagem escolhida do K. Cenario e camera do modelo vao
por escrito. Regra de 2026-10-07: cenario do Jordan e sempre de luxo maximo. Mapa: K01 -> V01 (T1), K02 -> V02 a V15.
Saidas por avatar: PROMPTS_<AVATAR>.md, FLOW_<AVATAR>.md e ENTREGA_<AVATAR>.md.  Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent


def ler(caminho):
    txt = caminho.read_text(encoding="utf-8")
    heads = dict(re.findall(r"^### (T\d+) · (.+)$", txt, re.M))
    takes = list(heads)
    assert takes == ["T%d" % i for i in range(1, 16)], takes
    falas = {}
    for bloco in re.split(r"^(?=### T\d+ · )", txt, flags=re.M)[1:]:
        t = re.match(r"### (T\d+)", bloco).group(1)
        m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
        falas[t] = m.group(1)
    tab = txt.split("## Tabela bilíngue completa")[1].split("\n## ")[0]
    pt = {t: p for t, e, p in re.findall(r"^\| (T\d+) \| (.+?) \| (.+?) \|$", tab, re.M)}
    assert set(pt) == set(takes) and set(falas) == set(takes)
    return takes, falas, pt


JORDAN_DIR = AQUI.parent / "auraly_venda_video_a_jordan_es"
TAKES, FALAS_EN, PT_EN = ler(AQUI / "ROTEIRO.md")
_, FALAS_ES, PT_ES = ler(JORDAN_DIR / "ROTEIRO.md")


MAPA = {"V01": "K01", **{"V%02d" % i: "K02" for i in range(2, 16)}}
FICCAO = "This is a fictional AI-generated character, no real person is depicted."
LUZ_COMUM = ("true neutral colors, soft even neutral daylight on the face and hands with no harsh shadows, the pale blue sky clearly visible "
             "through the window at the left and never white or blown out, no warm lamp light.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural strands, "
            "iPhone selfie footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, "
            "background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no brand names, no logos, no studio, no grey studio background, "
       "no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no glowing objects, no sparkles, "
       "no steam, no smoke, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no "
       "golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic "
       "lighting, no second person in frame, no candles, no floating text, no numbers in the air")
CARTAS = ("three Rider-Waite style tarot cards fanned out in one hand: the Wheel of Fortune card (an orange wheel with a red serpent on a "
          "blue sky, winged figures in the corners), The Star card (one large yellow eight-pointed star among small white stars on pale "
          "blue) and The Sun card (a big yellow sun on pale blue), each card with only its small printed title")

AVATARES = [
    dict(nome="Jordan Vale", arquivo="JORDAN_VALE", genero="homem", pos="his", es=True,
         sheet="producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg",
         identidade=("The exact fictional AI character Jordan Vale, explicitly male: American man aged about 68, slim and upright, full "
                     "head of thick silver-white hair combed back, thin gold-rimmed round glasses, narrow elegant face, light "
                     "blue-grey eyes with heavy lids, real aged skin with deep forehead lines, crow's feet, sun spots and soft "
                     "jowls, clean-shaven, a calm closed-mouth half smile."),
         roupa=("Cream off-white tailored dinner jacket with a white dress shirt and a black silk bow tie, a slim gold wristwatch on the "
                "left wrist and a plain gold ring on the left ring finger."),
         mao="his aged pale hand with a gold ring and a gold wristwatch", manga="a cream dinner-jacket cuff over a white shirt cuff",
         fundo=("at the left a tall arched glass window with a pale blue sky and soft cloud texture clearly visible through it and a white "
                "marble sill, a plain grey-beige silk-paneled wall with thin white molding, and behind the speaker the dark brown leather "
                "high back of an armchair in a grand mansion salon"),
         sotaque="latino-americano neutro, sem regionalismo marcado, de classe alta",
         voz="voz masculina grave, baixa e lenta de um homem de sessenta e oito anos de dinheiro antigo, autoridade tranquila",
         local="um salão de mansão silencioso"),
    dict(nome="Avery Knox", arquivo="AVERY_KNOX", genero="mulher", pos="her", es=False,
         sheet="producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg",
         identidade=("The exact fictional AI character Avery Knox: white American woman around fifty-six, voluminous shaggy "
                     "layered platinum-blonde hair with visible darker roots, brown eyes, fair skin with crow's feet and fine "
                     "lines, everyday makeup with defined brows, mascara and pink lipstick."),
         roupa=("White long-sleeve button-up shirt with a chest pocket and the cuffs rolled, a large turquoise and silver squash-blossom "
                "necklace, several big turquoise rings and silver cuff bracelets set with turquoise on both wrists."),
         mao="her fair hand with big turquoise rings and a silver turquoise cuff bracelet", manga="a rolled white shirt cuff",
         fundo=("at the left a window with a pale blue sky and soft cloud texture clearly visible through it and a white sill, a plain "
                "grey-beige wall, and behind the speaker the dark back of a sofa in an ordinary American living room"),
         sotaque="texano carregado", voz="voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos",
         local="uma sala de estar silenciosa"),
    dict(nome="Devon Price", arquivo="DEVON_PRICE", genero="mulher", pos="her", es=False,
         sheet="producao/_ancoras/character_sheets/devon_price_character_sheet.jpg",
         identidade=("The exact fictional AI character Devon Price: American woman aged about 50, slim, completely bald with a smooth "
                     "natural scalp and a few small freckles, no wig, no headscarf, light hazel-green eyes, thin natural pale eyebrows, "
                     "oval face with high cheekbones, freckles across the nose and cheeks, real aged skin with fine forehead lines, "
                     "crow's feet and laugh lines, no makeup, small silver stud earrings, a warm gentle half smile."),
         roupa=("Cream lace blazer over a cream lace camisole, a rose-gold beaded bracelet on the right wrist, a thin silver necklace "
                "with a small heart pendant, a silver band ring on the right ring finger and a thin silver ring on the left index finger."),
         mao="her freckled fair hand with a silver ring on the index finger", manga="a cream lace blazer cuff",
         fundo=("at the left a window with a pale blue sky and soft cloud texture clearly visible through it and a white sill, a plain "
                "grey-beige wall, and behind the speaker the dark back of a sofa in an ordinary American living room"),
         sotaque="neutro da Califórnia", voz="voz feminina suave, calorosa e feminina de uma mulher de cinquenta anos, acolhedora e espiritual",
         local="uma sala de estar silenciosa"),
]

EMOCAO = {
    "T1": "com espanto e entusiasmo, como quem acabou de descobrir algo",
    "T2": "em tom direto e confidencial", "T3": "em tom cansado e sincero",
    "T4": "em tom de quem conta a história de uma pessoa querida", "T5": "em tom sério, com a voz baixando no final",
    "T6": "em tom firme e convicto", "T7": "em tom suave e certo, quase um segredo",
    "T8": "em tom caloroso e respeitoso", "T9": "em tom claro e objetivo, marcando os números",
    "T10": "em tom próximo e confiante", "T11": "em tom emocionado e aliviado",
    "T12": "em tom firme e direto, marcando \"222\"", "T13": "em tom caloroso e animado",
    "T14": "em tom sério e urgente, sem levantar a voz", "T15": "em tom próximo e confiante, olhando direto na lente",
}
ACAO_EN = {
    "T1": "{n} segura três cartas de tarô abertas em leque (Wheel of Fortune, The Star e The Sun) bem perto da lente, no terço inferior do quadro, e fala olhando para a lente; por volta do quarto segundo baixa as cartas para o peito e passa a gesticular com a mão livre.",
    "T2": "{n} balança o dedo indicador em \"No\" e abre a mão em \"nobody answers\"; no fim aponta o dedo para a lente em \"for you\".",
    "T3": "{n} conta nos dedos de uma mão \"résumés\", \"inbox\", \"favors\" e \"course\" e balança a cabeça de leve em \"Nothing moved\".",
    "T4": "{n} fala olhando fixo para a lente, as duas mãos juntas diante do peito, com um pequeno aceno de cabeça em \"two hundred and twelve\".",
    "T5": "{n} imita a pergunta inclinando a cabeça em \"name one thing I haven't done\" e abre as mãos vazias em \"I'd run out of advice\".",
    "T6": "{n} bate a mão no ar em \"knock harder\", balança o indicador em \"doesn't answer to knocking\" e leva a mão ao peito em \"your porch light\".",
    "T7": "{n} aponta a mão aberta para o lado em \"the house with the porch light on\", fecha devagar os dedos em \"went dark\" e abre a mão em \"somewhere else\".",
    "T8": "{n} leva a mão ao peito em \"my great-aunt Beatrix\" e ergue os olhos por um instante em \"Archangel Chamuel\".",
    "T9": "{n} ergue três dedos em \"Three minutes\", aponta para baixo em \"on your front porch\" e faz o gesto de segurar chaves em \"your keys\".",
    "T10": "{n} faz o gesto de acender um interruptor em \"turns your porch light back on\" e abre a mão em direção à lente em \"waiting for you\".",
    "T11": "{n} sorri de leve e suspira com alívio em \"from relief\", uma mão aberta no peito.",
    "T12": "{n} aponta o dedo para a lente em \"comment 222\" e toca o peito com a mão em \"your name\".",
    "T13": "{n} ergue o polegar em \"Like this\", faz o gesto de salvar com a mão em \"Save it\" e leva a mão ao próprio peito em \"follow me\".",
    "T14": "{n} balança a cabeça devagar em \"never did it\" e aponta o indicador para a lente em \"Don't let it be you\".",
    "T15": "{n} aponta o indicador para baixo em \"tap my profile picture\" e abre as mãos em \"before the first application\".",
}
ACAO_ES = {
    "T1": ACAO_EN["T1"],
    "T2": "{n} balança o dedo indicador em \"No\" e abre a mão em \"nadie contesta\"; no fim aponta o dedo para a lente em \"hacia ti\".",
    "T3": "{n} conta nos dedos de uma mão \"currículums\", \"el correo\", \"favores\" e \"cursos\" e balança a cabeça de leve em \"nada se movía\".",
    "T4": "{n} fala olhando fixo para a lente, as duas mãos juntas diante do peito, com um pequeno aceno de cabeça em \"doscientas doce\".",
    "T5": "{n} imita a pergunta inclinando a cabeça em \"dime una sola cosa que no haya hecho\" e abre as mãos vazias em \"los consejos\".",
    "T6": "{n} bate a mão no ar em \"toques más fuerte\", balança o indicador em \"no responde a los golpes\" e leva a mão ao peito em \"la luz de tu porche\".",
    "T7": "{n} aponta a mão aberta para o lado em \"la luz del porche encendida\", fecha devagar os dedos em \"apagando\" e abre a mão em \"otro lado\".",
    "T8": "{n} leva a mão ao peito em \"mi tía abuela Beatriz\" e ergue os olhos por um instante em \"Arcángel Chamuel\".",
    "T9": "{n} ergue três dedos em \"Tres minutos\", aponta para baixo em \"en el porche de tu casa\" e faz o gesto de segurar chaves em \"tus llaves\".",
    "T10": "{n} faz o gesto de acender um interruptor em \"encender la luz de tu porche\" e abre a mão em direção à lente em \"te están esperando\".",
    "T11": "{n} sorri de leve e suspira com alívio em \"de alivio\", uma mão aberta no peito.",
    "T12": "{n} aponta o dedo para a lente em \"comenta 222\" e toca o peito com a mão em \"tu nombre\".",
    "T13": "{n} ergue o polegar em \"Dale like\", faz o gesto de salvar com a mão em \"Guárdalo\" e leva a mão ao próprio peito em \"sígueme\".",
    "T14": "{n} balança a cabeça devagar em \"nunca lo hizo\" e aponta o indicador para a lente em \"Que no seas tú\".",
    "T15": "{n} aponta o indicador para baixo em \"toca mi foto de perfil\" e abre as mãos em \"primera solicitud\".",
}


def luz(a):
    return ("Neutral overcast daylight coming from the window at the left, " + LUZ_COMUM)


def cena(a):
    return (f"A selfie taken at home, the speaker's head and shoulders fill the frame; behind the speaker, {a['fundo']}. "
            f"All of it under neutral overcast daylight.")


def keyframes(a):
    n, pos = a["nome"], a["pos"]
    base = {"fiction_note": FICCAO,
            "reference_use": (f"Use the attached image (character sheet) only for {n}'s exact identity (face, skin, hair, body) "
                              "and wardrobe; ignore its grey studio background. The setting, camera angle and framing are "
                              "described in full in the scene, camera and composition fields; no other image is attached."),
            "identity_main": a["identidade"], "wardrobe": a["roupa"]}
    cam = ("front camera selfie, phone held in the left hand about 12 inches from the face, about three and a half feet above the "
           "floor, 1x lens, level, slight natural handheld wobble")
    k1 = dict(base)
    k1.update({
        "scene": cena(a),
        "prop": f"The hero object is {CARTAS}, held fanned in {pos} right hand, very close to the lens in the lower foreground, large in frame, closer to the camera than {pos} face.",
        "posture": (f"{n} holds the phone for a selfie, looking straight into the lens, caught mid-sentence, lips naturally parted, an animated, "
                    f"wide-eyed expression, the right hand ({a['mao']}, {a['manga']}) holding the three fanned cards up near the lens."),
        "composition": (f"The three fanned cards are very close to the lens, about 10 inches from the lens, large in frame, about 35 percent of the frame, in the lower third, "
                        f"closer to the camera than {pos} face. {n}'s face and shoulders fill the frame, the top of the head near the upper 8 percent. "
                        f"Nothing else is in the foreground. The background is reduced by framing, never by blur."),
        "camera": cam,
        "lighting": luz(a),
        "state": f"Start frame: {n} is caught mid-sentence with lips parted and eyes wide, the three cards fanned close to the lens.",
        "realism": REALISMO, "aspect_ratio": "9:16 vertical",
        "negative": NEG + ", no readable text on the cards other than the small printed titles, no extra cards, no glowing cards",
    })
    k2 = dict(base)
    k2.update({
        "scene": cena(a),
        "prop": f"The hero object is {n}'s open raised right hand ({a['mao']}), palm half turned toward the lens with the fingers relaxed, in the lower right of the frame, gesturing as {pos} talks. No other prop.",
        "posture": (f"{n} holds the phone for a selfie, looking straight into the lens, caught mid-sentence, lips naturally "
                    f"parted, an animated, sincere expression, one hand raised open at chest height near the lens, {a['manga']} visible."),
        "composition": (f"The open hand is very close to the lens, about 14 inches from the lens, about 15 percent of the frame, in the lower right, closer to the camera than "
                        f"{pos} face. {n}'s face and shoulders fill the frame, the top of the head near the upper 8 percent. Nothing else is in the foreground. "
                        f"The background is reduced by framing, never by blur."),
        "camera": cam,
        "lighting": luz(a),
        "state": f"Start frame: {n} is caught mid-sentence, lips parted, the right hand open at chest height, no cards in hand.",
        "realism": REALISMO, "aspect_ratio": "9:16 vertical",
        "negative": NEG + ", no tarot card, no card in hand, no object in hand",
    })
    return [dict(codigo="K01", take="T1", titulo="gancho, selfie com três cartas de tarô em leque perto da lente", j=k1),
            dict(codigo="K02", take="T2 a T15", titulo=f"corpo, {n} em selfie, mão aberta gesticulando", j=k2)]


def falas(a):
    return (FALAS_ES, PT_ES) if a["es"] else (FALAS_EN, PT_EN)


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art = "o avatar" if h else "a avatar"
    fl, _ = falas(a)
    ACAO = ACAO_ES if a["es"] else ACAO_EN
    if a["es"]:
        idioma = (f"{art} ({a['genero']}) {n} fala em ESPANHOL (espanhol latino-americano neutro, não inglês) com sotaque {a['sotaque']}, {a['voz']}, em tom de "
                  "conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, no mesmo ritmo do vídeo modelo, ")
    else:
        idioma = (f"{art} ({a['genero']}) {n} fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, em tom de conversa de quem "
                  "grava um vídeo no celular para os seguidores, natural, próximo e confiante, no mesmo ritmo do vídeo modelo, ")
    diz = (f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar "
           "no final. Lip sync perfeito durante todo o vídeo.")
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        acao = ACAO[t].format(n=n)
        txt = (idioma + f"{EMOCAO[t]}, a seguinte frase: \"{fl[t]}\"" + "\n\n" + diz + "\n\n"
               f"o que acontece no vídeo: {acao}\n\ncâmera: selfie na mão com leve tremor natural, mesmo enquadramento do primeiro quadro, sem cortes\n\n"
               f"som ambiente: {a['local']}, leve ar-condicionado ao fundo, sem música")
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


def capcut(a):
    topo = "Te va a llegar una llamada 💫" if a["es"] else "A call is coming 💫"
    return [
        "1. Clipes na ordem: V01 a V15, jump cut seco entre eles (um frame de base, selfie contínua como no modelo).",
        f"2. Cartão fixo no meio do quadro durante o vídeo inteiro: `{topo}` (rosa, serifada itálica, como o modelo). Legenda branca no terço inferior" + (" em espanhol." if a["es"] else "."),
        "3. Sem insert: o modelo é uma selfie contínua. As frases do selo NÃO aparecem em tela (ficam no Stories).",
        "4. Sem Voice Changer: a voz vem do prompt de cada V. Isolate Voice / Keep Vocal no áudio.",
        "5. Música só depois do V01, baixa, fora da biblioteca do TikTok. Sem números brilhantes (222) na imagem.",
        "6. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao(a):
    fl, pt = falas(a)
    L = [("| Take | Español | Português |" if a["es"] else "| Take | English | Português |"), "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {fl[t]} | {pt[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# {a['nome']} | Auraly Venda Vídeo A | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `input/modelo.mp4` (115,9 s, pessoa real, orgânico)", "",
         f"Character sheet: `{a['sheet']}`", "",
         "Funil: venda, dinheiro e carreira. Comentar `222`, depois Stories. Rodada de validação." + (" **Idioma: espanhol latino neutro.**" if a["es"] else ""), "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|",
         f"| T1 | K01 | só o CHARACTER SHEET de {a['nome']} | GERAR DO ZERO |",
         f"| T2 a T15 | K02 | só o CHARACTER SHEET de {a['nome']} | GERAR DO ZERO |", "",
         "## Trava de identidade e continuidade", "",
         f"- Identidade: {a['identidade']}", f"- Roupa (do character sheet): {a['roupa']}",
         f"- Cenário: {cena(a)}", f"- Luz: {luz(a)}",
         f"- Voz (mesmo timbre em todos os V): {a['voz']}, " + ("espanhol latino neutro." if a["es"] else f"sotaque americano {a['sotaque']}."), "- Sem 2ª pessoa.", "",
         "## Trava do prop herói", "", f"- K01: {CARTAS}.", "- K02: a mão aberta do avatar, sem outro objeto.", "",
         "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "", "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · CHARACTER SHEET {a['nome'].upper()}", "",
              f"> ### 📎 ANEXAR: **1 IMAGEM**", f"> **1️⃣ CHARACTER SHEET {a['nome'].upper()}** `{a['sheet']}`", ">", "> ### 🆕 GERAR DO ZERO", "",
              f"Cena: {k['titulo']}.", "", "```json", json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Montagem no CapCut", ""] + capcut(a) + [""]
    flow = [f"# Blocos limpos para o Google Flow | {a['nome']}", "", f"Fonte interna: `PROMPTS_{a['arquivo']}.md`", "",
            "```text"] + mapa_kv() + ["```", "", "## BLOCO DE IMAGEM", "", "```text"]
    for k in ks:
        flow += [k["codigo"], texto_flow(k["j"]), ""]
    flow += ["```", "", "## BLOCO DE VÍDEO", "", "```text"]
    for cod, _, _, txt in vs:
        flow += [cod, txt, ""]
    flow += ["```", "", "## Transcrição final por take", ""] + transcricao(a)
    return "\n".join(L) + "\n", "\n".join(flow) + "\n"


def entrega(a):
    ks, vs = keyframes(a), videos(a)
    fl, _ = falas(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Venda Vídeo A", "",
         "Produção `auraly_venda_video_a` · Ângulo 3 · SALE (dinheiro e carreira) · vídeo modelo de pessoa real (orgânico) · rodada de VALIDAÇÃO · perfil AURALY"
         + (" · **em ESPANHOL**" if a["es"] else ""), "",
         "## 1. Anexos e mapa", "",
         f"- **Imagem (K):** anexar SÓ o character sheet de {a['nome']} (`{a['sheet']}`) e colar o prompt. Nada de frame modelo.",
         "- **Vídeo (V):** anexar SÓ a imagem que você escolheu daquele K e colar o prompt de vídeo.",
         "- Instruções do agente do Flow desta produção: `AGENTE_FLOW.md` (bloco colado no chat).",
         "", "```text"] + mapa_kv() + ["```", "", "## 2. PROMPTS DE IMAGEM (um bloco por K)", ""]
    for k in ks:
        L += [f"### {k['codigo']} · {k['take']}, {k['titulo']} · anexar SÓ o CHARACTER SHEET", "",
              "```text", k["codigo"], texto_flow(k["j"]), "```", ""]
    L += ["## 3. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · anexar SÓ a imagem escolhida do {kcod}", "", "```text", cod, txt, "```", ""]
    L += ["## 4. Montagem no CapCut", ""] + capcut(a)
    L += ["", "## 5. Transcrição final por take", ""] + transcricao(a)
    L += ["", "## 6. Roteiro final " + ("em espanhol" if a["es"] else "em inglês"), ""]
    for t in TAKES:
        L.append(f"{t[1:]}. {fl[t]}")
    L += ["", " ".join(fl[t] for t in TAKES), ""]
    return "\n".join(L)


def main():
    for a in AVATARES:
        p, f = pacote(a)
        AQUI_A = JORDAN_DIR if a["es"] else AQUI
        (AQUI_A / f"PROMPTS_{a['arquivo']}.md").write_text(p, encoding="utf-8")
        (AQUI_A / f"FLOW_{a['arquivo']}.md").write_text(f, encoding="utf-8")
        (AQUI_A / f"ENTREGA_{a['arquivo']}.md").write_text(entrega(a), encoding="utf-8")
    print("ok: %d avatares" % len(AVATARES))


if __name__ == "__main__":
    main()
