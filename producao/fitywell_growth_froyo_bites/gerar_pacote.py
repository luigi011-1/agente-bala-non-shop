"""Gera os pacotes por avatar da producao fitywell_growth_froyo_bites (organico, growth, validacao).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Nenhuma fala muda por
avatar. Identidade, roupa e cenario: fichas aprovadas em fitywell_growth_dentes_agua (2026-09-24),
conferidas de novo contra as ancoras anexadas nesta producao (uma por vez, 2026-09-25).

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

HEADS = re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M)
TAKES = [t for t, _ in HEADS]
assert TAKES == ["T%d" % i for i in range(1, 13)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == {"T1", "T8", "T12"}, FALAS
MUDOS = [t for t in TAKES if t not in FALAS]
VOZ_DE = {t: ("T1" if int(t[1:]) < 8 else "T8") for t in MUDOS}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."


def frame_modelo(cod):
    return f"input/frames_modelo/{cod}_modelo.png"


LUZ_INTERNA = ("Neutral overcast daylight from a window, the outside clearly visible through the window, "
               "soft even light on the face and hands with no harsh shadows.")
LUZ_EXTERNA = ("Overcast sky with visible cloud texture, never white or blown out, neutral daylight, "
               "soft even light on the face and hands with no harsh shadows.")

REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")

NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, "
            "no studio, no plastic-looking human skin, no extra fingers, no third hand, "
            "no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, "
            "no yellow tint, no golden glow, no golden hour light, no sunset, no hard sunlight shadows, "
            "no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, "
            "no second person in frame")
NEG_ROSTO = ", no perfect factory-made dessert, no ice cream cone, no popsicle stick"
NEG_POV = ", no face in frame, no perfect factory-made dessert, no glossy food-magazine styling"

BITE = ("a homemade frozen yogurt bite about the size of a palm: a round, slightly irregular handmade disc with a thick "
        "smooth frosty white shell of frozen Greek yogurt")
CORTE = ("cut in half, each cut face showing a thick dense purple-magenta filling of mashed raspberries, blueberries "
         "and black chia seeds, speckled with black seeds and dark blueberry skins, framed by the white yogurt shell")

AVATARES = [
    dict(nome="Eva Dall", arquivo="EVA_DALL", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/01_eva_dall.jpg",
         identidade="The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
         roupa="White ribbed tank top and a thin silver chain.",
         maos="his medium brown hands and bare forearms",
         cena="His own modern white kitchen with a strongly veined dark green marble counter in front of him, tall windows to the right and a small American flag on the shelf beside a small plant.",
         superficie="his dark green veined marble counter",
         postura="standing behind his counter, leaning slightly toward the camera",
         luz=LUZ_INTERNA, sotaque="de um homem negro americano",
         voz="voz média e amigável de um homem de quase cinquenta anos", som="cozinha residencial tranquila"),
    dict(nome="Ivy Carl", arquivo="IVY_CARL", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/02_ivy_carl.jpg",
         identidade="The exact fictional AI character Ivy Carl, explicitly male: Black American man around twenty-eight, dark brown skin, lean athletic build, long oval face, very light grey-hazel eyes, fine black braids beneath a plain black cap and a short goatee.",
         roupa="Plain black cap, fitted black long-sleeve athletic shirt, black trousers and small silver stud earrings.",
         maos="his dark brown hands with the black athletic sleeves at the wrists",
         cena="His own covered American backyard veranda with a weathered wooden table in front of him, beige walls, a black-framed glass door with a small American flag and a glimpse of turquoise pool at the right.",
         superficie="his weathered wooden table",
         postura="leaning on the wooden table toward the camera",
         luz=LUZ_EXTERNA, sotaque="de um homem negro americano",
         voz="voz clara e jovem de um homem no fim dos vinte anos", som="varanda tranquila ao ar livre"),
    dict(nome="Jamie Voss", arquivo="JAMIE_VOSS", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/03_jamie_voss.jpg",
         identidade="The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
         roupa="Beige cap backward, navy long-sleeve henley and jeans.",
         maos="his fair, slightly hairy hands with the navy henley sleeves at the wrists",
         cena="His own bright residential kitchen with a white-veined stone counter in front of him, cream upper cabinets and a black-framed window with a small American flag. The counter top is clear, with nothing on it except what he is using.",
         superficie="his white-veined stone counter",
         postura="leaning on the counter with his forearms, toward the camera",
         luz=LUZ_INTERNA, sotaque="de um homem branco americano",
         voz="voz grave e firme de um homem de quarenta e poucos anos", som="cozinha residencial tranquila"),
    dict(nome="Lais Collins", arquivo="LAIS_COLLINS", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/04_lais_collins.jpg",
         identidade="The exact fictional AI character Lais Collins, explicitly male: Black and mixed-race American man around thirty-two, light brown skin, highly athletic build, light grey-green eyes, short black locs, short beard and botanical line tattoos across chest, shoulders and arms.",
         roupa="Shirtless, black athletic shorts, a thin gold chain and small silver stud earrings.",
         maos="his light brown hands and forearms covered in fine botanical line tattoos",
         cena="His own bright contemporary apartment with a white kitchen island in front of him, floor-to-ceiling windows and a shelf of green plants with a small American flag.",
         superficie="his white kitchen island",
         postura="seated on a stool at the island, leaning slightly toward the camera",
         luz=LUZ_INTERNA, sotaque="de um homem negro americano",
         voz="voz média e energética de um homem de trinta e poucos anos", som="apartamento moderno tranquilo"),
    dict(nome="Robert Alves", arquivo="ROBERT_ALVES", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/05_robert_alves.jpg",
         identidade="The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
         roupa="Plain black polo shirt and black trousers.",
         maos="his medium brown hands and bare forearms",
         cena="His own American timber cabin kitchen with a light butcher-block counter in front of him, pine walls, large windows showing pine forest and a small American flag on a shelf.",
         superficie="his light butcher-block counter",
         postura="standing behind the counter, leaning slightly toward the camera",
         luz=LUZ_INTERNA, sotaque="de um homem negro americano",
         voz="voz média e calma de um homem de quarenta e poucos anos", som="cozinha de cabana tranquila"),
    dict(nome="Roberta Carvalho", arquivo="ROBERTA_CARVALHO", genero="mulher", pron="She", pos="her",
         ancora="input/ancoras/06_roberta_carvalho.jpg",
         identidade="The exact fictional AI character Roberta Carvalho: white American woman around forty-nine, lightly tanned fair skin, lean healthy build, oval face, blue-grey eyes, long medium-brown layered hair with soft waves, natural fine lines and discreet makeup.",
         roupa="Fitted navy T-shirt, two thin gold chains with a small circular pendant and small gold hoop earrings.",
         maos="her lightly tanned hands and bare forearms",
         cena="Her own residential kitchen with a light stone counter in front of her, dark wood cabinets, a broad window showing a green garden and a small American flag on the open shelf. The counter top is clear, with nothing on it except what she is using.",
         superficie="her light stone counter",
         postura="standing behind the counter, leaning slightly toward the camera",
         luz=LUZ_INTERNA, sotaque="de uma mulher branca americana",
         voz="voz feminina média e calorosa de uma mulher de quase cinquenta anos", som="cozinha residencial tranquila"),
]

TITULOS = {
    "T1": "gancho, as duas metades coladas na lente, falando",
    "T2": "gancho, macro do corte roxo na mão",
    "T3": "gancho, a mordida grande de olhos fechados",
    "T4": "frutas caindo na tigela branca, depois a chia",
    "T5": "garfo amassando as frutas com a chia",
    "T6": "xarope de bordo escorrendo, depois a mistura",
    "T7": "iogurte grego em espiral na pasta roxa",
    "T8": "colheradas na assadeira, narração fora de quadro",
    "T9": "costas da colher achatando os discos",
    "T10": "disco congelado banhado no iogurte",
    "T11": "faca corta e as mãos abrem o recheio",
    "T12": "CTA, bite mordido na lente, falando",
}

MOMENTO = {  # tempo no video modelo, para o CapCut
    "T1": "em quadro 0,0 a 0,4 s; áudio de 0,0 a ~6,4 s, por baixo do V02 ao V07",
    "T2": "0,4 a 0,9 s", "T3": "0,9 a 1,7 s", "T4": "1,7 a 2,3 s", "T5": "2,3 a 3,0 s",
    "T6": "3,0 a 4,2 s", "T7": "4,2 a 6,5 s",
    "T8": "em quadro 6,5 a 8,0 s; áudio de 6,5 a ~11,5 s, por baixo do V09 ao V11",
    "T9": "8,0 a 9,0 s", "T10": "9,0 a 10,0 s", "T11": "10,0 a 11,5 s",
    "T12": "11,5 s até o fim da fala (~6 s)",
}

EMOCAO = {
    "T1": "entonação séria e sincera de quem conta algo pessoal, sem drama, ficando mais firme na segunda frase",
    "T8": "entonação leve e animada, de quem mostra uma solução que achou para si",
    "T12": "entonação de prazer genuíno, sorrindo, acabando de mastigar, e a pergunta do fim sai quase para si mesmo",
}

ACOES = {
    "T1": "{n} segura as duas metades do froyo bite perto da câmera, o corte roxo virado para a lente, e fala olhando para a câmera, com pequenos movimentos naturais da mão.",
    "T2": "a mão de {n} gira devagar a metade do froyo bite, mostrando o recheio roxo com chia de perto.",
    "T3": "{n} morde o froyo bite com vontade, fecha os olhos, inclina a cabeça um pouco para trás e mastiga devagar, com prazer.",
    "T4": "punhados de framboesas e mirtilos caem na tigela branca e quicam; depois uma colher cheia de sementes de chia é virada sobre as frutas.",
    "T5": "o garfo amassa as frutas com a chia, pressionando várias vezes, até virar um purê grosso e vermelho.",
    "T6": "um fio de xarope de bordo escorre da colher sobre o purê; depois a colher mistura tudo até virar uma pasta roxa e brilhante.",
    "T7": "a colher solta o iogurte grego sobre a pasta roxa e faz espirais, dobrando o branco no roxo até a mistura ficar lilás e marmorizada.",
    "T8": "a colher deposita montinhos da mistura lilás no papel manteiga, um ao lado do outro. Só a mão de {n} aparece.",
    "T9": "as costas da colher pressionam cada montinho até ele virar um disco redondo e liso.",
    "T10": "a colher afunda o disco roxo congelado no iogurte grego, gira, e levanta o disco coberto de branco.",
    "T11": "a faca desce e corta o froyo bite ao meio; as duas mãos puxam as metades e abrem, virando o recheio roxo para a câmera.",
    "T12": "{n} segura o froyo bite mordido perto da câmera, fala direto para a lente sorrindo e, no fim, olha para o bite balançando levemente a cabeça.",
}
CAMERA = {
    "T1": "fixa, celular apoiado na bancada na altura do peito", "T2": "fixa, bem perto da mão, leve tremor natural",
    "T3": "fixa, celular apoiado na bancada na altura do peito", "T12": "fixa, celular apoiado na bancada na altura do peito",
}
CAMERA_POV = "fixa, de cima, como celular na mão de quem cozinha, leve tremor natural"
SOM_EXTRA = {
    "T3": ", som leve da mordida", "T4": ", som das frutas caindo na tigela", "T5": ", som do garfo amassando",
    "T6": ", som da colher raspando a tigela", "T7": ", som da colher mexendo", "T8": ", som leve da colher no papel",
    "T9": ", som leve da colher no papel", "T10": ", som da colher no iogurte", "T11": ", som da faca cortando o gelado",
}

TRANSCRICAO_PT = {
    "T1": "Depois de uma cirurgia de tumor cerebral, picos de açúcar não são uma opção para mim. A inflamação trava completamente a cicatrização.",
    "T8": "Então eu fiz esses bites de frozen yogurt anti-inflamatórios para matar minha vontade de doce sem a queda da glicose.",
    "T12": "Salva essa, e me segue pra não perder minhas próximas receitas saudáveis. Por que isso é tão bom?",
}


def keyframes(a):
    n, P, p = a["nome"], a["pron"], a["pos"]
    sup, maos = a["superficie"], a["maos"]
    boca = "caught mid-sentence, lips naturally parted, animated expression"
    ref = (f"Use the first attached image only for {n}'s exact identity, wardrobe and own setting. "
           f"Use the second attached image only as a composition reference for the camera position, framing and the "
           f"action with the food; do not copy its person, hands, rings, clothes, table, room, colors, hard sunlight "
           f"or the white caption text.")
    rosto = dict(scene=a["cena"], posture=f"{n} is {a['postura']}.", negative=NEG_BASE + NEG_ROSTO)
    pov = dict(negative=NEG_BASE + NEG_POV)
    ks = {
        "T1": dict(rosto,
                   prop=f"{n} holds up {BITE}, {CORTE}. The two halves are stacked one on top of the other, both cut faces turned toward the lens, held in the fingertips of one hand.",
                   composition=f"The two stacked halves are very close to the lens in the lower foreground, large in frame, closer to the camera than {p} face, nothing else competing with them. {P} is clear behind them in the upper half, head and upper chest. The background is reduced by framing, never by blur.",
                   camera="phone camera resting on the counter at chest height, straight on, fixed",
                   state=f"Start frame: {n} shows the cut halves to the camera, {boca}."),
        "T2": dict(scene=f"{n}'s hand close to the lens above {sup}, only the edge of the counter visible around it.",
                   prop=f"{n}'s hand holds one half of {BITE}, {CORTE}.",
                   posture=f"Only {maos} are in frame, holding the half between thumb and fingers.",
                   composition="Macro: the cut face of the half fills most of the frame, the purple filling and the white shell sharp and detailed, the fingers at the edges. The background is reduced by framing, never by blur.",
                   camera="phone camera very close to the hand, straight on, fixed",
                   state="Start frame: the cut face is turned straight to the lens, a few crumbs of filling at the edge.",
                   negative=NEG_BASE + NEG_POV),
        "T3": dict(rosto,
                   prop=f"{n} holds {BITE}, whole and uncut, at {p} mouth.",
                   composition=f"From the chest up, {p} face and the hand with the frozen yogurt bite clear in the upper half, {p} head tilted slightly back. The background is reduced by framing, never by blur.",
                   camera="phone camera resting on the counter at chest height, straight on, fixed",
                   state=f"Start frame: {n}'s mouth is wide open, the edge of the frozen yogurt bite just touching {p} lips, eyes starting to close."),
        "T4": dict(pov, scene=f"Top-down view of {sup}.",
                   prop=f"A wide, deep plain white ceramic bowl sits on {sup}. A few fresh raspberries and blueberries lie in the bottom of the empty bowl and a handful more are falling into it from {n}'s hand at the top edge of the frame.",
                   posture=f"Only {maos} enter from the top edge of the frame.",
                   composition="The white bowl fills most of the frame, very close to the lens, the counter visible around it. The background is reduced by framing, never by blur.",
                   camera="phone held straight above the bowl, looking down",
                   state="Start frame: the berries are mid-fall above the bowl, the bowl still mostly empty."),
        "T5": dict(pov, scene=f"Top-down view of {sup}.",
                   prop=f"The wide plain white ceramic bowl on {sup} is full of fresh raspberries and blueberries sprinkled with black chia seeds. {n}'s hand holds a black metal fork pressing down into the berries.",
                   posture=f"Only {maos} enter from the bottom edge of the frame, holding the fork.",
                   composition="The bowl fills most of the frame, very close to the lens. The background is reduced by framing, never by blur.",
                   camera="phone held straight above the bowl, looking down",
                   state="Start frame: the fork is pressing the first berries, a few already crushed red with juice."),
        "T6": dict(pov, scene=f"Top-down view of {sup}.",
                   prop=f"The wide plain white ceramic bowl on {sup} holds a chunky red mash of raspberries, blueberries and chia seeds. {n}'s hand holds a metal spoon full of amber maple syrup right above the mash, a thin drip just falling.",
                   posture=f"Only {maos} enter from the bottom edge of the frame.",
                   composition="The bowl fills most of the frame, very close to the lens. The background is reduced by framing, never by blur.",
                   camera="phone held straight above the bowl, looking down",
                   state="Start frame: the first thin drip of syrup is falling from the tipped spoon onto the red mash."),
        "T7": dict(pov, scene=f"Close top-down view of {sup}.",
                   prop=f"The plain white ceramic bowl on {sup} is full of a glossy thick deep red-purple paste of mashed berries and chia seeds. A big spoonful of thick white Greek yogurt has just been dropped in the middle, the spoon still touching it in {n}'s hand.",
                   posture=f"Only {maos} enter from the side of the frame.",
                   composition="The bowl fills the frame edge to edge, very close to the lens. The background is reduced by framing, never by blur.",
                   camera="phone held close above the bowl, looking down at a slight angle",
                   state="Start frame: a clean white dollop of yogurt sits on the purple paste, not mixed yet."),
        "T8": dict(pov, scene=f"Top-down view of {sup}.",
                   prop=f"A rimmed metal sheet pan lined with plain brown parchment paper sits on {sup}. One heaped mound of lilac berry and yogurt mixture is already on the paper, and {n}'s hand holds a metal spoon depositing a second heaped mound beside it.",
                   posture=f"Only {maos} enter from the bottom corner of the frame.",
                   composition="The sheet pan fills most of the frame, very close to the lens, shown diagonally. The background is reduced by framing, never by blur.",
                   camera="phone held straight above the sheet pan, looking down",
                   state="Start frame: the second mound is sliding off the spoon onto the parchment."),
        "T9": dict(pov, scene=f"Close top-down view of the parchment-lined sheet pan on {sup}.",
                   prop=f"Several heaped mounds of lilac berry and yogurt mixture sit in a row on plain brown parchment paper. {n}'s hand presses the back of a metal spoon onto one mound, already spreading it into a flat round disc.",
                   posture=f"Only {maos} enter from the side of the frame.",
                   composition="The mounds and the spoon fill the frame, very close to the lens. The background is reduced by framing, never by blur.",
                   camera="phone held close above the sheet pan, looking down",
                   state="Start frame: the back of the spoon rests on the first mound, which is half flattened."),
        "T10": dict(pov, scene=f"Top-down view of {sup}.",
                    prop=f"A wide dark brown ceramic bowl filled to the brim with thick smooth white Greek yogurt sits on {sup}. {n}'s hand holds a black metal spoon with a frozen lilac-purple disc of berry mixture on it, just above the yogurt.",
                    posture=f"Only {maos} enter from the bottom edge of the frame.",
                    composition="The dark bowl of white yogurt fills most of the frame, very close to the lens. The background is reduced by framing, never by blur.",
                    camera="phone held straight above the bowl, looking down",
                    state="Start frame: the frozen disc is about to touch the white yogurt, a light frost on its surface."),
        "T11": dict(pov, scene=f"Top-down view of plain brown parchment paper on {sup}.",
                    prop=f"One whole {BITE.replace('a homemade', 'homemade')} lies on the parchment, uncut. The blade of a large kitchen knife rests across its center, {n}'s hand on the handle, ready to cut.",
                    posture=f"Only {maos} are in frame, one on the knife handle, the other resting beside the bite.",
                    composition="The white frozen yogurt bite sits in the middle of the frame, very close to the lens, the knife crossing it. The background is reduced by framing, never by blur.",
                    camera="phone held straight above the parchment, looking down",
                    state="Start frame: the knife blade touches the top of the frosty white shell, nothing cut yet."),
        "T12": dict(rosto,
                    prop=f"{n} holds {BITE} with a big bite taken out of it, the bitten edge showing the purple-magenta berry and chia filling inside the white shell.",
                    composition=f"The bitten frozen yogurt bite is very close to the lens in the lower foreground, large in frame, closer to the camera than {p} face, nothing else competing with it. {P} is clear behind it in the upper half, the tightest shot of the video. The background is reduced by framing, never by blur.",
                    camera="phone camera resting on the counter at chest height, straight on, fixed",
                    state=f"Start frame: {n} has just finished chewing and smiles at the camera, {boca}."),
    }
    out = []
    for i, t in enumerate(TAKES, 1):
        d = ks[t]
        cod = f"K{i:02d}"
        j = {
            "shot_id": f"{cod}_{t.lower()}_{a['arquivo'].lower()}",
            "reference_use": ref,
            "fiction_note": FICCAO,
            "identity_main": a["identidade"],
            "wardrobe": a["roupa"],
            "scene": d["scene"],
            "prop": d["prop"],
            "posture": d["posture"],
            "composition": d["composition"],
            "camera": d["camera"],
            "state": d["state"],
            "lighting": a["luz"],
            "realism": REALISMO,
            "aspect_ratio": "9:16 vertical",
            "negative": d["negative"],
        }
        out.append(dict(codigo=cod, take=t, titulo=TITULOS[t], j=j))
    return out


def videos(a):
    n = a["nome"]
    art = "o avatar" if a["genero"] == "homem" else "a avatar"
    Art = art.capitalize()
    pr = "ele" if a["genero"] == "homem" else "ela"
    vs = []
    for i, t in enumerate(TAKES, 1):
        acao = ACOES[t].format(n=n, pr=pr)
        som = f"som ambiente: {a['som']}{SOM_EXTRA.get(t, '')}, sem música"
        cam = f"câmera: {CAMERA.get(t, CAMERA_POV)}"
        if t in ("T1", "T12"):
            txt = (f"{art} {n} ({a['genero']}) fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
                   f"em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, "
                   f"{EMOCAO[t]}, no mesmo ritmo do vídeo modelo, a seguinte frase: \"{FALAS[t]}\"\n\n"
                   f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
                   f"o que acontece no vídeo: {acao}\n\n{cam}\n\n{som}")
        elif t == "T8":
            txt = (f"{art} {n} ({a['genero']}) narra fora de quadro, em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
                   f"em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, "
                   f"{EMOCAO[t]}, no mesmo ritmo do vídeo modelo, a seguinte frase: \"{FALAS[t]}\"\n\n"
                   f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. "
                   f"O rosto não aparece: lip sync não se aplica, a voz é narração por cima da mão.\n\n"
                   f"o que acontece no vídeo: {acao}\n\n{cam}\n\n{som}")
        else:
            txt = (f"(sem fala no take: a fala do {VOZ_DE[t]} entra como voz-over na edição)\n\n"
                   f"nenhuma voz e nenhuma fala no clipe, só o som ambiente e o som da ação.\n\n"
                   f"o que acontece no vídeo: {acao[0].upper() + acao[1:]}\n\n{cam}\n\n{som}")
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


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    art = "o avatar" if a["genero"] == "homem" else "a avatar"
    L = [f"# {a['nome']} | FityWell Growth Froyo bites | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (13,8 s, pessoa real)", "",
         f"Âncora: `{a['ancora']}`", "",
         "Funil: growth, save + follow. Origem orgânica, rodada de validação, gancho fiel ao modelo. Sem produto em quadro.", "",
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
          f"- Mãos nos planos de cima: {a['maos']}, sobre {a['superficie']}.",
          f"- Luz: {a['luz']}",
          f"- Voz (mesmo timbre em V01, V08 e V12): {a['voz']}, sotaque americano {a['sotaque']}.",
          "- Sem 2ª pessoa.", "",
          "## Trava do prop herói", "",
          f"- Froyo bite: {BITE}. Cortado: {CORTE}.",
          "- Receita: framboesa, mirtilo, chia, xarope de bordo, iogurte grego. Tigela branca de cerâmica, "
          "assadeira de metal com papel manteiga, tigela marrom-escura de iogurte. Nenhuma embalagem em quadro.",
          "", "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "",
          "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · ÂNCORA {a['nome'].upper()} + FRAME DO MODELO", "",
              anexo(a, k), "", f"Cena: {k['titulo']}.", "", "```json",
              json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["## Bloco global de vídeo", "", "```text",
          f"{art} {a['nome']} ({a['genero']}) fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
          "em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, "
          "[emoção da fala], no mesmo ritmo do vídeo modelo, a seguinte frase: \"[FALA EXATA DO ROTEIRO]\"", "",
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
          "1. Fala de V01, V08 e V12 igual ao ROTEIRO, palavra por palavra. Os outros V são sem fala.",
          "2. Um take por passo da receita; nenhum take falado acima de 29 palavras.",
          "3. Origem orgânica: bandeira só onde a âncora já tem (planos de rosto); nos planos de cima, não entra.",
          "4. Zero travessão.", "5. Growth: sem keyword, CTA = save + follow.",
          "6. Produto fora de quadro, nenhuma embalagem com marca ou texto.",
          "7. Negative sem termo sensível.",
          "8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "9. Gancho fiel no conteúdo: metades coladas na lente, macro do corte, mordida.",
          "10. Um K = um V; o reveal do T11 é uma imagem só, do bite inteiro com a faca encostada.", ""]
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


def capcut():
    return [
        "1. Clipes numerados na ordem: V01 a V12.",
        "2. Cortar cada clipe no tempo da cena do modelo: " + "; ".join(f"V{t[1:].zfill(2)} {MOMENTO[t]}" for t in TAKES) + ".",
        "3. Voz-over: soltar o áudio do V01 e deixá-lo correr por baixo do V02 ao V07; soltar o áudio do V08 e "
        "deixá-lo correr por baixo do V09 ao V11. Os clipes sem fala entram com o áudio abaixado a zero, só o "
        "som da ação bem baixo se ajudar.",
        "4. Ritmo de corte seco: dentro de cada passo, picotar o mesmo clipe em pedaços de 0,2 a 0,7 s, como no modelo.",
        "5. Zero tempo morto: V01, V08 e V12 começam já falando. Isolate Voice / Keep Vocal no áudio.",
        "6. Legenda em frase curta, branca, negrito sem serifa, centralizada no meio do quadro, trocando por pedaço "
        "de frase, igual ao modelo. Escrever `tumor`, grafia americana.",
        "7. Sem Voice Changer: a voz vem do prompt de cada V.",
        "8. Música só depois do gancho (a partir do V04), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "9. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        if t in FALAS:
            L.append(f"| {t} | {FALAS[t]} | {TRANSCRICAO_PT[t]} |")
        else:
            L.append(f"| {t} | (voz-over do {VOZ_DE[t]}) | (voz-over do {VOZ_DE[t]}) |")
    return L


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
