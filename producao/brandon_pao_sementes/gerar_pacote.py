"""Gera o pacote da producao brandon_pao_sementes (avatar IA, growth, validacao, holistic.brandon).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Identidade, roupa e
cenario: a ancora aprovada em 2026-09-29 (avatar fixo por conta). Medidas de cada K: FICHA_FRAMES.md.
Prompt de imagem entregue em JSON (contrato do Flow v17). Gabarito:
fitywell_growth_modelo_intestino/gerar_pacote.py (branch claude/ola-d0d6f0).

Saidas: PROMPTS_BRANDON.md (fonte interna com JSON), FLOW_BRANDON.md (blocos limpos do Flow) e
PROMPTS_PRODUCAO.md (copia do avatar ACTIVE, que e o que o checar_entrega.py le).

Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")

HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 7)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES), FALAS
CURTAS = {t for t in TAKES if "CENA CURTA" in HEADS[t]}
TRANSCRICAO_PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$",
                                 ROTEIRO.split("## Tabela bilíngue")[1].split("## ")[0], re.M))
assert set(TRANSCRICAO_PT) == set(TAKES), TRANSCRICAO_PT

FICCAO = "This is a fictional AI-generated character, no real person is depicted."


def frame_modelo(cod):
    return f"input/frames_modelo/{cod}_modelo.png"


LUZ = ("Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no "
       "harsh shadows. The red neon glows on the wall but does not tint her skin or the food.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
LUZ_PAO = ("Neutral overcast daylight from a large window out of frame, soft even light on the bread with no harsh "
           "shadows. No neon glow on the bread.")
REALISMO_PAO = ("Real food texture with crumbs and uneven seeds, iPhone footage look, flat natural light, low contrast, "
                "slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, "
                "no AI polish.")
NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the kettle, "
            "blender, bowls or pan, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, "
            "no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, "
            "no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no second person, "
            "no kitchen cabinets, no marble counter, no silver cross")
NEG_SEM_ROSTO = ", no face in frame"

A = dict(
    nome="Brandon", arquivo="BRANDON", ancora="producao/_ancoras/holistic_brandon_ancora.jpg",
    identidade=("The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, "
                "athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown "
                "eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling "
                "over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo "
                "sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral "
                "tattoo below her left collarbone."),
    roupa=("Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain "
           "with a small gold cross pendant and small stud earrings."),
    cena=("Her own garage gym: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign "
          "reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading "
          "STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, "
          "discreet but clearly visible and in focus. A matte black table stands in front of her."),
    cena_cima=("Seen from above her matte black table; at the top edge of the frame, beyond the table, a strip of "
               "the white-painted concrete block wall with the small American flag pinned on it, discreet but "
               "clearly visible and in focus."),
    cena_pao=("Her own garage gym behind the bread, fully in focus: the white-painted concrete block wall, the "
              "whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. and the small "
              "American flag pinned above it, discreet but clearly visible and in focus."),
    voz="voz feminina clara e firme de uma mulher de uns trinta anos",
    sotaque="de uma mulher negra americana",
    som="box de treino em casa, tranquilo",
)

TIGELA_SECA = ("a large clear glass mixing bowl with a thick layer of dry black chia seeds covering its bottom")
PAO = ("a freshly baked seed loaf with a thick crust packed with seeds and green pumpkin seeds on top, its crumb "
       "dense and full of seeds, on a worn rectangular wooden cutting board")

EMOCAO = {
    "T1": "entonação animada e curiosa, como quem conta um segredo de cozinha",
    "T2": "entonação calma e didática, no ritmo de quem lista a receita",
    "T3": "entonação calma e didática", "T4": "entonação calma e didática",
    "T5": "entonação animada e satisfeita",
    "T6": "entonação animada e calorosa, sorrindo no yes",
}
ACOES = {
    "T1": ("{n} fala olhando para a câmera e inclina a chaleira elétrica branca; a água morna cai na tigela de vidro "
           "e cobre a chia, que vai afundando enquanto a tigela enche."),
    "T2": ("De cima, as mãos de {n} viram na chia hidratada, uma de cada vez, a tigelinha de linhaça moída, a de "
           "farinha de amêndoa, três ovos inteiros de uma tigelinha branca, uma pitada de sal entre os dedos e o "
           "fermento de um potinho de cerâmica; no fim, o mixer de mão entra no quadro. O rosto dela fica fora de "
           "quadro e a voz dela narra."),
    "T3": ("O mixer de mão bate a mistura dentro da tigela até virar uma massa bege pintadinha de chia. O rosto dela "
           "fica fora de quadro e a voz dela narra."),
    "T4": ("Os dedos de {n} salpicam sementes de abóbora verdes sobre a massa na forma de pão. O rosto dela fica "
           "fora de quadro e a voz dela narra."),
    "T5": ("O pão de sementes assado descansa na tábua com duas fatias cortadas na frente, a câmera gira devagar em "
           "volta dele. Ninguém em quadro; a voz dela narra."),
    "T6": ("{n} segura a fatia de pão virada para a câmera e fala direto com quem assiste, sorrindo no yes, com "
           "pequenos movimentos naturais."),
}
CAMERA = {"T5": "leve movimento em arco em volta do pão, bem perto", "T2": "fixa, de cima, bem perto da tigela",
          "T3": "fixa, de cima, bem perto da tigela", "T4": "fixa, de cima, bem perto da forma"}
SOM_EXTRA = {"T1": ", água caindo na tigela de vidro", "T2": ", ingredientes caindo na tigela",
             "T3": ", zumbido do mixer", "T4": ", sementes caindo na massa", "T5": ""}
MOMENTO = {"T1": "0,0 a 4,6 s", "T2": "4,6 a 12,3 s", "T3": "12,3 a 13,6 s", "T4": "13,6 a 16,6 s",
           "T5": "16,6 a 20,3 s", "T6": "20,3 a 27,7 s"}
TITULOS = {"T1": "gancho, água morna na chia, tigela colada na lente", "T2": "de cima, linhaça caindo na chia hidratada",
           "T3": "de cima, mixer batendo a massa", "T4": "de cima, sementes de abóbora na forma",
           "T5": "pão pronto na tábua, sem pessoa", "T6": "CTA, fatia na mão, pão colado na lente"}


def keyframes(a):
    n = a["nome"]
    boca = "caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens"
    ref = (f"Use the first attached image only for {n}'s exact identity, wardrobe and own garage gym. Use the second "
           "attached image only as a composition reference for the camera position, framing and the action; do not "
           "copy its person, red glasses, green shirt, kitchen cabinets, marble counter, under-cabinet lights or the white "
           "caption text.")
    ref_sem_pessoa = ("Use the first attached image only for the garage gym setting and the matte black table. Use "
                      "the second attached image only as a composition reference for the camera position, framing "
                      "and the food; do not copy its kitchen, under-cabinet lights, blurred background or the white caption text.")
    fechado = "Nothing else is on the table. The background is reduced by framing, never by blur."
    cam_frente = "phone resting on the table at the height of the bowl rim, standard 1x lens, straight-on, fixed"
    cam_cima = "phone held above the table, top-down, standard 1x lens pointing down at a steep angle, fixed"
    maos = f"Only her hands and forearms enter from the top of the frame, the floral tattoo sleeve visible on her right forearm."
    ks = {
        "T1": dict(
            prop=(f"{TIGELA_SECA[0].upper()}{TIGELA_SECA[1:]}, standing on her matte black table very close to the lens. "
                  "A small clear glass bowl of golden-brown ground flaxseed sits at the right edge of the frame, partly "
                  "cut by the edge. In her right hand, on the left side of the frame, she holds a plain white electric "
                  "kettle with no label, raised beside the bowl."),
            posture=(f"{n} stands behind her matte black table facing the camera, seen from the waist up, the kettle in "
                     "her right hand at the left side of the frame, her left hand resting on the table near the small "
                     "flaxseed bowl."),
            composition=("Straight-on shot: the phone lens is about 30 centimeters from the chia bowl, which fills the "
                         "lower 35 percent of the frame and about three quarters of its width, far closer to the camera "
                         "than her face and larger than her head, nothing else competing with it. Her face is in the "
                         "upper third of the frame. " + fechado),
            camera=cam_frente,
            state=(f"Start frame: the kettle is tilted just before the first pour and the chia is still dry. {n} is {boca}."),
            negative=NEG_BASE + ", no water in the bowl yet"),
        "T2": dict(
            scene=a["cena_cima"],
            prop=("The large clear glass mixing bowl full of soaked chia seeds, a dark glossy gel dotted with thousands "
                  "of tiny black and grey seeds. Her right hand enters from the top left holding a small clear glass "
                  "bowl of golden-brown ground flaxseed tipped over the chia; her left hand rests on the matte black "
                  "table at the top right."),
            posture=maos,
            composition=("Top-down close-up: the phone lens is about 20 centimeters above the bowl, and the bowl fills "
                         "the whole frame edge to edge, its rim cut by the left and right edges. " + fechado),
            camera=cam_cima,
            state="Start frame: the first golden-brown ground flaxseed is just sliding out of the small bowl onto the chia gel.",
            negative=NEG_BASE + NEG_SEM_ROSTO),
        "T3": dict(
            scene=a["cena_cima"],
            prop=("A black and stainless steel immersion hand blender with no label, its steel shaft plunged into the "
                  "large clear glass mixing bowl, blending a thick beige batter speckled all over with tiny black chia "
                  "seeds, a smooth swirl around the blade."),
            posture=("Only her right hand holds the blender handle at the top of the frame, and the fingertips of her "
                     "left hand steady the bowl rim at the right edge."),
            composition=("Top-down close-up: the phone lens is about 20 centimeters above the bowl; the bowl fills the "
                         "lower two thirds of the frame edge to edge and the black blender body comes down from the top "
                         "edge, large in frame. " + fechado),
            camera=cam_cima,
            state="Start frame: the blender is running in the speckled batter, the swirl just forming.",
            negative=NEG_BASE + NEG_SEM_ROSTO),
        "T4": dict(
            scene=a["cena_cima"],
            prop=("A rectangular metal loaf pan lined with crinkled white parchment paper, filled with smooth beige "
                  "batter speckled with tiny black chia seeds, standing on her matte black table; her fingers hold a "
                  "pinch of green pumpkin seeds just above it."),
            posture="Only her right hand enters from the top of the frame, the floral tattoo sleeve visible on her forearm.",
            composition=("Top-down close-up: the phone lens is about 25 centimeters above the pan, and the pan fills the "
                         "lower two thirds of the frame, almost touching the left and right edges. " + fechado),
            camera=cam_cima,
            state="Start frame: the first green pumpkin seeds are falling from her fingers onto the batter.",
            negative=NEG_BASE + NEG_SEM_ROSTO),
        "T5": dict(
            reference_use=ref_sem_pessoa,
            scene=a["cena_pao"],
            prop=(f"{PAO[0].upper()}{PAO[1:]} on her matte black table, with two thick slices cut and leaning in front "
                  "of the loaf."),
            posture="No person in frame.",
            composition=("Low three-quarter close-up: the phone lens is about 25 centimeters from the loaf, and the loaf, "
                         "the slices and the board fill the lower two thirds of the frame, nearly edge to edge. " + fechado),
            camera="phone resting on the table at the height of the cutting board, standard 1x lens, three-quarter angle, fixed",
            state="Start frame: the loaf rests on the board, still, the slices leaning in front of it.",
            negative=NEG_BASE + NEG_SEM_ROSTO + ", no person in frame, no hands"),
        "T6": dict(
            prop=(f"She holds up one thick slice of seed bread in her right hand at chest height, turned toward the "
                  f"camera. In front of her, on her matte black table very close to the lens, lies {PAO}, with one more "
                  "cut slice beside the loaf."),
            posture=(f"{n} stands behind her matte black table leaning slightly toward the camera, seen from the waist "
                     "up, the slice in her right hand at the left side of the frame."),
            composition=("Straight-on shot: the phone lens is about 30 centimeters from the loaf, and the loaf and the "
                         "board fill the lower 35 percent of the frame and most of its width, closer to the camera than "
                         "her face, nothing else competing with them. Her face is in the upper third of the frame, a "
                         "little closer than in the opening shot. " + fechado),
            camera="phone resting on the table at the height of the cutting board, standard 1x lens, straight-on, fixed",
            state=f"Start frame: {n} is {boca}.",
            negative=NEG_BASE),
    }
    out = []
    for i, t in enumerate(TAKES, 1):
        d = ks[t]
        cod = f"K{i:02d}"
        j = {
            "shot_id": f"{cod}_{t.lower()}_{a['arquivo'].lower()}",
            "fiction_note": FICCAO,
            "reference_use": d.get("reference_use", ref),
            "identity_main": a["identidade"] if t != "T5" else "No person appears in this image.",
            "wardrobe": a["roupa"] if t != "T5" else "Not visible.",
            "scene": d.get("scene", a["cena"]),
            "prop": d["prop"],
            "posture": d["posture"],
            "composition": d["composition"],
            "camera": d["camera"],
            "lighting": LUZ if t != "T5" else LUZ_PAO,
            "state": d["state"],
            "realism": REALISMO if t != "T5" else REALISMO_PAO,
            "aspect_ratio": "9:16 vertical",
            "negative": d["negative"],
        }
        out.append(dict(codigo=cod, take=t, titulo=TITULOS[t], j=j))
    return out


def videos(a):
    n = a["nome"]
    vs = []
    for i, t in enumerate(TAKES, 1):
        acao = ACOES[t].format(n=n)
        if t in CURTAS:
            acao += " Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim."
        txt = (f"a avatar {n}, mulher, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
               f"{EMOCAO[t]}, voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"{FALAS[t]}\"\n\n"
               "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por "
               "inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
               f"o que acontece no vídeo: {acao}\n\n"
               f"câmera: {CAMERA.get(t, 'fixa')}\n\n"
               f"som ambiente: {a['som']}{SOM_EXTRA.get(t, '')}, sem música")
        vs.append((f"V{i:02d}", t, f"K{i:02d}", txt))
    return vs


def texto_flow(j):
    """Prompt de imagem de EXECUCAO, em JSON (contrato do Flow v17): sem shot_id, com o formato na frente."""
    ordem = ["fiction_note", "reference_use", "identity_main", "wardrobe", "scene", "prop", "posture",
             "composition", "camera", "lighting", "state", "realism", "aspect_ratio", "negative"]
    assert set(ordem) == set(j) - {"shot_id"}, set(j) ^ set(ordem)
    d = {"format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."}
    d.update({k: j[k] for k in ordem})
    return json.dumps(d, ensure_ascii=False, indent=2)


def anexo(a, k):
    return "\n".join([
        "> ### 📎 ANEXAR: **2 IMAGENS**",
        f"> **1️⃣ ÂNCORA HOLISTIC BRANDON** `{a['ancora']}`",
        f"> **2️⃣ FRAME DO MODELO, só composição** `{frame_modelo(k['codigo'])}`",
        ">", "> ### 🆕 GERAR DO ZERO"])


def capcut():
    return [
        "1. Clipes numerados na ordem: V01 a V06.",
        "2. Cortar cada clipe no tempo da cena do modelo: " + "; ".join(f"V{t[1:].zfill(2)} {MOMENTO[t]}" for t in TAKES) + ".",
        "3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.",
        "4. L-cut no primeiro corte: o \"then add\" do V01 continua por cima dos primeiros 0,6 s do V02, como no modelo.",
        "5. Cenas curtas (V03, V04, V05): a fala vem no começo do clipe; cortar logo depois da última palavra, no tempo da cena.",
        "6. Legenda palavra a palavra, branca, no meio do quadro, com palavras-chave em serifa itálica, igual ao modelo.",
        "7. Sem Voice Changer: a voz vem do prompt de cada V.",
        "8. Música só depois do gancho (a partir do V02), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "9. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {TRANSCRICAO_PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = ["# holistic.brandon | FityWell Growth Pão de sementes | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (27,7 s, avatar IA)", "",
         f"Âncora: `{a['ancora']}`", "",
         "Funil: growth, comentário `yes` + follow. Rodada de validação, gancho fiel ao modelo. Sem produto em quadro.", "",
         "## Índice de geração", "",
         "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    for k in ks:
        L.append(f"| {k['take']} | {k['codigo']} | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO ({k['codigo']}) | GERAR DO ZERO |")
    L += ["", "Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro, "
          "então não existe `EDITAR do K__` aqui. O frame do modelo de cada K entra só como composição.", "",
          "## Trava de identidade e continuidade", "",
          f"- Identidade: {a['identidade']}",
          f"- Roupa (fixa da conta): {a['roupa']}",
          f"- Cenário-base (fixo da conta): {a['cena']}",
          f"- Luz: {LUZ}",
          f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.",
          "- Sem 2ª pessoa.", "",
          "## Trava do prop herói", "",
          f"- Gancho: {TIGELA_SECA}, e a chaleira elétrica branca lisa, sem rótulo.",
          "- Receita: linhaça moída, farinha de amêndoa, três ovos, sal, fermento, mixer de mão preto e inox sem rótulo, "
          "forma de pão de metal com papel manteiga, sementes de abóbora verdes.",
          f"- Resultado: {PAO}. Nenhuma embalagem com texto ou marca.", "",
          "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "",
          "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO", "",
              anexo(a, k), "", f"Cena: {k['titulo']}.", "", "```json",
              json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["## Bloco global de vídeo", "", "```text",
          f"a avatar {a['nome']}, mulher, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
          "[emoção da fala], voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"[FALA EXATA DO ROTEIRO]\"", "",
          "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.", "",
          "o que acontece no vídeo: [ação enxuta]", "", "câmera: [fixa]", "", f"som ambiente: {a['som']}, sem música",
          "```", "", "# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Mapa de âncoras", "", "| Keyframe | Referências a anexar | Modelo |", "|---|---|---|"]
    for k in ks:
        L.append(f"| {k['codigo']} | ÂNCORA HOLISTIC BRANDON + `{frame_modelo(k['codigo'])}` (só composição) | Nano Banana 2, 9:16 |")
    L += ["", "## Montagem no CapCut", ""] + capcut() + [
          "", "## Gates de qualidade", "",
          "1. Fala de cada V igual ao ROTEIRO, palavra por palavra.",
          "2. Um take por cena do modelo; cenas curtas marcadas; nenhum take acima de 29 palavras.",
          "3. Bandeira dos EUA no campo scene de todo K.",
          "4. Zero travessão.", "5. Keyword `yes` no T6.",
          "6. Produto fora de quadro: chaleira, mixer, tigelas e forma sem marca.",
          "7. Negative sem termo sensível.",
          "8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "9. Gancho fiel no conteúdo: água morna da chaleira caindo na chia seca, tigela colada na lente, falado desde o segundo 0.",
          "10. Um K = um V; o enchimento da tigela no T1 é uma imagem só, do estado inicial (chia seca).", ""]
    flow = ["# Blocos limpos para o Google Flow | holistic.brandon", "", "Fonte interna: `PROMPTS_BRANDON.md`", "",
            "## BLOCO DE IMAGEM", "", "```text"]
    for k in ks:
        flow += [k["codigo"], texto_flow(k["j"]), ""]
    flow += ["```", "", "## BLOCO DE VÍDEO", "", "```text"]
    for cod, _, _, txt in vs:
        flow += [cod, txt, ""]
    flow += ["```", "", "## Tabela de leitura humana", "", "| Código | Take | Anexar |", "|---|---|---|"]
    for k in ks:
        flow.append(f"| {k['codigo']} / V{k['codigo'][1:]} | {k['take']}, {k['titulo']} | ÂNCORA + `{frame_modelo(k['codigo'])}` |")
    flow += ["", "## Transcrição final por take", ""] + transcricao()
    return "\n".join(L) + "\n", "\n".join(flow) + "\n"


AVATARES = [A]


def main():
    p, f = pacote(A)
    (AQUI / "PROMPTS_BRANDON.md").write_text(p, encoding="utf-8")
    (AQUI / "FLOW_BRANDON.md").write_text(f, encoding="utf-8")
    (AQUI / "PROMPTS_PRODUCAO.md").write_text(p, encoding="utf-8")
    print("ok: pacote da Brandon; PROMPTS_PRODUCAO.md = holistic.brandon")


if __name__ == "__main__":
    main()
