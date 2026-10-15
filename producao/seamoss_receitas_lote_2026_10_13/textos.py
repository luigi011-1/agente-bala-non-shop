# Lote Sea Moss VENDA a partir de receitas virais (2026-10-13).
# Corpo da receita clonado do modelo; ponte = pontos fracos de fazer a receita (pedido do Luigi) -> sea moss
# fazendo o mesmo trabalho -> obstáculo derivado da receita -> Natural Rems -> yes -> Amazon -> Stories/bio -> follow.
# Cada take: (beat, setup, curta, ingles, portugues). "MUDO" no beat = take sem fala.
# AUT[video][avatar] substitui o take marcado com beat que contém "AUTORIDADE".

CTA = ("Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio.",
       "Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio.")

VID = {}
MODELO = {}
AUT = {}

# ---------------------------------------------------------------- 1. água de canela (modelo Jupi, já é venda)
MODELO["canela_limao"] = dict(
    arq="snapinsta-1791928587628.mp4", dur="60,1s", pasta="r_1791928587628",
    desc="mulher loira de camisa branca, mesa de madeira num gramado com vista de colinas; gancho = boneco humano de açúcar recebendo canela e se desfazendo; receita em closes; selfie com o copo; bandeja de ingredientes; pote da Jupi Hydration no CTA",
    cta_orig="That's why I just add one scoop of Jupy Hydration... If you're dealing with bloating every day, you can find it by searching Jupy Hydration on Amazon or just check the link in my bio. And if you're watching on Facebook, the link is in the description.",
    titulo="Água de canela, limão e mel → Natural Rems Sea Moss")
VID["canela_limao"] = [
("GANCHO", "A", 1, "This is what cinnamon does to the sugar in your body.",
 "Isto é o que a canela faz com o açúcar no seu corpo."),
("GANCHO · MUDO", "B", 1, "", "(sem fala: o boneco de açúcar se desfaz)"),
("RECEITA", "C", 1, "In a glass of warm water, mix one teaspoon of cinnamon,",
 "Num copo de água morna, misture uma colher de chá de canela,"),
("RECEITA", "D", 1, "a squeeze of fresh lemon juice,", "um pouco de suco de limão fresco,"),
("RECEITA", "E", 0, "and one tablespoon of raw honey. Now, if you wanna take this to the next level,",
 "e uma colher de sopa de mel cru. Agora, se você quer levar isso para o próximo nível,"),
("RECEITA", "F", 0, "add a slice of fresh ginger to get your digestion moving, a pinch of turmeric to calm the inflammation, and a tiny pinch of pink salt.",
 "coloque uma fatia de gengibre fresco para fazer a digestão andar, uma pitada de cúrcuma para acalmar a inflamação, e uma pitadinha de sal rosa."),
("PROTOCOLO", "G", 0, "Mix it well, then drink this on an empty stomach every single morning.",
 "Misture bem e beba isso em jejum, toda santa manhã."),
("RESULTADO", "G", 0, "Your energy starts coming back, your clothes start fitting better, and you finally start feeling like yourself again.",
 "A sua energia começa a voltar, as roupas começam a servir melhor, e você finalmente começa a se sentir você de novo."),
("VIRADA: O LADO RUIM DA RECEITA", "H", 0, "But let's be honest, grating ginger and measuring six ingredients on an empty stomach, before your day even starts, is annoying, and nobody sticks with that.",
 "Mas vamos ser sinceros, ralar gengibre e medir seis ingredientes em jejum, antes do seu dia nem começar, é chato, e ninguém aguenta isso."),
("PONTE + PRODUTO NO GESTO", "I", 0, "That's why I just chew one Natural Rems Sea Moss gummy. Ginger, turmeric, manuka honey and vitamin C, all in one gummy.",
 "É por isso que eu só mastigo uma goma de Natural Rems Sea Moss. Gengibre, cúrcuma, mel de manuka e vitamina C, tudo numa goma só."),
("OBSTÁCULO + AUTORIDADE", "I", 0, "", ""),
("DIFERENCIAL", "I", 0, "This one is wild Irish sea moss, made in the USA, with less than one gram of sugar, and it tastes like green apple.",
 "Esta é de sea moss irlandês selvagem, feita nos EUA, com menos de um grama de açúcar, e tem gosto de maçã verde."),
("COMENTÁRIO", "I", 0, "If you're dealing with bloating every day, comment yes, so I know who I'm making the next video for.",
 "Se você convive com o inchaço todo dia, comenta yes, pra eu saber pra quem eu faço o próximo vídeo."),
("CTA AMAZON + DESTINO", "J", 0, CTA[0], CTA[1]),
("FOLLOW", "J", 1, "And don't forget to hit that follow button.", "E não esquece de apertar o botão de seguir."),
]
AUT["canela_limao"] = {
 "meredith": ("And trust me, baby, I have made sea moss my whole life. Most gummies on the shelf are packed with sugar, and that undoes this whole drink.",
              "E confia em mim, meu bem, eu faço sea moss a vida inteira. A maioria das gomas da prateleira é cheia de açúcar, e isso desfaz essa bebida inteira."),
 "marshall": ("I have gathered seaweed from this ocean my whole life. Most gummies on the shelf are packed with sugar, and that undoes this whole drink.",
              "Eu colho alga deste oceano a vida inteira. A maioria das gomas da prateleira é cheia de açúcar, e isso desfaz essa bebida inteira."),
 "cassidy": ("And I've been raking Irish moss off these rocks since I was a kid. Most gummies on the shelf are packed with sugar, which undoes this whole drink.",
             "E eu tiro Irish moss destas pedras com o rastelo desde criança. A maioria das gomas da prateleira é cheia de açúcar, o que desfaz essa bebida inteira."),
}

# ---------------------------------------------------------------- 2. bolinho de maçã com aveia (growth no original)
MODELO["bolinho_maca"] = dict(
    arq="snapinsta-1791928442044.mp4", dur="35,0s", pasta="r_1791928442044",
    desc="homem musculoso de regata branca e boné USA numa cozinha de armários de madeira; gancho = maçã vermelha na mão perto da lente; receita em closes rápidos da tigela; forno; prato com os bolinhos perto da lente",
    cta_orig="Comment yes if this helped and follow me for more recipes like this.",
    titulo="Bolinho de maçã, canela e aveia → Natural Rems Sea Moss")
VID["bolinho_maca"] = [
("GANCHO", "A", 1, "Did you know that", "Você sabia que"),
("RECEITA", "B", 1, "if you dice apples into a bowl,", "se você picar maçãs numa tigela,"),
("RECEITA", "C", 1, "add cinnamon", "colocar canela"),
("RECEITA", "D", 1, "and a couple of eggs,", "e uns dois ovos,"),
("RECEITA", "E", 1, "throw in some oats", "jogar um pouco de aveia"),
("RECEITA", "F", 1, "and a pinch of baking powder.", "e uma pitada de fermento."),
("RECEITA", "G", 1, "Mix it all together", "Misturar tudo"),
("RECEITA", "H", 1, "and scoop into mounds on a baking pan.", "e colocar em montinhos numa assadeira."),
("RECEITA", "I", 1, "Then bake at 350 degrees until golden brown.", "Depois assar a 180 graus até dourar."),
("RESULTADO", "J", 1, "You get apple fritters like these without spiking your blood sugar,",
 "Você ganha bolinhos de maçã como estes sem disparar o seu açúcar no sangue,"),
("RESULTADO", "K", 1, "and they honestly taste like a bakery made them.", "e sinceramente parecem feitos por uma padaria."),
("MECANISMO", "L", 0, "The oats and apples flood your gut with fiber that keeps you full and kills the sugar craving.",
 "A aveia e a maçã enchem o seu intestino de fibra, que te mantém saciada e mata a vontade de doce."),
("MECANISMO", "M", 0, "So your body finally gets a chance to let go of that stubborn belly fat.",
 "Então o seu corpo finalmente tem a chance de soltar aquela gordura teimosa da barriga."),
("DOR", "L", 0, "If you crave something sweet but you're trying to lose weight, these are genuinely the ones to make.",
 "Se você tem vontade de doce mas está tentando emagrecer, estes são de verdade os que você tem que fazer."),
("VIRADA: O LADO RUIM DA RECEITA", "N", 0, "But let's be real. Dicing, mixing and baking a whole tray every time the craving hits takes an hour you don't have.",
 "Mas vamos falar a verdade. Picar, misturar e assar uma assadeira inteira toda vez que a vontade bate leva uma hora que você não tem."),
("CATEGORIA + AUTORIDADE", "N", 0, "", ""),
("OBSTÁCULO", "N", 0, "But most sea moss gummies are loaded with sugar, the exact craving you were trying to kill.",
 "Mas a maioria das gomas de sea moss é carregada de açúcar, exatamente a vontade que você estava tentando matar."),
("PRODUTO NO GESTO", "O", 0, "The one I trust is Natural Rems Sea Moss. Wild Irish sea moss, apple, apple cider vinegar, ginger and dandelion, sixteen in one gummy.",
 "A que eu confio é a Natural Rems Sea Moss. Sea moss irlandês selvagem, maçã, vinagre de maçã, gengibre e dente-de-leão, dezesseis numa goma."),
("DIFERENCIAL", "O", 0, "Less than one gram of sugar, it tastes like green apple, and you just chew one a day with a meal.",
 "Menos de um grama de açúcar, tem gosto de maçã verde, e você só mastiga uma por dia com uma refeição."),
("COMENTÁRIO", "O", 0, "Comment yes if that sugar craving gets you every afternoon, so I know who needs the next one.",
 "Comenta yes se essa vontade de doce te pega toda tarde, pra eu saber quem precisa do próximo."),
("CTA AMAZON + DESTINO", "P", 0, CTA[0], CTA[1]),
("FOLLOW", "P", 1, "And don't forget to hit that follow button.", "E não esquece de apertar o botão de seguir."),
]
AUT["bolinho_maca"] = {
 "meredith": ("So on busy days, baby, I reach for what my grandmother gave me back in Kingston, sea moss. It feeds that same gut, no oven.",
              "Então nos dias corridos, meu bem, eu pego o que a minha avó me dava lá em Kingston, sea moss. Ele alimenta o mesmo intestino, sem forno."),
 "marshall": ("So on busy days I reach for what the ocean has given me for fifty years, sea moss. It feeds that same gut, no oven.",
              "Então nos dias corridos eu pego o que o oceano me dá há cinquenta anos, sea moss. Ele alimenta o mesmo intestino, sem forno."),
 "cassidy": ("So on busy days I reach for what I rake off these rocks every summer, sea moss. It feeds that same gut, no oven.",
             "Então nos dias corridos eu pego o que eu tiro destas pedras todo verão, sea moss. Ele alimenta o mesmo intestino, sem forno."),
}

# ---------------------------------------------------------------- 3. wrap de lentilha (growth no original)
MODELO["wrap_lentilha"] = dict(
    arq="snapinsta-1791928495894.mp4", dur="34,2s", pasta="r_1791928495894",
    desc="mulher loira de camisa branca dentro de um motorhome; gancho = lentilha vermelha despejada numa tigela de vidro com a câmera embaixo do vidro; mixer; massa na frigideira de ferro; sentada no banco com a pilha de wraps; saco de lentilha colado na lente",
    cta_orig="I share real recipes to boost your health, help with bloating, brain fog, immunity and just feel better. Comment yes if you want more like this and follow me so you don't miss the next one.",
    titulo="Wrap de lentilha vermelha → Natural Rems Sea Moss")
VID["wrap_lentilha"] = [
("GANCHO", "A", 1, "Did you know if you soak one cup of red lentils", "Você sabia que se você deixar uma xícara de lentilha vermelha de molho"),
("RECEITA", "B", 1, "in water for three hours, add a pinch of salt", "na água por três horas, colocar uma pitada de sal"),
("RECEITA", "C", 1, "and blend them smooth,", "e bater até ficar liso,"),
("RECEITA", "D", 1, "pour a ladle into a hot skillet", "despejar uma concha numa frigideira quente"),
("RECEITA", "E", 1, "and cook for two minutes on each side,", "e cozinhar dois minutos de cada lado,"),
("RESULTADO", "F", 0, "you end up with soft wraps that fold like a tortilla, made from one ingredient, zero flour, zero eggs, zero dairy.",
 "você fica com wraps macios que dobram como tortilha, feitos com um ingrediente só, zero farinha, zero ovo, zero laticínio."),
("MECANISMO", "G", 1, "Lentils are packed with fiber that feeds the good bacteria in your gut,",
 "A lentilha é cheia de fibra que alimenta as bactérias boas do seu intestino,"),
("MECANISMO", "H", 1, "and they carry enough plant protein to keep you full for hours,",
 "e ela tem proteína vegetal suficiente para te deixar saciada por horas,"),
("MECANISMO", "I", 1, "without the blood sugar crash you get from bread.", "sem a queda de açúcar no sangue que o pão te dá."),
("VIRADA: O LADO RUIM DA RECEITA", "J", 0, "But I'll be honest, soaking lentils three hours ahead and flipping them one by one at the stove does not happen on a busy weekday.",
 "Mas vou ser sincera, deixar lentilha de molho três horas antes e virar uma por uma no fogão não acontece num dia corrido de semana."),
("CATEGORIA + AUTORIDADE", "J", 0, "", ""),
("OBSTÁCULO", "J", 0, "But most sea moss gummies are packed with sugar, and that's the same blood sugar crash you just got rid of.",
 "Mas a maioria das gomas de sea moss é cheia de açúcar, e essa é a mesma queda de açúcar no sangue de que você acabou de se livrar."),
("PRODUTO NO GESTO", "K", 0, "The one I keep is Natural Rems Sea Moss. Wild Irish sea moss, elderberry, vitamin C and D3, and ginger for your gut, sixteen in one gummy.",
 "A que eu tenho em casa é a Natural Rems Sea Moss. Sea moss irlandês selvagem, sabugueiro, vitamina C e D3, e gengibre para o intestino, dezesseis numa goma."),
("DIFERENCIAL", "K", 0, "Less than one gram of sugar and no seaweed taste. One green apple gummy a day with a meal, and nothing to soak.",
 "Menos de um grama de açúcar e nenhum gosto de alga. Uma goma de maçã verde por dia com uma refeição, e nada de deixar de molho."),
("COMENTÁRIO", "K", 0, "Comment yes if bread leaves you bloated and crashing by the afternoon, so I know who needs this next.",
 "Comenta yes se o pão te deixa inchada e sem energia à tarde, pra eu saber quem precisa disso no próximo."),
("CTA AMAZON + DESTINO", "L", 0, CTA[0], CTA[1]),
("FOLLOW", "L", 1, "And don't forget to hit that follow button.", "E não esquece de apertar o botão de seguir."),
]
AUT["wrap_lentilha"] = {
 "meredith": ("So for the bloating and my immune system, I lean on what every auntie in my building swears by, sea moss.",
              "Então para o inchaço e para a minha imunidade, eu me apoio no que toda tia do meu prédio jura que funciona, sea moss."),
 "marshall": ("So for the bloating and my immune system, I lean on what the divers of my village have trusted for generations, sea moss.",
              "Então para o inchaço e para a minha imunidade, eu me apoio no que as mergulhadoras da minha vila confiam há gerações, sea moss."),
 "cassidy": ("So for the bloating and my immune system, I lean on what my family has hauled out of the Atlantic for generations, sea moss.",
             "Então para o inchaço e para a minha imunidade, eu me apoio no que a minha família tira do Atlântico há gerações, sea moss."),
}

# ---------------------------------------------------------------- 4. sorvete de banana (modelo em espanhol, growth)
MODELO["sorvete_banana"] = dict(
    arq="snapinsta-1791928419561.mp4", dur="53,9s", pasta="r_1791928419561",
    desc="mulher negra de cabelo cacheado, boné vermelho e blusa creme numa cozinha com bancada de mármore e janela; gancho = saco de banana congelada despejado no liquidificador colado na lente; cacau, pasta de amendoim, POV do liquidificador girando, leite, freezer visto de cima, tigela com sorvete; transições de glitch",
    cta_orig="Tengo recetas así para cualquier dulce que se te ocurra. Comenta scoop si quieres más como ésta y sígueme para que no te pierdas ni una.",
    titulo="Sorvete de banana com chocolate → Natural Rems Sea Moss")
VID["sorvete_banana"] = [
("GANCHO", "A", 0, "How old were you when you found out that if you put frozen bananas in a blender",
 "Quantos anos você tinha quando descobriu que se você colocar banana congelada no liquidificador"),
("RECEITA", "B", 1, "with a little cocoa powder", "com um pouquinho de cacau em pó"),
("RECEITA", "C", 1, "and peanut butter,", "e pasta de amendoim,"),
("RECEITA", "D", 0, "and blend it until it's completely smooth, you can turn it into creamy chocolate ice cream?",
 "e bater até ficar completamente liso, você consegue transformar isso num sorvete cremoso de chocolate?"),
("RECEITA", "E", 1, "Add a splash of milk", "Coloque um pouquinho de leite"),
("RECEITA", "F", 0, "and blend it all together until it's like soft chocolate ice cream, really thick.",
 "e bata tudo junto até ficar como um sorvete de chocolate macio, bem grosso."),
("RECEITA", "G", 0, "Pour it into a small container and put it in the freezer for about thirty minutes.",
 "Passe para um pote pequeno e coloque no freezer por uns trinta minutos."),
("RECEITA", "H", 1, "Then serve it in a bowl.", "Depois sirva numa tigela."),
("RESULTADO", "I", 0, "You get a creamy chocolate ice cream that doesn't just taste like the one from the ice cream shop, it's packed with potassium",
 "Você ganha um sorvete cremoso de chocolate que não só tem gosto de sorveteria, ele é cheio de potássio"),
("RESULTADO", "J", 0, "and made without all the refined sugar ice cream usually has. No refined sugar, no effort, just bananas.",
 "e é feito sem todo o açúcar refinado que o sorvete costuma ter. Sem açúcar refinado, sem esforço, só banana."),
("VIRADA: O LADO RUIM DA RECEITA", "J", 0, "Okay, a little effort. You freeze the bananas the night before, fight the blender, and wait thirty minutes when the craving is right now.",
 "Tá, um pouquinho de esforço. Você congela as bananas na noite anterior, briga com o liquidificador e espera trinta minutos quando a vontade é agora."),
("CATEGORIA + AUTORIDADE", "J", 0, "", ""),
("OBSTÁCULO", "J", 0, "But careful, most sea moss gummies are just candy, loaded with the same refined sugar this ice cream was made to avoid.",
 "Mas cuidado, a maioria das gomas de sea moss é só bala, carregada do mesmo açúcar refinado que este sorvete foi feito para evitar."),
("PRODUTO NO GESTO", "K", 0, "The one I trust is Natural Rems Sea Moss. Wild Irish sea moss and sixteen ingredients, with less than one gram of sugar and four calories.",
 "A que eu confio é a Natural Rems Sea Moss. Sea moss irlandês selvagem e dezesseis ingredientes, com menos de um grama de açúcar e quatro calorias."),
("COMENTÁRIO", "K", 0, "Comment yes if that sweet tooth gets you every night, so I know who needs my next recipe.",
 "Comenta yes se essa vontade de doce te pega toda noite, pra eu saber quem precisa da minha próxima receita."),
("CTA AMAZON + DESTINO", "L", 0, CTA[0], CTA[1]),
("FOLLOW", "L", 1, "And don't forget to hit that follow button.", "E não esquece de apertar o botão de seguir."),
]
AUT["sorvete_banana"] = {
 "meredith": ("So on those nights, baby, I chew one green apple gummy instead. It's sea moss, the same thing I've been blending in my kitchen since the eighties.",
              "Então nessas noites, meu bem, eu mastigo uma goma de maçã verde no lugar. É sea moss, a mesma coisa que eu bato na minha cozinha desde os anos oitenta."),
 "marshall": ("So on those nights I chew one green apple gummy instead. It is sea moss, the plant I have dived for since I was a girl.",
              "Então nessas noites eu mastigo uma goma de maçã verde no lugar. É sea moss, a planta atrás da qual eu mergulho desde menina."),
 "cassidy": ("So on those nights I chew one green apple gummy instead. It's sea moss, the same stuff my dad taught me to rake off these rocks.",
             "Então nessas noites eu mastigo uma goma de maçã verde no lugar. É sea moss, a mesma coisa que o meu pai me ensinou a tirar destas pedras."),
}

# Exceções por avatar e take: (video, avatar, número do take) -> (inglês, português).
# 2026-10-14 (Luigi, opção 1): o V09 da Marshall cortou em "and no" (26 palavras não couberam em 8s);
# a fala termina em "is annoying." e a virada continua de pé.
OVR = {
 ('sorvete_banana', 'cassidy', 14): ('The one I trust is Natural Rems Sea Moss. Wild Irish sea moss and sixteen ingredients.',
   'A que eu confio é a Natural Rems Sea Moss. Sea moss irlandês selvagem e dezesseis ingredientes, com menos de um grama de açúcar e quatro calorias. [fala ajustada ao take gerado]'),
 ('wrap_lentilha', 'cassidy', 13): ('The one I keep is Natural Rems Sea Moss. Wild Irish sea moss, elderberry, vitamin C and D3, and ginger for your gut.',
   'A que eu tenho em casa é a Natural Rems Sea Moss. Sea moss irlandês selvagem, sabugueiro, vitamina C e D3, e gengibre para o intestino, dezesseis numa goma. [fala ajustada ao take gerado]'),
 ('wrap_lentilha', 'marshall', 13): ('The one I keep is Natural Rems Sea Moss. Wild Irish sea moss, elderberry, vitamin C and D3, and ginger for your gut.',
   'A que eu tenho em casa é a Natural Rems Sea Moss. Sea moss irlandês selvagem, sabugueiro, vitamina C e D3, e gengibre para o intestino, dezesseis numa goma. [fala ajustada ao take gerado]'),
 ('wrap_lentilha', 'marshall', 6): ('you end up with soft wraps that fold like a tortilla, made from one ingredient, zero flour.',
   'você fica com wraps macios que dobram como tortilha, feitos com um ingrediente só, zero farinha, zero ovo, zero laticínio. [fala ajustada ao take gerado]'),
 ('wrap_lentilha', 'meredith', 13): ('The one I keep is Natural Rems Sea Moss. Wild Irish sea moss, elderberry, vitamin C and D3, and ginger for your gut.',
   'A que eu tenho em casa é a Natural Rems Sea Moss. Sea moss irlandês selvagem, sabugueiro, vitamina C e D3, e gengibre para o intestino, dezesseis numa goma. [fala ajustada ao take gerado]'),
 ('bolinho_maca', 'cassidy', 21): ("Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories.",
   'Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories. [fala ajustada ao take gerado: o take terminou antes da bio]'),
 ('bolinho_maca', 'cassidy', 18): ('The one I trust is Natural Rems Sea Moss. Wild Irish sea moss, apple, apple cider vinegar, ginger and dandelion.',
   'A que eu confio é a Natural Rems Sea Moss. Sea moss irlandês selvagem, maçã, vinagre de maçã, gengibre e dente-de-leão, dezesseis numa goma. [fala ajustada ao take gerado]'),
 ('bolinho_maca', 'marshall', 16): ('So on busy days I reach for what the ocean has given me for fifty years, sea moss. It feeds that same gut.',
   'Então nos dias corridos eu pego o que o oceano me dá há cinquenta anos, sea moss. Ele alimenta o mesmo intestino, sem forno. [take cortado pelo Flow: a fala termina em "gut."]'),
 ('bolinho_maca', 'marshall', 15): ("But let's be real. Dicing, mixing and baking a whole tray every time the craving hits takes an hour.",
   'Mas vamos falar a verdade. Picar, misturar e assar uma assadeira inteira toda vez que a vontade bate leva uma hora que você não tem. [take cortado pelo Flow: a fala termina em "Dicing."]'),
 ("bolinho_maca", "meredith", 16): ("So on busy days, baby, I reach for what my grandmother gave me back in Kingston, sea moss. It feeds that same gut.",
                                    "Então nos dias corridos, meu bem, eu pego o que a minha avó me dava lá em Kingston, sea moss. Ele alimenta o mesmo intestino."),
 ("canela_limao", "cassidy", 9): ("But let's be honest, grating ginger and measuring six ingredients on an empty stomach, before your day even starts, is annoying.",
                                  "Mas vamos ser sinceros, ralar gengibre e medir seis ingredientes em jejum, antes do seu dia nem começar, é chato."),
 ("canela_limao", "marshall", 9): ("But let's be honest, grating ginger and measuring six ingredients on an empty stomach, before your day even starts, is annoying.",
                                   "Mas vamos ser sinceros, ralar gengibre e medir seis ingredientes em jejum, antes do seu dia nem começar, é chato."),
}
