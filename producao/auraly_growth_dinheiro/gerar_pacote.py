"""Gera os pacotes por avatar da producao auraly_growth_dinheiro (Auraly, growth, dinheiro, avatar IA, validacao).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Identidade, roupa e
cenario: ROSTER AURALY ATIVO (avatares-fichas) e as ancoras em cena real. Medidas: FICHA_FRAMES.md.
Prompt de imagem em JSON (Flow v17). Mapa K/V: K01 -> V01 (gancho mudo), K02 -> V02 a V19 (corpo).

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
assert TAKES == ["T%d" % i for i in range(1, 20)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES) - {"T1"}, FALAS.keys()
PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$", ROTEIRO.split("## Tradução completa (Português)")[1].split("\n## ")[0], re.M))
assert set(PT) == set(TAKES), PT

MAPA = {"V01": "K01", **{"V%02d" % i: "K02" for i in range(2, 20)}}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
LUZ_INTERNA = ("Neutral overcast daylight from a window, the outside clearly visible through the window, never white or "
               "blown out, soft even light on the face, hands and feet with no harsh shadows.")
LUZ_EXTERNA = ("Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on "
               "the face, hands and feet with no harsh shadows.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no printed lettering or brand on the perfume bottle, "
       "no studio, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, "
       "no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, "
       "no golden hour light, no sunset, no red neon, no de-aging, no beauty smoothing, no visible phone, no HDR, "
       "no cinematic lighting, no second person in frame, no bathroom, no bathtub")
FRASCO = ("a tall faceted gold perfume bottle with an ornate embossed pattern and a gold cap, completely plain with no "
          "label")

AVATARES = [
    dict(nome="Darlene Pruitt", arquivo="DARLENE_PRUITT", genero="mulher", pron="She", pos="her",
         ancora="producao/_ancoras/darlene_pruitt_ancora.jpg",
         identidade=("The exact fictional AI character Darlene Pruitt: white American woman around fifty-six from Texas, "
                     "voluminous shaggy layered platinum-blonde hair with visible dark roots, brown eyes, fair skin with "
                     "crow's feet and fine lines, everyday makeup with defined brows, mascara and pink lipstick."),
         roupa=("White long-sleeve button-up shirt with the cuffs loosely rolled, blue jeans rolled up at the ankles, "
                "barefoot, a large turquoise and silver squash-blossom necklace, several big turquoise rings on the fingers "
                "of both hands and a silver cuff bracelet set with turquoise."),
         superficie="her wooden kitchen island",
         cena=("Her own rustic American kitchen with knotty pine wood-paneled walls, the same lived-in kitchen as the "
               "reference, unchanged: the wooden kitchen island, the pine wall with a framed astrological chart and a small "
               "wooden crucifix, and the open wooden shelves by the window with glass jars, a lit white candle and a small "
               "American flag, discreet but visible and in focus."),
         assento="a low wooden stool beside her kitchen island",
         carta=("the holographic SOULMATE card from the reference: a tarot-sized card with a rainbow mirror-foil border and "
                "saturated art of a dark-haired woman and a man embracing forehead to forehead under a starry purple sky, a "
                "glowing red heart between them and red roses around, with the word SOULMATE on a cream banner at the bottom"),
         luz=LUZ_INTERNA, sotaque="texano carregado",
         voz="voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos",
         som="cozinha residencial silenciosa"),
    dict(nome="Lorraine Vance", arquivo="LORRAINE_VANCE", genero="mulher", pron="She", pos="her",
         ancora="producao/_ancoras/lorraine_vance_ancora.jpg",
         identidade=("The exact fictional AI character Lorraine Vance: white American woman around fifty-two, closely "
                     "shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, "
                     "defined jaw, fine lines and no makeup."),
         roupa=("Light-wash denim shirt worn open over a fitted black crew-neck T-shirt, dark jeans rolled up at the ankles, "
                "barefoot, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses "
                "hanging from the T-shirt collar."),
         superficie="her white quartz kitchen counter",
         cena=("Her own bright white American kitchen, the same lived-in kitchen as the reference, unchanged: white walls and "
               "white quartz counters, the light wood floating shelves with clear quartz crystal points, a lit incense stick, "
               "a white pillar candle and a small American flag, discreet but visible and in focus, a framed zodiac wheel "
               "chart and a small wooden crucifix on the wall, and a window with the street clearly visible."),
         assento="a low stool beside her kitchen counter",
         carta=("the holographic SOULMATE card from the reference: a tarot-sized card with a rainbow mirror-foil border and "
                "saturated art of a brown-haired woman and a man embracing under a rainbow glow, a bright heart and red roses "
                "at the bottom, with the word SOULMATE on a pale banner at the bottom"),
         luz=LUZ_INTERNA, sotaque="de Chicago",
         voz="voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago",
         som="cozinha residencial silenciosa"),
    dict(nome="Walt Hensley", arquivo="WALT_HENSLEY", genero="homem", pron="He", pos="his",
         ancora="producao/_ancoras/walt_hensley_ancora.jpg",
         identidade=("The exact fictional AI character Walt Hensley, explicitly male: white American man around fifty-eight, "
                     "long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, "
                     "sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded "
                     "traditional American tattoos with no lettering, a swallow and a red rose on the left forearm."),
         roupa="Black leather vest over a heather grey crew-neck T-shirt and dark blue jeans rolled up at the ankles, barefoot.",
         superficie="his small wooden porch side table",
         cena=("His own American front porch with grey weathered wooden siding and a grey wooden deck, the same lived-in porch "
               "as the reference, unchanged: the old wooden rocking chair, the framed astrological chart and a small wooden "
               "crucifix on the siding, the small wooden side table with a white candle in a jar and crystals, and a small "
               "American flag on the porch post against the overcast sky, discreet but visible and in focus."),
         assento="the seat of his old wooden rocking chair",
         carta=("the holographic SOULMATE card from the reference: a tarot-sized card with a rainbow mirror-foil border and "
                "saturated art of a long-haired woman in red and a bearded tattooed man embracing, surrounded by red roses, "
                "with an iridescent heart at the bottom and the word SOULMATE on a white banner at the bottom"),
         luz=LUZ_EXTERNA, sotaque="do Tennessee",
         voz="voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee",
         som="varanda tranquila, leve vento e passarinhos ao longe"),
]

EMOCAO = {
    "T2": "confiante e direta, apontando para quem assiste", "T3": "baixa, como quem conta um segredo de gente rica",
    "T4": "firme", "T5": "séria", "T6": "séria e próxima", "T7": "intrigante, marcando \"It is about your feet\"",
    "T8": "calma e convicta", "T9": "suave", "T10": "calma e inspirada", "T11": "reverente, como quem ora",
    "T12": "reverente e emocionada", "T13": "calorosa, depois animada", "T14": "firme e convicta",
    "T15": "animada", "T16": "firme, em ritmo de instrução", "T17": "firme e rápida",
    "T18": "firme, depois séria", "T19": "próxima e urgente, olhando direto na lente",
}
MASC = {"séria": "sério", "próxima": "próximo", "convicta": "convicto", "calma": "calmo", "inspirada": "inspirado",
        "emocionada": "emocionado", "calorosa": "caloroso", "animada": "animado", "rápida": "rápido",
        "confiante": "confiante", "direta": "direto", "baixa": "baixo", "intrigante": "intrigante"}
ACAO = {
    "T2": "{n} aponta para a lente com uma mão, segurando a carta com a outra, e fala.",
    "T7": "{n} aponta para os próprios pés descalços enquanto fala.",
    "T11": "{n} fecha os olhos por um instante, como quem ora, e volta a olhar para a lente.",
    "T12": "{n} fala de olhos semicerrados, com a mão livre no peito.",
    "T16": "{n} mostra a carta para a lente e fala com firmeza.",
    "T19": "{n} se inclina para a lente e aponta para ela, segurando a carta.",
}
ACAO_PADRAO = "{n} aponta para a lente com uma mão e segura a carta com a outra, falando com pequenos gestos naturais."
TITULOS = {"K01": "gancho mudo, perfume no pé descalço colado na lente", "K02": "corpo, câmera alta, apontando para a lente"}


def keyframes(a):
    n, P, p = a["nome"], a["pron"], a["pos"]
    ref = (f"Use the first attached image only for {n}'s exact identity, wardrobe, jewelry, SOULMATE card and own "
           f"setting. Use the second attached image only as a composition reference for the camera position, framing "
           f"and pose; do not copy its person, robe, bathroom, gold fixtures, labels or on-screen text.")
    k01 = {
        "prop": (f"The sole of the bare foot of {n} rests on the edge of {a['superficie']}, right in front of the lens, "
                 f"toes up. In one hand {n} holds {FRASCO}, and sprays it toward the sole of the bare foot."),
        "posture": (f"{n} sits right behind the foot on {a['assento']}, one leg stretched out with the bare foot resting "
                    f"on the edge, leaning back slightly, spraying the perfume, looking at the lens with a calm, serious face, "
                    f"mouth closed."),
        "composition": (f"Extreme low-angle close-up: the sole of the bare foot is very close to the lens, about 6 inches from "
                        f"the lens, filling the right half of the frame, about 45 percent of the frame, touching the right "
                        f"edge, far larger than {p} head, nothing else competing with it. {n} sits behind it, left of center, "
                        f"face in the upper third; the gold perfume bottle in {p} hand at chest height on the left. Nothing "
                        f"else is on the edge. The background is reduced by framing, never by blur."),
        "camera": "phone resting low, at the height of the table edge, 0.5x ultra-wide lens, pointing slightly upward, fixed",
        "state": "Start frame: a fine mist of perfume is leaving the bottle toward the sole of the bare foot.",
        "negative": NEG + ", no card in frame, no shoes, no socks",
    }
    k02 = {
        "prop": (f"On the edge of {a['superficie']} in the lower left corner stands {FRASCO}. With one hand {n} points at the "
                 f"lens; in the other hand, at chest height and facing the lens, {P.lower()} holds {a['carta']}."),
        "posture": (f"{n} sits on a low seat, {a['assento']}, leaning forward toward the lens, bare feet on the floor, one "
                    f"hand pointing at the lens."),
        "composition": (f"High-angle shot: the gold perfume bottle is very close to the lens in the lower left corner, about 12 "
                        f"inches from the lens, and takes up about 15 percent of the frame, closer to the camera than {p} "
                        f"face. {n} sits low in the center, seen from the top of the head down to the bare feet, face in the "
                        f"upper third, one hand pointing at the lens. Nothing else is on the edge. The background is reduced "
                        f"by framing, never by blur."),
        "camera": "phone held up high, high angle from above looking down at about forty-five degrees, 1x lens, fixed",
        "state": f"Start frame: {n} points at the lens, caught mid-sentence, lips naturally parted, animated expression.",
        "negative": NEG + ", no second card, no standing pose",
    }
    out = []
    for cod, d, take in (("K01", k01, "T1"), ("K02", k02, "T2 a T19")):
        j = {"shot_id": f"{cod}_{a['arquivo'].lower()}", "fiction_note": FICCAO, "reference_use": ref,
             "identity_main": a["identidade"], "wardrobe": a["roupa"], "scene": a["cena"], "prop": d["prop"],
             "posture": d["posture"], "composition": d["composition"], "camera": d["camera"], "lighting": a["luz"],
             "state": d["state"], "realism": REALISMO, "aspect_ratio": "9:16 vertical", "negative": d["negative"]}
        out.append(dict(codigo=cod, take=take, titulo=TITULOS[cod], j=j))
    return out


def emocao(t, homem):
    e = EMOCAO[t]
    return re.sub(r"\w+", lambda m: MASC.get(m.group(0), m.group(0)), e) if homem else e


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art = "o avatar" if h else "a avatar"
    ouvido = "ouvido" if h else "ouvida"
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        if t == "T1":
            txt = (f"(sem fala no take: gancho mudo, {art} fica em silêncio o clipe inteiro, boca fechada)\n\n"
                   f"o que acontece no vídeo: {n} borrifa o frasco dourado de perfume na sola do pé descalço, que está "
                   f"colado na lente; depois larga o frasco e esfrega o pé devagar com as duas mãos.\n\n"
                   "câmera: fixa, rente à superfície, grande angular, sem movimento\n\n"
                   f"som ambiente: {a['som']}, som do borrifo do perfume, sem música")
        else:
            txt = (f"{art} {n}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
                   f"{emocao(t, h)}, voz autêntica, como se exigisse ser {ouvido}, a seguinte frase: \"{FALAS[t]}\"\n\n"
                   f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
                   f"sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
                   f"o que acontece no vídeo: {ACAO.get(t, ACAO_PADRAO).format(n=n)}\n\n"
                   "câmera: fixa, de cima, sem movimento\n\n"
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
        "1. Clipes numerados na ordem: V01 a V19.",
        "2. V01 (gancho mudo): usar ~2,6 s. Tarja \"PUT PERFUME ON YOUR FEET\" em amarelo no alto e \"Millionaire mode: "
        "Unlocked 🔒\" num balão branco no meio. Flash de luz de 0,1 s no corte para o V02.",
        "3. V02 a V19: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / "
        "Keep Vocal. Todos saem do mesmo frame, então a troca de clipe fica no mesmo enquadramento, como no modelo.",
        "4. Legenda karaokê amarela e branca, do V02 ao V19; \"222 ✨\" fixo no canto superior esquerdo do V02 ao V19.",
        "5. Setas vermelhas apontando para cima no V19.",
        "6. Sem Voice Changer: a voz vem do prompt de cada V.",
        "7. Música só a partir do V02, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "8. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS.get(t, '(sem fala)')} | {PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# {a['nome']} | Auraly Growth Dinheiro | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `/Users/macbookairm2/Downloads/snapinsta-1790652632203.mp4` (130,6 s, avatar IA)", "",
         f"Âncora: `{a['ancora']}`", "",
         "Funil: growth, like + save + envio + `222` + follow. Rodada de validação.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|",
         f"| T1 | K01 | ÂNCORA {a['nome'].upper()} + FRAME DO MODELO (K01) | GERAR DO ZERO |",
         f"| T2 a T19 | K02 | ÂNCORA {a['nome'].upper()} + FRAME DO MODELO (K02) | GERAR DO ZERO |", "",
         "## Trava de identidade e continuidade", "",
         f"- Identidade: {a['identidade']}", f"- Roupa (fixa da conta): {a['roupa']}",
         f"- Cenário-base (fixo da conta): {a['cena']}", f"- Luz: {a['luz']}",
         f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.", "- Sem 2ª pessoa.", "",
         "## Trava do prop herói", "", f"- Frasco: {FRASCO}.", f"- Carta: {a['carta']}.", "",
         "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "", "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · ÂNCORA {a['nome'].upper()} + FRAME DO MODELO", "",
              "> ### 📎 ANEXAR: **2 IMAGENS**", f"> **1️⃣ ÂNCORA {a['nome'].upper()}** `{a['ancora']}`",
              f"> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/{k['codigo']}_modelo.png`", ">",
              "> ### 🆕 GERAR DO ZERO", "", f"Cena: {k['titulo']}.", "", "```json",
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


CHECKLIST = ("Checklist de envio: 32/32 aprovados (N/A: A1, A2, A7, A9 fiéis ao modelo, gancho mudo; A10 growth sem "
             "produto; C3 a C7 sem segunda pessoa, selfie, frase curta repetida, cena atuada ou motion control)")
FICHA = "Ficha: 2/2 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)"


def entrega(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Growth Dinheiro", "",
         "Produção `auraly_growth_dinheiro` · Ângulo 3 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY", "",
         f"## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v{VERSAO})", "",
         "Colar inteiro na memória do agente antes do primeiro K.", "", "```text", BLOCO_FLOW, "```", "",
         CHECKLIST, "", FICHA, "", "## Anexos e mapa", "",
         f"- **Âncora {a['nome']}:** `{a['ancora']}` em TODOS os K.",
         "- **Em cada K**, anexar também o frame do modelo daquele K (`input/frames_modelo/Kxx_modelo.png`), só como composição.",
         "", "```text"] + mapa_kv() + ["```", "", "## 2. PROMPTS DE IMAGEM (um bloco por K)", ""]
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
        L.append(f"{i}. {FALAS.get(t, '(sem fala: gancho mudo)')}")
    L += ["", " ".join(FALAS[t] for t in TAKES if t in FALAS), ""]
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
