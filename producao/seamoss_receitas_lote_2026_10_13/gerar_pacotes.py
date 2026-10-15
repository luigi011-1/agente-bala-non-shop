"""Pacotes do lote Sea Moss VENDA a partir de receitas virais (2026-10-13).
4 modelos (canela_limao, bolinho_maca, wrap_lentilha, sorvete_banana) x 3 avatares = 12 produções em
producao/<avatar>_seamoss_<receita>/. Textos aprovados em textos.py (mesma fonte do ROTEIRO.md).
Gerador comum: producao/_flow/pacote_minimo.py. Rodar da raiz:
python3 producao/seamoss_receitas_lote_2026_10_13/gerar_pacotes.py
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
def ks_canela(a):
    t = TABLE[a]
    return {
     1: ("Gancho: boneco humano de açúcar ao lado dela, colado na lente; ela despeja canela de um pote de vidro na cabeça dele.",
         f"Hero: a life-size human figure sculpted entirely from coarse white sugar crystals stands right beside her, its head "
         f"and shoulders {NEAR}, a reddish-brown dusting of ground cinnamon already on its shoulders. She raises a small glass jar "
         f"of ground cinnamon above its head and pours a stream of cinnamon onto the crown. {MID}",
         ("0,0 a 2,7s (cena 1, selfie no gramado)", "boneco humano de cristais de açúcar + pote de canela despejando na cabeça",
          "~45%", "colado", "ao lado do boneco, braço erguido despejando canela")),
     2: ("Take mudo: o boneco de açúcar sozinho no cenário da conta, inteiro, com canela nos ombros.",
         "",
         ("2,7 a 5,4s (cena 2, boneco sozinho contra o céu)", "boneco humano de cristais de açúcar de corpo inteiro",
          "~60%", "1,5 m, de corpo inteiro", "boneco em pé, braços ao lado do corpo"),
         sem_pessoa(a, "Vertical photo of an empty scene. Hero: a life-size human figure sculpted entirely from coarse white sugar "
                       "crystals stands upright in the center of the frame, full body, arms at its sides, a reddish-brown "
                       "dusting of ground cinnamon on its head and shoulders, a small pile of loose sugar crystals at its feet.")),
     3: ("Copo de água colado na lente; ela põe uma colher de canela. Meio limão e pote de mel ao lado.",
         f"Hero: on {t} in the lower foreground, {NEAR}: a clear glass of warm water. She holds a teaspoon of ground cinnamon "
         f"over the glass, tipping it in; half a lemon and a small glass jar of raw honey stand beside the glass. {MID}",
         ("5,4 a 8,6s (cena 3, mesa)", "copo de água + colher de canela + meio limão + pote de mel", "~35%", "colado",
          "atrás da mesa, colher de canela sobre o copo")),
     4: ("Close: ela espreme meio limão em cima do copo, colado na lente.",
         f"Hero: in the lower foreground, {NEAR}: the clear glass of water with cinnamon floating on top, and her hand squeezing "
         f"half a fresh lemon over it, juice dripping in. {MID}",
         ("8,6 a 12,4s (cena 4, close)", "meio limão sendo espremido sobre o copo", "~50%", "colado", "espreme o limão")),
     5: ("Ela segura uma colher de mel cru sobre o copo; potinhos de cúrcuma e sal rosa ao lado.",
         f"Hero: on {t} in the lower foreground, {NEAR}: the glass of cloudy cinnamon lemon water. She holds a tablespoon of "
         f"thick raw honey over it; a small ceramic bowl of bright turmeric powder and a small bowl of pink salt stand beside it. {MID}",
         ("12,4 a 16,5s (cena 5, plano médio)", "colher de mel sobre o copo + potinhos de cúrcuma e sal rosa", "~35%", "colado",
          "colher de mel na mão direita")),
     6: ("Close: ela solta uma fatia de gengibre fresco dentro do copo; potinhos de cúrcuma e sal rosa ao lado.",
         f"Hero: in the lower foreground, {NEAR}: the glass of golden drink with a slice of lemon inside. Her fingers drop a thin "
         f"round slice of fresh ginger into it; a small ceramic bowl of turmeric powder and a small bowl of pink salt stand "
         f"beside the glass. {MID}",
         ("16,5 a 24,5s (cena 6, close)", "fatia de gengibre entrando no copo + potinhos de cúrcuma e sal rosa", "~50%",
          "colado", "dedos soltando o gengibre")),
     7: ("Ela segura o copo pronto, dourado e turvo com fatia de limão, perto da lente.",
         f"Hero: she holds the finished glass of cloudy golden drink with a slice of lemon and a slice of ginger inside out "
         f"toward the camera in her right hand, {NEAR}. {MID}",
         ("24,5 a 36,7s (cenas 7 a 9, selfie com o copo)", "copo pronto com limão e gengibre", "~25%", "colado",
          "segura o copo com a mão direita")),
     8: ("Ela segura uma tábua redonda com os seis ingredientes e o copo, perto da lente.",
         f"Hero: she holds a round wooden board out toward the camera with both hands, {NEAR}: on it a glass mug of the golden "
         f"drink, cinnamon sticks, a knob of fresh ginger, a small pile of grated ginger, a mound of turmeric powder, half a "
         f"lemon and a small jar of honey. {MID}",
         ("36,7 a 43,4s (cenas 10 e 11, bandeja)", "tábua redonda com copo, canela em pau, gengibre, cúrcuma, limão e mel",
          "~45%", "colada", "segura a tábua com as duas mãos")),
     9: ("Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado.",
         k_pote(), ficha_pote("43,4 a 60,1s (cena 12, pote na mão)"), {"anexos": [AV[a]["anexo"], PRODUTO]}),
    }


def ks_bolinho(a):
    t = TABLE[a]
    return {
     1: ("Gancho: ela segura uma maçã vermelha perto da lente; tábua de corte e tigela creme na mesa.",
         f"Hero: she holds one shiny red apple out toward the camera in her right hand, {NEAR}; a walnut cutting board and a "
         f"large cream ceramic mixing bowl rest on {t}. {MID}",
         ("0,0 a 2,0s (cena 1)", "maçã vermelha na mão + tábua e tigela creme na mesa", "~20%", "colada", "mão direita estendida com a maçã")),
     2: ("Close: faca picando maçã vermelha em cubos na tábua colada na lente.",
         f"Hero: on {t} in the lower foreground, {NEAR}: a walnut cutting board with a pile of small diced red apple cubes. "
         f"She is dicing a red apple into small cubes on the board; the cream mixing bowl waits beside the board. {MID}",
         ("2,0 a 4,3s (cenas 2 e 3, mesma tábua)", "tábua com cubos de maçã sendo picados", "~50%", "colada", "pica a maçã com a faca")),
     3: ("Tigela de maçã picada colada na lente; colher de canela por cima.",
         f"Hero: on {t} in the lower foreground, {NEAR}: the large cream ceramic mixing bowl full of diced red apple. She holds "
         f"a spoon heaped with ground cinnamon over the bowl. {MID}",
         ("4,3 a 5,3s (cena 4)", "tigela de maçã picada + colher de canela", "~50%", "colada", "colher sobre a tigela")),
     4: ("Ela quebra um ovo na tigela de maçã com canela colada na lente.",
         f"Hero: on {t} in the lower foreground, {NEAR}: the cream mixing bowl of diced apple dusted with cinnamon. She cracks a "
         f"brown egg over the bowl with one hand. {MID}",
         ("5,3 a 6,8s (cena 5)", "tigela de maçã com canela + ovo", "~50%", "colada", "quebra o ovo")),
     5: ("Ela despeja aveia de um pote de vidro na tigela colada na lente.",
         f"Hero: on {t} in the lower foreground, {NEAR}: the cream mixing bowl of diced apple. She tips a clear jar of rolled "
         f"oats, a stream of oats pouring onto the apples. {MID}",
         ("6,8 a 7,8s (cena 6)", "pote de aveia despejando na tigela", "~50%", "colada", "inclina o pote de aveia")),
     6: ("Pitada de fermento de um potinho branco sobre a tigela colada na lente.",
         f"Hero: on {t} in the lower foreground, {NEAR}: the cream mixing bowl with a mound of oats over the apples. She holds "
         f"a small white ramekin of baking powder and sprinkles a pinch over the bowl. {MID}",
         ("7,8 a 8,9s (cena 7)", "potinho de fermento + tigela com aveia", "~50%", "colada", "pitada com os dedos")),
     7: ("Ela mistura a massa grossa de maçã e aveia com colher de pau, colada na lente.",
         f"Hero: on {t} in the lower foreground, {NEAR}: the cream mixing bowl of thick chunky apple and oat batter. She stirs "
         f"it with a wooden spoon. {MID}",
         ("8,9 a 10,5s (cena 8)", "tigela com massa de maçã e aveia + colher de pau", "~50%", "colada", "mistura")),
     8: ("Ela põe montinhos de massa com boleador numa assadeira com papel manteiga colada na lente.",
         f"Hero: on {t} in the lower foreground, {NEAR}: a baking sheet lined with parchment paper with one round mound of "
         f"apple oat batter on it. She drops a second mound from a metal cookie scoop. {MID}",
         ("10,5 a 12,3s (cena 9)", "assadeira com papel manteiga + montinho de massa + boleador", "~50%", "colada", "solta a massa do boleador")),
     9: ("Ela leva a assadeira com os montinhos crus ao forninho elétrico aberto.",
         f"Hero: in the lower foreground, {NEAR}: a baking sheet of six raw round apple oat mounds. She holds it with both "
         f"hands, sliding it into {OVEN}. {MID}",
         ("12,3 a 14,2s (cena 10, forno)", "assadeira de montinhos crus + forninho aberto", "~45%", "colada", "desliza a assadeira para o forno")),
     10: ("Ela segura a assadeira de bolinhos de maçã dourados perto da lente.",
          f"Hero: she holds a baking sheet of nine golden baked apple oat fritters out toward the camera with both hands, {NEAR}. {MID}",
          ("14,2 a 17,3s (cena 11)", "assadeira de bolinhos dourados", "~45%", "colada", "segura a assadeira com as duas mãos")),
     11: ("Ela segura um prato com três bolinhos empilhados perto da lente.",
          f"Hero: she holds a round cream plate out toward the camera, {NEAR}, with a stack of three golden apple oat fritters. {MID}",
          ("17,3 e 31,8s (cenas 12 e 16, prato)", "prato com pilha de três bolinhos", "~40%", "colado", "segura o prato")),
     12: ("Ela segura um bolinho partido ao meio perto da lente, mostrando a maçã por dentro.",
          f"Hero: she holds one golden apple oat fritter broken in half out toward the camera with both hands, {NEAR}, soft apple "
          f"pieces and oats visible inside; the plate of fritters rests on {t}. {MID}",
          ("19,8 a 31,8s (cenas 13 a 15)", "bolinho partido ao meio nas duas mãos", "~30%", "colado", "segura as duas metades")),
     13: ("Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado.",
          k_pote(), ficha_pote("31,8 a 35,0s (cena final; o pote entra no lugar do prato)"), {"anexos": [AV[a]["anexo"], PRODUTO]}),
    }


def ks_wrap(a):
    t = TABLE[a]
    return {
     1: ("Gancho: tigela de vidro colada na lente vista de baixo; ela despeja lentilha vermelha de um saco.",
         f"Hero: a clear glass mixing bowl held just above the lens, seen from below through the glass, {NEAR}; she tips a clear "
         f"zip bag of dry red lentils, a stream of orange lentils pouring into the bowl, her face looking down through the glass. "
         f"Low angle from below the bowl. {MID}",
         ("0,0 a 3,2s (cena 1, câmera embaixo da tigela)", "tigela de vidro + saco de lentilha despejando", "~60%", "colada",
          "inclinada sobre a tigela, despeja o saco")),
     2: ("Tigela de vidro com lentilha de molho colada na lente; ela joga uma pitada de sal.",
         f"Hero: on {t} in the lower foreground, {NEAR}: a clear glass bowl of red lentils soaking in water. Her fingers sprinkle "
         f"a pinch of salt over it. {MID}",
         ("3,2 a 4,3s (cena 2)", "tigela de lentilha de molho + pitada de sal", "~50%", "colada", "pitada de sal com os dedos")),
     3: ("Mixer de mão dentro da tigela de lentilha, colado na lente.",
         f"Hero: in the lower foreground, {NEAR}: the clear glass bowl of soaked red lentils with a black immersion blender "
         f"plunged into it. She holds the blender handle. {MID}",
         ("4,3 a 5,5s (cena 3)", "mixer de mão dentro da tigela de lentilha", "~55%", "colado", "segura o mixer")),
     4: ("Ela despeja uma concha de massa laranja na frigideira de ferro sobre o fogareiro.",
         f"Hero: in the lower foreground, {NEAR}: a black cast iron skillet on {BURNER}. She pours a ladle of smooth orange "
         f"lentil batter into the hot skillet. {MID}",
         ("5,5 a 7,2s (cena 4)", "frigideira de ferro + concha despejando massa laranja", "~45%", "colada", "despeja a concha")),
     5: ("Close: wrap fino de lentilha cozinhando na frigideira de ferro, espátula ao lado.",
         f"Hero: in the lower foreground, {NEAR}: the black cast iron skillet with one thin round golden-orange lentil wrap "
         f"cooking, small bubbles on its surface; she holds a metal spatula at its edge. {MID}",
         ("7,2 a 9,2s (cena 5, close)", "frigideira com wrap cozinhando + espátula", "~55%", "colada", "espátula na borda")),
     6: ("Ela dobra um wrap de lentilha macio perto da lente; pilha de wraps num prato na mesa.",
         f"Hero: she holds one soft golden lentil wrap out toward the camera with both hands, {NEAR}, folding it in half like a "
         f"tortilla; a stack of wraps on a round plate rests on {t}. {MID}",
         ("9,2 a 21,0s (cenas 6 e 7, sentada com o wrap)", "wrap dobrando nas mãos + prato com pilha de wraps", "~35%", "colado", "dobra o wrap")),
     7: ("Ela segura um saco transparente de lentilha vermelha seca colado na lente.",
         f"Hero: she holds a large clear plastic bag of dry red lentils up toward the camera with both hands, {NEAR}. {MID}",
         ("21,0 a 24,8s (cenas 8 e 9)", "saco transparente de lentilha vermelha", "~55%", "colado", "segura o saco com as duas mãos")),
     8: ("Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado.",
         k_pote(), ficha_pote("24,8 a 34,2s (cena final; o pote entra no lugar do wrap)"), {"anexos": [AV[a]["anexo"], PRODUTO]}),
    }


def ks_sorvete(a):
    t = TABLE[a]
    return {
     1: ("Gancho: copo de liquidificador colado na lente; ela despeja banana congelada de um saco.",
         f"Hero: on {t} in the lower foreground, {NEAR}: a glass blender jar on its base. She leans toward the camera tipping a "
         f"clear zip bag of frozen banana slices, the slices tumbling into the jar. {MID}",
         ("0,0 a 4,9s (cena 1)", "copo de liquidificador + saco de banana congelada despejando", "~45%", "colado",
          "inclinada para a lente, despeja o saco")),
     2: ("Ela põe uma colher de cacau em pó no liquidificador com banana, colado na lente.",
         f"Hero: on {t} in the lower foreground, {NEAR}: the glass blender jar filled with frozen banana slices. She holds a "
         f"spoon heaped with dark cocoa powder over it. {MID}",
         ("4,9 a 7,3s (cena 2)", "liquidificador com banana + colher de cacau", "~45%", "colado", "colher de cacau sobre o copo")),
     3: ("Ela solta uma colherada de pasta de amendoim no liquidificador, colado na lente.",
         f"Hero: in the lower foreground, {NEAR}: the glass blender jar of frozen banana slices dusted with cocoa. She drops a "
         f"thick spoonful of creamy peanut butter from a metal spoon into the jar. {MID}",
         ("7,3 a 9,9s (cenas 3 a 6, mesma colher)", "colher de pasta de amendoim + liquidificador", "~50%", "colado", "solta a pasta da colher")),
     4: ("Vista de cima para dentro do liquidificador: creme grosso de chocolate girando, colado na lente.",
         f"Hero: top-down view into the open glass blender jar, {NEAR}: a thick glossy chocolate banana cream swirling around "
         f"the blade, cocoa specks on the side; she holds the jar with one hand. {MID}",
         ("9,9 a 15,1s (cenas 7 a 9, POV do liquidificador)", "creme de chocolate girando dentro do copo", "~65%", "colado",
          "segura o copo, câmera por cima")),
     5: ("Ela despeja um pouco de leite de uma garrafinha de vidro no liquidificador, colado na lente.",
         f"Hero: on {t} in the lower foreground, {NEAR}: the glass blender jar of thick chocolate cream. She pours a splash of "
         f"milk from a small glass bottle into it. {MID}",
         ("15,1 a 16,7s (cena 10)", "garrafinha de leite despejando + liquidificador", "~45%", "colado", "despeja o leite")),
     6: ("O liquidificador cheio de sorvete de chocolate grosso na mesa, colado na lente; mão dela no copo.",
         f"Hero: on {t} in the lower foreground, {NEAR}: the glass blender jar full of thick soft chocolate ice cream; her hand "
         f"rests on the jar. {MID}",
         ("16,7 a 22,4s (cenas 11 e 12)", "liquidificador cheio de sorvete grosso", "~45%", "colado", "mão no copo")),
     7: ("Vista de cima: ela segura um pote branco com o creme de chocolate sobre o freezer aberto.",
         f"Hero: high top-down view, she holds a small white square container of smooth chocolate cream with both hands, {NEAR}, "
         f"right above {FREEZER}; she looks up at the camera. {MID}",
         ("24,2 a 29,5s (cena 14, freezer visto de cima)", "pote branco de creme + freezer aberto", "~35%", "colado",
          "segura o pote sobre o freezer, olhando para cima")),
     8: ("Ela segura uma tigela branca de sorvete de chocolate perto da lente.",
         f"Hero: she holds a round white bowl of creamy chocolate banana ice cream out toward the camera, {NEAR}. {MID}",
         ("29,5 a 35,3s (cenas 15 e 16)", "tigela branca de sorvete de chocolate", "~40%", "colada", "segura a tigela")),
     9: ("Tigela de sorvete na mesa colada na lente; ela tira uma bola com o boleador de metal.",
         f"Hero: on {t} in the lower foreground, {NEAR}: the round white bowl of creamy chocolate banana ice cream. She digs a "
         f"metal ice cream scoop into it, lifting a round scoop. {MID}",
         ("35,3 a 53,9s (cenas 17 a 19; no fim o modelo mostra brownie por engano, aqui fica o sorvete)",
          "tigela de sorvete + boleador", "~45%", "colada", "tira uma bola com o boleador")),
     10: ("Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado.",
          k_pote(), ficha_pote("46,4 a 53,9s (cena final; o pote entra no lugar do prato)"), {"anexos": [AV[a]["anexo"], PRODUTO]}),
    }


# take -> K (pela ordem dos takes em textos.py)
MAPAK = {
 "canela_limao": [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 9, 9, 9, 9],
 "bolinho_maca": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12, 11, 11, 11, 13, 13, 13, 13, 13],
 "wrap_lentilha": [1, 2, 3, 4, 5, 6, 6, 7, 7, 6, 6, 6, 8, 8, 8, 8, 8],
 "sorvete_banana": [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10],
}
KS = {"canela_limao": ks_canela, "bolinho_maca": ks_bolinho, "wrap_lentilha": ks_wrap, "sorvete_banana": ks_sorvete}
MUDO_V = ("(no speech) The white sugar sculpture in the image slowly melts away grain by grain, the sugar crystals sliding "
          "down like fine sand into a soft heap on the ground, a light dust of cinnamon drifting down with them.\n"
          "Fixed camera, no music.")
TELA = {
 "canela_limao": "\"What cinnamon does to the SUGAR in your body\"",
 "bolinho_maca": "\"Apple fritters that won't spike your blood sugar\"",
 "wrap_lentilha": "\"One ingredient wraps. Zero flour.\"",
 "sorvete_banana": "\"Chocolate ice cream with just bananas\"",
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


IGNORADOS = {("marshall", "canela_limao"): "**Edição:** o V02 foi IGNORADO nesta produção (não gerou no Flow, decisão do Luigi em 2026-10-13). Montar V01 → V03 → ... → V15, sem o take mudo."}


def main():
    ok = True
    for v in ["canela_limao", "bolinho_maca", "wrap_lentilha", "sorvete_banana"]:
        m = MODELO[v]
        for a in ["meredith", "marshall", "cassidy"]:
            av = AV[a]
            pasta = os.path.join(RAIZ, "producao", f"{a}_seamoss_{v}")
            tk = takes(v, a)
            assert len(tk) == len(MAPAK[v]), v
            n_pote = next(t for t in tk if "PRODUTO" in t[1])[0]
            qual = (f"**Vídeo: {m['titulo']}.**\n\n"
                    f"**O que acontece:** {av['nome']}, no cenário fixo da conta, faz a receita do modelo cena a cena, "
                    "mostra o resultado e os benefícios, admite o lado ruim de fazer a receita e passa para o sea moss; "
                    f"a partir do {n_pote} segura o pote do Natural Rems Sea Moss parado e legível até o fim. "
                    "Fecha com comment yes, Amazon, Stories e bio, e o lembrete do follow.\n\n"
                    f"**Gancho:** {KS[v](a)[1][0]}")
            capcut = ("Edição automática (`editar.py`, acabamento HyperFrames): legenda palavra por palavra, cortes de pausa, "
                      f"música a -18 dB da voz. Texto de tela no gancho (V01): {TELA[v]}. "
                      + ("O V02 é mudo: entra logo depois da fala do V01, como no modelo. " if v == "canela_limao" else "")
                      + "Nos takes de CENA CURTA, cortar no fim da fala (o resto do clipe de 8s é sobra). O pote fica parado e "
                      "legível do take do produto até o fim, sem corte para outro plano. Legenda do post: "
                      "`#ad #syntheticperformer #naturalrems` no topo, sem link; chave de conteúdo de IA ligada; Story no ar "
                      "com o link da Amazon.")
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
