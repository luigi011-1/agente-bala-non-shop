"""Gera os pacotes por avatar da producao auraly_venda_prosperidade_v1 (Auraly, SALE, dinheiro e prosperidade,
avatar IA, validacao, plano unico de fala numa sala de luxo).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Identidade e roupa: os CHARACTER
SHEETS (producao/_ancoras/character_sheets/). Cenario e angulo de camera: os do VIDEO MODELO (FICHA_FRAMES.md).
Anexos (Luigi, 2026-10-06): K = so o character sheet; V = so a imagem escolhida do K. Prompt de imagem em JSON.
Mapa K/V: K01 -> V01 a V15 (plano unico).

Saidas por avatar: PROMPTS_<AVATAR>.md, FLOW_<AVATAR>.md e ENTREGA_<AVATAR>.md. Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")

HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 16)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES), FALAS.keys()
PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$", ROTEIRO.split("## Tradução completa (Português)")[1].split("\n## ")[0], re.M))
assert set(PT) == set(TAKES), PT

MAPA = {"V%02d" % i: "K01" for i in range(1, 16)}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
BANDEIRA = "a small American flag (discreet but visible and in focus)"
CENA_MODELO = (
    "The luxurious American living room of the reference video: on the left a tall arched window with a dark steel frame "
    "looking out over a pale-stone hillside town and a tall dark-green cypress tree under a clear blue sky with soft white "
    "clouds, with green potted palms in front of the window; behind the person on the right a built-in dark wooden bookcase "
    "full of closed hardcover books with blank spines; the edge of a cream sofa with a gold cushion at the far left and a "
    "patterned Persian rug on the floor. In the lower right foreground stands a polished dark-wood console table with carved "
    "gilded legs; on it a gold embossed planter holds a green leafy plant with " + BANDEIRA + " tucked into the soil, next to "
    "a stack of two closed hardcover books with blank spines.")
CENA_JORDAN = (
    "The grand salon of a luxury mansion, the reference video's living room made grander: on the left a floor-to-ceiling "
    "arched window with a dark steel frame looking out over a manicured estate garden with a tall dark-green cypress and a "
    "stone fountain under a clear blue sky with soft white clouds, with tall green potted palms in front of the window; behind "
    "the person on the right a floor-to-ceiling built-in dark wooden bookcase with a rolling library ladder, full of closed "
    "hardcover books with blank spines; polished cream marble floor with an inlaid patterned border and the edge of a cream "
    "silk sofa with a gold cushion at the far left. In the lower right foreground stands a polished dark-wood console "
    "table with a cream marble top and carved gilded legs; on it a large gold embossed planter shaped like an urn holds a green leafy plant with " + BANDEIRA + " tucked into "
    "the soil, next to a stack of two closed hardcover books with blank spines.")
LUZ = ("Neutral overcast daylight coming in from the arched window on the left, cool and even, the sky outside a clear blue "
       "with soft white cloud texture, never white or blown out, the lamps switched off, soft even light on the face and body "
       "with no harsh shadows.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no letters or writing anywhere in the room, no studio, "
       "no grey studio background, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no "
       "supernatural lighting, no glowing objects, no blur, no bokeh, no artificial lighting, no warm orange color cast, no "
       "yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no "
       "visible phone, no HDR, no cinematic lighting, no second person in frame, no religious symbols, no framed text on "
       "the wall, no candles, no tarot cards")
CAMERA = ("phone fixed on a tripod at chest height about 4.5 feet above the floor, about 5 feet from the person, 1x lens, "
          "pointing level, fixed")

AVATARES = [
    dict(nome="Avery Knox", arquivo="AVERY_KNOX", genero="mulher", pos="her", cena=CENA_MODELO,
         sheet="producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg",
         identidade=("The exact fictional AI character Avery Knox: white American woman around sixty, voluminous shaggy "
                     "layered platinum-blonde hair with visible darker roots, brown eyes, fair skin with crow's feet and "
                     "fine lines, everyday makeup with defined brows, mascara and pink lipstick."),
         roupa=("White long-sleeve button-up shirt with a chest pocket and the cuffs rolled, medium-blue bootcut jeans, a "
                "large turquoise and silver squash-blossom necklace, several big turquoise rings and silver cuff bracelets "
                "set with turquoise on both wrists."),
         maos="her fair hands with big turquoise rings",
         sotaque="texano carregado",
         voz="voz feminina média, levemente rouca e calorosa de uma texana de sessenta anos"),
    dict(nome="Jordan Vale", arquivo="JORDAN_VALE", genero="homem", pos="his", cena=CENA_JORDAN,
         sheet="producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg",
         identidade=("The exact fictional AI character Jordan Vale, explicitly male: white American man around "
                     "sixty-eight, slim, full silver-white hair swept back, round thin gold-rimmed glasses, light blue-grey "
                     "eyes, fair skin with freckles, age spots and deep forehead lines, light grey stubble."),
         roupa=("Cream dinner jacket with peak lapels over a white dress shirt with a black bow tie, black tuxedo trousers, "
                "a gold wristwatch on the left wrist and a gold ring on the left hand."),
         maos="his slim, freckled hand with a gold ring",
         sotaque="refinado da Costa Leste",
         voz="voz masculina grave, polida e calma de um homem rico de sessenta e oito anos"),
    dict(nome="Devon Price", arquivo="DEVON_PRICE", genero="mulher", pos="her", cena=CENA_MODELO,
         sheet="producao/_ancoras/character_sheets/devon_price_character_sheet.jpg",
         identidade=("The exact fictional AI character Devon Price: white American woman around fifty, completely bald "
                     "with a smooth bare scalp, hazel eyes, freckles and fine lines, no makeup, small silver stud earrings."),
         roupa=("Cream lace blazer with three-quarter sleeves over a cream lace camisole, a thin silver chain necklace with a "
                "small heart pendant, a rose-gold beaded bracelet and silver rings, dark blue skinny jeans."),
         maos="her freckled hand with silver rings",
         sotaque="de Chicago",
         voz="voz feminina grave, direta e de humor seco de uma mulher de cinquenta anos de Chicago"),
]

TOM = {
    "T1": "firme e protetor", "T2": "confessional e baixo", "T3": "sério e comovido", "T4": "reflexivo e honesto",
    "T5": "revelador e calmo", "T6": "caloroso e sereno", "T7": "caloroso e sereno", "T8": "sereno e acolhedor",
    "T9": "baixo, de segredo", "T10": "calmo e didático", "T11": "solene e firme", "T12": "aliviado e carinhoso",
    "T13": "firme e direto", "T14": "sério e urgente", "T15": "acolhedor e próximo",
}
ACAO = {
    "T1": "{n} fala olhando fixo para a lente e ergue o indicador da mão direita, apontando para a lente na frase 'don't sell it'.",
    "T2": "{n} balança a cabeça de leve, como quem se arrepende, olhando para a lente.",
    "T3": "{n} fala olhando para a lente, com um pequeno aceno de cabeça no fim de cada frase curta.",
    "T4": "{n} faz uma pausa curta antes de 'I couldn't answer' e depois olha para a lente com firmeza.",
    "T5": "{n} abre a mão direita com a palma para cima e depois aponta para baixo, como quem mostra a casa.",
    "T6": "{n} ergue um dedo da mão direita na primeira frase, o sinal um.",
    "T7": "{n} ergue dois dedos da mão direita na primeira frase, o sinal dois.",
    "T8": "{n} ergue três dedos da mão direita na primeira frase, o sinal três.",
    "T9": "{n} se inclina um pouco para a lente e baixa a voz no segredo, com o indicador da mão direita levantado.",
    "T10": "{n} desenha no ar uma linha descendente com a mão direita, como a água escorrendo, enquanto fala.",
    "T11": "{n} fala devagar, olhando fixo para a lente, e fecha a mão direita em punho solto no peito na última frase.",
    "T12": "{n} sorri de leve ao falar de Loretta e depois fica sério na última frase.",
    "T13": "{n} aponta para baixo, para os comentários, e depois para a lente.",
    "T14": "{n} fala olhando para a lente, a mão direita no peito, e ergue o dedo ao dizer 'Follow me'.",
    "T15": "{n} se inclina um pouco para a lente e aponta para ela com a mão direita, sorrindo de leve no 'Blessings, my friend'.",
}


def keyframe(a):
    n, p = a["nome"], a["pos"]
    ref = (f"Use the attached character sheet only for {n}'s exact identity (face, skin, hair, body) and wardrobe; ignore "
           f"its grey studio background. The setting, camera angle, pose and framing are described in full in the scene, "
           f"camera and composition fields; no other image is attached.")
    j = {
        "fiction_note": FICCAO, "reference_use": ref, "identity_main": a["identidade"], "wardrobe": a["roupa"],
        "scene": a["cena"],
        "prop": (f"Nothing is held in either hand. The left hand of {n}, {a['maos']}, rests flat on the polished top of "
                 f"the console table beside the gold planter."),
        "posture": (f"{n} stands upright and relaxed, slightly left of center, facing the lens, the right hand raised in a loose fist at chest height (on the viewer's "
                    f"left), the left hand resting flat on the console table (on the viewer's right), looking "
                    f"straight into the lens."),
        "composition": (f"The polished console table is very close to the lens in the lower right foreground, its near end about "
                        f"28 inches from the lens, about 20 percent of the frame, closer to the camera than {p} face, nothing "
                        f"else competing with it. {n} stands about 4 feet behind it, framed from the top of the head (about 12 "
                        f"percent from the top edge) to mid-thigh, {p} face in the upper third, about 5 feet from the lens. "
                        f"Nothing else is in the foreground. The background is reduced by framing, never by blur."),
        "camera": CAMERA, "lighting": LUZ,
        "state": f"Start frame: {n} caught mid-sentence, lips naturally parted, calm confident expression, the fist at the chest held still.",
        "realism": REALISMO, "aspect_ratio": "9:16 vertical",
        "negative": NEG + ", no hand holding anything, no shoes visible, no text on the books",
    }
    return j


def texto_flow(j):
    ordem = ["fiction_note", "reference_use", "identity_main", "wardrobe", "scene", "prop", "posture",
             "composition", "camera", "lighting", "state", "realism", "aspect_ratio", "negative"]
    assert set(ordem) == set(j), set(j) ^ set(ordem)
    d = {"format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."}
    d.update({k: j[k] for k in ordem})
    return json.dumps(d, ensure_ascii=False, indent=2)


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art = "o avatar" if h else "a avatar"
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        txt = (f"{art} {n} ({a['genero']}) fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, em tom {TOM[t]}, "
               f"voz autêntica, dinâmica e emocional, a seguinte frase: \"{FALAS[t]}\"\n\n"
               f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem "
               f"cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
               f"o que acontece no vídeo: {ACAO[t].format(n=n)} A mão esquerda continua apoiada na console e a sala atrás não muda.\n\n"
               "câmera: fixa, sem movimento\n\n"
               "som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música")
        vs.append((cod, t, MAPA[cod], txt))
    return vs


def mapa_kv():
    return ["MAPA K/V"] + [f"{v}: {k}" for v, k in MAPA.items()]


def capcut():
    return [
        "1. Clipes numerados na ordem: V01 a V15.",
        "2. Zero tempo morto: todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / Keep Vocal. "
        "Todos saem do mesmo frame (K01), então a troca de clipe fica no mesmo enquadramento, como no modelo (plano único).",
        "3. Legenda karaokê branca em caixa alta com contorno preto, uma palavra por vez, no centro-baixo do quadro, do V01 ao V15, como o modelo.",
        "4. Texto de tela do gancho no V01 (CapCut, nunca no K): \"These three signs? Don't even think about moving.\"",
        "5. No V15, seta apontando para a foto de perfil.",
        "6. Sem Voice Changer: a voz vem do prompt de cada V.",
        "7. Som ambiente baixo, sem música por baixo da fala.",
        "8. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {PT[t]} |")
    return L


def pacote(a):
    j = keyframe(a)
    vs = videos(a)
    up = a["nome"].upper()
    L = [f"# {a['nome']} | Auraly Venda Prosperidade v1 | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `producao/auraly_venda_prosperidade_v1/input/modelo.mp4` (103,4 s, avatar IA)", "",
         f"Character sheet: `{a['sheet']}`", "",
         "Funil: SALE, `222` no T13, curtir e salvar no T14, follow no T14, Stories no T15. Rodada de validação, cenário e ângulo do modelo.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|",
         f"| T1 a T15 | K01 | SÓ O CHARACTER SHEET {up} | GERAR DO ZERO |", "",
         "## Trava de identidade e continuidade", "",
         f"- Identidade (character sheet): {a['identidade']}", f"- Roupa (character sheet): {a['roupa']}",
         f"- Cenário (do vídeo modelo): {a['cena']}", f"- Luz: {LUZ}",
         f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.", "- Sem 2ª pessoa.", "",
         "## Trava do prop herói", "", "- A console de madeira polida com o vaso dourado, sempre em primeiro plano à direita.", "",
         "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "",
         "## Prompts de imagem", "",
         f"## K01 · T1 a T15 · GERAR DO ZERO · SÓ O CHARACTER SHEET {up}", "",
         "> ### 📎 ANEXAR: **1 IMAGEM**", f"> **1️⃣ CHARACTER SHEET {up}** `{a['sheet']}`", ">",
         "> ### 🆕 GERAR DO ZERO", "", "Cena: o avatar de pé numa sala de luxo, mão esquerda na console, falando para a lente.", "",
         "```json", json.dumps({"shot_id": f"k01_{a['arquivo'].lower()}", **j}, ensure_ascii=False, indent=2), "```", "",
         "# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Montagem no CapCut", ""] + capcut() + [""]
    flow = [f"# Blocos limpos para o Google Flow | {a['nome']}", "", f"Fonte interna: `PROMPTS_{a['arquivo']}.md`", "",
            "```text"] + mapa_kv() + ["```", "", "## BLOCO DE IMAGEM", "", "```text", "K01", texto_flow(j), "", "```", "",
            "## BLOCO DE VÍDEO", "", "```text"]
    for cod, _, _, txt in vs:
        flow += [cod, txt, ""]
    flow += ["```", "", "## Transcrição final por take", ""] + transcricao()
    return "\n".join(L) + "\n", "\n".join(flow) + "\n"


CHECKLIST = ("Checklist de envio: 32/32 aprovados (N/A: A1 a A4 e A10 fiéis ao modelo, hook fiel da validação; C3 a C7 sem "
             "segunda pessoa, selfie, frase curta repetida, cena atuada ou motion control)")
FICHA = "Ficha: 1/1 K conferido contra o frame do modelo, placar 14/14 (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)"
AGENTE = (AQUI / "AGENTE_FLOW.md").read_text(encoding="utf-8") if (AQUI / "AGENTE_FLOW.md").exists() else ""


def entrega(a):
    j = keyframe(a)
    vs = videos(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Venda Prosperidade v1 (SALE)", "",
         "Produção `auraly_venda_prosperidade_v1` · Ângulo 3 · SALE (dinheiro e prosperidade) · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY", "",
         "## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI", "",
         "Colar inteiro na memória do agente antes do K01 (versão só desta produção: `AGENTE_FLOW.md`).", "", "```text",
         AGENTE.rstrip(), "```", "", CHECKLIST, "", FICHA, "", "## Anexos e mapa", "",
         f"- **Imagem (K01):** anexar SÓ o character sheet de {a['nome']} (`{a['sheet']}`) e colar o prompt. 4 variações, 9:16.",
         "- **Vídeo (V):** anexar SÓ a imagem escolhida do K01 e colar o prompt. 1 variação, 9:16.", "", "```text"] + mapa_kv() + ["```", "",
         "## 2. PROMPT DE IMAGEM", "", "### K01 · T1 a T15 · anexar SÓ o CHARACTER SHEET", "", "```text", "K01", texto_flow(j), "```", "",
         "## 3. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · anexar SÓ a imagem escolhida do {kcod}", "", "```text", cod, txt, "```", ""]
    L += ["## 4. Montagem no CapCut", ""] + capcut()
    L += ["", "## 5. Transcrição final por take", ""] + transcricao()
    L += ["", "## 6. Roteiro final em inglês", ""]
    for i, t in enumerate(TAKES, 1):
        L.append(f"{i}. {FALAS[t]}")
    L += ["", " ".join(FALAS[t] for t in TAKES), ""]
    return "\n".join(L)


def main():
    for a in AVATARES:
        p, f = pacote(a)
        (AQUI / f"PROMPTS_{a['arquivo']}.md").write_text(p, encoding="utf-8")
        (AQUI / f"FLOW_{a['arquivo']}.md").write_text(f, encoding="utf-8")
        (AQUI / f"ENTREGA_{a['arquivo']}.md").write_text(entrega(a), encoding="utf-8")
    print("ok: %d avatares" % len(AVATARES))


if __name__ == "__main__":
    main()
