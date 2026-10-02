# FICHA DO FRAME · brandon_maca_alho

Regra e método: `GATE_VISUAL.md` Parte 6. Cada K sai daqui, nunca da memória. O frame do modelo manda no
CONTEÚDO (forma, quadro, distância, câmera, pose, o que está em quadro); o gate manda no ACABAMENTO e impõe o
piso de proximidade do herói. A evidência de cada OK é um trecho que existe literalmente no K
(conferido por `gerar_pacote.py` com assert antes de gravar).

## K01
Frame: `input/frames_modelo/K01_modelo.png`
Take: T1
Herói: maçã vermelha inteira com o miolo escavado (buraco redondo no topo) na palma da mão, e o dente de alho descascado na outra mão logo acima do buraco
Termos de forma: "red apple with its core scooped out" · "single peeled garlic clove"
Quadro: no modelo a maçã ocupa uns 30% de baixo, à esquerda do centro, maior que a cabeça; no K 35%
Distância da lente: uns 20 cm no modelo (grande-angular); no K, 15 cm
Câmera: celular na altura do peito, inclinado para baixo, grande-angular 0,5x
Pose: debruçado sobre a bancada na direção da lente, uma mão com a maçã, a outra com o alho
Lista fechada: maçã, alho, mãos, avatar, cenário de fundo; bancada vazia
Frame 0: alho logo acima do buraco, ainda fora; buraco limpo, sem espuma
Desvio (acabamento ou avatar fixo): cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); óculos e camiseta cinza → regata branca e cruz de ouro; luz neutra (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "red apple with its core scooped out" · "single peeled garlic clove" |
| F2 quanto do quadro | OK | "fills the lower 35 percent of the frame" |
| F3 distancia da lente | OK | "about 15 centimeters from the apple" |
| F4 camera | OK | "wide 0.5x lens" |
| F5 pose do avatar | OK | "leans over the black table toward the lens" |
| F6 lista fechada | OK | "nothing else in her hands" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |

## K02
Frame: `input/frames_modelo/K02_modelo.png`
Take: T2
Herói: jarra de vidro do liquidificador vazia no primeiro plano e a tigela branca de maçã picada com casca inclinada sobre ela
Termos de forma: "glass blender jar" · "white ceramic bowl full of apple chunks with red skin"
Quadro: a jarra ocupa uns 35% de baixo à esquerda e a tigela o canto de cima à direita; no K igual
Distância da lente: uns 45 cm no modelo; no K, 40 cm
Câmera: celular na altura do peito, levemente de cima, lente 1x
Pose: em pé atrás da bancada, as duas mãos segurando a tigela inclinada sobre a jarra
Lista fechada: jarra, tigela, meio limão, dente de alho, copo de água na bancada, avatar
Frame 0: primeiros pedaços escorregando da tigela para a jarra vazia
Desvio (acabamento ou avatar fixo): copo medidor do modelo → copo de vidro liso; bancada de mármore → mesa preta

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "glass blender jar" · "white ceramic bowl full of apple chunks with red skin" |
| F2 quanto do quadro | OK | "fills the lower 35 percent of the frame" |
| F3 distancia da lente | OK | "about 40 centimeters from the blender jar" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "both hands holding the bowl tilted over the jar" |
| F6 lista fechada | OK | "Nothing else is on the table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |

## K03
Frame: `input/frames_modelo/K03_modelo.png`
Take: T3
Herói: jarra com a maçã picada no primeiro plano e o dente de alho na mão logo acima da boca da jarra
Termos de forma: "glass blender jar" · "single peeled garlic clove"
Quadro: a jarra ocupa uns 35% de baixo no centro-esquerda; no K 40%
Distância da lente: uns 50 cm no modelo; no K, 45 cm
Câmera: celular na altura do peito, levemente de cima, lente 1x
Pose: em pé atrás da bancada, mão direita com o alho sobre a jarra, mão esquerda na borda da mesa
Lista fechada: jarra com maçã, alho, meio limão inteiro, copo de água, avatar
Frame 0: alho prestes a cair; limão ainda não espremido
Desvio (acabamento ou avatar fixo): bancada de mármore → mesa preta (avatar fixo)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "glass blender jar" · "single peeled garlic clove" |
| F2 quanto do quadro | OK | "fills the lower 40 percent of the frame" |
| F3 distancia da lente | OK | "about 45 centimeters from the blender jar" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "her right hand holds the garlic clove right above the open jar" |
| F6 lista fechada | OK | "Nothing else is on the table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |

## K04
Frame: `input/frames_modelo/K04_modelo.png`
Take: T4
Herói: jarra cheia de maçã e o copo de água sendo erguido ao lado da boca da jarra; o meio limão espremido colado na lente no canto de baixo
Termos de forma: "glass blender jar" · "clear drinking glass full of water" · "squeezed lemon half"
Quadro: a jarra ocupa uns 35% de baixo no centro e o limão o canto de baixo à esquerda; no K 40%
Distância da lente: o limão a uns 20 cm e a jarra a uns 45 cm no modelo; no K, 15 cm e 40 cm
Câmera: celular na altura do peito, levemente de cima, lente 1x
Pose: em pé atrás da bancada, mão direita erguendo o copo de água sobre a jarra
Lista fechada: jarra, copo de água, limão espremido, avatar
Frame 0: copo inclinado logo acima da boca da jarra, a água ainda não caiu
Desvio (acabamento ou avatar fixo): bancada de mármore → mesa preta (avatar fixo)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "glass blender jar" · "clear drinking glass full of water" · "squeezed lemon half" |
| F2 quanto do quadro | OK | "fills the lower 40 percent of the frame" |
| F3 distancia da lente | OK | "about 15 centimeters from the lens" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "her right hand lifts the clear drinking glass" |
| F6 lista fechada | OK | "Nothing else is on the table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |

## K05
Frame: `input/frames_modelo/K05_modelo.png`
Take: T5
Herói: a jarra solta da base, cheia de suco grosso amarelo-esverdeado claro, inclinada sobre um copo vazio na outra mão
Termos de forma: "thick pale creamy yellow-green apple drink" · "empty clear drinking glass"
Quadro: jarra e copo ocupam uns 40% do quadro no centro-direita, maiores que a cabeça; no K 45%
Distância da lente: uns 35 cm no modelo; no K, 30 cm
Câmera: celular na altura do peito, levemente de cima, lente 1x
Pose: debruçado sobre a bancada, a jarra numa mão e o copo na outra
Lista fechada: jarra, copo, avatar, bancada vazia
Frame 0: o primeiro fio de suco começando a cair no copo vazio
Desvio (acabamento ou avatar fixo): bancada de mármore → mesa preta (avatar fixo)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "thick pale creamy yellow-green apple drink" · "empty clear drinking glass" |
| F2 quanto do quadro | OK | "fill the lower 45 percent of the frame" |
| F3 distancia da lente | OK | "about 30 centimeters from the jar" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "leaning over the black table" |
| F6 lista fechada | OK | "Nothing else is on the table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |

## K06
Frame: `input/frames_modelo/K06_modelo.png`
Take: T6
Herói: o copo de vidro cheio do suco amarelo-claro, erguido na mão direita na altura do peito, à frente do corpo
Termos de forma: "clear drinking glass full of a pale creamy yellow apple drink"
Quadro: no modelo o copo ocupa uns 12% de baixo à esquerda; no K 20% (piso de proximidade)
Distância da lente: uns 55 cm no modelo; no K, 40 cm
Câmera: celular na altura dos olhos, de frente, lente 1x
Pose: em pé atrás da bancada, antebraços apoiados, copo na mão direita, a outra mão gesticula
Lista fechada: copo, avatar, bancada vazia, cenário de fundo
Frame 0: falando para a câmera com o copo erguido; mão livre open in a small gesture
Desvio (acabamento ou avatar fixo): bancada de mármore e cozinha → mesa preta e box de treino (avatar fixo); o copo mais perto da lente que no modelo (piso de proximidade do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "clear drinking glass full of a pale creamy yellow apple drink" |
| F2 quanto do quadro | OK | "fills the lower left 20 percent of the frame" |
| F3 distancia da lente | OK | "about 40 centimeters from the glass" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "leaning on its edge with both forearms" |
| F6 lista fechada | OK | "Nothing else is on the table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |

## K07
Frame: `input/frames_modelo/K07_modelo.png`
Take: T7
Herói: o copo de vidro cheio do suco amarelo-claro, erguido na mão direita na altura do peito, à frente do corpo
Termos de forma: "clear drinking glass full of a pale creamy yellow apple drink"
Quadro: no modelo o copo ocupa uns 12% de baixo à esquerda; no K 20% (piso de proximidade)
Distância da lente: uns 55 cm no modelo; no K, 40 cm
Câmera: celular na altura dos olhos, de frente, lente 1x
Pose: em pé atrás da bancada, antebraços apoiados, copo na mão direita, a outra mão gesticula
Lista fechada: copo, avatar, bancada vazia, cenário de fundo
Frame 0: falando para a câmera com o copo erguido; mão livre raised with the index finger up
Desvio (acabamento ou avatar fixo): bancada de mármore e cozinha → mesa preta e box de treino (avatar fixo); o copo mais perto da lente que no modelo (piso de proximidade do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "clear drinking glass full of a pale creamy yellow apple drink" |
| F2 quanto do quadro | OK | "fills the lower left 20 percent of the frame" |
| F3 distancia da lente | OK | "about 40 centimeters from the glass" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "leaning on its edge with both forearms" |
| F6 lista fechada | OK | "Nothing else is on the table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |

## K08
Frame: `input/frames_modelo/K08_modelo.png`
Take: T8
Herói: o copo de vidro cheio do suco amarelo-claro, erguido na mão direita na altura do peito, à frente do corpo
Termos de forma: "clear drinking glass full of a pale creamy yellow apple drink"
Quadro: no modelo o copo ocupa uns 12% de baixo à esquerda; no K 22% (piso de proximidade)
Distância da lente: uns 55 cm no modelo; no K, 35 cm
Câmera: celular na altura dos olhos, de frente, lente 1x
Pose: em pé atrás da bancada, antebraços apoiados, copo na mão direita, a outra mão gesticula
Lista fechada: copo, avatar, bancada vazia, cenário de fundo
Frame 0: falando para a câmera com o copo erguido; mão livre resting flat on the table
Desvio (acabamento ou avatar fixo): bancada de mármore e cozinha → mesa preta e box de treino (avatar fixo); o copo mais perto da lente que no modelo (piso de proximidade do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "clear drinking glass full of a pale creamy yellow apple drink" |
| F2 quanto do quadro | OK | "fills the lower left 22 percent of the frame" |
| F3 distancia da lente | OK | "about 35 centimeters from the glass" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "leaning on its edge with both forearms" |
| F6 lista fechada | OK | "Nothing else is on the table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |

## K09
Frame: `input/frames_modelo/K09_modelo.png`
Take: T9
Herói: o copo de vidro cheio do suco amarelo-claro, erguido na mão direita na altura do peito, à frente do corpo
Termos de forma: "clear drinking glass full of a pale creamy yellow apple drink"
Quadro: no modelo o copo ocupa uns 12% de baixo à esquerda; no K 22% (piso de proximidade)
Distância da lente: uns 55 cm no modelo; no K, 35 cm
Câmera: celular na altura dos olhos, de frente, lente 1x
Pose: em pé atrás da bancada, antebraços apoiados, copo na mão direita, a outra mão gesticula
Lista fechada: copo, avatar, bancada vazia, cenário de fundo
Frame 0: falando para a câmera com o copo erguido; mão livre counting on her fingers
Desvio (acabamento ou avatar fixo): bancada de mármore e cozinha → mesa preta e box de treino (avatar fixo); o copo mais perto da lente que no modelo (piso de proximidade do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "clear drinking glass full of a pale creamy yellow apple drink" |
| F2 quanto do quadro | OK | "fills the lower left 22 percent of the frame" |
| F3 distancia da lente | OK | "about 35 centimeters from the glass" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "leaning on its edge with both forearms" |
| F6 lista fechada | OK | "Nothing else is on the table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |

## K10
Frame: `input/frames_modelo/K10_modelo.png`
Take: T10
Herói: o copo de vidro cheio do suco amarelo-claro, erguido na mão direita na altura do peito, à frente do corpo
Termos de forma: "clear drinking glass full of a pale creamy yellow apple drink"
Quadro: no modelo o copo ocupa uns 12% de baixo à esquerda; no K 22% (piso de proximidade)
Distância da lente: uns 55 cm no modelo; no K, 35 cm
Câmera: celular na altura dos olhos, de frente, lente 1x
Pose: em pé atrás da bancada, antebraços apoiados, copo na mão direita, a outra mão gesticula
Lista fechada: copo, avatar, bancada vazia, cenário de fundo
Frame 0: falando para a câmera com o copo erguido; mão livre open with the palm up
Desvio (acabamento ou avatar fixo): bancada de mármore e cozinha → mesa preta e box de treino (avatar fixo); o copo mais perto da lente que no modelo (piso de proximidade do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "clear drinking glass full of a pale creamy yellow apple drink" |
| F2 quanto do quadro | OK | "fills the lower left 22 percent of the frame" |
| F3 distancia da lente | OK | "about 35 centimeters from the glass" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "leaning on its edge with both forearms" |
| F6 lista fechada | OK | "Nothing else is on the table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |

## K11
Frame: `input/frames_modelo/K11_modelo.png`
Take: T11
Herói: o copo de vidro cheio do suco amarelo-claro, erguido na mão direita na altura do peito, à frente do corpo
Termos de forma: "clear drinking glass full of a pale creamy yellow apple drink"
Quadro: no modelo o copo ocupa uns 12% de baixo à esquerda; no K 22% (piso de proximidade)
Distância da lente: uns 55 cm no modelo; no K, 35 cm
Câmera: celular na altura dos olhos, de frente, lente 1x
Pose: em pé atrás da bancada, antebraços apoiados, copo na mão direita, a outra mão gesticula
Lista fechada: copo, avatar, bancada vazia, cenário de fundo
Frame 0: falando para a câmera com o copo erguido; mão livre pointing loosely toward the lens
Desvio (acabamento ou avatar fixo): bancada de mármore e cozinha → mesa preta e box de treino (avatar fixo); o copo mais perto da lente que no modelo (piso de proximidade do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "clear drinking glass full of a pale creamy yellow apple drink" |
| F2 quanto do quadro | OK | "fills the lower left 22 percent of the frame" |
| F3 distancia da lente | OK | "about 35 centimeters from the glass" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "leaning on its edge with both forearms" |
| F6 lista fechada | OK | "Nothing else is on the table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |

## K12
Frame: `input/frames_modelo/K12_modelo.png`
Take: T12
Herói: o copo de vidro cheio do suco amarelo-claro, erguido na mão direita na altura do peito, à frente do corpo
Termos de forma: "clear drinking glass full of a pale creamy yellow apple drink"
Quadro: no modelo o copo ocupa uns 12% de baixo à esquerda; no K 25% (piso de proximidade)
Distância da lente: uns 55 cm no modelo; no K, 30 cm
Câmera: celular na altura dos olhos, de frente, lente 1x
Pose: em pé atrás da bancada, antebraços apoiados, copo na mão direita, a outra mão gesticula
Lista fechada: copo, avatar, bancada vazia, cenário de fundo
Frame 0: falando para a câmera com o copo erguido; mão livre resting on the table
Desvio (acabamento ou avatar fixo): bancada de mármore e cozinha → mesa preta e box de treino (avatar fixo); o copo mais perto da lente que no modelo (piso de proximidade do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "clear drinking glass full of a pale creamy yellow apple drink" |
| F2 quanto do quadro | OK | "fills the lower left 25 percent of the frame" |
| F3 distancia da lente | OK | "about 30 centimeters from the glass" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "leaning on its edge with both forearms" |
| F6 lista fechada | OK | "Nothing else is on the table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |

## K13
Frame: `input/frames_modelo/K13_modelo.png`
Take: T13
Herói: o copo de vidro cheio do suco amarelo-claro, erguido na mão direita na altura do peito, à frente do corpo
Termos de forma: "clear drinking glass full of a pale creamy yellow apple drink"
Quadro: no modelo o copo ocupa uns 12% de baixo à esquerda; no K 28% (piso de proximidade)
Distância da lente: uns 55 cm no modelo; no K, 25 cm
Câmera: celular na altura dos olhos, de frente, lente 1x
Pose: em pé atrás da bancada, antebraços apoiados, copo na mão direita, a outra mão gesticula
Lista fechada: copo, avatar, bancada vazia, cenário de fundo
Frame 0: falando para a câmera com o copo erguido; mão livre resting on the table
Desvio (acabamento ou avatar fixo): bancada de mármore e cozinha → mesa preta e box de treino (avatar fixo); o copo mais perto da lente que no modelo (piso de proximidade do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "clear drinking glass full of a pale creamy yellow apple drink" |
| F2 quanto do quadro | OK | "fills the lower left 28 percent of the frame" |
| F3 distancia da lente | OK | "about 25 centimeters from the glass" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "leaning on its edge with both forearms" |
| F6 lista fechada | OK | "Nothing else is on the table" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |

