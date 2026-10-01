"""Gera os pacotes por avatar da producao fitywell_growth_modelo_intestino (avatar IA, growth, validacao).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Nenhuma fala muda por
avatar. Identidade, roupa e cenario: as fichas de fitywell_growth_froyo_bites (2026-09-25), com as
ancoras desta producao, que sao os mesmos arquivos (md5 identico).

Prompt de imagem entregue em JSON (Luigi, 2026-09-25, contrato do Flow v17).

Saidas: PROMPTS_<AVATAR>.md (fonte interna com JSON), FLOW_<AVATAR>.md (blocos limpos do Flow)
e PROMPTS_PRODUCAO.md (copia do avatar ACTIVE, que e o que o checar_entrega.py le).

Uso: python3 gerar_pacote.py [NOME_DO_ATIVO]   (padrao: o ACTIVE do AVATAR_QUEUE.md)
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")

HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 14)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES), FALAS
CURTAS = {t for t in TAKES if "CENA CURTA" in HEADS[t]}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."


def frame_modelo(cod):
    return f"input/frames_modelo/{cod}_modelo.png"


LUZ_INTERNA = ("Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, "
               "soft even light on the face and hands with no harsh shadows.")
LUZ_EXTERNA = ("Overcast sky with visible cloud texture, never white or blown out, neutral daylight, "
               "soft even light on the face and hands with no harsh shadows.")

REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")

NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any bottle, "
            "jar or package, no studio, no plastic-looking human skin, no extra fingers, no third hand, "
            "no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, "
            "no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, "
            "no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame")
NEG_HOOK = (", no real human body, no simple zigzag tube, no single folded hose, no small toy-sized model, "
            "no model standing far from the camera, no items lying on the counter, no clean clear tube yet")
NEG_CORPO = ", no teaching model in frame"

MODELO = ("A large hollow clear transparent plastic anatomical teaching model shaped exactly like the complete "
          "human intestinal tract seen from the front, about as tall as a man's torso: a thick bulging outer tube with "
          "rounded pouch-like segments frames the left side, the top and the right side like an upside-down U; a dense "
          "tangle of narrower winding loops fills the whole middle; a short straight clear funnel neck opens at the top "
          "center; and a short straight clear tube drops out of the bottom center down to {sup}. Every tube and loop is "
          "packed full of lumpy, knobby, dark brown and caramel-brown compacted matter with visible chunks and small air "
          "bubbles pressed against the clear plastic, so the whole shape reads brown, with only thin clear gaps between "
          "the loops. It is clearly a classroom teaching model made of clear plastic.")
PANELA = ("a clear glass cooking pot of boiling water on a small single-burner electric hot plate, standing on {sup}")
COPO = "a tall clear glass full of warm golden-amber lemon and turmeric tea with a few chia seeds floating in it"

AVATARES = [
    dict(nome="Eva Dall", cena_hook="His own modern white kitchen seen from a very low angle at counter level: the dark green veined marble counter under the model, and behind him the white ceiling with recessed lights, the tall bright windows and the small American flag on the shelf beside a small plant.", arquivo="EVA_DALL", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/01_eva_dall.jpg",
         identidade="The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
         roupa="White ribbed tank top and a thin silver chain.",
         maos="his medium brown hands and bare forearms",
         cena="His own modern white kitchen with a strongly veined dark green marble counter in front of him, tall windows to the right and a small American flag on the shelf beside a small plant.",
         superficie="his dark green veined marble counter",
         postura="standing behind his counter, leaning slightly toward the camera",
         luz=LUZ_INTERNA, sotaque="de um homem negro americano",
         voz="voz média e amigável de um homem de quase cinquenta anos", som="cozinha residencial tranquila"),
    dict(nome="Ivy Carl", cena_hook="His own covered American backyard veranda seen from a very low angle at table level: the weathered wooden table under the model, and behind him the beige veranda ceiling with a recessed light, the black-framed glass door with the small American flag and a glimpse of turquoise pool.", arquivo="IVY_CARL", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/02_ivy_carl.jpg",
         identidade="The exact fictional AI character Ivy Carl, explicitly male: Black American man around twenty-eight, dark brown skin, lean athletic build, long oval face, very light grey-hazel eyes, fine black braids beneath a plain black cap and a short goatee.",
         roupa="Plain black cap, fitted black long-sleeve athletic shirt, black trousers and small silver stud earrings.",
         maos="his dark brown hands with the black athletic sleeves at the wrists",
         cena="His own covered American backyard veranda with a weathered wooden table in front of him, beige walls, a black-framed glass door with a small American flag and a glimpse of turquoise pool at the right.",
         superficie="his weathered wooden table",
         postura="leaning on the wooden table toward the camera",
         luz=LUZ_EXTERNA, sotaque="de um homem negro americano",
         voz="voz clara e jovem de um homem no fim dos vinte anos", som="varanda tranquila ao ar livre"),
    dict(nome="Lais Collins", cena_hook="His own bright contemporary apartment seen from a very low angle at island level: the white kitchen island under the model, and behind him the white ceiling, the floor-to-ceiling windows and the shelf of green plants with the small American flag.", arquivo="LAIS_COLLINS", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/03_lais_collins.jpg",
         identidade="The exact fictional AI character Lais Collins, explicitly male: Black and mixed-race American man around thirty-two, light brown skin, highly athletic build, light grey-green eyes, short black locs, short beard and botanical line tattoos across chest, shoulders and arms.",
         roupa="Shirtless, black athletic shorts, a thin gold chain and small silver stud earrings.",
         maos="his light brown hands and forearms covered in fine botanical line tattoos",
         cena="His own bright contemporary apartment with a white kitchen island in front of him, floor-to-ceiling windows and a shelf of green plants with a small American flag.",
         superficie="his white kitchen island",
         postura="seated on a stool at the island, leaning slightly toward the camera",
         luz=LUZ_INTERNA, sotaque="de um homem negro americano",
         voz="voz média e energética de um homem de trinta e poucos anos", som="apartamento moderno tranquilo"),
    dict(nome="Robert Alves", cena_hook="His own American timber cabin kitchen seen from a very low angle at counter level: the light butcher-block counter under the model, and behind him the pine ceiling beams, the large windows showing pine forest and the small American flag on a shelf.", arquivo="ROBERT_ALVES", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/04_robert_alves.jpg",
         identidade="The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
         roupa="Plain black polo shirt and black trousers.",
         maos="his medium brown hands and bare forearms",
         cena="His own American timber cabin kitchen with a light butcher-block counter in front of him, pine walls, large windows showing pine forest and a small American flag on a shelf.",
         superficie="his light butcher-block counter",
         postura="standing behind the counter, leaning slightly toward the camera",
         luz=LUZ_INTERNA, sotaque="de um homem negro americano",
         voz="voz média e calma de um homem de quarenta e poucos anos", som="cozinha de cabana tranquila"),
    dict(nome="Roberta Carvalho", cena_hook="Her own residential kitchen seen from a very low angle at counter level: the light stone counter under the model, and behind her the white ceiling with a recessed light, the broad window showing the green garden and the small American flag on the open shelf.", arquivo="ROBERTA_CARVALHO", genero="mulher", pron="She", pos="her",
         ancora="input/ancoras/05_roberta_carvalho.jpg",
         identidade="The exact fictional AI character Roberta Carvalho: white American woman around forty-nine, lightly tanned fair skin, lean healthy build, oval face, blue-grey eyes, long medium-brown layered hair with soft waves, natural fine lines and discreet makeup.",
         roupa="Fitted navy T-shirt, two thin gold chains with a small circular pendant and small gold hoop earrings.",
         maos="her lightly tanned hands and bare forearms",
         cena="Her own residential kitchen with a light stone counter in front of her, dark wood cabinets, a broad window showing a green garden and a small American flag on the open shelf. The counter top is clear, with nothing on it except what she is using.",
         superficie="her light stone counter",
         postura="standing behind the counter, leaning slightly toward the camera",
         luz=LUZ_INTERNA, sotaque="de uma mulher branca americana",
         voz="voz feminina média e calorosa de uma mulher de quase cinquenta anos", som="cozinha residencial tranquila"),
]


EMOCAO = {
    "T1": "entonação provocadora e convicta, desafiando quem assiste",
    "T2": "entonação confiante, com um meio sorriso",
    "T3": "entonação calma e didática", "T4": "entonação calma e didática", "T5": "entonação calma e didática",
    "T6": "entonação calma e didática", "T7": "entonação calma e didática", "T8": "entonação calma e didática",
    "T9": "entonação calma e didática",
    "T10": "entonação animada e convicta",
    "T11": "entonação calorosa e segura",
    "T12": "entonação animada e convidativa, sorrindo",
    "T13": "entonação firme e próxima, olhando direto na lente",
}
ACOES = {
    "T1": "{n} segura o modelo transparente com uma mão e, conforme nomeia cada comida, joga pelo gargalo os cubos de maçã e depois traz de fora do quadro, uma de cada vez, a coxa de frango crua, o maço de espinafre e o copinho de iogurte branco, que ele despeja; a massa marrom dentro das alças não se mexe.",
    "T2": "{n} despeja a jarrinha da bebida âmbar pelo gargalo; a massa marrom começa a descer pelas alças e escorre para fora pela ponta de baixo, espalhando na bancada, e as alças de cima vão ficando transparentes.",
    "T3": "{n} inclina a tábua e os pedaços de limão caem na panela de água fervendo.",
    "T4": "os pedaços de limão boiam na água fervendo e {n} mexe com a colher.",
    "T5": "{n} vira a colher de chia na água e as sementes se espalham.",
    "T6": "{n} inclina o pote de cúrcuma sobre a panela e a água vai ficando amarela.",
    "T7": "{n} vira o pequeno galheteiro de vidro âmbar e cai um pouco de líquido na panela.",
    "T8": "a mão de {n} solta uma pitada de pimenta-do-reino sobre a água amarela, com limão e chia boiando.",
    "T9": "{n} levanta a panela pelas alças sobre a jarra com peneira.",
    "T10": "{n} segura o copo da bebida na altura do peito e fala para a câmera, com pequenos movimentos naturais.",
    "T11": "{n} segura o copo com uma mão e gesticula com a outra, falando para a câmera.",
    "T12": "{n} segura o copo com uma mão, se inclina um pouco para a câmera e fala direto com ela, sorrindo.",
    "T13": "{n} olha direto para a lente, sério e próximo, segurando o copo mais abaixo.",
}
CAMERA = {"T1": "fixa, rente à bancada, grande angular, leve handheld", "T2": "fixa, rente à bancada, grande angular, leve handheld", "T8": "fixa, bem perto da panela"}
SOM_EXTRA = {
    "T1": ", som das comidas caindo no plástico", "T2": ", som da bebida caindo e da massa escorrendo",
    "T3": ", água fervendo", "T4": ", água fervendo", "T5": ", água fervendo", "T6": ", água fervendo",
    "T7": ", água fervendo", "T8": ", água fervendo", "T9": ", água fervendo",
}
MOMENTO = {
    "T1": "0,0 a 8,1 s", "T2": "8,1 a 11,2 s", "T3": "11,2 a 15,0 s", "T4": "15,0 a 16,7 s",
    "T5": "16,7 a 18,0 s", "T6": "18,0 a 20,2 s", "T7": "20,2 a 21,9 s", "T8": "21,9 a 23,4 s",
    "T9": "23,4 a 24,8 s", "T10": "24,8 a 29,8 s", "T11": "29,8 a 34,8 s",
    "T12": "~5 s (o bloco do produto do modelo saiu)", "T13": "51,4 a 53,7 s do modelo, ~2,3 s",
}
TITULOS = {
    "T1": "gancho, comidas entrando no modelo transparente", "T2": "reveal, a bebida faz a massa sair por baixo",
    "T3": "limão da tábua para a panela", "T4": "limão boiando, colher mexendo", "T5": "colher de chia",
    "T6": "cúrcuma, a água amarelando", "T7": "splash do bitters, galheteiro sem rótulo", "T8": "close da panela, pimenta",
    "T9": "panela sobre a jarra com peneira", "T10": "copo na altura do peito", "T11": "copo, gesto com a mão",
    "T12": "CTA, copo na mão", "T13": "follow, plano mais fechado",
}
TRANSCRICAO_PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$", ROTEIRO.split("## Tabela bilíngue")[1].split("## ")[0], re.M))
assert set(TRANSCRICAO_PT) == set(TAKES), TRANSCRICAO_PT


def keyframes(a):
    n, P, p = a["nome"], a["pron"], a["pos"]
    sup, maos = a["superficie"], a["maos"]
    boca = "caught mid-sentence, lips naturally parted, animated expression"
    ref = (f"Use the first attached image only for {n}'s exact identity, wardrobe and own setting. "
           f"Use the second attached image only as a composition reference for the camera position, framing and the "
           f"action; do not copy its person, cap, clothes, pool, backyard, colors, the brand bottle or the white "
           f"caption text.")
    cena, post = a["cena"], f"{n} is {a['postura']}."
    # Medidas da FICHA_FRAMES.md: panela e fogareiro nos 40% de baixo, avatar agachado atras (K03-K07);
    # copo no primeiro plano, um terco do quadro, sempre mais perto que o rosto (K10-K12).
    comp_panela = ("The phone lens is only a few inches from the pot: the pot and the hot plate fill the lower forty "
                   f"percent of the frame, far closer to the camera than {p} face and larger than {p} head, nothing else "
                   f"competing with them. {P} crouches right behind the pot, head and shoulders above it in the upper "
                   "half. Nothing else is on the counter. The background is reduced by framing, never by blur.")
    comp_copo = ("The phone lens is only a few inches from the glass of tea: it sits in the lower foreground and takes up "
                 f"about a third of the frame, closer to the camera than {p} face, nothing else competing with it. {P} "
                 "leans toward the lens right behind it, from the chest up, face clear in the upper half. The background "
                 "is reduced by framing, never by blur.")
    cam_panela = "phone resting on the counter at the height of the pot rim, wide lens a few inches from the pot, fixed"
    cam_copo = "phone resting on the counter at chest height, wide lens a few inches from the glass, fixed"
    post_panela = (f"{n} crouches low behind the counter, NOT standing upright, so {p} head and shoulders rise just "
                   "above the pot.")
    comp_hook = (f"Extreme low-angle close-up taken with the phone's ultra-wide lens only a few inches from the model: the "
                 f"model is the hero and fills the lower sixty percent of the frame, almost touching the left and right "
                 f"edges, its bottom tube reaching the bottom edge, far closer to the camera than {p} face and much larger "
                 f"than {p} head, nothing else competing with it. {P} crouches right behind it, head and shoulders rising "
                 f"above the model in the upper part of the frame, face centered, leaning toward the lens. The counter "
                 f"around the model is empty. The background is reduced by framing, never by blur.")
    cam_hook = ("phone lying almost flat on the counter, ultra-wide 0.5x lens a few inches from the model, pointing slightly "
                "upward, slight wide-angle perspective")
    post_hook = (f"{n} crouches low behind the counter, NOT standing upright, so only {p} head, shoulders and arms rise above "
                 f"the model; one hand grips the left edge of the model close to the lens, looking large in frame.")
    ks = {
        "T1": dict(scene=a["cena_hook"],
                   prop=MODELO.format(sup=sup) + f" With the other hand {n} holds a small clear plastic cup of diced red and "
                   "yellow apple tipped right above the funnel neck, close to the lens.",
                   posture=post_hook, composition=comp_hook, camera=cam_hook,
                   state=f"Start frame: the first apple cubes are just falling into the funnel neck; every loop is still packed brown. {n} is {boca}.",
                   negative=NEG_BASE + NEG_HOOK),
        "T2": dict(scene=a["cena_hook"],
                   prop=MODELO.format(sup=sup) + f" With the other hand {n} holds a clear glass measuring jug of golden-amber "
                   "lemon and turmeric tea tipped right above the funnel neck, the amber stream just starting to fall in.",
                   posture=post_hook, composition=comp_hook, camera=cam_hook,
                   state=f"Start frame: the amber stream is just entering the funnel neck; every loop is still packed brown and nothing has come out yet. {n} is {boca}.",
                   negative=NEG_BASE + NEG_HOOK),
        "T3": dict(prop=PANELA.format(sup=sup) + f", very close to the lens in the lower foreground. {n} holds a wooden "
                   "cutting board with a fresh lemon chopped into chunks tipped over the pot.",
                   posture=post_panela, composition=comp_panela, camera=cam_panela,
                   state=f"Start frame: the first lemon chunks are sliding off the board toward the water, steam rising. {n} is {boca}.",
                   negative=NEG_BASE + NEG_CORPO),
        "T4": dict(prop=PANELA.format(sup=sup) + f", very close to the lens in the lower foreground, lemon chunks floating "
                   f"in the water. {n} holds a metal spoon inside the pot.",
                   posture=post_panela, composition=comp_panela, camera=cam_panela,
                   state=f"Start frame: the lemon chunks bob in the boiling water, the spoon just starting to stir. {n} is {boca}.",
                   negative=NEG_BASE + NEG_CORPO),
        "T5": dict(prop=PANELA.format(sup=sup) + f", very close to the lens in the lower foreground, lemon chunks floating "
                   f"in the clear water. {n} holds a teaspoon heaped with black chia seeds right above the water.",
                   posture=post_panela, composition=comp_panela, camera=cam_panela,
                   state=f"Start frame: the spoon is tipping and the first chia seeds are falling. {n} is {boca}.",
                   negative=NEG_BASE + NEG_CORPO),
        "T6": dict(prop=PANELA.format(sup=sup) + f", very close to the lens in the lower foreground, lemon chunks and chia "
                   f"seeds in the water. {n} tips a small plain glass jar of bright orange ground turmeric, with no label, over the pot.",
                   posture=post_panela, composition=comp_panela, camera=cam_panela,
                   state=f"Start frame: the first turmeric powder hits the water and a yellow cloud starts to spread. {n} is {boca}.",
                   negative=NEG_BASE + NEG_CORPO),
        "T7": dict(prop=PANELA.format(sup=sup) + f", very close to the lens in the lower foreground, the water now bright "
                   f"yellow with lemon chunks and chia seeds. {n} tips a small glass kitchen cruet of dark amber herbal bitters, with no label, over the pot.",
                   posture=post_panela, composition=comp_panela, camera=cam_panela,
                   state=f"Start frame: a small splash of dark liquid is leaving the spout of the cruet. {n} is {boca}.",
                   negative=NEG_BASE + NEG_CORPO),
        "T8": dict(scene=f"Close view of the pot on {sup}; at the top edge of the frame, part of {p} own kitchen with the small American flag, discreet but visible and in focus.",
                   prop=f"The clear glass pot of bright yellow boiling tea with lemon chunks, black chia seeds and a few black pepper flecks floating. {n}'s fingers release a pinch of ground black pepper above the water.",
                   posture=f"Only {maos} enter from the top of the frame.",
                   composition="The phone lens is only a few inches from the pot: it fills the frame edge to edge, very large and close. The background is reduced by framing, never by blur.",
                   camera="phone with a wide lens a few inches from the side of the pot, just above the rim",
                   state="Start frame: the pinch of black pepper is falling onto the yellow water.",
                   negative=NEG_BASE + NEG_CORPO + ", no face in frame"),
        "T9": dict(prop=f"{n} lifts the clear glass pot of yellow tea with lemon chunks by both handles, right above a clear "
                   f"glass pitcher with a fine metal mesh strainer on top, standing on {sup} next to the small electric hot plate.",
                   posture=f"{n} stands behind the counter holding the pot with both hands.",
                   composition=f"The phone lens is only a few inches from the pot and the pitcher: they fill the lower half of the frame, large and close, {p} chest and face at the top edge of the frame, partly cut. Nothing else is on the counter. The background is reduced by framing, never by blur.",
                   camera="phone resting on the counter at counter height, wide lens a few inches from the pitcher, fixed",
                   state=f"Start frame: the pot is lifted just above the strainer, about to tip. {n} is {boca}.",
                   negative=NEG_BASE + NEG_CORPO),
        "T10": dict(prop=f"{n} holds {COPO} at chest height. No bottle anywhere in frame.", posture=post,
                    composition=comp_copo, camera=cam_copo,
                    state=f"Start frame: {n} looks into the lens holding the glass, {boca}.", negative=NEG_BASE + NEG_CORPO),
        "T11": dict(prop=f"{n} holds {COPO} at chest height in one hand, the other hand open in a natural gesture. No bottle anywhere in frame.", posture=post,
                    composition=comp_copo, camera=cam_copo,
                    state=f"Start frame: {n} looks into the lens mid-gesture, {boca}.", negative=NEG_BASE + NEG_CORPO),
        "T12": dict(prop=f"{n} holds {COPO} in one hand, leaning a little toward the lens. No bottle anywhere in frame.", posture=post,
                    composition=comp_copo, camera=cam_copo,
                    state=f"Start frame: {n} smiles at the lens, {boca}.", negative=NEG_BASE + NEG_CORPO),
        "T13": dict(prop=f"{n} holds {COPO} low in one hand. No bottle anywhere in frame.", posture=post,
                    composition=f"The tightest shot of the video: {p} face and upper chest fill the upper two thirds of the frame, close to the lens, and the glass sits at the bottom edge a few inches from the lens. The background is reduced by framing, never by blur.",
                    camera=cam_copo,
                    state=f"Start frame: {n} looks straight into the lens, serious and close, {boca}.", negative=NEG_BASE + NEG_CORPO),
    }
    out = []
    for i, t in enumerate(TAKES, 1):
        d = ks[t]
        cod = f"K{i:02d}"
        j = {
            "shot_id": f"{cod}_{t.lower()}_{a['arquivo'].lower()}",
            "fiction_note": FICCAO,
            "reference_use": ref,
            "identity_main": a["identidade"],
            "wardrobe": a["roupa"],
            "scene": d.get("scene", cena),
            "prop": d["prop"],
            "posture": d["posture"],
            "composition": d["composition"],
            "camera": d["camera"],
            "lighting": a["luz"],
            "state": d["state"],
            "realism": REALISMO,
            "aspect_ratio": "9:16 vertical",
            "negative": d["negative"],
        }
        out.append(dict(codigo=cod, take=t, titulo=TITULOS[t], j=j))
    return out


def videos(a):
    n = a["nome"]
    art = "o avatar" if a["genero"] == "homem" else "a avatar"
    ouvido = "ouvido" if a["genero"] == "homem" else "ouvida"
    vs = []
    for i, t in enumerate(TAKES, 1):
        acao = ACOES[t].format(n=n)
        acao = acao[0].upper() + acao[1:]
        if t in CURTAS:
            acao += (" " + ("Ele" if a["genero"] == "homem" else "Ela")
                     + " diz a frase em ritmo natural logo no começo e continua a ação em silêncio até o fim.")
        txt = (f"{art} {n}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
               f"{EMOCAO[t]}, voz autêntica, como se exigisse ser {ouvido}, a seguinte frase: \"{FALAS[t]}\"\n\n"
               f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
               f"o que acontece no vídeo: {acao}\n\n"
               f"câmera: {CAMERA.get(t, 'fixa')}\n\n"
               f"som ambiente: {a['som']}{SOM_EXTRA.get(t, '')}, sem música")
        vs.append((f"V{i:02d}", t, f"K{i:02d}", txt))
    return vs


def texto_flow(j):
    """Prompt de imagem de EXECUCAO, em JSON (Luigi, 2026-09-25, contrato do Flow v17).
    Mesmo conteudo do JSON interno, sem o shot_id (metadata) e com o formato na frente."""
    ordem = ["fiction_note", "reference_use", "identity_main", "wardrobe", "scene", "prop", "posture",
             "composition", "camera", "lighting", "state", "realism", "aspect_ratio", "negative"]
    assert set(ordem) == set(j) - {"shot_id"}, set(j) ^ set(ordem)
    d = {"format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."}
    d.update({k: j[k] for k in ordem})
    return json.dumps(d, ensure_ascii=False, indent=2)


def anexo(a, k):
    return "\n".join([
        "> ### 📎 ANEXAR: **2 IMAGENS**",
        f"> **1️⃣ ÂNCORA {a['nome'].upper()}** `{a['ancora']}`",
        f"> **2️⃣ FRAME DO MODELO, só composição** `{frame_modelo(k['codigo'])}`",
        ">", "> ### 🆕 GERAR DO ZERO"])


def capcut():
    return [
        "1. Clipes numerados na ordem: V01 a V13.",
        "2. Cortar cada clipe no tempo da cena do modelo: " + "; ".join(f"V{t[1:].zfill(2)} {MOMENTO[t]}" for t in TAKES) + ".",
        "3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.",
        "4. Cenas curtas (V02 a V09 e V13): a fala vem no começo do clipe; cortar logo depois da última palavra, no tempo da cena.",
        "5. No V01 e no V02, os zooms de corte do modelo (na coxa de frango, no espinafre, na massa saindo) saem do mesmo clipe: recortar e aproximar na edição.",
        "6. Legenda palavra a palavra, branca, no meio do quadro, com a palavra-chave em serifa itálica, igual ao modelo.",
        "7. Sem Voice Changer: a voz vem do prompt de cada V.",
        "8. Música só depois do gancho (a partir do V03), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "9. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {TRANSCRICAO_PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    art = "o avatar" if a["genero"] == "homem" else "a avatar"
    ouvido = "ouvido" if a["genero"] == "homem" else "ouvida"
    L = [f"# {a['nome']} | FityWell Growth Modelo de intestino | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (53,7 s, avatar IA)", "",
         f"Âncora: `{a['ancora']}`", "",
         "Funil: growth, comentário `yes` + follow. Rodada de validação, gancho fiel ao modelo. Sem produto em quadro.", "",
         "## Índice de geração", "",
         "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    for k in ks:
        L.append(f"| {k['take']} | {k['codigo']} | ÂNCORA {a['nome'].upper()} + FRAME DO MODELO ({k['codigo']}) | GERAR DO ZERO |")
    L += ["", "Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro, "
          "então não existe `EDITAR do K__` aqui. O frame do modelo de cada K entra só como composição.", "",
          "## Trava de identidade e continuidade", "",
          f"- Identidade: {a['identidade']}",
          f"- Roupa (fixa da conta): {a['roupa']}",
          f"- Cenário-base (fixo da conta): {a['cena']}",
          f"- Luz: {a['luz']}",
          f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.",
          "- Sem 2ª pessoa.", "",
          "## Trava do prop herói", "",
          "- Gancho: " + MODELO.format(sup=a["superficie"]),
          "- Receita: panela de vidro no fogareiro elétrico de uma boca, limão, chia, cúrcuma em pote liso, "
          "bitters em galheteiro de vidro âmbar liso, pimenta-do-reino. Corpo: " + COPO + ". Nenhuma embalagem com texto ou marca.",
          "", "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "",
          "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · ÂNCORA {a['nome'].upper()} + FRAME DO MODELO", "",
              anexo(a, k), "", f"Cena: {k['titulo']}.", "", "```json",
              json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["## Bloco global de vídeo", "", "```text",
          f"{art} {a['nome']}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
          f"[emoção da fala], voz autêntica, como se exigisse ser {ouvido}, a seguinte frase: \"[FALA EXATA DO ROTEIRO]\"", "",
          f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.", "",
          "o que acontece no vídeo: [ação enxuta]", "", "câmera: [fixa]", "", f"som ambiente: {a['som']}, sem música",
          "```", "", "# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Mapa de âncoras", "", "| Keyframe | Referências a anexar | Modelo |", "|---|---|---|"]
    for k in ks:
        L.append(f"| {k['codigo']} | ÂNCORA {a['nome'].upper()} + `{frame_modelo(k['codigo'])}` (só composição) | Nano Banana 2, 9:16 |")
    L += ["", "## Montagem no CapCut", ""] + capcut() + [
          "", "## Gates de qualidade", "",
          "1. Fala de cada V igual ao ROTEIRO, palavra por palavra.",
          "2. Um take por cena do modelo; cenas curtas marcadas; nenhum take acima de 29 palavras.",
          "3. Bandeira dos EUA no campo scene de todo K (formato de avatar IA).",
          "4. Zero travessão.", "5. Keyword `yes` no T12.",
          "6. Produto fora de quadro: nenhuma embalagem com marca; o bloco do produto da Amazon saiu.",
          "7. Negative sem termo sensível.",
          "8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "9. Gancho fiel no conteúdo: comidas entrando no modelo transparente sem efeito, e a bebida que faz a massa sair.",
          "10. Um K = um V; o reveal do T2 é uma imagem só, do estado inicial (modelo inteiro marrom).", ""]
    flow = [f"# Blocos limpos para o Google Flow | {a['nome']}", "", f"Fonte interna: `PROMPTS_{a['arquivo']}.md`", "",
            "## BLOCO DE IMAGEM", "", "```text"]
    for k in ks:
        flow += [k["codigo"], texto_flow(k["j"]), ""]
    flow += ["```", "", "## BLOCO DE VÍDEO", "", "```text"]
    for cod, _, _, txt in vs:
        flow += [cod, txt, ""]
    flow += ["```", "", "## Tabela de leitura humana", "", "| Código | Take | Anexar |", "|---|---|---|"]
    for k in ks:
        flow.append(f"| {k['codigo']} / V{k['codigo'][1:]} | {k['take']}, {k['titulo']} | ÂNCORA + `{frame_modelo(k['codigo'])}` |")
    flow += ["", "## Transcrição final por take", ""] + transcricao()
    return "\n".join(L) + "\n", "\n".join(flow) + "\n"


def main():
    fila = (AQUI / "AVATAR_QUEUE.md").read_text(encoding="utf-8")
    ativo = sys.argv[1] if len(sys.argv) > 1 else re.search(r"\| ACTIVE \| ([^|]+?) \|", fila).group(1)
    for a in AVATARES:
        p, f = pacote(a)
        (AQUI / f"PROMPTS_{a['arquivo']}.md").write_text(p, encoding="utf-8")
        (AQUI / f"FLOW_{a['arquivo']}.md").write_text(f, encoding="utf-8")
        if a["nome"] == ativo:
            (AQUI / "PROMPTS_PRODUCAO.md").write_text(p, encoding="utf-8")
    print("ok: %d pacotes; PROMPTS_PRODUCAO.md = %s" % (len(AVATARES), ativo))


if __name__ == "__main__":
    main()
