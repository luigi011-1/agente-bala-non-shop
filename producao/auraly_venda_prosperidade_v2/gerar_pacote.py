"""Gera os pacotes por avatar da producao auraly_venda_prosperidade_v2 (Auraly, venda, dinheiro e prosperidade, validacao, avatar IA).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco). Regra do Luigi de 2026-10-06: o K so anexa o character sheet do
avatar e o V so anexa a imagem escolhida; cenario, camera, pose e acao do modelo vao por extenso dentro de cada prompt.
Mapa K/V: um unico plano no modelo, entao K01 -> V01 a V13. Saidas por avatar: PROMPTS_, FLOW_ e ENTREGA_<AVATAR>.md,
mais AGENTE_FLOW.md e FICHA_FRAMES.md da producao. Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")
HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 14)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES), FALAS.keys()
PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$", ROTEIRO.split("## Tradução completa")[1].split("\n## ")[0], re.M))
assert set(PT) == set(TAKES), PT

MAPA = {"V%02d" % i: "K01" for i in range(1, 14)}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
MIC = ("a small black wireless lavalier microphone about two and a half inches long, pinched between the thumb and index "
       "finger, its tip pointing up toward the chin")
LUZ = ("Neutral overcast daylight coming through the car windows, the outside clearly visible through the window under a "
       "grey-blue overcast sky with visible cloud texture, never white or blown out, soft even light on the face and hands "
       "with no harsh shadows.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no numbers overlaid on the image, no glowing numbers, "
       "no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no glowing "
       "aura, no sparkles, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the "
       "skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic "
       "lighting, no second person in frame, no other objects in the hands, no phone in frame")

CARRO = ("The rear passenger seat of an ordinary luxury sedan seen from across the car at chest height: a cream leather "
         "bench seat with a tall quilted headrest at the left, a pale beige headliner with the edge of a sunroof and a "
         "grab handle at the top, and at the right the rear door window showing green palm trees and a white stone gate "
         "pillar with a small American flag on a short pole beside it, discreet but visible and in focus. At the lower "
         "right a dark wood door armrest, and a silver door-pull at the lower left.")
PHANTOM = ("The rear passenger seat of a Rolls-Royce Phantom parked in front of a mansion, seen from across the car at "
           "chest height: an ivory leather bench seat with a deep tufted headrest at the left, a pale grey headliner with a "
           "sunroof edge at the top, polished open-pore wood trim on the door armrest at the lower right, and at the right "
           "the rear door window showing a white limestone mansion with tall columns, palm trees and a stone gate pillar "
           "with a small American flag on a short pole beside it, discreet but visible and in focus.")

AVATARES = [
    dict(nome="Avery Knox", arquivo="AVERY_KNOX", genero="mulher", pron="She", pos="her", cena=CARRO,
         sheet="producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg",
         identidade=("The exact fictional AI character Avery Knox: white American woman around sixty, voluminous shaggy "
                     "layered platinum-blonde hair with darker roots, brown eyes, fair skin with crow's feet and fine "
                     "lines, everyday makeup with defined brows, mascara and soft pink lipstick."),
         roupa=("White long-sleeve button-up shirt with the cuffs loosely rolled to the forearms, blue bootcut jeans, a "
                "large turquoise and silver squash-blossom necklace, several big turquoise rings, and a silver cuff "
                "bracelet set with turquoise."),
         maos="her fair hands with big turquoise rings and the silver turquoise cuff bracelet below the rolled white cuffs",
         voz="voz feminina quente e firme, levemente rouca, de uma mulher de sessenta anos"),
    dict(nome="Devon Price", arquivo="DEVON_PRICE", genero="mulher", pron="She", pos="her", cena=CARRO,
         sheet="producao/_ancoras/character_sheets/devon_price_character_sheet.jpg",
         identidade=("The exact fictional AI character Devon Price: white American woman around fifty with a completely "
                     "bald smooth head, hazel eyes, freckles across the face and scalp, fine lines, no makeup and no wig."),
         roupa=("Cream lace blazer over a cream lace camisole, a thin silver chain necklace with a small heart pendant, "
                "small silver stud earrings, a rose-gold beaded bracelet, thin silver rings, and blue skinny jeans."),
         maos="her freckled fair hands with thin silver rings and the rose-gold beaded bracelet below the lace cuffs",
         voz="voz feminina calma e direta, de uma mulher de cinquenta anos"),
    dict(nome="Jordan Vale", arquivo="JORDAN_VALE", genero="homem", pron="He", pos="his", cena=PHANTOM,
         sheet="producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg",
         identidade=("The exact fictional AI character Jordan Vale, explicitly male: very rich white American man around "
                     "sixty-eight, slim, full silver-white hair swept back, thin round gold-rimmed glasses, light blue-grey "
                     "eyes, age spots, freckles and deep forehead lines."),
         roupa=("Cream dinner jacket over a crisp white shirt with a black bow tie, black tuxedo trousers, a gold "
                "wristwatch on the left wrist and a gold ring."),
         maos="his slim aged hands with a gold ring and the gold wristwatch below the cream cuff",
         voz="voz masculina grave, calma e distinta, de um homem de sessenta e oito anos"),
]

ACAO = {
    "T1": "{n} olha firme para a lente e fala com a mão do microfone parada perto do peito, a outra mão pousada na coxa, um leve aceno de cabeça na última frase.",
    "T2": "{n} balança a cabeça de leve ao dizer que não é azar, e a mão livre sobe da coxa e conta os itens no ar, voltando para a coxa no fim.",
    "T3": "{n} fala em tom de lembrança, o olhar firme na lente, a mão do microfone parada, a mão livre aberta e baixa sobre a coxa.",
    "T4": "{n} faz uma pausa curta, ergue as sobrancelhas ao dizer que as bênçãos dela estavam chegando e aponta o indicador da mão livre para a lente em \"nobody was signing for them\".",
    "T5": "{n} inclina o corpo um pouco para a lente e abre a mão livre, a palma para cima, ao dizer \"three delivery attempts\".",
    "T6": "{n} fala calmo e certo, a mão livre desenha um arco curto no ar na imagem da tela de rastreio, o microfone parado.",
    "T7": "{n} olha para cima por um instante ao citar o arcanjo e volta para a lente, a mão livre aberta sobre o peito na palavra Seal.",
    "T8": "{n} ergue um dedo da mão livre ao dizer \"three seals\" e bate o polegar no ar na palavra \"like\", a outra mão segura o microfone parado.",
    "T9": "{n} mostra dois dedos da mão livre no segundo selo e aponta para si mesmo no terceiro, olhar firme na lente.",
    "T10": "{n} fica solene, aponta o indicador da mão livre para baixo no 222 e depois para a lente, sem sorrir.",
    "T11": "{n} suaviza a expressão ao contar a noite da Dolores, um meio sorriso leve no fim, a mão livre aberta sobre o peito.",
    "T12": "{n} olha direto para a lente, a mão livre aponta para a lente na primeira frase e abre no ar em \"I wish I'd known sooner\".",
    "T13": "{n} aponta o indicador da mão livre para baixo, em direção à foto de perfil, e depois para a lente, com leve sorriso de convite.",
}
EMOCAO = {
    "T1": "grave, em tom de aviso importante", "T2": "firme e confessional", "T3": "calma, como quem lembra uma história",
    "T4": "séria, com um tom de descoberta", "T5": "baixa e confidencial, como quem conta um segredo", "T6": "calma e certa",
    "T7": "reverente e firme", "T8": "firme e urgente", "T9": "firme e convicta", "T10": "grave e solene, em tom de aviso",
    "T11": "mais suave e aliviada", "T12": "próxima e urgente", "T13": "calorosa e firme, em tom de convite",
}
MASC = {"convicta": "convicto", "certa": "certo", "calma": "calmo", "aliviada": "aliviado", "baixa": "baixo",
        "reverente": "reverente", "próxima": "próximo", "calorosa": "caloroso", "séria": "sério", "firme": "firme",
        "urgente": "urgente", "confidencial": "confidencial", "confessional": "confessional", "suave": "suave",
        "mais": "mais", "muito": "muito", "grave": "grave", "solene": "solene"}
SOM = "interior silencioso de carro de luxo parado, leve eco natural da voz, ruído suave de tecido e de couro do banco, sem música"


def emocao(t, homem):
    e = EMOCAO[t]
    return re.sub(r"\w+", lambda m: MASC.get(m.group(0), m.group(0)), e) if homem else e


def keyframe(a):
    n, P, p = a["nome"], a["pron"], a["pos"]
    ref = (f"Use the attached character sheet only for {n}'s exact identity (face, skin, hair, body), wardrobe and "
           f"jewelry; ignore its grey studio background. The setting, camera angle, pose and action are fully "
           f"described in this prompt.")
    j = {
        "fiction_note": FICCAO, "reference_use": ref, "identity_main": a["identidade"], "wardrobe": a["roupa"],
        "scene": a["cena"],
        "prop": (f"In {p} right hand, raised to chest height and held out in front of the torso, {n} pinches {MIC}; the "
                 f"microphone and hand are in the lower foreground about 26 inches from the lens, closer to the camera "
                 f"than {p} face, and they take up about 8 percent of the frame. {p.capitalize()} left hand rests open on "
                 f"{p} left thigh. Nothing else is held in either hand."),
        "posture": (f"{n} sits upright in the middle of the rear seat with the torso turned straight toward the lens, "
                    f"shoulders relaxed, looking straight into the lens, caught mid-sentence, lips naturally parted, "
                    f"animated expression; {a['maos']}."),
        "composition": (f"{n} fills the frame from the top of the head, about 15 percent from the top edge, down to the "
                        f"thighs at the bottom edge, centered slightly left, the face about 36 inches from the lens. The seat "
                        f"headrest fills the left, the car window the right. Nothing else is in frame. The background is "
                        f"reduced by framing, never by blur."),
        "camera": ("phone camera at the chest height of the seated person, 1x lens, level, fixed with a slight natural "
                   "handheld shake"),
        "lighting": LUZ,
        "state": f"Start frame: {n} is already looking into the lens, caught mid-sentence, microphone raised near the chest.",
        "realism": REALISMO, "aspect_ratio": "9:16 vertical", "negative": NEG,
    }
    return {"codigo": "K01", "take": "T1 a T13", "titulo": "corpo, sentado no banco de trás com o microfone de lapela na mão", "j": j}


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art = "o avatar" if h else "a avatar"
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        txt = (f"{art} {n} ({a['genero']}) fala em inglês com sotaque americano de {n}, {a['voz']}, em tom de gravação "
               f"direta para a câmera, natural e confiante, {emocao(t, h)}, a seguinte frase: \"{FALAS[t]}\"\n\n"
               f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
               f"sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
               f"o que acontece no vídeo: {ACAO[t].format(n=n)}\n\n"
               "câmera: fixa, na altura do peito de quem está sentado, com leve tremor natural de celular\n\n"
               f"som ambiente: {SOM}")
        vs.append((cod, t, MAPA[cod], txt))
    return vs


def texto_flow(j):
    ordem = ["fiction_note", "reference_use", "identity_main", "wardrobe", "scene", "prop", "posture",
             "composition", "camera", "lighting", "state", "realism", "aspect_ratio", "negative"]
    assert set(ordem) == set(j), set(j) ^ set(ordem)
    d = {"format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."}
    d.update({k: j[k] for k in ordem})
    return json.dumps(d, ensure_ascii=False, indent=2)


def mapa_kv():
    return ["MAPA K/V"] + [f"{v}: {k}" for v, k in MAPA.items()]


def capcut():
    return [
        "1. Clipes numerados na ordem: V01 a V13, todos saem do mesmo frame, então o enquadramento não muda, como no modelo (plano único).",
        "2. Jump cut a cada take, cortando logo depois da última palavra. Isolate Voice / Keep Vocal no áudio.",
        "3. Tarja fixa no topo o vídeo inteiro, branca, fonte grossa: \"DELIVERY ATTEMPT 3 OF 3\". Legenda karaokê branca grossa embaixo, palavra a palavra, como no modelo. Nada disso entra no K nem no V.",
        "4. Sem Voice Changer: a voz vem do prompt de cada V. Sem música no gancho; música baixa a partir do V02, fora da biblioteca do TikTok.",
        "5. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {PT[t]} |")
    return L


def pacote(a):
    k, vs = keyframe(a), videos(a)
    L = [f"# {a['nome']} | Auraly Venda Prosperidade v2 | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `input/modelo.mp4` (76,3 s, avatar IA: homem de túnica azul no banco de trás de um carro de luxo, plano único)", "",
         f"Character sheet: `{a['sheet']}`", "",
         "Funil: venda, dinheiro e prosperidade. 222 + primeiro nome, depois foto de perfil e Stories. Rodada de validação.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|",
         f"| T1 a T13 | K01 | CHARACTER SHEET {a['nome'].upper()} | GERAR DO ZERO |", "",
         "## Trava de identidade e continuidade", "",
         f"- Identidade: {a['identidade']}", f"- Roupa (a do character sheet): {a['roupa']}",
         f"- Cenário (o do modelo, versão {a['nome']}): {a['cena']}", f"- Luz: {LUZ}",
         f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano.", "- Sem 2ª pessoa.", "",
         "## Trava do prop herói", "", f"- Microfone: {MIC}.", "",
         "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "", "## Prompts de imagem", ""]
    L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · CHARACTER SHEET {a['nome'].upper()}", "",
          "> ### 📎 ANEXAR: **1 IMAGEM**", f"> **1️⃣ CHARACTER SHEET {a['nome'].upper()}** `{a['sheet']}`", ">",
          "> ### 🆕 GERAR DO ZERO", "", f"Cena: {k['titulo']}.", "", "```json", json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Montagem no CapCut", ""] + capcut() + [""]
    flow = [f"# Blocos limpos para o Google Flow | {a['nome']}", "", f"Fonte interna: `PROMPTS_{a['arquivo']}.md`", "",
            "```text"] + mapa_kv() + ["```", "", "## BLOCO DE IMAGEM", "", "```text", k["codigo"], texto_flow(k["j"]), "", "```", "",
            "## BLOCO DE VÍDEO", "", "```text"]
    for cod, _, _, txt in vs:
        flow += [cod, txt, ""]
    flow += ["```", "", "## Transcrição final por take", ""] + transcricao()
    return "\n".join(L) + "\n", "\n".join(flow) + "\n"


def entrega(a):
    k, vs = keyframe(a), videos(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Venda Prosperidade v2", "",
         "Produção `auraly_venda_prosperidade_v2` · Ângulo 3 · SALE (dinheiro e prosperidade) · rodada de VALIDAÇÃO · perfil AURALY", "",
         "Instruções do agente do Flow: `AGENTE_FLOW.md` desta produção (colado no chat).", "",
         "## Anexos e mapa", "",
         f"- **Imagem (K):** anexar SÓ o character sheet de {a['nome']} (`{a['sheet']}`) e colar o prompt. 4 variações, 9:16.",
         "- **Vídeo (V):** anexar SÓ a imagem escolhida daquele K e colar o prompt. 1 variação, 9:16.", "", "```text"] + mapa_kv() + [
         "```", "", "## 1. PROMPTS DE IMAGEM (um bloco por K)", "",
         f"### {k['codigo']} · {k['take']}, {k['titulo']} · anexar SÓ o CHARACTER SHEET", "", "```text", k["codigo"], texto_flow(k["j"]), "```", "",
         "## 2. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · anexar SÓ a imagem escolhida do {kcod}", "", "```text", cod, txt, "```", ""]
    L += ["## 3. Montagem no CapCut", ""] + capcut()
    L += ["", "## 4. Transcrição final por take", ""] + transcricao()
    L += ["", "## 5. Roteiro final em inglês", ""]
    for t in TAKES:
        L.append(f"{t[1:]}. {FALAS[t]}")
    L += ["", " ".join(FALAS[t] for t in TAKES), ""]
    return "\n".join(L)


FICHA = """# FICHA DO FRAME · auraly_venda_prosperidade_v2

Regra e método: `GATE_VISUAL.md` Parte 6. Cada K sai daqui. O frame do modelo manda no CONTEÚDO (forma, quadro,
distância, câmera, pose, cenário); o gate manda no ACABAMENTO e no piso de proximidade. Origem avatar IA: bandeira dos EUA
no cenário. Regra do Luigi de 2026-10-06: o frame NÃO é anexado; tudo o que está aqui vai por extenso no K.

## K01
Frame: `input/frames_modelo/K01_modelo.png`
Take: T1 a T13 (plano único do modelo, fala direta desde o frame 0, sem cortes)
Herói: microfone de lapela preto pequeno, pinçado entre polegar e indicador da mão direita perto do peito, e o rosto falando
Termos de forma: "small black wireless lavalier microphone" · "pinches"
Quadro: o avatar vai da cabeça (a ~15% do topo) até as coxas na borda de baixo; o microfone e a mão ocupam cerca de 8% do quadro
Distância da lente: rosto a uns 36 inches; microfone a uns 26 inches, mais perto que o rosto (o modelo tem o microfone mais ou menos no plano do peito, o gate pede mais perto)
Câmera: celular na altura do peito de quem está sentado, lente 1x, nivelada, fixa com leve tremor de mão
Pose: sentado reto no meio do banco de trás, torso virado para a lente; mão direita ergue o microfone, mão esquerda pousada aberta na coxa
Lista fechada: avatar, microfone, banco de couro creme, cabeceira, janela com palmeiras e portão, apoio de braço escuro; nada mais nas mãos
Frame 0: já olhando para a lente, no meio da frase, microfone perto do peito
Desvio (acabamento ou avatar fixo): túnica azul e homem do modelo viram o avatar do character sheet com a roupa dele; luz neutra de dia nublado e céu com textura (gate); pequena bandeira dos EUA no portão visto pela janela (formato IA); Jordan Vale no Rolls-Royce Phantom diante de uma mansão (regra do cenário do Jordan); tarja e legenda ficam só no CapCut
Cenário do modelo: banco de trás de sedã de luxo, couro creme com cabeceira acolchoada à esquerda, teto bege claro com borda de teto solar e alça, janela traseira à direita com palmeiras e pilar de pedra branca, apoio de braço escuro e puxador prateado embaixo

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "small black wireless lavalier microphone" · "pinches" |
| F2 quanto do quadro | OK | "about 8 percent of the frame" |
| F3 distancia da lente | OK | "about 26 inches from the lens" |
| F4 camera | OK | "1x lens" · "chest height" |
| F5 pose do avatar | OK | "sits upright in the middle of the rear seat" |
| F6 lista fechada | OK | "Nothing else is held in either hand" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "never white or blown out" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |
"""

AGENTE = """# Agente do Flow, produção atual: Auraly App, venda de prosperidade (vídeo 2)

Você é o executor do Google Flow. Você só gera imagens e vídeos a partir de prompts prontos. Você não cria, não edita e não melhora prompt.

## Produção atual
- Conta: Auraly App, vídeo de venda sobre prosperidade e dinheiro (auraly_venda_prosperidade_v2).
- Avatares: Avery Knox, Devon Price e Jordan Vale. Um avatar por vez, o que o operador disser que está ativo.
- Cada avatar tem 1 prompt de imagem (K01) e 13 prompts de vídeo (V01 a V13). Todo V usa a imagem escolhida do K01.

## O que é anexado (só isto, nada mais)
- IMAGEM (K01): você recebe o character sheet do avatar ativo. Anexe só ele e cole o prompt.
- VÍDEO (V): você recebe a imagem que o operador escolheu do K01. Anexe só ela e cole o prompt de vídeo.
- Não existe frame modelo, anchor, referência de cenário nem segunda imagem. O cenário, a pose, a câmera e a ação já estão escritos dentro de cada prompt. Pare só se faltar o character sheet (K) ou a imagem escolhida (V).

## Imagem (código K01)
1. Modelo: Nano Banana 2.1 (no menu: Pro, 2 Lite e 2.1; use só o 2.1). Formato: 9:16 vertical.
2. Gere 4 variações. Confira o 4 e o 9:16 antes de gerar, porque a tela volta sozinha para 1.
3. Cole o prompt inteiro, de `{` até `}`, sem o código K01, sem resumir, sem alterar uma palavra.
4. Nomeie as quatro: `K01-1`, `K01-2`, `K01-3`, `K01-4`.
5. Se saírem menos de 4, ou formato diferente de 9:16, gere de novo com o MESMO prompt e o MESMO character sheet até existirem 4 em 9:16.
6. Gere e PARE. Avise: "K01 pronto, 4 imagens. Aguardando sua escolha." Não escolha, não apague e não gere vídeo.
7. O operador apaga 3 e deixa 1 escolhida a dedo. Nunca questione e nunca recrie uma imagem apagada.

## Vídeos (códigos V01 a V13)
1. Só começa quando o operador mandar. Todo V usa a imagem que sobrou do K01. Se o K01 tiver mais de uma imagem ou nenhuma, pare e pergunte qual.
2. Modelo: Veo 3.1 - Lite (use só esse). Duração: 8 segundos. Formato: 9:16. Imagem entra como INITIAL FRAME, nunca como ingredient ou elemento.
3. Gere 1 variação por V. Confira o 1 antes de cada V.
4. O campo de texto recebe só o prompt V, inteiro, sem alterar uma palavra. Antes de enviar, confirme que ele contém `o que acontece no vídeo:`, `câmera:` e `som ambiente:`. Se faltar, é prompt de imagem: pare e avise.
5. No máximo 7 V por vez. Terminou o lote, relate e espere o operador dizer `prossiga`.

## Falhou, censura ou bloqueio
- Se a geração falhar, cair na censura, der erro ou o prompt for bloqueado: refaça com o MESMO prompt, sem trocar, cortar ou suavizar uma palavra, e tente de novo até aquele item sair.
- Não pare e não passe para o próximo item sem avisar qual está pendente. Se precisar seguir, diga: "V03 ainda pendente, tentativas: N."
- Você nunca reescreve prompt, mesmo que ache que ajudaria. Só o operador altera.
- Se a interface não permitir 9:16, 4 variações (imagem) ou 1 variação (vídeo), avise antes de mudar qualquer configuração.

## Relatório de status
Depois de cada K ou V, diga: avatar, código, resultado (pronto, tentando de novo, pendente) e quantas tentativas. No fim do lote, liste concluídos e pendentes. Geração de um avatar não conclui a fila: espere o operador dizer qual é o próximo avatar e anexe o novo character sheet. Nunca misture avatares.

## Regras gerais
- Não adicione música, legenda, texto ou tradução.
- A fala do prompt é literal. Não corrija nem complete.
- Em caso de dúvida real (pacote incompleto, código duplicado, anexo faltando), pare e pergunte em uma linha.
"""


def main():
    for a in AVATARES:
        p, f = pacote(a)
        (AQUI / f"PROMPTS_{a['arquivo']}.md").write_text(p, encoding="utf-8")
        (AQUI / f"FLOW_{a['arquivo']}.md").write_text(f, encoding="utf-8")
        (AQUI / f"ENTREGA_{a['arquivo']}.md").write_text(entrega(a), encoding="utf-8")
    (AQUI / "FICHA_FRAMES.md").write_text(FICHA, encoding="utf-8")
    (AQUI / "AGENTE_FLOW.md").write_text(AGENTE, encoding="utf-8")
    print("ok: %d avatares" % len(AVATARES))


if __name__ == "__main__":
    main()
