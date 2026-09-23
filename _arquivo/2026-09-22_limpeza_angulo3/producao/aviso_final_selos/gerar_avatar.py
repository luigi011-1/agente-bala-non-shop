"""Gera os 5 CENARIO_*.md de um avatar a partir do ROTEIRO.md aprovado. Uso: python3 gerar_avatar.py <id>"""
import json, re, sys, os
BASE = "producao/aviso_final_selos"
AVS = {
 "02_cabelo_prateado_camisa_azul": dict(
  ident=("The EXACT man from the attached fingerprint sheet: white man in his early sixties, thick wavy silver-grey hair "
         "of medium length swept back from the forehead with loose waves over the ears, short grey stubble on the jaw, "
         "light blue-grey eyes, tanned sun-weathered skin with freckles and visible pores, deep lines on the forehead and "
         "around the eyes, straight long nose, lean build."),
  acc="a steel watch with a green dial on a dark brown leather strap on the left wrist and a braided brown leather bracelet",
  lock=("Homem branco de sessenta e poucos anos, cabelo prateado grosso e ondulado de comprimento medio penteado para tras, "
        "barba curta grisalha por fazer, olhos azul-acinzentados, pele bronzeada com sardas. Relogio de mostrador verde "
        "com pulseira de couro marrom e pulseira de couro trancada no pulso esquerdo em todos os cenarios."),
  wards=["Light blue linen button-up shirt, sleeves rolled to the forearm, top two buttons open",
         "White linen button-up shirt, sleeves rolled to the forearm, top button open",
         "Navy crew-neck cotton sweater with the sleeves pushed to the forearm",
         "Plain heather grey crew-neck cotton t-shirt",
         "Beige cotton button-up shirt, sleeves rolled to the forearm, top button open"],
  gram="silver hair"),
 "03_dreads_loiros_longos_jeans": dict(
  ident=("The EXACT man from the attached fingerprint sheet: Black man in his late thirties, very long platinum blonde "
         "locs falling past the chest with darker roots at the scalp, full thick black beard neatly trimmed with a "
         "moustache, dark brown eyes, deep brown skin with visible pores, strong jaw, broad athletic build."),
  acc="a thin silver chain necklace",
  lock=("Homem negro de trinta e muitos anos, dreads longos loiro-platinados passando do peito com raiz escura, barba cheia "
        "preta aparada, olhos castanho-escuros, pele marrom escura, porte atletico. Corrente de prata fina no pescoco em "
        "todos os cenarios."),
  wards=["Dark indigo linen button-up shirt, sleeves rolled to the forearm, top two buttons open",
         "Plain black crew-neck cotton t-shirt",
         "Olive green cotton overshirt worn open over a white crew-neck t-shirt",
         "Plain white crew-neck cotton t-shirt",
         "Light grey linen button-up shirt, sleeves rolled to the forearm, top button open"],
  gram="locs"),
 "04_dreads_loiros_medios_verde": dict(
  ident=("The EXACT man from the attached fingerprint sheet: Black man in his early thirties, shoulder-length locs that "
         "are black at the roots and fade to sandy blonde at the ends, short neatly trimmed beard and goatee, brown eyes, "
         "medium brown skin with visible pores and faint freckles, slim lean build, small silver hoop earrings."),
  acc="a black cord necklace with a small stone pendant",
  lock=("Homem negro de trinta e poucos anos, dreads na altura dos ombros pretos na raiz e loiro-areia nas pontas, barba curta "
        "aparada com cavanhaque, olhos castanhos, porte magro, argolas pequenas de prata. Cordao preto com pingente de pedra "
        "em todos os cenarios."),
  wards=["Olive green cotton button-up shirt worn open over a white tank top, sleeves rolled to the forearm",
         "Plain charcoal grey crew-neck cotton t-shirt",
         "Faded denim button-up shirt, sleeves rolled to the forearm, top two buttons open",
         "Plain white crew-neck cotton t-shirt",
         "Rust brown linen button-up shirt, sleeves rolled to the forearm, top button open"],
  gram="locs"),
}
av = sys.argv[1]; A = AVS[av]
FP = f"{BASE}/fingerprints/{av}.jpg"
rot = open(f"{BASE}/ROTEIRO.md").read()
falas = {m.group(1): m.group(2) for m in re.finditer(r"^### (T\d+) .*?\n> \"(.+?)\"$", rot, re.M)}
assert len(falas) == 13
REF = ("Use the attached fingerprint sheet ONLY for the man's face, identity, body and skin. Do NOT copy its "
       "clothing, background, pose, framing or lighting.")
REAL = ("UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows "
        "and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty "
        "smoothing, no blur anywhere, everything in sharp focus including the background.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, "
       "no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no seated pose")
LC = "Flat neutral overcast daylight from the kitchen window, cool and even, no warm cast."
LB = "Flat neutral overcast daylight from a frosted bathroom window, cool and even, no warm cast."
BR = "a pair of plain red cotton men's boxer briefs"
CARD = ("a vertical tarot card with saturated illustrated art of a couple embracing under a starry deep blue night sky, "
        "red roses in the corners, a band across the bottom with the word SOULMATE in gold capital letters, and a mirrored "
        "metallic border with rainbow holographic reflections around the whole edge")
VAS = "a large open white tub of petroleum jelly"
CV = "a thick transparent film of petroleum jelly, glossy and heavy, with a single long clear strand hanging from its bottom edge toward the pot"
CEN = [
 dict(n=1, slug="carta_vaselina", hook="HOOK 1", var="OBJETO", nome="A carta SOULMATE mergulhada", room="k", pote=VAS,
      sub="vaselina", tipo="card", obj=CARD, opt="a carta", coat=CV),
 dict(n=2, slug="mel", hook="HOOK 5", var="SUBSTANCIA", nome="Mel ambar no lugar da vaselina", room="k",
      pote="a large wide open glass jar of thick amber honey", sub="mel", tipo="cloth", obj=BR, opt="a peça",
      coat="thick glossy amber honey, heavy, with a single long golden strand of honey hanging from its bottom edge toward the pot"),
 dict(n=3, slug="cera_vermelha", hook="HOOK 6", var="SUBSTANCIA", nome="Cera vermelha derretida", room="k",
      pote="a wide open metal tin of melted glossy red candle wax", sub="cera", tipo="cloth", obj=BR, opt="a peça",
      coat="a layer of red candle wax that is starting to set, with a single thick red strand of wax stiffening in the air below its bottom edge toward the pot"),
 dict(n=4, slug="banheiro", hook="HOOK 8", var="LOCAL", nome="O mesmo gesto no banheiro", room="b", pote=VAS,
      sub="vaselina", tipo="cloth", obj=BR, opt="a peça", coat=CV),
 dict(n=5, slug="alianca", hook="HOOK 2", var="OBJETO", nome="A alianca que sai do pote", room="k", pote=VAS,
      sub="vaselina", tipo="ring", obj="a plain polished gold wedding band", opt="a aliança",
      coat="a thick transparent film of petroleum jelly, glossy, with a single long clear strand hanging from it toward the pot"),
]
FLAG = "a small United States flag on a short desk stand"
def sh(c):
    if c["room"] == "b":
        return ("A real lived-in American bathroom with white tiled walls. A portable single-burner camping stove resting on the "
                f"wide edge of the bathtub in front of him with a steel pot of water at a rolling boil, {c['pote']} resting on the "
                f"tub edge beside the pot, and {FLAG} on the sink counter behind him, fully in focus and unobstructed.")
    return ("A real lived-in American home kitchen. A gas stove directly in front of him with a steel pot of water at a rolling "
            f"boil, {c['pote']} resting on the stovetop beside the pot, and {FLAG} on the windowsill behind him, fully in focus and unobstructed.")
def sb(c):
    kit = ("a worn tarot deck, a raw rose quartz crystal, a lit incense stick with a thin smoke line and a white pillar candle")
    if c["room"] == "b":
        return ("The same real lived-in American bathroom with white tiled walls. A portable single-burner camping stove on the wide "
                "edge of the bathtub in front of him with a steel pot of water at a rolling boil sending up visible steam. On the "
                f"bathroom shelf beside him {kit}. On the tiled wall behind him a small dark wooden cross and {FLAG}, both fully in focus and unobstructed.")
    return ("The same real lived-in American home kitchen. A gas stove in front of him with a steel pot of water at a rolling boil "
            f"sending up visible steam. On the counter beside him a short shelf holding {kit}. On the wall behind him a small dark "
            f"wooden cross and {FLAG}, both fully in focus and unobstructed.")
def cont(c):
    return re.sub(r"^a (large wide open|large open|wide open) ", "the open ", c["pote"])
def k(c, i):
    w = f"{A['wards'][c['n']-1]}, {A['acc']}."
    if i == 1:
        if c["tipo"] == "ring":
            comp = "Chest-up in the upper half of the frame. His right hand, the ring and the open tub fill the lower foreground, closer to the lens than his face. Nothing else in frame."
            st = f"Start frame: he holds {c['obj']} upright between his right thumb and index finger, about ten centimetres directly above {cont(c)}, his fingers about to sink into it. The ring is completely clean."
        elif c["tipo"] == "card":
            comp = "Chest-up in the upper half of the frame. His two hands and the tarot card fill the lower foreground, closer to the lens than his face, directly above the open tub. Nothing else in frame."
            st = f"Start frame: he holds a tarot card flat between both hands, horizontally, about twenty centimetres directly above {cont(c)}, not yet touching it. The card is completely clean and dry. The card is {c['obj']}."
        else:
            comp = "Chest-up in the upper half of the frame. His two hands and the garment fill the lower foreground, closer to the lens than his face, directly above the open container. Nothing else in frame."
            st = f"Start frame: he holds {c['obj']} spread open between both hands, about twenty centimetres directly above {cont(c)}, not yet touching it. The garment is completely clean and dry."
        return {"shot_id": f"C{c['n']}_T1_hook_initial", "reference_use": REF, "identity_main": A["ident"], "wardrobe": w,
                "scene": sh(c), "posture": "Standing upright, leaning slightly forward over the container, chin down, eyes on his own hands, mouth closed.",
                "composition": comp, "camera": "chest level, angled slightly down toward the container", "state": st,
                "lighting": LB if c["room"] == "b" else LC, "realism": REAL, "aspect_ratio": "9:16 vertical", "negative": NEG}
    nom = {"ring": "the ring", "card": "the tarot card", "cloth": "the garment"}[c["tipo"]]
    hold = "between thumb and index finger " if c["tipo"] == "ring" else ""
    st = f"Start frame: speaking directly to camera while holding {nom} steady above the pot. {nom[0].upper()+nom[1:]} is now fully coated in {c['coat']}."
    if c["tipo"] == "card":
        st += f" The card is {c['obj']}."
    if c["tipo"] == "cloth":
        st = f"Start frame: speaking directly to camera while holding {c['obj']} steady above the pot. The garment is fully coated in {c['coat']}."
    return {"shot_id": f"C{c['n']}_T2_T14_body", "reference_use": REF, "identity_main": A["ident"], "wardrobe": w,
            "scene": sb(c), "posture": "Standing upright, squared to the camera, chin up, speaking directly to the lens with a calm confidential expression.",
            "composition": f"Chest-up, filling the upper half of the frame. His right hand holds {nom} up {hold}in the lower foreground, closer to the lens than his face, suspended above the boiling pot. Nothing else in frame.",
            "camera": "eye level, straight-on", "state": st, "lighting": LB if c["room"] == "b" else LC,
            "realism": REAL, "aspect_ratio": "9:16 vertical", "negative": NEG}
G = {"T2": "fala direto para a câmera segurando {o} parada acima da panela", "T3": "fala direto para a câmera e leva o indicador livre até os lábios uma vez",
     "T4": "fala direto para a câmera e balança a cabeça devagar em negativa", "T5": "fala direto para a câmera e aponta o indicador livre para a lente",
     "T6": "fala direto para a câmera e levanta dois dedos da mão livre", "T7": "fala direto para a câmera e olha um instante para cima antes de voltar à lente",
     "T8": "fala direto para a câmera e ergue {o} um pouco mais perto da lente", "T9": "fala direto para a câmera e ergue as sobrancelhas uma vez",
     "T10": "fala direto para a câmera e franze a testa na segunda metade da frase", "T11": "fala direto para a câmera e conta três dedos na mão livre",
     "T12": "fala direto para a câmera e aponta o indicador livre para baixo", "T13": "fala direto para a câmera e assente uma vez com a cabeça",
     "T14": "fala direto para a câmera e aponta o indicador livre para cima, na direção do topo da tela"}
def som(c): return "banheiro azulejado, água fervendo e eco leve" if c["room"] == "b" else "cozinha, água fervendo"
def v1(c):
    em = {"vaselina": "na vaselina", "mel": "no mel", "cera": "na cera"}[c["sub"]]
    pote = {"vaselina": "vaselina", "mel": "mel", "cera": "cera vermelha derretida"}[c["sub"]]
    if c["tipo"] == "ring":
        a = (f"ele afunda a mão com a aliança por inteiro dentro do pote de {pote}, corta para um macro fechado da mão no instante em que os dedos entram {em}, "
             "corta para um macro da aliança sendo puxada coberta com um fio longo e transparente escorrendo dela, e corta de volta para ele de pé segurando a aliança acima da panela fervendo")
    else:
        o = c["opt"]; oo = "a carta" if c["tipo"] == "card" else "a peça"
        a = (f"ele baixa {oo} e a afunda por inteiro dentro do pote de {pote}, corta para um macro fechado das duas mãos no instante em que {oo} entra {em}, "
             f"corta para um macro d{oo} sendo erguida coberta com um fio longo escorrendo dela, e corta de volta para ele de pé segurando {oo} acima da panela fervendo")
    return ("(sem fala no take: o take do gancho e mudo, exatamente como no video modelo)\n\n"
            f"o que acontece no vídeo: {a}\n\ncâmera: cortes internos ao clipe, três mudanças de plano, câmera fixa em cada uma\n\n"
            f"som ambiente: {som(c)} e o chiado do fogo, sem música")
def vf(c, t):
    return ("o avatar (homem) fala em inglês com sotaque americano, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, "
            f"a seguinte frase: \"{falas[t]}\"\n\no avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. "
            f"Lip sync perfeito durante todo o vídeo.\n\no que acontece no vídeo: ele {G[t].format(o=c['opt'])}\n\ncâmera: fixa\n\nsom ambiente: {som(c)}, sem música")
MAPA = "MAPA K/V\nV01: K01\n" + "\n".join(f"V{i:02d}: K02" for i in range(2, 15))
os.makedirs(f"{BASE}/{av}", exist_ok=True)
chat = []
for c in CEN:
    ka, kb = k(c, 1), k(c, 2)
    vs = [("V01", "T1", "K01", v1(c))] + [(f"V{i:02d}", f"T{i}", "K02", vf(c, f"T{i}")) for i in range(2, 15)]
    L = [f"# CENARIO {c['n']} - {c['nome']} · {av}", "", "Producao: `aviso_final_selos` · Angulo 3 / Auraly · Objetivo GROWTH",
         f"Gancho: {c['hook']} do `GANCHOS_VISUAIS.md` · Variavel trocada: `{c['var']}`", f"Fingerprint: `{FP}`", "",
         "## Indice de geracao", "", "| Take | Keyframe | Anexo | Acao de geracao |", "|---|---|---|---|",
         "| T1 (mudo) | K01 | 1 imagem: a fingerprint | 🆕 GERAR DO ZERO |", "| T2 a T14 | K02 | 1 imagem: a fingerprint | 🆕 GERAR DO ZERO |", "",
         "## MAPA K/V", "", "```text", MAPA, "```", "", "## Trava de identidade e continuidade", "", A["lock"], "", "---", ""]
    for kid, kj, ex in (("K01", ka, ""), ("K02", kb, "\n> 🚫 NUNCA anexar o K01 aqui")):
        L += [f"## {kid}", "", "> ### 📎 ANEXAR: **1 IMAGEM**", f"> **1️⃣ FINGERPRINT** `{FP}`", ">", "> ### 🆕 GERAR DO ZERO" + ex, "",
              "```json", json.dumps(kj, ensure_ascii=False, indent=2), "```", ""]
    L += ["---", "", "## Bloco global de video (colar em todo prompt V)", "",
          "Veo 3.1 Lite · Lower Priority · 8 segundos · 3 variacoes por codigo · INITIAL FRAME conforme o MAPA K/V.", ""]
    for vid, t, kk, txt in vs:
        L += [f"## {vid} · {t} · usa {kk}", "", "```text", txt, "```", ""]
    L += ["---", "", "## Montagem no CapCut", "", "1. `V01` abre o video com o texto de tela `This is your last warning!`.",
          "2. `V02` a `V14` na ordem, cortando o respiro entre takes.", "3. Legenda karaoke branca com a palavra falada em amarelo.",
          "4. No `V14`, seta para o topo da tela.", "5. Sem musica.", "", "## Gates de qualidade", "",
          "1. Heroi no lower foreground. ✅", "2. Bandeira dos EUA visivel nos dois K. ✅", "3. Luz neutra, negative anti tom quente. ✅",
          "4. `no captions`, sem termo sensivel. ✅", "5. Registro divino, rosto da alma gemea nunca aparece. ✅", "6. Fala literal do ROTEIRO.md. ✅", ""]
    p = f"{BASE}/{av}/CENARIO_{c['n']}_{c['slug']}.md"; open(p, "w").write("\n".join(L))
    chat.append(f"## CENÁRIO {c['n']} · {c['nome']} · `{c['var']}`\n\n**BLOCO DE IMAGEM**\n\n```\nK01\n{json.dumps(ka, ensure_ascii=False, separators=(',', ':'))}\n\nK02\n{json.dumps(kb, ensure_ascii=False, separators=(',', ':'))}\n```\n\n**BLOCO DE VÍDEO**\n\n```\n" + "\n\n".join(f"{v}\n{x}" for v, _, _, x in vs) + "\n```\n")
open(f"{BASE}/{av}/_CHAT.md", "w").write("\n---\n\n".join(chat))
print("ok", av)
