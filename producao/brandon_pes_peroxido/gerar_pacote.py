"""Gera o pacote da producao brandon_pes_peroxido (avatar IA, growth, validacao, holistic.brandon).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Identidade, roupa e
cenario: a ancora aprovada em 2026-09-29 (avatar fixo por conta). Medidas de cada K: FICHA_FRAMES.md.
Prompt de imagem entregue em JSON (contrato do Flow v17). Gabarito: brandon_pao_sementes/gerar_pacote.py.

Troca obrigatoria aprovada com o roteiro: o spray do modelo vira agua oxigenada num borrifador marrom
sem rotulo. Nenhuma marca aparece nem e nomeada nos prompts.

Saidas: PROMPTS_BRANDON.md, FLOW_BRANDON.md e PROMPTS_PRODUCAO.md (copia do avatar ACTIVE).

Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")

HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 10)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES), FALAS
TRANSCRICAO_PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$",
                                 ROTEIRO.split("## Tabela bilíngue")[1].split("## ")[0], re.M))
assert set(TRANSCRICAO_PT) == set(TAKES), TRANSCRICAO_PT
# T1 e CENA CURTA so no numero de palavras: o modelo fala devagar a cena inteira.
FALA_NO_COMECO = {"T4", "T8"}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."


def frame_modelo(cod):
    return f"input/frames_modelo/{cod}_modelo.png"


LUZ = ("Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and feet "
       "with no harsh shadows. The red neon glows on the wall but does not tint her skin.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the "
            "trigger sprayer, container, glass or spoon, no studio, no plastic-looking skin, no extra fingers, no extra toes, "
            "no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden "
            "hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, "
            "no second person, no metal aerosol can, no wooden floor, no living room rug, no ceramic tile floor, "
            "no leather vest, no feathers, no silver cross")
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
           "with a small gold cross pendant and small stud earrings. Barefoot."),
    cena=("Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY "
          "REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY "
          "DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly "
          "visible and in focus. The floor is black rubber gym flooring."),
    cena_macro=("At the top edge of the frame, beyond the container, a strip of the black rubber gym floor and the "
                "white-painted concrete block wall with the small American flag pinned on it, discreet but clearly "
                "visible and in focus."),
    voz="voz feminina clara e firme de uma mulher de uns trinta anos",
    sotaque="de uma mulher negra americana",
    som="box de treino em casa, tranquilo",
)

SPRAY = "a plain brown plastic trigger sprayer with a white trigger and no label, filled with hydrogen peroxide"
POTE = "a clear rectangular plastic storage container"
BANCO = "a black padded gym bench"

EMOCAO = {
    "T1": "entonação intrigante e desafiadora, devagar, como quem avisa",
    "T2": "entonação séria, baixando um pouco a voz",
    "T3": "entonação calma e didática",
    "T4": "entonação calma e didática",
    "T5": "entonação didática e convicta",
    "T6": "entonação convicta e animada",
    "T7": "entonação calma e segura",
    "T8": "entonação calma e reflexiva",
    "T9": "entonação calorosa e convidativa, sorrindo no yes",
}
ACOES = {
    "T1": ("{n} borrifa o spray no dorso do pé descalço; por volta de 2 segundos uma espuma branca aparece na pele e "
           "vai crescendo em bolhas grossas; nos últimos segundos a câmera se aproxima devagar do pé."),
    "T2": "{n}, sentada no chão com a espuma branca no pé, olha para a câmera e fala, séria.",
    "T3": ("{n} borrifa três vezes dentro do pote, despeja o copo de água morna no pote e vira a colher de "
           "bicarbonato na água."),
    "T4": "{n}, sentada no banco com os dois pés dentro do pote, fala para a câmera enquanto bolhas começam a subir em volta dos pés.",
    "T5": ("A água em volta dos pés efervesce, com bolhas subindo e espuma branca crescendo. O rosto dela fica fora de "
           "quadro e a voz dela narra."),
    "T6": "{n}, sentada no banco, fala para a câmera com as mãos nas coxas, com pequenos movimentos naturais.",
    "T7": "{n} fala para a câmera e abre uma das mãos num gesto pequeno e natural.",
    "T8": "{n} se inclina um pouco para a frente e fala para a câmera, calma.",
    "T9": "{n} fala direto com quem assiste, sorrindo no yes, com as mãos nas coxas.",
}
CAMERA = {"T1": "fixa no chão, com aproximação lenta até o pé nos últimos segundos", "T5": "fixa, colada na parede do pote"}
SOM_EXTRA = {"T1": ", chiado do spray e espuma estalando", "T2": ", espuma estalando baixinho",
             "T3": ", água caindo no pote", "T4": ", água borbulhando", "T5": ", água borbulhando"}
MOMENTO = {"T1": "0,0 a 5,8 s", "T2": "5,8 a 9,6 s", "T3": "9,8 a 17,7 s", "T4": "17,7 a 20,4 s",
           "T5": "20,4 a 25,6 s", "T6": "25,6 a 33,3 s", "T7": "33,3 a 38,2 s", "T8": "38,2 a 41,3 s",
           "T9": "41,3 a 48,8 s"}
TITULOS = {"T1": "gancho, spray no pé colado na lente", "T2": "espuma no pé, olhando para a câmera",
           "T3": "receita no chão, spray no pote", "T4": "sentada no banco, pés no pote",
           "T5": "macro dos pés na água borbulhando", "T6": "no banco, resultado", "T7": "no banco, autoridade",
           "T8": "no banco, inclinada", "T9": "CTA, plano mais fechado"}


def keyframes(a):
    n = a["nome"]
    boca = "caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens"
    ref = (f"Use the first attached image only for {n}'s exact identity, wardrobe and own garage gym. Use the second "
           "attached image only as a composition reference for the camera position, framing and the action; do not "
           "copy its person, leather vest, feathers, wooden floor, rug, tiles, the blue and yellow aerosol can or the "
           "caption text.")
    cam_chao = "phone resting on the floor, standard 1x lens pointing slightly upward, straight-on, fixed"
    cam_banco = "phone on a small tripod at waist height, standard 1x lens, straight-on, fixed"
    pe = ("Her left leg is stretched forward so her bare left foot rests on the black rubber floor very close to the "
          "lens, the top of the foot facing the camera.")
    post_chao = (f"{n} sits cross-legged on the black rubber gym floor, her left leg stretched forward, her left hand "
                 "resting on her shin, her right hand holding the trigger sprayer.")
    comp_pe = ("Floor-level shot: the phone lens is about 30 centimeters from her bare foot, which fills the lower 30 "
               "percent of the frame at the center right, far closer to the camera than her face and larger than her "
               "head, nothing else competing with it; the trigger sprayer sits at the lower left and her head is in the "
               "upper part of the frame. Nothing else is on the floor. The background is reduced by framing, never by blur.")
    post_banco = f"{n} sits upright on {BANCO}, knees apart, both hands resting on her thighs, seen from the head down to mid-thigh."
    comp_banco = ("Straight-on medium shot: the phone lens is about 60 centimeters from her; her face and torso fill "
                  "the upper two thirds of the frame and her hands on her thighs sit in the lower part, closer to the "
                  "lens than her face. Nothing else is in frame. The background is reduced by framing, never by blur.")
    fora = "No prop in her hands; the trigger sprayer and the container are out of frame."
    ks = {
        "T1": dict(prop=f"{SPRAY[0].upper()}{SPRAY[1:]}, held in her right hand and pointed at the top of her bare left foot. " + pe,
                   posture=post_chao, composition=comp_pe, camera=cam_chao,
                   state=f"Start frame: the first fine mist is leaving the nozzle toward the top of the foot; the skin is still clean, no foam yet. {n} is {boca}.",
                   negative=NEG_BASE + ", no foam yet"),
        "T2": dict(prop=(f"A thick patch of white foam with big bubbles covers the top of her bare left foot and ankle. {pe} "
                         f"Lowered in her right hand she holds {SPRAY}."),
                   posture=post_chao, composition=comp_pe, camera=cam_chao,
                   state=f"Start frame: the foam sits on the foot, still. {n} is {boca}, serious."),
        "T3": dict(prop=(f"{POTE[0].upper()}{POTE[1:]}, empty, standing on the black rubber floor very close to the lens; a "
                         "clear drinking glass full of warm water stands to its left and a metal spoon heaped with white "
                         f"baking soda lies on the floor in front of it. She holds {SPRAY} in her right hand, pointed into "
                         "the container."),
                   posture=f"{n} sits cross-legged on the black rubber floor right behind the container, leaning slightly toward it.",
                   composition=("Floor-level shot: the phone lens is about 35 centimeters from the container, which with the "
                                "glass fills the lower 30 percent of the frame, closer to the camera than her face; her head "
                                "and torso fill the upper part of the frame. Nothing else is on the floor. The background is "
                                "reduced by framing, never by blur."),
                   camera=cam_chao,
                   state=f"Start frame: the first spray of mist is going into the empty container. {n} is {boca}."),
        "T4": dict(prop=(f"Both of her bare feet stand inside {POTE} filled with warm water, on the black rubber floor very "
                         "close to the lens."),
                   posture=f"{n} sits upright on {BANCO}, knees apart, both hands resting on her knees, seen from head to feet.",
                   composition=("Low floor-level wide shot: the phone lens is about 40 centimeters from the container, which "
                                "fills the lower 25 percent of the frame, closer to the camera than her face; she fills the "
                                "rest of the frame from head to feet. Nothing else is on the floor. The background is reduced "
                                "by framing, never by blur."),
                   camera=cam_chao,
                   state=f"Start frame: small bubbles are starting to rise around her feet. {n} is {boca}."),
        "T5": dict(scene=a["cena_macro"],
                   prop=(f"Her two bare feet inside {POTE}, seen through its clear side wall, the warm water full of rising "
                         "bubbles and a thick layer of white foam fizzing around her ankles."),
                   posture="Only her feet and lower shins are in frame.",
                   composition=("Macro close-up at floor level: the phone lens is about 10 centimeters from the side wall of "
                                "the container, which fills the whole frame edge to edge. Nothing else is in frame. The "
                                "background is reduced by framing, never by blur."),
                   camera="phone resting on the floor against the container, standard 1x lens, level, fixed",
                   state="Start frame: the water is fizzing, bubbles rising along the toes and the foam building around the ankles.",
                   negative=NEG_BASE + NEG_SEM_ROSTO),
        "T6": dict(prop=fora, posture=post_banco, composition=comp_banco, camera=cam_banco,
                   state=f"Start frame: {n} is {boca}, calm and sure."),
        "T7": dict(prop=fora, posture=post_banco.replace("both hands resting on her thighs", "one hand resting on her thigh, the other hand open in a small gesture"),
                   composition=comp_banco, camera=cam_banco,
                   state=f"Start frame: {n} is {boca}, one hand open in a small gesture."),
        "T8": dict(prop=fora, posture=post_banco.replace("sits upright", "sits leaning slightly forward"),
                   composition=comp_banco, camera=cam_banco,
                   state=f"Start frame: {n} leans slightly toward the lens and is {boca}."),
        "T9": dict(prop=fora, posture=post_banco,
                   composition=("Straight-on medium close shot, the tightest of the video: the phone lens is about 45 "
                                "centimeters from her; her face and torso fill the upper three quarters of the frame and "
                                "her hands on her thighs sit at the bottom edge. Nothing else is in frame. The background is "
                                "reduced by framing, never by blur."),
                   camera=cam_banco,
                   state=f"Start frame: {n} is smiling warmly, {boca}."),
    }
    out = []
    for i, t in enumerate(TAKES, 1):
        d = ks[t]
        cod = f"K{i:02d}"
        j = {
            "shot_id": f"{cod}_{t.lower()}_{a['arquivo'].lower()}",
            "fiction_note": FICCAO,
            "reference_use": ref,
            "identity_main": a["identidade"],
            "wardrobe": a["roupa"],
            "scene": d.get("scene", a["cena"]),
            "prop": d["prop"],
            "posture": d["posture"],
            "composition": d["composition"],
            "camera": d["camera"],
            "lighting": LUZ,
            "state": d["state"],
            "realism": REALISMO,
            "aspect_ratio": "9:16 vertical",
            "negative": d.get("negative", NEG_BASE),
        }
        out.append(dict(codigo=cod, take=t, titulo=TITULOS[t], j=j))
    return out


def videos(a):
    n = a["nome"]
    vs = []
    for i, t in enumerate(TAKES, 1):
        acao = ACOES[t].format(n=n)
        if t in FALA_NO_COMECO:
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
        "1. Clipes numerados na ordem: V01 a V09.",
        "2. Cortar cada clipe no tempo da cena do modelo: " + "; ".join(f"V{t[1:].zfill(2)} {MOMENTO[t]}" for t in TAKES) + ".",
        "3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.",
        "4. Flash branco de ~0,2 s entre o V02 e o V03, e dissolve curto entre o V04 e o V05, como no modelo.",
        "5. No V01 a fala ocupa quase a cena inteira, devagar; não acelerar. Nos V04 e V08 (cenas curtas) a fala vem no começo; cortar logo depois da última palavra.",
        "6. Legenda em caixa alta, branca, com a palavra-chave em amarelo, na metade de baixo do quadro, igual ao modelo.",
        "7. Sem Voice Changer: a voz vem do prompt de cada V.",
        "8. Música só depois do gancho (a partir do V03), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "9. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {TRANSCRICAO_PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = ["# holistic.brandon | FityWell Growth Pés com água oxigenada | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (48,8 s, avatar IA)", "",
         f"Âncora: `{a['ancora']}`", "",
         "Funil: growth, follow + comentário `yes`. Rodada de validação, gancho fiel ao modelo com a troca obrigatória do spray. Sem produto em quadro.", "",
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
          f"- Gancho: {SPRAY}; a espuma branca nasce no dorso do pé descalço.",
          f"- Receita: {POTE}, copo de vidro com água morna, colher com bicarbonato. Corpo: {BANCO}.",
          "- Nenhuma embalagem com texto ou marca; a lata de aerossol azul e amarela do modelo não entra.", "",
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
          "4. Zero travessão.", "5. Keyword `yes` no T9.",
          "6. Nenhuma marca em quadro nem na fala: borrifador, pote, copo e colher lisos.",
          "7. Negative sem termo sensível.",
          "8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "9. Gancho fiel no conteúdo: spray no pé descalço colado na lente e a espuma branca crescendo, falado desde o segundo 0.",
          "10. Um K = um V; a espuma do T1 é uma imagem só, do estado inicial (pé limpo).", ""]
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
