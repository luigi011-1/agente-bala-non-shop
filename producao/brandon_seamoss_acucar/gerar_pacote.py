"""Gera o pacote da producao brandon_seamoss_acucar (Angulo 1, Natural Rems Sea Moss, VENDA, validacao).

Formato: talking head de uma avatar so (holistic.brandon, avatar fixo da conta, box de treino). Gancho = duas
cenas de demonstracao de dose (colher e despejo), depois plano unico, depois produto + CTA da marca.
Fonte unica da fala: ROTEIRO.md aprovado (lido do disco). Cada K sai da ficha escrita olhando
input/frames_modelo/Kxx_modelo.png, gravada em FICHA_FRAMES.md com a evidencia conferida por assert.
Prompt de imagem em JSON (Flow v17). Gabarito: brandon_seamoss_vizinha/gerar_pacote.py.

Saidas: FICHA_FRAMES.md, PROMPTS_BRANDON.md, FLOW_BRANDON.md e PROMPTS_PRODUCAO.md.
Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")

HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 12)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES), sorted(set(TAKES) - set(FALAS))
TRANSCRICAO_PT = dict(re.findall(r"^\| (T\d+) \| [^|]+ \| .+? \| (.+?) \|$",
                                 ROTEIRO.split("## Tabela bilíngue")[1].split("\n## ")[0], re.M))
assert set(TRANSCRICAO_PT) == set(TAKES), set(TAKES) - set(TRANSCRICAO_PT)
PRODUTO_T = {"T9", "T10", "T11"}

FICCAO_B = "This is a fictional AI-generated character, no real person is depicted."
ANCORA = "producao/_ancoras/holistic_brandon_ancora.jpg"
FOTO_PRODUTO = "producao/_ancoras/natural_rems_seamoss_produto.jpg"


def frame_modelo(cod):
    return f"input/frames_modelo/{cod}_modelo.png"


REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG_COMUM = ("no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, "
             "no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden "
             "hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone")
BOCA = "caught mid-sentence, lips naturally parted, animated expression"

B = dict(
    nome="Brandon", arquivo="BRANDON",
    identidade=("The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, "
                "athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown "
                "eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling "
                "over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo "
                "sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral "
                "tattoo below her left collarbone."),
    roupa=("Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain "
           "with a small gold cross pendant and small stud earrings."),
    cena=("Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY "
          "REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY "
          "DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly "
          "visible and in focus. In front of her stands a plain matte black table."),
    voz="voz feminina clara e firme de uma mulher de uns trinta anos",
    sotaque="de uma mulher negra americana",
    som="box de treino em casa, tranquilo",
)
LUZ_BOX = ("Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the "
           "table with no harsh shadows. The red neon glows on the wall but does not tint her skin.")
NEG_BOX = (NEG_COMUM + ", no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, "
           "no houses, no silver cross")
NEG_SEM_ROTULO = ", no printed labels or lettering on the glass, bottle or jars"
NEG_PRODUTO = (", no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering "
               "the label")
REF_B = ("Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black "
         "table. Use the second attached image only as a composition reference for the camera position, framing and "
         "how the objects are held and poured; do not copy its person, wooden courtyard, red robe, bottle brand, "
         "table or the caption text.")
REF_B_PROD = (REF_B + " Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, "
              "without the MADE IN USA banner at the top, without the second jar behind it and without the loose "
              "gummies.")
FRASCO = ("the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale "
          "cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss "
          "Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill "
          "shapes and green seaweed illustrations on both sides, label facing the camera, fully readable")
GARRAFA = ("a tall clear glass bottle with a narrow neck filled with white granulated sugar, with a plain blank "
           "kraft-paper label that has no text on it")
POTE = "a large clear glass jar with a wide mouth, no lid, no label"
COPINHO = "a small clear shot glass"
COLHER = "a metal spoon"
CAM_B = "phone at her chest height, straight-on, standard 1x lens, light handheld"
POSE_MESA = "stands behind the black table"

BR = {
    "T1": dict(titulo="gancho 1, a dose da goma na colher",
               comp=("Straight-on medium shot: the phone lens is about 40 centimeters from the bottle, which she tilts "
                     "toward the lens in her right hand and which fills the right 35 percent of the frame, closer to "
                     "the camera than her face; her face and shoulders fill the upper half of the frame, the black "
                     "table edge is at the bottom. The background is reduced by framing, never by blur."),
               prop=(f"{GARRAFA[0].upper()}{GARRAFA[1:]}, tilted in her right hand with a thin stream of sugar falling "
                     f"onto {COLHER} held below the neck in her left hand; {COPINHO} stands on the black table and the "
                     f"edge of {POTE} is cut by the lower left corner of the frame."),
               pose="Brandon stands behind the black table, tilting the bottle toward the lens with her right hand and holding the spoon under the neck with her left",
               est="calm and a little playful, talking while she pours",
               f6="a tall clear glass bottle with a narrow neck filled with white granulated sugar",
               lista="garrafa de açúcar, colher, copinho de shot, pote grande cortado na borda, avatar, mesa preta",
               heroi="a garrafa de açúcar inclinada na mão direita, colada na lente, e a colher embaixo do gargalo",
               termos=["tilting the bottle toward the lens", "metal spoon"],
               desvio="monge sentado num pátio de madeira, garrafa de vodka de marca e mesa de madeira → Brandon em pé atrás da mesa preta no box (avatar fixo); vodka vira açúcar, rótulo kraft sem texto; garrafa mais perto da lente (piso do gate)"),
    "T2": dict(titulo="gancho 2, o despejo grande no pote",
               comp=("Straight-on close medium shot: the phone lens is about 30 centimeters from the large jar, which "
                     "she grips with her left hand and which fills the lower left 30 percent of the frame, closer to "
                     "the camera than her face; the bottle pours into it from the upper right; her face and shoulders "
                     "fill the upper half of the frame. The background is reduced by framing, never by blur."),
               prop=(f"{POTE[0].upper()}{POTE[1:]}, gripped by its side in her left hand, already half full of white "
                     f"granulated sugar, with {GARRAFA} tilted in her right hand pouring a thick stream of sugar into "
                     f"it; {COPINHO} and {COLHER} lie on the black table."),
               pose="Brandon leans forward over the black table, gripping the jar with her left hand and pouring the bottle into it with her right",
               est="animated, eyebrows raised, talking while she pours",
               f6="a large clear glass jar with a wide mouth",
               lista="pote grande com açúcar, garrafa de açúcar despejando, copinho, colher, avatar, mesa preta",
               heroi="o pote grande segurado na borda de baixo recebendo o despejo grosso de açúcar da garrafa",
               termos=["gripped by its side in her left hand", "pouring a thick stream of sugar"],
               desvio="monge sentado, garrafa de vodka de marca → Brandon em pé atrás da mesa preta no box (avatar fixo); vodka vira açúcar, sem marca"),
    "T3": dict(titulo="gancho 3, o despejo continua e o pote enche",
               comp=("Straight-on close medium shot: the phone lens is about 30 centimeters from the large jar, which "
                     "she grips with her left hand and which fills the lower left 35 percent of the frame, closer to "
                     "the camera than her face; the bottle pours into it from the upper right; her face and shoulders "
                     "fill the upper half of the frame. The background is reduced by framing, never by blur."),
               prop=(f"{POTE[0].upper()}{POTE[1:]}, gripped by its side in her left hand, now three quarters full of "
                     f"white granulated sugar, with {GARRAFA} tilted in her right hand still pouring sugar into it; "
                     f"{COPINHO} and {COLHER} lie on the black table."),
               pose="Brandon leans forward over the black table, gripping the jar with her left hand and finishing the pour with her right",
               est="knowing and confident, a small smile, talking while she pours",
               f6="a large clear glass jar with a wide mouth",
               lista="pote grande quase cheio de açúcar, garrafa de açúcar despejando, copinho, colher, avatar, mesa preta",
               heroi="o pote grande quase cheio de açúcar, a garrafa ainda despejando",
               termos=["three quarters full of white granulated sugar", "finishing the pour"],
               desvio="monge sentado, garrafa de vodka de marca → Brandon em pé atrás da mesa preta no box (avatar fixo); vodka vira açúcar, sem marca"),
}
MESA = (f"On the black table, at the left {POTE}, now full of white granulated sugar, at the "
        f"right {GARRAFA}, between them {COPINHO} and {COLHER}.")
for t, (tit, est, pose) in {
    "T4": ("pontos 1 e 2", "lively, counting on one finger", "Brandon sits back from the table and counts on one raised finger with her right hand, left hand open"),
    "T5": ("pontos 3 e 4", "lively and a little teasing", "Brandon gestures with both open hands, then counts on two fingers"),
    "T6": ("ponto 5, a virada", "serious and warm, lowering her voice", "Brandon leans a little toward the lens with both hands open above the table"),
    "T7": ("autoridade da coach", "calm and sure", "Brandon rests both forearms on the black table edge and speaks straight to the lens"),
    "T8": ("o princípio", "warm and certain", "Brandon opens both hands slowly in front of her as if offering something"),
}.items():
    BR[t] = dict(
        titulo=tit,
        comp=("Straight-on medium shot from the chest up: the phone lens is about 45 centimeters from the large sugar "
              "jar on the table, which fills the lower left 25 percent of the frame, closer to the camera than her "
              "face; the bottle stands at the right edge; her face and shoulders fill the upper 55 percent of the "
              "frame. The background is reduced by framing, never by blur."),
        prop=MESA, pose=pose, est=est,
        f6="now full of white granulated sugar",
        lista="pote grande cheio de açúcar, garrafa de açúcar, copinho, colher, avatar, mesa preta",
        heroi="o pote grande cheio de açúcar na mesa preta, no primeiro plano, e a Brandon gesticulando atrás",
        termos=["full of white granulated sugar"],
        desvio="monge sentado, mesa de madeira com garrafa de vodka de marca → Brandon atrás da mesa preta no box (avatar fixo); vodka vira açúcar, sem marca; pote e garrafa mais perto da lente que no modelo (piso do gate)")
BR["T9"] = dict(
    titulo="o produto, o frasco sobe no nome",
    comp=("Straight-on medium shot: the phone lens is about 35 centimeters from the jar, which she holds low in her "
          "right hand just above the black table and fills the lower right 20 percent of the frame, closer to the "
          "camera than her face; her face and shoulders fill the upper half of the frame. The black table is empty. "
          "The background is reduced by framing, never by blur."),
    prop=f"In her right hand, held low just above the black table, {FRASCO}. Nothing else on the table.",
    pose="Brandon holds the jar low in her right hand, about to raise it beside her face",
    est="proud, about to show it", lista="frasco Natural Rems Sea Moss, avatar, mesa vazia",
    heroi="o frasco Natural Rems Sea Moss baixo na mão direita, rótulo de frente",
    termos=["short wide jar of dark amber plastic with a black screw cap", "Sea Moss Gummies"],
    f6="Nothing else on the table",
    desvio="sem produto no modelo (o monge nunca mostra o livro) → frasco Natural Rems Sea Moss, passo 1 da marca; potes de açúcar saem da mesa para o frasco ficar limpo")
FRASCO_ALTO = dict(
    comp=("Straight-on medium shot: the jar is held up beside her right cheek and pushed slightly toward the camera, "
          "the phone lens is about 30 centimeters from the jar, which fills 20 percent of the frame at the right of "
          "her face, closer to the camera than her face, label facing the camera and fully readable. The background "
          "is reduced by framing, never by blur."),
    prop=f"In her right hand, held still beside her right cheek, {FRASCO}. Her left hand rests on the black table.",
    pose="Brandon holds the jar still beside her right cheek, label toward the lens",
    lista="frasco Natural Rems Sea Moss, avatar, mesa vazia",
    heroi="o frasco Natural Rems Sea Moss parado ao lado do rosto, rótulo de frente e legível",
    termos=["short wide jar of dark amber plastic with a black screw cap", "Sea Moss Gummies"],
    f6="Her left hand rests on the black table",
    desvio="sem produto no modelo → Natural Rems perto da lente, rótulo legível e parado (passo 1 da marca)")
BR["T10"] = dict(FRASCO_ALTO, titulo="comment yes + follow", est="inviting, smiling on yes")
BR["T11"] = dict(FRASCO_ALTO, titulo="CTA da marca, Amazon e legenda", est="clear and slow on the brand name")

EMOCAO = {
    "T1": "entonação calma e um pouco brincalhona, mostrando a dose pequena",
    "T2": "entonação animada, sobrancelhas erguidas, mostrando o tanto",
    "T3": "entonação confiante, como quem promete uma virada",
    "T4": "entonação animada, contando nos dedos",
    "T5": "entonação animada e um pouco provocadora",
    "T6": "entonação séria e acolhedora, baixando a voz",
    "T7": "entonação calma e segura de quem tem autoridade",
    "T8": "entonação calorosa e firme",
    "T9": "entonação orgulhosa, dizendo Natural Rems Sea Moss devagar e por inteiro",
    "T10": "entonação convidativa, sorrindo no yes",
    "T11": "entonação clara, dizendo Natural Rems Sea Moss devagar e por inteiro",
}
ACOES_B = {
    "T1": "{n} despeja uma fina linha de açúcar da garrafa na colher e a colher pinga uma pitada no copinho de shot, falando para a câmera.",
    "T2": "{n} segura o pote grande pela lateral e despeja a garrafa de açúcar dentro dele em jato grosso, falando para a câmera.",
    "T3": "{n} continua o despejo até o pote ficar quase cheio, falando para a câmera.",
    "T4": "{n} fala para a câmera contando um ponto de cada vez nos dedos.",
    "T5": "{n} fala para a câmera gesticulando com as duas mãos e contando nos dedos.",
    "T6": "{n} se inclina um pouco para a câmera e fala com as mãos abertas.",
    "T7": "{n} fala para a câmera com os antebraços na borda da mesa.",
    "T8": "{n} fala para a câmera abrindo as duas mãos devagar.",
    "T9": "{n} ergue o frasco devagar da altura da cintura até o lado do rosto no nome do produto e o deixa parado, rótulo de frente.",
    "T10": "{n} fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente, sorrindo no yes.",
    "T11": "{n} fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente, do começo ao fim, sem baixar o frasco.",
}
MOMENTO = {"T1": "0,00 a 4,40 s", "T2": "4,40 a ~9,80 s", "T3": "~9,80 a 14,30 s"}


def k_brandon(t):
    d = BR[t]
    neg = NEG_BOX + (NEG_PRODUTO if t in PRODUTO_T else NEG_SEM_ROTULO)
    return dict(
        fiction_note=FICCAO_B,
        reference_use=REF_B_PROD if t in PRODUTO_T else REF_B,
        identity_main=B["identidade"],
        wardrobe=B["roupa"],
        scene=B["cena"],
        prop=d["prop"],
        posture=d["pose"] + ".",
        composition=d["comp"],
        camera=CAM_B,
        lighting=LUZ_BOX,
        state=f"Start frame: Brandon is {BOCA}, looking straight into the lens, {d['est']}.",
        realism=REALISMO,
        aspect_ratio="9:16 vertical",
        negative=neg,
    )


def keyframes():
    out = []
    for i, t in enumerate(TAKES, 1):
        cod = f"K{i:02d}"
        j = dict(shot_id=f"{cod}_{t.lower()}", **k_brandon(t))
        out.append(dict(codigo=cod, take=t, titulo=BR[t]["titulo"], j=j))
    return out


def anexos(k):
    t = k["take"]
    lst = [f"ÂNCORA HOLISTIC BRANDON `{ANCORA}`", f"FRAME DO MODELO `{frame_modelo(k['codigo'])}` (só composição)"]
    if t in PRODUTO_T:
        lst.append(f"FOTO DO PRODUTO `{FOTO_PRODUTO}` (só o pote da frente)")
    return lst


def ficha(ks):
    L = ["# FICHA DO FRAME · brandon_seamoss_acucar", "",
         "Regra e método: `GATE_VISUAL.md` Parte 6. Cada K sai daqui, nunca da memória. O frame do modelo manda no",
         "CONTEÚDO (forma, quadro, distância, câmera, pose, o que está em quadro); o gate manda no ACABAMENTO e impõe o",
         "piso de proximidade do herói. A evidência de cada OK é um trecho que existe literalmente no K",
         "(conferido por `gerar_pacote.py` com assert antes de gravar).", ""]
    for k in ks:
        t, cod, j = k["take"], k["codigo"], k["j"]
        texto = json.dumps(j, ensure_ascii=False)
        d = BR[t]
        comp = j["composition"]
        m_pct = re.search(r"fills? (?:the (?:lower |upper )?(?:right |left )?)?\d+ percent of the frame", comp)
        m_cm = re.search(r"about \d+ centimeters from [a-z ]+?(?=[,.])", comp)
        assert m_pct and m_cm, (cod, comp)
        ev = dict(F2=m_pct.group(0), F3=m_cm.group(0), F4="standard 1x lens", F5=d["pose"][:55].rsplit(" ", 1)[0],
                  F6=d.get("f6") or d["prop"].split(";")[0].split(",")[0].rstrip("."))
        quadro = (f"no modelo o prop ocupa uns 25 a 35% do quadro, colado na lente, e a pessoa fica atrás; "
                  f"no K: {m_pct.group(0)} (mesmo enquadramento, piso de proximidade do gate)")
        ev = dict(ev, G1='"Neutral overcast daylight"', G3='"everything in sharp focus"', G4='"Real skin with visible pores"',
                  G5='"no warm orange color cast"', G6='"no captions"', G7='"small American flag"',
                  G8='"caught mid-sentence, lips naturally parted"')
        for it in ("F2", "F3", "F4", "F5", "F6"):
            ev[it] = f'"{ev[it]}"'
        ev["F1"] = " · ".join(f'"{x}"' for x in d["termos"])
        for item, e in ev.items():
            for trecho in re.findall(r'"([^"]+)"', e):
                assert trecho.lower() in texto.lower(), (cod, item, trecho)
        L += [f"## {cod}", f"Frame: `{frame_modelo(cod)}`", f"Take: {t}", f"Herói: {d['heroi']}",
              "Termos de forma: " + ev["F1"], f"Quadro: {quadro}", f"Distância da lente: {m_cm.group(0)}",
              f"Câmera: {j['camera']}", f"Pose: {d['pose']}", f"Lista fechada: {d['lista']}", f"Frame 0: {j['state']}",
              f"Desvio (acabamento ou avatar fixo): {d['desvio']}", "",
              "| Item | Status | Evidência (trecho literal do K) |", "|---|---|---|"]
        nomes = ["F1 forma do heroi", "F2 quanto do quadro", "F3 distancia da lente", "F4 camera",
                 "F5 pose do avatar", "F6 lista fechada", "G1 luz neutra", "G2 ceu ou janela", "G3 foco",
                 "G4 realismo", "G5 sem tom quente", "G6 sem texto", "G7 bandeira", "G8 boca no K de fala"]
        for nome in nomes:
            it = nome[:2]
            if it == "G2":
                L.append(f"| {nome} | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |")
            else:
                L.append(f"| {nome} | OK | {ev[it]} |")
        L.append("")
    return "\n".join(L)


def videos():
    vs = []
    n = B["nome"]
    for i, t in enumerate(TAKES, 1):
        acao = ACOES_B[t].format(n=n)
        if "CENA CURTA" in HEADS[t]:
            acao += " Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim."
        txt = (f"a avatar {n}, mulher, fala em inglês com sotaque americano {B['sotaque']}, {B['voz']}, "
               f"{EMOCAO[t]}, voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"{FALAS[t]}\"\n\n"
               "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por "
               "inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
               f"o que acontece no vídeo: {acao}\n\n"
               f"câmera: {'fixa' if t in PRODUTO_T else 'fixa, leve handheld natural'}\n\n"
               f"som ambiente: {B['som']}, sem música")
        vs.append((f"V{i:02d}", t, f"K{i:02d}", txt))
    return vs


ORDEM_K = ["fiction_note", "reference_use", "identity_main", "wardrobe", "scene", "prop", "posture",
           "composition", "camera", "lighting", "state", "realism", "aspect_ratio", "negative"]


def texto_flow(j):
    assert set(ORDEM_K) == set(j) - {"shot_id"}, set(j) ^ set(ORDEM_K)
    d = {"format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."}
    d.update({k: j[k] for k in ORDEM_K})
    return json.dumps(d, ensure_ascii=False, indent=2)


def bloco_anexo(k):
    lst = anexos(k)
    nums = ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]
    L = [f"> ### 📎 ANEXAR: **{len(lst)} IMAGENS**"]
    L += [f"> **{nums[i]} {a}**" for i, a in enumerate(lst)]
    L += [">", "> ### 🆕 GERAR DO ZERO"]
    return "\n".join(L)


def capcut():
    return [
        "1. Clipes numerados na ordem: V01 a V11.",
        "2. Gancho no tempo do modelo: V01 " + MOMENTO["T1"] + "; V02 " + MOMENTO["T2"] + "; V03 " + MOMENTO["T3"] + ". Cortar logo depois da última palavra de cada clipe.",
        "3. Corte seco entre clipes, sem transição. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.",
        "4. Legenda de tela branca sem serifa, duas a três palavras por vez, no meio do quadro, igual ao modelo. "
        "No V10, `yes` grande e isolado na tela. No V11, duas setas vermelhas apontando para baixo (para a legenda do post).",
        "5. Sem Voice Changer: a voz da Brandon vem do prompt de cada V.",
        "6. Música opcional só a partir do V04, nunca no gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "7. Rótulo pequeno `AI-generated` num canto do vídeo.",
        "8. No V09 a V11 o frasco não pode ser cortado nem coberto: nenhum B-roll por cima (regra da marca).",
    ]


LEGENDA = [
    "Primeira linha, sempre: `#ad #syntheticperformer #naturalrems`",
    "Logo abaixo: o link da Amazon do Natural Rems Sea Moss (o V11 manda tocar no link da legenda).",
    "Chave de conteúdo de IA da plataforma LIGADA.",
]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {TRANSCRICAO_PT[t]} |")
    return L


def pacote():
    ks, vs = keyframes(), videos()
    L = ["# holistic.brandon | Natural Rems Sea Moss Venda, açúcar no sea moss | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (63,2 s, avatar IA, monge demonstra dose e lista 5 pontos)", "",
         f"Âncora: `{ANCORA}` (T1 a T11) · Foto do produto: `{FOTO_PRODUTO}` (T9 a T11)", "",
         "Funil: VENDA. Gancho de dose (colher e despejo de açúcar) → 5 pontos do sea moss genérico → autoridade de "
         "coach → Natural Rems Sea Moss com comment `yes` + follow, busca na Amazon e link na legenda. Rodada de "
         "validação, gancho fiel ao modelo. Perfil CLÁSSICO.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    for k in ks:
        L.append(f"| {k['take']} | {k['codigo']} | " + " + ".join(a.split(" `")[0] for a in anexos(k)) + " | GERAR DO ZERO |")
    L += ["", "Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro. "
          "O frame do modelo de cada K entra só como composição.", "",
          "## Trava de identidade e continuidade", "",
          f"- Brandon, identidade: {B['identidade']}",
          f"- Brandon, roupa (fixa da conta): {B['roupa']}",
          f"- Brandon, cenário-base (fixo da conta): {B['cena']}",
          f"- Luz do box: {LUZ_BOX}",
          "- Voz: o mesmo timbre da Brandon em todos os V.", "",
          "## Trava do prop herói", "",
          f"- Gancho e corpo: {GARRAFA}; {POTE}; {COPINHO}; {COLHER}. Nada com texto ou marca.",
          f"- Produto: {FRASCO}. Só o pote da frente da foto oficial; sem a faixa MADE IN USA, sem o segundo pote, sem gomas soltas.", "",
          "## Trava da 2ª pessoa (REF-A)", "",
          "- Não há 2ª pessoa nem REF-A: só a Brandon em quadro.", "",
          "# Prompts de imagem", ""]
    for k in ks:
        refs = " + ".join(a.split(" `")[0].split(" (")[0] for a in anexos(k))
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · {refs.upper()}", "",
              bloco_anexo(k), "", f"Cena: {k['titulo']}.", "", "```json",
              json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["## Bloco global de vídeo", "", "```text",
          f"a avatar {B['nome']}, mulher, fala em inglês com sotaque americano {B['sotaque']}, {B['voz']}, "
          "[emoção da fala], voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"[FALA EXATA DO ROTEIRO]\"", "",
          "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.", "",
          "o que acontece no vídeo: [ação enxuta]", "", "câmera: [fixa]", "", f"som ambiente: {B['som']}, sem música",
          "```", "", "# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Mapa de âncoras", "", "| Código | Anexar, nesta ordem | Modelo |", "|---|---|---|"]
    for k in ks:
        L.append(f"| {k['codigo']} | " + " + ".join(anexos(k)) + " | Nano Banana 2, 9:16 |")
    L += ["", "Vídeo: Omni Flash, 8 segundos, um resultado por V, a imagem escolhida do K de mesmo número como INITIAL FRAME.",
          "", "## Montagem no CapCut", ""] + capcut() + ["", "Legenda do post:", ""] + [f"- {x}" for x in LEGENDA] + [
          "", "## Gates de qualidade", "",
          "1. Mesmo rosto, cabelo, roupa e box da âncora em todos os K.",
          "2. Fala de cada V igual ao ROTEIRO, palavra por palavra.",
          "3. Um take por cena do modelo no gancho; T1 marcado CENA CURTA; nenhum take acima de 29 palavras.",
          "4. Bandeira dos EUA no campo scene de todo K (quadro branco do box).",
          "5. Zero travessão.",
          "6. Natural Rems: frasco parado e legível do V09 ao V11; \"Search Natural Rems Sea Moss on Amazon\" antes do link; nada depois do link; comment `yes` + follow no V10, antes da Amazon.",
          "7. Compliance da marca: nada médico em fala ou quadro, sem antes/depois, sem cura ou resultado garantido, sem concorrente, sem marca no vidro; legenda com `#ad #syntheticperformer #naturalrems` no topo.",
          "8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "9. Gancho fiel: colherzinha de açúcar no copinho, depois o despejo grosso da garrafa no pote grande.",
          "10. Um K = um V.",
          "11. `python3 checar_entrega.py producao/brandon_seamoss_acucar` sem FALHA.", ""]
    flow = ["# Blocos limpos para o Google Flow | holistic.brandon", "", "Fonte interna: `PROMPTS_BRANDON.md`", "",
            "## BLOCO DE IMAGEM", "", "```text"]
    for k in ks:
        flow += [k["codigo"], texto_flow(k["j"]), ""]
    flow += ["```", "", "## BLOCO DE VÍDEO", "", "```text"]
    for cod, _, _, txt in vs:
        flow += [cod, txt, ""]
    flow += ["```", "", "## Tabela de leitura humana", "", "| Código | Take | Anexar |", "|---|---|---|"]
    for k in ks:
        flow.append(f"| {k['codigo']} / V{k['codigo'][1:]} | {k['take']}, {k['titulo']} | " + " + ".join(anexos(k)) + " |")
    flow += ["", "## Transcrição final por take", ""] + transcricao()
    return "\n".join(L) + "\n", "\n".join(flow) + "\n", ficha(ks) + "\n"


def main():
    p, f, fi = pacote()
    (AQUI / "FICHA_FRAMES.md").write_text(fi, encoding="utf-8")
    (AQUI / "PROMPTS_BRANDON.md").write_text(p, encoding="utf-8")
    (AQUI / "FLOW_BRANDON.md").write_text(f, encoding="utf-8")
    (AQUI / "PROMPTS_PRODUCAO.md").write_text(p, encoding="utf-8")
    print("ok: ficha + pacote; %d K, %d V" % (len(keyframes()), len(videos())))


if __name__ == "__main__":
    main()
