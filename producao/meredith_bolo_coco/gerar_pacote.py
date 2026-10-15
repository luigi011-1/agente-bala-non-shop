import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "_flow"))
from pacote_minimo import gerar  # noqa: E402

AVATAR = dict(
    anexo="meredith callahan .png",
    id=("Match the attached image exactly for the woman's identity and outfit: a woman around seventy with deep brown skin, "
        "dark freckles on her cheekbones, deep laugh lines, gold-capped front teeth, silver-gray locs piled high inside a "
        "tall emerald-green and saffron-yellow patterned head wrap, red reading glasses resting on the front of the wrap, "
        "large gold bamboo hoop earrings, a stack of thin gold bangles on her left wrist, a loose cream cotton short-sleeve "
        "blouse with green leaf embroidery at the neckline, and a rust-orange apron tied at the waist."),
    set=("She stands behind a mint-green speckled Formica kitchen table in her small Brooklyn apartment kitchen: wooden "
         "cabinets, a row of large glass jars of pale golden sea moss and a glass blender on the counter at the left, a window "
         "at the right showing a red brick building with black iron balconies under an overcast blue-gray sky, and a small American "
         "flag in a potted plant on the windowsill, in sharp focus."),
    nome="Meredith Callahan", ancora="producao/_ancoras/meredith_callahan_ancora.png",
    entrega="ENTREGA_MEREDITH.md", angulo="Ângulo 1 Sea Moss (conta da Meredith)", conta="Natural Rems Sea Moss (Meredith)",
    descr="a senhora de turbante verde e amarelo, blusa creme e avental laranja", cenario="da cozinha do Brooklyn",
    g3="'row of large glass jars of pale golden sea moss' + 'red brick building' + 'small American flag'",
    trava="Mesmo turbante verde e açafrão, mesmos óculos vermelhos, mesmas argolas e pulseiras de ouro, mesma blusa e avental, mesma mesa de fórmica e bandeira em todo K.")

MID = "She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression."
NEAR = "very close to the lens, large in frame and closer to the camera than her face"

KS = {
 1: ("Tigela de vidro colada na lente; ela despeja três ovos de uma tigelinha creme.",
     f"Hero: on the table in the lower foreground, {NEAR}: a large clear glass mixing bowl. She holds a small cream ceramic "
     "bowl of three cracked raw eggs tilted over it, the eggs sliding into the glass bowl, and an open tub of thick white "
     "Greek yogurt with a spoon stands beside the bowl. " + MID,
     ("0,0s (cena 1)", "tigela de vidro vazia + tigelinha creme com três ovos inclinada sobre ela + pote de iogurte grego", "~40%", "colada", "inclina a tigelinha de ovos sobre a tigela")),
 2: ("A tigela com a massa amarelada, coco ralado, baunilha e a forma forrada; ela bate e despeja na forma.",
     f"Hero: on the table in the lower foreground, {NEAR}: the clear glass mixing bowl of smooth pale yellow batter topped "
     "with a pile of white shredded coconut, a small bottle of vanilla extract and a loaf pan lined with parchment paper "
     "beside it. She whisks the batter with a metal balloon whisk. " + MID,
     ("5,9 a 9,7s (cenas 5 a 8)", "tigela de vidro com massa amarela + coco ralado + baunilha + forma forrada, fouet", "~45%", "colada", "bate com o fouet")),
 3: ("O bolo de coco dourado no papel manteiga, colado na lente; ela corta em pedaços.",
     f"Hero: on the table in the lower foreground, {NEAR}: a golden baked coconut loaf cake on crumpled parchment paper, its "
     "top sprinkled with toasted shredded coconut. She slices it into thick squares with a wide cake server. " + MID,
     ("11,3 e 14,2s (cenas 9 e 10)", "bolo de coco dourado no papel manteiga, coco tostado por cima, espátula de bolo", "~45%", "colado", "corta o bolo")),
 4: ("Ela segura um prato preto com duas fatias grossas de bolo de coco perto da lente.",
     f"Hero: she holds a round black plate out toward the camera with both hands, {NEAR}, with two thick golden squares of "
     "coconut cake on it, toasted shredded coconut scattered on top and on the plate. " + MID,
     ("24,0 e 31,6s (cenas 11 e 12)", "prato preto com duas fatias grossas de bolo de coco", "~35%", "colado, segurado nas mãos", "segura o prato com as duas mãos")),
}

TAKES = [
 ("T1", "Gancho", "Ela despeja os três ovos na tigela.", "How old were you when you found out that if you mixed three eggs into Greek yogurt,", "Quantos anos você tinha quando descobriu que se você misturar três ovos no iogurte grego,", 1),
 ("T2", "Receita", "Ela bate com coco e baunilha.", "whisk it together with shredded coconut and a little vanilla, then pour it into a mold,", "bater junto com coco ralado e um pouquinho de baunilha, e depois despejar numa forma,", 2),
 ("T3", "Receita + resultado", "Ela corta o bolo assado.", "bake it for thirty minutes, and let it chill. You end up with a fluffy coconut cake.", "assar por trinta minutos e deixar esfriar. Você termina com um bolo de coco fofinho.", 3),
 ("T4", "Benefício", "Ela mostra o prato com o bolo.", "It not only tastes amazing, but it is light on the stomach, loaded with healthy fats, and will not send your blood sugar through the roof, baby.", "Ele não só é uma delícia, como é leve pro estômago, cheio de gordura boa, e não vai mandar o seu açúcar no sangue lá pro teto, meu bem.", 4),
 ("T5", "Benefício", "Ela segue com o prato.", "And the best part? The eggs and yogurt carry a massive dose of protein. No refined sugar, no flour, high protein.", "E a melhor parte? Os ovos e o iogurte carregam uma dose enorme de proteína. Sem açúcar refinado, sem farinha, muita proteína.", 4),
 ("T6", "Autoridade", "Ela segue com o prato.", "I got recipes like this for every sweet treat you can think of.", "Eu tenho receitas assim pra todo doce que você imaginar.", 4),
 ("T7", "CTA + follow", "Ela fecha com o prato.", "Comment yes if you want more recipes like this, and don't forget to hit that follow button so you do not miss a single one.", "Comenta yes se você quer mais receitas assim, e não esquece de clicar no botão de seguir pra não perder nenhuma.", 4),
]

QUAL = ("**Vídeo: bolo de coco com ovos e iogurte grego.**\n\n"
        "**O que acontece:** a Meredith, na mesa de fórmica da cozinha dela, mistura ovos e iogurte grego, bate com coco ralado e "
        "baunilha, despeja na forma, corta o bolo assado e mostra o prato. Fala dos benefícios e fecha com comment yes e o "
        "lembrete do follow.\n\n"
        "**Gancho:** fala de abertura \"How old were you when you found out\" com ela despejando três ovos na tigela de vidro "
        "colada na lente.")

MAPA = "V01 a V03 usam o K de mesmo número; V04 a V07 usam a mesma imagem escolhida do K04 (plano único do prato)."
CAPCUT = ("Edição automática (`editar.py`, acabamento HyperFrames): legenda palavra por palavra, cortes de pausa, música a -18 dB "
          "da voz. Salvar os vídeos como V01 a V07. Sem Voice Changer. Legenda do post: `#ad #syntheticperformer #naturalrems` "
          "no topo, sem link; chave de conteúdo de IA ligada.")

if __name__ == "__main__":
    ok = gerar(D, "Sea Moss Growth · bolo de coco", QUAL, MAPA, TAKES, KS,
               "Modelo: smartphone frontal na altura do peito, cozinha cinza; cenário trocado pela cozinha da avatar (avatar fixo da conta).",
               CAPCUT, avatar=AVATAR)
    sys.exit(0 if ok else 1)
