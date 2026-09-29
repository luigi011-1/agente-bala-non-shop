"""Gera os pacotes por avatar da producao auraly_growth_prece (Auraly, growth, origem organica, validacao).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Identidade, roupa e
cenario: ROSTER AURALY ATIVO (avatares-fichas) e as ancoras em cena real. Medidas: FICHA_FRAMES.md.
Origem organica (PERFIL_ORGANICO.md): selfie apoiada, maos em prece coladas na lente, sem kit
obrigatorio, sem carta, primeira linha do V no tom de conversa de celular. Prompt de imagem em JSON
(Flow v17). Mapa K/V: o plano unico do modelo vira um K01 que alimenta V01 a V14.

Saidas por avatar: PROMPTS_<AVATAR>.md, FLOW_<AVATAR>.md e ENTREGA_<AVATAR>.md.
Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")
INSTR = (AQUI.parent / "_flow" / "INSTRUCOES_AGENTE_FLOW.md").read_text(encoding="utf-8")
VERSAO = re.search(r"^Versao (\d+)", INSTR, re.M).group(1)
BLOCO_FLOW = re.search(r"## Bloco para a memoria do executor\n\n(.*?)\n## Historico resumido", INSTR, re.S).group(1).rstrip()

HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 15)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES), FALAS
PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$", ROTEIRO.split("## Tradução completa (Português)")[1].split("\n## ")[0], re.M))
assert set(PT) == set(TAKES), PT

MAPA = {"V%02d" % i: "K01" for i in range(1, 15)}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
LUZ_INTERNA = ("Neutral overcast daylight from a window, the outside clearly visible through the window, never white or "
               "blown out, soft even light on the face and hands with no harsh shadows.")
LUZ_EXTERNA = ("Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on "
               "the face and hands with no harsh shadows.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra "
       "fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color "
       "cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no lamp glow, no de-aging, no "
       "beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no card in hand, "
       "no props in the hands, no standing pose")

AVATARES = [
    dict(nome="Darlene Pruitt", arquivo="DARLENE_PRUITT", genero="mulher", pron="She", pos="her",
         ancora="producao/_ancoras/darlene_pruitt_ancora.jpg",
         identidade=("The exact fictional AI character Darlene Pruitt: white American woman around fifty-six from Texas, "
                     "voluminous shaggy layered platinum-blonde hair with visible dark roots, brown eyes, fair skin with "
                     "crow's feet and fine lines, everyday makeup with defined brows, mascara and pink lipstick."),
         roupa=("White long-sleeve button-up shirt with the cuffs loosely rolled, blue jeans, a large turquoise and silver "
                "squash-blossom necklace, several big turquoise rings on the fingers of both hands and a silver cuff "
                "bracelet set with turquoise."),
         maos="her fair hands with big turquoise rings on several fingers",
         cena=("Her own rustic American kitchen with knotty pine wood-paneled walls, the same lived-in kitchen as the "
               "reference, unchanged. She sits at her wooden kitchen island; behind her the pine wall with a framed "
               "astrological chart and a small wooden crucifix, and the open wooden shelves by the window with glass jars "
               "and a small American flag, discreet but visible and in focus."),
         luz=LUZ_INTERNA, sotaque="texano carregado",
         voz="voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos",
         som="cozinha residencial silenciosa"),
    dict(nome="Lorraine Vance", arquivo="LORRAINE_VANCE", genero="mulher", pron="She", pos="her",
         ancora="producao/_ancoras/lorraine_vance_ancora.jpg",
         identidade=("The exact fictional AI character Lorraine Vance: white American woman around fifty-two, closely "
                     "shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, "
                     "defined jaw, fine lines and no makeup."),
         roupa=("Light-wash denim shirt worn open over a fitted black crew-neck T-shirt, dark jeans, large silver hoop "
                "earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar."),
         maos="her freckled fair hands with bare fingers",
         cena=("Her own bright white American kitchen, the same lived-in kitchen as the reference, unchanged. She sits at "
               "her white quartz counter; behind her the light wood floating shelves with clear quartz crystal points, a "
               "white pillar candle and a small American flag, discreet but visible and in focus, and a window at the left "
               "with the street clearly visible."),
         luz=LUZ_INTERNA, sotaque="de Chicago",
         voz="voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago",
         som="cozinha residencial silenciosa"),
    dict(nome="Walt Hensley", arquivo="WALT_HENSLEY", genero="homem", pron="He", pos="his",
         ancora="producao/_ancoras/walt_hensley_ancora.jpg",
         identidade=("The exact fictional AI character Walt Hensley, explicitly male: white American man around fifty-eight, "
                     "long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, "
                     "sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded "
                     "traditional American tattoos with no lettering, a swallow and a red rose on the left forearm."),
         roupa="Black leather vest over a heather grey crew-neck T-shirt and dark blue jeans.",
         maos="his weathered hands with faded tattoos on the forearms",
         cena=("His own American front porch with grey weathered wooden siding, the same lived-in porch as the reference, "
               "unchanged. He sits in his old wooden rocking chair; behind him the siding with the framed astrological "
               "chart and a small wooden crucifix, and at the right a small American flag on the porch post against the "
               "overcast sky, discreet but visible and in focus."),
         luz=LUZ_EXTERNA, sotaque="do Tennessee",
         voz="voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee",
         som="varanda tranquila, leve vento e passarinhos ao longe"),
]

EMOCAO = {
    "T1": "quase em segredo", "T2": "séria, em tom de aviso", "T3": "baixa e animada",
    "T4": "aliviada e emocionada", "T5": "firme e calma", "T6": "séria, depois intrigada",
    "T7": "intensa", "T8": "calorosa", "T9": "firme", "T10": "urgente e próxima",
    "T11": "em ritmo de instrução", "T12": "firme, depois animada", "T13": "baixa e séria",
    "T14": "próxima e firme",
}
MASC = {"séria": "sério", "animada": "animado", "aliviada": "aliviado", "emocionada": "emocionado",
        "intrigada": "intrigado", "intensa": "intenso", "calorosa": "caloroso", "próxima": "próximo",
        "baixa": "baixo", "calma": "calmo"}
ACAO = {
    "T1": "{n} mantém as mãos juntas em prece perto da lente e fala baixo olhando para a lente.",
    "T5": "{n} aperta de leve as mãos juntas em prece enquanto fala.",
    "T6": "{n} fecha os olhos por um instante e volta a olhar para a lente, com as mãos em prece.",
    "T11": "{n} abre as mãos por um instante e junta de novo em prece enquanto fala.",
    "T14": "{n} se inclina um pouco para a lente, com as mãos em prece.",
}
ACAO_PADRAO = "{n} mantém as mãos juntas em prece perto da lente e fala olhando para a lente, piscando devagar."


def keyframes(a):
    n, P, p = a["nome"], a["pron"], a["pos"]
    j = {
        "shot_id": f"K01_{a['arquivo'].lower()}",
        "fiction_note": FICCAO,
        "reference_use": (f"Use the first attached image only for {n}'s exact identity, wardrobe, jewelry and own setting. "
                          f"Use the second attached image only as a composition reference for the camera position, framing "
                          f"and pose; do not copy its person, clothes, bedroom, lamp or on-screen text."),
        "identity_main": a["identidade"],
        "wardrobe": a["roupa"],
        "scene": a["cena"],
        "prop": (f"No objects: {a['maos']} are the only thing in the foreground, hands pressed together in prayer with the "
                 f"fingers interlaced and the fingertips pointing up."),
        "posture": (f"{n} sits facing the lens, elbows resting in front of {p} chest, hands pressed together in prayer "
                    f"right in front of the phone, looking straight into the lens."),
        "composition": (f"Casual selfie framing: the hands pressed together in prayer are very close to the lens in the "
                        f"bottom center, about 8 inches from the lens, and take up about 20 percent of the frame, touching the "
                        f"bottom edge, closer to the camera than {p} face, nothing else competing with them. {p.capitalize()} "
                        f"face sits in the upper middle of the frame, shoulders and chest in the middle, the setting behind in the "
                        f"top third. Nothing else is in the foreground. The background is reduced by framing, never by blur."),
        "camera": "phone propped on the surface just below the chin, at chest height, 1x front lens, pointing slightly upward, fixed",
        "lighting": a["luz"],
        "state": f"Start frame: {n} looks into the lens, caught mid-sentence, lips naturally parted, calm and intimate expression.",
        "realism": REALISMO,
        "aspect_ratio": "9:16 vertical",
        "negative": NEG,
    }
    return [dict(codigo="K01", take="T1 a T14", titulo="selfie apoiada, mãos em prece coladas na lente", j=j)]


def emocao(t, homem):
    e = EMOCAO[t]
    return re.sub(r"\w+", lambda m: MASC.get(m.group(0), m.group(0)), e) if homem else e


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art = "o avatar" if h else "a avatar"
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        txt = (f"{art} {n} ({a['genero']}) fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, em tom de "
               f"conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, "
               f"{emocao(t, h)}, no mesmo ritmo do vídeo modelo, a seguinte frase: \"{FALAS[t]}\"\n\n"
               f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
               f"sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
               f"o que acontece no vídeo: {ACAO.get(t, ACAO_PADRAO).format(n=n)}\n\n"
               "câmera: celular apoiado, fixo, sem movimento\n\n"
               f"som ambiente: {a['som']}, sem música")
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
        "2. Zero tempo morto: todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / "
        "Keep Vocal no áudio. Todos saem do mesmo frame, então a troca de clipe vira jump cut no mesmo enquadramento, "
        "a gramática do próprio formato orgânico.",
        "3. Legenda em serifa branca, 3 a 4 palavras por vez, no meio do quadro, do V01 ao V14, igual ao modelo.",
        "4. \"222\" fixo no canto superior esquerdo e \"11:11\" no canto superior direito, o vídeo inteiro.",
        "5. Sem Voice Changer: a voz vem do prompt de cada V.",
        "6. Música só depois do gancho (a partir do V02), baixa, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "7. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# {a['nome']} | Auraly Growth Prece | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `/Users/macbookairm2/Downloads/snapinsta-1790643406245.mp4` (117,3 s, pessoa real)", "",
         f"Âncora: `{a['ancora']}`", "",
         "Funil: growth, save + double tap + `222` + follow. Origem orgânica, rodada de validação.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|",
         f"| T1 a T14 | K01 | ÂNCORA {a['nome'].upper()} + FRAME DO MODELO (K01) | GERAR DO ZERO |", "",
         "## Trava de identidade e continuidade", "",
         f"- Identidade: {a['identidade']}", f"- Roupa (fixa da conta): {a['roupa']}",
         f"- Cenário-base (fixo da conta): {a['cena']}", f"- Luz: {a['luz']}",
         f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.", "- Sem 2ª pessoa.", "",
         "## Trava do prop herói", "", "- Não há prop: o herói são as mãos juntas em prece coladas na lente.", "",
         "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "", "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · ÂNCORA {a['nome'].upper()} + FRAME DO MODELO", "",
              "> ### 📎 ANEXAR: **2 IMAGENS**", f"> **1️⃣ ÂNCORA {a['nome'].upper()}** `{a['ancora']}`",
              "> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K01_modelo.png`", ">", "> ### 🆕 GERAR DO ZERO",
              "", f"Cena: {k['titulo']}.", "", "```json", json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
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


CHECKLIST = ("Checklist de envio: 32/32 aprovados (N/A: A1, A2, A7, A9 fiéis ao modelo orgânico; A10 growth sem "
             "produto; C3 a C7 sem segunda pessoa, selfie na mão, frase curta repetida, cena atuada ou motion control)")
FICHA = "Ficha: 1/1 K conferido contra o frame do modelo, placar 14/14 (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)"


def entrega(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Growth Prece", "",
         "Produção `auraly_growth_prece` · Ângulo 3 · GROWTH · vídeo modelo de pessoa real (orgânico) · rodada de VALIDAÇÃO · perfil AURALY", "",
         f"## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v{VERSAO})", "",
         "Colar inteiro na memória do agente antes do primeiro K.", "", "```text", BLOCO_FLOW, "```", "",
         CHECKLIST, "", FICHA, "", "## Anexos e mapa", "",
         f"- **Âncora {a['nome']}:** `{a['ancora']}` no K01.",
         "- **No K01**, anexar também `input/frames_modelo/K01_modelo.png`, só como composição.",
         "", "```text"] + mapa_kv() + ["```", "", "## 2. PROMPT DE IMAGEM", ""]
    for k in ks:
        L += [f"### {k['codigo']} · {k['take']}, {k['titulo']} · anexar ÂNCORA + FRAME DO MODELO", "",
              "```text", k["codigo"], texto_flow(k["j"]), "```", ""]
    L += ["## 3. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · frame inicial = a imagem escolhida do {kcod}", "", "```text", cod, txt, "```", ""]
    L += ["## 4. Montagem no CapCut", ""] + capcut()
    L += ["", "## 5. Transcrição final por take", ""] + transcricao()
    L += ["", "## 6. Roteiro final em inglês", ""]
    for i, t in enumerate(TAKES, 1):
        L.append(f"{i}. {FALAS[t]}")
    L += ["", " ".join(FALAS[t] for t in TAKES), ""]
    return "\n".join(L)


def main():
    for a in AVATARES:
        p, f = pacote(a)
        (AQUI / f"PROMPTS_{a['arquivo']}.md").write_text(p, encoding="utf-8")
        (AQUI / f"FLOW_{a['arquivo']}.md").write_text(f, encoding="utf-8")
        (AQUI / f"ENTREGA_{a['arquivo']}.md").write_text(entrega(a), encoding="utf-8")
    print("ok: %d avatares, Flow v%s" % (len(AVATARES), VERSAO))


if __name__ == "__main__":
    main()
