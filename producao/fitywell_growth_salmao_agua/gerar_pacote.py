"""Gera os pacotes por avatar da producao fitywell_growth_salmao_agua.

Fonte unica da fala: ROTEIRO.md aprovado em 2026-09-30 (lido do disco, nunca redigitado). A fala e
identica para os dois avatares (tabela de congruencia do ROTEIRO).
Identidade, roupa e cenario: Eva Dall pela ficha usada em fitywell_growth_dentes_agua (conferida de
novo contra o anexo); holistic.brandon pela ficha de 2026-09-29 em avatares-fichas, conferida contra
a ancora anexada (identica, byte a byte).

K em JSON tambem no bloco do Flow (Luigi, 2026-09-25 e 2026-09-30): `format` na frente, sem shot_id.

Saidas: PROMPTS_<AVATAR>.md (fonte interna com JSON e shot_id), FLOW_<AVATAR>.md (blocos limpos do
Flow) e PROMPTS_PRODUCAO.md (copia do avatar ACTIVE, que e o que o checar_entrega.py le).

Uso: python3 gerar_pacote.py [NOME_DO_ATIVO]   (padrao: o ACTIVE do AVATAR_QUEUE.md)
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")

FALAS = {}
for m in re.finditer(r'^### (T\d+) · .*?\n\n> "(.+?)"\s*$', ROTEIRO, re.M | re.S):
    FALAS[m.group(1)] = m.group(2)
assert len(FALAS) == 5, FALAS
TAKES = list(FALAS)

FORMATO = "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."
FICCAO = "This is a fictional AI-generated character, no real person is depicted."
FRAME = "input/frames_modelo/K01_modelo.png"

LUZ_INTERNA = ("Neutral overcast daylight from a window, the outside clearly visible through the window, "
               "soft even light on the face with no harsh shadows.")
LUZ_BOX = ("Neutral overcast daylight coming in from a wide open garage door out of frame, soft even light on "
           "the face with no harsh shadows, the red neon adding only a faint glow on the wall behind her.")

REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, "
            "no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, "
            "no sunset, no captions, no subtitles, no words overlaid on the image.")

NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container "
            "or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, "
            "no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, "
            "no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, "
            "no cinematic lighting, no second person in frame")
NEG_TANQUE = (", no aquarium gravel, no aquarium plants or decorations, no live fish swimming, no lid on the tank, "
              "no cooked fish")

AVATARES = [
    dict(nome="Eva Dall", arquivo="EVA_DALL", genero="homem", pron="He", pos="his",
         ancora="producao/_ancoras/eva_dall_ancora.jpeg",
         identidade="The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
         roupa="White ribbed tank top and a thin silver chain.",
         torso="his white ribbed tank top and thin silver chain",
         cena="His own modern white kitchen, the same room as the reference image, unchanged: a strongly veined dark green marble counter in front of him, a matching dark green marble wall behind the stove at the left, tall windows to the right and a small American flag on the shelf beside a small potted plant.",
         superficie="the dark green veined marble counter",
         postura="standing behind his dark green marble counter, leaning slightly toward the camera",
         luz=LUZ_INTERNA, sotaque="de um homem negro americano",
         voz="voz média e amigável de um homem de quase cinquenta anos", som="cozinha residencial tranquila"),
    dict(nome="Brandon", arquivo="HOLISTIC_BRANDON", genero="mulher", pron="She", pos="her",
         ancora="producao/_ancoras/holistic_brandon_ancora.jpg",
         identidade="The exact fictional AI character Brandon, explicitly female: Black mixed-race American woman around thirty, athletic build, light brown skin with light freckles across her nose and cheeks, brown eyes, cornrow braids that turn into long loose braids down to her waist with wooden and gold beads at the tips, small stud earrings, a floral blackwork tattoo sleeve on her right arm, a fine tattoo on the inside of her left arm and a fine floral tattoo on her chest below the left collarbone.",
         roupa="White ribbed tank top, loose black lightweight training shorts, and a thin gold chain with a small gold cross pendant.",
         torso="her white ribbed tank top and thin gold chain with the small gold cross",
         cena="Her own garage training box, the same room as the reference image, unchanged: white-painted concrete block walls under a dark wood slat ceiling, a red neon sign on the left wall, a small American flag high on the wall at the right, and a metal-and-wood shelf with glass jars of seeds at the far right. A black table stands in front of her.",
         superficie="the black table",
         postura="standing behind her black table, leaning slightly toward the camera",
         luz=LUZ_BOX, sotaque="de uma mulher negra americana",
         voz="voz feminina média, firme e calorosa de uma mulher atlética de uns trinta anos", som="box de treino tranquilo"),
]

TANQUE = ("A rectangular clear glass tank with no lid, shaped like a small aquarium about as wide as {pos} shoulders "
          "and one hand deep, stands on {sup}")


def keyframes(a):
    n, P, p = a["nome"], a["pron"], a["pos"]
    ref = f"Use the attached image only for {n}'s exact identity, wardrobe and own setting. Do not copy its pose or framing."
    boca = "caught mid-sentence, lips naturally parted, animated expression"
    tanque = TANQUE.format(pos=p, sup=a["superficie"])
    fala_meio = (f"From the chest up, {p} head and upper chest clear and centered in the upper half of the frame, "
                 f"{p} face about 70 centimeters from the lens")
    cam_meio = "phone camera on a small tripod at chest height, 26 mm wide lens, straight on, slight downward angle toward the work surface, fixed"
    ks = [
        dict(codigo="K01", take="T1", titulo="gancho, o filé de salmão entrando no aquário de água quente", anexos=2, j={
            "reference_use": ref + " Use the second attached image only as a composition reference for the glass tank filling the lower third, the hand lowering the salmon fillet into it and the person centered behind it; do not copy its man, his T-shirt, his room or its colors.",
            "prop": tanque + f", filled almost to the top with clear hot water. {n}'s right hand is lowering a thick raw salmon fillet, bright orange with thin white fat lines, held by one corner between the fingertips: the lower half of the fillet is already under the water, the upper half still above the surface, with small ripples spreading around it. The work surface is otherwise empty.",
            "posture": f"{n} is {a['postura']}, the right hand reaching down into the tank, the left forearm resting on the work surface beside it.",
            "composition": f"The glass tank fills the bottom 35 percent of the frame, very close to the lens, its front glass wall about 30 centimeters from the camera, large in frame and closer to the camera than {p} face; the salmon fillet sits in the center of that lower third and is the brightest thing in the frame. {fala_meio}. Nothing else competes with the salmon fillet. The background is reduced by framing, never by blur.",
            "camera": cam_meio,
            "state": f"Start frame: the salmon fillet is half submerged and still perfectly whole, ripples on the water. {n} looks into the lens, {boca}.",
            "negative": NEG_BASE + NEG_TANQUE + ", no broken or flaking fillet yet",
        }),
        dict(codigo="K02", take="T2", titulo="close do aquário, o filé inteiro no fundo antes de se desmanchar", anexos=1, j={
            "reference_use": ref,
            "prop": tanque + f", filled with clear hot water, seen at water level through its front glass wall. One whole thick raw salmon fillet, bright orange with thin white fat lines, rests flat on the glass bottom in the center of the tank, intact. Nothing else is inside the tank.",
            "posture": f"Behind the tank only {n}'s torso is visible, {a['torso']}, with the fingertips of one hand resting on the top edge of the tank. {p.capitalize()} face is above the top edge of the frame.",
            "composition": f"Close shot at tank height: the tank fills the frame from the bottom edge up to about 75 percent of its height, its front glass wall about 20 centimeters from the lens, very close to the lens, large in frame; the salmon fillet sits in the center of the frame, larger than {p} hand. Above the waterline only {p} torso. No face in frame. The background is reduced by framing, never by blur.",
            "camera": "phone camera low, at counter level, at the height of the water, about 20 centimeters from the front glass, 26 mm wide lens, straight on, fixed",
            "state": "Start frame: the water is calm and clear, the fillet lies whole and still on the bottom, not a single flake floating yet.",
            "negative": NEG_BASE + NEG_TANQUE + ", no face in frame, no broken or flaking fillet yet",
        }),
        dict(codigo="K03", take="T3", titulo="salmão inteiro entrando na água fria", anexos=1, j={
            "reference_use": ref,
            "prop": tanque + f", filled with clear cold water. {n}'s right hand holds a whole raw salmon by the back, silver skin with small black spots, head and tail intact, lying on its side and longer than the tank is deep, and lowers it into the water: the belly is just under the surface and the tail hangs over the front edge, with ripples around it. The work surface is otherwise empty.",
            "posture": f"{n} is {a['postura']}, the right hand holding the fish over the tank, the left forearm resting on the work surface.",
            "composition": f"The glass tank with the whole salmon fills the bottom 35 percent of the frame, very close to the lens, its front glass wall about 30 centimeters from the camera, large in frame and closer to the camera than {p} face; the salmon runs almost the full width of the frame. {fala_meio}. Nothing else competes with the salmon. The background is reduced by framing, never by blur.",
            "camera": cam_meio,
            "state": f"Start frame: the whole salmon is half in the water, not yet released. {n} looks into the lens, {boca}.",
            "negative": NEG_BASE + NEG_TANQUE,
        }),
        dict(codigo="K04", take="T4", titulo="brócolis na tigela de vidro, água despejada", anexos=1, j={
            "reference_use": ref,
            "prop": f"A round clear glass mixing bowl full of fresh, clean-looking bright green broccoli florets half covered in water stands on {a['superficie']} in the lower foreground. {n}'s right hand holds a clear plastic water bottle with no label, tilted over the bowl, pouring a steady stream of water onto the florets. A small plain clear glass vinegar cruet with no label stands on the work surface beside the bowl. Nothing else is on the work surface.",
            "posture": f"{n} is {a['postura']}, the left hand resting flat on the work surface beside the bowl.",
            "composition": f"The glass bowl of broccoli fills the bottom 30 percent of the frame, very close to the lens, about 30 centimeters from the camera, large in frame and closer to the camera than {p} face. {fala_meio}. Nothing else competes with the broccoli bowl. The background is reduced by framing, never by blur.",
            "camera": cam_meio,
            "state": f"Start frame: water is streaming from the water bottle onto the broccoli, small splashes on the surface. {n} looks into the lens, {boca}.",
            "negative": NEG_BASE + ", no cooked broccoli, no sauce, no plate",
        }),
        dict(codigo="K05", take="T5", titulo="tábua com frango, salmão e truta, CTA", anexos=1, j={
            "reference_use": ref,
            "prop": f"{n} holds a thick rectangular wooden cutting board horizontally with both hands, pushed toward the lens, very close to the camera in the lower foreground, large in frame: on the board a whole raw chicken on the left, three thick raw salmon fillet portions standing side by side in the middle, bright orange with white fat lines, and a whole raw trout with silver and pink skin on the right. Nothing else is on the board.",
            "posture": f"{n} is {a['postura']}, holding the board by its two short ends.",
            "composition": f"The cutting board fills the bottom 35 percent of the frame, its front edge about 30 centimeters from the lens, closer to the camera than {p} face, the salmon portions in the center. {fala_meio}. This is the tightest talking shot of the video. The background is reduced by framing, never by blur.",
            "camera": cam_meio,
            "state": f"Start frame: {n} smiles wide with excitement, eyes on the lens, {boca}.",
            "negative": NEG_BASE + ", no cooked food, no packaging, no price tags",
        }),
    ]
    for k in ks:
        j = k["j"]
        k["j"] = {
            "shot_id": f"{k['codigo']}_{k['take'].lower()}_{a['arquivo'].lower()}",
            "format": FORMATO,
            "fiction_note": FICCAO,
            "reference_use": j["reference_use"],
            "identity_main": a["identidade"],
            "wardrobe": a["roupa"],
            "scene": a["cena"],
            "prop": j["prop"],
            "posture": j["posture"],
            "composition": j["composition"],
            "camera": j["camera"],
            "lighting": a["luz"],
            "state": j["state"],
            "realism": REALISMO,
            "aspect_ratio": "9:16 vertical",
            "negative": j["negative"],
        }
    return ks


EMOCAO = {
    "T1": "entonação direta e curiosa, de quem vai mostrar um teste que pouca gente conhece",
    "T2": "entonação séria e firme, com um toque de alerta",
    "T3": "entonação didática e confiante, explicando com clareza",
    "T4": "entonação didática, com um leve tom de nojo no fim da frase",
    "T5": "entonação animada e convidativa, sorrindo",
}
ACOES = {
    "T1": "{n} termina de baixar o filé de salmão na água do aquário, solta o filé e ele desce devagar até o fundo; {pr} fala olhando para a câmera. {Pr} diz a frase em ritmo natural logo no começo e depois fica olhando para o aquário em silêncio.",
    "T2": "o filé de salmão parado no fundo do aquário começa a rachar pelas linhas brancas de gordura e se desfaz em dezenas de lascas laranja que se soltam e flutuam pela água; atrás do vidro só aparece o torso, parado, com a mão apoiada na borda do aquário. A voz diz a frase em ritmo natural logo no começo e o resto do clipe é o filé se desmanchando.",
    "T3": "{n} solta o salmão inteiro dentro da água; o peixe afunda devagar e fica deitado no fundo do aquário; {pr} apoia os braços dos dois lados do aquário e fala para a câmera.",
    "T4": "{n} despeja a água da garrafa sobre os brócolis, larga a garrafa, pega a garrafinha de vinagre e despeja um fio dentro da tigela; na metade do clipe a câmera avança devagar até a tigela encher o quadro e o rosto sair por cima; no close, pequenas larvinhas finas e bege se soltam dos floretes e ficam boiando na água.",
    "T5": "{n} segura a tábua com as duas mãos e fala para a câmera, sorrindo {animado}; nos últimos segundos a câmera avança devagar até a tábua, o rosto sai por cima e o quadro fecha nas postas de salmão.",
}
CAMERA = {
    "T1": "fixa, no tripé, na altura do peito",
    "T2": "fixa, na altura da água, colada no vidro do aquário",
    "T3": "fixa, no tripé, com uma leve descida e aproximação contínua, sem corte",
    "T4": "fixa no começo, depois push-in lento e contínuo até a tigela, sem corte",
    "T5": "fixa, depois push-in lento e contínuo até a tábua nos últimos segundos, sem corte",
}
SOM_EXTRA = {"T1": ", som leve de água mexendo", "T2": ", som leve e abafado de água",
             "T3": ", som de água mexendo quando o peixe entra", "T4": ", som da água caindo na tigela"}

TRANSCRICAO_PT = {
    "T1": "Se você comprou salmão no mercado, coloque ele na água quente.",
    "T2": "Se ele se desmanchar fácil, a carne não é de verdade.",
    "T3": "Número dois, coloque o seu peixe na água fria. Se ele afundar, está fresco. Se ele boiar, ficou tempo demais na prateleira.",
    "T4": "Número três, coloque o brócolis na água com um pouco de vinagre. Qualquer inseto escondido e os ovos dele vão se soltar e ficar na água.",
    "T5": "Eu tenho dicas assim para quase todo alimento que você compra. Salve isso e comente outros alimentos para ver mais. Me siga para não perder nada.",
}
CORTE = {"T1": "0,0 a 3,0 s", "T2": "3,0 a 7,5 s", "T3": "7,5 a 15,1 s", "T4": "15,1 a 22,8 s", "T5": "22,8 a 30,0 s"}


def videos(a):
    n = a["nome"]
    mulher = a["genero"] == "mulher"
    art = "a avatar" if mulher else "o avatar"
    pr = "ela" if mulher else "ele"
    ouvido = "ouvida" if mulher else "ouvido"
    vs = []
    for i, take in enumerate(TAKES, 1):
        acao = ACOES[take].format(n=n, pr=pr, Pr=pr.capitalize(), animado="animada" if mulher else "animado")
        fora = ", fora de quadro (só o torso aparece, o rosto fica acima do quadro)," if take == "T2" else ","
        txt = (f"{art} {n}, {a['genero']}{fora} fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
               f"{EMOCAO[take]}, voz autêntica, como se exigisse ser {ouvido}, a seguinte frase: \"{FALAS[take]}\"\n\n"
               f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
               f"o que acontece no vídeo: {acao}\n\n"
               f"câmera: {CAMERA[take]}\n\n"
               f"som ambiente: {a['som']}{SOM_EXTRA.get(take, '')}, sem música")
        vs.append((f"V{i:02d}", take, f"K{i:02d}", txt))
    return vs


def json_flow(j):
    """O K do Flow: objeto JSON inteiro, `format` na frente, sem shot_id (metadata)."""
    return json.dumps({k: v for k, v in j.items() if k != "shot_id"}, ensure_ascii=False, indent=2)


def anexo(a, k):
    linhas = [f"> ### 📎 ANEXAR: **{k['anexos']} {'IMAGENS' if k['anexos'] > 1 else 'IMAGEM'}**",
              f"> **1️⃣ ÂNCORA {a['nome'].upper()}** `{a['ancora']}`"]
    if k["anexos"] > 1:
        linhas.append(f"> **2️⃣ FRAME DO MODELO, só composição** `{FRAME}`")
    linhas += [">", "> ### 🆕 GERAR DO ZERO"]
    return "\n".join(linhas)


def rotulo_anexo(a, k):
    return f"ÂNCORA {a['nome'].upper()}" + (" + FRAME DO MODELO" if k["anexos"] > 1 else "")


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    art = "a avatar" if a["genero"] == "mulher" else "o avatar"
    ouvido = "ouvida" if a["genero"] == "mulher" else "ouvido"
    L = [f"# {a['nome']} | FityWell Growth Salmão na água | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (30,0 s, Jake Miller Health)", "",
         f"Âncora: `{a['ancora']}`", "",
         "Funil: growth, save + comment + follow. Rodada de validação, gancho fiel ao modelo. Sem produto em quadro.", "",
         "## Índice de geração", "",
         "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    for k in ks:
        L.append(f"| {k['take']} | {k['codigo']} | {rotulo_anexo(a, k)} | GERAR DO ZERO |")
    L += ["", "Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro, "
          "então não existe `EDITAR do K__` aqui. Um K = um V pelo número.", "",
          "## Trava de identidade e continuidade", "",
          f"- Identidade: {a['identidade']}",
          f"- Roupa: {a['roupa']}",
          f"- Cenário (fixo da conta, em todos os K): {a['cena']}",
          f"- Luz: {a['luz']}",
          f"- Voz (igual em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.",
          "- Sem 2ª pessoa.", "",
          "## Trava do prop herói", "",
          "- Gancho e T2: " + TANQUE.format(pos=a["pos"], sup=a["superficie"]) + ", cheio de água quente, com um filé grosso de salmão cru, laranja com linhas brancas de gordura.",
          "- T3: o mesmo aquário, água fria, salmão inteiro cru prateado com pintinhas pretas.",
          "- T4: tigela redonda de vidro com floretes de brócolis na água, garrafa plástica de água e garrafinha de vidro de vinagre, as duas sem rótulo.",
          "- T5: tábua de madeira grossa com frango inteiro cru, três postas de salmão e uma truta inteira crua.",
          "- Nenhuma embalagem com texto ou marca.", "",
          "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "",
          "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · {rotulo_anexo(a, k)}", "", anexo(a, k), "",
              f"Cena: {k['titulo']}.", "", "```json", json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["## Bloco global de vídeo", "", "```text",
          f"{art} {a['nome']}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
          f"[emoção da fala], voz autêntica, como se exigisse ser {ouvido}, a seguinte frase: \"[FALA EXATA DO ROTEIRO]\"", "",
          f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.", "",
          "o que acontece no vídeo: [ação enxuta]", "", "câmera: [fixa]", "", f"som ambiente: {a['som']}, sem música",
          "```", "", "# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Mapa de âncoras", "", "| Keyframe | Referências a anexar | Modelo |", "|---|---|---|",
          f"| K01 | ÂNCORA {a['nome'].upper()} + FRAME DO MODELO (`{FRAME}`, só composição) | Nano Banana 2, 9:16, 4 imagens |",
          f"| K02 a K05 | ÂNCORA {a['nome'].upper()} | Nano Banana 2, 9:16, 4 imagens |", "",
          "## Montagem no CapCut", "",
          *montagem(), "",
          "## Gates de qualidade", "",
          "1. Fala de cada V igual ao ROTEIRO, palavra por palavra.",
          "2. Um take por cena do modelo; T1 e T2 marcados CENA CURTA; nenhum take acima de 29 palavras.",
          "3. Bandeira dos EUA no campo scene de todo K.",
          "4. Zero travessão.",
          "5. Growth: sem keyword, sem produto, sem link; CTA save + comment + follow do próprio modelo.",
          "6. Produto fora de quadro, nenhuma garrafa ou embalagem com marca ou texto.",
          "7. Negative sem termo sensível.",
          "8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente com medida, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "9. Gancho fiel no conteúdo: filé de salmão cru entrando no aquário de água, falado desde o segundo 0; payoff do filé se desmanchando no close do T2.",
          "10. Um K = um V; os reveals (filé desmanchando, peixe afundando, larvinhas, push-in) acontecem dentro do clipe, a imagem é o estado inicial.",
          "11. FICHA_FRAMES.md com placar de cada K antes do envio.", ""]
    flow = [f"# Blocos limpos para o Google Flow | {a['nome']}", "", f"Fonte interna: `PROMPTS_{a['arquivo']}.md`", "",
            "## BLOCO DE IMAGEM", "", "```text"]
    for k in ks:
        flow += [k["codigo"], json_flow(k["j"]), ""]
    flow += ["```", "", "## BLOCO DE VÍDEO", "", "```text"]
    for cod, _, _, txt in vs:
        flow += [cod, txt, ""]
    flow += ["```", "", "## Tabela de leitura humana", "", "| Código | Take | Anexar |", "|---|---|---|"]
    for k in ks:
        flow.append(f"| {k['codigo']} / V{k['codigo'][1:]} | {k['take']}, {k['titulo']} | {rotulo_anexo(a, k)} |")
    flow += ["", "## Transcrição final por take", "", "| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        flow.append(f"| {t} | {FALAS[t]} | {TRANSCRICAO_PT[t]} |")
    return "\n".join(L) + "\n", "\n".join(flow) + "\n"


def montagem():
    return [
        "1. Clipes numerados na ordem: V01, V02, V03, V04, V05.",
        "2. Cortar cada clipe no tempo da cena do modelo: " + "; ".join(f"V{t[1:].zfill(2)} {CORTE[t]}" for t in TAKES) + ".",
        "3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.",
        "4. V01 e V02 são cenas curtas: a fala vem no começo; cortar V01 logo depois de \"hot water\" e V02 quando o filé estiver todo em lascas, no tempo da cena.",
        "5. Legenda de 2 a 3 palavras por vez, caixa alta, fonte bold branca com contorno preto e a palavra falada em amarelo, no meio do quadro, do começo ao fim, igual ao modelo.",
        "6. Sem Voice Changer: a voz vem do prompt de cada V.",
        "7. Música só do V03 em diante, nunca no gancho (V01 e V02), entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "8. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def main():
    fila = (AQUI / "AVATAR_QUEUE.md").read_text(encoding="utf-8")
    ativo = sys.argv[1] if len(sys.argv) > 1 else re.search(r"\| ACTIVE \| ([^|]+?) \|", fila).group(1)
    ativo = "Brandon" if "brandon" in ativo.lower() else ativo
    for a in AVATARES:
        p, f = pacote(a)
        (AQUI / f"PROMPTS_{a['arquivo']}.md").write_text(p, encoding="utf-8")
        (AQUI / f"FLOW_{a['arquivo']}.md").write_text(f, encoding="utf-8")
        if a["nome"] == ativo:
            (AQUI / "PROMPTS_PRODUCAO.md").write_text(p, encoding="utf-8")
    print("ok: %d pacotes; PROMPTS_PRODUCAO.md = %s" % (len(AVATARES), ativo))


if __name__ == "__main__":
    main()
