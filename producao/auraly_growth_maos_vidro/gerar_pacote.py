"""Gera o pacote da producao auraly_growth_maos_vidro (Auraly, growth, origem organica, validacao).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Identidade, roupa e
cenario: ficha da Morgan Vance (avatares-fichas) e a ancora em cena real. Medidas: FICHA_FRAMES.md.
Origem organica (PERFIL_ORGANICO.md): celular apoiado numa mesa de vidro, maos juntas com os dedos
entrelacados na frente do peito, reflexo no vidro no terco de baixo, sem carta e sem kit obrigatorio,
primeira linha do V no tom de conversa de celular. Prompt de imagem em JSON (Flow v17). Mapa K/V: o
plano unico do modelo vira um K01 que alimenta V01 a V15.

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
assert TAKES == ["T%d" % i for i in range(1, 16)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES), FALAS
PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$", ROTEIRO.split("## Tradução completa (Português)")[1].split("\n## ")[0], re.M))
assert set(PT) == set(TAKES), PT

MAPA = {"V%02d" % i: "K01" for i in range(1, 16)}

FICCAO = "This is a fictional AI-generated character, no real person is depicted; she resembles no real or famous person."
LUZ_INTERNA = ("Neutral overcast daylight from the bedroom window, the outside clearly visible through the window, never "
               "white or blown out, soft even light on the face and hands with no harsh shadows. The room lamps are switched off.")
REALISMO = ("Real skin with visible pores, irregular texture, small acne marks and soft asymmetry, baby hairs and natural "
            "flyaways, iPhone front-camera footage look, flat natural light, low contrast, slight JPEG compression, boring "
            "everyday reality, not professional photography, background fully in focus, everything in sharp focus, no AI "
            "polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no studio, no ring light, no plastic-looking human skin, "
       "no extra fingers, no third hand, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow "
       "tint on the skin, no golden glow, no golden hour light, no sunset, no lamp glow, no night, no beauty smoothing, no "
       "visible phone, no HDR, no cinematic lighting, no second person in frame, no card in hand, no props in the hands, "
       "no standing pose")

AVATARES = [
    dict(nome="Morgan Vance", arquivo="MORGAN_VANCE", genero="mulher", pron="She", pos="her",
         ancora="producao/_ancoras/morgan_vance_ancora.jpg",
         identidade=("The exact fictional AI character Morgan Vance: Black American woman around twenty-five, long "
                     "knotless box braids down to the waist with a middle part and a few small gold braid cuffs, sleek "
                     "laid baby-hair edges, deep brown skin with visible pores and small acne marks on the forehead and "
                     "cheeks, dark brown eyes, long lashes, defined brows, glossy lips, a small gold hoop in the nostril "
                     "and small gold earrings."),
         roupa=("Cobalt-blue ribbed long-sleeve top with a scoop neck and a thin gold chain with a small gold heart "
                "pendant."),
         maos="her deep brown hands",
         cena=("Her own bright white bedroom with a sloped ceiling, the same lived-in bedroom as the reference, unchanged. "
               "Behind her a large American flag is pinned flat to the white wall, clearly visible and in focus; at the "
               "left a window with a raised white blind shows trees and an overcast sky; at the right a white dresser "
               "holds a clear quartz crystal point on a wooden base and a short stack of books. She sits at a small "
               "clear glass-top desk placed in her bedroom."),
         luz=LUZ_INTERNA, sotaque="leve de Atlanta",
         voz="voz feminina média e jovem, confiante e direta de uma mulher afro-americana de vinte e cinco anos",
         som="quarto silencioso"),
]

EMOCAO = {
    "T1": "baixa, quase em segredo", "T2": "séria, em tom de aviso", "T3": "animada e confiante",
    "T4": "aliviada e calorosa", "T5": "firme e calma", "T6": "séria, depois intrigada", "T7": "intensa",
    "T8": "calorosa", "T9": "firme", "T10": "urgente e próxima", "T11": "em ritmo de instrução",
    "T12": "em ritmo de instrução, depois firme", "T13": "animada, depois séria", "T14": "baixa e séria",
    "T15": "próxima e firme",
}
GESTO = ("{n} solta as mãos e abre as palmas num gesto curto enquanto fala, depois volta a juntar as mãos com os dedos "
         "entrelaçados na frente do peito, os cotovelos no vidro, olhando para a lente.")
ACAO = {
    "T1": ("{n} mantém as mãos juntas com os dedos entrelaçados na frente do peito, os cotovelos no vidro, e fala baixo "
           "olhando para a lente."),
    "T3": GESTO, "T6": GESTO, "T10": GESTO, "T13": GESTO,
    "T5": ("{n} fecha a mão direita na frente do peito enquanto fala, depois volta a juntar as mãos, os cotovelos no "
           "vidro, olhando para a lente."),
    "T11": ("{n} abre as mãos devagar enquanto fala e depois volta a juntá-las com os dedos entrelaçados, os cotovelos "
            "no vidro, olhando para a lente."),
    "T15": ("{n} se inclina um pouco para a lente com as mãos juntas na frente do peito, os cotovelos no vidro, e fala "
            "olhando para a lente."),
}
ACAO_PADRAO = ("{n} mantém as mãos juntas com os dedos entrelaçados na frente do peito, os cotovelos no vidro, e fala "
               "olhando para a lente, piscando devagar.")
CAMERA = "phone propped upright on the glass desk at chest height about two feet away, 1x front lens, straight on, fixed"


def keyframes(a):
    n, p = a["nome"], a["pos"]
    j = {
        "shot_id": f"K01_{a['arquivo'].lower()}",
        "fiction_note": FICCAO,
        "reference_use": (f"Use the first attached image only for {n}'s exact identity, wardrobe, jewelry and own bedroom; "
                          f"do not copy its selfie pose or the card in her hand. Use the second attached image only as a "
                          f"composition reference for the camera position, framing, the glass desk and the clasped hands; "
                          f"do not copy its person, clothes, night window, lamp or on-screen text."),
        "identity_main": a["identidade"],
        "wardrobe": a["roupa"],
        "scene": a["cena"],
        "prop": (f"No objects: {a['maos']} are clasped together in front of {p} chest with the fingers interlaced, the "
                 f"elbows resting on the clear glass desktop."),
        "posture": (f"{n} sits facing the lens at the glass desk, elbows on the glass, hands clasped together with the "
                    f"fingers interlaced right in front of {p} chest, looking straight into the lens."),
        "composition": (f"The hands clasped together are in the center of the frame just above the front edge of the glass "
                        f"desk, about 15 percent of the frame, about 12 inches from the lens, closer to the camera than "
                        f"{p} face. {p.capitalize()} face sits in the upper middle of the frame, framed from the top of the "
                        f"head to the waist. The bottom third of the frame is the clear glass desktop, showing a soft "
                        f"upside-down reflection of {p} arms and top on the glass. Nothing else is in the foreground. The "
                        f"background is reduced by framing, never by blur."),
        "camera": CAMERA,
        "lighting": a["luz"],
        "state": (f"Start frame: {n} looks into the lens, caught mid-sentence, lips naturally parted, calm, confident "
                  f"and direct expression."),
        "realism": REALISMO,
        "aspect_ratio": "9:16 vertical",
        "negative": NEG,
    }
    return [dict(codigo="K01", take="T1 a T15", titulo="mãos juntas na mesa de vidro, celular apoiado", j=j)]


def videos(a):
    n = a["nome"]
    art = "o avatar" if a["genero"] == "homem" else "a avatar"
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        txt = (f"{art} {n} ({a['genero']}) fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, em tom de "
               f"conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, "
               f"{EMOCAO[t]}, no mesmo ritmo do vídeo modelo, a seguinte frase: \"{FALAS[t]}\"\n\n"
               f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
               f"sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
               f"o que acontece no vídeo: {ACAO.get(t, ACAO_PADRAO).format(n=n)}\n\n"
               "câmera: celular apoiado na mesa de vidro, fixo, sem movimento\n\n"
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
        "1. Clipes numerados na ordem: V01 a V15.",
        "2. Zero tempo morto: todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / "
        "Keep Vocal no áudio. Todos saem do mesmo frame, então a troca de clipe vira jump cut no mesmo enquadramento, "
        "a gramática do próprio formato orgânico.",
        "3. Legenda branca em negrito itálico caixa alta, 2 a 3 palavras por vez, na linha da borda da mesa de vidro, "
        "do V01 ao V15, igual ao modelo.",
        "4. \"222\" pequeno à esquerda e \"111\" pequeno à direita, o vídeo inteiro.",
        "5. No V15, seta vermelha para baixo à esquerda (foto de perfil, onde fica o follow), em \"follow me\".",
        "6. Sem Voice Changer: a voz vem do prompt de cada V.",
        "7. Música só depois do gancho (a partir do V02), baixa, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "8. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# {a['nome']} | Auraly Growth Mãos no Vidro | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `/Users/macbookairm2/Downloads/snapinsta-1790816368613.mp4` (100,1 s, pessoa real)", "",
         f"Âncora: `{a['ancora']}`", "",
         "Funil: growth, save + double tap + `222` + follow. Origem orgânica, rodada de validação.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|",
         f"| T1 a T15 | K01 | ÂNCORA {a['nome'].upper()} + FRAME DO MODELO (K01) | GERAR DO ZERO |", "",
         "## Trava de identidade e continuidade", "",
         f"- Identidade: {a['identidade']}", f"- Roupa (fixa da conta): {a['roupa']}",
         f"- Cenário-base (fixo da conta): {a['cena']}", f"- Luz: {a['luz']}",
         f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.", "- Sem 2ª pessoa.", "",
         "## Trava do prop herói", "", "- Não há prop: o herói são as mãos juntas sobre a mesa de vidro.", "",
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


CHECKLIST = ("Checklist de envio: 33/33 aprovados (N/A: A1, A2, A4, A7, A10 fiéis ao modelo orgânico; C3 sem segunda "
             "pessoa; C4 celular apoiado, sem selfie na mão; C6 sem cena atuada; C7 sem motion control)")
FICHA = "Ficha: 1/1 K conferido contra o frame do modelo, placar 14/14 (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)"


def entrega(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Growth Mãos no Vidro", "",
         "Produção `auraly_growth_maos_vidro` · Ângulo 3 · GROWTH · vídeo modelo de pessoa real (orgânico) · rodada de VALIDAÇÃO · perfil AURALY", "",
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
    print("ok: %d avatar(es), Flow v%s" % (len(AVATARES), VERSAO))


if __name__ == "__main__":
    main()
