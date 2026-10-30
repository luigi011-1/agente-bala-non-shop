# Lote Sea Moss VENDA a partir de receitas virais (2026-10-15). Formato de [[formato-receita-ponte-venda]].
# Corpo do modelo clonado; ponte = lado ruim de fazer a receita -> sea moss faz o mesmo trabalho (autoridade
# da conta) -> obstáculo (gomas comuns cheias de açúcar) -> Natural Rems -> yes -> Amazon -> bio -> follow.
# CTA (Luigi, 2026-10-15): "regra da amazon + link da bio + follow". Sem Stories neste lote.
# Cada take: (beat, setup, curta, ingles, portugues). "MUDO" no beat = take sem fala.
# AUT[video][avatar] substitui o take cujo beat contém "AUTORIDADE".
# Teto prático ~20 palavras por take nas avatares 60+ (lição do lote 13-14/10).

CTA = ("Search Natural Rems Sea Moss on Amazon. Or you can also find the link in my bio.",
       "Procure Natural Rems Sea Moss na Amazon. Ou você também encontra o link na minha bio.")
FOLLOW = ("And don't forget to hit that follow button.", "E não esquece de apertar o botão de seguir.")

VID = {}
MODELO = {}
AUT = {}
OVR = {}

# ---------------------------------------------------------------- V01. crosta na calha + água de limão (espanhol)
MODELO["crosta_limao"] = dict(
    arq="snapinsta-1792081855261.mp4", dur="41,9s", pasta="m_1792081855261",
    desc="homem de camisa azul num escritório com estante; gancho = calha transparente com crosta escura rachada recebendo água com limão e fibra em pó sem efeito, depois o líquido amarelo da receita derretendo a crosta; receita em closes na panela; ele segura o copo e fala até o fim",
    cta_orig="Si quieren más recetas como esta comenten libro abajo, pero primero asegúrense de seguirme para que pueda llegarles.",
    titulo="Crosta na calha e água de limão → Natural Rems Sea Moss")
VID["crosta_limao"] = [
("GANCHO", "A", 1, "Stop drinking lemon water, it's not enough.",
 "Pare de tomar água com limão, não é suficiente."),
("GANCHO", "B", 0, "You can add apple cider vinegar, fiber powder, whatever, and it won't clean out what's been building up for years.",
 "Você pode colocar vinagre de maçã, fibra em pó, o que for, e não vai limpar o que está acumulado há anos."),
("GANCHO", "C", 1, "Let me show you what does work.", "Deixa eu te mostrar o que funciona."),
("RECEITA", "D", 0, "Put a pot of water on, chop up a fresh lemon, and drop it into the boiling water.",
 "Coloque uma panela com água no fogo, pique um limão fresco e jogue na água fervendo."),
("RECEITA", "E", 1, "Add a teaspoon of chia,", "Coloque uma colher de chá de chia,"),
("RECEITA", "F", 1, "one of turmeric,", "uma de cúrcuma,"),
("RECEITA", "G", 1, "one of fresh ginger, and finish with a pinch of black pepper.",
 "uma de gengibre fresco, e termine com uma pitada de pimenta-do-reino."),
("PROTOCOLO", "H", 1, "Let it boil for ten minutes and strain it.", "Deixe ferver dez minutos e coe."),
("RESULTADO", "I", 0, "This wakes up your whole system, the inflammation calms down, your gut finally feels clean, and your body feels lighter.",
 "Isso desperta o seu sistema inteiro, a inflamação acalma, o seu intestino finalmente fica limpo, e o seu corpo fica mais leve."),
("VIRADA: O LADO RUIM DA RECEITA", "I", 0, "But I'll be honest, buying fresh lemon and ginger every single week adds up, and half of it goes bad.",
 "Mas vou ser sincera, comprar limão e gengibre frescos toda semana pesa no bolso, e metade estraga."),
("CATEGORIA + AUTORIDADE", "I", 0, "", ""),
("OBSTÁCULO", "I", 0, "But careful, most sea moss gummies are coated in sugar, and that buries your gut right back under the crust.",
 "Mas cuidado, a maioria das gomas de sea moss é coberta de açúcar, e isso enterra o seu intestino de novo debaixo da crosta."),
("PRODUTO NO GESTO", "J", 0, "My pick is Natural Rems Sea Moss. Ginger, turmeric and black pepper, just like this pot, in one gummy.",
 "A minha escolhida é a Natural Rems Sea Moss. Gengibre, cúrcuma e pimenta-do-reino, igual a esta panela, numa goma só."),
("DIFERENCIAL", "J", 0, "Sixteen ingredients, wild Irish sea moss, less than one gram of sugar, and it tastes like green apple.",
 "Dezesseis ingredientes, sea moss irlandês selvagem, menos de um grama de açúcar, e tem gosto de maçã verde."),
("COMENTÁRIO", "J", 0, "Comment yes if you feel heavy and bloated no matter how clean you eat, so I know who needs this.",
 "Comenta yes se você se sente pesada e inchada não importa o quanto coma limpo, pra eu saber quem precisa disso."),
("CTA AMAZON + BIO", "K", 0, CTA[0], CTA[1]),
("FOLLOW", "K", 1, FOLLOW[0], FOLLOW[1]),
]
AUT["crosta_limao"] = {
 "cassidy": ("So I lean on what grows on the rocks right under this dock, sea moss. Nothing to spoil.",
             "Então eu me apoio no que cresce nas pedras bem debaixo deste cais, sea moss. Nada pra estragar."),
 "marshall": ("So I lean on what the tide brings to this shore every morning, sea moss. Nothing to spoil.",
              "Então eu me apoio no que a maré traz pra esta praia toda manhã, sea moss. Nada pra estragar."),
 "meredith": ("So, baby, I lean on what every Jamaican kitchen kept in a jar, sea moss. Nothing to spoil.",
              "Então, meu bem, eu me apoio no que toda cozinha jamaicana guardava num pote, sea moss. Nada pra estragar."),
}

# ---------------------------------------------------------------- V02. intestino transparente + chá de chia
MODELO["intestino_chia"] = dict(
    arq="snapinsta-1792081815692.mp4", dur="47,0s", pasta="m_1792081815692",
    desc="homem de cabelo longo e polo preta numa cozinha branca com bandeira dos EUA; gancho = modelo transparente de intestino cheio de grãos recebendo chia, água com limão, suco de ameixa e o chá amarelo; receita no fogareiro de indução; bandeja de madeira com a caneca e os ingredientes; livro 'Ancient Remedy Bible' na mão diante da estante no CTA",
    cta_orig="This is one of 53 remedies in my ancient remedies Bible. Comment, book, and I'll send it to you. Follow me so it reaches you.",
    titulo="Intestino transparente e chá de chia → Natural Rems Sea Moss")
VID["intestino_chia"] = [
("GANCHO", "A", 0, "Stop drinking chia seeds, they don't fix your constipation. The best drink for constipation is not apple cider vinegar,",
 "Pare de tomar semente de chia, ela não resolve a sua prisão de ventre. A melhor bebida para a prisão de ventre não é vinagre de maçã,"),
("GANCHO", "B", 1, "it's not lemon water,", "não é água com limão,"),
("GANCHO", "C", 1, "and it's definitely not prune juice.", "e com certeza não é suco de ameixa."),
("GANCHO", "D", 1, "Chia on its own does nothing.", "Chia sozinha não faz nada."),
("GANCHO", "E", 1, "Here is what actually works.", "Isto é o que funciona de verdade."),
("RECEITA", "F", 1, "Get a pot of water going and squeeze in a lemon.", "Ponha uma panela de água no fogo e esprema um limão."),
("RECEITA", "G", 1, "Add a tablespoon of chia seeds,", "Coloque uma colher de sopa de semente de chia,"),
("RECEITA", "H", 1, "a thumb of fresh grated ginger,", "um dedo de gengibre fresco ralado,"),
("RECEITA", "I", 1, "and a teaspoon of turmeric.", "e uma colher de chá de cúrcuma."),
("PROTOCOLO", "J", 1, "Let it simmer for ten minutes,", "Deixe ferver em fogo baixo por dez minutos,"),
("RESULTADO", "K", 0, "then strain it. This feeds your gut and gets everything moving. The bloating clears, and your whole body feels lighter.",
 "depois coe. Isso alimenta o seu intestino e faz tudo andar. O inchaço some, e o seu corpo inteiro fica mais leve."),
("MECANISMO", "K", 0, "Nobody can patent ginger, turmeric, or lemon, so nobody spends millions telling you about them.",
 "Ninguém consegue patentear gengibre, cúrcuma ou limão, então ninguém gasta milhões te contando sobre eles."),
("VIRADA: O LADO RUIM DA RECEITA", "K", 0, "But let's be honest, straining chia slime out of a pot while turmeric stains everything yellow gets old fast.",
 "Mas vamos ser sinceros, coar gosma de chia de uma panela enquanto a cúrcuma mancha tudo de amarelo cansa rápido."),
("CATEGORIA + AUTORIDADE", "K", 0, "", ""),
("OBSTÁCULO", "K", 0, "And most sea moss gummies are packed with sugar, the last thing a stuck gut needs.",
 "E a maioria das gomas de sea moss é cheia de açúcar, a última coisa que um intestino travado precisa."),
("PRODUTO NO GESTO", "L", 0, "Mine is Natural Rems Sea Moss. Ginger, turmeric and vitamin C, sixteen ingredients in one green apple gummy.",
 "A minha é a Natural Rems Sea Moss. Gengibre, cúrcuma e vitamina C, dezesseis ingredientes numa goma de maçã verde."),
("DIFERENCIAL", "L", 0, "Wild Irish sea moss, made in the USA, under one gram of sugar, one a day with a meal.",
 "Sea moss irlandês selvagem, feita nos EUA, menos de um grama de açúcar, uma por dia com uma refeição."),
("COMENTÁRIO", "L", 0, "Comment yes if your gut feels stuck no matter what you drink, so I know who needs the next one.",
 "Comenta yes se o seu intestino parece travado não importa o que você beba, pra eu saber quem precisa do próximo."),
("CTA AMAZON + BIO", "M", 0, CTA[0], CTA[1]),
("FOLLOW", "M", 1, FOLLOW[0], FOLLOW[1]),
]
AUT["intestino_chia"] = {
 "cassidy": ("So I reach for what dries on that rack behind me every August, sea moss. Same gut work, no strainer.",
             "Então eu pego o que seca naquela estante atrás de mim todo agosto, sea moss. Mesmo trabalho no intestino, sem coador."),
 "marshall": ("So I reach for what I still pull off the reef by hand, sea moss. Same gut work, no strainer.",
              "Então eu pego o que eu ainda tiro do recife com a mão, sea moss. Mesmo trabalho no intestino, sem coador."),
 "meredith": ("So, baby, I go back to what my mama soaked every Sunday, sea moss. Same gut work, no strainer.",
              "Então, meu bem, eu volto pro que a minha mãe deixava de molho todo domingo, sea moss. Mesmo trabalho no intestino, sem coador."),
}

# ---------------------------------------------------------------- V03. banana com canela + vitamina
MODELO["banana_canela"] = dict(
    arq="snapinsta-1792081717971.mp4", dur="35,3s", pasta="m_1792081717971",
    desc="homem de regata branca e boné azul numa cozinha de armários azul-marinho; gancho = canela despejada sobre três bananas descascadas colada na lente, depois push-in até o macro; receita no liquidificador; copo da vitamina na mão; fecho sentado no sofá com o copo",
    cta_orig="If you want more simple weight loss recipes that kill your cravings in a healthy way, comment yes and follow me so you don't miss the next one.",
    titulo="Banana com canela e vitamina → Natural Rems Sea Moss")
VID["banana_canela"] = [
("GANCHO", "A", 1, "Put cinnamon on a banana and just watch what happens.",
 "Coloque canela numa banana e só observe o que acontece."),
("GANCHO", "B", 0, "Big Pharma does not want you to know this, because they would lose billions of dollars overnight.",
 "A grande indústria farmacêutica não quer que você saiba disso, porque perderia bilhões de dólares da noite pro dia."),
("RECEITA", "C", 1, "Add one fresh banana to a blender,", "Coloque uma banana fresca no liquidificador,"),
("RECEITA", "D", 1, "a teaspoon of cinnamon, squeeze in half a lemon,", "uma colher de chá de canela, esprema meio limão,"),
("RECEITA", "E", 1, "add a glass of water,", "coloque um copo de água,"),
("RECEITA", "F", 1, "and blend this whole thing until it is smooth.", "e bata tudo isso até ficar liso."),
("RESULTADO", "G", 1, "This smoothie hits your insides like a reset button you never knew existed.",
 "Essa vitamina bate no seu organismo como um botão de reiniciar que você nem sabia que existia."),
("RESULTADO", "G", 1, "It calms the bloating, keeps you full for hours, and keeps your sugar cravings in check.",
 "Ela acalma o inchaço, te deixa saciada por horas, e segura a sua vontade de doce."),
("VIRADA: O LADO RUIM DA RECEITA", "H", 0, "But let's be real, bananas go brown in two days, and scrubbing a blender every single morning is a chore.",
 "Mas vamos falar a verdade, banana escurece em dois dias, e lavar liquidificador toda santa manhã é um saco."),
("CATEGORIA + AUTORIDADE", "H", 0, "", ""),
("OBSTÁCULO", "H", 0, "But most sea moss gummies are loaded with sugar, and sugar is exactly what feeds those cravings.",
 "Mas a maioria das gomas de sea moss é carregada de açúcar, e açúcar é exatamente o que alimenta essa vontade."),
("PRODUTO NO GESTO", "I", 0, "I chew Natural Rems Sea Moss. Ashwagandha, apple cider vinegar and vitamin C, sixteen ingredients in one gummy.",
 "Eu mastigo Natural Rems Sea Moss. Ashwagandha, vinagre de maçã e vitamina C, dezesseis ingredientes numa goma."),
("DIFERENCIAL", "I", 0, "Under one gram of sugar, four calories, and it tastes like green apple, not seaweed.",
 "Menos de um grama de açúcar, quatro calorias, e tem gosto de maçã verde, não de alga."),
("COMENTÁRIO", "I", 0, "Comment yes if sugar cravings win every night in your house, so I know who this is for.",
 "Comenta yes se a vontade de doce ganha toda noite na sua casa, pra eu saber pra quem é isso."),
("CTA AMAZON + BIO", "J", 0, CTA[0], CTA[1]),
("FOLLOW", "J", 1, FOLLOW[0], FOLLOW[1]),
]
AUT["banana_canela"] = {
 "cassidy": ("So on busy mornings I trust what I haul up every low tide, sea moss. No blender.",
             "Então nas manhãs corridas eu confio no que eu puxo toda maré baixa, sea moss. Sem liquidificador."),
 "marshall": ("So on busy mornings I trust what I have dried on these bamboo mats for decades, sea moss. No blender.",
              "Então nas manhãs corridas eu confio no que eu seco nestas esteiras de bambu há décadas, sea moss. Sem liquidificador."),
 "meredith": ("So on busy mornings, baby, I trust what Jamaicans have stirred into drinks for generations, sea moss. No blender.",
              "Então nas manhãs corridas, meu bem, eu confio no que os jamaicanos mexem nas bebidas há gerações, sea moss. Sem liquidificador."),
}

# ---------------------------------------------------------------- V04. máscara de vaselina e bicarbonato (espanhol)
MODELO["mascara_vaselina"] = dict(
    arq="snapinsta-1792081632145.mp4", dur="33,4s", pasta="m_1792081632145",
    desc="homem grisalho de óculos âmbar e camisa jeans numa varanda de subúrbio com bandeira dos EUA; gancho = bicarbonato despejado dentro do pote de vaselina; receita em colheres sobre uma tigela de vidro na mesa de madeira; tigela com o creme branco colada na lente até o fim",
    cta_orig="Comenta libro y te enviaré mi antigua Biblia de sanación. Pero tienes que seguirme o no podré comunicarme contigo.",
    titulo="Máscara de vaselina e bicarbonato → Natural Rems Sea Moss")
VID["mascara_vaselina"] = [
("GANCHO", "A", 0, "Mix petroleum jelly with baking soda, and you won't believe it. The pharmacies don't want you to know this.",
 "Misture vaselina com bicarbonato, e você não vai acreditar. As farmácias não querem que você saiba disso."),
("RECEITA", "B", 1, "One teaspoon of petroleum jelly, one teaspoon of honey,", "Uma colher de chá de vaselina, uma colher de chá de mel,"),
("RECEITA", "C", 0, "one to two teaspoons of baking soda, and one teaspoon of coconut oil in a bowl. Mix for one minute,",
 "uma a duas colheres de chá de bicarbonato, e uma colher de chá de óleo de coco numa tigela. Misture por um minuto,"),
("PROTOCOLO", "D", 1, "apply it to your face, leave it on for fifteen minutes, and rinse with warm water.",
 "aplique no rosto, deixe por quinze minutos e enxágue com água morna."),
("RESULTADO", "D", 1, "This removes dead skin, brightens your face, fades dark spots, and gives you a natural glow.",
 "Isso tira a pele morta, ilumina o rosto, clareia as manchas e te dá um brilho natural."),
("VIRADA: O LADO RUIM DA RECEITA", "E", 0, "Okay, real talk, baking soda stings, and fifteen minutes with goo on your face every night? Nobody keeps that up.",
 "Tá, falando sério, bicarbonato arde, e quinze minutos com gosma no rosto toda noite? Ninguém aguenta."),
("CATEGORIA + AUTORIDADE", "E", 0, "", ""),
("OBSTÁCULO", "E", 0, "But most sea moss gummies are packed with sugar, and sugar shows up on your skin.",
 "Mas a maioria das gomas de sea moss é cheia de açúcar, e o açúcar aparece na sua pele."),
("PRODUTO NO GESTO", "F", 0, "What I take is Natural Rems Sea Moss. Vitamin C, manuka honey and burdock root, sixteen ingredients in one gummy.",
 "O que eu tomo é a Natural Rems Sea Moss. Vitamina C, mel de manuka e raiz de bardana, dezesseis ingredientes numa goma."),
("DIFERENCIAL", "F", 0, "It's wild Irish sea moss, made right here in the USA, with no seaweed taste at all.",
 "É sea moss irlandês selvagem, feita aqui mesmo nos EUA, sem gosto nenhum de alga."),
("COMENTÁRIO", "F", 0, "Comment yes if your skin looks tired no matter what you put on it, so I know you're out there.",
 "Comenta yes se a sua pele parece cansada não importa o que você passe, pra eu saber que você está aí."),
("CTA AMAZON + BIO", "G", 0, CTA[0], CTA[1]),
("FOLLOW", "G", 1, FOLLOW[0], FOLLOW[1]),
]
AUT["mascara_vaselina"] = {
 "cassidy": ("For my skin, after forty winters of wind on this dock, I work from the inside, with sea moss.",
             "Pra minha pele, depois de quarenta invernos de vento neste cais, eu trabalho de dentro pra fora, com sea moss."),
 "marshall": ("For my skin, after a lifetime of salt and sun, I work from the inside, with sea moss.",
              "Pra minha pele, depois de uma vida inteira de sal e sol, eu trabalho de dentro pra fora, com sea moss."),
 "meredith": ("For my skin, baby, I work from the inside, with the sea moss I've had in my tea for decades.",
              "Pra minha pele, meu bem, eu trabalho de dentro pra fora, com o sea moss que eu ponho no meu chá há décadas."),
}
