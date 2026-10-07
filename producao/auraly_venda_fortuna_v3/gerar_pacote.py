"""Gera os pacotes por avatar da producao auraly_venda_fortuna_v3 (Auraly, venda, dinheiro, validacao, avatar IA).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco). Regra do Luigi de 2026-10-06: o K so anexa o
character sheet do avatar e o V so anexa a imagem escolhida; cenario, camera, pose e acao do modelo vao por
extenso dentro de cada prompt. Regra do Luigi de 2026-10-07: o cenario do Gordon Ashby e sempre de luxo maximo
(dentro de casa = mansao fazendo a mesma acao). Mapa K/V: K01 -> V01 (gancho mudo), K02 -> V02 a V14 (corpo).
Saidas por avatar: PROMPTS_<AVATAR>.md, FLOW_<AVATAR>.md e ENTREGA_<AVATAR>.md. Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")
HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 15)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES) - {"T1"}, FALAS.keys()
PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$", ROTEIRO.split("## Tradução completa (Português)")[1].split("\n## ")[0], re.M))
assert set(PT) == set(TAKES), PT

MAPA = {"V01": "K01", **{"V%02d" % i: "K02" for i in range(2, 15)}}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
LUZ = ("Neutral overcast daylight from a tall window on the right, the sky outside showing grey-blue cloud texture, "
       "never white or blown out, soft even light on the face and hands with no harsh shadows and no warm cast.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no numbers overlaid on the image, no glowing "
            "numbers, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural "
            "lighting, no glowing aura, no sparkles, no light coming out of the money, no floating bills, no blur, "
            "no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, "
            "no golden hour light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, "
            "no second person in frame")
NOTA = ("a crisp US one-hundred-dollar bill, pale green-blue with a blue security ribbon, a portrait in the oval and "
        "a large gold-green 100 in the lower corner, about six inches long, with no readable serial number or text")
MACOS = ("tight stacks of US one-hundred-dollar bills, each stack held by a yellow paper band, piled in rows to the "
         "top of the cavity")

# Cenarios (modelo: cozinha americana; Avery copia o modelo, Gordon o mesmo layout em mansao, regra de 2026-10-07)
COZ_A_ORIG = ("An ordinary American family kitchen as in the model: white shaker cabinets with small brass pulls, a "
              "white marble island end with grey veining and a squared waterfall edge on the left of the frame, large "
              "beige floor tiles, a white tile backsplash at the top of the frame, and a small American flag in a "
              "brass holder on a counter far behind. The wooden toe-kick panel at the base of the white cabinet is "
              "tilted out of its slot.")
COZ_B_ORIG = ("An ordinary American family kitchen as in the model: dark walnut cabinets with brass pulls and a "
              "warm wooden toe-kick, a white marble island corner with grey veining on the left edge of the frame, a "
              "cream tile backsplash with a knife block behind, large beige floor tiles at the bottom of the frame, "
              "and a small American flag in a brass holder on the far counter.")
COZ_A_MANSAO = ("The kitchen of a luxury mansion, the same layout as the model: custom white cabinetry with solid brass "
                "pulls, a huge Calacatta marble island end with bold grey veining and a squared waterfall edge on the "
                "left of the frame, large polished cream marble floor tiles, a marble backsplash at the top of the "
                "frame, and a small American flag in a brass holder on a counter far behind. The wooden toe-kick "
                "panel at the base of the white cabinet is tilted out of its slot.")
COZ_B_MANSAO = ("The kitchen of a luxury mansion, the same layout as the model: custom dark walnut cabinetry with solid "
                "brass pulls, a huge Calacatta marble island corner with bold grey veining on the left edge of the "
                "frame, a cream marble backsplash with a professional range hood behind, large polished cream marble "
                "floor tiles at the bottom of the frame, and a small American flag in a brass holder on the far "
                "counter.")

AVATARES = [
    dict(nome="Gordon Ashby", arquivo="GORDON_ASHBY", genero="homem", pron="He", pos="his",
         sheet="producao/_ancoras/character_sheets/gordon_ashby_character_sheet.jpg",
         coz_a=COZ_A_MANSAO, coz_b=COZ_B_MANSAO, ambiente="cozinha de mansão",
         identidade=("The exact fictional AI character Gordon Ashby, explicitly male: white American man aged about 68, "
                     "slim and upright, full thick silver-white hair combed back, thin gold-rimmed round glasses, "
                     "light blue-grey eyes with heavy lids, narrow face, long straight nose, deep forehead lines, "
                     "crow's feet, sun spots on temples and cheeks, real aged skin, clean-shaven."),
         roupa=("Cream off-white tailored dinner jacket over a white dress shirt with a black silk bow tie, black dress "
                "trousers, black polished leather oxford shoes, a slim gold wristwatch on the left wrist and a plain "
                "gold ring on the left ring finger."),
         maos="his aged hands with a plain gold ring on the left ring finger and a slim gold wristwatch below the cream cuff",
         voz="voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo"),
    dict(nome="Avery Knox", arquivo="AVERY_KNOX", genero="mulher", pron="She", pos="her",
         sheet="producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg",
         coz_a=COZ_A_ORIG, coz_b=COZ_B_ORIG, ambiente="cozinha do modelo",
         identidade=("The exact fictional AI character Avery Knox: white American woman around sixty, voluminous shaggy "
                     "layered platinum-blonde hair with darker roots, brown eyes, fair skin with crow's feet and fine "
                     "lines, everyday makeup with defined brows, mascara and soft pink lipstick."),
         roupa=("White long-sleeve button-up shirt with the cuffs loosely rolled to the forearms, blue bootcut jeans, a "
                "large turquoise and silver squash-blossom necklace, several big turquoise rings on her fingers, a "
                "silver cuff bracelet set with turquoise, and tan suede ankle boots."),
         maos="her fair hands with big turquoise rings and the silver turquoise cuff bracelet below the rolled white cuffs",
         voz="voz feminina quente e firme, levemente rouca, de uma mulher de sessenta anos"),
]

ACAO = {
    "T2": "{n} fala baixo e confidencial olhando para a lente, a nota de $100 parada na mão direita, o braço esquerdo apoiado na quina de mármore, e balança a cabeça de leve na última frase.",
    "T3": "{n} inclina a cabeça um pouco para a lente e ergue a nota de $100 alguns centímetros na última frase, o braço esquerdo apoiado na quina de mármore.",
    "T4": "{n} fica sério e firme, olha direto para a lente e mexe a nota de $100 de leve na mão direita, o braço esquerdo apoiado na quina de mármore.",
    "T5": "{n} olha firme para a lente, balança a cabeça de leve em negativa duas vezes nas palavras finais, a nota de $100 parada na mão direita.",
    "T6": "{n} faz uma pausa curta, respira e fala com calma e certeza para a lente, a nota de $100 parada na mão direita, o braço esquerdo apoiado na quina de mármore.",
    "T7": "{n} fica solene, aponta a nota de $100 de leve em direção à lente na última frase, o braço esquerdo apoiado na quina de mármore.",
    "T8": "{n} olha para a lente em tom de alerta, inclina o corpo um pouco para a frente, a nota de $100 parada na mão direita.",
    "T9": "{n} fecha os olhos por um instante e volta a olhar para a lente com firmeza, a nota de $100 parada na mão direita.",
    "T10": "{n} faz um aceno firme com a cabeça em cada selo, a nota de $100 parada na mão direita, o braço esquerdo apoiado na quina de mármore.",
    "T11": "{n} aponta a nota de $100 para a lente na palavra final, olhar sério, o braço esquerdo apoiado na quina de mármore.",
    "T12": "{n} fica grave e solene, sem sorrir, inclina o corpo um pouco para a lente e segura a nota de $100 firme na mão direita.",
    "T13": "{n} olha para a lente com certeza tranquila e balança a cabeça de leve uma vez ao fim da frase, a nota de $100 parada na mão direita.",
    "T14": "{n} se inclina um pouco para a lente e aponta a nota de $100 para baixo e para a lente na palavra final, olhar direto.",
}
EMOCAO = {
    "T2": "baixa e confidencial, como quem conta um segredo", "T3": "séria e direta, quase sussurrando no começo",
    "T4": "firme, em tom de alerta", "T5": "calma e certa", "T6": "calma e segura, com pausa curta no começo",
    "T7": "séria, como quem anuncia algo importante", "T8": "firme e em tom de alerta",
    "T9": "firme e convicta", "T10": "firme e solene em cada selo", "T11": "firme e muito séria",
    "T12": "grave e solene, em tom de aviso", "T13": "calma e certa", "T14": "próxima e urgente, olhando direto para a lente",
}
MASC = {"séria": "sério", "firme": "firme", "convicta": "convicto", "certa": "certo", "calma": "calmo", "segura": "seguro",
        "baixa": "baixo", "próxima": "próximo", "confidencial": "confidencial", "direta": "direto",
        "grave": "grave", "solene": "solene", "urgente": "urgente", "muito": "muito"}
SOM = "cozinha silenciosa, leve eco natural da voz, ruído suave de roupa, sem música"


def emocao(t, homem):
    e = EMOCAO[t]
    return re.sub(r"\w+", lambda m: MASC.get(m.group(0), m.group(0)), e) if homem else e


def keyframes(a):
    n, P, p = a["nome"], a["pron"], a["pos"]
    ref = (f"Use the attached character sheet only for {n}'s exact identity (face, skin, hair, body), wardrobe and "
           f"jewelry; ignore its grey studio background. The setting, camera angle, pose and action are fully "
           f"described in this prompt.")
    k01 = {
        "scene": a["coz_a"],
        "prop": (f"The wooden toe-kick panel, about 30 inches wide and 5 inches tall, is tilted out of the base of the "
                 f"cabinet and held by {n}'s right hand at its lower edge. In the dark cavity behind it are {MACOS}, "
                 f"clearly visible. Nothing else is in the cavity or in the hands."),
        "posture": (f"{n} kneels on {p} right knee on the floor tiles beside the marble island end, {p} left arm "
                    f"stretched out and the left hand resting flat on the marble edge for balance, head lowered, "
                    f"looking down at the open cavity with a focused expression; {a['maos']}."),
        "composition": (f"{n} fills the frame from the top of the head, about 12 percent from the top edge, down to the "
                        f"floor at the bottom edge, placed in the right two thirds of the frame. The open cavity with "
                        f"the stacks of bills and the tilted panel take up about 30 percent of the frame in the lower "
                        f"left, about 28 inches from the lens, and are closer to the camera than {p} face. The marble "
                        f"edge runs along the left side. Nothing else is in frame. The background is reduced by framing, "
                        f"never by blur."),
        "camera": ("phone camera at about knee height, 1x lens looking slightly down toward the cavity, handheld with a "
                   "slight natural shake"),
        "state": f"Start frame: the panel has just been tilted out and {n}'s eyes are on the stacks of bills.",
        "negative": NEG_BASE + ", no face turned to the lens, no other props, no bills outside the cavity",
    }
    k02 = {
        "scene": a["coz_b"],
        "prop": (f"In {p} right hand, held low in the lower foreground at about 12 inches from the lens, {n} holds "
                 f"{NOTA}. Nothing else is held in either hand."),
        "posture": (f"{n} kneels very near the lens on {p} right knee, leaning forward, {p} left forearm resting on the "
                    f"squared marble corner at the left of the frame with the hand hanging over the edge, head tilted "
                    f"slightly, looking straight into the lens, caught mid-sentence, lips naturally parted; "
                    f"{a['maos']}."),
        "composition": (f"{n} fills the frame from the top of the head, about 8 percent from the top edge, down to the "
                        f"thighs at the bottom edge, centered slightly right. The bill is held in the lower foreground "
                        f"left of center, tilted toward the lens, about 12 inches from the lens, closer to the camera "
                        f"than {p} face, and takes up about 8 percent of the frame. The marble corner runs down the "
                        f"left edge and the cabinets and backsplash fill the rest. Nothing else is in frame. The "
                        f"background is reduced by framing, never by blur."),
        "camera": ("phone camera at about waist height of the kneeling person, roughly two feet above the floor, 1x "
                   "lens tilted slightly up toward the face, fixed with a slight natural handheld shake"),
        "state": f"Start frame: {n} is already looking into the lens, caught mid-sentence, the bill held low and tilted.",
        "negative": NEG_BASE + ", no second bill, no stack of bills in frame, no face covered by the hand",
    }
    out = []
    for cod, d, take, titulo in (("K01", k01, "T1", "gancho mudo, painel do rodapé aberto com maços de notas de $100"),
                                 ("K02", k02, "T2 a T14", "corpo, ajoelhado com o braço na quina de mármore e a nota de $100 na mão")):
        j = {"shot_id": f"{cod}_{a['arquivo'].lower()}", "fiction_note": FICCAO, "reference_use": ref,
             "identity_main": a["identidade"], "wardrobe": a["roupa"], "scene": d["scene"], "prop": d["prop"],
             "posture": d["posture"], "composition": d["composition"], "camera": d["camera"], "lighting": LUZ,
             "state": d["state"], "realism": REALISMO, "aspect_ratio": "9:16 vertical", "negative": d["negative"]}
        out.append(dict(codigo=cod, take=take, titulo=titulo, j=j))
    return out


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art = "o avatar" if h else "a avatar"
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        if t == "T1":
            txt = (f"(sem fala no take: gancho mudo, ninguém fala, sem voz)\n\n"
                   f"o que acontece no vídeo: plano 1, {n} ajoelhado inclina o painel de madeira do rodapé para o lado "
                   f"com a mão direita e o deixa cair no piso, e os maços de notas de $100 com cintas amarelas ficam "
                   f"à vista dentro do vão. Corte para plano 2, close do vão: a mão de {n} tira uma nota de $100 do topo "
                   f"do maço e a levanta, com a nota e os dedos em foco no instante em que sai do maço. Corte para plano 3, "
                   f"{n} de frente, em pé na cozinha, segurando a nota diante do peito e girando a nota para a lente, "
                   f"olhar sério.\n\n"
                   "câmera: cortes internos ao clipe, três planos, mão livre com leve tremor natural: plano 1 baixo, na "
                   "altura do joelho; plano 2 em close, no vão do rodapé; plano 3 frontal na altura do peito\n\n"
                   "som ambiente: cozinha silenciosa, madeira raspando no piso, farfalhar de notas de papel, sem música")
        else:
            txt = (f"{art} {n} ({a['genero']}) fala em inglês com sotaque americano de {n}, {a['voz']}, em tom de conversa de "
                   f"quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, {emocao(t, h)}, a "
                   f"seguinte frase: \"{FALAS[t]}\"\n\n"
                   f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
                   f"sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
                   f"o que acontece no vídeo: {ACAO[t].format(n=n)}\n\n"
                   "câmera: fixa, na altura da cintura de quem está ajoelhado, com leve tremor natural de celular\n\n"
                   f"som ambiente: {SOM}")
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
        "1. Clipes numerados na ordem: V01 a V14.",
        "2. V01 (gancho mudo): usar ~5,4 s, do painel caindo até a nota girando para a lente. Tarja fixa no topo, branca com contorno escuro: \"If you need urgent and unexpected money:\". Flash curto de transição para o V02.",
        "3. V02 a V14: jump cut a cada take, todos saem do mesmo frame, então o enquadramento não muda, como no modelo. Cortar logo depois da última palavra. Isolate Voice / Keep Vocal no áudio.",
        "4. Legenda karaokê branca, palavra atual em amarelo, no centro do quadro, do V02 ao V14.",
        "5. Números `444` com emoji de dinheiro no canto superior esquerdo e `11:11` no canto superior direito, só no CapCut, do V02 ao V14. Emojis (coração, olho, saco de dinheiro) sobre a nota no V03, como no modelo. Nunca dentro do K.",
        "6. Sem Voice Changer: a voz vem do prompt de cada V. Música só a partir do V02, baixa, fora da biblioteca do TikTok.",
        "7. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS.get(t, '(sem fala)')} | {PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# {a['nome']} | Auraly Venda Fortuna v3 | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `input/modelo.mp4` (102,2 s, careca abrindo o painel do rodapé com notas de $100)", "",
         f"Character sheet: `{a['sheet']}`", "",
         "Funil: venda, dinheiro e fortuna. Selos + `222`, depois foto de perfil e Stories. Rodada de validação.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|",
         f"| T1 | K01 | CHARACTER SHEET {a['nome'].upper()} | GERAR DO ZERO |",
         f"| T2 a T14 | K02 | CHARACTER SHEET {a['nome'].upper()} | GERAR DO ZERO |", "",
         "## Trava de identidade e continuidade", "",
         f"- Identidade: {a['identidade']}", f"- Roupa (a do character sheet): {a['roupa']}",
         f"- Cenário ({a['ambiente']}), gancho: {a['coz_a']}", f"- Cenário ({a['ambiente']}), corpo: {a['coz_b']}",
         f"- Luz: {LUZ}", f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano.", "- Sem 2ª pessoa.", "",
         "## Trava do prop herói", "", f"- Nota: {NOTA}.", f"- Maços: {MACOS}.", "",
         "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "",
         "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · CHARACTER SHEET {a['nome'].upper()}", "",
              "> ### 📎 ANEXAR: **1 IMAGEM**",
              f"> **1️⃣ CHARACTER SHEET {a['nome'].upper()}** `{a['sheet']}`",
              ">", "> ### 🆕 GERAR DO ZERO", "", f"Cena: {k['titulo']}.", "", "```json",
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


def entrega(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Venda Fortuna v3", "",
         "Produção `auraly_venda_fortuna_v3` · Ângulo 3 · SALE (dinheiro e fortuna) · rodada de VALIDAÇÃO · perfil AURALY", "",
         "Instruções do agente do Flow: `AGENTE_FLOW.md` desta produção (memória do agente, só esta produção).", "",
         "## Anexos e mapa", "",
         f"- **Imagem (K):** anexar SÓ o character sheet de {a['nome']} (`{a['sheet']}`) e colar o prompt. 4 variações, 9:16.",
         "- **Vídeo (V):** anexar SÓ a imagem escolhida daquele K e colar o prompt. 1 variação, 9:16.",
         "", "```text"] + mapa_kv() + ["```", "", "## 1. PROMPTS DE IMAGEM (um bloco por K)", ""]
    for k in ks:
        L += [f"### {k['codigo']} · {k['take']}, {k['titulo']} · anexar SÓ o CHARACTER SHEET", "",
              "```text", k["codigo"], texto_flow(k["j"]), "```", ""]
    L += ["## 2. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · anexar SÓ a imagem escolhida do {kcod}", "", "```text", cod, txt, "```", ""]
    L += ["## 3. Montagem no CapCut", ""] + capcut()
    L += ["", "## 4. Transcrição final por take", ""] + transcricao()
    L += ["", "## 5. Roteiro final em inglês", ""]
    for t in TAKES:
        L.append(f"{t[1:]}. {FALAS.get(t, '(sem fala)')}")
    L += ["", " ".join(FALAS[t] for t in TAKES if t in FALAS), ""]
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
