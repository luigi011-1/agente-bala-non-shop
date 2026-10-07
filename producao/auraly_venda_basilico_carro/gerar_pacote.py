"""Gera os pacotes por avatar da producao auraly_venda_basilico_carro (Auraly, venda, dinheiro/fortuna, validacao, origem ORGANICA).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco). Regra do Luigi de 2026-10-06: K so com o character sheet
do avatar; V so com a imagem escolhida do K. Cenario e camera do modelo vao por escrito. Regra de 2026-10-07: o cenario
do Gordon e sempre de luxo maximo (carro vira carro de luxo). Mapa: K01 -> V01 (T1 mudo), K02 -> V02 a V10.
Saidas por avatar: PROMPTS_<AVATAR>.md, FLOW_<AVATAR>.md e ENTREGA_<AVATAR>.md.  Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")
HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 11)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    t = re.match(r"### (T\d+)", bloco).group(1)
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[t] = m.group(1)
assert set(FALAS) == set(TAKES) - {"T1"}
tab = ROTEIRO.split("## Tradução completa")[1].split("\n## ")[0]
PT = {t: p for t, e, p in re.findall(r"^\| (T\d+) \| (.+?) \| (.+?) \|$", tab, re.M)}
assert set(PT) == set(TAKES), PT

MAPA = {"V01": "K01", **{"V%02d" % i: "K02" for i in range(2, 11)}}
FICCAO = "This is a fictional AI-generated character, no real person is depicted."
LUZ = ("Bright neutral daylight under a blue sky with soft white clouds, the person in the open shade of the car door, soft even "
       "light on the face and hands with no harsh shadows, the sky clearly visible and never white or blown out, true neutral "
       "colors with no golden light.")
LUZ1 = ("Soft neutral daylight falling from above and behind into the open car door, even and shaded, no harsh shadows, true "
        "neutral colors with no golden light.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural strands, "
            "iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, "
            "background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no floating numbers, no glowing numbers, no brand names, no "
       "logos and no printed text on the jar, no studio, no grey studio background, no plastic-looking human skin, no extra "
       "fingers, no third hand, no supernatural lighting, no glowing objects, no sparkles, no steam, no smoke, no blur, no "
       "bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour "
       "light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person "
       "in frame, no tarot cards, no candles")
JAR = ("a clear glass jar with a wide screw mouth, lid off and out of frame, no label and no printed text")

AVATARES = [
    dict(nome="Gordon Ashby", arquivo="GORDON_ASHBY", genero="homem", pos="his", sheet="producao/_ancoras/character_sheets/gordon_ashby_character_sheet.jpg",
         identidade=("The exact fictional AI character Gordon Ashby, explicitly male: American man aged about 68, slim and upright, full "
                     "head of thick silver-white hair combed back, thin gold-rimmed round glasses, narrow elegant face, light "
                     "blue-grey eyes with heavy lids, real aged skin with deep forehead lines, crow's feet, sun spots and soft "
                     "jowls, clean-shaven, a calm closed-mouth half smile."),
         roupa=("Cream off-white tailored dinner jacket with a white dress shirt and a black silk bow tie, black dress trousers, black "
                "polished leather oxford shoes, a slim gold wristwatch on the left wrist and a plain gold ring on the left ring finger."),
         mao_quem="his aged pale hand with a gold ring and a gold wristwatch", manga="a cream dinner-jacket cuff over a white shirt cuff",
         carro="a black Bentley Bentayga", pisoDesc="a thick black carpet floor mat with cream leather trim",
         assento="cream quilted leather", chao="pale limestone paving",
         fundo=("behind it a limestone mansion facade with tall windows and clipped boxwood hedges"),
         agach=("squats low on his heels beside the open rear door in his cream dinner jacket, knees bent, forearms resting on his thighs"),
         sotaque="de Nova York, de classe alta", voz="voz masculina grave, baixa e lenta de um homem de sessenta e oito anos de dinheiro antigo, autoridade tranquila",
         tom="de voz baixa e calma, quase confidencial", lux=True),
    dict(nome="Avery Knox", arquivo="AVERY_KNOX", genero="mulher", pos="her", sheet="producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg",
         identidade=("The exact fictional AI character Avery Knox: white American woman around fifty-six, voluminous shaggy "
                     "layered platinum-blonde hair with visible darker roots, brown eyes, fair skin with crow's feet and fine "
                     "lines, everyday makeup with defined brows, mascara and pink lipstick."),
         roupa=("White long-sleeve button-up shirt with a chest pocket and the cuffs rolled, medium-blue bootcut jeans, a "
                "large turquoise and silver squash-blossom necklace, several big turquoise rings and silver cuff bracelets "
                "set with turquoise on both wrists."),
         mao_quem="her fair hand with big turquoise rings and a silver turquoise cuff bracelet", manga="a rolled white shirt cuff",
         carro="a grey full-size SUV", pisoDesc="a black ribbed rubber floor mat",
         assento="black fabric", chao="pale concrete",
         fundo=("behind it a beige two-storey house with a white garage door and a leafy green tree"),
         agach=("squats low on her heels beside the open rear door in jeans and the white shirt, knees bent, forearms resting on her thighs"),
         sotaque="texano carregado", voz="voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos",
         tom="de voz firme e calorosa", lux=False),
]

EMOCAO = {
    "T2": "em voz baixa e confidencial, como quem dá uma ordem em segredo",
    "T3": "em tom sério e convicto",
    "T4": "em tom calmo, certo e firme",
    "T5": "em tom firme e direto, sem sorrir",
    "T6": "em tom duro e urgente, sem levantar a voz",
    "T7": "em tom firme, marcando \"222\" e \"your name\"",
    "T8": "em tom próximo e urgente, olhando direto na lente",
    "T9": "em tom solene e respeitoso",
    "T10": "em tom intenso e convicto, fechando com firmeza",
}
ACAO_PADRAO = "{n} fala olhando fixo para a lente, com um pequeno aceno de cabeça, o pote de vidro vazio parado nas duas mãos diante do peito. Nada mais muda."
ACAO = {
    "T2": "{n} ergue o pote vazio um pouco em direção à lente na palavra \"mouth\" e leva o dedo indicador aos lábios por um instante em \"shut\", sem cobrir a boca.",
    "T3": "{n} inclina a cabeça de leve para a frente, olhando fixo para a lente, o pote vazio nas duas mãos.",
    "T4": "{n} balança a cabeça devagar em \"Do not scroll away\" e olha fixo para a lente, o pote nas duas mãos.",
    "T5": "{n} ergue uma das mãos, palma para cima, na frase \"a refund, a bonus, a payout\", segurando o pote com a outra.",
    "T6": "{n} aponta o indicador da mão livre para o tapete do carro em \"the mat stays down\" e depois de volta para a lente em \"Tell one person\".",
    "T7": "{n} aponta o indicador para a lente na palavra \"comment\" e toca o peito com a mão livre em \"your name\".",
    "T8": "{n} aponta o indicador para a lente e depois para baixo na palavra \"stories\", olhando direto para a lente.",
    "T9": "{n} ergue o olhar por um instante e volta para a lente, uma mão aberta no peito, o pote na outra.",
    "T10": "{n} abre uma das mãos devagar em direção à lente em \"prophecy\" e aponta para baixo em \"stories\", olhando para a lente.",
}


def cena_carro(a):
    if a["lux"]:
        return (f"A private estate courtyard on a bright day: {a['chao']}, {a['carro']} with its rear door wide open showing "
                f"{a['assento']} seats and {a['pisoDesc']}, and {a['fundo']}, all under a blue sky with soft white clouds.")
    return (f"A quiet American suburban driveway on a bright day: {a['chao']} driveway, {a['carro']} with its rear door wide open "
            f"showing {a['assento']} seats and {a['pisoDesc']}, and {a['fundo']}, all under a blue sky with soft white clouds.")


def keyframes(a):
    n, pos = a["nome"], a["pos"]
    base = {"fiction_note": FICCAO,
            "reference_use": (f"Use the attached image (character sheet) only for {n}'s exact identity (face, skin, hair, body) "
                              "and wardrobe; ignore its grey studio background. The setting, camera angle and framing are "
                              "described in full in the scene, camera and composition fields; no other image is attached."),
            "identity_main": a["identidade"], "wardrobe": a["roupa"]}
    k1 = dict(base)
    k1.update({
        "scene": (f"Looking down into the rear footwell of {a['carro']} through its open rear door: the lower part of the "
                  f"{a['assento']} rear seat at the top of the frame, and the dark carpeted floor of the footwell filling the "
                  f"lower two thirds of the frame, with {a['pisoDesc']} half flipped back from the floor."),
        "prop": (f"The hero objects are {JAR}, tipped on its side in {pos} right hand so that dry basil leaves, olive-green and "
                 f"brown crumbled leaves and flakes, slide out of the mouth and start to fall, and {a['pisoDesc']}, lifted at "
                 f"its edge by {pos} other hand. A few dry leaf fragments already lie on the bare dark carpet."),
        "posture": (f"Only {n}'s two hands and forearms are in the frame, no face: the right hand tips the jar from the upper left, "
                    f"the other hand ({a['mao_quem']}) holds up the edge of the mat from the right, {a['manga']} showing at each wrist."),
        "composition": (f"The tipped glass jar and the hand holding it are very close to the lens, about 14 inches from the lens, "
                        f"large in frame, about 35 percent of the frame together, with the lifted mat edge crossing the middle of the "
                        f"frame. The bare carpet and the first leaves fill the lower foreground. Nothing else is in the foreground. "
                        f"The background is reduced by framing, never by blur."),
        "camera": "handheld phone held about 20 inches above the floor of the car, looking steeply down into the footwell, 1x lens, steady",
        "lighting": LUZ1,
        "state": f"Start frame: the jar is already tipped and the first dry basil leaves are just sliding out of its mouth, the mat edge held up, no face in the frame.",
        "realism": REALISMO, "aspect_ratio": "9:16 vertical",
        "negative": NEG + ", no face in frame, no leaves already piled up, no bay leaves, no jar lid in frame",
    })
    k2 = dict(base)
    k2.update({
        "scene": cena_carro(a),
        "prop": (f"The hero object is {JAR}, empty except for a few dry green-brown basil crumbs stuck to the glass, held in both of "
                 f"{pos} hands at chest height just in front of {pos} body, tilted slightly toward the lens."),
        "posture": (f"{n} {a['agach']}, holding the empty glass jar in both hands, looking straight into the lens, caught "
                    f"mid-sentence, lips naturally parted, animated and serious expression."),
        "composition": (f"The glass jar is very close to the lens in the lower foreground, about 25 percent of the frame, about 30 inches "
                        f"from the lens, closer to the camera than {pos} face, nothing else competing with it. {n} is framed fully "
                        f"squatting, from the top of the head to the shoes, the open car door and {a['assento']} seats at the left "
                        f"and behind, the rest of the setting behind. Nothing else is in the foreground. The background is reduced "
                        f"by framing, never by blur."),
        "camera": "phone propped about three feet above the ground, about four and a half feet from the person, 1x lens, pointing level, fixed",
        "lighting": LUZ,
        "state": f"Start frame: {n} squats beside the open door holding the empty jar, mid-sentence, the floor mat lying flat and back in place.",
        "realism": REALISMO, "aspect_ratio": "9:16 vertical",
        "negative": NEG + ", no leaves on the ground, no second jar, no jar lid, no hands in the car",
    })
    return [dict(codigo="K01", take="T1", titulo="gancho, mãos despejam o manjericão seco sob o tapete do carro", j=k1),
            dict(codigo="K02", take="T2 a T10", titulo=f"corpo, {n} agachado ao lado da porta aberta do carro, pote de vidro vazio nas mãos", j=k2)]


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art = "o avatar" if h else "a avatar"
    lux = a["lux"]
    local = "a entrada de uma mansão" if lux else "uma entrada de garagem de bairro"
    abre = (f"{art} {n}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, em tom de conversa de quem "
            "grava um vídeo no celular para os seguidores, natural, próximo e confiante, no mesmo ritmo de um vídeo orgânico, "
            "{emo}, a seguinte frase: \"{fala}\"")
    diz = (f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar "
           "no final. Lip sync perfeito durante todo o vídeo.")
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        if t == "T1":
            txt = ("(sem fala no take: gancho mudo, " + ("o avatar não aparece falando" if False else "ninguém fala") + ", boca fechada o clipe inteiro)\n\n"
                   f"o que acontece no vídeo: as mãos de {n} inclinam o pote de vidro e as folhas secas de manjericão escorrem e caem sobre o piso escuro do carro, enquanto a outra mão mantém o tapete levantado; corte para MACRO das folhas caindo e se espalhando no piso, que dura um instante; corte para o plano aberto de {n} agachado ao lado da porta aberta, que baixa o tapete sobre as folhas, alisa a borda com a mão e olha para a lente, o pote vazio na outra mão.\n\n"
                   "câmera: celular fixo e firme, com cortes internos ao clipe: plano das mãos de cima, macro das folhas, plano aberto do avatar agachado\n\n"
                   f"som ambiente: {local} tranquila, folhas secas caindo e o estalo leve da borracha do tapete, sem música")
        else:
            acao = ACAO.get(t, ACAO_PADRAO).format(n=n)
            txt = (abre.format(emo=EMOCAO[t], fala=FALAS[t]) + "\n\n" + diz + "\n\n"
                   f"o que acontece no vídeo: {acao}\n\ncâmera: celular apoiado, fixo, sem movimento\n\n"
                   f"som ambiente: {local} tranquila, leve vento e passarinhos ao longe, sem música")
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
        "1. Clipes numerados na ordem: V01 a V10.",
        "2. V01: usar uns 6 s (mãos, macro, plano aberto) e cortar seco para o V02, como no modelo. Texto de tela do gancho no CapCut: `Keep your mouth shut` / `Tell nobody`.",
        "3. V02 a V10: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Todos saem do mesmo frame (jump cut).",
        "4. Legenda karaokê palavra a palavra no centro do quadro, branca, destaque verde-limão na palavra falada, do V02 ao V10.",
        "5. Sem Voice Changer: a voz vem do prompt de cada V. Isolate Voice / Keep Vocal no áudio.",
        "6. Música só depois do V01, baixa, fora da biblioteca do TikTok. Sem números brilhantes (222, 333) na imagem.",
        "7. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|", "| T1 | (sem fala, inserto mudo) | (sem fala, inserto mudo) |"]
    for t in TAKES[1:]:
        L.append(f"| {t} | {FALAS[t]} | {PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# {a['nome']} | Auraly Venda Manjericão no Carro | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `input/modelo.mp4` (86,6 s, pessoa real, orgânico)", "",
         f"Character sheet: `{a['sheet']}`", "",
         "Funil: venda, ramificação de dinheiro e fortuna. Comentar `222` com o nome, depois Stories. Rodada de validação.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|",
         f"| T1 | K01 | só o CHARACTER SHEET de {a['nome']} | GERAR DO ZERO |",
         f"| T2 a T10 | K02 | só o CHARACTER SHEET de {a['nome']} | GERAR DO ZERO |", "",
         "## Trava de identidade e continuidade", "",
         f"- Identidade: {a['identidade']}", f"- Roupa (do character sheet): {a['roupa']}",
         f"- Cenário: {cena_carro(a)}", f"- Luz: {LUZ}",
         f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.", "- Sem 2ª pessoa.", "",
         "## Trava do prop herói", "", f"- Pote: {JAR}.", f"- Tapete: {a['pisoDesc']}.", "",
         "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "", "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · CHARACTER SHEET {a['nome'].upper()}", "",
              f"> ### 📎 ANEXAR: **1 IMAGEM**", f"> **1️⃣ CHARACTER SHEET {a['nome'].upper()}** `{a['sheet']}`", ">", "> ### 🆕 GERAR DO ZERO", "",
              f"Cena: {k['titulo']}.", "", "```json", json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
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


def entrega(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Venda Manjericão no Carro", "",
         "Produção `auraly_venda_basilico_carro` · Ângulo 3 · SALE (dinheiro e fortuna) · vídeo modelo de pessoa real (orgânico) · rodada de VALIDAÇÃO · perfil AURALY", "",
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
    L += ["## 4. Montagem no CapCut", ""] + capcut()
    L += ["", "## 5. Transcrição final por take", ""] + transcricao()
    L += ["", "## 6. Roteiro final em inglês", ""]
    for t in TAKES[1:]:
        L.append(f"{t[1:]}. {FALAS[t]}")
    L += ["", " ".join(FALAS[t] for t in TAKES[1:]), ""]
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
