"""Gera os pacotes por avatar da producao auraly_oracao_repetir (Auraly, growth, origem organica, validacao).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Identidade, roupa e
cenario: ROSTER AURALY ATIVO (avatares-fichas) e as ancoras em cena real. Nomes = nomes dos arquivos
que o Luigi enviou (2026-10-04): avery.knox_ (ficha Darlene Pruitt), devon.price_usa (ficha Lorraine Vance),
jordan_vale.us (ficha Walt Hensley) e Morgan Vance; mesmas imagens, conferidas por md5. Medidas: FICHA_FRAMES.md.
Origem organica (PERFIL_ORGANICO.md): celular apoiado na altura do peito olhando levemente para cima,
baralho de taro dourado colado na lente, sem kit obrigatorio, sem carta SOULMATE, primeira linha do V
no tom de conversa de celular. Prompt de imagem em JSON (Flow v17). Mapa K/V como no modelo:
K01 (baralho, T1), K02 (a carta da Roda da Fortuna de pe colada na lente, T2 a T4) e K03 (a mao no
peito para a oracao, T5 a T8; no modelo ela fica parada com a mao no queixo ate o CTA).

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
assert TAKES == ["T%d" % i for i in range(1, 9)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES), FALAS
PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$", ROTEIRO.split("## Tradução completa (Português)")[1].split("\n## ")[0], re.M))
assert set(PT) == set(TAKES), PT

MAPA = {"V01": "K01", "V02": "K02", "V03": "K02", "V04": "K02",
        "V05": "K03", "V06": "K03", "V07": "K03", "V08": "K03"}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
LUZ_INTERNA = ("Neutral overcast daylight from a window, the outside clearly visible through the window, never white or "
               "blown out, soft even light on the face and hands with no harsh shadows.")
LUZ_EXTERNA = ("Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on "
               "the face and hands with no harsh shadows.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra "
            "fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange "
            "color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no lamp glow, no "
            "de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, "
            "no standing pose, no loose cards falling")
BARALHO = ("a gold tarot deck with shiny gold foil card edges and dark antique-gold card backs printed with a fine black "
           "line drawing of a sun and stars")
CARTA = ("the Wheel of Fortune tarot card from the same gold deck: a shiny gold foil card with a metallic gold border "
         "and a saturated illustration of a large orange and red wheel in the center over teal clouds with a red ribbon")

AVATARES = [
    dict(nome="Avery Knox", arquivo="AVERY_KNOX", genero="mulher", pos="her",
         ancora="/Users/macbookairm2/Desktop/AVATARES/avatares appyon/avery.knox_ .jpeg",
         identidade=("The exact fictional AI character Avery Knox: white American woman around fifty-six from Texas, "
                     "voluminous shaggy layered platinum-blonde hair with visible dark roots, brown eyes, fair skin with "
                     "crow's feet and fine lines, everyday makeup with defined brows, mascara and pink lipstick."),
         roupa=("White long-sleeve button-up shirt with the cuffs loosely rolled, blue jeans, a large turquoise and silver "
                "squash-blossom necklace, several big turquoise rings on the fingers of both hands and a silver cuff "
                "bracelet set with turquoise."),
         maos="her fair hands with big turquoise rings on several fingers",
         assento="sits at her wooden kitchen island",
         apoio="propped on the wooden kitchen island",
         cena=("Her own rustic American kitchen with knotty pine wood-paneled walls, the same lived-in kitchen as the "
               "reference, unchanged. She sits at her wooden kitchen island; behind her the pine wall with a framed "
               "astrological chart and a small wooden crucifix, and the open wooden shelves by the window with glass jars "
               "and a small American flag, discreet but visible and in focus."),
         luz=LUZ_INTERNA, sotaque="texano carregado",
         voz="voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos",
         som="cozinha residencial silenciosa"),
    dict(nome="Devon Price", arquivo="DEVON_PRICE", genero="mulher", pos="her",
         ancora="/Users/macbookairm2/Desktop/AVATARES/avatares appyon/devon.price_usa .jpeg",
         identidade=("The exact fictional AI character Devon Price: white American woman around fifty-two, closely "
                     "shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, "
                     "defined jaw, fine lines and no makeup."),
         roupa=("Light-wash denim shirt worn open over a fitted black crew-neck T-shirt, dark jeans, large silver hoop "
                "earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar."),
         maos="her freckled fair hands with bare fingers",
         assento="sits at her white quartz counter",
         apoio="propped on the white quartz counter",
         cena=("Her own bright white American kitchen, the same lived-in kitchen as the reference, unchanged. She sits at "
               "her white quartz counter; behind her the light wood floating shelves with clear quartz crystal points, a "
               "white pillar candle and a small American flag, discreet but visible and in focus, and a window at the left "
               "with the street clearly visible."),
         luz=LUZ_INTERNA, sotaque="de Chicago",
         voz="voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago",
         som="cozinha residencial silenciosa"),
    dict(nome="Jordan Vale", arquivo="JORDAN_VALE", genero="homem", pos="his",
         ancora="/Users/macbookairm2/Desktop/AVATARES/avatares appyon/jordan_vale.us .jpeg",
         identidade=("The exact fictional AI character Jordan Vale, explicitly male: white American man around fifty-eight, "
                     "long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, "
                     "sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded "
                     "traditional American tattoos with no lettering, a swallow and a red rose on the left forearm."),
         roupa="Black leather vest over a heather grey crew-neck T-shirt and dark blue jeans.",
         maos="his weathered hands with faded tattoos on the forearms",
         assento="sits in his old wooden rocking chair",
         apoio="propped on the small wooden side table",
         cena=("His own American front porch with grey weathered wooden siding, the same lived-in porch as the reference, "
               "unchanged. He sits in his old wooden rocking chair; behind him the siding with the framed astrological "
               "chart and a small wooden crucifix, and at the right a small American flag on the porch post against the "
               "overcast sky, discreet but visible and in focus."),
         luz=LUZ_EXTERNA, sotaque="do Tennessee",
         voz="voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee",
         som="varanda tranquila, leve vento e passarinhos ao longe"),
    dict(nome="Morgan Vance", arquivo="MORGAN_VANCE", genero="mulher", pos="her",
         ancora="/Users/macbookairm2/Desktop/AVATARES/avatares appyon/Morgan Vance.jpg",
         identidade=("The exact fictional AI character Morgan Vance: Black American woman around twenty-five, long knotless "
                     "box braids down to the waist with a middle part and a few small gold cuffs in the braids, neat baby "
                     "hairs, dark brown skin with real texture, visible pores and acne marks on the forehead and cheeks, "
                     "dark brown eyes, long lashes, defined brows, glossy lips, a small gold hoop in her nostril and small "
                     "gold earrings."),
         roupa=("Cobalt blue ribbed long-sleeve top with a scoop neckline and a thin gold chain necklace with a small gold "
                "heart pendant."),
         maos="her dark brown hands with short natural nails",
         assento="sits on the edge of her bed",
         apoio="propped on a small stand in front of her bed",
         cena=("Her own bright white American bedroom with a sloped ceiling, the same lived-in room as the reference, "
               "unchanged. She sits on the edge of her bed; behind her the white wall with a large American flag pinned "
               "up with grommets, in focus, a window at the left with the white blind raised and trees outside on an "
               "overcast day, and a white dresser at the right with a clear quartz crystal point on a wooden base and a "
               "short stack of books."),
         luz=LUZ_INTERNA, sotaque="leve de Atlanta",
         voz="voz feminina média e jovem, confiante e direta, de uma mulher de vinte e cinco anos de Atlanta",
         som="quarto silencioso"),
]

EMOCAO = {
    "T1": "calma e direta, como quem dá uma ordem baixinha", "T2": "animada e segura",
    "T3": "em voz mais baixa, quase em segredo", "T4": "calorosa e convidativa",
    "T5": "devagar e sincera, a voz um pouco mais baixa, com uma pausa curta no fim de cada frase, como numa oração",
    "T6": "devagar e serena, a voz um pouco mais baixa, com uma pausa curta no fim de cada frase, como numa oração",
    "T7": "sorridente e leve", "T8": "próxima e animada",
}
MASC = {"calma": "calmo", "direta": "direto", "animada": "animado", "segura": "seguro", "calorosa": "caloroso",
        "convidativa": "convidativo", "sincera": "sincero", "serena": "sereno", "sorridente": "sorridente",
        "próxima": "próximo"}
ACAO = {
    "T1": ("{n} segura o baralho de tarô dourado com as duas mãos perto da lente, passa algumas cartas de uma mão para "
           "a outra, puxa uma única carta e a ergue de pé, colada na lente, com a face virada para a câmera, e levanta "
           "o olhar para a lente enquanto fala."),
    "T2": ("{n} segura a carta dourada de pé, colada na lente, com uma mão e, em \"not random\", ergue o dedo "
           "indicador da outra mão."),
    "T3": ("{n} segura a carta dourada de pé na frente do peito com uma mão e gesticula de leve com a outra mão."),
    "T4": ("{n} baixa a carta dourada para a borda do quadro e abre a outra mão para a lente, convidando, enquanto "
           "fala."),
    "T5": ("{n} mantém a mão espalmada sobre o coração, a carta baixa na outra mão, e fala devagar olhando para a "
           "lente."),
    "T6": ("{n} mantém a mão espalmada sobre o coração e fala devagar olhando para a lente; na última frase fecha os "
           "olhos por um instante e abre de novo."),
    "T7": ("{n} tira a mão do peito, sorri, junta o polegar e o indicador num gesto leve e ergue o dedo indicador em "
           "\"seven days\"."),
    "T8": ("{n} sorri, aponta de leve para baixo da tela em \"Comment 222\" e, no fim, ergue a carta dourada para a "
           "lente."),
}


def camera(a):
    return (f"phone {a['apoio']} at chest height about two feet away, 1x front lens, straight on, pointing slightly "
            f"upward, fixed")


def keyframes(a):
    n, p = a["nome"], a["pos"]
    base = {
        "fiction_note": FICCAO,
        "reference_use": (f"Use the first attached image only for {n}'s exact identity, wardrobe, jewelry and own setting. "
                          f"Use the second attached image only as a composition reference for the camera position, framing "
                          f"and hand position; do not copy its person, clothes, sofa, wall or on-screen text."),
        "identity_main": a["identidade"],
        "wardrobe": a["roupa"],
        "scene": a["cena"],
        "camera": camera(a),
        "lighting": a["luz"],
        "realism": REALISMO,
        "aspect_ratio": "9:16 vertical",
    }
    quadro = (f"{p.capitalize()} face sits in the upper middle of the frame with a little headroom, {p} chest in the "
              f"middle, the setting behind in the top third, framed from the top of the head to the waist. Nothing "
              f"else is in the foreground. The background is reduced by framing, never by blur.")
    k1 = dict(base, shot_id=f"K01_{a['arquivo'].lower()}")
    k1.update({
        "prop": (f"The only object is {BARALHO}, in {a['maos']}, caught mid-pass: most of the deck held in one hand with "
                 f"the gold foil card edges toward the lens and a small packet of cards lifted off the top by the other "
                 f"hand; only the card backs are visible."),
        "posture": (f"{n} {a['assento']}, facing the lens, both forearms raised in front of {p} body, passing the tarot "
                    f"cards right in front of the phone."),
        "composition": (f"The hands and the gold tarot deck are in the bottom center of the frame, pushed toward the lens, "
                        f"about 14 inches from the lens, taking up about 30 percent of the frame and touching the bottom "
                        f"edge, closer to the camera than {p} face, nothing else competing with them. " + quadro),
        "state": (f"Start frame: {n} glances down at the deck, caught mid-sentence, lips naturally parted, calm and "
                  f"focused expression, the hands in motion."),
        "negative": NEG_BASE + ", no card faces showing, no other objects in the hands",
    })
    k2 = dict(base, shot_id=f"K02_{a['arquivo'].lower()}")
    k2.update({
        "prop": (f"The only object is {CARTA}, in one of {a['maos']}, held upright by its top corner between the thumb "
                 f"and fingers, the illustrated face turned straight to the lens; the other hand rests out of frame and "
                 f"the rest of the deck is out of frame."),
        "posture": (f"{n} {a['assento']}, facing the lens, one forearm raised, holding the card up in front of {p} chest, "
                    f"looking straight into the lens."),
        "composition": (f"The card and the hand holding it are in the lower center of the frame, pushed toward the lens, "
                        f"about 12 inches from the lens, taking up about 25 percent of the frame, the bottom of the card "
                        f"near the bottom edge, closer to the camera than {p} face, nothing else competing with it. "
                        + quadro),
        "state": (f"Start frame: {n} looks straight into the lens, caught mid-sentence, lips naturally parted, bright and "
                  f"confident expression."),
        "negative": NEG_BASE + ", no second card, no other cards in frame, no other objects in the hands",
    })
    k3 = dict(base, shot_id=f"K03_{a['arquivo'].lower()}")
    k3.update({
        "prop": (f"In {a['maos']}: one hand pressed flat over {p} heart on the chest, fingers relaxed; the other hand "
                 f"holds the gold Wheel of Fortune card low at the right edge of the frame, partly cut off by the frame "
                 f"edge. The card is {CARTA}."),
        "posture": (f"{n} {a['assento']}, facing the lens, upright and still, one hand pressed flat over {p} heart, "
                    f"looking softly into the lens."),
        "composition": (f"The hand pressed flat over the heart is in the center of the frame on the chest, about 20 inches "
                        f"from the lens, taking up about 10 percent of the frame, closer to the camera than {p} face; the "
                        f"card is only a sliver at the right edge, partly cut off by the frame edge. " + quadro),
        "state": (f"Start frame: {n} looks softly into the lens, caught mid-sentence, lips naturally parted, calm and "
                  f"sincere expression, as if saying a prayer."),
        "negative": NEG_BASE + ", no phone screen overlay, no app interface, no other objects in the hands",
    })
    return [dict(codigo="K01", take="T1", titulo="baralho de tarô dourado nas duas mãos colado na lente", j=k1),
            dict(codigo="K02", take="T2 a T4", titulo="a carta da Roda da Fortuna de pé colada na lente", j=k2),
            dict(codigo="K03", take="T5 a T8", titulo="a mão espalmada no coração, a carta na borda do quadro", j=k3)]


def emocao(t, homem):
    e = EMOCAO[t]
    return re.sub(r"\w+", lambda m: MASC.get(m.group(0), m.group(0)), e) if homem else e


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art = "o avatar" if h else "a avatar"
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        txt = (f"{art} {n} ({a['genero']}) fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, em tom de "
               f"conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, "
               f"{emocao(t, h)}, no mesmo ritmo do vídeo modelo, a seguinte frase: \"{FALAS[t]}\"\n\n"
               f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
               f"sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
               f"o que acontece no vídeo: {ACAO[t].format(n=n)}\n\n"
               "câmera: celular apoiado na altura do peito, fixo, sem movimento\n\n"
               f"som ambiente: {a['som']}, sem música")
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
        "1. Clipes numerados na ordem: V01 a V08.",
        "2. Zero tempo morto: todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / "
        "Keep Vocal no áudio. V02 a V04 saem do K02 e V05 a V08 do K03, então a troca de clipe vira jump cut no mesmo "
        "enquadramento, a gramática do próprio formato orgânico.",
        "3. Tarja branca fixa no topo, do V01 ao V08: \"💫 you are about to have THE BEST OCTOBER of your life 💫\".",
        "4. Legenda branca pequena no meio de baixo, a fala inteira, do V01 ao V08, igual ao modelo.",
        "5. No V05 e no V06 (a oração), um cartão escuro translúcido no centro do peito, no lugar do print do app do "
        "modelo, com as linhas da oração em serifa branca e a linha que está sendo falada em destaque, para quem "
        "assiste ler e repetir junto. Sem nome nem ícone de app.",
        "6. Sem Voice Changer: a voz vem do prompt de cada V.",
        "7. Música só depois do gancho (a partir do V02), baixa, entre -19 e -20 dB, fora da biblioteca do TikTok; "
        "baixar mais ainda na oração (V05 e V06) para a voz ficar na frente.",
        "8. Rótulo pequeno `AI-generated` num canto do vídeo.",
        "9. Postar em outubro de 2026: \"the best October\" está na fala e na tarja.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {PT[t]} |")
    return L


INDICE = [("T1", "K01"), ("T2 a T4", "K02"), ("T5 a T8", "K03")]


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    up = a["nome"].upper()
    L = [f"# {a['nome']} | Auraly Oração Repetir | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `producao/auraly_oracao_repetir/input/modelo.mp4` (41,4 s, pessoa real)", "",
         f"Âncora: `{a['ancora']}`", "",
         "Funil: growth, save + voltar em 7 dias + `222` + follow. Origem orgânica, rodada de validação.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    L += [f"| {t} | {k} | ÂNCORA {up} + FRAME DO MODELO ({k}) | GERAR DO ZERO |" for t, k in INDICE]
    L += ["", "## Trava de identidade e continuidade", "",
          f"- Identidade: {a['identidade']}", f"- Roupa (fixa da conta): {a['roupa']}",
          f"- Cenário-base (fixo da conta): {a['cena']}", f"- Luz: {a['luz']}",
          f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.", "- Sem 2ª pessoa.", "",
          "## Trava do prop herói", "", f"- O baralho: {BARALHO}.", f"- A carta: {CARTA}. Igual no K02 e no K03.", "",
          "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "", "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · ÂNCORA {up} + FRAME DO MODELO", "",
              "> ### 📎 ANEXAR: **2 IMAGENS**", f"> **1️⃣ ÂNCORA {up}** `{a['ancora']}`",
              f"> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/{k['codigo']}_modelo.png`", ">",
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


CHECKLIST = ("Checklist de envio: 33/33 aprovados (N/A: A1, A2, A4, A7, A10 fiéis ao modelo orgânico; C3 sem segunda "
             "pessoa; C4 celular apoiado, sem selfie na mão; C6 sem cena atuada; C7 sem motion control)")
FICHA = "Ficha: 3/3 K conferidos contra o frame do modelo, placar 14/14 em cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)"


def entrega(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Oração Repetir", "",
         "Produção `auraly_oracao_repetir` · Ângulo 3 · GROWTH · vídeo modelo de pessoa real (orgânico) · rodada de VALIDAÇÃO · perfil AURALY", "",
         f"## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v{VERSAO})", "",
         "Colar inteiro na memória do agente antes do primeiro K.", "", "```text", BLOCO_FLOW, "```", "",
         CHECKLIST, "", FICHA, "", "## Anexos e mapa", "",
         f"- **Âncora {a['nome']}:** `{a['ancora']}` no K01, no K02 e no K03.",
         "- Em cada K, anexar também o frame do modelo do mesmo código (`input/frames_modelo/K01_modelo.png`, "
         "`K02_modelo.png`, `K03_modelo.png`), só como composição.",
         "", "```text"] + mapa_kv() + ["```", "", "## 2. PROMPTS DE IMAGEM", ""]
    for k in ks:
        L += [f"### {k['codigo']} · {k['take']}, {k['titulo']} · anexar ÂNCORA + FRAME DO MODELO", "",
              "```text", k["codigo"], texto_flow(k["j"]), "```", ""]
    L += ["## 3. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · frame inicial = a imagem escolhida do {kcod}", "", "```text", cod, txt, "```", ""]
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
    print("ok: %d avatares, Flow v%s" % (len(AVATARES), VERSAO))


if __name__ == "__main__":
    main()
