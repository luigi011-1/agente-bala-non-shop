import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "_flow"))
from pacote_minimo import gerar  # noqa: E402

MID = "She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression."

KS = {
 1: ("Travessa de vidro na mesa colada na lente; ela sentada atrás despejando um líquido âmbar de uma garrafa sem rótulo e chacoalhando um pote de canela em pó.",
     "Hero: a clear rectangular glass baking dish sits on the black table in the lower foreground, very close to the lens, large "
     "in frame and closer to the camera than her face, already holding a layer of cinnamon powder. She sits behind it, pouring a "
     "thin stream of amber liquid from a plain amber glass bottle in her right hand while shaking cinnamon powder from a tall "
     "brown cinnamon shaker in her left hand into the dish, with an intense secretive expression. " + MID,
     ("0,0s (gancho, cena 1)", "travessa de vidro retangular + garrafa âmbar sem rótulo + pote de canela", "~40%", "colada, mais perto que o rosto", "sentada, despejando com as duas mãos")),
 2: ("Ela em pé atrás da mesa, mãos na borda, a travessa com a mistura âmbar de canela colada na lente; plano único que serve aos takes T2 a T14.",
     "Hero: the clear rectangular glass baking dish filled with a thick amber cinnamon mixture sits on the black table in the "
     "lower foreground, very close to the lens, large in frame and closer to the camera than her face. She stands behind it, "
     "chest up, leaning forward with both hands resting on the edge of the table, serious and urgent expression. " + MID,
     ("6,5s a 91,8s (plano único depois do flash)", "travessa de vidro com a mistura âmbar de canela", "~30%", "colada", "em pé, mãos na borda da mesa, inclinada pra câmera")),
}

L = [
 ("T1", "Gancho · a mistura", "Mix alcohol with cinnamon powder. I know it sounds ridiculous, but you will thank me for the rest of your life.", "Misture álcool com canela em pó. Eu sei que parece ridículo, mas você vai me agradecer pelo resto da vida."),
 ("T2", "Segredo", "Keep your mouth shut after you watch this. Do not tell anyone. Not everyone is going to understand why this simple remedy works.", "Fique de boca fechada depois de ver isso. Não conte pra ninguém. Nem todo mundo vai entender por que esse remédio simples funciona."),
 ("T3", "Não rola", "Keep your mouth shut after you watch. I do not know your name, but do not scroll.", "Fique de boca fechada depois de ver. Eu não sei o seu nome, mas não passa o vídeo."),
 ("T4", "Aviso final + a promessa", "Because if this reached you today, it reached you as a final warning. A powerful wave of stamina, vitality, and full body wellness is heading your way.", "Porque se isso chegou em você hoje, chegou como um último aviso. Uma onda forte de disposição, vitalidade e bem-estar no corpo inteiro está vindo na sua direção."),
 ("T5", "É aqui que vira", "Do not tell anyone, but this is where it turns. The constant fatigue and strain do not have to stay.", "Não conta pra ninguém, mas é aqui que vira. O cansaço e o desgaste constantes não precisam ficar."),
 ("T6", "O que eu já vi nas clientes", "I have watched energy and deep recovery walk back into the lives of the women I coach.", "Eu já vi a energia e a recuperação profunda voltarem pra vida das mulheres que eu acompanho."),
 ("T7", "Feche a mão", "Before you scroll, close your right hand and listen until the end. This video is not for everyone.", "Antes de passar, feche a mão direita e ouça até o fim. Esse vídeo não é pra todo mundo."),
 ("T8", "Te achou por um motivo", "It found you for a reason. If you skip right now, you lose it.", "Ele te achou por um motivo. Se você pular agora, você perde."),
 ("T9", "Algo vai acontecer", "Something very unusual is about to happen to your health. The inflammation keeping you trapped in daily fatigue starts breaking.", "Algo muito incomum está pra acontecer com a sua saúde. A inflamação que te prende no cansaço de todo dia começa a se quebrar."),
 ("T10", "O cansaço começa a sair", "The physical strain on your body starts going out. In the next seven minutes, the low energy that was following you is going to start lifting.", "O desgaste físico no seu corpo começa a sair. Nos próximos sete minutos, a energia baixa que estava te seguindo vai começar a levantar."),
 ("T11", "Volte em sete minutos", "So send this video to yourself right now, because in seven minutes you are going to come back to confirm the shift for yourself.", "Então manda esse vídeo pra você mesma agora, porque em sete minutos você vai voltar pra confirmar a virada com os seus olhos."),
 ("T12", "Salve e dois toques", "Now open your hand and save this video, so you have it. Double tap quickly on your screen, so it stays in your feed.", "Agora abra a mão e salve esse vídeo, pra ter ele com você. Dê dois toques rápidos na tela, pra ele ficar no seu feed."),
 ("T13", "Comente yes + aviso", "Comment yes so I can see you did everything. But pay close attention. This is fragile, and poor habits can completely undo it.", "Comenta yes pra eu ver que você fez tudo. Mas presta muita atenção. Isso é frágil, e maus hábitos podem desfazer tudo."),
 ("T14", "Follow pra segunda parte", "So follow me right now, because the second part of this is coming next, and you do not want to miss it.", "Então me segue agora, porque a segunda parte disso vem a seguir, e você não vai querer perder."),
]
TAKES = [(t, b, "Despejando a mistura na travessa." if t == "T1" else "Ela fala atrás da travessa.", en, pt, 1 if t == "T1" else 2)
         for t, b, en, pt in L]

QUAL = ("**Vídeo: canela e o aviso (\"keep your mouth shut\").**\n\n"
        "**O que acontece:** ela despeja um líquido âmbar e canela numa travessa e diz que parece ridículo, mas a pessoa vai agradecer. "
        "Depois, num plano único atrás da travessa, segura a atenção com comandos de segredo e retenção (boca fechada, mão fechada, "
        "volte em sete minutos), promete energia e recuperação, pede salvar, dois toques e comentar yes, e fecha pedindo o follow "
        "para a segunda parte. A receita nunca é explicada, igual ao modelo.\n\n"
        "**Gancho:** fala de abertura \"Mix alcohol with cinnamon powder.\" com ela despejando a garrafa âmbar e a canela na travessa "
        "de vidro colada na lente.")

MAPA = ("Dois K para catorze V: **V01 usa K01** (gancho); **V02 a V14 usam todos a mesma imagem do K02** (plano único do modelo, "
        "igual nos cortes).")
CAPCUT = ("Edição automática (`editar.py`, estilo FitWell): ritmo ~3,8 palavras/s, sem silêncio, legenda serifada branca, "
          "sem light leak, música a -25 dB da voz. Salvar os vídeos como V01 a V14: a ordem dos takes de plano único vem da fala. "
          "Sem Voice Changer. Marcar o post como conteúdo gerado por IA.")

if __name__ == "__main__":
    ok = gerar(D, "FitWell Growth · canela e o aviso", QUAL, MAPA, TAKES, KS,
               "Modelo: gancho com a câmera um pouco acima da bancada, depois plano único frontal na altura do peito; cenário trocado pelo box da avatar.", CAPCUT)
    sys.exit(0 if ok else 1)
