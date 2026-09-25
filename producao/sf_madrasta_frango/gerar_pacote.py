"""Gera PROMPTS_PRODUCAO.md (JSON interno, lido pelo linter) e FLOW_PACOTE.md (blocos limpos do
Flow) a partir de UMA fonte, para os dois nunca divergirem. Short form sf_madrasta_frango.

Uso: python3 producao/sf_madrasta_frango/gerar_pacote.py
"""
import json
from pathlib import Path

AQUI = Path(__file__).parent

# ------------------------------------------------------------------ blocos repetidos
FICCAO = "This is a fictional AI-generated scene with fictional characters, no real person is depicted."
CENA = ("A bright modern American family kitchen in daytime: white shaker cabinets, a white marble "
        "backsplash, a large kitchen island with a light grey quartz countertop, an open doorway to a "
        "hallway in the background, a window over the sink showing a green backyard under an overcast "
        "sky with visible cloud texture, and a small American flag magnet on the stainless steel "
        "refrigerator, discreet but clearly visible and in sharp focus.")
LUZ = ("Neutral overcast daylight from the window, the outside clearly visible through the window, soft "
       "even light on every face with no harsh shadows, no warm orange cast and no yellow tint.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven "
            "natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, "
            "boring everyday reality, background fully in focus, everything in sharp focus, no blur, no "
            "bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden "
            "glow, no golden hour light, no sunset.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, "
       "no blur, no bokeh, no warm orange color cast, no yellow tint, no golden hour light, no AI polish, "
       "no beauty smoothing, no cinematic lighting")
PRATO = ("a white plate piled high with golden fried chicken pieces and, right next to it, a small grey "
         "bowl of plain cold white rice")
COMPOSICAO_REF = ("The last attached image is a composition reference only: copy its camera position and "
                  "where each person stands, never its faces, bodies, clothes or room.")

# ------------------------------------------------------------------ elenco
P = {
    "P1": ("the stepmother: a white American woman around forty, slim, platinum blonde hair pulled back "
           "into a low neat bun, pale skin with light freckles, light blue eyes, a thin straight nose and "
           "thin lips, fine lines around the eyes, wearing a cream silk long-sleeve button-up blouse "
           "tucked into high-waisted black tailored trousers and small gold stud earrings"),
    "P2": ("the father: a Black American man around forty-two, medium-dark brown skin, athletic build, "
           "very short black hair with a sharp hairline, a short neat black beard and a strong jaw, "
           "wearing a navy blue long-sleeve button-up dress shirt with white buttons, dark navy trousers "
           "and a silver watch on his left wrist"),
    "P3": ("Emily: a Black American girl around six, dark brown skin, a round face, big dark brown eyes, "
           "her hair in two puffy pigtails tied with pink hair ties, wearing a pink short-sleeve dress "
           "with ruffled cap sleeves"),
    "P4": ("the son: a Black American boy around eight, medium brown skin, close-cropped hair, wearing a "
           "light blue long-sleeve oxford button-down shirt tucked into khaki chinos with a brown leather "
           "belt, the top edge of a blue iPhone showing from his right front pocket"),
}
NOME = {"P1": "MADRASTA", "P2": "PAI", "P3": "EMILY", "P4": "FILHO"}


def cap(t):
    return t[0].upper() + t[1:]


# Quem aparece so em parte recebe so a descricao da parte (senao o modelo desenha a pessoa inteira)
PARTE = {
    "P2_mao": ("the father's hand entering the frame, with dark brown skin, the cuff of a navy blue dress "
               "shirt with white buttons and a silver watch on the left wrist"),
    "P1_bracos": "the stepmother's crossed arms in a cream silk blouse, pale freckled skin, her face out of frame",
    "P2_ombro": "the father's shoulder and back in a navy blue dress shirt",
    "P4_quadril": ("the son's right hip and right hand, with medium brown skin, a light blue oxford shirt "
                   "tucked into khaki chinos and a brown leather belt"),
    "P2_braco": "the father's outstretched arm in a navy blue sleeve, with his dark brown hand,",
}
CENA_INSERTO = ("In the background of this American family kitchen, the light grey quartz countertop of the "
                "island and the stainless steel refrigerator with a small American flag magnet, discreet but "
                "clearly visible and in sharp focus.")

VOZ = {
    "P1": "voz feminina de uns quarenta anos, média-aguda, fria e cortante, sotaque americano padrão",
    "P2": "voz masculina grave de barítono, uns quarenta anos, sotaque americano de homem negro",
    "P3": "voz de menina de seis anos, fina e aguda, sotaque americano",
    "P4": "voz de menino de oito anos, clara e ainda infantil, sotaque americano",
}
QUEM = {
    "P1": "a MADRASTA (mulher branca loira de coque baixo e blusa creme)",
    "P2": "o PAI (homem negro de barba curta e camisa azul-marinho)",
    "P3": "EMILY (menina de marias-chiquinhas e vestido rosa)",
    "P4": "o FILHO (menino de camisa azul-clara e calça cáqui)",
}

# ------------------------------------------------------------------ character sheets
def ref(pid, extra=""):
    return {
        "shot_id": "REF-%s_character_sheet_%s" % (pid, NOME[pid].lower()),
        "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
        "sheet_layout": ("CHARACTER SHEET of ONE person on a plain light grey wall background: three "
                         "full-body views side by side (front, three-quarter and profile) in the lower two "
                         "thirds, and a large front close-up of the face across the top third. The same "
                         "person, the same clothes and the same hair in every view."),
        "identity_main": P[pid][0].upper() + P[pid][1:] + "." + (" " + extra if extra else ""),
        "expression": "Neutral relaxed expression, mouth closed, looking straight ahead.",
        "lighting": ("Flat neutral daylight, soft and even on the face and body, no harsh shadows, "
                     "no warm orange cast and no yellow tint."),
        "realism": REALISMO,
        "aspect_ratio": "9:16 vertical",
        "negative": NEG + ", no labels, no numbers, no arrows, no second person",
    }

REFS = [
    ("REF-P1", "P1", ref("P1")),
    ("REF-P2", "P2", ref("P2")),
    ("REF-P3", "P3", ref("P3", "Her face is clean, with no marks.")),
    ("REF-P4", "P4", ref("P4")),
]

# ------------------------------------------------------------------ keyframes
def uso(ids):
    nomes = {"P1": "the stepmother", "P2": "the father", "P3": "Emily", "P4": "the son"}
    partes = ["%s is the person in the %s character sheet" % (nomes[i], ["first", "second", "third"][n])
              for n, i in enumerate(ids)]
    return ("Use the attached character sheets ONLY for faces, hair, bodies and clothes: "
            + "; ".join(partes) + ". " + COMPOSICAO_REF)

K = []

K.append(("K01", "T1", "TRANSGRESSÃO + FLAGRANTE", ["P3", "P1", "P2"], {
    "shot_id": "K01_transgressao_flagrante",
    "reference_use": uso(["P3", "P1", "P2"]),
    "fiction_note": FICCAO,
    "cast": ("Three people. " + P["P3"] + ", standing at the near side of the kitchen island. "
             + P["P1"][0].upper() + P["P1"][1:] + ", standing right beside her on the right. "
             + P["P2"][0].upper() + P["P2"][1:] + ", small but clearly recognizable, stepping through the "
             "open doorway in the background."),
    "prop": ("On the island, " + PRATO + ". The plate and the bowl are very close to the lens in the lower "
             "foreground, large in frame, closer to the camera than any face."),
    "scene": CENA,
    "posture": ("Emily stretches one small hand toward the fried chicken. The stepmother turns toward her "
                "with a furious face, leaning in, caught mid-sentence, lips naturally parted. The father has just stepped into the doorway "
                "behind them, mid-step, staring."),
    "composition": ("The plate and bowl fill the lower foreground. Emily's head, shoulders and reaching hand "
                    "sit in the middle of the frame, the stepmother on the right from the waist up, the "
                    "father small in the doorway in the background. Every face in sharp focus."),
    "camera": "adult eye level from across the island, slightly high, like someone in the kitchen filming with a phone",
    "state": "Start frame: the hand is reaching and nobody has been touched yet.",
    "lighting": LUZ,
    "realism": REALISMO,
    "aspect_ratio": "9:16 vertical",
    "negative": NEG,
}))

K.append(("K02", "T2", "REVELAÇÃO", ["P2", "P3"], {
    "shot_id": "K02_revelacao",
    "reference_use": uso(["P2", "P3"]),
    "fiction_note": FICCAO,
    "cast": ("Two people. " + cap(P["P2"]) + ", crouching low at the corner of the kitchen island. "
             + P["P3"][0].upper() + P["P3"][1:] + ", held tight against his chest in both of his arms."),
    "prop": ("The corner of the island countertop enters the lower left foreground with " + PRATO
             + ", very close to the lens, large in frame, closer to the camera than the faces."),
    "scene": CENA,
    "posture": ("Emily's face is turned toward the camera, tears on her cheeks, three thin red marks across "
                "her left cheek, her mouth open mid-sob. The father's face is right next to hers, turned "
                "toward the camera, jaw clenched, lips naturally parted as if about to speak."),
    "composition": ("A tight two-shot: both faces fill the upper half of the frame side by side, the plate "
                    "and bowl in the lower left foreground. The top of the father's head is cropped by the "
                    "top edge. No other person in frame."),
    "camera": "adult chest level, close, straight-on, like someone in the kitchen filming with a phone",
    "state": "Start frame: she is crying in his arms and he is about to speak.",
    "lighting": LUZ,
    "realism": REALISMO,
    "aspect_ratio": "9:16 vertical",
    "negative": NEG,
}))

K.append(("K03", "T3", "INSERTO DO PRATO", ["P2", "P1"], {
    "shot_id": "K03_inserto_prato",
    "reference_use": uso(["P2", "P1"]),
    "fiction_note": FICCAO,
    "cast": ("Only parts of two people: " + PARTE["P2_mao"] + "; and behind the plate, "
             + PARTE["P1_bracos"] + "."),
    "prop": ("On the island, " + PRATO + ". The plate and the bowl fill the lower two thirds of the frame, "
             "very close to the lens, large in frame, the hero of the image."),
    "scene": CENA_INSERTO,
    "posture": "The father's hand enters from the left edge, index finger extended, about to point at the chicken.",
    "composition": ("The plate and the bowl dominate the lower two thirds. The pointing hand enters from the "
                    "left. The stepmother's crossed arms and blouse sit at the upper right edge, cut by the "
                    "frame. The refrigerator with the small flag magnet is visible behind, in sharp focus."),
    "camera": "close, slightly high, looking down at the countertop",
    "state": "Start frame: the finger is just above the plate and has not pointed yet.",
    "lighting": LUZ,
    "realism": REALISMO,
    "aspect_ratio": "9:16 vertical",
    "negative": NEG,
}))

K.append(("K04", "T4", "EXPLOSÃO", ["P1", "P2"], {
    "shot_id": "K04_explosao",
    "reference_use": uso(["P1", "P2"]),
    "fiction_note": FICCAO,
    "cast": ("Two people. " + cap(P["P1"]) + ", standing on the far side of the kitchen island. In the "
             "foreground, " + PARTE["P2_ombro"] + ", cut by the left edge of the frame."),
    "prop": ("On the island, " + PRATO + ", very close to the lens in the lower foreground, closer to the "
             "camera than her face."),
    "scene": CENA,
    "posture": ("The stepmother stands with her arms crossed tightly over her blouse, chin down, lips "
                "pressed together, glaring across the island, furious and about to explode."),
    "composition": ("The stepmother from the waist up in the center, the father's shoulder cut by the left "
                    "edge, the plate and bowl in the lower foreground. Her face in sharp focus."),
    "camera": "adult eye level from across the island, like someone in the kitchen filming with a phone",
    "state": "Start frame: her arms are still crossed and she has not moved yet.",
    "lighting": LUZ,
    "realism": REALISMO,
    "aspect_ratio": "9:16 vertical",
    "negative": NEG,
}))

K.append(("K05", "T5", "VIRADA + PROVA", ["P4", "P1", "P2"], {
    "shot_id": "K05_virada_prova",
    "reference_use": uso(["P4", "P1", "P2"]),
    "fiction_note": FICCAO,
    "cast": ("Three people. " + cap(P["P4"]) + ", standing at the near side of the kitchen island. Across the "
             "island, " + P["P1"] + ", and beside her " + P["P2"] + "."),
    "prop": ("On the island next to the boy, " + PRATO + ", in the lower foreground close to the lens."),
    "scene": CENA,
    "posture": ("The boy stands three-quarter to the camera, his face clearly visible, looking across the "
                "island at his mother, lips naturally parted, about to speak. The stepmother stares at him "
                "in shock. The father stands beside her, tense, his face clearly visible."),
    "composition": ("The boy from the waist up on the left side of the frame, closest to the camera. The "
                    "stepmother and the father across the island on the right, both faces in sharp focus. "
                    "The plate at the bottom of the frame."),
    "camera": "adult chest level, slightly behind the boy's shoulder, like someone in the kitchen filming with a phone",
    "state": "Start frame: nobody has moved yet and the iPhone is still in his pocket.",
    "lighting": LUZ,
    "realism": REALISMO,
    "aspect_ratio": "9:16 vertical",
    "negative": NEG,
}))

K.append(("K06", "T6", "INSERTO DO CELULAR", ["P4"], {
    "shot_id": "K06_inserto_celular",
    "reference_use": uso(["P4"]),
    "fiction_note": FICCAO,
    "cast": ("Only one person, in part: " + PARTE["P4_quadril"] + "."),
    "prop": ("His right hand is halfway into the right front pocket of his khaki chinos, fingers closed on a "
             "blue iPhone whose top edge is already out. The hand and the iPhone are very close to the lens, "
             "large in frame, the hero of the image."),
    "scene": CENA_INSERTO,
    "posture": "The light blue shirt is tucked in above the brown leather belt. The hand is starting to pull.",
    "composition": ("A tight shot of the hip and hand filling the frame. Behind, in sharp focus, the island "
                    "countertop and the stainless refrigerator with the small American flag magnet."),
    "camera": "close, at hip height, straight-on",
    "state": "Start frame: the iPhone is half out of the pocket.",
    "lighting": LUZ,
    "realism": REALISMO,
    "aspect_ratio": "9:16 vertical",
    "negative": NEG,
}))

K.append(("K07", "T7", "CORTE", ["P1"], {
    "shot_id": "K07_corte",
    # 2026-09-23: travou na censura. Saiu o braco do pai (braco de homem + rosto de mulher em choque
    # le como agressao) e o frame de composicao agora tem o rosto coberto (close de rosto real).
    "reference_use": ("Use the attached character sheet ONLY for her face, hair, body and clothes. The last "
                      "attached image is a composition reference only, with the face covered by a grey box: "
                      "copy its camera position and framing, never its body, clothes or room."),
    "fiction_note": FICCAO,
    "cast": "One person. " + cap(P["P1"]) + ". Nobody else is in the frame.",
    "prop": "No prop. Her frozen face is the hero of the image.",
    "scene": CENA_INSERTO,
    "posture": ("She is caught completely off guard: eyes wide open, eyebrows raised, lips slightly "
                "parted, standing perfectly still."),
    "composition": ("Her face and shoulders fill the frame, the top of her head cropped by the top edge. "
                    "Behind her, the white cabinets and the refrigerator with the small American flag "
                    "magnet, in sharp focus."),
    "camera": "eye level, close, straight-on",
    "state": "Start frame: she has just frozen.",
    "lighting": LUZ,
    "realism": REALISMO,
    "aspect_ratio": "9:16 vertical",
    "negative": NEG,
}))

# ------------------------------------------------------------------ videos
LIPSYNC = ("cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última "
           "palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de "
           "quem está falando.")
CAM_CENA = "leve handheld, como alguém na cozinha filmando com o celular, sem trocar de plano"

def dialogo(falas, calado):
    linhas = ["falas no take, em inglês, na ordem:"]
    for n, (pid, emocao, fala) in enumerate(falas, 1):
        linhas.append('%d. %s, %s, fala %s: "%s"' % (n, QUEM[pid], VOZ[pid], emocao, fala))
    linhas.append(calado)
    return "\n".join(linhas)

V = [
    ("V01", "T1", "K01", dialogo([
        ("P1", "com raiva explosiva, gritando", "Don't touch my son's food!"),
        ("P2", "em choque e com fúria, alto", "What did you do to my daughter?"),
    ], "EMILY não diz nenhuma palavra, só chora."),
     "Emily estica a mão para o frango. A madrasta acerta o rosto dela com a mão aberta e grita a fala "
     "dela. Emily recua chorando, com a mão na bochecha. O pai, na porta ao fundo, vê tudo e avança rápido "
     "até a bancada enquanto fala.",
     CAM_CENA, "cozinha silenciosa de casa, o choro da menina, passos rápidos, sem música"),
    ("V02", "T2", "K02", dialogo([
        ("P3", "chorando, com a voz tremendo", "Daddy, I was just hungry."),
        ("P2", "com indignação contida, firme", "Why does my daughter only get cold rice?"),
        ("P3", "baixinho, entre soluços", "She won't let me eat when you're gone."),
    ], "Ninguém mais fala."),
     "O pai abraça Emily com força. Ela fala com o rosto colado no peito dele, as lágrimas escorrendo. Ele "
     "olha para o lado com raiva enquanto fala e depois volta a olhar para ela.",
     CAM_CENA, "cozinha silenciosa de casa, os soluços da menina, sem música"),
    ("V03", "T3", "K03", '(sem fala no take: a fala do PAI no V02, "Why does my daughter only get cold rice?", '
     "entra por cima na edição)",
     "O dedo indicador do pai aponta para o frango frito e depois se move e aponta para a tigela de arroz "
     "frio. Os braços cruzados da madrasta continuam parados ao fundo.",
     "fixa", "cozinha silenciosa de casa, sem música"),
    ("V04", "T4", "K04", "(sem fala no take: a madrasta grita de raiva, sem dizer nenhuma palavra)",
     "A madrasta encara, descruza os braços de repente, solta um grito de raiva e contorna a bancada "
     "partindo para cima do pai. O pai a segura pelos braços.",
     "leve handheld de quem está na cozinha assistindo, acompanha o movimento",
     "grito de raiva sem palavras, passos no piso, sem música"),
    ("V05", "T5", "K05", dialogo([
        ("P4", "firme, com a voz um pouco trêmula", "Mom locked Emily up without dinner yesterday."),
        ("P2", "com autoridade, alto e duro", "Don't you dare touch them!"),
        ("P4", "firme e desafiador", "I recorded everything, Mom. Even what you did afterwards."),
    ], "A MADRASTA não diz nenhuma palavra."),
     "O menino fala olhando para a mãe. A madrasta avança na direção dele com a mão levantada; o pai estica "
     "o braço na frente dela e a bloqueia enquanto fala. O menino tira o celular azul do bolso e o segura à "
     "frente do corpo na última fala. A madrasta congela.",
     CAM_CENA, "cozinha silenciosa de casa, passos no piso, sem música"),
    ("V06", "T6", "K06", '(sem fala no take: "I recorded everything, Mom." do V05 entra por cima na edição)',
     "A mão do menino puxa devagar o celular azul do bolso da calça cáqui e o levanta.",
     "fixa", "cozinha silenciosa de casa, o tecido da calça, sem música"),
    ("V07", "T7", "K07", '(sem fala no take: "Even what you did afterwards." do V05 entra por cima na edição)',
     "A madrasta fica parada, olhos arregalados, boca entreaberta, sem piscar. Só a respiração dela se mexe.",
     "leve push-in lento no rosto dela", "cozinha em silêncio total, sem música"),
]


def v_texto(abertura, acao, camera, som):
    fala = not abertura.startswith("(sem fala")
    partes = [abertura]
    if fala:
        partes.append(LIPSYNC)
    partes += ["o que acontece no vídeo: " + acao, "câmera: " + camera, "som ambiente: " + som]
    return "\n\n".join(partes)


def flow_k(d, edit=False):
    """JSON -> paragrafo autossuficiente do Flow."""
    if "sheet_layout" in d:
        partes = ["CHARACTER SHEET.", d["fiction_note"], "Vertical 9:16.", d["sheet_layout"],
                  d["identity_main"], d["expression"], d["lighting"], d["realism"]]
    else:
        partes = ["IMPORTANT: THIS IS IPHONE FOOTAGE.", d["fiction_note"], "Vertical 9:16.",
                  d["reference_use"], d["cast"], d["prop"], d["scene"], d["posture"], d["composition"],
                  "Camera " + d["camera"] + ".", d["state"], d["lighting"], d["realism"]]
    neg = d["negative"]
    partes.append(neg[0].upper() + neg[1:] + ".")
    return " ".join(p.strip() for p in partes)


def main():
    out = {}
    refs_json = []
    for code, pid, d in REFS:
        refs_json.append("## %s · %s · CHARACTER SHEET · GERAR DO ZERO\n\n"
                         "> ### 📎 ANEXAR: **NENHUMA IMAGEM**\n>\n> ### 🆕 GERAR DO ZERO, aprovar antes de qualquer K\n\n"
                         "```json\n%s\n```\n" % (code, NOME[pid], json.dumps(d, ensure_ascii=False, indent=2)))
    ks_json = []
    for code, take, beat, ids, d in K:
        anexos = " + ".join("REF-" + i for i in ids)
        lista = "\n".join("> **%d️⃣ REF-%s (%s)** aprovado" % (n + 1, i, NOME[i]) for n, i in enumerate(ids))
        ks_json.append("## %s · %s · %s · GERAR DO ZERO · %s\n\n"
                       "> ### 📎 ANEXAR: **%d IMAGENS**\n%s\n> **%d️⃣ COMPOSIÇÃO** `modelo/composicao_%s.jpg` (por último)\n>\n"
                       "> ### 🆕 GERAR DO ZERO\n\n```json\n%s\n```\n"
                       % (code, take, beat, anexos, len(ids) + 1, lista, len(ids) + 1, code,
                          json.dumps(d, ensure_ascii=False, indent=2)))
    vs = []
    for code, take, k, abertura, acao, cam, som in V:
        vs.append("### %s · %s · usa %s\n\n```text\n%s\n```\n" % (code, take, k, v_texto(abertura, acao, cam, som)))
    out["refs"] = "\n".join(refs_json)
    out["ks"] = "\n".join(ks_json)
    out["vs"] = "\n".join(vs)
    # blocos do Flow
    img = "\n\n".join(["%s\n%s" % (code, flow_k(d)) for code, _, d in REFS] +
                      ["%s\n%s" % (code, flow_k(d)) for code, _, _, _, d in K])
    vid = "\n\n".join("%s\n%s" % (code, v_texto(a, b, c, s).replace("\n\n", "\n")) for code, _, _, a, b, c, s in V)
    mapa = "\n".join(["| %s | nenhuma | gerar do zero, aprovar |" % code for code, _, _ in REFS] +
                     ["| %s | %s, depois `modelo/composicao_%s.jpg` |  |" % (code, ", ".join("REF-" + i for i in ids), code)
                      for code, _, _, ids, _ in K])
    out["img"], out["vid"], out["mapa"] = img, vid, mapa
    for tpl, destino in (("_tpl_prompts.md", "PROMPTS_PRODUCAO.md"), ("_tpl_flow.md", "FLOW_PACOTE.md")):
        txt = (AQUI / tpl).read_text(encoding="utf-8")
        for chave, valor in out.items():
            txt = txt.replace("{{%s}}" % chave.upper(), valor)
        assert "{{" not in txt, "placeholder sem valor em " + tpl
        (AQUI / destino).write_text(txt, encoding="utf-8")
    print("ok: %d REF, %d K, %d V" % (len(REFS), len(K), len(V)))


if __name__ == "__main__":
    main()
