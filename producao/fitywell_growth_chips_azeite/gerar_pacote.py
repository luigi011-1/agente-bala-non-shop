import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "_flow"))
from pacote_minimo import gerar  # noqa: E402

MID = "She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression."
NEAR = "very close to the lens, large in frame and closer to the camera than her face"

KS = {
 1: ("Dois montinhos de batata chips com plaquinhas REAL e FAKE e duas velas acesas colados na lente; ela segura uma chip com pegador sobre cada vela.",
     f"Hero: on the black table in the lower foreground, {NEAR}: two small piles of potato chips with small wooden sign cards "
     "reading REAL and FAKE, and two white pillar candles each topped by a small steady flame. She holds a single potato chip "
     "with metal tongs above each candle, eyes wide with intrigue. " + MID,
     ("0,0s (cena 1)", "dois montes de chips + plaquinhas REAL/FAKE + duas velas acesas + chips no pegador", "~45%", "colados", "um pegador em cada mão sobre as velas")),
 2: ("Duas garrafas de azeite de vidro verde e dois copos vazios com plaquinhas REAL e FAKE, colados na lente; ela atrás com as mãos na mesa.",
     f"Hero: on the black table in the lower foreground, {NEAR}: two tall dark green glass olive oil bottles with plain labels "
     "and two empty clear glasses in front of them, with small wooden sign cards reading REAL and FAKE. She stands behind them "
     "with both hands resting on the table. " + MID,
     ("7,6s (cena 2)", "duas garrafas verdes de azeite + dois copos vazios + plaquinhas", "~50%", "colados", "mãos apoiadas na mesa")),
 3: ("Bandeja com dois fogareiros pequenos de chama baixa, dois frascos âmbar e plaquinhas REAL e FAKE; ela segura uma colher sobre cada chama.",
     f"Hero: on a metal tray on the black table in the lower foreground, {NEAR}: two small black burner stands, each with a "
     "small steady blue flame, two small amber glass bottles with plain cream labels, and small chalkboard signs reading REAL "
     "and FAKE. She holds a metal spoon of dark vanilla extract above each small flame. " + MID,
     ("15,4s (cena 3)", "bandeja com dois fogareiros de chama baixa + frascos âmbar + plaquinhas + colheres", "~45%", "colados", "uma colher em cada mão sobre as chamas")),
 4: ("Dois pratos brancos com gelo raspado e plaquinhas REAL e FAKE; ela derrama xarope de uma colher em cada prato, à esquerda uma fita grossa âmbar.",
     f"Hero: on the black table in the lower foreground, {NEAR}: two white plates heaped with shaved ice, with small white paper "
     "cards reading REAL and FAKE and glass bottles of amber syrup at the sides. She pours amber syrup from a spoon onto each "
     "plate: on the left plate it falls in a thick amber ribbon, on the right plate it spreads thin and watery. " + MID,
     ("23,2s (cena 4)", "dois pratos com gelo raspado + xarope + plaquinhas", "~45%", "colados", "uma colher em cada mão derramando")),
 5: ("Ela atrás da mesa falando, os pratos de gelo e as garrafas de xarope ainda na frente.",
     f"Hero: the two white plates of shaved ice with amber syrup and the syrup bottles stay on the black table in the lower "
     f"foreground, close to the lens. She stands behind them, chest up, one hand open in front of her chest. " + MID,
     ("31,2s (cena 5)", "pratos e garrafas de xarope na mesa", "~30%", "colados", "mão aberta, falando")),
}

TAKES = [
 ("T1", "Chips", "A chip sobre a vela.", "Hold a flame to a potato chip. If it burns like a candle, it is loaded with oil, and your gut cannot break it down.", "Encoste uma chama numa batata chips. Se ela queimar igual vela, está cheia de óleo, e o seu intestino não consegue quebrar isso.", 1),
 ("T2", "Azeite", "As garrafas de azeite.", "Number two, olive oil. Chill it overnight. Real extra virgin turns cloudy. If it stays clear, it was cut with seed oils.", "Número dois, azeite. Deixe na geladeira de um dia pro outro. O extravirgem de verdade fica turvo. Se continuar claro, foi cortado com óleo de semente.", 2),
 ("T3", "Baunilha", "A baunilha nas colheres sobre a chama.", "Number three, vanilla. Light some on a spoon. Real vanilla burns blue. If it smokes yellow, it is imitation.", "Número três, baunilha. Acenda um pouco numa colher. Baunilha de verdade queima azul. Se soltar fumaça amarela, é imitação.", 3),
 ("T4", "Maple syrup", "O xarope caindo nos pratos de gelo.", "Number four, maple syrup. Pour some on a cold plate. Real syrup falls in a thick amber ribbon. If it spreads like water, it is colored sugar syrup.", "Número quatro, maple syrup. Derrame um pouco num prato gelado. O de verdade cai numa fita grossa cor de âmbar. Se espalhar igual água, é xarope de açúcar com corante.", 4),
 ("T5", "Autoridade + CTA + follow", "Ela fecha falando.", "With the women I coach, we trust food that behaves the way nature made it. Comment yes if you want more, and follow so you never miss one.", "Com as mulheres que eu acompanho, a gente confia na comida que se comporta do jeito que a natureza fez. Comenta yes se você quer mais, e me segue pra nunca perder nenhum.", 5),
]

QUAL = ("**Vídeo: real ou falso (chips, azeite, baunilha e maple syrup).**\n\n"
        "**O que acontece:** quatro testes rápidos de comida falsa com plaquinhas REAL e FAKE: chama na batata chips (queima como "
        "vela = cheia de óleo), azeite na geladeira (o de verdade fica turvo), baunilha na colher com chama (a de verdade queima "
        "azul) e maple syrup no prato gelado (o de verdade cai em fita grossa). Fecha com a frase de coach, comment yes e follow.\n\n"
        "**Gancho:** fala de abertura \"Hold a flame to a potato chip.\" com ela segurando uma chip no pegador sobre cada vela acesa, "
        "os montes de chips e as plaquinhas REAL e FAKE colados na lente.")

MAPA = "Um K por V: V01 usa K01, V02 usa K02, e assim por diante."
CAPCUT = ("Edição automática (`editar.py`, estilo FitWell): ritmo ~3,8 palavras/s, sem silêncio, legenda serifada branca, "
          "sem light leak, música a -25 dB da voz. Salvar os vídeos como V01 a V05. Sem Voice Changer. "
          "Marcar o post como conteúdo gerado por IA.")

if __name__ == "__main__":
    ok = gerar(D, "FitWell Growth · real ou falso", QUAL, MAPA, TAKES, KS,
               "Modelo: smartphone frontal na altura do peito, mesa com plaquinhas REAL/FAKE; cenário trocado pelo box da avatar.", CAPCUT)
    sys.exit(0 if ok else 1)
