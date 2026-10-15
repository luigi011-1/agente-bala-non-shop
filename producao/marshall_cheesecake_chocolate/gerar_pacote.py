import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "_flow"))
from pacote_minimo import gerar  # noqa: E402

AVATAR = dict(
    anexo="marshall beckett .jpg",
    id=("Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies "
        "with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong "
        "build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on "
        "top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on "
        "a black cord."),
    set=("She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a "
         "black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub "
         "on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag "
         "tied to the right wooden post, in sharp focus."),
    nome="Marshall Beckett", ancora="producao/_ancoras/marshall_beckett_ancora.jpg",
    entrega="ENTREGA_MARSHALL.md", angulo="Ângulo 1 Sea Moss (conta da Marshall)", conta="Natural Rems Sea Moss (Marshall)",
    descr="a senhora de roupa branca de mergulhadora com a máscara de latão na testa", cenario="do galpão de zinco na costa de lava",
    g3="'rusted corrugated tin roof' + 'bamboo mats of drying green and dark red seaweed' + 'small American flag'",
    trava="Mesma roupa branca, mesmo lenço com a máscara de latão, mesmo pingente de abalone, mesmo galpão de zinco, alga secando e bandeira em todo K.")

MID = "She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression."
NEAR = "very close to the lens, large in frame and closer to the camera than her face"

KS = {
 1: ("Tigela de vidro colada na lente; ela tira iogurte grego de um pote com a colher.",
     f"Hero: on the table in the lower foreground, {NEAR}: a large clear glass mixing bowl with a dollop of thick white Greek "
     "yogurt inside. She leans toward the camera holding a small glass jar of Greek yogurt in one hand and a spoon in the "
     "other, scooping more yogurt into the bowl; a small jar of honey and a small bowl of cocoa powder stand beside it. " + MID,
     ("0,0s (cena 1)", "tigela de vidro com iogurte grego + pote de iogurte e colher nas mãos + mel e cacau ao lado", "~40%", "colada", "inclinada para a lente, tira iogurte do pote")),
 2: ("A tigela com o creme de chocolate colada na lente; ela quebra um ovo e bate.",
     f"Hero: on the table in the lower foreground, {NEAR}: the clear glass mixing bowl of glossy smooth chocolate cream with "
     "one raw egg yolk just cracked on top. She whisks it with a metal balloon whisk, the cream swirling. " + MID,
     ("12,1 a 14,7s (cenas 7 a 15)", "tigela de vidro com creme de chocolate + gema, fouet", "~45%", "colada", "bate com o fouet")),
 3: ("Travessa branca com o creme de chocolate colada na lente, forninho elétrico aberto ao lado; ela leva ao forno.",
     f"Hero: on the table in the lower foreground, {NEAR}: a small square white ceramic baking dish filled with smooth "
     "chocolate filling. She holds the dish with both hands, about to slide it into a small electric countertop oven with its "
     "door open at the side of the table. " + MID,
     ("14,8 a 17,9s (cenas 16 a 18)", "travessa branca com recheio de chocolate + forninho elétrico aberto", "~40%", "colada", "segura a travessa com as duas mãos rumo ao forno")),
 4: ("Ela segura a travessa branca com os quadradinhos de chocolate assados perto da lente.",
     f"Hero: she holds the small square white ceramic baking dish out toward the camera with both hands, {NEAR}, filled with "
     "baked chocolate cheesecake squares with a soft glossy top. " + MID,
     ("19,2s (cena 19)", "travessa branca com quadradinhos de chocolate assados", "~40%", "colada, segurada nas mãos", "segura a travessa com as duas mãos")),
 5: ("Ela segura um garfo com um quadradinho de chocolate perto da lente.",
     f"Hero: she holds a fork up toward the camera, {NEAR}, with one thick fudgy chocolate cheesecake square on it; the white "
     "baking dish rests on the table below. " + MID,
     ("28,9s (cena 20)", "garfo com um quadradinho de chocolate + travessa embaixo", "~35%", "colado", "segura o garfo erguido")),
 6: ("Ela segura um prato com uma pilha de quadradinhos de chocolate perto da lente.",
     f"Hero: she holds a round cream plate out toward the camera with both hands, {NEAR}, piled high with thick fudgy "
     "chocolate cheesecake squares. " + MID,
     ("35,4s (cena 21)", "prato com pilha de quadradinhos de chocolate", "~40%", "colado, segurado nas mãos", "segura o prato com as duas mãos")),
}

TAKES = [
 ("T1", "Gancho", "Ela põe iogurte grego na tigela.", "How old were you when you found out that if you add Greek yogurt with a little cocoa powder and honey, then whisk completely smooth,", "Quantos anos você tinha quando descobriu que se você juntar iogurte grego com um pouco de cacau em pó e mel, e bater até ficar bem liso,", 1),
 ("T2", "Receita", "Ela quebra o ovo e bate o creme.", "you can turn it into creamy chocolate cheesecake bites, crack in one egg, and mix everything together until it turns into a creamy chocolate filling.", "dá pra transformar em cheesecake bites cremosos de chocolate, quebrar um ovo e misturar tudo até virar um recheio cremoso de chocolate.", 2),
 ("T3", "Receita", "Ela leva a travessa ao forninho.", "Pour it into a small greased baking dish, and bake it at three twenty-five for about twenty-five minutes.", "Despeja numa travessinha untada e assa a cento e sessenta graus por uns vinte e cinco minutos.", 3),
 ("T4", "Resultado", "Ela mostra a travessa assada.", "You end up with creamy chocolate cheesecake bites that not only taste like something you would get from a bakery,", "Você termina com cheesecake bites cremosos de chocolate que não só têm gosto de coisa de padaria,", 4),
 ("T5", "Benefício", "Ela segue com a travessa.", "but are packed with protein and made without all the refined sugar you would normally find in cheesecake.", "como são cheios de proteína e feitos sem todo o açúcar refinado que normalmente tem no cheesecake.", 4),
 ("T6", "Benefício + autoridade", "Ela mostra um pedaço no garfo.", "No refined sugar, low effort, high protein. I have recipes like this for every sweet treat you can think of.", "Sem açúcar refinado, pouco esforço, muita proteína. Eu tenho receitas assim pra todo doce que você imaginar.", 5),
 ("T7", "CTA + follow", "Ela fecha com o prato cheio.", "Comment yes if you want more like this, and don't forget to hit that follow button so you do not miss a single one.", "Comenta yes se você quer mais assim, e não esquece de clicar no botão de seguir pra não perder nenhuma.", 6),
]

QUAL = ("**Vídeo: cheesecake bites de chocolate com iogurte grego.**\n\n"
        "**O que acontece:** a Marshall, na mesa de tábua do galpão de zinco, junta iogurte grego, cacau e mel, quebra um ovo, bate "
        "até virar recheio cremoso, leva ao forninho e mostra os quadradinhos assados. Fala dos benefícios e fecha com comment yes "
        "e o lembrete do follow.\n\n"
        "**Gancho:** fala de abertura \"How old were you when you found out\" com ela inclinada para a lente pondo iogurte grego "
        "na tigela de vidro colada na lente.")

MAPA = "V01 a V03 usam o K de mesmo número; V04 e V05 usam a mesma imagem escolhida do K04; V06 usa o K05; V07 usa o K06."
CAPCUT = ("Edição automática (`editar.py`, acabamento HyperFrames): legenda palavra por palavra, cortes de pausa, música a -18 dB "
          "da voz. Salvar os vídeos como V01 a V07. Sem Voice Changer. Legenda do post: `#ad #syntheticperformer #naturalrems` "
          "no topo, sem link; chave de conteúdo de IA ligada.")

if __name__ == "__main__":
    ok = gerar(D, "Sea Moss Growth · cheesecake bites de chocolate", QUAL, MAPA, TAKES, KS,
               "Modelo: smartphone frontal na altura do peito, cozinha de loft; cenário trocado pelo galpão da avatar (avatar fixo da conta).",
               CAPCUT, avatar=AVATAR)
    sys.exit(0 if ok else 1)
