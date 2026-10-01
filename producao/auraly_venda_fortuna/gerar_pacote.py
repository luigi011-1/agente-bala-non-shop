"""Gera os pacotes por avatar da producao auraly_venda_fortuna (Auraly, venda, ramificacao de dinheiro, validacao).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Identidade, roupa e
cenario: ROSTER AURALY ATIVO (avatares-fichas) e as ancoras em cena real. Medidas: FICHA_FRAMES.md.
Prompt de imagem em JSON (Flow v17). Mapa K/V explicito: K01 -> V01 (gancho mudo), K02 -> V02
(inserto mudo), K03 -> V03 a V18 (corpo no enquadramento unico do modelo).

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
assert TAKES == ["T%d" % i for i in range(1, 19)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
MUDOS = [t for t in TAKES if "MUDO" in HEADS[t]]
assert MUDOS == ["T1", "T2"] and set(FALAS) == set(TAKES) - set(MUDOS), (MUDOS, FALAS.keys())
PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$", ROTEIRO.split("## Tradução completa (Português)")[1].split("\n## ")[0], re.M))
assert set(PT) == set(TAKES), PT

MAPA = {"V01": "K01", "V02": "K02", **{"V%02d" % i: "K03" for i in range(3, 19)}}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
LUZ_INTERNA = ("Neutral overcast daylight from the open window, the street outside clearly visible through the window, "
               "never white or blown out, soft even light on the face and hands with no harsh shadows.")
LUZ_EXTERNA = ("Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on "
               "the face and hands with no harsh shadows.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no printed lettering on the plate, the bowl or "
            "the medallion, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural "
            "lighting, no glowing aura, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow "
            "tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no "
            "visible phone, no HDR, no cinematic lighting, no second person in frame")

PRATO = "a shallow round gold plate with a wide flat rim, plain polished gold with soft reflections"
TIGELA = "a small dark wooden bowl heaped with coarse white salt crystals"
MEDALHAO = ("a large round gold coin medallion about the size of a palm, with a raised sunburst and a small star "
            "engraved on its face and a thick beaded rim, hanging from a thick gold rope chain")

AVATARES = [
    dict(nome="Darlene Pruitt", arquivo="DARLENE_PRUITT", genero="mulher", pron="She", pos="her",
         ancora="producao/_ancoras/darlene_pruitt_ancora.jpg",
         identidade=("The exact fictional AI character Darlene Pruitt: white American woman around fifty-six from Texas, "
                     "voluminous shaggy layered platinum-blonde hair with visible dark roots, brown eyes, fair skin with "
                     "crow's feet and fine lines, everyday makeup with defined brows, mascara and pink lipstick."),
         roupa=("White long-sleeve button-up shirt with the cuffs loosely rolled, blue jeans, a large turquoise and silver "
                "squash-blossom necklace, several big turquoise rings on the fingers of both hands and a silver cuff "
                "bracelet set with turquoise."),
         maos="her fair hand with big turquoise rings",
         cena=("Her own rustic American kitchen with knotty pine wood-paneled walls, the same lived-in kitchen as the "
               "reference, unchanged. She stands at the kitchen window, its wooden frame opened wide, with a wide wooden "
               "ledge under it; through the open window a quiet American residential street with houses, lawns and parked "
               "cars is clearly visible. On the open wooden shelf beside the window a small American flag, discreet but "
               "visible and in focus, and a lit white candle; on the pine wall behind her a framed astrological chart and a "
               "small wooden crucifix."),
         abertura="the open kitchen window",
         carta=("the holographic SOULMATE card from the reference: a tarot-sized card with a rainbow mirror-foil border and "
                "saturated art of a dark-haired woman and a man embracing forehead to forehead under a starry purple sky, a "
                "glowing red heart between them and red roses around, with the word SOULMATE on a cream banner at the bottom"),
         luz=LUZ_INTERNA, sotaque="texano carregado",
         voz="voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos",
         som="cozinha silenciosa, rua tranquila lá fora pela janela aberta"),
    dict(nome="Lorraine Vance", arquivo="LORRAINE_VANCE", genero="mulher", pron="She", pos="her",
         ancora="producao/_ancoras/lorraine_vance_ancora.jpg",
         identidade=("The exact fictional AI character Lorraine Vance: white American woman around fifty-two, closely "
                     "shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, "
                     "defined jaw, fine lines and no makeup."),
         roupa=("Light-wash denim shirt worn open over a fitted black crew-neck T-shirt, dark jeans, large silver hoop "
                "earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar."),
         maos="her freckled fair hand with bare fingers",
         cena=("Her own bright white American kitchen, the same lived-in kitchen as the reference, unchanged. She stands at "
               "the white-framed kitchen window opened wide, with a wide white ledge under it; through the open window a "
               "quiet American residential street with houses, lawns and parked cars is clearly visible. On the light wood "
               "floating shelf beside the window clear quartz crystal points, a lit incense stick with a thin line of smoke "
               "and a small American flag, discreet but visible and in focus; on the white wall a framed zodiac wheel chart "
               "and a small wooden crucifix."),
         abertura="the open kitchen window",
         carta=("the holographic SOULMATE card from the reference: a tarot-sized card with a rainbow mirror-foil border and "
                "saturated art of a brown-haired woman and a man embracing under a rainbow glow, a bright heart and red roses "
                "at the bottom, with the word SOULMATE on a pale banner at the bottom"),
         luz=LUZ_INTERNA, sotaque="de Chicago",
         voz="voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago",
         som="cozinha silenciosa, rua tranquila lá fora pela janela aberta"),
    dict(nome="Walt Hensley", arquivo="WALT_HENSLEY", genero="homem", pron="He", pos="his",
         ancora="producao/_ancoras/walt_hensley_ancora.jpg",
         identidade=("The exact fictional AI character Walt Hensley, explicitly male: white American man around fifty-eight, "
                     "long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, "
                     "sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded "
                     "traditional American tattoos with no lettering, a swallow and a red rose on the left forearm."),
         roupa="Black leather vest over a heather grey crew-neck T-shirt and dark blue jeans.",
         maos="his weathered tattooed hand",
         cena=("His own American front porch with grey weathered wooden siding, the same lived-in porch as the reference, "
               "unchanged. He stands at the porch railing, whose wide flat wooden top rail is the ledge; beyond the railing a "
               "quiet American residential street with houses, lawns and parked cars under the overcast sky. A small "
               "American flag on the porch post, discreet but visible and in focus; on the siding behind him the framed "
               "astrological chart and a small wooden crucifix, and the chrome handlebar of his motorcycle at the edge."),
         abertura="the open porch railing",
         carta=("the holographic SOULMATE card from the reference: a tarot-sized card with a rainbow mirror-foil border and "
                "saturated art of a long-haired woman in red and a bearded tattooed man embracing, surrounded by red roses, "
                "with an iridescent heart at the bottom and the word SOULMATE on a white banner at the bottom"),
         luz=LUZ_EXTERNA, sotaque="do Tennessee",
         voz="voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee",
         som="varanda aberta, rua tranquila, leve vento"),
]

EMOCAO = {
    "T3": "quase sussurrando, séria e confidencial",
    "T4": "firme, em tom de alerta",
    "T5": "baixa e emocionada, como quem revela um segredo",
    "T6": "calma e certa, com pausa antes de \"You were chosen\"",
    "T7": "séria, em tom de aviso",
    "T8": "calma e firme",
    "T9": "de olhos semicerrados, como quem está vendo algo, baixa e intensa",
    "T10": "firme e solene",
    "T11": "emocionada e convicta, marcando \"exactly 11:11\"",
    "T12": "calorosa e emocionada",
    "T13": "suave e segura",
    "T14": "séria e solene",
    "T15": "firme, em ritmo de instrução",
    "T16": "firme e rápida",
    "T17": "animada, depois baixa e séria",
    "T18": "próxima e urgente, olhando direto na lente",
}
MASC = {"séria": "sério", "emocionada": "emocionado", "calorosa": "caloroso", "suave": "suave", "segura": "seguro",
        "baixa": "baixo", "intensa": "intenso", "convicta": "convicto", "animada": "animado", "rápida": "rápido",
        "próxima": "próximo", "certa": "certo", "calma": "calmo"}
ACAO = {
    "T3": "{n} segura o medalhão pendurado na corrente com uma mão e a carta com a outra, e fala baixo para a câmera.",
    "T4": "{n} olha firme para a lente, o medalhão balançando de leve na corrente.",
    "T9": "{n} fecha os olhos por um instante e volta a olhar para a lente, segurando o medalhão e a carta.",
    "T11": "{n} ergue um pouco o medalhão na corrente enquanto fala.",
    "T16": "{n} mostra a carta para a lente e fala com firmeza.",
    "T18": "{n} se inclina um pouco para a lente, segurando o medalhão e a carta.",
}
ACAO_PADRAO = "{n} segura o medalhão pendurado na corrente com uma mão e a carta com a outra, e fala para a câmera com pequenos movimentos naturais."
TITULOS = {"K01": "gancho mudo, sal no prato dourado e as pombas", "K02": "inserto mudo, medalhão colado na lente",
           "K03": "corpo, medalhão e carta na janela"}


def keyframes(a):
    n, P, p = a["nome"], a["pron"], a["pos"]
    ref = (f"Use the first attached image only for {n}'s exact identity, wardrobe, jewelry, SOULMATE card and own "
           f"setting. Use the second attached image only as a composition reference for the camera position, framing "
           f"and action; do not copy its person, clothes, room, pendant, labels or on-screen text.")
    k01 = {
        "prop": (f"{PRATO[0].upper() + PRATO[1:]}, sits empty on the ledge of {a['abertura']} in the lower left corner. "
                 f"{n} holds {TIGELA} with both hands at waist height, starting to tip it toward the plate."),
        "posture": (f"{n} stands right beside the plate, body turned slightly toward the lens, looking straight into the "
                    f"lens with a serious, calm face, mouth closed."),
        "composition": (f"The gold plate is very close to the lens in the lower left corner, about 12 inches from the lens, "
                        f"and takes up about 20 percent of the frame; the bowl in {p} hands sits just behind it; both are "
                        f"closer to the camera than {p} face, nothing else competing with them. {n} fills the right half "
                        f"from the waist up, face in the upper third; {a['abertura']} fills the left half. Nothing else is "
                        f"on the ledge. The background is reduced by framing, never by blur."),
        "camera": "phone on a tripod at chest height, 1x lens, about three feet from the face, straight on, fixed",
        "state": "Start frame: the bowl is just starting to tip; the plate is still empty; no birds in frame yet.",
        "negative": NEG_BASE + ", no birds yet, no salt already on the plate, no pendant in frame, no card in frame",
    }
    k02 = {
        "prop": (f"{n} raises the medallion: {MEDALHAO}, held up by the chain in one raised hand, the medallion hanging "
                 f"motionless right in front of the lens. In the other hand, at waist height, {TIGELA.replace('a small', 'the small')}. "
                 f"On the ledge behind, {PRATO.replace('a shallow', 'the shallow')}, now covered with coarse white salt."),
        "posture": (f"{n} stands beside the ledge, one arm raised holding the chain high, the gold coin medallion hanging "
                    f"between the lens and {p} face; {p} face is visible behind it, looking into the lens."),
        "composition": (f"Extreme close-up: the gold coin medallion hangs about 6 inches from the lens in the center and takes "
                        f"up about 30 percent of the frame, far larger than {p} face, the gold rope chain running up to "
                        f"{a['maos']} at the top edge. The bowl sits in the lower right corner and the plate in the lower "
                        f"left. Nothing else is on the ledge. The background is reduced by framing, never by blur."),
        "camera": "phone on a tripod at chest height, 1x lens, straight on, fixed",
        "state": "Start frame: the medallion is already raised and still in front of the lens.",
        "negative": NEG_BASE + ", no birds in frame, no card in frame, no figurine pendant",
    }
    k03 = {
        "prop": (f"With one hand {n} holds the gold rope chain up at shoulder height so {MEDALHAO.replace('a large', 'the large')}"
                 f", hangs at chest height, held a little forward toward the lens. In the other hand, at chest height and facing "
                 f"the lens, {P.lower()} holds {a['carta']}. On the ledge in the lower left corner, {PRATO}, now empty."),
        "posture": (f"{n} stands right beside the plate, body turned slightly toward the lens, from the waist up, talking "
                    f"to the lens."),
        "composition": (f"The empty gold plate is very close to the lens in the lower left corner, about 12 inches from the "
                        f"lens, and takes up about 20 percent of the frame; the gold coin medallion hangs at chest height "
                        f"held forward, closer to the camera than {p} face. {n} fills the right half from the waist up, face "
                        f"in the upper third; {a['abertura']} fills the left half. Nothing else is on the ledge. The "
                        f"background is reduced by framing, never by blur."),
        "camera": "phone on a tripod at chest height, 1x lens, about three feet from the face, straight on, fixed",
        "state": f"Start frame: {n} looks into the lens, caught mid-sentence, lips naturally parted, animated expression.",
        "negative": NEG_BASE + ", no birds in frame, no bowl in frame, no figurine pendant, no second card",
    }
    out = []
    for cod, d, take in (("K01", k01, "T1"), ("K02", k02, "T2"), ("K03", k03, "T3 a T18")):
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
    parado = "parado" if h else "parada"
    abertura = (f"{art} {n}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
                "{emo}, voz autêntica, como se exigisse ser " + ouvido + ", a seguinte frase: \"{fala}\"")
    diz = (f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
           "sem cortar no final. Lip sync perfeito durante todo o vídeo.")
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        if t == "T1":
            txt = (f"(sem fala no take: gancho mudo, {art} fica em silêncio o clipe inteiro, boca fechada)\n\n"
                   f"o que acontece no vídeo: {n} inclina a tigela e o sal grosso cai no prato dourado {'em cima da grade da varanda' if h else 'do parapeito'}, "
                   f"formando um montinho branco. Perto dos dois segundos e meio, "
                   f"{'um vento passa pela varanda' if h else 'a cortina entra com o vento'} e duas pombas brancas entram voando "
                   f"{'pela grade aberta da varanda' if h else 'pela janela aberta'} e pousam no prato de sal. {n} fica {parado} segurando a tigela, olhando {'sério' if h else 'séria'} para a lente.\n\n"
                   "câmera: fixa, no tripé, sem movimento\n\n"
                   f"som ambiente: {a['som']}, sal caindo no prato, vento e bater de asas, sem música")
        elif t == "T2":
            txt = (f"(sem fala no take: inserto mudo, {art} fica em silêncio)\n\n"
                   f"o que acontece no vídeo: o medalhão dourado de moeda balança de leve na corrente diante da lente, "
                   f"segurado no alto pela mão de {n}, que olha para a lente atrás dele.\n\n"
                   "câmera: fixa, bem perto do medalhão\n\n"
                   f"som ambiente: {a['som']}, leve tilintar da corrente, sem música")
        else:
            txt = (abertura.format(emo=emocao(t, h), fala=FALAS[t]) + "\n\n" + diz + "\n\n"
                   f"o que acontece no vídeo: {ACAO.get(t, ACAO_PADRAO).format(n=n)}\n\n"
                   "câmera: fixa, no tripé, sem movimento\n\n"
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
        "1. Clipes numerados na ordem: V01 a V18.",
        "2. V01 (gancho mudo): usar ~4,5 s, do sal caindo até as pombas pousadas. Tarja fixa em duas linhas no meio do "
        "quadro: \"TELL NO ONE!\" / \"The 11:11 portal just opened.\"",
        "3. V02 (inserto mudo): usar ~1 s do medalhão parado na lente; a primeira palavra do V03 pode entrar por cima.",
        "4. V03 a V18: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. "
        "Isolate Voice / Keep Vocal no áudio. Todos saem do mesmo frame, então a troca de clipe fica no mesmo "
        "enquadramento, como no modelo.",
        "5. \"11:11\" amarelo fixo no canto superior direito do V01 ao V18.",
        "6. Legenda karaokê em caixa alta, branca, palavra atual em amarelo, na altura do prato, do V03 ao V18.",
        "7. Sem Voice Changer: a voz vem do prompt de cada V.",
        "8. Música só a partir do V03, nunca no gancho mudo, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "9. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS.get(t, '(sem fala)')} | {PT[t]} |")
    return L


def anexo(a, k):
    return "\n".join([
        "> ### 📎 ANEXAR: **2 IMAGENS**",
        f"> **1️⃣ ÂNCORA {a['nome'].upper()}** `{a['ancora']}`",
        f"> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/{k['codigo']}_modelo.png`",
        ">", "> ### 🆕 GERAR DO ZERO"])


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# {a['nome']} | Auraly Venda Fortuna | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `/Users/macbookairm2/Downloads/snapinsta-1790635245074.mp4` (124,9 s, avatar IA)", "",
         f"Âncora: `{a['ancora']}`", "",
         "Funil: venda, ramificação de dinheiro. Like + save + envio + `222`, depois foto de perfil e Stories. Rodada de validação.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|",
         f"| T1 | K01 | ÂNCORA {a['nome'].upper()} + FRAME DO MODELO (K01) | GERAR DO ZERO |",
         f"| T2 | K02 | ÂNCORA {a['nome'].upper()} + FRAME DO MODELO (K02) | GERAR DO ZERO |",
         f"| T3 a T18 | K03 | ÂNCORA {a['nome'].upper()} + FRAME DO MODELO (K03) | GERAR DO ZERO |", "",
         "## Trava de identidade e continuidade", "",
         f"- Identidade: {a['identidade']}", f"- Roupa (fixa da conta): {a['roupa']}",
         f"- Cenário-base (fixo da conta): {a['cena']}", f"- Luz: {a['luz']}",
         f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.", "- Sem 2ª pessoa.", "",
         "## Trava do prop herói", "", f"- Prato: {PRATO}.", f"- Tigela: {TIGELA}.", f"- Medalhão: {MEDALHAO}.",
         f"- Carta: {a['carta']}.", "", "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "",
         "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · ÂNCORA {a['nome'].upper()} + FRAME DO MODELO", "",
              anexo(a, k), "", f"Cena: {k['titulo']}.", "", "```json",
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


CHECKLIST = ("Checklist de envio: 33/33 aprovados (N/A: A1, A7, A9 fiéis ao modelo, gancho mudo sem fala; "
             "C3 a C7 sem segunda pessoa, selfie, frase curta repetida, cena atuada ou motion control)")
FICHA = "Ficha: 3/3 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)"


def entrega(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Venda Fortuna", "",
         "Produção `auraly_venda_fortuna` · Ângulo 3 · SALE (ramificação de dinheiro) · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY", "",
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
    print("ok: %d avatares, Flow v%s" % (len(AVATARES), VERSAO))


if __name__ == "__main__":
    main()
