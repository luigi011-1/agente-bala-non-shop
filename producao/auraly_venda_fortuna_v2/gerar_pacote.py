"""Gera os pacotes por avatar da producao auraly_venda_fortuna_v2 (Auraly, venda, dinheiro, validacao, origem organica).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco). Regra do Luigi de 2026-10-06: o K so anexa o
character sheet do avatar e o V so anexa a imagem escolhida; cenario, camera, pose e acao do modelo vao por
extenso dentro de cada prompt. Mapa K/V: K01 -> V01 (gancho mudo POV), K02 -> V02 a V14 (corpo, plano unico).
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
HALL = ("An ordinary American family-house entryway hall: smooth white walls with white baseboards and a light oak "
        "hardwood plank floor. On the right a white six-panel front door with two round black door knobs and a glass "
        "window at the top, and a tall glass sidelight window beside it; through the glass the overcast grey sky, a "
        "green lawn and neighbouring houses are clearly visible. On the left wall a small black-framed picture with a "
        "beige mat, and behind it a dark open doorway into a hallway.")
LUZ = ("Neutral overcast daylight from the glass of the front door and the sidelight, the sky outside with visible cloud "
       "texture, never white or blown out, soft even light on the face and hands with no harsh shadows.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no numbers overlaid on the image, no glowing "
            "numbers, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural "
            "lighting, no glowing aura, no sparkles, no light coming out of the leaf, no blur, no bokeh, no "
            "artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour "
            "light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, no second person in frame")
CELULAR = ("a modern dark graphite smartphone with a three-lens camera block in its top left corner, in a clear "
           "transparent phone case with reinforced shock-absorbing corners")
FOLHA = "a single dried bay leaf, olive-green with a pale central vein and a pointed tip, about four inches long"

AVATARES = [
    dict(nome="Avery Knox", arquivo="AVERY_KNOX", genero="mulher", pron="She", pos="her", obj="her",
         sheet="producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg",
         identidade=("The exact fictional AI character Avery Knox: white American woman around sixty, voluminous shaggy "
                     "layered platinum-blonde hair with darker roots, brown eyes, fair skin with crow's feet and fine "
                     "lines, everyday makeup with defined brows, mascara and soft pink lipstick."),
         roupa=("White long-sleeve button-up shirt with the cuffs loosely rolled to the forearms, blue bootcut jeans, a "
                "large turquoise and silver squash-blossom necklace, several big turquoise rings on her fingers, a "
                "silver cuff bracelet set with turquoise, and tan suede ankle boots."),
         maos="her fair hands with big turquoise rings and the silver turquoise cuff bracelet below the rolled white cuffs",
         voz="voz feminina quente e firme, levemente rouca, de uma mulher de sessenta anos"),
    dict(nome="Devon Price", arquivo="DEVON_PRICE", genero="mulher", pron="She", pos="her", obj="her",
         sheet="producao/_ancoras/character_sheets/devon_price_character_sheet.jpg",
         identidade=("The exact fictional AI character Devon Price: white American woman around fifty-five with a closely "
                     "buzzed head of grey hair, freckles and sunspots across her face, light grey-green eyes, a defined "
                     "jaw, fine lines and no makeup."),
         roupa=("Light-wash denim shirt worn open over a fitted black crew-neck T-shirt, dark blue jeans, large silver hoop "
                "earrings, a thin silver chain necklace with black-framed reading glasses hanging from the T-shirt "
                "collar, and olive slip-on shoes."),
         maos="her freckled fair hands with bare fingers below the rolled denim cuffs",
         voz="voz feminina grave, direta e de humor seco, de uma mulher de cinquenta e cinco anos"),
    dict(nome="Jordan Vale", arquivo="JORDAN_VALE", genero="homem", pron="He", pos="his", obj="him",
         sheet="producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg",
         identidade=("The exact fictional AI character Jordan Vale, explicitly male: white American man around sixty, long "
                     "grey-white beard down to mid-chest, grey hair combed back, sun-weathered skin with freckles and deep "
                     "crow's feet, light hazel eyes, both forearms covered in faded traditional American tattoos with no "
                     "lettering, a swallow and a red rose among them."),
         roupa="Black leather vest with snap buttons over a heather grey crew-neck T-shirt, dark blue jeans and olive slip-on shoes.",
         maos="his weathered hands and tattooed forearms with faded swallow and rose tattoos",
         voz="voz masculina grave, calma e gentil, de um homem de sessenta anos"),
]

ACAO = {
    "T2": "{n} fala olhando para a lente, balança a cabeça de leve e aponta o indicador da mão direita para o celular que segura na mão esquerda, com a folha de louro visível na capinha.",
    "T3": "{n} fecha os olhos por um instante e volta a olhar para a lente, sem sorrir, o indicador da mão direita apontando para a lente na última frase.",
    "T4": "{n} aponta o indicador da mão direita para a lente com firmeza na última frase, o celular com a folha parado na mão esquerda.",
    "T5": "{n} olha firme para a lente e aponta o indicador da mão direita para a lente quando diz a palavra final, o celular parado na mão esquerda.",
    "T6": "{n} faz uma pausa curta, gira a mão direita aberta na frente do peito e aponta para a lente na palavra final, o celular com a folha na mão esquerda.",
    "T7": "{n} inclina o corpo um pouco para a lente e aponta o indicador da mão direita para a lente, o celular com a folha na mão esquerda.",
    "T8": "{n} aponta para a lente com a mão direita, depois aponta para o próprio celular que segura na mão esquerda, olhar sério.",
    "T9": "{n} olha para a lente e acena firme com a cabeça, a mão direita aberta apontando para baixo em direção ao celular, a esquerda segura o celular.",
    "T10": "{n} fica firme e solene, sem sorrir, o indicador da mão direita levantado na frente do rosto para marcar o aviso, o celular com a folha na mão esquerda.",
    "T11": "{n} olha para a lente em tom solene, abre a mão direita e a vira para cima, o celular com a folha na mão esquerda.",
    "T12": "{n} aponta o indicador da mão direita para baixo, para a própria mão e para a lente, com o celular com a folha na mão esquerda.",
    "T13": "{n} fecha os olhos por um instante e volta a olhar para a lente, a mão direita aberta no ar, o celular com a folha na mão esquerda.",
    "T14": "{n} se inclina um pouco para a lente e aponta o indicador da mão direita para baixo e para a lente, o celular com a folha na mão esquerda.",
}
EMOCAO = {
    "T2": "baixa e confidencial, como quem conta um segredo", "T3": "séria e direta, quase sussurrando no começo",
    "T4": "firme, em tom de alerta", "T5": "calma e certa", "T6": "calma e segura, com pausa antes de \"okay\"",
    "T7": "séria, como quem anuncia algo importante", "T8": "firme e muito séria", "T9": "firme e convicta",
    "T10": "grave e solene, em tom de aviso", "T11": "calma e firme", "T12": "próxima e urgente",
    "T13": "baixa e intensa", "T14": "próxima e urgente, olhando direto para a lente",
}
MASC = {"séria": "sério", "firme": "firme", "convicta": "convicto", "certa": "certo", "calma": "calmo", "segura": "seguro",
        "baixa": "baixo", "intensa": "intenso", "próxima": "próximo", "confidencial": "confidencial", "direta": "direto",
        "grave": "grave", "solene": "solene", "urgente": "urgente", "muito": "muito"}
SOM = "hall de casa silencioso, leve eco natural da voz, ruído suave de roupa, sem música"


def emocao(t, homem):
    e = EMOCAO[t]
    return re.sub(r"\w+", lambda m: MASC.get(m.group(0), m.group(0)), e) if homem else e


def keyframes(a):
    n, P, p = a["nome"], a["pron"], a["pos"]
    ref = (f"Use the attached character sheet only for {n}'s exact identity (face, skin, hair, body), wardrobe and "
           f"jewelry; ignore its grey studio background. The setting, camera angle, pose and action are fully "
           f"described in this prompt.")
    k01 = {
        "prop": (f"In {p} left hand {n} holds {CELULAR}, upright with its back facing the lens. With {p} right hand "
                 f"{P.lower()} pinches {FOLHA}, and is sliding it in under the right edge of the clear case on the back "
                 f"of the phone, the leaf half hidden. Nothing else is in the hands."),
        "posture": (f"First-person point of view from {n}'s own eyes: only {p} two hands and forearms and the phone are "
                    f"visible, {a['maos']}; no face is visible."),
        "composition": (f"The phone and the two hands are very close to the lens in the lower foreground, the phone about "
                        f"10 inches from the lens, and together they take up about 40 percent of the frame; the phone is "
                        f"left of center, tall in frame, camera block at the top. The light hardwood floor fills the bottom "
                        f"third and the hall behind fills the rest. Nothing else is in frame. The background is reduced by "
                        f"framing, never by blur."),
        "camera": ("phone camera at chest height looking down about 30 degrees toward the hands, 1x lens, handheld with a "
                   "slight natural shake"),
        "state": "Start frame: the leaf is pinched at the right edge of the phone and has just started to slide under the case.",
        "negative": NEG_BASE + ", no face in frame, no other props, no leaf already inside the case",
    }
    k02 = {
        "prop": (f"In {p} left hand, held out at chest height on the left side of the frame, {n} holds {CELULAR}, its back "
                 f"facing the lens, with {FOLHA} lying flat and centered under the clear case. The index finger of {p} "
                 f"right hand points toward the phone. Nothing else is held in either hand."),
        "posture": (f"{n} is crouched low on {p} heels very near the lens, knees up and apart, forearms resting on the "
                    f"thighs, leaning slightly forward, head tilted a little, looking straight into the lens, caught "
                    f"mid-sentence, lips naturally parted, animated expression."),
        "composition": (f"{n} fills the frame from the top of the head, about 10 percent from the top edge, down to the "
                        f"knees at the bottom edge, centered slightly right. The phone with the bay leaf is held forward at "
                        f"the left, about 24 inches from the lens, closer to the camera than {p} face, and takes up about "
                        f"10 percent of the frame. The hall behind fills the rest. Nothing else is in frame. The "
                        f"background is reduced by framing, never by blur."),
        "camera": ("phone camera at about two feet above the floor, roughly the waist height of the crouched person, 1x "
                   "lens tilted slightly up toward the face, fixed with a slight natural handheld shake"),
        "state": f"Start frame: {n} is already looking into the lens, caught mid-sentence, finger pointing toward the phone.",
        "negative": NEG_BASE + ", no second leaf, no other props in the hands, no face covered by the phone",
    }
    out = []
    for cod, d, take, titulo in (("K01", k01, "T1", "gancho mudo, POV das mãos encaixando a folha de louro na capinha"),
                                 ("K02", k02, "T2 a T14", "corpo, agachado com o celular e a folha de louro")):
        j = {"shot_id": f"{cod}_{a['arquivo'].lower()}", "fiction_note": FICCAO, "reference_use": ref,
             "identity_main": a["identidade"], "wardrobe": a["roupa"], "scene": HALL, "prop": d["prop"],
             "posture": d["posture"], "composition": d["composition"], "camera": d["camera"], "lighting": LUZ,
             "state": d["state"], "realism": REALISMO, "aspect_ratio": "9:16 vertical", "negative": d["negative"]}
        out.append(dict(codigo=cod, take=take, titulo=titulo, j=j))
    return out


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art = "o avatar" if h else "a avatar"
    ouvido = "ouvido" if h else "ouvida"
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        if t == "T1":
            txt = (f"(sem fala no take: gancho mudo, ninguém fala, sem voz)\n\n"
                   f"o que acontece no vídeo: em primeira pessoa, {n} encaixa a folha de louro sob a borda direita da capinha "
                   f"transparente do celular com a mão direita, empurra a folha até o meio e alisa com o polegar até ela ficar "
                   f"centrada na parte de trás do celular, que segura na mão esquerda. Em seguida a mão direita sai de quadro e a "
                   f"folha fica visível sob a capinha.\n\n"
                   "câmera: fixa, ponto de vista de quem segura o celular, com leve tremor natural de mão\n\n"
                   "som ambiente: hall de casa silencioso, leve ruído de papel e de dedos na capinha, sem música")
        else:
            txt = (f"{art} {n} ({a['genero']}) fala em inglês com sotaque americano de {n}, {a['voz']}, em tom de conversa de "
                   f"quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, {emocao(t, h)}, a "
                   f"seguinte frase: \"{FALAS[t]}\"\n\n"
                   f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
                   f"sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
                   f"o que acontece no vídeo: {ACAO[t].format(n=n)}\n\n"
                   "câmera: fixa, na altura da cintura de quem está agachado, com leve tremor natural de celular\n\n"
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
        "2. V01 (gancho mudo): usar ~3,3 s, da folha entrando sob a capinha até ela centrada. Tarja fixa no topo, caixa branca, letras vermelhas: \"HIDE A BAY LEAF IN YOUR PHONE CASE\". Corte seco (flash branco curto) para o V02.",
        "3. V02 a V14: jump cut a cada take, todos saem do mesmo frame, então o enquadramento não muda, como no modelo. Cortar logo depois da última palavra. Isolate Voice / Keep Vocal no áudio.",
        "4. Legenda karaokê branca, palavra atual em amarelo, na altura do celular, do V02 ao V14.",
        "5. Números neon pequenos (777 no peito, 888, 111 e 222 soltos no ar, como no modelo) só no CapCut, do V03 em diante. Nunca dentro do K.",
        "6. Emoji de dedo apontando para baixo no canto inferior esquerdo no V14.",
        "7. Sem Voice Changer: a voz vem do prompt de cada V. Música só a partir do V02, baixa, fora da biblioteca do TikTok.",
        "8. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS.get(t, '(sem fala)')} | {PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# {a['nome']} | Auraly Venda Fortuna v2 | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `input/modelo.mp4` (78,5 s, orgânico: homem real, folha de louro na capinha)", "",
         f"Character sheet: `{a['sheet']}`", "",
         "Funil: venda, dinheiro e fortuna. Enviar + `222`, salvar, depois foto de perfil e Stories. Rodada de validação.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|",
         f"| T1 | K01 | CHARACTER SHEET {a['nome'].upper()} | GERAR DO ZERO |",
         f"| T2 a T14 | K02 | CHARACTER SHEET {a['nome'].upper()} | GERAR DO ZERO |", "",
         "## Trava de identidade e continuidade", "",
         f"- Identidade: {a['identidade']}", f"- Roupa (a do character sheet): {a['roupa']}",
         f"- Cenário (o do modelo): {HALL}", f"- Luz: {LUZ}",
         f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano.", "- Sem 2ª pessoa.", "",
         "## Trava do prop herói", "", f"- Celular: {CELULAR}.", f"- Folha: {FOLHA}.", "",
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
    L = [f"# ENTREGA | {a['nome']} | Auraly Venda Fortuna v2", "",
         "Produção `auraly_venda_fortuna_v2` · Ângulo 3 · SALE (dinheiro e fortuna) · vídeo modelo orgânico · rodada de VALIDAÇÃO · perfil AURALY", "",
         "Instruções do agente do Flow: já estão em `flow_agente/AGENTE_FLOW_AURALY_ATUAL.md` (memória do agente desta produção); não há outro bloco de instruções neste pacote.", "",
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
