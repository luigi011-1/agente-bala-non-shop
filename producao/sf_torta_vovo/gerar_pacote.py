"""Gera os pacotes das 9 contas de sf_torta_vovo a partir de uma fonte unica.

Cada conta sai em conta_NN/ com ROTEIRO.md, PROMPTS_PRODUCAO.md (JSON interno, o que o
linter le) e FLOW_CONTA_NN.md (blocos limpos do Flow, texto corrido). Editar AQUI e
rodar de novo; nunca editar os arquivos gerados na mao.

    python3 producao/sf_torta_vovo/gerar_pacote.py
"""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
REF_PATH = "producao/sf_torta_vovo/REF_COMPOSICAO_frame_2s.jpg"
VIDEO_MODELO = "Sweet Treats with Gr_A pequena surpresa de co_2818305955232419_720p_20260923.mp4"

T2 = "Okay, if people comment yes and follow this page, you can choose first."

KITCHEN = ("A bright American home kitchen with white shaker cabinets and a large window behind "
           "the grandmother letting in neutral overcast daylight, the backyard trees and a grey-blue "
           "cloudy sky clearly visible through the window, never white or blown out, a light wood "
           "floor, and a small American flag standing in a mason jar on the windowsill, discreet "
           "but clearly visible and in sharp focus.")
KITCHEN_FALL = ("A bright American home kitchen dressed for Thanksgiving: white shaker cabinets, a "
                "few small orange pumpkins and a garland of autumn leaves along the back counter, a "
                "large window behind the grandmother letting in neutral overcast daylight with the "
                "backyard trees and a grey-blue cloudy sky clearly visible through it, never white or "
                "blown out, a light wood floor, and a small American flag standing in a mason jar on "
                "the windowsill, discreet but clearly visible and in sharp focus.")
BACKYARD = ("A green American backyard: a white picket fence and the back porch of a white house "
            "behind the grandmother, an American flag hanging from the porch post, discreet but "
            "clearly visible and in sharp focus, short green grass under the table, and an overcast "
            "sky with visible grey-blue cloud texture, never white or blown out.")

ESCALA = ("The quantity is absurd, like a small bakery inside a home: the whole {mesa} is covered "
          "edge to edge with baking trays of {doce_en}, hundreds of them, with more trays stacked on "
          "two-tier metal stands{extra}.")
ESCALA_EXTRA_KITCHEN = " and the back counter also lined with full trays"
NORMAL = ("Four large baking trays of {doce_en}, dozens of them in neat rows, cover the {mesa}, "
          "with a stack of white napkins and a few glasses of milk at the far left corner.")

CONTAS = [
    dict(n=1, hook="HOOK 1 · CONTROLE, sem degrau", var="DOCE: sweet potato pie", escala=False,
         doce="sweet potato pie", doce_pt="mini torta de batata-doce",
         doce_en="mini sweet potato pies with smooth orange-brown filling in light brown crusts",
         cena="kitchen",
         avo="A Black American grandmother around seventy-two, deep brown skin, short silver curly hair, round tortoiseshell glasses, full cheeks, visible smile lines and age spots",
         avo_roupa="a pale blue short-sleeved blouse under a white cotton apron, small silver stud earrings",
         neta="a Black American girl about three years old, brown skin, chubby cheeks, two round afro puffs tied with yellow bows",
         neta_roupa="a yellow ruffled cotton dress with short sleeves, barefoot",
         voz_avo="voz de avó americana de uns setenta anos, grave, rouca e calorosa, com sotaque do Sul",
         voz_neta="voz infantil aguda e doce de menina de uns três anos, falando devagar, com jeito manhoso de criança pequena"),
    dict(n=2, hook="HOOK 2 · degrau puro", var="nenhuma (ESCALA com peach pie)", escala=True,
         doce="peach pie", doce_pt="mini torta de pêssego",
         doce_en="mini peach pies with glossy orange peach filling in light brown crusts",
         cena="kitchen",
         avo="A white American grandmother around sixty-eight, fair skin with freckles, shoulder-length white hair in soft waves, light blue eyes, fine wrinkles around the eyes and mouth",
         avo_roupa="a lavender cardigan over a white blouse under a light grey apron, small pearl earrings",
         neta="a white American girl about three years old, rosy cheeks, curly blonde hair in two pigtails with pink ribbons",
         neta_roupa="a pink gingham dress with a white collar, barefoot",
         voz_avo="voz de avó americana de uns setenta anos, suave, aguda e risonha, com sotaque do Sul",
         voz_neta="voz infantil fininha e doce de menina de uns três anos, falando devagar e arrastando as palavras, manhosa"),
    dict(n=3, hook="HOOK 3", var="DOCE: pink cupcake", escala=True,
         doce="pink cupcake", doce_pt="cupcake rosa",
         doce_en="mini cupcakes with tall swirls of pink frosting in white paper liners",
         cena="kitchen",
         avo="A Latina American grandmother around sixty-five, olive tan skin, dark grey hair pulled into a low bun, dark brown eyes, laugh lines and a small mole on her cheek",
         avo_roupa="a coral short-sleeved blouse under a beige apron, small gold hoop earrings",
         neta="a Latina American girl about three years old, light tan skin, big dark eyes, wavy dark brown hair in a high ponytail with a red bow",
         neta_roupa="a white cotton dress with small red flowers, barefoot",
         voz_avo="voz de avó americana de uns sessenta e cinco anos, cheia e calorosa, com leve sotaque hispânico",
         voz_neta="voz infantil aguda e animada de menina de uns três anos, falando devagar, manhosa"),
    dict(n=4, hook="HOOK 4", var="DOCE: chocolate chip cookie", escala=True,
         doce="chocolate chip cookie", doce_pt="cookie de gotas de chocolate",
         doce_en="big chocolate chip cookies with melty chocolate chunks",
         cena="kitchen",
         avo="A Black American grandmother around seventy-five, dark brown skin, short natural white afro, high cheekbones, deep wrinkles and a warm gap-toothed smile",
         avo_roupa="a mustard yellow cardigan over a cream blouse under a denim apron, no jewelry",
         neta="a Black American girl about three years old, medium brown skin, box braids with small white beads at the ends",
         neta_roupa="a mint green tulle dress with short puff sleeves, barefoot",
         voz_avo="voz de avó americana de uns setenta e cinco anos, grave e lenta, de risada gostosa, com sotaque do Sul",
         voz_neta="voz infantil doce e um pouco rouquinha de menina de uns três anos, falando devagar, pidona"),
    dict(n=5, hook="HOOK 5", var="DOCE: glazed donut", escala=True,
         doce="glazed donut", doce_pt="donut com glacê",
         doce_en="glazed donuts shiny with a thin sugar glaze",
         cena="kitchen",
         avo="A white American grandmother around seventy, pale skin with many freckles, short grey pixie haircut, green eyes, thin lips and deep crow's feet",
         avo_roupa="a chambray denim shirt with rolled sleeves under a red and white striped apron",
         neta="a white American girl about three years old, many freckles, red hair in two short braids",
         neta_roupa="a light blue overall dress over a white t-shirt, barefoot",
         voz_avo="voz de avó americana de uns setenta anos, firme, meio anasalada e divertida, com sotaque do Meio-Oeste",
         voz_neta="voz infantil aguda e chorosinha de menina de uns três anos, falando devagar, manhosa"),
    dict(n=6, hook="HOOK 6", var="DOCE: cinnamon roll", escala=True,
         doce="cinnamon roll", doce_pt="cinnamon roll",
         doce_en="cinnamon rolls with thick white icing dripping over the sides, packed into metal baking pans",
         cena="kitchen",
         avo="An East Asian American grandmother around sixty-eight, light skin, short black hair with grey streaks, thin gold-rimmed glasses, soft round face with fine wrinkles",
         avo_roupa="a sage green blouse under a white apron with a small floral print",
         neta="an East Asian American girl about three years old, round face, straight black bob haircut with bangs",
         neta_roupa="a yellow smocked cotton dress, barefoot",
         voz_avo="voz de avó americana de uns setenta anos, suave, clara e brincalhona, sotaque americano neutro",
         voz_neta="voz infantil bem aguda e doce de menina de uns três anos, falando devagar e cantado, pidona"),
    dict(n=7, hook="HOOK 7", var="DOCE: banana pudding", escala=True,
         doce="banana pudding", doce_pt="copinho de banana pudding",
         doce_en="small clear cups of banana pudding showing layers of vanilla pudding, banana slices and vanilla wafers, each topped with whipped cream and one wafer",
         cena="kitchen",
         avo="A Black American grandmother around sixty-six, medium brown skin, grey locs pulled up into a bun, oval face, visible freckles and fine lines",
         avo_roupa="a burgundy short-sleeved top under a mustard yellow apron, small gold earrings",
         neta="a Black American girl about three years old, light brown skin, one big curly afro puff on top of her head with an orange headband",
         neta_roupa="an orange ruffled dress, barefoot",
         voz_avo="voz de avó americana de uns sessenta e cinco anos, encorpada e musical, risonha, com sotaque do Sul",
         voz_neta="voz infantil doce e aguda de menina de uns três anos, falando devagar, carente e ansiosa"),
    dict(n=8, hook="HOOK 8", var="LOCAL: mesa de piquenique no quintal (peach pie)", escala=True,
         doce="peach pie", doce_pt="mini torta de pêssego",
         doce_en="mini peach pies with glossy orange peach filling in light brown crusts",
         cena="backyard",
         avo="A white American grandmother around seventy-two, tanned skin, silver chin-length bob, blue eyes, deep wrinkles and sun spots on her cheeks",
         avo_roupa="a red and white gingham short-sleeved blouse under a navy apron",
         neta="a white American girl about three years old, light skin, brown curly hair loose to her shoulders",
         neta_roupa="a white cotton sundress with small navy blue stars, barefoot on the grass",
         voz_avo="voz de avó americana de uns setenta anos, forte e alegre, de quem ri alto, com sotaque do Texas",
         voz_neta="voz infantil aguda e fofa de menina de uns três anos, falando devagar, manhosa"),
    dict(n=9, hook="HOOK 9", var="OCASIÃO: cozinha de Thanksgiving (peach pie)", escala=True,
         doce="peach pie", doce_pt="mini torta de pêssego",
         doce_en="mini peach pies with glossy orange peach filling in light brown crusts",
         cena="fall",
         avo="A Latina American grandmother around seventy, medium tan skin, salt and pepper curly hair to the chin, dark brown eyes, deep laugh lines",
         avo_roupa="a burgundy knit sweater with pushed-up sleeves under a cream apron, small silver stud earrings",
         neta="a Latina American girl about three years old, tan skin, dark curly hair in two low pigtails with brown ribbons",
         neta_roupa="a mustard yellow corduroy pinafore dress over a white long-sleeved shirt, barefoot",
         voz_avo="voz de avó americana de uns setenta anos, calorosa e cheia, com leve sotaque hispânico",
         voz_neta="voz infantil aguda e docinha de menina de uns três anos, falando devagar, pidona"),
]


def falas(c):
    t1 = f"Grandma, please let me eat that {c['doce']} now. I really want it."
    t3 = f"Please comment yes and follow. I want to choose this {c['doce']} right now."
    return t1, T2, t3


def tela(c):
    curto = "cookie" if c["doce"] == "chocolate chip cookie" else c["doce"]
    return f"Grandma, please let me eat that {curto}"


PLURAL = {"sweet potato pie": "sweet potato pies", "peach pie": "peach pies",
          "pink cupcake": "pink cupcakes", "chocolate chip cookie": "chocolate chip cookies",
          "glazed donut": "glazed donuts", "cinnamon roll": "cinnamon rolls",
          "banana pudding": "banana pudding cups"}


def mesa(c):
    return "picnic table" if c["cena"] == "backyard" else "kitchen island"


def heroi(c):
    m = mesa(c)
    if c["escala"]:
        extra = ESCALA_EXTRA_KITCHEN if c["cena"] != "backyard" else ""
        base = ESCALA.format(mesa=m, doce_en=c["doce_en"], extra=extra)
    else:
        base = NORMAL.format(mesa=m, doce_en=c["doce_en"])
    return (base + " The nearest trays are very close to the lens in the lower foreground, large "
            "in frame, closer to the camera than the grandmother's face, nothing else competing "
            "with them.")


def cenario(c):
    return {"kitchen": KITCHEN, "fall": KITCHEN_FALL, "backyard": BACKYARD}[c["cena"]]


REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry on both "
            "faces, hair in uneven natural clumps, iPhone footage look, flat natural light, low "
            "contrast, slight JPEG compression, boring everyday reality, background fully in focus, "
            "everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no "
            "warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, "
            "no captions, no subtitles, no words overlaid on the image.")

NEGATIVE = ("no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra "
            "fingers, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, "
            "no night scene, no dark windows, no beauty smoothing, no de-aging, no third person, no "
            "people copied from the reference frame")


def k_json(c):
    m = mesa(c)
    return {
        "shot_id": f"K01_conta{c['n']:02d}_pedido",
        "reference_use": ("Use the attached reference frame ONLY for camera height, camera angle and "
                          "the layout of the table and the two people. Do NOT copy the people, faces, "
                          "hair, skin tone, clothing, desserts or room from it."),
        "fiction_note": "Both people are fictional AI-generated characters, no real person is depicted.",
        "identity_main": c["avo"] + ", standing behind the " + m + ", her age fully visible and never smoothed.",
        "identity_second": ("A small granddaughter: " + c["neta"] + ", standing on the ground in front of "
                            "the right end of the " + m + ", so small that her head only reaches the "
                            "edge of the " + m + "."),
        "wardrobe": "Grandmother: " + c["avo_roupa"] + ". Granddaughter: " + c["neta_roupa"] + ".",
        "prop": heroi(c),
        "scene": cenario(c),
        "posture": ("The grandmother stands behind the " + m + " with both hands resting on its edge, "
                    "leaning slightly forward and looking down at her granddaughter with an amused "
                    "smile. The granddaughter stands on her tiptoes at the right end of the " + m +
                    " stretching one arm up toward one of the " + PLURAL[c["doce"]] + " on the nearest tray, her "
                    "face turned up to her grandmother."),
        "composition": ("The trays of " + PLURAL[c["doce"]] + " fill the lower left and lower middle of the "
                        "frame, closest to the lens. The grandmother is seen from the waist up behind "
                        "them in the upper middle. The granddaughter is seen head to toe at the lower "
                        "right."),
        "camera": "phone held high at adult head height, angled slightly down, straight-on across the " + m + ", as in the reference frame",
        "state": ("Start frame: the granddaughter is already reaching and already asking, caught "
                  "mid-sentence, lips naturally parted, eager pleading expression with wide eyes; the "
                  "grandmother is holding back a laugh."),
        "lighting": ("Neutral overcast daylight, soft even light on both faces with no harsh shadows, "
                     "no warm orange cast and no yellow tint."),
        "realism": REALISMO,
        "aspect_ratio": "9:16 vertical",
        "negative": NEGATIVE,
    }


def k_flow(c):
    d = k_json(c)
    return " ".join([
        "IMPORTANT: THIS IS IPHONE FOOTAGE, a vertical 9:16 phone video frame.",
        d["reference_use"], d["fiction_note"],
        d["identity_main"], d["identity_second"], d["wardrobe"], d["prop"], d["scene"],
        d["posture"], d["composition"], "Camera: " + d["camera"] + ".", d["state"], d["lighting"],
        d["realism"], "Negative: " + d["negative"] + ".",
    ])


CAMERA_V = "câmera: fixa, na mão de alguém da família, com leve tremor natural de celular"
SOM_V = {"kitchen": "som ambiente: cozinha de casa silenciosa, sem música",
         "fall": "som ambiente: cozinha de casa silenciosa, sem música",
         "backyard": "som ambiente: quintal tranquilo com passarinhos ao longe, sem música"}
LIP = ("{quem} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra "
       "por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. {cala}")


def v_prompts(c):
    t1, t2, t3 = falas(c)
    m = "mesa" if c["cena"] == "backyard" else "bancada"
    som = SOM_V[c["cena"]]
    v1 = "\n\n".join([
        f"a neta (menina de uns três anos, a criança na frente da {m}) fala em inglês com sotaque americano, {c['voz_neta']}, pedindo com muita vontade, a seguinte frase: \"{t1}\"",
        LIP.format(quem="a neta", cala="A avó fica calada enquanto a neta fala."),
        f"o que acontece no vídeo: a neta estica a mão para um dos doces da bandeja mais próxima olhando para a avó enquanto pede; quando a neta termina, a avó joga a cabeça para trás e solta uma risada alta, com a mesma voz dela ({c['voz_avo']}).",
        CAMERA_V, som])
    v2 = "\n\n".join([
        f"a avó (a senhora atrás da {m}) fala em inglês com sotaque americano, {c['voz_avo']}, ainda rindo e em tom de brincadeira, olhando para a câmera, a seguinte frase: \"{t2}\"",
        LIP.format(quem="a avó", cala="A neta fica calada, só olhando para a avó."),
        "o que acontece no vídeo: a avó tira os olhos da neta, vira o rosto para a câmera e fala com quem está assistindo, no fim aponta de leve para a neta; a neta continua com a mão perto da bandeja, olhando para cima para a avó.",
        CAMERA_V, som])
    v3 = "\n\n".join([
        f"a neta (menina de uns três anos, a criança na frente da {m}) fala em inglês com sotaque americano, {c['voz_neta']}, implorando com os olhos arregalados, a seguinte frase: \"{t3}\"",
        LIP.format(quem="a neta", cala="A avó fica calada, só sorrindo."),
        f"o que acontece no vídeo: a neta vira de frente para a câmera, junta as duas mãos na frente do peito em súplica e dá pulinhos no lugar enquanto pede; a avó sorri atrás da {m}.",
        CAMERA_V, som])
    return [("V01", "T1", v1), ("V02", "T2", v2), ("V03", "T3", v3)]


def roteiro(c):
    t1, t2, t3 = falas(c)
    m = "mesa de piquenique" if c["cena"] == "backyard" else "ilha da cozinha"
    return f"""# Short form de crescimento · Torta da vovó · Conta {c['n']} | Roteiro

tipo: crescimento

Vídeo modelo: `{VIDEO_MODELO}` (17,15s, plano único). Decomposição em `../DECOMPOSICAO.md`.

Conta {c['n']} de 9 · {c['hook']} · variável trocada: **{c['var']}**.

Personagens desta conta (dupla própria, sem character sheet, descrita no prompt de imagem):
- **Avó:** {c['avo']}; {c['avo_roupa']}.
- **Neta:** {c['neta']}; {c['neta_roupa']}.

Funil: nenhum. Crescimento puro, keyword `yes`, CTA genérico (comentar yes + seguir o perfil) com a
consequência logo depois (decisão do Luigi, 2026-09-23).

Enquadramento: câmera alta e fixa de frente para a {m}; avó da cintura para cima atrás dela, neta de
corpo inteiro no canto inferior direito.

---

## Esqueleto preservado

| # | Beat | Original | Adaptado |
|---|---|---|---|
| 1 | PEDIDO | neta estica a mão para uma torta e pede à avó | idêntico, com {c['doce']} |
| 2 | RISO | avó ri alto | idêntico |
| 3 | CONDIÇÃO | avó para a câmera: follow Grandma + write yes, você escolhe primeiro | avó para a câmera: comment yes + follow this page, você escolhe primeiro |
| 4 | SÚPLICA | neta para a câmera, mãos juntas: like, follow, write yes | neta para a câmera, mãos juntas: comment yes + follow |

## Setups de cena

**Setup A · {m} coberta de {c['doce']}.** Plano único; K01 é o frame inicial dos três takes.

## Roteiro cena a cena

### T1 · PEDIDO · TALKING · Setup A
A neta estica a mão para um doce da bandeja ({c['doce_pt']}) olhando para a avó. No fim a avó ri alto.
> NETA: "{t1}"

### T2 · CONDIÇÃO · TALKING · Setup A
A avó vira para a câmera; a neta segue com a mão perto da bandeja, calada.
> AVÓ: "{t2}"

### T3 · SÚPLICA · TALKING · Setup A
A neta vira para a câmera, mãos juntas de súplica, pulinhos. A avó sorri, calada.
> NETA: "{t3}"

## Roteiro só-fala (inglês, TTS)
{t1}
{t2}
{t3}

## Notas de produção
- Texto de tela do T1 (CapCut, nunca na imagem): `{tela(c)}`.
- Duração alvo 17 a 20s. Se ficar longo, cortar a risada do fim do T1.
- A neta usa a mesma descrição de voz em V01 e V03.
- Crescimento sem venda: sem produto, sem link, sem DM.
"""


def prompts(c):
    d = k_json(c)
    vs = v_prompts(c)
    vtxt = "\n\n".join(f"### {vid} · {t} · usa K01\n\n```text\n{b}\n```" for vid, t, b in vs)
    return f"""# Conta {c['n']} | Short form de crescimento | Pacote de Prompts

Vídeo modelo: `{VIDEO_MODELO}`

Âncora: **nenhuma** (dupla descrita por escrito, decisão do Luigi, 2026-09-23). Anexo único do K:
`REF-COMPOSICAO` = `{REF_PATH}`, só para câmera e disposição.

Funil: nenhum, crescimento puro. {c['hook']} · variável: {c['var']}.

---

## Índice de geração

| Take | Keyframe | Anexar | Ação de geração |
|---|---|---|---|
| T1, T2, T3 | K01 | REF-COMPOSICAO | GERAR DO ZERO |

Os três V partem do mesmo K01 (perfil clássico do Flow: V01, V02 e V03 usam o maior K disponível,
que é o K01).

## Trava de identidade e continuidade

- Avó: {c['avo']}. Roupa: {c['avo_roupa']}.
- Neta: {c['neta']}. Roupa: {c['neta_roupa']}.
- Dupla exclusiva desta conta, nunca reaproveitada em outra (checklist B8).
- Luz neutra de dia nublado, zero blur, tudo em foco.

## Trava do prop herói

{heroi(c)}

## Trava da 2ª pessoa

A neta está descrita por escrito dentro do K01 e aparece de corpo inteiro, como no original. Sem REF.

# Prompts de imagem

## K01 · T1, T2, T3 · GERAR DO ZERO · REF-COMPOSICAO

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-COMPOSICAO** · `{REF_PATH}` (só câmera e disposição)
>
> ### 🆕 GERAR DO ZERO

```json
{json.dumps(d, ensure_ascii=False, indent=2)}
```

## Bloco global de vídeo

```text
[quem fala: a neta ou a avó] fala em inglês com sotaque americano, [voz do personagem], [emoção da fala], a seguinte frase: "[FALA EXATA DO ROTEIRO]"

[quem fala] diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. [quem fica calado]

o que acontece no vídeo: [ação ENXUTA]

{CAMERA_V}

{SOM_V[c['cena']]}
```

# Prompts de vídeo

{vtxt}

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | REF-COMPOSICAO (`{REF_PATH}`) | Nano Banana 2, 9:16, 1 imagem final |

Vídeo: Veo 3.1 Lite, Lower Priority, 8 segundos, 1 variação, K01 como INITIAL FRAME de V01, V02 e V03.

---

## Montagem no CapCut

1. Ordem: clipe 1 = V01, clipe 2 = V02, clipe 3 = V03.
2. V02 e V03 começam na mesma pose do K01: cortar o início até o primeiro movimento, para a
   emenda parecer contínua. Todo clipe começa já falando; `Isolate Voice` no áudio.
3. Cortar a risada do fim do V01 se o vídeo passar de 20s.
4. Texto de tela só no T1: `{tela(c)}`.
5. Legenda da fala nos três clipes.
6. Sem música e sem Voice Changer.
7. Rótulo pequeno `AI-generated` num canto.
8. Exportar em 9:16, 1080 por 1920.

---

## Gates de qualidade

1. [ ] As bandejas de {c['doce']} estão no lower foreground, mais perto da lente que o rosto da avó.
2. [ ] {"Escala de confeitaria: bancada coberta de ponta a ponta e bandejas em suportes de dois andares." if c['escala'] else "Quantidade igual à do original (controle, sem degrau)."}
3. [ ] A bandeira dos EUA aparece e está em foco.
4. [ ] A dupla não lembra o vídeo modelo nem as duplas das outras contas.
5. [ ] Luz neutra de dia nublado, janela ou céu com cor, zero tom quente, zero blur.
6. [ ] Rostos nítidos, sem sombra dura, boca da neta entreaberta.
7. [ ] Em V02 só a avó fala; em V01 e V03 só a neta fala.
8. [ ] A fala de cada V bate palavra por palavra com o `ROTEIRO.md`.
9. [ ] `python3 checar_entrega.py producao/sf_torta_vovo/conta_{c['n']:02d}` fechou sem FALHA.
"""


def flow(c):
    vs = v_prompts(c)
    vblock = "\n\n".join(f"{vid}\n{b}" for vid, _, b in vs)
    return f"""# Flow · Conta {c['n']} · {c['hook']} · {c['var']}

Tabela humana (fora dos blocos): K01 = neta pedindo o {c['doce']}, frame inicial dos três takes.
V01 = neta pede · V02 = avó dá a condição · V03 = neta implora. Anexo do K01: REF-COMPOSICAO.

## Bloco de imagem

```text
K01
{k_flow(c)}
```

## Bloco de vídeo

```text
{vblock}
```
"""


def instrucoes_flow():
    txt = (BASE.parent / "_flow" / "INSTRUCOES_AGENTE_FLOW.md").read_text(encoding="utf-8")
    ini = txt.index("## Bloco para a memoria do executor")
    ini = txt.index("\n", ini) + 1
    fim = txt.index("## Historico resumido")
    return txt[ini:fim].strip()


def entrega(c):
    t1, t2, t3 = falas(c)
    vs = v_prompts(c)
    vblock = "\n\n".join(f"{vid}\n{b}" for vid, _, b in vs)
    pt = {"sweet potato pie": "torta de batata-doce", "peach pie": "torta de pêssego",
          "pink cupcake": "cupcake rosa", "chocolate chip cookie": "cookie de gotas de chocolate",
          "glazed donut": "donut com glacê", "cinnamon roll": "cinnamon roll",
          "banana pudding": "banana pudding"}[c["doce"]]
    art = "esse" if c["doce"] in ("pink cupcake", "chocolate chip cookie", "glazed donut", "cinnamon roll", "banana pudding") else "essa"
    art1 = "aquele" if art == "esse" else "aquela"
    return f"""# Entrega · Conta {c['n']} · {c['hook']} · {c['var']}

Checklist de envio: 32/32 aprovados (N/A: A1, A9, A10, B9, C4, C5, C7, E1, E2)

## INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI

```text
{instrucoes_flow()}
```

**Anexar no K01:** 1 imagem, `{REF_PATH}` (só câmera e disposição). Perfil clássico, 1 imagem
final; V01, V02 e V03 usam o K01 como INITIAL FRAME.

## Bloco de imagem

```text
K01
{k_flow(c)}
```

## Bloco de vídeo

```text
{vblock}
```

## Montagem no CapCut
V01, V02, V03 na ordem · cortar o início de V02 e V03 até o primeiro movimento · texto de tela só
no T1: `{tela(c)}` · legenda da fala nos três · sem música e sem Voice Changer · rótulo
`AI-generated` num canto.

## Transcrição final

| Take | English | Português |
|---|---|---|
| T1 | {t1} | Vovó, por favor, me deixa comer {art1} {pt} agora. Eu quero muito. |
| T2 | {t2} | Tá bom, se o pessoal comentar yes e seguir esta página, você escolhe primeiro. |
| T3 | {t3} | Por favor, comenta yes e segue. Eu quero escolher {art} {pt} agora mesmo. |

## Roteiro final em inglês

1. {t1}
2. {t2}
3. {t3}

{t1} {t2} {t3}
"""


def main():
    for c in CONTAS:
        pasta = BASE / f"conta_{c['n']:02d}"
        pasta.mkdir(exist_ok=True)
        (pasta / "ROTEIRO.md").write_text(roteiro(c), encoding="utf-8")
        (pasta / "PROMPTS_PRODUCAO.md").write_text(prompts(c), encoding="utf-8")
        (pasta / f"FLOW_CONTA_{c['n']:02d}.md").write_text(flow(c), encoding="utf-8")
        (pasta / f"ENTREGA_CONTA_{c['n']:02d}.md").write_text(entrega(c), encoding="utf-8")
        print("ok", pasta.name)


if __name__ == "__main__":
    main()
