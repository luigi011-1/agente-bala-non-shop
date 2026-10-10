import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "_flow"))
from pacote_minimo import gerar  # noqa: E402

MID = "She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression."
TANQUE = ("Hero: a shallow clear glass tank of cold water on the black table fills the lower half of the frame, very close "
          "to the lens, large in frame and closer to the camera than her face.")

KS = {
 1: ("Aquário raso de água fria colado na lente; ela atrás segurando uma colher cheia de grãos de pimenta-do-reino em cada mão sobre a água.",
     TANQUE + " She leans in behind it, chest up, holding a metal spoon heaped with black peppercorns in each hand just above "
     "the water, eyebrows raised in disbelief. " + MID,
     ("0,0s (cena 1)", "aquário raso de vidro com água + duas colheres de grãos", "~50%", "colado, mais perto que o rosto", "inclinada, uma colher em cada mão sobre a água")),
 2: ("Mesmo aquário: quase todos os grãos no fundo e algumas sementes de mamão boiando; ela atrás com as colheres vazias.",
     TANQUE + " Most black peppercorns rest on the glass bottom of the tank, while a few small round dried papaya seeds float "
     "on the water surface. She leans behind it holding the two empty spoons above the water. " + MID,
     ("4,7s a 10,7s (fim da cena 1)", "aquário com grãos no fundo e sementes boiando", "~50%", "colado", "colheres vazias sobre a água")),
 3: ("Mesmo aquário; ela aponta as sementes que boiam, sobrancelha levantada.",
     TANQUE + " Black peppercorns rest on the bottom and a few small round dried papaya seeds float on top. She points at the "
     "floating seeds with her right index finger, one eyebrow raised. " + MID,
     ("10,7s (cena 2)", "aquário com sementes boiando", "~50%", "colado", "aponta as sementes que boiam")),
 4: ("Dois copos de água morna colados na lente; ela segura uma colher de cúrcuma em pó sobre cada copo.",
     "Hero: two clear drinking glasses of warm water side by side on the black table in the lower foreground, very close to "
     "the lens, large in frame and closer to the camera than her face. She holds a metal spoon heaped with bright orange-yellow "
     "turmeric powder above each glass. " + MID,
     ("15,5s (cena 3)", "dois copos de vidro com água + duas colheres de cúrcuma", "~45%", "colados", "uma colher sobre cada copo")),
 5: ("Um copo colado na lente: a nuvem de cúrcuma descendo devagar na água clara; ela atrás olhando a câmera.",
     "Hero: one clear drinking glass of water fills the lower two thirds of the frame, very close to the lens, large in frame "
     "and closer to the camera than her face; a cloud of orange-yellow turmeric powder drifts slowly down through the clear "
     "water toward the bottom. She stands behind the glass, chest up. " + MID,
     ("19,0s (cena 4, macro)", "um copo de vidro com a nuvem de cúrcuma descendo", "~65%", "colado, quase macro", "atrás do copo, olhando a câmera")),
 6: ("Os dois copos lado a lado: um claro com a cúrcuma no fundo, o outro amarelo forte; ela segura um em cada mão.",
     "Hero: two clear drinking glasses side by side on the black table, very close to the lens, large in frame and closer to "
     "the camera than her face. The left glass holds clear water with turmeric settled at the bottom, the right glass holds "
     "bright opaque yellow water. She holds one glass in each hand. " + MID,
     ("23,7s (cena 5)", "dois copos: um claro com pó no fundo, um amarelo forte", "~45%", "colados", "um copo em cada mão")),
 7: ("Ela segura dois paus de canela colados na lente: um em camadas finas como charuto, outro uma casca grossa só.",
     "Hero: she holds two cinnamon sticks upright close to the lens, one in each hand, large in frame and closer to the camera "
     "than her face. The left stick is rolled in many thin paper-like layers like a cigar, the right stick is a single thick "
     "hard curl of bark. " + MID,
     ("26,6s (cena 6)", "dois paus de canela verticais, finos em camadas x casca grossa", "~40%", "colados", "um pau em cada mão, à frente do peito")),
 8: ("Ela empurra a casca grossa para perto da lente, o pau fino mais baixo, expressão séria.",
     "Hero: she holds the single thick hard curl of cinnamon bark forward toward the lens in her right hand, large in frame "
     "and closer to the camera than her face, while the thin layered cinnamon stick rests lower in her left hand. Serious "
     "warning expression. " + MID,
     ("37,2s (fim da cena 6)", "a casca grossa de cássia em destaque", "~35%", "colada", "casca grossa à frente, sério")),
 9: ("Três potinhos na mesa (pimenta, cúrcuma, paus de canela) colados na lente; ela atrás com as mãos abertas.",
     "Hero: on the black table in the lower foreground, very close to the lens, three small bowls: black peppercorns, bright "
     "yellow turmeric powder and cinnamon sticks. She stands behind them, chest up, both hands open in front of her chest. " + MID,
     ("41,4s (cena 7)", "três potinhos com os temperos", "~30%", "colados", "mãos abertas, falando")),
}

TAKES = [
 ("T1", "Pimenta · o teste", "Ela segura as colheres de pimenta sobre o aquário.", "If you bought black pepper from the store, drop a spoonful into cold water.", "Se você comprou pimenta-do-reino no mercado, jogue uma colher em água fria.", 1),
 ("T2", "Pimenta · o resultado", "Grãos no fundo, sementes boiando.", "Real peppercorns sink. If some float, those are dried papaya seeds mixed in to fill the jar.", "Pimenta de verdade afunda. Se alguns boiarem, são sementes de mamão secas misturadas pra encher o pote.", 2),
 ("T3", "Pimenta · por quê", "Ela aponta as sementes que boiam.", "Why? Papaya seeds are cheap filler, sold at pepper prices.", "Por quê? Semente de mamão é enchimento barato, vendido a preço de pimenta.", 3),
 ("T4", "Cúrcuma · o teste", "Colheres de cúrcuma sobre os dois copos.", "Turmeric. Stir a spoonful into warm water.", "Cúrcuma. Misture uma colher em água morna.", 4),
 ("T5", "Cúrcuma · o resultado", "A cúrcuma descendo devagar no copo.", "Real turmeric slowly settles. If the water turns bright yellow right away, it has been dyed.", "Cúrcuma de verdade assenta devagar. Se a água ficar amarelo forte na hora, ela foi tingida.", 5),
 ("T6", "Cúrcuma · por quê", "Os dois copos lado a lado.", "Why? Dye hides old, weak powder.", "Por quê? O corante esconde pó velho e fraco.", 6),
 ("T7", "Canela · o teste", "Os dois paus de canela.", "Cinnamon sticks. Real cinnamon has thin paper layers, like a cigar. One thick, hard curl is cassia, the cheaper kind.", "Canela em pau. Canela de verdade tem camadas finas como papel, igual um charuto. Uma casca grossa e dura é cássia, a mais barata.", 7),
 ("T8", "Canela · por quê", "A casca grossa em destaque.", "Why? Cassia is high in coumarin, which can strain the liver.", "Por quê? A cássia tem muita cumarina, que pode sobrecarregar o fígado.", 8),
 ("T9", "Autoridade + CTA + follow", "Os três temperos na mesa.", "My clients and I study our food closely, because what we eat becomes us. Comment yes for more, and follow for the next one.", "Eu e as minhas clientes estudamos a nossa comida de perto, porque o que a gente come vira a gente. Comenta yes pra mais, e me segue pro próximo.", 9),
]

QUAL = ("**Vídeo: temperos falsos (pimenta, cúrcuma e canela).**\n\n"
        "**O que acontece:** três testes de cozinha para descobrir tempero falsificado: pimenta na água fria (a de verdade afunda, "
        "o que boia é semente de mamão), cúrcuma na água morna (a tingida deixa a água amarela na hora) e canela em pau (camadas "
        "finas é canela de verdade, casca grossa é cássia). Fecha com a frase de coach dela, comment yes e follow.\n\n"
        "**Gancho:** fala de abertura \"If you bought black pepper from the store, drop a spoonful into cold water.\" com ela "
        "segurando uma colher de grãos em cada mão sobre um aquário de água colado na lente.")

MAPA = "Um K por V: V01 usa K01, V02 usa K02, e assim por diante."
CAPCUT = ("Edição automática (`editar.py`, estilo FitWell): ritmo ~3,8 palavras/s, sem silêncio, legenda serifada branca, "
          "sem light leak, música a -25 dB da voz. Salvar os vídeos como V01 a V09 (a ordem também é conferida pela fala). "
          "Sem Voice Changer. Marcar o post como conteúdo gerado por IA.")

if __name__ == "__main__":
    ok = gerar(D, "FitWell Growth · temperos falsos", QUAL, MAPA, TAKES, KS,
               "Modelo: smartphone frontal na altura do peito; cenário trocado pelo box da avatar (avatar fixo da conta).", CAPCUT)
    sys.exit(0 if ok else 1)
