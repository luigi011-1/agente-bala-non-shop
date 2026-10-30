"""Pacotes do lote Sea Moss VENDA a partir de receitas virais (2026-10-15).
4 modelos (crosta_limao, intestino_chia, banana_canela, mascara_vaselina) x 3 avatares = 12 produções em
producao/<avatar>_seamoss_<receita>/. Textos aprovados em textos.py (mesma fonte do ROTEIRO.md).
Gerador comum: producao/_flow/pacote_minimo.py. Rodar da raiz:
python3 producao/seamoss_venda_lote_2026_10_15/gerar_pacotes.py
"""
import importlib.util
import os
import sys

D = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(D, "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "producao", "_flow"))
import pacote_minimo as PM  # noqa: E402

exec(open(os.path.join(D, "textos.py"), encoding="utf8").read())


def _avatar(pasta):
    spec = importlib.util.spec_from_file_location("g_" + pasta, os.path.join(RAIZ, "producao", pasta, "gerar_pacote.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.AVATAR


AV = {"meredith": _avatar("meredith_bolo_coco"), "marshall": _avatar("marshall_cheesecake_chocolate"),
      "cassidy": _avatar("cassidy_paes_batata_abacate")}
PRODUTO = "natural_rems_seamoss_produto.jpg"

# Take mudo: o V não leva fala (take-mudo-so-sem-voz). O resto segue o V padrão do pacote mínimo.
_v_padrao = PM.v_texto


def _v(fala):
    return MUDO_V if fala == "(no speech)" else _v_padrao(fala)


PM.v_texto = _v

MID = "She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression."
NEAR = "very close to the lens, large in frame and closer to the camera than her face"
TABLE = {"meredith": "the mint-green Formica table", "marshall": "the gray plank table", "cassidy": "the wooden workbench"}
OVEN = "a small electric countertop oven with its door open at the side of the table"
BURNER = "a single-burner portable stove on the table"
FREEZER = "a small open chest freezer beside the table, filled with frozen food bags and an ice tray"
POTE = ("the Natural Rems Sea Moss Gummies jar exactly as in the second attached image: a short wide jar of dark amber plastic "
        "with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves, the "
        "big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, and the line GREEN APPLE FLAVOR")
REF_POTE = "Second image: front jar only."


def k_pote(prop_extra=""):
    return (f"Hero: she holds {POTE} in her right hand out toward the camera, {NEAR}, label fully readable, fingers on the "
            f"sides, held still.{prop_extra} {MID} {REF_POTE}")


def ficha_pote(frame):
    return (frame, "pote do Natural Rems Sea Moss, rótulo de frente, parado", "~25%", "colado",
            "segura o pote com a mão direita estendida para a câmera")


def sem_pessoa(a, hero):
    """K sem avatar (boneco de açúcar sozinho): cenário da conta por escrito, nenhum anexo."""
    cen = AV[a]["set"].replace("She stands behind", "The scene is set behind", 1).replace("behind her", "behind it")
    return {"raw": (f"{hero} {cen} {PM.CAM} Soft neutral even daylight, true neutral colors, crisp crystal texture, "
                    "smartphone footage look, everything in sharp focus, 9:16 vertical."), "anexos": ["-"]}


# --------------------------------------------------------------------------- K por vídeo
TROUGH = ("a long narrow clear acrylic trough, tapered like a teardrop and tilted toward the camera, packed with a thick dry "
          "dark-brown crust that is deeply cracked like dried mud, resting on a clear plastic storage bin")
GUT = ("A large hollow clear plastic teaching model of the human intestinal tract, as tall as her torso: a thick "
       "pouched outer tube around the sides and top, narrow winding loops in the middle, a short funnel neck at the top, "
       "all packed with a speckled brown grain mixture")


def ks_crosta(a):
    t = TABLE[a]
    return {
     1: ("Gancho: calha transparente com crosta escura rachada colada na lente; ela despeja água com rodelas de limão por cima.",
         f"Hero: in the lower foreground, {NEAR}: {TROUGH}. She tips a clear glass pitcher of water with thin lemon slices "
         f"floating in it, a stream of lemon water splashing onto the cracked crust and running off without softening it. {MID}",
         ("0,0 a 7,5s (cena 1, água de limão na crosta)", "calha transparente com crosta escura rachada + jarra de água com limão",
          "~55%", "colada", "atrás da calha, inclina a jarra com a mão direita")),
     2: ("A mesma calha com a crosta molhada por cima; ela polvilha fibra em pó branca com uma colher medidora.",
         f"Hero: in the lower foreground, {NEAR}: {TROUGH}, a thin film of lemon water pooled on top of the crust. She holds a "
         f"white plastic measuring scoop and shakes a dusting of white fiber powder onto the cracked crust, the powder sitting "
         f"on the surface. {MID}",
         ("7,5 a 11,5s (cena 1, fibra em pó)", "calha com crosta + colher medidora de fibra em pó", "~55%", "colada",
          "colher medidora erguida sobre a calha")),
     3: ("Payoff: ela despeja o líquido amarelo-alaranjado da receita na calha e a crosta começa a amolecer e escorrer.",
         f"Hero: in the lower foreground, {NEAR}: {TROUGH}. She pours a thick stream of bright yellow-orange drink from a clear "
         f"glass pitcher onto the crust; where it lands the crust is darkening, softening and starting to slide down the "
         f"trough into the bin, a little yellow liquid already pooled in the bin below. {MID}",
         ("11,5 a 14,9s (cena 2, líquido amarelo derretendo a crosta)", "calha com crosta amolecendo + jarra de líquido amarelo",
          "~55%", "colada", "inclina a jarra com as duas mãos")),
     4: ("Panela de água fervendo no fogareiro colada na lente; ela solta pedaços de limão fresco picado dentro.",
         f"Hero: in the lower foreground, {NEAR}: a wide stainless steel pot of boiling water on {BURNER}. She drops a handful "
         f"of chopped fresh lemon pieces into the water from her cupped hand; a small cutting board with lemon halves rests on "
         f"{t}. {MID}",
         ("14,9 a 19,9s (cena 3, panela e limão)", "panela fervendo + pedaços de limão caindo", "~45%", "colada",
          "atrás da panela, solta o limão da mão em concha")),
     5: ("Close: colher de chia sobre a panela com pedaços de limão boiando.",
         f"Hero: in the lower foreground, {NEAR}: the stainless steel pot of steaming water with chopped lemon pieces floating. "
         f"She holds a teaspoon heaped with black chia seeds over the pot, a few seeds falling in. {MID}",
         ("19,9 a 21,6s (cena 4, chia)", "panela com limão + colher de chia", "~55%", "colada", "colher sobre a panela")),
     6: ("Close: colher de cúrcuma sobre a panela com limão e chia.",
         f"Hero: in the lower foreground, {NEAR}: the stainless steel pot of steaming water with lemon pieces and chia seeds. "
         f"She tips a teaspoon of bright orange turmeric powder into it, the powder spreading on the water. {MID}",
         ("21,6 a 24,4s (cena 5, cúrcuma)", "panela + colher de cúrcuma", "~55%", "colada", "inclina a colher")),
     7: ("Close: ela solta gengibre fresco ralado na panela; potinho de pimenta-do-reino ao lado.",
         f"Hero: in the lower foreground, {NEAR}: the pot of golden water with lemon pieces, chia and turmeric. Her fingers drop "
         f"a pinch of fresh grated ginger into it; a small dish of whole black peppercorns stands beside the burner. {MID}",
         ("24,4 a 26,5s (cena 6, gengibre)", "panela dourada + gengibre ralado caindo + potinho de pimenta", "~55%", "colada",
          "dedos soltando o gengibre")),
     8: ("Ela despeja a panela por um coador de metal dentro de um copo de vidro, colado na lente.",
         f"Hero: in the lower foreground, {NEAR}: a fine metal mesh strainer held over a tall clear glass. She tilts the "
         f"stainless steel pot, a stream of golden-orange drink with lemon pieces, chia and ginger pouring into the strainer, the "
         f"glass filling below. {MID}",
         ("26,5 a 28,6s (cena 7, coando)", "coador sobre o copo + panela despejando", "~55%", "colada", "inclina a panela")),
     9: ("Ela segura o copo alto de bebida dourada coada perto da lente.",
         f"Hero: she holds a tall clear glass of strained golden-orange drink with a few chia seeds suspended in it out toward "
         f"the camera in her right hand, {NEAR}. {MID}",
         ("28,6 a 41,9s (cena 8, copo na mão até o fim)", "copo alto de bebida dourada", "~25%", "colado",
          "segura o copo com a mão direita")),
     10: ("Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado.",
          k_pote(), ficha_pote("28,6 a 41,9s (o pote entra no lugar do copo para a ponte e o CTA)"),
          {"anexos": [AV[a]["anexo"], PRODUTO]}),
    }


def ks_intestino(a):
    t = TABLE[a]
    return {
     1: ("Gancho: ela segura o modelo transparente de intestino cheio de grãos colado na lente e despeja semente de chia pelo gargalo.",
         f"Hero: {GUT}. She holds it upright against her chest with her left hand, {NEAR}. With her right hand she tips a clear "
         f"glass measuring cup of black chia seeds into the funnel neck, a stream of seeds pouring in. {MID}",
         ("0,0 a 8,7s (cenas 1 a 3, chia entrando no modelo; o macro de 1s vira push-in dentro do V)",
          "modelo transparente de intestino cheio de grãos + copo de chia", "~65%", "colado",
          "segura o modelo contra o peito, despeja com a mão direita")),
     2: ("Ela despeja um copo de água com rodelas de limão pelo gargalo do modelo.",
         f"Hero: {GUT}. She holds it upright against her chest, {NEAR}. She tips a clear glass of water with lemon slices into the "
         f"funnel neck. {MID}",
         ("8,7 a 10,1s (cena 4, água de limão)", "modelo transparente + copo de água com limão", "~65%", "colado",
          "despeja com a mão direita")),
     3: ("Ela despeja um copo de suco de ameixa escuro pelo gargalo do modelo.",
         f"Hero: {GUT}. She holds it upright against her chest, {NEAR}. She tips a clear glass of dark purple-brown prune juice "
         f"into the funnel neck. {MID}",
         ("10,1 a 12,0s (cena 5, suco de ameixa)", "modelo transparente + copo de suco de ameixa", "~65%", "colado",
          "despeja com a mão direita")),
     4: ("Ela segura o modelo transparente parado com as duas mãos e fala para a câmera.",
         f"Hero: {GUT}. She holds it upright against her chest with both hands, {NEAR}, nothing pouring. {MID}",
         ("12,0 a 14,0s (cena 6, só o modelo)", "modelo transparente parado", "~65%", "colado", "segura com as duas mãos")),
     5: ("Ela despeja a bebida amarelo-dourada da receita pelo gargalo do modelo.",
         f"Hero: {GUT}. She holds it upright against her chest, {NEAR}. She tips a clear glass measuring cup of bright golden-yellow "
         f"drink into the funnel neck, the yellow liquid starting to run down into the first loop. {MID}",
         ("14,0 a 17,6s (cena 7, bebida amarela)", "modelo transparente + copo medidor de bebida amarela", "~65%", "colado",
          "despeja com a mão direita")),
     6: ("Panela de água no fogareiro colada na lente; ela espreme meio limão em cima.",
         f"Hero: in the lower foreground, {NEAR}: a stainless steel saucepan of water on {BURNER}. She squeezes half a fresh "
         f"lemon over it with her right hand, juice dripping in. {MID}",
         ("17,6 a 19,7s (cena 8, fogareiro)", "panela de água + meio limão espremido", "~45%", "colada",
          "atrás da panela, espreme o limão")),
     7: ("Close: colher de pau cheia de chia sobre a panela.",
         f"Hero: in the lower foreground, {NEAR}: the stainless steel saucepan of water on the burner. She holds a small wooden "
         f"spoon heaped with black chia seeds over it. {MID}",
         ("19,7 a 22,7s (cena 9, chia)", "panela + colher de pau com chia", "~55%", "colada", "colher sobre a panela")),
     8: ("Close: colher de gengibre fresco ralado sobre a panela com chia.",
         f"Hero: in the lower foreground, {NEAR}: the saucepan of water with chia seeds floating. She holds a spoon of fresh "
         f"grated ginger over it. {MID}",
         ("22,7 a 24,2s (cena 10, gengibre)", "panela com chia + colher de gengibre ralado", "~55%", "colada",
          "colher sobre a panela")),
     9: ("Close: ela mexe a panela já amarelo-alaranjada de cúrcuma com uma colher.",
         f"Hero: in the lower foreground, {NEAR}: the saucepan of bright golden-orange liquid with lemon and chia. She stirs it "
         f"with a metal spoon. {MID}",
         ("24,2 a 25,7s (cena 11, cúrcuma)", "panela amarelo-alaranjada + colher mexendo", "~55%", "colada", "mexe a panela")),
     10: ("Ela inclina a panela e despeja a bebida por um coador dentro de um copo de vidro.",
          f"Hero: in the lower foreground, {NEAR}: a fine metal strainer over a clear glass on {t}. She tilts the saucepan, "
          f"golden-orange drink pouring through the strainer into the glass. {MID}",
          ("25,7 a 26,7s (cena 12, coando)", "panela inclinada + coador + copo", "~50%", "colada", "inclina a panela")),
     11: ("Ela segura uma tábua redonda de madeira perto da lente com a caneca de chá e os ingredientes.",
          f"Hero: she holds a round wooden board out toward the camera with both hands, {NEAR}: on it a clear glass mug of "
          f"golden tea, half a lemon, a small mound of black chia seeds, a small pile of grated ginger and a small mound of "
          f"orange turmeric powder. {MID}",
          ("26,7 a 39,7s (cena 13, bandeja)", "tábua redonda com caneca, limão, chia, gengibre e cúrcuma", "~45%", "colada",
           "segura a tábua com as duas mãos")),
     12: ("Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado.",
          k_pote(), ficha_pote("39,7 a 47,0s (cena 14; o pote entra no lugar do livro)"),
          {"anexos": [AV[a]["anexo"], PRODUTO]}),
    }


def ks_banana(a):
    t = TABLE[a]
    return {
     1: ("Gancho: ela segura três bananas descascadas colada na lente e despeja canela de um potinho por cima.",
         f"Hero: she holds three peeled bananas side by side, peels folded down around the base, up toward the camera in her "
         f"left hand, {NEAR}, their tops already dusted with ground cinnamon. With her right hand she tips a small unlabeled "
         f"glass spice jar, a stream of reddish-brown cinnamon falling onto the bananas. {MID}",
         ("0,0 a 3,4s (cena 1, canela caindo)", "três bananas descascadas + potinho de canela despejando", "~60%", "colada",
          "segura as bananas com a esquerda, despeja com a direita")),
     2: ("Macro: as três bananas cobertas de canela empurradas quase encostando na lente, rosto dela atrás.",
         f"Hero: three peeled bananas thickly coated in ground cinnamon pushed right up to the lens, filling the lower two "
         f"thirds of the frame in extreme close-up, the cinnamon texture crisp; her face is partly visible just behind the "
         f"banana tips. {MID}",
         ("3,4 a 9,5s (cena 1, push-in até o macro)", "bananas com canela em macro", "~80%", "quase encostando",
          "empurra as bananas para a lente")),
     3: ("Ela segura uma colher de canela e uma banana sobre o copo vazio do liquidificador; meio limão e copo de água na mesa.",
         f"Hero: on {t} in the lower foreground, {NEAR}: an empty glass blender jar on its black base, half a lemon and a glass "
         f"of water beside it. She holds a peeled banana in one hand and a teaspoon of ground cinnamon in the other above the "
         f"jar. {MID}",
         ("9,5 a 12,8s (cena 2, liquidificador)", "liquidificador vazio + banana + colher de canela", "~40%", "colado",
          "banana e colher erguidas sobre o copo")),
     4: ("Close: banana dentro do copo do liquidificador; ela segura meio limão espremendo por cima.",
         f"Hero: in the lower foreground, {NEAR}: the glass blender jar with a peeled banana and a dusting of cinnamon inside. "
         f"She squeezes half a lemon over the jar with her right hand. {MID}",
         ("12,8 a 14,5s (cena 3, limão)", "copo do liquidificador com banana + meio limão", "~55%", "colado", "espreme o limão")),
     5: ("Ela despeja um copo de água no liquidificador com a banana.",
         f"Hero: in the lower foreground, {NEAR}: the glass blender jar with the banana and cinnamon inside. She pours a glass "
         f"of water into it. {MID}",
         ("14,5 a 15,9s (cena 4, água)", "liquidificador + copo de água despejando", "~50%", "colado", "despeja o copo")),
     6: ("Mão dela na tampa do liquidificador batendo, a vitamina bege girando, colado na lente.",
         f"Hero: in the lower foreground, {NEAR}: the glass blender with its lid on, a creamy beige banana smoothie swirling "
         f"inside. She presses the lid down with one hand. {MID}",
         ("15,9 a 18,2s (cena 5, batendo)", "liquidificador batendo a vitamina", "~50%", "colado", "mão na tampa")),
     7: ("Ela segura o copo alto de vitamina de banana perto da lente; liquidificador atrás.",
         f"Hero: she holds a tall clear glass of thick beige banana cinnamon smoothie out toward the camera in her right hand, "
         f"{NEAR}; the half-empty blender stands on {t} behind it. {MID}",
         ("18,2 a 27,9s (cena 6, copo na mão)", "copo alto de vitamina de banana", "~30%", "colado", "segura o copo")),
     8: ("Ela sentada num banco junto à mesa, segurando o copo de vitamina perto da lente.",
         f"Hero: she sits on a wooden stool beside {t}, relaxed, holding the tall glass of beige banana smoothie out toward the "
         f"camera, {NEAR}. {MID}",
         ("27,9 a 35,3s (cena 7, sentado com o copo)", "copo de vitamina", "~30%", "colado", "sentada, copo na mão direita")),
     9: ("Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado.",
         k_pote(), ficha_pote("27,9 a 35,3s (o pote entra no lugar do copo para o produto e o CTA)"),
         {"anexos": [AV[a]["anexo"], PRODUTO]}),
    }


def ks_mascara(a):
    t = TABLE[a]
    return {
     1: ("Gancho: ela despeja bicarbonato de uma caixa branca sem marca dentro de um pote aberto de vaselina sem marca, colado na lente.",
         f"Hero: she holds an open plain white tub of petroleum jelly with no label in her left hand, {NEAR}, the clear jelly "
         f"glistening inside. With her right hand she tips a plain white cardboard box with no printing, a stream of fine white "
         f"baking soda pouring into the tub. {MID}",
         ("0,0 a 6,8s (cena 1, varanda)", "pote de vaselina sem marca + caixa de bicarbonato despejando", "~40%", "colado",
          "segura o pote com a esquerda, despeja com a direita")),
     2: ("Tigela de vidro vazia na mesa colada na lente; ela segura uma colher de vaselina e outra de mel sobre ela.",
         f"Hero: on {t} in the lower foreground, {NEAR}: an empty clear glass bowl. She holds a spoon of clear petroleum jelly in "
         f"one hand and a spoon of golden honey in the other above the bowl. {MID}",
         ("6,8 a 10,1s (cena 2, colheres)", "tigela de vidro + colher de vaselina + colher de mel", "~45%", "colada",
          "uma colher em cada mão")),
     3: ("Colher de bicarbonato sobre a tigela com mel no fundo; potinho de óleo de coco ao lado.",
         f"Hero: on {t} in the lower foreground, {NEAR}: the clear glass bowl with honey and petroleum jelly at the bottom, a "
         f"small glass jar of white coconut oil beside it. She holds a spoon heaped with white baking soda over the bowl. {MID}",
         ("10,1 a 16,4s (cena 3, bicarbonato)", "tigela com mel + colher de bicarbonato + pote de óleo de coco", "~45%", "colada",
          "colher sobre a tigela")),
     4: ("Ela segura a tigela de vidro com o creme branco liso perto da lente com as duas mãos.",
         f"Hero: she holds the clear glass bowl full of smooth swirled white cream out toward the camera with both hands, "
         f"{NEAR}. {MID}",
         ("16,4 a 26,1s (cena 4, tigela na mão)", "tigela com creme branco", "~40%", "colada", "segura a tigela com as duas mãos")),
     5: ("A tigela de creme branco ainda mais perto da lente, quase enchendo a parte de baixo do quadro.",
         f"Hero: she pushes the clear glass bowl of smooth white cream even closer to the lens with both hands, the bowl filling "
         f"the lower half of the frame. {MID}",
         ("26,1 a 33,4s (cena 5, tigela mais perto)", "tigela com creme branco", "~55%", "quase encostando",
          "empurra a tigela para a lente")),
     6: ("Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado.",
         k_pote(), ficha_pote("26,1 a 33,4s (o pote entra no lugar da tigela para o produto e o CTA)"),
         {"anexos": [AV[a]["anexo"], PRODUTO]}),
    }


MAPAK = {
 "crosta_limao": [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10],
 "intestino_chia": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12],
 "banana_canela": [1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 8, 9, 9, 9, 9, 9],
 "mascara_vaselina": [1, 2, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6],
}
KS = {"crosta_limao": ks_crosta, "intestino_chia": ks_intestino, "banana_canela": ks_banana, "mascara_vaselina": ks_mascara}
MUDO_V = ""
TELA = {
 "crosta_limao": "\"Stop drinking lemon water\"",
 "intestino_chia": "\"Stop drinking chia seeds\"",
 "banana_canela": "\"Put cinnamon on a banana\"",
 "mascara_vaselina": "\"Petroleum jelly + baking soda?\"",
}
CENA_PT = {"PRODUTO": "Ela segura o pote parado, rótulo legível."}


def takes(v, a):
    out = []
    for i, (beat, setup, curta, en, pt) in enumerate(VID[v], 1):
        if "AUTORIDADE" in beat:
            en, pt = AUT[v][a]
        en, pt = OVR.get((v, a, i), (en, pt))
        k = MAPAK[v][i - 1]
        if "MUDO" in beat:
            en, pt = "(no speech)", "(sem fala)"
        cena = KS[v](a)[k][0]
        out.append((f"T{i}", beat.replace(" · MUDO", ""), cena, en, pt, k))
    return out


def mapa_txt(m):
    g = {}
    for i, k in enumerate(m, 1):
        g.setdefault(k, []).append(i)
    def _l(v):
        if len(v) == 1:
            return f"V{v[0]:02d} usa K"
        if v == list(range(v[0], v[-1] + 1)):
            return f"V{v[0]:02d} a V{v[-1]:02d} usam a mesma imagem escolhida do K"
        return ", ".join(f"V{x:02d}" for x in v[:-1]) + f" e V{v[-1]:02d} usam a mesma imagem escolhida do K"
    return "; ".join(f"{_l(v)}{k:02d}" for k, v in g.items()) + "."


IGNORADOS = {}


def main():
    ok = True
    for v in ["crosta_limao", "intestino_chia", "banana_canela", "mascara_vaselina"]:
        m = MODELO[v]
        for a in ["cassidy", "marshall", "meredith"]:
            av = AV[a]
            pasta = os.path.join(RAIZ, "producao", f"{a}_seamoss_{v}")
            tk = takes(v, a)
            assert len(tk) == len(MAPAK[v]), v
            n_pote = next(t for t in tk if "PRODUTO" in t[1])[0]
            qual = (f"**Vídeo: {m['titulo']}.**\n\n"
                    f"**O que acontece:** {av['nome']}, no cenário fixo da conta, faz a receita do modelo cena a cena, "
                    "mostra o resultado e os benefícios, admite o lado ruim de fazer a receita e passa para o sea moss; "
                    f"a partir do {n_pote} segura o pote do Natural Rems Sea Moss parado e legível até o fim. "
                    "Fecha com comment yes, Amazon, link na bio, e o lembrete do follow.\n\n"
                    f"**Gancho:** {KS[v](a)[1][0]}")
            capcut = ("Edição automática (`editar.py`, acabamento HyperFrames): legenda palavra por palavra, cortes de pausa, "
                      f"música a -18 dB da voz. Texto de tela no gancho (V01): {TELA[v]}. "
                      + ("O V02 é mudo: entra logo depois da fala do V01, como no modelo. " if v == "canela_limao" else "")
                      + "Nos takes de CENA CURTA, cortar no fim da fala (o resto do clipe de 8s é sobra). O pote fica parado e "
                      "legível do take do produto até o fim, sem corte para outro plano. Legenda do post: "
                      "`#ad #syntheticperformer #naturalrems` no topo, sem link; chave de conteúdo de IA ligada; link da Amazon "
                      "na bio.")
            ok &= PM.gerar(pasta, f"Sea Moss Venda · {m['titulo']}", qual, mapa_txt(MAPAK[v]), tk, KS[v](a),
                           f"Modelo: {m['desc']}. O cenário do modelo vira o cenário fixo da avatar (avatar fixo da conta); "
                           "forno, fogareiro e freezer entram como aparelhos de bancada quando a receita pede.",
                           capcut, avatar=av, tipo="VENDA")
            if (a, v) in IGNORADOS:
                with open(os.path.join(pasta, "PROMPTS_PRODUCAO.md"), "a", encoding="utf8") as f:
                    f.write("\n" + IGNORADOS[a, v] + "\n")
            ent_p = os.path.join(pasta, av["entrega"])
            ent = open(ent_p, encoding="utf8").read()
            ag = open(os.path.join(pasta, "AGENTE_FLOW.md"), encoding="utf8").read()
            cab, resto = ent.split("## Qual vídeo é este", 1)
            open(ent_p, "w", encoding="utf8").write(
                cab + "## 0. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW (colar inteiro antes do primeiro K)\n\n"
                "```text\n" + ag.strip() + "\n```\n\n## Qual vídeo é este" + resto)
    return ok


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
