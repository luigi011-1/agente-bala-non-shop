"""Gera os pacotes por avatar da producao auraly_venda_prosperidade_v3 (Auraly, venda, dinheiro/prosperidade, validacao, origem ORGANICA).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco). Regra do Luigi de 2026-10-06: K so com o character sheet do avatar;
V so com a imagem escolhida do K. Cenario e camera do modelo vao por escrito. Regra de 2026-10-07: cenario do Jordan e sempre
de luxo maximo (sala = mansao). Mapa: K01 -> V01 (T1), K02 -> V02 a V15.
Saidas por avatar: PROMPTS_<AVATAR>.md, FLOW_<AVATAR>.md e ENTREGA_<AVATAR>.md.  Uso: python3 gerar_pacote.py
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
    t = re.match(r"### (T\d+)", bloco).group(1)
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    FALAS[t] = m.group(1)
assert set(FALAS) == set(TAKES)
tab = ROTEIRO.split("## Tabela bilíngue completa")[1].split("\n## ")[0]
PT = {t: p for t, e, p in re.findall(r"^\| (T\d+) \| (.+?) \| (.+?) \|$", tab, re.M)}
assert set(PT) == set(TAKES), PT

MAPA = {"V01": "K01", **{"V%02d" % i: "K02" for i in range(2, 16)}}
FICCAO = "This is a fictional AI-generated character, no real person is depicted."
LUZ = ("Neutral overcast daylight coming from the large glass door and window on the right, the grey-white sky and green garden "
       "clearly visible through it and never white or blown out, soft even light on the face and hands with no harsh shadows, true "
       "neutral colors, the under-cabinet lights in the kitchen behind are cool white and dim, no warm lamp light.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural strands, "
            "iPhone selfie footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, "
            "background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no brand names, no logos, no studio, no grey studio background, "
       "no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no glowing objects, no sparkles, "
       "no steam, no smoke, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no "
       "golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic "
       "lighting, no second person in frame, no candles, no floating text, no numbers in the air")
CARTA_COSTAS = ("an ornate black and gold tarot card back, a rectangular black card with a thin gold border and a gold wheel-like "
                "circular pattern with small stars, held at the card's edge")

AVATARES = [
    dict(nome="Jordan Vale", arquivo="JORDAN_VALE", genero="homem", pos="his", sheet="producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg",
         identidade=("The exact fictional AI character Jordan Vale, explicitly male: American man aged about 68, slim and upright, full "
                     "head of thick silver-white hair combed back, thin gold-rimmed round glasses, narrow elegant face, light "
                     "blue-grey eyes with heavy lids, real aged skin with deep forehead lines, crow's feet, sun spots and soft "
                     "jowls, clean-shaven, a calm closed-mouth half smile."),
         roupa=("Cream off-white tailored dinner jacket with a white dress shirt and a black silk bow tie, a slim gold wristwatch on the "
                "left wrist and a plain gold ring on the left ring finger."),
         mao="his aged pale hand with a gold ring and a gold wristwatch", manga="a cream dinner-jacket cuff over a white shirt cuff",
         sofa="a deep ivory silk sofa", fundo=("an open luxury kitchen of white marble and pale lacquered cabinets with brass handles, a marble island "
                                              "and a crystal pendant light, a tall pale-wood door frame at the right"),
         casa="a grand mansion salon", janela="a tall arched glass door and window with a manicured garden, clipped hedges and a stone terrace",
         sotaque="de Nova York, de classe alta", voz="voz masculina grave, baixa e lenta de um homem de sessenta e oito anos de dinheiro antigo, autoridade tranquila",
         local="um salão de mansão silencioso", lux=True),
    dict(nome="Avery Knox", arquivo="AVERY_KNOX", genero="mulher", pos="her", sheet="producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg",
         identidade=("The exact fictional AI character Avery Knox: white American woman around fifty-six, voluminous shaggy "
                     "layered platinum-blonde hair with visible darker roots, brown eyes, fair skin with crow's feet and fine "
                     "lines, everyday makeup with defined brows, mascara and pink lipstick."),
         roupa=("White long-sleeve button-up shirt with a chest pocket and the cuffs rolled, a large turquoise and silver squash-blossom "
                "necklace, several big turquoise rings and silver cuff bracelets set with turquoise on both wrists."),
         mao="her fair hand with big turquoise rings and a silver turquoise cuff bracelet", manga="a rolled white shirt cuff",
         sofa="a big light-grey sofa with a grey faux-fur throw", fundo=("an open American kitchen with white cabinets, recessed ceiling lights, a stainless-steel "
                                                                       "fridge and a dark door frame at the right"),
         casa="an ordinary American living room", janela="a large sliding glass door and window with a green backyard",
         sotaque="texano carregado", voz="voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos",
         local="uma sala de estar silenciosa", lux=False),
    dict(nome="Devon Price", arquivo="DEVON_PRICE", genero="mulher", pos="her", sheet="producao/_ancoras/character_sheets/devon_price_character_sheet.jpg",
         identidade=("The exact fictional AI character Devon Price: American woman aged about 50, slim, completely bald with a smooth "
                     "natural scalp and a few small freckles, no wig, no headscarf, light hazel-green eyes, thin natural pale eyebrows, "
                     "oval face with high cheekbones, freckles across the nose and cheeks, real aged skin with fine forehead lines, "
                     "crow's feet and laugh lines, no makeup, small silver stud earrings, a warm gentle half smile."),
         roupa=("Cream lace blazer over a cream lace camisole, a rose-gold beaded bracelet on the right wrist, a thin silver necklace "
                "with a small heart pendant, a silver band ring on the right ring finger and a thin silver ring on the left index finger."),
         mao="her freckled fair hand with a silver ring on the index finger", manga="a cream lace blazer cuff",
         sofa="a big light-grey sofa with a grey faux-fur throw", fundo=("an open American kitchen with white cabinets, recessed ceiling lights, a stainless-steel "
                                                                       "fridge and a dark door frame at the right"),
         casa="an ordinary American living room", janela="a large sliding glass door and window with a green backyard",
         sotaque="neutro da Califórnia", voz="voz feminina suave, calorosa e feminina de uma mulher de cinquenta anos, acolhedora e espiritual",
         local="uma sala de estar silenciosa", lux=False),
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
ACAO = {
    "T1": "{n} segura a carta de tarô com as costas pretas e douradas voltadas para a lente, perto do rosto, e a gira devagar com o polegar até mostrar a frente, The Empress (uma imperatriz sentada num trono, fundo amarelo, manto vermelho), apoiando-a na palma aberta ao lado do queixo; no fim da fala baixa a carta e sorri para a lente.",
    "T2": "{n} ergue o dedo indicador em \"it's not because you work harder\" e depois abre a mão em \"worked harder than anyone\".",
    "T3": "{n} conta as quatro frases curtas nos dedos de uma mão e balança a cabeça de leve em \"the money was gone before the month was\".",
    "T4": "{n} fala olhando fixo para a lente, as duas mãos juntas diante do peito, com um pequeno aceno de cabeça em \"She did everything right\".",
    "T5": "{n} imita a pergunta inclinando a cabeça em \"what could you possibly tell me\" e fica em silêncio um instante em \"I had no answer\".",
    "T6": "{n} faz o gesto de \"ok\" com a mão em \"effort\" e bate o dedo no ar em \"the lock on the door\".",
    "T7": "{n} gira o punho como quem aperta uma trava em \"tightened it\" e abre a mão em \"rusted shut\".",
    "T8": "{n} leva a mão ao peito em \"my grandmother Odessa\" e ergue os olhos por um instante em \"Archangel Uriel\".",
    "T9": "{n} ergue três dedos em \"three sentences\" e aponta para baixo em \"right before bed\".",
    "T10": "{n} ergue três dedos em \"three times\" e abre a mão em direção à lente em \"waiting for you\".",
    "T11": "{n} sorri de leve e suspira com alívio em \"finally opened\", uma mão aberta no peito.",
    "T12": "{n} aponta o dedo para a lente em \"comment 222\" e toca o peito com a mão em \"your name\".",
    "T13": "{n} ergue o polegar em \"Like\", faz o gesto de salvar com a mão em \"Save it\" e leva a mão ao próprio peito em \"follow me\".",
    "T14": "{n} balança a cabeça devagar em \"Marlene's cousin skipped one\" e aponta o indicador para a lente em \"Skip one\".",
    "T15": "{n} aponta o indicador para baixo em \"tap my profile picture\" e abre as mãos em \"I wish I'd known this sooner\".",
}


def cena(a):
    if a["lux"]:
        return (f"{a['casa'].capitalize()} at the end of a day, seen from a sofa: behind the speaker, the back of {a['sofa']}, and beyond it "
                f"{a['fundo']}, with {a['janela']} on the right, all under a grey-white overcast sky.")
    return (f"{a['casa'].capitalize()} seen from the sofa: behind the speaker, the back of {a['sofa']}, and beyond it {a['fundo']}, "
            f"with {a['janela']} on the right, all under a grey-white overcast sky.")


def keyframes(a):
    n, pos = a["nome"], a["pos"]
    base = {"fiction_note": FICCAO,
            "reference_use": (f"Use the attached image (character sheet) only for {n}'s exact identity (face, skin, hair, body) "
                              "and wardrobe; ignore its grey studio background. The setting, camera angle and framing are "
                              "described in full in the scene, camera and composition fields; no other image is attached."),
            "identity_main": a["identidade"], "wardrobe": a["roupa"]}
    k1 = dict(base)
    k1.update({
        "scene": cena(a),
        "prop": f"The hero object is {CARTA_COSTAS}, held up in {pos} right hand beside {pos} face on the right side of the frame, its back turned toward the lens.",
        "posture": (f"{n} sits on the sofa holding the phone for a selfie, looking wide-eyed and delighted into the lens, mouth open, caught "
                    f"mid-sentence, the right hand ({a['mao']}, {a['manga']}) holding the card up near the lens."),
        "composition": (f"The card is very close to the lens, about 12 inches from the lens, large in frame, about 20 percent of the frame, at the right "
                        f"edge beside the face, closer to the camera than {pos} face. {n}'s head and shoulders fill the frame, the top of the head near the upper "
                        f"12 percent. Nothing else is in the foreground. The background is reduced by framing, never by blur."),
        "camera": "front camera selfie, phone held in the left hand about 14 inches from the face, about three and a half feet above the floor, 1x lens, level, slight natural handheld wobble",
        "lighting": LUZ,
        "state": f"Start frame: {n} is caught mid-sentence with lips parted and eyes wide, the card back toward the lens, just about to turn it.",
        "realism": REALISMO, "aspect_ratio": "9:16 vertical",
        "negative": NEG + ", no text on the card, no card front visible, no second card",
    })
    k2 = dict(base)
    k2.update({
        "scene": cena(a),
        "prop": f"The hero object is {n}'s open raised right hand ({a['mao']}), palm half turned toward the lens with the fingers relaxed, in the lower right of the frame, gesturing as {pos} talks. No other prop.",
        "posture": (f"{n} sits on the sofa holding the phone for a selfie, looking straight into the lens, caught mid-sentence, lips naturally "
                    f"parted, an animated, sincere expression, one hand raised open at chest height near the lens, {a['manga']} visible."),
        "composition": (f"The open hand is very close to the lens, about 14 inches from the lens, about 15 percent of the frame, in the lower right, closer to the camera than "
                        f"{pos} face. {n}'s head and shoulders fill the frame, the top of the head near the upper 12 percent. Nothing else is in the foreground. "
                        f"The background is reduced by framing, never by blur."),
        "camera": "front camera selfie, phone held in the left hand about 14 inches from the face, about three and a half feet above the floor, 1x lens, level, slight natural handheld wobble",
        "lighting": LUZ,
        "state": f"Start frame: {n} is caught mid-sentence, lips parted, the right hand open at chest height, no card in hand.",
        "realism": REALISMO, "aspect_ratio": "9:16 vertical",
        "negative": NEG + ", no tarot card, no card in hand, no object in hand",
    })
    return [dict(codigo="K01", take="T1", titulo="gancho, selfie com a carta de tarô de costas perto da lente", j=k1),
            dict(codigo="K02", take="T2 a T15", titulo=f"corpo, {n} em selfie no sofá, mão aberta gesticulando", j=k2)]


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art = "o avatar" if h else "a avatar"
    abre = (f"{art} ({a['genero']}) {n} fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, em tom de conversa de quem "
            "grava um vídeo no celular para os seguidores, natural, próximo e confiante, no mesmo ritmo do vídeo modelo, "
            "{emo}, a seguinte frase: \"{fala}\"")
    diz = (f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar "
           "no final. Lip sync perfeito durante todo o vídeo.")
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        acao = ACAO[t].format(n=n)
        if not h:
            pass
        txt = (abre.format(emo=EMOCAO[t], fala=FALAS[t]) + "\n\n" + diz + "\n\n"
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


def capcut():
    return [
        "1. Clipes na ordem: V01 a V15, jump cut seco entre eles (um frame de base, selfie contínua como no modelo).",
        "2. Texto fixo no topo durante o vídeo inteiro: `You are going to become WEALTHY` (creme, serifada). Legenda karaokê no terço inferior, branca em caixa alta, palavra-chave com tarja rosa.",
        "3. Insert entre V09 e V10: cartão de player de áudio genérico, sem marca, título `Seven Night Seal`, frases borradas (o conteúdo fica no Stories).",
        "4. Sem Voice Changer: a voz vem do prompt de cada V. Isolate Voice / Keep Vocal no áudio.",
        "5. Música só depois do V01, baixa, fora da biblioteca do TikTok. Sem números brilhantes (222) na imagem.",
        "6. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# {a['nome']} | Auraly Venda Prosperidade v3 | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `input/modelo.mp4` (37,1 s, pessoa real, orgânico)", "",
         f"Character sheet: `{a['sheet']}`", "",
         "Funil: venda, dinheiro e prosperidade. Comentar `222`, depois Stories. Rodada de validação.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|",
         f"| T1 | K01 | só o CHARACTER SHEET de {a['nome']} | GERAR DO ZERO |",
         f"| T2 a T15 | K02 | só o CHARACTER SHEET de {a['nome']} | GERAR DO ZERO |", "",
         "## Trava de identidade e continuidade", "",
         f"- Identidade: {a['identidade']}", f"- Roupa (do character sheet): {a['roupa']}",
         f"- Cenário: {cena(a)}", f"- Luz: {LUZ}",
         f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.", "- Sem 2ª pessoa.", "",
         "## Trava do prop herói", "", f"- K01: {CARTA_COSTAS}.", "- K02: a mão aberta do avatar, sem outro objeto.", "",
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
    L = [f"# ENTREGA | {a['nome']} | Auraly Venda Prosperidade v3", "",
         "Produção `auraly_venda_prosperidade_v3` · Ângulo 3 · SALE (dinheiro e prosperidade) · vídeo modelo de pessoa real (orgânico) · rodada de VALIDAÇÃO · perfil AURALY", "",
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
    for t in TAKES:
        L.append(f"{t[1:]}. {FALAS[t]}")
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
