# FICHA DO FRAME · brandon_seamoss_muffin

Regra e método: `GATE_VISUAL.md` Parte 6. Cada K sai daqui, nunca da memória. O frame do modelo manda no
CONTEÚDO (forma, quadro, distância, câmera, pose, o que está em quadro); o gate manda no ACABAMENTO e impõe o
piso de proximidade do herói. A evidência de cada OK é um trecho que existe literalmente no K
(conferido por `gerar_pacote.py` com assert antes de gravar).

## K01
Frame: `input/frames_modelo/K01_modelo.png`
Take: T1
Herói: o ralador de inox de quatro faces em pé dentro da tigela branca com cenoura ralada, a cenoura esfregada nas lâminas
Termos de forma: "four-sided box grater" · "half full of bright orange finely grated carrot"
Quadro: no K: fill the lower 45 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 30 centimeters from the bowl and the grater
Câmera: phone at her chest height, tilted down toward the bowl, standard 1x lens, light handheld
Pose: Brandon leans over the black table toward the lens, grating the carrot into the bowl
Lista fechada: tigela, ralador, cenoura, mãos, avatar; mesa sem mais nada
Frame 0: cenoura no meio do movimento sobre o ralador, um monte de cenoura ralada já na tigela
Desvio (acabamento ou avatar fixo): cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); óculos e camiseta cinza do modelo → identidade e roupa da âncora; luz neutra (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "four-sided box grater" · "half full of bright orange finely grated carrot" |
| F2 quanto do quadro | OK | "fill the lower 45 percent of the frame" |
| F3 distancia da lente | OK | "about 30 centimeters from the bowl and the grater" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon leans over the black table toward the lens," |
| F6 lista fechada | OK | "In the lower foreground" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K02
Frame: `input/frames_modelo/K02_modelo.png`
Take: T2
Herói: a tigela de cenoura ralada no centro-baixo com os ingredientes em volta e a aveia caindo
Termos de forma: "glass measuring cup of rolled oats" · "half full of bright orange finely grated carrot"
Quadro: no K: fills the lower 30 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 55 centimeters from the bowl
Câmera: phone at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld
Pose: Brandon stands behind the black table, tipping the cup of oats into the bowl
Lista fechada: tigela, aveia, dois ovos, mel, canela com colher, avatar
Frame 0: primeiros flocos de aveia caindo do copo medidor
Desvio (acabamento ou avatar fixo): cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); óculos e camiseta cinza do modelo → identidade e roupa da âncora; luz neutra (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "glass measuring cup of rolled oats" · "half full of bright orange finely grated carrot" |
| F2 quanto do quadro | OK | "fills the lower 30 percent of the frame" |
| F3 distancia da lente | OK | "about 55 centimeters from the bowl" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon stands behind the black table, tipping the cup" |
| F6 lista fechada | OK | "On the black table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K03
Frame: `input/frames_modelo/K03_modelo.png`
Take: T3
Herói: o ovo sendo quebrado em cima da tigela
Termos de forma: "white egg cracked open over the bowl"
Quadro: no K: fills the lower 30 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 55 centimeters from the bowl
Câmera: phone at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld
Pose: Brandon stands behind the black table, cracking an egg over the bowl with both hands
Lista fechada: tigela com cenoura e aveia, ovo na mão, mel, canela, avatar
Frame 0: casca aberta logo acima da tigela, gema ainda não caiu
Desvio (acabamento ou avatar fixo): cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); óculos e camiseta cinza do modelo → identidade e roupa da âncora; luz neutra (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "white egg cracked open over the bowl" |
| F2 quanto do quadro | OK | "fills the lower 30 percent of the frame" |
| F3 distancia da lente | OK | "about 55 centimeters from the bowl" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon stands behind the black table, cracking an egg" |
| F6 lista fechada | OK | "On the black table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K04
Frame: `input/frames_modelo/K04_modelo.png`
Take: T4
Herói: o fio grosso de mel âmbar caindo do copinho de vidro na tigela
Termos de forma: "small clear glass cup of amber raw honey"
Quadro: no K: fills the lower 30 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 50 centimeters from the bowl
Câmera: phone at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld
Pose: Brandon stands behind the black table, pouring honey from the glass cup into the bowl
Lista fechada: tigela, copinho de mel, canela com colher, avatar
Frame 0: o primeiro fio de mel saindo do copinho
Desvio (acabamento ou avatar fixo): cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); óculos e camiseta cinza do modelo → identidade e roupa da âncora; luz neutra (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "small clear glass cup of amber raw honey" |
| F2 quanto do quadro | OK | "fills the lower 30 percent of the frame" |
| F3 distancia da lente | OK | "about 50 centimeters from the bowl" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon stands behind the black table, pouring honey" |
| F6 lista fechada | OK | "On the black table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K05
Frame: `input/frames_modelo/K05_modelo.png`
Take: T5
Herói: a colher de chá cheia de canela logo acima da tigela
Termos de forma: "measuring teaspoon heaped with ground cinnamon"
Quadro: no K: fills the lower 30 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 50 centimeters from the bowl
Câmera: phone at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld
Pose: Brandon stands behind the black table, holding the teaspoon of cinnamon over the bowl
Lista fechada: tigela, colher de canela, tigelinha de canela, avatar
Frame 0: colher parada acima da tigela, canela ainda não caiu
Desvio (acabamento ou avatar fixo): cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); óculos e camiseta cinza do modelo → identidade e roupa da âncora; luz neutra (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "measuring teaspoon heaped with ground cinnamon" |
| F2 quanto do quadro | OK | "fills the lower 30 percent of the frame" |
| F3 distancia da lente | OK | "about 50 centimeters from the bowl" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon stands behind the black table, holding the" |
| F6 lista fechada | OK | "On the black table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K06
Frame: `input/frames_modelo/K06_modelo.png`
Take: T6
Herói: a tigela inclinada de massa laranja e a forma de 12 com forminhas de papel, a colherada caindo
Termos de forma: "thick orange carrot oat batter" · "12-cup muffin tin lined with white paper cups"
Quadro: no K: fill the lower 50 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 35 centimeters from the tilted bowl and the muffin tin
Câmera: phone at her chest height, tilted down toward the tin, standard 1x lens, light handheld
Pose: Brandon leans over the black table, spooning batter from the tilted bowl into the muffin tin
Lista fechada: tigela de massa, colher, forma com forminhas, avatar
Frame 0: a primeira colherada caindo numa forminha vazia
Desvio (acabamento ou avatar fixo): cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); óculos e camiseta cinza do modelo → identidade e roupa da âncora; luz neutra (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "thick orange carrot oat batter" · "12-cup muffin tin lined with white paper cups" |
| F2 quanto do quadro | OK | "fill the lower 50 percent of the frame" |
| F3 distancia da lente | OK | "about 35 centimeters from the tilted bowl and the muffin tin" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon leans over the black table, spooning batter" |
| F6 lista fechada | OK | "Her left hand tilts the white mixing bowl full of thick orange carrot oat batter toward the lens" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K07
Frame: `input/frames_modelo/K07_modelo.png`
Take: T7
Herói: o muffin de cenoura assado na mão, colado na lente, e a forma cheia na mesa
Termos de forma: "baked carrot oat muffin with a domed golden orange top" · "12-cup muffin tin filled with baked"
Quadro: no K: fills about 18 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 25 centimeters from the muffin
Câmera: phone at her eye level, straight-on, standard 1x lens, light handheld
Pose: Brandon stands behind the black table holding up one muffin toward the lens
Lista fechada: muffin na mão, forma de muffins, avatar
Frame 0: falando para a câmera com o muffin erguido
Desvio (acabamento ou avatar fixo): cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); muffin um pouco mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "baked carrot oat muffin with a domed golden orange top" · "12-cup muffin tin filled with baked" |
| F2 quanto do quadro | OK | "fills about 18 percent of the frame" |
| F3 distancia da lente | OK | "about 25 centimeters from the muffin" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon stands behind the black table holding up one" |
| F6 lista fechada | OK | "In her right hand" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K08
Frame: `input/frames_modelo/K08_modelo.png`
Take: T8
Herói: o muffin de cenoura assado na mão, colado na lente, e a forma cheia na mesa
Termos de forma: "baked carrot oat muffin with a domed golden orange top" · "12-cup muffin tin filled with baked"
Quadro: no K: fills about 18 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 25 centimeters from the muffin
Câmera: phone at her eye level, straight-on, standard 1x lens, light handheld
Pose: Brandon stands behind the black table holding up one muffin toward the lens
Lista fechada: muffin na mão, forma de muffins, avatar
Frame 0: falando para a câmera com o muffin erguido
Desvio (acabamento ou avatar fixo): cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); muffin um pouco mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "baked carrot oat muffin with a domed golden orange top" · "12-cup muffin tin filled with baked" |
| F2 quanto do quadro | OK | "fills about 18 percent of the frame" |
| F3 distancia da lente | OK | "about 25 centimeters from the muffin" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon stands behind the black table holding up one" |
| F6 lista fechada | OK | "In her right hand" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K09
Frame: `input/frames_modelo/K09_modelo.png`
Take: T9
Herói: o muffin de cenoura assado na mão, colado na lente, e a forma cheia na mesa
Termos de forma: "baked carrot oat muffin with a domed golden orange top" · "12-cup muffin tin filled with baked"
Quadro: no K: fills about 18 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 25 centimeters from the muffin
Câmera: phone at her eye level, straight-on, standard 1x lens, light handheld
Pose: Brandon stands behind the black table holding up one muffin toward the lens
Lista fechada: muffin na mão, forma de muffins, avatar
Frame 0: falando para a câmera com o muffin erguido
Desvio (acabamento ou avatar fixo): cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); muffin um pouco mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "baked carrot oat muffin with a domed golden orange top" · "12-cup muffin tin filled with baked" |
| F2 quanto do quadro | OK | "fills about 18 percent of the frame" |
| F3 distancia da lente | OK | "about 25 centimeters from the muffin" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon stands behind the black table holding up one" |
| F6 lista fechada | OK | "In her right hand" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K10
Frame: `input/frames_modelo/K10_modelo.png`
Take: T10
Herói: o muffin de cenoura assado na mão, colado na lente, e a forma cheia na mesa
Termos de forma: "baked carrot oat muffin with a domed golden orange top" · "12-cup muffin tin filled with baked"
Quadro: no K: fills about 15 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 30 centimeters from the muffin
Câmera: phone at her eye level, straight-on, standard 1x lens, light handheld
Pose: Brandon stands behind the black table holding up one muffin toward the lens
Lista fechada: muffin na mão, forma de muffins, avatar
Frame 0: falando para a câmera com o muffin erguido
Desvio (acabamento ou avatar fixo): cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); muffin um pouco mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "baked carrot oat muffin with a domed golden orange top" · "12-cup muffin tin filled with baked" |
| F2 quanto do quadro | OK | "fills about 15 percent of the frame" |
| F3 distancia da lente | OK | "about 30 centimeters from the muffin" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon stands behind the black table holding up one" |
| F6 lista fechada | OK | "In her right hand" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K11
Frame: `input/frames_modelo/K11_modelo.png`
Take: T11
Herói: o muffin de cenoura assado na mão, colado na lente, e a forma cheia na mesa
Termos de forma: "baked carrot oat muffin with a domed golden orange top" · "12-cup muffin tin filled with baked"
Quadro: no K: fills about 15 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 30 centimeters from the muffin
Câmera: phone at her eye level, straight-on, standard 1x lens, light handheld
Pose: Brandon stands behind the black table holding up one muffin toward the lens
Lista fechada: muffin na mão, forma de muffins, avatar
Frame 0: falando para a câmera com o muffin erguido
Desvio (acabamento ou avatar fixo): cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); muffin um pouco mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "baked carrot oat muffin with a domed golden orange top" · "12-cup muffin tin filled with baked" |
| F2 quanto do quadro | OK | "fills about 15 percent of the frame" |
| F3 distancia da lente | OK | "about 30 centimeters from the muffin" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon stands behind the black table holding up one" |
| F6 lista fechada | OK | "In her right hand" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K12
Frame: `input/frames_modelo/K12_modelo.png`
Take: T12
Herói: o muffin de cenoura assado na mão, colado na lente, e a forma cheia na mesa
Termos de forma: "baked carrot oat muffin with a domed golden orange top" · "12-cup muffin tin filled with baked"
Quadro: no K: fills about 15 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 30 centimeters from the muffin
Câmera: phone at her eye level, straight-on, standard 1x lens, light handheld
Pose: Brandon stands behind the black table holding up one muffin toward the lens
Lista fechada: muffin na mão, forma de muffins, avatar
Frame 0: falando para a câmera com o muffin erguido
Desvio (acabamento ou avatar fixo): cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); muffin um pouco mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "baked carrot oat muffin with a domed golden orange top" · "12-cup muffin tin filled with baked" |
| F2 quanto do quadro | OK | "fills about 15 percent of the frame" |
| F3 distancia da lente | OK | "about 30 centimeters from the muffin" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon stands behind the black table holding up one" |
| F6 lista fechada | OK | "In her right hand" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K13
Frame: `input/frames_modelo/K13_modelo.png`
Take: T13
Herói: o frasco Natural Rems Sea Moss baixo na mão direita, rótulo de frente
Termos de forma: "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies"
Quadro: no K: fills the lower right 20 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 35 centimeters from the jar
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the jar low in her right hand, about to raise it beside her face
Lista fechada: frasco, avatar, mesa vazia
Frame 0: frasco baixo, prestes a subir
Desvio (acabamento ou avatar fixo): o modelo segura o muffin aqui; no bloco de venda o frasco entra no lugar, já na mão para nascer da foto real

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies" |
| F2 quanto do quadro | OK | "fills the lower right 20 percent of the frame" |
| F3 distancia da lente | OK | "about 35 centimeters from the jar" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the jar low in her right hand, about to" |
| F6 lista fechada | OK | "Nothing else on the table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K14
Frame: `input/frames_modelo/K14_modelo.png`
Take: T14
Herói: o frasco parado ao lado do rosto, rótulo de frente e legível
Termos de forma: "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies"
Quadro: no K: fills 20 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 30 centimeters from the jar
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the jar still beside her right cheek, label toward the lens
Lista fechada: frasco, avatar, mesa vazia
Frame 0: falando com o frasco parado
Desvio (acabamento ou avatar fixo): o modelo abre as mãos no follow; aqui o frasco fica parado e legível (passo 1 da marca)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies" |
| F2 quanto do quadro | OK | "fills 20 percent of the frame" |
| F3 distancia da lente | OK | "about 30 centimeters from the jar" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the jar still beside her right cheek," |
| F6 lista fechada | OK | "Her left hand rests on the black table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K15
Frame: `input/frames_modelo/K15_modelo.png`
Take: T15
Herói: o frasco parado ao lado do rosto, rótulo de frente e legível
Termos de forma: "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies"
Quadro: no K: fills 20 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 30 centimeters from the jar
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the jar still beside her right cheek, label toward the lens
Lista fechada: frasco, avatar, mesa vazia
Frame 0: falando com o frasco parado
Desvio (acabamento ou avatar fixo): o modelo abre as mãos no follow; aqui o frasco fica parado e legível (passo 1 da marca)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies" |
| F2 quanto do quadro | OK | "fills 20 percent of the frame" |
| F3 distancia da lente | OK | "about 30 centimeters from the jar" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the jar still beside her right cheek," |
| F6 lista fechada | OK | "Her left hand rests on the black table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K16
Frame: `input/frames_modelo/K16_modelo.png`
Take: T16
Herói: o frasco parado ao lado do rosto, rótulo de frente e legível
Termos de forma: "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies"
Quadro: no K: fills 20 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 30 centimeters from the jar
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the jar still beside her right cheek, label toward the lens
Lista fechada: frasco, avatar, mesa vazia
Frame 0: falando com o frasco parado
Desvio (acabamento ou avatar fixo): o modelo abre as mãos no follow; aqui o frasco fica parado e legível (passo 1 da marca)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies" |
| F2 quanto do quadro | OK | "fills 20 percent of the frame" |
| F3 distancia da lente | OK | "about 30 centimeters from the jar" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the jar still beside her right cheek," |
| F6 lista fechada | OK | "Her left hand rests on the black table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K17
Frame: `input/frames_modelo/K17_modelo.png`
Take: T17
Herói: o frasco parado ao lado do rosto, rótulo de frente e legível
Termos de forma: "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies"
Quadro: no K: fills 20 percent of the frame (medido contra o frame do modelo)
Distância da lente: about 30 centimeters from the jar
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the jar still beside her right cheek, label toward the lens
Lista fechada: frasco, avatar, mesa vazia
Frame 0: falando com o frasco parado
Desvio (acabamento ou avatar fixo): o modelo abre as mãos no follow; aqui o frasco fica parado e legível (passo 1 da marca)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies" |
| F2 quanto do quadro | OK | "fills 20 percent of the frame" |
| F3 distancia da lente | OK | "about 30 centimeters from the jar" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the jar still beside her right cheek," |
| F6 lista fechada | OK | "Her left hand rests on the black table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

