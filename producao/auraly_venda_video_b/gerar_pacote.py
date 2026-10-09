"""Gera os pacotes por avatar da producao auraly_venda_video_b (Auraly, venda, dinheiro e prosperidade, validacao, avatar IA).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco). Avery e Devon falam ingles; Jordan Vale fala ESPANHOL (tabela
Espanol do ROTEIRO.md). Regra do Luigi de 2026-10-06: o K so anexa o character sheet do avatar e o V so anexa a imagem
escolhida; cenario, camera, pose e acao do modelo vao por extenso dentro de cada prompt.
Mapa K/V: K01 (gancho mudo, garrafa de uisque) -> V01; K02 (corpo, maos em oracao com a chama) -> V02 a V14.
Saidas por avatar: PROMPTS_, FLOW_ e ENTREGA_<AVATAR>.md, mais AGENTE_FLOW.md e FICHA_FRAMES.md da producao.
Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")
HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 15)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
# T1 e mudo: sem fala
assert set(FALAS) == set(TAKES) - {"T1"}, FALAS.keys()


def tabela(titulo):
    sec = ROTEIRO.split(titulo)[1].split("\n## ")[0]
    return {t: (a, b) for t, a, b in re.findall(r"^\| (T\d+) \| (.+?) \| (.+?) \|$", sec, re.M)}


TAB_EN = tabela("## Tradução completa: Avery Knox e Devon Price")
TAB_ES = tabela("## Tradução completa: Jordan Vale (espanhol)")
for t in TAKES[1:]:
    assert TAB_EN[t][0] == FALAS[t], t
ES = {t: TAB_ES[t][0] for t in TAKES[1:]}
PT_EN = {t: TAB_EN[t][1] for t in TAKES}
PT_ES = {t: TAB_ES[t][1] for t in TAKES}

MAPA = {"V01": "K01"}
MAPA.update({"V%02d" % i: "K02" for i in range(2, 15)})

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
LUZ = ("Neutral overcast daylight coming through the window, the outside clearly visible through it under a grey-blue "
       "overcast sky with visible cloud texture, never white or blown out, soft even light on the face and hands with no "
       "harsh shadows; the only bright point is the small real flame itself and it does not tint the skin or the room.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no numbers overlaid on the image, no readable text on "
       "the bottle, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, "
       "no glowing aura, no sparkles, no floating objects, no blur, no bokeh, no artificial lighting, no warm orange color "
       "cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty "
       "smoothing, no HDR, no cinematic lighting, no second person in frame, no phone in frame")

TABUA = ("a rectangular wooden cutting board lying on the wooden table in the lower foreground, holding a mound of coarse "
         "white sea salt, a few dried bay leaves and three cinnamon sticks")

CENA_CASA = ("A cozy American living room seen from a phone propped on the table at table height: a pale cream ceiling "
             "with angled edges and a garland of gold paper stars with thin curling ribbons hanging from its edge, a white "
             "horizontal window blind at the right with soft neutral daylight behind it, and a small American flag on a "
             "short stand on a shelf at the left, discreet but visible and in focus. In the lower foreground " + TABUA + ".")
CENA_MANSAO = ("The dining room of a luxury mansion seen from a phone propped on the table at table height: an ornate "
               "cream plaster ceiling with the edge of a crystal chandelier, a tall arched window at the right with a "
               "linen drape and soft neutral daylight over a clipped garden, and a small American flag on a slim brass "
               "stand on a console at the left, discreet but visible and in focus. In the lower foreground a white marble "
               "dining table holding a teak cutting board with a mound of coarse white sea salt, a few dried bay leaves "
               "and three cinnamon sticks.")
CAM = ("phone camera propped on the table at table height, about 12 inches behind the board, 1x lens, level, fixed with "
       "a slight natural handheld shake")

AVATARES = [
    dict(nome="Avery Knox", arquivo="AVERY_KNOX", genero="mulher", pron="She", pos="her", cena=CENA_CASA, lingua="en",
         sheet="producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg",
         identidade=("The exact fictional AI character Avery Knox: white American woman around sixty, voluminous shaggy "
                     "layered platinum-blonde hair with darker roots, brown eyes, fair skin with crow's feet and fine "
                     "lines, everyday makeup with defined brows, mascara and soft pink lipstick."),
         roupa=("White long-sleeve button-up shirt with the cuffs loosely rolled to the forearms, blue bootcut jeans, a "
                "large turquoise and silver squash-blossom necklace, several big turquoise rings, and a silver cuff "
                "bracelet set with turquoise."),
         maos="her fair hands with big turquoise rings and the silver turquoise cuff bracelet below the rolled white cuffs",
         voz="voz feminina quente e firme, levemente rouca, de uma mulher de sessenta anos"),
    dict(nome="Devon Price", arquivo="DEVON_PRICE", genero="mulher", pron="She", pos="her", cena=CENA_CASA, lingua="en",
         sheet="producao/_ancoras/character_sheets/devon_price_character_sheet.jpg",
         identidade=("The exact fictional AI character Devon Price: white American woman around fifty with a completely "
                     "bald smooth head, hazel eyes, freckles across the face and scalp, fine lines, no makeup and no wig."),
         roupa=("Cream lace blazer over a cream lace camisole, a thin silver chain necklace with a small heart pendant, "
                "small silver stud earrings, a rose-gold beaded bracelet, thin silver rings, and blue skinny jeans."),
         maos="her freckled fair hands with thin silver rings and the rose-gold beaded bracelet below the lace cuffs",
         voz="voz feminina calma e direta, de uma mulher de cinquenta anos"),
    dict(nome="Jordan Vale", arquivo="JORDAN_VALE", genero="homem", pron="He", pos="his", cena=CENA_MANSAO, lingua="es",
         sheet="producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg",
         identidade=("The exact fictional AI character Jordan Vale, explicitly male: very rich white American man around "
                     "sixty-eight, slim, full silver-white hair swept back, thin round gold-rimmed glasses, light blue-grey "
                     "eyes, age spots, freckles and deep forehead lines."),
         roupa=("Cream dinner jacket over a crisp white shirt with a black bow tie, black tuxedo trousers, a gold "
                "wristwatch on the left wrist and a gold ring."),
         maos="his slim aged hands with a gold ring and the gold wristwatch below the cream cuff",
         voz="voz masculina grave, calma e distinta, de um homem de sessenta e oito anos"),
]

ACAO = {
    "T2": "{n} olha firme para a lente com as mãos juntas em oração e a chama subindo entre elas, dá um leve aceno de cabeça no fim da última frase.",
    "T3": "{n} fala com o olhar firme na lente, as mãos juntas imóveis, e fecha os olhos por um instante ao lembrar da oração, voltando para a lente.",
    "T4": "{n} ergue as sobrancelhas de leve ao dizer o número de anos, a chama balança um pouco, as mãos continuam juntas.",
    "T5": "{n} inclina a cabeça para o lado ao repetir a pergunta e fica parado um instante olhando para a lente, depois o olhar clareia na palavra final.",
    "T6": "{n} fala baixo e confidencial, inclina o corpo um pouco para a lente, as mãos juntas com a chama no meio.",
    "T7": "{n} olha para a tábua por um instante ao falar da panela e volta o olhar para a lente na última frase, as mãos juntas.",
    "T8": "{n} olha para cima por um instante ao citar o arcanjo e volta para a lente, um aceno de cabeça firme no fim.",
    "T9": "{n} olha para a tábua com a chama ao dizer o que está queimando e volta para a lente, as mãos juntas imóveis.",
    "T10": "{n} fala com firmeza, inclina a cabeça para baixo e à frente ao dizer \"abaixo\" e depois volta o olhar para a lente, as mãos juntas.",
    "T11": "{n} fica solene e baixa a voz ao falar da pessoa que pulou o selo, sem sorrir, as mãos juntas, a chama baixa e firme.",
    "T12": "{n} suaviza a expressão e dá um meio sorriso, os olhos úmidos, a chama sobe um pouco entre as mãos.",
    "T13": "{n} olha direto para a lente, inclina levemente a cabeça no convite e dá um leve aceno de cabeça no fim.",
    "T14": "{n} inclina a cabeça levemente para baixo e para o lado em direção ao perfil e volta para a lente com leve sorriso de convite, as mãos juntas com a chama.",
}
EMOCAO = {
    "T2": "grave, em tom de aviso", "T3": "firme e confessional", "T4": "calma, como quem lembra uma história",
    "T5": "séria, com um tom de descoberta", "T6": "baixa e confidencial, como quem conta um segredo", "T7": "calma e certa",
    "T8": "reverente e firme", "T9": "firme e convicta", "T10": "firme e urgente", "T11": "grave e solene, em tom de aviso",
    "T12": "mais suave e aliviada", "T13": "próxima e firme", "T14": "calorosa e firme, em tom de convite",
}
MASC = {"convicta": "convicto", "certa": "certo", "calma": "calmo", "aliviada": "aliviado", "baixa": "baixo",
        "reverente": "reverente", "próxima": "próximo", "calorosa": "caloroso", "séria": "sério", "firme": "firme",
        "urgente": "urgente", "confidencial": "confidencial", "confessional": "confessional", "suave": "suave",
        "mais": "mais", "muito": "muito", "grave": "grave", "solene": "solene"}
SOM = ("sala de casa em silêncio, leve crepitar baixo da chama sobre a tábua, voz com leve eco natural, ruído suave de tecido, sem música")
SOM_MANSAO = ("sala de jantar ampla em silêncio, leve crepitar baixo da chama sobre a tábua, voz com leve eco natural de ambiente grande, ruído suave de tecido, sem música")


def emocao(t, homem):
    e = EMOCAO[t]
    return re.sub(r"\w+", lambda m: MASC.get(m.group(0), m.group(0)), e) if homem else e


def prompt_k(a, tipo):
    n, P, p = a["nome"], a["pron"], a["pos"]
    ref = (f"Use the attached character sheet only for {n}'s exact identity (face, skin, hair, body), wardrobe and "
           f"jewelry; ignore its grey studio background. The setting, camera angle, pose and action are fully "
           f"described in this prompt.")
    if tipo == "K01":
        j = {
            "fiction_note": FICCAO, "reference_use": ref, "identity_main": a["identidade"], "wardrobe": a["roupa"],
            "scene": a["cena"],
            "prop": (f"{n} holds an amber glass bottle of whiskey with a plain cream paper label with no readable text, "
                     f"with both hands against the chest, the right hand twisting the cap; the bottle is in the lower "
                     f"foreground about 24 inches from the lens, closer to the camera than {p} face, and it takes up about "
                     f"25 percent of the frame. The board with salt, bay leaves and cinnamon sits at the very bottom edge of the frame."),
            "posture": (f"{n} sits upright behind the table with the torso straight toward the lens, shoulders relaxed, "
                        f"smiling softly into the lens, caught mid-motion as {P.lower()} starts to open the bottle; {a['maos']}."),
            "composition": (f"{n} fills the frame from the top of the head, about 8 percent from the top edge, down to the "
                            f"bottle and the board at the bottom edge, centered, the face about 36 inches from the lens. "
                            f"The wall and window fill the sides. Nothing else is in frame. The background is reduced by "
                            f"framing, never by blur."),
            "camera": CAM, "lighting": LUZ,
            "state": f"Start frame: {n} is already smiling at the lens with the unopened bottle held against the chest, the right hand starting to twist the cap.",
            "realism": REALISMO, "aspect_ratio": "9:16 vertical", "negative": NEG,
        }
        return {"codigo": "K01", "take": "T1", "titulo": "gancho mudo, segurando a garrafa de uísque diante da tábua", "j": j}
    j = {
        "fiction_note": FICCAO, "reference_use": ref, "identity_main": a["identidade"], "wardrobe": a["roupa"],
        "scene": a["cena"].replace("In the lower foreground " + TABUA + ".", "In the lower foreground " + TABUA + ", burning with a small real flame about eight inches tall."),
        "prop": (f"On the board in the lower foreground a small real flame burns on the pile of coarse salt, bay leaves and "
                 f"cinnamon sticks and rises between {n}'s hands; {p} hands are pressed together palm to palm in a prayer "
                 f"position at chest height, fingertips pointing up and just behind the flame, about 24 inches from the "
                 f"lens, closer to the camera than {p} face, and hands plus flame take up about 22 percent of the frame. "
                 f"Nothing else is held in either hand."),
        "posture": (f"{n} sits upright behind the table with the torso turned straight toward the lens, shoulders relaxed, "
                    f"looking straight into the lens, caught mid-sentence, lips naturally parted, calm animated expression; {a['maos']}."),
        "composition": (f"{n} fills the frame from the top of the head, about 8 percent from the top edge, down to the "
                        f"burning board at the bottom edge, centered, the face about 36 inches from the lens. The wall and "
                        f"window fill the sides. Nothing else is in frame. The background is reduced by framing, never by blur."),
        "camera": CAM, "lighting": LUZ,
        "state": f"Start frame: {n} is already looking into the lens with the hands pressed together and the flame standing between them, caught mid-sentence.",
        "realism": REALISMO, "aspect_ratio": "9:16 vertical", "negative": NEG,
    }
    return {"codigo": "K02", "take": "T2 a T14", "titulo": "corpo, mãos em oração com a chama entre elas", "j": j}


def keyframes(a):
    return [prompt_k(a, "K01"), prompt_k(a, "K02")]


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art = "o avatar" if h else "a avatar"
    som = SOM_MANSAO if h else SOM
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        if t == "T1":
            ambiente = ("a sala de jantar de mansão" if h else "a sala")
            txt = (f"(sem fala no take: o clipe é mudo e {art} {n} não fala; o texto de tela entra só na edição)\n\n"
                   f"{art} fica em silêncio o tempo todo; os lábios fecham e não há voz nem sussurro.\n\n"
                   f"o que acontece no vídeo: {n} já começou a abrir a garrafa de uísque e sorri para a lente; corte para {n} "
                   f"inclinando a garrafa e derramando o uísque sobre o sal grosso, as folhas de louro e os paus de canela na tábua; "
                   f"corte para um MACRO das mãos e da tábua no instante do payoff: um isqueiro acende e a chama toma o sal, o louro "
                   f"e a canela; corte de volta para o plano de corpo: as mãos de {n} se juntam em oração com a chama alta entre elas "
                   f"e {art} olha para a lente.\n\n"
                   "câmera: cortes internos ao clipe (plano de corpo, plano do derrame, macro das mãos e da tábua, plano de corpo), "
                   "câmera de celular apoiada na mesa na altura da mesa, com leve tremor natural\n\n"
                   f"som ambiente: {ambiente} em silêncio, líquido caindo, clique do isqueiro, o som baixo da chama subindo, sem música e sem voz")
        elif a["lingua"] == "es":
            txt = (f"{art} {n} ({a['genero']}) fala em ESPANHOL latino neutro, sem sotaque americano e sem falar inglês, {a['voz']}, "
                   f"em tom de gravação direta para a câmera, natural e confiante, {emocao(t, h)}, a seguinte frase em espanhol: \"{ES[t]}\"\n\n"
                   f"{art} fala espanhol do começo ao fim, diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
                   f"sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
                   f"o que acontece no vídeo: {ACAO[t].format(n=n)}\n\n"
                   "câmera: fixa, apoiada na mesa na altura da mesa, com leve tremor natural de celular\n\n"
                   f"som ambiente: {som}")
        else:
            txt = (f"{art} {n} ({a['genero']}) fala em inglês com sotaque americano de {n}, {a['voz']}, em tom de gravação "
                   f"direta para a câmera, natural e confiante, {emocao(t, h)}, a seguinte frase: \"{FALAS[t]}\"\n\n"
                   f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
                   f"sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
                   f"o que acontece no vídeo: {ACAO[t].format(n=n)}\n\n"
                   "câmera: fixa, apoiada na mesa na altura da mesa, com leve tremor natural de celular\n\n"
                   f"som ambiente: {som}")
        vs.append((cod, t, MAPA[cod], txt))
    return vs


def texto_flow(j):
    ordem = ["fiction_note", "reference_use", "identity_main", "wardrobe", "scene", "prop", "posture",
             "composition", "camera", "lighting", "state", "realism", "aspect_ratio", "negative"]
    assert set(ordem) == set(j), set(j) ^ set(ordem)
    d = {"format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."}
    d.update({k: j[k] for k in ordem})
    return json.dumps(d, ensure_ascii=False, indent=2)


def mapa_kv():
    return ["MAPA K/V"] + [f"{v}: {k}" for v, k in MAPA.items()]


def capcut(a):
    es = a["lingua"] == "es"
    tela = '"Funciona tan rápido que asusta..."' if es else '"It works so fast it scares me..."'
    return [
        "1. Clipes numerados na ordem: V01 a V14. V01 é mudo e o modelo gasta só 4,7s nele: cortar a sobra. V02 a V14 saem do mesmo frame (K02), então o enquadramento não muda, como no modelo.",
        "2. Jump cut a cada take, cortando logo depois da última palavra. Isolate Voice / Keep Vocal no áudio.",
        f"3. Texto de abertura no V01: {tela}. Legenda karaokê branca grossa embaixo, palavra a palavra, como no modelo; adesivos pequenos \"222\" e \"444\" nos cantos; setas vermelhas no V14. Nada disso entra no K nem no V.",
        "4. Sem Voice Changer: a voz vem do prompt de cada V. Sem música no gancho; música baixa a partir do V02, fora da biblioteca do TikTok.",
        "5. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao(a):
    es = a["lingua"] == "es"
    L = ["| Take | " + ("Español" if es else "English") + " | Português |", "|---|---|---|"]
    for t in TAKES:
        if t == "T1":
            L.append("| T1 | " + ("(gancho ritual mudo, sin palabras)" if es else "(mute ritual hook, no words)") + f" | {PT_ES['T1'] if es else PT_EN['T1']} |")
        else:
            L.append(f"| {t} | {ES[t] if es else FALAS[t]} | {(PT_ES if es else PT_EN)[t]} |")
    return L


def fala_do(a, t):
    return ES[t] if a["lingua"] == "es" else FALAS[t]


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# {a['nome']} | Auraly Venda Vídeo B | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `input/modelo.mp4` (119,8 s, avatar IA falando espanhol: queima de sal, louro e canela com uísque, chama entre as mãos em oração, plano único depois do gancho mudo)", "",
         f"Character sheet: `{a['sheet']}`", "",
         "Idioma da fala: " + ("ESPANHOL latino neutro" if a["lingua"] == "es" else "inglês americano") + ".", "",
         "Funil: venda, dinheiro e prosperidade. 222 + primeiro nome, depois perfil e Stories. Rodada de validação.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|",
         f"| T1 | K01 | CHARACTER SHEET {a['nome'].upper()} | GERAR DO ZERO |",
         f"| T2 a T14 | K02 | CHARACTER SHEET {a['nome'].upper()} | GERAR DO ZERO |", "",
         "## Trava de identidade e continuidade", "",
         f"- Identidade: {a['identidade']}", f"- Roupa (a do character sheet): {a['roupa']}",
         f"- Cenário (o do modelo, versão {a['nome']}): {a['cena']}", f"- Luz: {LUZ}",
         f"- Voz (mesmo timbre em todos os V): {a['voz']}, " + ("espanhol latino neutro" if a["lingua"] == "es" else "sotaque americano") + ".", "- Sem 2ª pessoa.", "",
         "## Trava do prop herói", "", "- K01: garrafa de uísque âmbar sem rótulo legível. K02: a chama sobre sal, louro e canela entre as mãos em oração.", "",
         "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "", "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · CHARACTER SHEET {a['nome'].upper()}", "",
              "> ### 📎 ANEXAR: **1 IMAGEM**", f"> **1️⃣ CHARACTER SHEET {a['nome'].upper()}** `{a['sheet']}`", ">",
              "> ### 🆕 GERAR DO ZERO", "", f"Cena: {k['titulo']}.", "", "```json", json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Montagem no CapCut", ""] + capcut(a) + [""]
    flow = [f"# Blocos limpos para o Google Flow | {a['nome']}", "", f"Fonte interna: `PROMPTS_{a['arquivo']}.md`", "",
            "Idioma da fala: " + ("ESPANHOL latino neutro" if a["lingua"] == "es" else "inglês americano") + ".", "",
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
    es = a["lingua"] == "es"
    L = [f"# ENTREGA | {a['nome']} | Auraly Venda Vídeo B", "",
         "Produção `auraly_venda_video_b` · Ângulo 3 · SALE (dinheiro e prosperidade) · rodada de VALIDAÇÃO · perfil AURALY" + (" · FALA EM ESPANHOL" if es else ""), "",
         "Instruções do agente do Flow: `AGENTE_FLOW.md` desta produção (colado no chat).", "",
         "## Anexos e mapa", "",
         f"- **Imagem (K):** anexar SÓ o character sheet de {a['nome']} (`{a['sheet']}`) e colar o prompt. 4 variações, 9:16.",
         "- **Vídeo (V):** anexar SÓ a imagem escolhida daquele K e colar o prompt. 1 variação, 9:16.", "", "```text"] + mapa_kv() + [
         "```", "", "## 1. PROMPTS DE IMAGEM (um bloco por K)", ""]
    for k in ks:
        L += [f"### {k['codigo']} · {k['take']}, {k['titulo']} · anexar SÓ o CHARACTER SHEET", "", "```text", k["codigo"], texto_flow(k["j"]), "```", ""]
    L += ["## 2. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · anexar SÓ a imagem escolhida do {kcod}", "", "```text", cod, txt, "```", ""]
    L += ["## 3. Montagem no CapCut", ""] + capcut(a)
    L += ["", "## 4. Transcrição final por take", ""] + transcricao(a)
    L += ["", "## 5. Roteiro final em " + ("espanhol" if es else "inglês"), ""]
    for t in TAKES[1:]:
        L.append(f"{t[1:]}. {fala_do(a, t)}")
    L += ["", " ".join(fala_do(a, t) for t in TAKES[1:]), ""]
    return "\n".join(L)


def ficha():
    L = ["# FICHA DO FRAME · auraly_venda_video_b", "",
         "Regra e método: `GATE_VISUAL.md` Parte 6. Cada K sai daqui. O frame do modelo manda no CONTEÚDO (forma, quadro,",
         "distância, câmera, pose, cenário); o gate manda no ACABAMENTO e no piso de proximidade. Origem avatar IA: bandeira dos EUA",
         "no cenário. Regra do Luigi de 2026-10-06: o frame NÃO é anexado; tudo o que está aqui vai por extenso no K.", ""]
    cena_modelo = ("sala aconchegante, teto claro de bordas anguladas com guirlanda de estrelas douradas e fitas, persiana branca "
                   "horizontal à direita com luz de dia, trepadeira artificial na parede à esquerda, tábua de madeira em mesa de madeira")
    L += ["## K01", "Frame: `input/frames_modelo/K01_modelo.png`",
          "Take: T1 (hook mudo; os cortes seguintes nascem dentro do V01)",
          "Herói: garrafa de uísque âmbar segurada com as duas mãos contra o peito, a mão direita girando a tampa",
          'Termos de forma: "amber glass bottle of whiskey" · "twisting the cap"',
          "Quadro: a garrafa ocupa cerca de 25% do quadro; a tábua com sal, louro e canela fica na borda de baixo",
          "Distância da lente: rosto a uns 36 inches; garrafa a uns 24 inches, mais perto que o rosto (o modelo a tem mais ou menos no plano do peito, o gate pede mais perto)",
          "Câmera: celular apoiado na mesa na altura da mesa, lente 1x, nivelada, fixa com leve tremor de mão",
          "Pose: sentada reta atrás da mesa, torso virado para a lente, sorrindo, começando a abrir a garrafa",
          "Lista fechada: avatar, garrafa de uísque sem rótulo legível, tábua com sal, louro e canela, guirlanda de estrelas, persiana com luz de dia, bandeira",
          "Frame 0: já sorrindo para a lente com a garrafa fechada contra o peito, a mão direita começando a girar a tampa",
          "Desvio (acabamento ou avatar fixo): blusa floral e mulher do modelo viram o avatar do character sheet com a roupa dele; rótulo da marca de uísque do modelo vira rótulo liso sem texto (trava de marca); luz neutra de dia nublado no lugar do tom amarelado (gate); trepadeira artificial do modelo fica de fora para manter 3 âncoras (estrelas, persiana, bandeira); pequena bandeira dos EUA (formato IA); Jordan Vale em sala de jantar de mansão com mesa de mármore (regra do cenário do Jordan); texto de tela só no CapCut",
          f"Cenário do modelo: {cena_modelo}", "", "| Item | Status | Evidência (trecho literal do K) |", "|---|---|---|"]
    k1, k2 = keyframes(AVATARES[0])
    ev1 = [("F1 forma do heroi", '"amber glass bottle of whiskey" · "twisting the cap"'), ("F2 quanto do quadro", '"about 25 percent of the frame"'),
           ("F3 distancia da lente", '"about 24 inches from the lens"'), ("F4 camera", '"1x lens" · "table height"'),
           ("F5 pose do avatar", '"sits upright behind the table"'), ("F6 lista fechada", '"Nothing else is in frame"'),
           ("G1 luz neutra", '"Neutral overcast daylight"'), ("G2 ceu ou janela", '"never white or blown out"'),
           ("G3 foco", '"everything in sharp focus"'), ("G4 realismo", '"Real skin with visible pores"'),
           ("G5 sem tom quente", '"no warm orange color cast"'), ("G6 sem texto", '"no captions"'),
           ("G7 bandeira", '"American flag"'), ("G8 boca no K de fala", '"caught mid-motion"')]
    L += [f"| {a} | OK | {b} |" for a, b in ev1]
    L += ["", "## K02", "Frame: `input/frames_modelo/K02_modelo.png`",
          "Take: T2 a T14 (plano único do modelo depois do gancho, fala direta, sem cortes)",
          "Herói: a chama pequena sobre sal, louro e canela subindo entre as mãos juntas em oração, e o rosto falando",
          'Termos de forma: "small real flame" · "pressed together palm to palm"',
          "Quadro: mãos e chama ocupam cerca de 22% do quadro; o avatar vai da cabeça (a ~8% do topo) até a tábua na borda de baixo",
          "Distância da lente: rosto a uns 36 inches; mãos e chama a uns 24 inches, mais perto que o rosto (o modelo tem as mãos mais ou menos no plano do peito, o gate pede mais perto)",
          "Câmera: celular apoiado na mesa na altura da mesa, lente 1x, nivelada, fixa com leve tremor de mão",
          "Pose: sentada reta atrás da mesa, torso virado para a lente; mãos juntas em oração à altura do peito com a chama entre elas",
          "Lista fechada: avatar, chama sobre sal, louro e canela na tábua, guirlanda de estrelas, persiana com luz de dia, bandeira; nada mais nas mãos",
          "Frame 0: já olhando para a lente com as mãos juntas e a chama de pé entre elas, no meio da frase",
          "Desvio (acabamento ou avatar fixo): blusa floral e mulher do modelo viram o avatar do character sheet com a roupa dele; luz neutra de dia nublado no lugar do tom amarelado (gate); trepadeira artificial do modelo fora (3 âncoras); pequena bandeira dos EUA (formato IA); Jordan Vale em sala de jantar de mansão com mesa de mármore; adesivos 222/444, legenda e setas só no CapCut",
          f"Cenário do modelo: {cena_modelo}", "", "| Item | Status | Evidência (trecho literal do K) |", "|---|---|---|"]
    ev2 = [("F1 forma do heroi", '"small real flame" · "pressed together palm to palm"'), ("F2 quanto do quadro", '"about 22 percent of the frame"'),
           ("F3 distancia da lente", '"about 24 inches from the lens"'), ("F4 camera", '"1x lens" · "table height"'),
           ("F5 pose do avatar", '"sits upright behind the table"'), ("F6 lista fechada", '"Nothing else is held in either hand"'),
           ("G1 luz neutra", '"Neutral overcast daylight"'), ("G2 ceu ou janela", '"never white or blown out"'),
           ("G3 foco", '"everything in sharp focus"'), ("G4 realismo", '"Real skin with visible pores"'),
           ("G5 sem tom quente", '"no warm orange color cast"'), ("G6 sem texto", '"no captions"'),
           ("G7 bandeira", '"American flag"'), ("G8 boca no K de fala", '"caught mid-sentence"')]
    L += [f"| {a} | OK | {b} |" for a, b in ev2]
    return "\n".join(L) + "\n"


AGENTE = """# Agente do Flow, produção atual: Auraly App, venda de prosperidade (vídeo B, ritual do fogo)

Você é o executor do Google Flow. Você só gera imagens e vídeos a partir de prompts prontos. Você não cria, não edita e não melhora prompt.

## Produção atual
- Conta: Auraly App, vídeo de venda sobre prosperidade e dinheiro (auraly_venda_video_b).
- Avatares: Avery Knox, Devon Price e Jordan Vale. Um avatar por vez, o que o operador disser que está ativo. Avery e Devon falam inglês; Jordan Vale fala espanhol (a fala dentro do prompt dele já está em espanhol).
- Cada avatar tem 2 prompts de imagem (K01 e K02) e 14 prompts de vídeo (V01 a V14). V01 usa a imagem escolhida do K01. V02 a V14 usam a imagem escolhida do K02. V01 é mudo.

## O que é anexado (só isto, nada mais)
- IMAGEM (K01 e K02): você recebe o character sheet do avatar ativo. Anexe só ele e cole o prompt.
- VÍDEO (V): você recebe a imagem que o operador escolheu do K correspondente. Anexe só ela e cole o prompt de vídeo.
- Não existe frame modelo, anchor, referência de cenário nem segunda imagem. O cenário, a pose, a câmera e a ação já estão escritos dentro de cada prompt. Pare só se faltar o character sheet (K) ou a imagem escolhida (V).

## Imagem (códigos K01 e K02)
1. Modelo: Nano Banana 2.1 (no menu: Pro, 2 Lite e 2.1; use só o 2.1). Formato: 9:16 vertical.
2. Gere 4 variações por K. Confira o 4 e o 9:16 antes de gerar, porque a tela volta sozinha para 1.
3. Cole o prompt inteiro, de `{` até `}`, sem o código K, sem resumir, sem alterar uma palavra.
4. Nomeie as quatro: `K01-1` a `K01-4` e `K02-1` a `K02-4`.
5. Se saírem menos de 4, ou formato diferente de 9:16, gere de novo com o MESMO prompt e o MESMO character sheet até existirem 4 em 9:16.
6. Gere e PARE. Avise: "K01 pronto, 4 imagens. Aguardando sua escolha." (idem K02). Não escolha, não apague e não gere vídeo.
7. O operador apaga 3 e deixa 1 escolhida a dedo. Nunca questione e nunca recrie uma imagem apagada.

## Vídeos (códigos V01 a V14)
1. Só começa quando o operador mandar. V01 usa a imagem que sobrou do K01; V02 a V14 usam a que sobrou do K02. Se um K tiver mais de uma imagem ou nenhuma, pare e pergunte qual.
2. Modelo: Veo 3.1 - Lite (use só esse). Duração: 8 segundos. Formato: 9:16. Imagem entra como INITIAL FRAME, nunca como ingredient ou elemento.
3. Gere 1 variação por V. Confira o 1 antes de cada V.
4. O campo de texto recebe só o prompt V, inteiro, sem alterar uma palavra. Antes de enviar, confirme que ele contém `o que acontece no vídeo:`, `câmera:` e `som ambiente:`. Se faltar, é prompt de imagem: pare e avise.
5. No máximo 7 V por vez. Terminou o lote, relate e espere o operador dizer `prossiga`.

## Falhou, censura ou bloqueio
- Se a geração falhar, cair na censura, der erro ou o prompt for bloqueado: refaça com o MESMO prompt, sem trocar, cortar ou suavizar uma palavra, e tente de novo até aquele item sair.
- Não pare e não passe para o próximo item sem avisar qual está pendente. Se precisar seguir, diga: "V03 ainda pendente, tentativas: N."
- Você nunca reescreve prompt, mesmo que ache que ajudaria. Só o operador altera.
- Se a interface não permitir 9:16, 4 variações (imagem) ou 1 variação (vídeo), avise antes de mudar qualquer configuração.

## Relatório de status
Depois de cada K ou V, diga: avatar, código, resultado (pronto, tentando de novo, pendente) e quantas tentativas. No fim do lote, liste concluídos e pendentes. Geração de um avatar não conclui a fila: espere o operador dizer qual é o próximo avatar e anexe o novo character sheet. Nunca misture avatares.

## Regras gerais
- Não adicione música, legenda, texto ou tradução.
- A fala do prompt é literal. Não corrija nem complete. No Jordan Vale a fala é em espanhol e assim fica.
- Em caso de dúvida real (pacote incompleto, código duplicado, anexo faltando), pare e pergunte em uma linha.
"""


def main():
    for a in AVATARES:
        p, f = pacote(a)
        (AQUI / f"PROMPTS_{a['arquivo']}.md").write_text(p, encoding="utf-8")
        (AQUI / f"FLOW_{a['arquivo']}.md").write_text(f, encoding="utf-8")
        (AQUI / f"ENTREGA_{a['arquivo']}.md").write_text(entrega(a), encoding="utf-8")
    (AQUI / "FICHA_FRAMES.md").write_text(ficha(), encoding="utf-8")
    (AQUI / "AGENTE_FLOW.md").write_text(AGENTE, encoding="utf-8")
    print("ok: %d avatares" % len(AVATARES))


if __name__ == "__main__":
    main()
