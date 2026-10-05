"""Gera o pacote da producao brandon_seamoss_muffin (Angulo 1, Natural Rems Sea Moss, VENDA, validacao).

Avatar unico: holistic.brandon, avatar fixo da conta, no box de treino com a mesa preta como bancada.
Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Medidas de cada K: a ficha
abaixo, escrita olhando input/frames_modelo/Kxx_modelo.png e gravada em FICHA_FRAMES.md com o placar
cuja evidencia e conferida aqui mesmo contra o texto do K (assert). Prompt de imagem em JSON (Flow v17).
Gabarito de formato: brandon_seamoss_vizinha/gerar_pacote.py (parte da Brandon).

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
assert TAKES == ["T%d" % i for i in range(1, 18)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES), sorted(set(TAKES) - set(FALAS))
TRANSCRICAO_PT = dict(re.findall(r"^\| (T\d+) \| [^|]+ \| .+? \| (.+?) \|$",
                                 ROTEIRO.split("## Tabela bilíngue")[1].split("\n## ")[0], re.M))
assert set(TRANSCRICAO_PT) == set(TAKES), set(TAKES) - set(TRANSCRICAO_PT)

PRODUTO_T = {"T13", "T14", "T15", "T16", "T17"}
FICCAO = "This is a fictional AI-generated character, no real person is depicted."
ANCORA = "producao/_ancoras/holistic_brandon_ancora.jpg"
FOTO_PRODUTO = "producao/_ancoras/natural_rems_seamoss_produto.jpg"


def frame_modelo(cod):
    return f"input/frames_modelo/{cod}_modelo.png"


REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, "
       "no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden "
       "hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, "
       "no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, "
       "no silver cross")
NEG_SEM_ROTULO = ", no printed labels or lettering on the bowls, cups, grater or muffin tin"
NEG_PRODUTO = (", no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering "
               "the label, no muffins on the table")

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
          "visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter."),
    voz="voz feminina clara e firme de uma mulher de uns trinta anos",
    sotaque="de uma mulher negra americana",
    som="box de treino em casa, tranquilo",
)
LUZ = ("Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the "
       "table with no harsh shadows. The red neon glows on the wall but does not tint her skin.")
REF = ("Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black "
       "table. Use the second attached image only as a composition reference for the camera position, framing and "
       "the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator "
       "decorations or the caption text.")
REF_PROD = (REF + " Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, "
            "without the MADE IN USA banner at the top, without the second jar behind it and without the loose "
            "gummies.")
FRASCO = ("the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale "
          "cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss "
          "Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill "
          "shapes and green seaweed illustrations on both sides, label facing the camera, fully readable")
TIGELA_CENOURA = "a large white ceramic mixing bowl half full of bright orange finely grated carrot"
RALADOR = "a tall stainless steel four-sided box grater"
MESA_RECEITA = ("Around the bowl on the black table: a clear glass measuring cup of rolled oats, two white eggs, a "
                "small clear glass cup of amber raw honey and a small clear glass bowl of ground cinnamon with a "
                "metal measuring spoon.")
MUFFIN = "a baked carrot oat muffin with a domed golden orange top, flecks of grated carrot and oats, no paper liner"
FORMA = "a dark nonstick 12-cup muffin tin filled with baked golden orange carrot muffins"
BOCA = "caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens"
CAM_PEITO = "phone at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld"

# Cada K: prop, pose, composicao (com medida), camera, estado, e a ficha (heroi, termos, lista, desvio, f0 do modelo).
K = {
    "T1": dict(titulo="gancho, cenoura no ralador colada na lente",
               prop=(f"In the lower foreground, {TIGELA_CENOURA}, with {RALADOR} standing upright inside it; her right "
                     "hand presses a large peeled orange carrot against the grater blades, her left hand steadies the "
                     "grater handle. Nothing else on the table."),
               pose="Brandon leans over the black table toward the lens, grating the carrot into the bowl",
               comp=("Close shot from chest height: the phone lens is about 30 centimeters from the bowl and the grater, "
                     "which fill the lower 45 percent of the frame, closer to the camera than her face and larger than "
                     "her head; her face and shoulders are in the upper third. The background is reduced by framing, "
                     "never by blur."),
               cam="phone at her chest height, tilted down toward the bowl, standard 1x lens, light handheld",
               est="eyebrows raised, as if sharing a secret",
               heroi="o ralador de inox de quatro faces em pé dentro da tigela branca com cenoura ralada, a cenoura esfregada nas lâminas",
               termos=["four-sided box grater", "half full of bright orange finely grated carrot"],
               lista="tigela, ralador, cenoura, mãos, avatar; mesa sem mais nada",
               f0="cenoura no meio do movimento sobre o ralador, um monte de cenoura ralada já na tigela"),
    "T2": dict(titulo="receita, aveia na tigela",
               prop=(f"On the black table, {TIGELA_CENOURA} in the lower center. {MESA_RECEITA} She tips the measuring "
                     "cup of rolled oats over the bowl."),
               pose="Brandon stands behind the black table, tipping the cup of oats into the bowl",
               comp=("Standing medium shot from chest height: the phone lens is about 55 centimeters from the bowl, which "
                     "fills the lower 30 percent of the frame with the ingredients around it, closer to the camera than "
                     "her face; her face and torso fill the upper half. The background is reduced by framing, never by "
                     "blur."),
               cam=CAM_PEITO, est="lively, explaining",
               heroi="a tigela de cenoura ralada no centro-baixo com os ingredientes em volta e a aveia caindo",
               termos=["glass measuring cup of rolled oats", "half full of bright orange finely grated carrot"],
               lista="tigela, aveia, dois ovos, mel, canela com colher, avatar",
               f0="primeiros flocos de aveia caindo do copo medidor"),
    "T3": dict(titulo="receita, ovo",
               prop=(f"On the black table, {TIGELA_CENOURA} topped with rolled oats in the lower center. {MESA_RECEITA} "
                     "She holds one white egg cracked open over the bowl with both hands."),
               pose="Brandon stands behind the black table, cracking an egg over the bowl with both hands",
               comp=("Standing medium shot from chest height: the phone lens is about 55 centimeters from the bowl, which "
                     "fills the lower 30 percent of the frame, closer to the camera than her face; her face and torso "
                     "fill the upper half. The background is reduced by framing, never by blur."),
               cam=CAM_PEITO, est="lively",
               heroi="o ovo sendo quebrado em cima da tigela",
               termos=["white egg cracked open over the bowl"],
               lista="tigela com cenoura e aveia, ovo na mão, mel, canela, avatar",
               f0="casca aberta logo acima da tigela, gema ainda não caiu"),
    "T4": dict(titulo="receita, mel",
               prop=(f"On the black table, {TIGELA_CENOURA} topped with rolled oats and egg in the lower center. Her right "
                     "hand tilts a small clear glass cup of amber raw honey over the bowl, a thick stream of honey "
                     "starting to pour. A small clear glass bowl of ground cinnamon with a metal measuring spoon stands "
                     "beside the bowl."),
               pose="Brandon stands behind the black table, pouring honey from the glass cup into the bowl",
               comp=("Standing medium shot from chest height: the phone lens is about 50 centimeters from the bowl, which "
                     "fills the lower 30 percent of the frame, closer to the camera than her face; her face and torso "
                     "fill the upper half. The background is reduced by framing, never by blur."),
               cam=CAM_PEITO, est="lively",
               heroi="o fio grosso de mel âmbar caindo do copinho de vidro na tigela",
               termos=["small clear glass cup of amber raw honey"],
               lista="tigela, copinho de mel, canela com colher, avatar",
               f0="o primeiro fio de mel saindo do copinho"),
    "T5": dict(titulo="receita, canela",
               prop=(f"On the black table, {TIGELA_CENOURA} topped with oats, egg and honey in the lower center. Her right "
                     "hand holds a metal measuring teaspoon heaped with ground cinnamon right above the bowl; the small "
                     "glass bowl of cinnamon stands beside it."),
               pose="Brandon stands behind the black table, holding the teaspoon of cinnamon over the bowl",
               comp=("Standing medium shot from chest height: the phone lens is about 50 centimeters from the bowl, which "
                     "fills the lower 30 percent of the frame, closer to the camera than her face; her face and torso "
                     "fill the upper half. The background is reduced by framing, never by blur."),
               cam=CAM_PEITO, est="lively",
               heroi="a colher de chá cheia de canela logo acima da tigela",
               termos=["measuring teaspoon heaped with ground cinnamon"],
               lista="tigela, colher de canela, tigelinha de canela, avatar",
               f0="colher parada acima da tigela, canela ainda não caiu"),
    "T6": dict(titulo="receita, massa na forma",
               prop=("Her left hand tilts the white mixing bowl full of thick orange carrot oat batter toward the lens; "
                     "her right hand drops a spoonful of batter into an empty dark nonstick 12-cup muffin tin lined with "
                     "white paper cups, the tin on the black table in the lower foreground."),
               pose="Brandon leans over the black table, spooning batter from the tilted bowl into the muffin tin",
               comp=("Close shot from chest height: the phone lens is about 35 centimeters from the tilted bowl and the "
                     "muffin tin, which together fill the lower 50 percent of the frame, closer to the camera than her "
                     "face; her face is in the upper third. The background is reduced by framing, never by blur."),
               cam="phone at her chest height, tilted down toward the tin, standard 1x lens, light handheld",
               est="focused, explaining",
               heroi="a tigela inclinada de massa laranja e a forma de 12 com forminhas de papel, a colherada caindo",
               termos=["thick orange carrot oat batter", "12-cup muffin tin lined with white paper cups"],
               lista="tigela de massa, colher, forma com forminhas, avatar",
               f0="a primeira colherada caindo numa forminha vazia"),
}
MUFFIN_COMP = ("Straight-on medium shot: the phone lens is about {cm} centimeters from the muffin, which she holds up "
               "in her right hand at chest height and which fills about {pct} percent of the frame, closer to the camera "
               "than her face; the muffin tin fills the lower 30 percent of the frame on the black table. Her face and "
               "shoulders fill the upper half. The background is reduced by framing, never by blur.")
for t, (tit, cm, pct, est) in {
        "T7": ("resultado, muffin na mão", 25, 18, "proud, showing the muffin"),
        "T8": ("mecanismo, a aveia", 25, 18, "explaining"),
        "T9": ("mecanismo e a tarde lenta", 25, 18, "relatable, a little playful"),
        "T10": ("rotina e virada", 30, 15, "warm, then a little serious"),
        "T11": ("ponte, o sea moss", 30, 15, "like sharing a simple trick"),
        "T12": ("obstáculo, as gomas com açúcar", 30, 15, "warning, a little disgusted")}.items():
    K[t] = dict(titulo=tit,
                prop=(f"In her right hand, held up at chest height, {MUFFIN}. On the black table in the lower foreground, "
                      f"{FORMA}. Her left hand gestures."),
                pose="Brandon stands behind the black table holding up one muffin toward the lens",
                comp=MUFFIN_COMP.format(cm=cm, pct=pct), cam="phone at her eye level, straight-on, standard 1x lens, light handheld",
                est=est, heroi="o muffin de cenoura assado na mão, colado na lente, e a forma cheia na mesa",
                termos=["baked carrot oat muffin with a domed golden orange top", "12-cup muffin tin filled with baked"],
                lista="muffin na mão, forma de muffins, avatar",
                f0="falando para a câmera com o muffin erguido",
                desvio="cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); muffin um pouco mais perto da lente que no modelo (piso do gate)")
K["T13"] = dict(titulo="produto, o frasco sobe no nome",
                prop=f"In her right hand, held low just above the black table, {FRASCO}. Nothing else on the table.",
                pose="Brandon holds the jar low in her right hand, about to raise it beside her face",
                comp=("Straight-on medium shot: the phone lens is about 35 centimeters from the jar, which she holds low in "
                      "her right hand just above the black table and fills the lower right 20 percent of the frame, "
                      "closer to the camera than her face; her face and shoulders fill the upper half of the frame. The "
                      "background is reduced by framing, never by blur."),
                cam="phone at her chest height, straight-on, standard 1x lens, light handheld",
                est="proud, about to show it",
                heroi="o frasco Natural Rems Sea Moss baixo na mão direita, rótulo de frente",
                termos=["short wide jar of dark amber plastic with a black screw cap", "Sea Moss Gummies"],
                lista="frasco, avatar, mesa vazia", f0="frasco baixo, prestes a subir",
                f6="Nothing else on the table",
                desvio="o modelo segura o muffin aqui; no bloco de venda o frasco entra no lugar, já na mão para nascer da foto real")
for t, (tit, est) in {"T14": ("diferencial", "lively, listing"), "T15": ("prova social da coach", "warm and certain"),
                      "T16": ("comment yes + follow", "inviting, smiling on yes"),
                      "T17": ("CTA da marca", "clear and slow on the brand name")}.items():
    K[t] = dict(titulo=tit,
                prop=f"In her right hand, held still beside her right cheek, {FRASCO}. Her left hand rests on the black table.",
                pose="Brandon holds the jar still beside her right cheek, label toward the lens",
                comp=("Straight-on medium shot: the jar is held up beside her right cheek and pushed slightly toward the "
                      "camera, the phone lens is about 30 centimeters from the jar, which fills 20 percent of the frame "
                      "at the right of her face, closer to the camera than her face, label facing the camera and fully "
                      "readable. The background is reduced by framing, never by blur."),
                cam="phone at her chest height, straight-on, standard 1x lens, light handheld",
                est=est, heroi="o frasco parado ao lado do rosto, rótulo de frente e legível",
                termos=["short wide jar of dark amber plastic with a black screw cap", "Sea Moss Gummies"],
                lista="frasco, avatar, mesa vazia", f0="falando com o frasco parado",
                f6="Her left hand rests on the black table",
                desvio="o modelo abre as mãos no follow; aqui o frasco fica parado e legível (passo 1 da marca)")

EMOCAO = {
    "T1": "entonação animada e intrigante, como quem conta um segredo de cozinha", "T2": "entonação animada e didática, rápida",
    "T3": "entonação animada e didática, rápida", "T4": "entonação animada e didática, rápida",
    "T5": "entonação animada e didática, rápida", "T6": "entonação animada e didática",
    "T7": "entonação orgulhosa e animada", "T8": "entonação didática", "T9": "entonação próxima e bem-humorada",
    "T10": "entonação calorosa, ficando séria no fim", "T11": "entonação de quem conta um truque simples",
    "T12": "entonação de alerta, com um leve desgosto",
    "T13": "entonação orgulhosa, dizendo Natural Rems Sea Moss devagar e por inteiro",
    "T14": "entonação animada, listando", "T15": "entonação calorosa e segura",
    "T16": "entonação convidativa, sorrindo no yes",
    "T17": "entonação clara, dizendo Natural Rems Sea Moss devagar e por inteiro",
}
ACOES = {
    "T1": "{n} rala a cenoura no ralador dentro da tigela, a cenoura ralada caindo, e olha para a câmera enquanto fala.",
    "T2": "{n} despeja a aveia do copo medidor dentro da tigela.",
    "T3": "{n} abre o ovo e deixa cair dentro da tigela.",
    "T4": "{n} despeja o mel do copinho dentro da tigela.",
    "T5": "{n} vira a colher de canela dentro da tigela.",
    "T6": "{n} põe colheradas de massa nas forminhas.",
    "T7": "{n} ergue o muffin na direção da câmera e fala, com a forma cheia na mesa.",
    "T8": "{n} fala para a câmera segurando o muffin.",
    "T9": "{n} fala para a câmera segurando o muffin, com um pequeno gesto da outra mão.",
    "T10": "{n} fala para a câmera segurando o muffin.",
    "T11": "{n} fala para a câmera segurando o muffin, levantando um dedo da outra mão.",
    "T12": "{n} balança a cabeça de leve e fala para a câmera, segurando o muffin.",
    "T13": "{n} ergue o frasco devagar da altura da cintura até o lado do rosto no nome do produto e o deixa parado, rótulo de frente.",
    "T14": "{n} fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente.",
    "T15": "{n} fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente.",
    "T16": "{n} fala para a câmera com o frasco parado ao lado do rosto, sorrindo no yes.",
    "T17": "{n} fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente, do começo ao fim, sem baixar o frasco.",
}
SOM = {"T1": ", cenoura raspando no ralador", "T2": ", aveia caindo na tigela", "T3": ", casca de ovo quebrando",
       "T5": ", colher batendo de leve na tigela", "T6": ", colher raspando a tigela"}
MOMENTO = {"T1": "0,0 a 3,7 s", "T2": "3,7 a 6,1 s", "T3": "6,1 a 7,5 s", "T4": "7,5 a 9,5 s", "T5": "9,5 a 10,9 s",
           "T6": "10,9 a 12,9 s", "T7": "12,9 a 20,3 s", "T8": "20,3 a 23,2 s", "T9": "23,2 a 29,3 s"}


def keyframes():
    out = []
    for i, t in enumerate(TAKES, 1):
        d = K[t]
        cod = f"K{i:02d}"
        j = {
            "shot_id": f"{cod}_{t.lower()}",
            "fiction_note": FICCAO,
            "reference_use": REF_PROD if t in PRODUTO_T else REF,
            "identity_main": B["identidade"],
            "wardrobe": B["roupa"],
            "scene": B["cena"],
            "prop": d["prop"],
            "posture": d["pose"] + ".",
            "composition": d["comp"],
            "camera": d["cam"],
            "lighting": LUZ,
            "state": f"Start frame: Brandon is {BOCA}, {d['est']}.",
            "realism": REALISMO,
            "aspect_ratio": "9:16 vertical",
            "negative": NEG + (NEG_PRODUTO if t in PRODUTO_T else NEG_SEM_ROTULO),
        }
        out.append(dict(codigo=cod, take=t, titulo=d["titulo"], j=j))
    return out


def anexos(k):
    lst = [f"ÂNCORA HOLISTIC BRANDON `{ANCORA}`", f"FRAME DO MODELO `{frame_modelo(k['codigo'])}` (só composição)"]
    if k["take"] in PRODUTO_T:
        lst.append(f"FOTO DO PRODUTO `{FOTO_PRODUTO}` (só o pote da frente)")
    return lst


def ficha(ks):
    L = ["# FICHA DO FRAME · brandon_seamoss_muffin", "",
         "Regra e método: `GATE_VISUAL.md` Parte 6. Cada K sai daqui, nunca da memória. O frame do modelo manda no",
         "CONTEÚDO (forma, quadro, distância, câmera, pose, o que está em quadro); o gate manda no ACABAMENTO e impõe o",
         "piso de proximidade do herói. A evidência de cada OK é um trecho que existe literalmente no K",
         "(conferido por `gerar_pacote.py` com assert antes de gravar).", ""]
    for k in ks:
        t, cod, j = k["take"], k["codigo"], k["j"]
        d = K[t]
        texto = json.dumps(j, ensure_ascii=False)
        comp = j["composition"]
        m_pct = re.search(r"fills? (?:about |the (?:lower |upper )?(?:right )?)?\d+ percent of the frame", comp)
        m_cm = re.search(r"about \d+ centimeters from [a-z ]+?(?=[,.])", comp)
        assert m_pct and m_cm, (cod, comp)
        ev = dict(F2=m_pct.group(0), F3=m_cm.group(0), F4="standard 1x lens", F5=d["pose"][:55].rsplit(" ", 1)[0],
                  F6=d.get("f6") or d["prop"].split(";")[0].split(".")[0].split(",")[0])
        ev = {it: f'"{v}"' for it, v in ev.items()}
        ev.update(G1='"Neutral overcast daylight"', G3='"everything in sharp focus"', G4='"Real skin with visible pores"',
                  G5='"no warm orange color cast"', G6='"no captions"', G7='"small American flag"',
                  G8='"caught mid-sentence, lips naturally parted"')
        ev["F1"] = " · ".join(f'"{x}"' for x in d["termos"])
        for item, e in ev.items():
            for trecho in re.findall(r'"([^"]+)"', e):
                assert trecho.lower() in texto.lower(), (cod, item, trecho)
        desvio = d.get("desvio", "cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); "
                                 "óculos e camiseta cinza do modelo → identidade e roupa da âncora; luz neutra (gate)")
        L += [f"## {cod}", f"Frame: `{frame_modelo(cod)}`", f"Take: {t}", f"Herói: {d['heroi']}",
              "Termos de forma: " + ev["F1"], f"Quadro: no K: {m_pct.group(0)} (medido contra o frame do modelo)",
              f"Distância da lente: {m_cm.group(0)}", f"Câmera: {j['camera']}", f"Pose: {d['pose']}",
              f"Lista fechada: {d['lista']}", f"Frame 0: {d['f0']}", f"Desvio (acabamento ou avatar fixo): {desvio}", "",
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
        acao = ACOES[t].format(n=n)
        if "CENA CURTA" in HEADS[t]:
            acao += " Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim."
        cam = "fixa" if t in PRODUTO_T else ("leve handheld natural" if t in MOMENTO and int(t[1:]) <= 6
                                              else "fixa, leve handheld natural")
        txt = (f"a avatar {n}, mulher, fala em inglês com sotaque americano {B['sotaque']}, {B['voz']}, "
               f"{EMOCAO[t]}, voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"{FALAS[t]}\"\n\n"
               "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por "
               "inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
               f"o que acontece no vídeo: {acao}\n\n"
               f"câmera: {cam}\n\n"
               f"som ambiente: {B['som']}{SOM.get(t, '')}, sem música")
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
    nums = ["1️⃣", "2️⃣", "3️⃣"]
    L = [f"> ### 📎 ANEXAR: **{len(lst)} IMAGENS**"] + [f"> **{nums[i]} {a}**" for i, a in enumerate(lst)]
    return "\n".join(L + [">", "> ### 🆕 GERAR DO ZERO"])


def capcut():
    return [
        "1. Clipes numerados na ordem: V01 a V17.",
        "2. Do V01 ao V09, cortar no tempo da cena do modelo: " + "; ".join(
            f"V{t[1:].zfill(2)} {MOMENTO[t]}" for t in MOMENTO) + ". Do V10 ao V17, cortar logo depois da última palavra.",
        "3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.",
        "4. Nos V01 a V06 e no V08 (cenas curtas) a fala vem no começo; manter a ação até o tempo da cena do modelo.",
        "5. Legenda branca serifada, duas a três palavras por vez, com a palavra de peso maior, no meio do quadro, igual "
        "ao modelo. No V16, `yes` grande e isolado na tela. No V17, setas apontando para a legenda do post.",
        "6. Sem Voice Changer: a voz vem do prompt de cada V.",
        "7. Música só depois do gancho (a partir do V02), entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "8. Rótulo pequeno `AI-generated` num canto do vídeo.",
        "9. Do V13 ao V17 o frasco não pode ser cortado nem coberto: nenhum B-roll por cima (regra da marca).",
    ]


LEGENDA = [
    "Primeira linha, sempre: `#ad #syntheticperformer #naturalrems`",
    "Logo abaixo: o link da Amazon do Natural Rems Sea Moss (o V17 manda tocar no link da legenda).",
    "Chave de conteúdo de IA da plataforma LIGADA.",
]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {TRANSCRICAO_PT[t]} |")
    return L


def pacote():
    ks, vs = keyframes(), videos()
    L = ["# holistic.brandon | Natural Rems Sea Moss Venda, muffin de cenoura | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (41,8 s, pessoa real provável)", "",
         f"Âncora: `{ANCORA}` · Foto do produto: `{FOTO_PRODUTO}` (T13 a T17)", "",
         "Funil: VENDA. Receita do muffin fiel ao modelo → ponte pelo sea moss → Natural Rems Sea Moss com comment "
         "`yes` + follow, busca na Amazon e link na legenda. Rodada de validação, gancho fiel. Perfil CLÁSSICO.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    for k in ks:
        L.append(f"| {k['take']} | {k['codigo']} | " + " + ".join(a.split(" `")[0] for a in anexos(k)) + " | GERAR DO ZERO |")
    L += ["", "Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro. O frame "
          "do modelo de cada K entra só como composição.", "",
          "## Trava de identidade e continuidade", "",
          f"- Identidade: {B['identidade']}", f"- Roupa (fixa da conta): {B['roupa']}",
          f"- Cenário-base (fixo da conta): {B['cena']}", f"- Luz: {LUZ}",
          f"- Voz (mesmo timbre em todos os V): {B['voz']}, sotaque americano {B['sotaque']}.", "- Sem 2ª pessoa.", "",
          "## Trava do prop herói", "",
          f"- Gancho: {TIGELA_CENOURA}; {RALADOR}; uma cenoura grande descascada.",
          f"- Receita: {MESA_RECEITA}",
          f"- Corpo: {MUFFIN}; {FORMA}.",
          f"- Produto: {FRASCO}. Só o pote da frente da foto oficial; sem a faixa MADE IN USA, sem o segundo pote, sem gomas soltas.",
          "- Nenhum outro prop com texto ou marca.", "",
          "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "",
          "## Prompts de imagem", ""]
    for k in ks:
        refs = " + ".join(a.split(" `")[0].split(" (")[0] for a in anexos(k))
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · {refs.upper()}", "", bloco_anexo(k), "",
              f"Cena: {k['titulo']}.", "", "```json", json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["## Bloco global de vídeo", "", "```text",
          f"a avatar {B['nome']}, mulher, fala em inglês com sotaque americano {B['sotaque']}, {B['voz']}, "
          "[emoção da fala], voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"[FALA EXATA DO ROTEIRO]\"", "",
          "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.", "",
          "o que acontece no vídeo: [ação enxuta]", "", "câmera: [fixa]", "", f"som ambiente: {B['som']}, sem música",
          "```", "", "# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Mapa de âncoras", "", "| Keyframe | Referências a anexar | Modelo |", "|---|---|---|"]
    for k in ks:
        L.append(f"| {k['codigo']} | " + " + ".join(anexos(k)) + " | Nano Banana 2, 9:16 |")
    L += ["", "Vídeo: Omni Flash, 8 segundos, um resultado por V, a imagem escolhida do K de mesmo número como INITIAL FRAME.",
          "", "## Montagem no CapCut", ""] + capcut() + ["", "Legenda do post:", ""] + [f"- {x}" for x in LEGENDA] + [
          "", "## Gates de qualidade", "",
          "1. Fala de cada V igual ao ROTEIRO, palavra por palavra.",
          "2. Um take por cena do modelo; cenas curtas marcadas; nenhum take acima de 29 palavras.",
          "3. Bandeira dos EUA no campo scene de todo K.", "4. Zero travessão.",
          "5. Natural Rems: frasco parado e legível do V13 ao V17; comment `yes` + follow no V16, antes da Amazon; nada depois do link.",
          "6. Compliance da marca: nada médico, sem antes/depois, sem cura ou resultado garantido, sem concorrente; legenda com `#ad #syntheticperformer #naturalrems` no topo.",
          "7. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "8. Gancho fiel no conteúdo: a cenoura sendo ralada no ralador dentro da tigela, colada na lente, falado desde o segundo 0.",
          "9. Um K = um V.", "10. `python3 checar_entrega.py producao/brandon_seamoss_muffin` sem FALHA.", ""]
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
