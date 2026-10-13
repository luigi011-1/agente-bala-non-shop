import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "_flow"))
from pacote_minimo import gerar  # noqa: E402

AVATAR = dict(
    anexo="cassidy hargrove .jpg",
    id=("Match the attached image exactly for the woman's identity and outfit: a woman in her early sixties with long "
        "wind-tossed copper-red hair worn in one thick loose braid over her left shoulder, dense freckles on her face and "
        "forearms, wind-weathered fair skin, light eyes, a small reddish mark on her chin, a thick cream cable-knit wool "
        "fisherman sweater with the sleeves pushed up, bright yellow oilskin bib overalls with black buckles, and a silver "
        "Claddagh ring on her left hand."),
    set=("She stands behind a weathered wooden plank workbench on a seaside dock in Maine: behind her a gray cedar-shingled "
         "harvest shed with an open door and wooden rakes inside, a wooden rack of drying dark purple-red seaweed on the left, "
         "gray-blue ocean and dark rocks on the right under an overcast blue-gray sky with visible clouds, and a small American "
         "flag mounted on the shed wall beside the door, in sharp focus."),
    nome="Cassidy Hargrove", ancora="producao/_ancoras/cassidy_hargrove_ancora.jpg",
    entrega="ENTREGA_CASSIDY.md", angulo="Ângulo 1 Sea Moss (conta da Cassidy)", conta="Natural Rems Sea Moss (Cassidy)",
    descr="a mulher ruiva de trança, suéter creme e macacão amarelo", cenario="do cais na frente do galpão de cedro",
    g3="'gray cedar-shingled harvest shed' + 'rack of drying dark purple-red seaweed' + 'small American flag'",
    trava="Mesmo suéter creme, mesmo macacão amarelo, mesma trança ruiva, mesmo galpão, alga secando e bandeira em todo K.")

MID = "She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression."
NEAR = "very close to the lens, large in frame and closer to the camera than her face"

KS = {
 1: ("Tigela de vidro com uma batata cozida e meio abacate na mão dela, perto da lente; amassador na outra mão.",
     f"Hero: she holds a clear glass mixing bowl out toward the camera, {NEAR}, holding one whole boiled yellow potato and "
     "one avocado half with its pit removed; in her other hand a stainless steel potato masher is lowered into the bowl, "
     "pressing the potato. " + MID,
     ("0,0s (cena 1)", "tigela de vidro com batata cozida inteira + meio abacate, amassador de inox", "~40%", "colada, segurada na mão", "segura a tigela com uma mão e o amassador com a outra")),
 2: ("A tigela com a massa verde de batata e abacate na bancada, colada na lente, com ovo, iogurte grego, fermento e sal ao lado; ela bate com o fouet.",
     f"Hero: on the workbench in the lower foreground, {NEAR}: the clear glass mixing bowl holding a smooth pale green potato "
     "and avocado batter with a cracked egg yolk and a spoonful of thick white Greek yogurt on top, a small glass bowl of "
     "yogurt, a small tin of baking powder and a small dish of salt beside it. She whisks the batter with a metal balloon "
     "whisk. " + MID,
     ("5,7 a 13,4s (cenas 5 a 10)", "tigela de vidro com massa verde, gema, iogurte grego, fouet; potinhos de iogurte, fermento e sal", "~45%", "colada", "bate com o fouet")),
 3: ("Assadeira com pãezinhos crus verde-claros colada na lente; ela pincela gema e joga gergelim.",
     f"Hero: on the workbench in the lower foreground, {NEAR}: a metal baking tray lined with parchment paper holding six "
     "round pale green dough buns, the nearest one glossy with brushed egg yolk, a small glass dish of egg yolk and a small "
     "bowl of sesame seeds beside it. She brushes the top of a bun with a pastry brush. " + MID,
     ("15,4 a 19,4s (cenas 12 e 13)", "assadeira com seis pãezinhos verdes crus, pincel, gema, gergelim", "~45%", "colada", "pincela o pãozinho")),
 4: ("Assadeira de pãezinhos dourados com gergelim na bancada; ela segura um pãozinho perto da lente.",
     f"Hero: she holds one golden-brown sesame-topped avocado potato bun up toward the camera, {NEAR}; below it on the "
     "workbench a baking tray of golden sesame buns, one bun torn open showing a soft pale green crumb. " + MID,
     ("21,3 e 29,1s (cenas 16 e 17)", "pãozinho dourado com gergelim na mão + assadeira de pães, um aberto ao meio", "~35%", "colado, segurado na mão", "segura o pãozinho com as duas mãos")),
}

TAKES = [
 ("T1", "Gancho", "Ela amassa a batata e o abacate na tigela.", "Did you know that if you mash one boiled potato with avocado, add eggs, Greek yogurt,", "Você sabia que se você amassar uma batata cozida com abacate, juntar ovos, iogurte grego,", 1),
 ("T2", "Receita", "Ela bate a massa com o fouet.", "baking powder, and salt, and mix the whole lot together until smooth. Then shape it into buns,", "fermento e sal, e misturar tudo até ficar liso. Depois modelar em pãezinhos,", 2),
 ("T3", "Receita", "Ela pincela gema e joga gergelim nos pãezinhos.", "brush the tops with egg yolk, chuck sesame seeds over, and bake until golden.", "pincelar o topo com gema, jogar gergelim por cima e assar até dourar.", 3),
 ("T4", "Resultado", "Ela mostra o pãozinho dourado.", "What you get are incredibly soft, fluffy avocado potato buns with zero flour anywhere near them.", "O que você ganha são pãezinhos de batata com abacate incrivelmente macios e fofinhos, sem farinha nenhuma por perto.", 4),
 ("T5", "CTA + follow", "Ela fecha com o pãozinho na mão.", "Comment yes if you want more recipes like this, and don't forget to hit that follow button.", "Comenta yes se você quer mais receitas assim, e não esquece de clicar no botão de seguir.", 4),
]

QUAL = ("**Vídeo: pãezinhos de batata com abacate, sem farinha.**\n\n"
        "**O que acontece:** a Cassidy, na bancada do cais, amassa batata cozida com abacate, junta ovo, iogurte grego, fermento e "
        "sal, modela os pãezinhos, pincela gema e gergelim e mostra os pães dourados. Fecha com comment yes e o lembrete do follow.\n\n"
        "**Gancho:** fala de abertura \"Did you know that if you mash one boiled potato with avocado\" com ela segurando a tigela de "
        "vidro com a batata e o meio abacate colada na lente, amassador na mão.")

MAPA = "V01 a V03 usam o K de mesmo número; V04 e V05 usam a mesma imagem escolhida do K04 (plano único do pãozinho)."
CAPCUT = ("Edição automática (`editar.py`, acabamento HyperFrames): legenda palavra por palavra, cortes de pausa, música a -18 dB "
          "da voz. Salvar os vídeos como V01 a V05. Sem Voice Changer. Legenda do post: `#ad #syntheticperformer #naturalrems` "
          "no topo, sem link; chave de conteúdo de IA ligada.")

if __name__ == "__main__":
    ok = gerar(D, "Sea Moss Growth · pãezinhos de batata com abacate", QUAL, MAPA, TAKES, KS,
               "Modelo: smartphone frontal na altura do peito, cozinha branca; cenário trocado pelo cais da avatar (avatar fixo da conta).",
               CAPCUT, avatar=AVATAR)
    sys.exit(0 if ok else 1)
