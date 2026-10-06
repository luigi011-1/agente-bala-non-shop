"""Gera os pacotes por avatar da producao auraly_venda_dinheiro_v1 (Auraly, venda, dinheiro, validacao, origem ORGANICA).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco). Regra do Luigi de 2026-10-06: K so com o character
sheet do avatar; V so com a imagem escolhida do K. Nada de frame modelo anexado: cenario, pose, camera e acao
vao por escrito em cada prompt. Mapa: K01 -> V01 (T1), K02 -> V02 a V16 (corpo, enquadramento unico).
Saidas por avatar: PROMPTS_<AVATAR>.md, FLOW_<AVATAR>.md e ENTREGA_<AVATAR>.md.
Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")

HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 17)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES)
tab = ROTEIRO.split("## Tradução completa")[1].split("\n## ")[0]
PT = {t: p for t, e, p in re.findall(r"^\| (T\d+)(?: \(novo\))? \| (.+?) \| (.+?) \|$", tab, re.M)}
assert set(PT) == set(TAKES), PT

MAPA = {"V01": "K01", **{"V%02d" % i: "K02" for i in range(2, 17)}}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
COZINHA = ("An ordinary American home kitchen, bright and lived in: a white glossy subway-tile wall, a large window with a "
           "white frame on the left with the outside clearly visible through it (a wooden fence with a lattice top and a "
           "small garden of green plants under an overcast sky), and on the right a light-wood open shelf holding a trailing "
           "green pothos plant in a white pot and a row of cookbooks, above a light-grey quartz countertop that runs along "
           "the whole bottom of the frame.")
LUZ = ("Neutral overcast daylight from the large window on the left, the outside clearly visible through the window, "
       "never white or blown out, soft even light on the face and hands with no harsh shadows, no warm kitchen lights.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, "
            "iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, "
            "background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no brand names, no logos and no printed text on the bottle, "
       "the jar or the dish, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no third "
       "hand, no supernatural lighting, no glowing objects, no steam, no smoke, no blur, no bokeh, no artificial lighting, "
       "no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, "
       "no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no tarot cards, "
       "no candles")

GARRAFA = ("a white plastic bottle of rubbing alcohol with a flip cap and a plain pale-blue label with no readable text")
POTE = ("a small clear glass spice jar full of ground cinnamon powder with a plain red-brown label with no readable text "
        "and a brown cap")
PIREX = "a rectangular clear glass baking dish with straight sides"

AVATARES = [
    dict(nome="Avery Knox", arquivo="AVERY_KNOX", genero="mulher", pos="her", sheet="producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg",
         identidade=("The exact fictional AI character Avery Knox: white American woman around fifty-six, voluminous shaggy "
                     "layered platinum-blonde hair with visible darker roots, brown eyes, fair skin with crow's feet and fine "
                     "lines, everyday makeup with defined brows, mascara and pink lipstick."),
         roupa=("White long-sleeve button-up shirt with a chest pocket and the cuffs rolled, medium-blue bootcut jeans, a "
                "large turquoise and silver squash-blossom necklace, several big turquoise rings and silver cuff bracelets "
                "set with turquoise on both wrists."),
         maos="her fair hand with big turquoise rings", sotaque="texano carregado",
         voz="voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos"),
    dict(nome="Devon Price", arquivo="DEVON_PRICE", genero="mulher", pos="her", sheet="producao/_ancoras/character_sheets/devon_price_character_sheet.jpg",
         identidade=("The exact fictional AI character Devon Price: white American woman around fifty-two, closely shaved head "
                     "with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, "
                     "fine lines and no makeup."),
         roupa=("Light-wash denim shirt worn open with the cuffs rolled over a fitted black crew-neck T-shirt, dark blue jeans, "
                "large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the "
                "T-shirt collar."),
         maos="her freckled fair hand with bare fingers", sotaque="de Chicago",
         voz="voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago"),
    dict(nome="Jordan Vale", arquivo="JORDAN_VALE", genero="homem", pos="his", sheet="producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg",
         identidade=("The exact fictional AI character Jordan Vale, explicitly male: white American man around fifty-eight, long "
                     "grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, "
                     "sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded "
                     "traditional American tattoos with no lettering, a swallow and a red rose on the left forearm."),
         roupa="Black leather vest over a heather grey crew-neck T-shirt, dark blue straight jeans.",
         maos="his weathered tattooed hand", sotaque="do Tennessee",
         voz="voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee"),
]

EMOCAO = {
    "T1": "em tom firme e confiante, como quem mostra um truque estranho",
    "T2": "em voz baixa e confidencial",
    "T3": "em tom sério e convicto, quase sussurrando",
    "T4": "em tom calmo e certo, com pausa depois de \"first\" e depois de \"second\"",
    "T5": "em tom firme e direto",
    "T6": "em tom caloroso e seguro",
    "T7": "em tom animado e forte, subindo de intensidade",
    "T8": "em tom solene e respeitoso",
    "T9": "em tom firme e aliviado ao dizer \"the worst is finally over\"",
    "T10": "em tom intenso e convicto",
    "T11": "em tom firme, marcando \"222\" e \"followed by your name\"",
    "T12": "em tom solene, de última palavra",
    "T13": "em tom firme, em ritmo de instrução, um selo de cada vez",
    "T14": "em tom duro, urgente e sério, sem levantar a voz",
    "T15": "em tom calmo e certo",
    "T16": "em tom próximo e urgente, olhando direto na lente",
}
ACAO_PADRAO = "{n} fala olhando fixo para a lente, com um pequeno aceno de cabeça. O recipiente de vidro com a pasta marrom continua parado na bancada diante dele ou dela e nada mais muda."
ACAO = {
    "T2": "{n} abre uma das mãos e dá de ombros de leve, olhando fixo para a lente, a outra mão apoiada na borda da bancada.",
    "T3": "{n} inclina a cabeça de leve para a frente e leva um dedo aos lábios por um instante na palavra \"secret\", sem cobrir a boca.",
    "T4": "{n} ergue o dedo indicador na palavra \"first\" e dois dedos na palavra \"second\", olhando para a lente.",
    "T7": "{n} abre as duas mãos devagar, como quem indica algo grande vindo na direção da lente.",
    "T8": "{n} ergue o olhar por um instante e volta para a lente na frase do portal, uma mão aberta no peito.",
    "T9": "{n} sacode a cabeça devagar na palavra \"over\" e solta o ar, ombros relaxando.",
    "T11": "{n} aponta o dedo indicador para a lente na palavra \"comment\" e depois toca o peito com a mão aberta em \"your name\".",
    "T12": "{n} baixa o queixo e olha fixo para a lente, uma mão apoiada na bancada, a outra fechada em punho leve junto ao peito na palavra \"Like\".",
    "T13": "{n} conta nos dedos, um dedo em \"second seal\" e três dedos em \"third seal\", olhando para a lente.",
    "T14": "{n} levanta uma das mãos aberta, palma para a lente, na frase \"Hear me clearly\" e depois a baixa devagar e aponta para a bancada vazia ao lado do recipiente em \"the door closes\".",
    "T16": "{n} aponta o dedo indicador para a lente e depois para baixo na palavra \"stories\", olhando direto para a lente.",
}


def keyframes(a):
    n, pos = a["nome"], a["pos"]
    base = {"fiction_note": FICCAO,
            "reference_use": (f"Use the attached image (character sheet) only for {n}'s exact identity (face, skin, hair, body) "
                              "and wardrobe; ignore its grey studio background. The kitchen, camera, pose and action are "
                              "described in this prompt."),
            "identity_main": a["identidade"], "wardrobe": a["roupa"]}
    k1 = dict(base)
    k1.update({
        "scene": COZINHA + " The countertop in the lower foreground is empty except for one clear glass baking dish.",
        "prop": (f"The hero objects are {GARRAFA}, held up in one of {pos} hands, and {POTE}, held up in the other hand, both "
                 f"raised at chest height on either side of the face, labels toward the lens. On the countertop in the lower "
                 f"foreground sits {PIREX}, empty and dry."),
        "posture": (f"{n} stands upright behind the counter facing the lens, both arms raised with the bottle in one hand and "
                    "the jar in the other, looking straight into the lens with a flat knowing look, caught mid-sentence, "
                    "lips naturally parted, animated expression."),
        "composition": (f"The white plastic bottle of rubbing alcohol and the small clear glass spice jar are very close to the "
                        f"lens, about 14 inches from the lens, large in frame, about 30 percent of the frame together, closer "
                        f"to the camera than {pos} face, nothing else competing with them. The empty glass baking dish sits "
                        f"on the counter at the bottom edge of the frame, about 22 inches from the lens. {n} is framed from "
                        f"the top of the head to the waist. Nothing else is in the foreground. The background is reduced by "
                        f"framing, never by blur."),
        "camera": "phone propped on a stand on the counter about four feet above the floor, about three feet from the person, 1x lens, pointing level, fixed",
        "lighting": LUZ,
        "state": f"Start frame: {n} holds the sealed bottle and the sealed jar up, the baking dish empty, caught mid-sentence.",
        "realism": REALISMO, "aspect_ratio": "9:16 vertical",
        "negative": NEG + ", no liquid already poured, no cinnamon already in the dish, no hands in the dish",
    })
    k2 = dict(base)
    k2.update({
        "scene": COZINHA,
        "prop": (f"The hero object is {PIREX} on the countertop, filled with a swirled brown paste of cinnamon and alcohol with "
                 f"small darker clumps floating in it, a spiral pattern from the stirring. The bottle and the jar are gone "
                 f"from the scene."),
        "posture": (f"{n} stands upright behind the counter facing the lens, one hand resting flat on the counter beside the "
                    f"dish, the other hand raised open at chest height in a small explaining gesture, looking straight into "
                    f"the lens, caught mid-sentence, lips naturally parted, animated expression."),
        "composition": (f"The rectangular clear glass dish with the swirled brown paste is very close to the lens in the lower "
                        f"foreground, about 25 percent of the frame, its near edge about 20 inches from the lens, closer to "
                        f"the camera than {pos} face, nothing else competing with it. {n} is framed from the top of the head "
                        f"to the waist. Nothing else is in the foreground and the counter beside the dish is empty. The "
                        f"background is reduced by framing, never by blur."),
        "camera": "phone propped on a stand on the counter about four feet above the floor, about three feet from the person, 1x lens, pointing level, fixed",
        "lighting": LUZ,
        "state": f"Start frame: {n} stands with one hand on the counter and the other raised open, mid-sentence, the paste still in the dish.",
        "realism": REALISMO, "aspect_ratio": "9:16 vertical",
        "negative": NEG + ", no bottle in frame, no jar in frame, no utensils, no spoon",
    })
    return [dict(codigo="K01", take="T1", titulo="gancho, frasco de álcool e pote de canela erguidos, recipiente vazio", j=k1),
            dict(codigo="K02", take="T2 a T16", titulo="corpo, recipiente com a pasta de canela, fala para a lente", j=k2)]


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art = "o avatar" if h else "a avatar"
    abre = (f"{art} {n}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, em tom de conversa de quem "
            "grava um vídeo no celular para os seguidores, natural, próximo e confiante, no mesmo ritmo de um vídeo orgânico, "
            "{emo}, a seguinte frase: \"{fala}\"")
    diz = (f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar "
           "no final. Lip sync perfeito durante todo o vídeo.")
    quem = "o homem" if h else "a mulher"
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        if t == "T1":
            acao = (f"{n} já está falando com o frasco de álcool numa mão e o pote de canela na outra. Em seguida inclina o frasco e o "
                    "álcool cai num fio fino dentro do recipiente de vidro na bancada; depois inclina o pote e a canela em pó cai "
                    "por cima do álcool; depois larga o pote, mexe a mistura com o dedo indicador em círculos até virar uma pasta "
                    "marrom; por fim segura o recipiente com as duas mãos e o ergue em direção à lente, olhando para a lente na "
                    "última frase.")
            cam = "celular apoiado, fixo, sem movimento, um plano só, sem cortes"
            som = "cozinha silenciosa, líquido caindo no vidro e o ruído leve da mistura, sem música"
        else:
            acao = ACAO.get(t, ACAO_PADRAO).format(n=n).replace("dele ou dela", "dele" if h else "dela")
            cam = "celular apoiado, fixo, sem movimento"
            som = "cozinha silenciosa, leve zumbido de geladeira ao fundo, sem música"
        txt = (abre.format(emo=EMOCAO[t], fala=FALAS[t]) + "\n\n" + diz + "\n\n"
               f"o que acontece no vídeo: {acao}\n\ncâmera: {cam}\n\nsom ambiente: {som}")
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
        "1. Clipes numerados na ordem: V01 a V16.",
        "2. V01: usar do início até o recipiente erguido (~6 s) e fechar com um flash branco rápido (0,5 s) entrando no V02, como no modelo.",
        "3. V02 a V16: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Todos saem do mesmo "
        "frame, então a troca de clipe fica no mesmo enquadramento (jump cut), como no modelo.",
        "4. Legenda karaokê palavra a palavra no centro do quadro, branca, fonte serifada grossa, do V01 ao V16.",
        "5. Sem Voice Changer: a voz vem do prompt de cada V. Isolate Voice / Keep Vocal no áudio.",
        "6. Música só depois do V01, baixa, fora da biblioteca do TikTok.",
        "7. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# {a['nome']} | Auraly Venda Dinheiro v1 | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `input/modelo.mp4` (110,8 s, pessoa real, orgânico)", "",
         f"Character sheet: `{a['sheet']}`", "",
         "Funil: venda, ramificação de dinheiro. Selos (like, save, envio), comentar `222` com o nome, depois Stories. Rodada de validação.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|",
         f"| T1 | K01 | só o CHARACTER SHEET de {a['nome']} | GERAR DO ZERO |",
         f"| T2 a T16 | K02 | só o CHARACTER SHEET de {a['nome']} | GERAR DO ZERO |", "",
         "## Trava de identidade e continuidade", "",
         f"- Identidade: {a['identidade']}", f"- Roupa (do character sheet): {a['roupa']}",
         f"- Cenário (do modelo): {COZINHA}", f"- Luz: {LUZ}",
         f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.", "- Sem 2ª pessoa.", "",
         "## Trava do prop herói", "", f"- Frasco: {GARRAFA}.", f"- Pote: {POTE}.", f"- Recipiente: {PIREX}.", "",
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
    L = [f"# ENTREGA | {a['nome']} | Auraly Venda Dinheiro v1", "",
         "Produção `auraly_venda_dinheiro_v1` · Ângulo 3 · SALE (dinheiro, prosperidade e fortuna) · vídeo modelo de pessoa real (orgânico) · rodada de VALIDAÇÃO · perfil AURALY", "",
         "## 1. Anexos e mapa", "",
         f"- **Imagem (K):** anexar SÓ o character sheet de {a['nome']} (`{a['sheet']}`) e colar o prompt. Nada de frame modelo.",
         "- **Vídeo (V):** anexar SÓ a imagem que você escolheu daquele K e colar o prompt de vídeo.",
         "- Instruções do agente do Flow: já estão com você (`flow_agente/AGENTE_FLOW_AURALY_ATUAL.md`), não repito aqui.",
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
