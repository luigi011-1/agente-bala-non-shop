# FICHA DO FRAME · brandon_seamoss_vizinha

Regra e método: `GATE_VISUAL.md` Parte 6. Cada K sai daqui, nunca da memória. O frame do modelo manda no
CONTEÚDO (forma, quadro, distância, câmera, pose, o que está em quadro); o gate manda no ACABAMENTO e impõe o
piso de proximidade do herói. A evidência de cada OK é um trecho que existe literalmente no K
(conferido por `gerar_pacote.py` com assert antes de gravar).

## K01
Frame: `input/frames_modelo/K01_modelo.png`
Take: T1
Herói: o contraste: a vizinha sarada podando no primeiro plano e o casal correndo ao fundo
Termos de forma: "bent forward at the hips, trimming the hedge" · "jog side by side toward the camera"
Quadro: no K: fills the left 40 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 100 centimeters from the lens
Câmera: phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld
Pose: the neighbor stands in profile in the left foreground, bent forward at the hips, trimming the hedge; far behind her on the wet sidewalk, the husband and the wife jog side by side toward the camera
Lista fechada: vizinha com a tesoura, cerca viva, marido e esposa correndo, calçada, casas, árvores, bandeira
Frame 0: Start frame: mid-stride jogging, the shears half closed, nobody has spoken yet.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "bent forward at the hips, trimming the hedge" · "jog side by side toward the camera" |
| F2 quanto do quadro | OK | "fills the left 40 percent of the frame" |
| F3 distancia da lente | OK | "about 100 centimeters from the lens" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "the neighbor stands in profile in the left foreground, bent" |
| F6 lista fechada | OK | "Long-handled wooden hedge shears in the neighbor's gloved hands, the blades open against the hedge" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | N/A | take sem fala (B-ROLL mudo ou reação de choque sem palavra) |

## K02
Frame: `input/frames_modelo/K02_modelo.png`
Take: T2
Herói: o rosto da esposa em choque, mãos coladas na cabeça, boca escancarada
Termos de forma: "both palms pressed flat against the sides of her head" · "mouth stretched wide open"
Quadro: no K: fills the upper 70 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 25 centimeters from the lens
Câmera: phone held at her eye level, wide 0.5x lens, light handheld
Pose: the wife stares past the camera in shock, both palms pressed flat against the sides of her head, eyes wide open, mouth stretched wide open in a silent gasp
Lista fechada: esposa, mãos na cabeça, árvores e céu atrás
Frame 0: Start frame: frozen mid-gasp, mouth wide open, eyebrows high.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "both palms pressed flat against the sides of her head" · "mouth stretched wide open" |
| F2 quanto do quadro | OK | "fills the upper 70 percent of the frame" |
| F3 distancia da lente | OK | "about 25 centimeters from the lens" |
| F4 camera | OK | "wide 0.5x lens" |
| F5 pose do avatar | OK | "the wife stares past the camera in shock, both palms" |
| F6 lista fechada | OK | "No object in her hands; both palms pressed flat against the sides of her head" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | N/A | take sem fala (B-ROLL mudo ou reação de choque sem palavra) |

## K03
Frame: `input/frames_modelo/K03_modelo.png`
Take: T3
Herói: o marido chegando sorridente, visto por cima do ombro da vizinha
Termos de forma: "seen over the neighbor's shoulder" · "one hand raised in a small wave"
Quadro: no K: filling the left 25 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 20 centimeters from the lens
Câmera: phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld
Pose: seen over the neighbor's shoulder, the husband walks up toward her smiling, one hand raised in a small wave; the wife is still jogging, small, on the sidewalk behind him
Lista fechada: ombro e cabelo da vizinha, marido, esposa ao fundo, calçada, casas, bandeira
Frame 0: Start frame: the husband mid-step, caught mid-sentence, lips naturally parted, animated expression.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "seen over the neighbor's shoulder" · "one hand raised in a small wave" |
| F2 quanto do quadro | OK | "filling the left 25 percent of the frame" |
| F3 distancia da lente | OK | "about 20 centimeters from the lens" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "seen over the neighbor's shoulder, the husband walks up" |
| F6 lista fechada | OK | "The hedge shears hang from the neighbor's gloved hand" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K04
Frame: `input/frames_modelo/K04_modelo.png`
Take: T4
Herói: a vizinha virando, tesoura na mão, casa de pedra atrás
Termos de forma: "holding the shears" · "the husband's bare shoulder"
Quadro: no K: filling 60 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 70 centimeters from the lens
Câmera: phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld
Pose: the neighbor has just turned toward the husband, polite and cool, holding the shears
Lista fechada: vizinha com a tesoura, ombro do marido, casa de pedra, árvore, bandeira
Frame 0: Start frame: the neighbor is caught mid-sentence, lips naturally parted, animated expression.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "holding the shears" · "the husband's bare shoulder" |
| F2 quanto do quadro | OK | "filling 60 percent of the frame" |
| F3 distancia da lente | OK | "about 70 centimeters from the lens" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "the neighbor has just turned toward the husband, polite and" |
| F6 lista fechada | OK | "The neighbor holds the wooden hedge shears closed in front of her waist" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K05
Frame: `input/frames_modelo/K05_modelo.png`
Take: T5
Herói: o marido se apresentando enquanto a esposa, ao fundo, está curvada com as mãos nos joelhos
Termos de forma: "gesturing with an open hand toward the house next door" · "bent over with her hands on her knees"
Quadro: no K: filling 55 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 120 centimeters from the lens
Câmera: phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld
Pose: the husband stands facing the neighbor, gesturing with an open hand toward the house next door; behind him on the sidewalk the wife is bent over with her hands on her knees, catching her breath
Lista fechada: marido, esposa curvada ao fundo, ombro da vizinha, calçada, casas, bandeira
Frame 0: Start frame: the husband is caught mid-sentence, lips naturally parted, animated expression.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "gesturing with an open hand toward the house next door" · "bent over with her hands on her knees" |
| F2 quanto do quadro | OK | "filling 55 percent of the frame" |
| F3 distancia da lente | OK | "about 120 centimeters from the lens" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "the husband stands facing the neighbor, gesturing with an" |
| F6 lista fechada | OK | "No props in the husband's hands" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K06
Frame: `input/frames_modelo/K06_modelo.png`
Take: T6
Herói: o rosto e o peito do marido, sorriso galanteador
Termos de forma: "flirty half smile" · "leafy green hedge branch"
Quadro: no K: fill 70 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 40 centimeters from the lens
Câmera: phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld
Pose: the husband looks just past the lens at the neighbor with a flirty half smile
Lista fechada: marido, galho da cerca, casa e árvore atrás, bandeira
Frame 0: Start frame: the husband is caught mid-sentence, lips naturally parted, animated expression, flirty.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "flirty half smile" · "leafy green hedge branch" |
| F2 quanto do quadro | OK | "fill 70 percent of the frame" |
| F3 distancia da lente | OK | "about 40 centimeters from the lens" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "the husband looks just past the lens at the neighbor with a" |
| F6 lista fechada | OK | "A leafy green hedge branch pokes into the lower left corner of the frame" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K07
Frame: `input/frames_modelo/K07_modelo.png`
Take: T7
Herói: a vizinha olhando a esposa que se afasta correndo
Termos de forma: "jogging away down the sidewalk with her back to the camera"
Quadro: no K: filling the left 55 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 80 centimeters from the lens
Câmera: phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld
Pose: the neighbor, in three-quarter view, glances past the husband toward the wife, who is jogging away down the sidewalk with her back to the camera
Lista fechada: vizinha, braço do marido, esposa de costas correndo, calçada, casas, bandeira
Frame 0: Start frame: the neighbor is caught mid-sentence, lips naturally parted, animated expression, eyebrows slightly raised.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "jogging away down the sidewalk with her back to the camera" |
| F2 quanto do quadro | OK | "filling the left 55 percent of the frame" |
| F3 distancia da lente | OK | "about 80 centimeters from the lens" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "the neighbor, in three-quarter view, glances past the" |
| F6 lista fechada | OK | "The hedge shears hang from the neighbor's gloved hand" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K08
Frame: `input/frames_modelo/K08_modelo.png`
Take: T8
Herói: o marido de perfil falando com a vizinha, a esposa pequena ao fundo
Termos de forma: "stands in profile looking at the neighbor"
Quadro: no K: filling the right 50 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 100 centimeters from the lens
Câmera: phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld
Pose: the husband stands in profile looking at the neighbor, one hand open toward her; far behind, the wife keeps jogging away
Lista fechada: marido de perfil, borda da vizinha, esposa ao longe, galho, calçada, casas, bandeira
Frame 0: Start frame: the husband is caught mid-sentence, lips naturally parted, animated expression.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "stands in profile looking at the neighbor" |
| F2 quanto do quadro | OK | "filling the right 50 percent of the frame" |
| F3 distancia da lente | OK | "about 100 centimeters from the lens" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "the husband stands in profile looking at the neighbor, one" |
| F6 lista fechada | OK | "A hedge branch crosses the lower foreground" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K09
Frame: `input/frames_modelo/K09_modelo.png`
Take: T9
Herói: o rosto da vizinha, seca, sem sorrir
Termos de forma: "dry and unimpressed"
Quadro: no K: filling 65 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 45 centimeters from the lens
Câmera: phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld
Pose: the neighbor looks at the husband, dry and unimpressed
Lista fechada: vizinha, cabo da tesoura, ombro do marido, casa de pedra com janela, bandeira
Frame 0: Start frame: the neighbor is caught mid-sentence, lips naturally parted, animated expression, no smile.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "dry and unimpressed" |
| F2 quanto do quadro | OK | "filling 65 percent of the frame" |
| F3 distancia da lente | OK | "about 45 centimeters from the lens" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "the neighbor looks at the husband, dry and" |
| F6 lista fechada | OK | "The wooden handle of the hedge shears in her gloved hand at the bottom of the frame" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K10
Frame: `input/frames_modelo/K10_modelo.png`
Take: T10
Herói: o rosto do marido, curioso
Termos de forma: "tilts his head, curious"
Quadro: no K: fill 70 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 40 centimeters from the lens
Câmera: phone held just below his chin height, tilted slightly up, standard 1x lens, light handheld
Pose: the husband tilts his head, curious and still flirting
Lista fechada: marido, folhas da cerca, casas e árvores atrás, bandeira
Frame 0: Start frame: the husband is caught mid-sentence, lips naturally parted, animated expression.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "tilts his head, curious" |
| F2 quanto do quadro | OK | "fill 70 percent of the frame" |
| F3 distancia da lente | OK | "about 40 centimeters from the lens" |
| F4 camera | OK | "tilted slightly up" |
| F5 pose do avatar | OK | "the husband tilts his head, curious and still" |
| F6 lista fechada | OK | "Hedge leaves in the lower left corner of the frame" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K11
Frame: `input/frames_modelo/K11_modelo.png`
Take: T11
Herói: a vizinha podando e respondendo por cima do ombro
Termos de forma: "shears open in both hands, glancing back over her shoulder"
Quadro: no K: filling 55 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 90 centimeters from the lens
Câmera: phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld
Pose: the neighbor is back at the hedge, shears open in both hands, glancing back over her shoulder
Lista fechada: vizinha com a tesoura aberta, cerca viva, braço do marido, casa de pedra, bandeira
Frame 0: Start frame: the neighbor is caught mid-sentence, lips naturally parted, animated expression, matter-of-fact.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "shears open in both hands, glancing back over her shoulder" |
| F2 quanto do quadro | OK | "filling 55 percent of the frame" |
| F3 distancia da lente | OK | "about 90 centimeters from the lens" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "the neighbor is back at the hedge, shears open in both" |
| F6 lista fechada | OK | "The wooden hedge shears open in both gloved hands, against the hedge" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K12
Frame: `input/frames_modelo/K12_modelo.png`
Take: T12
Herói: o rosto do marido em choque
Termos de forma: "eyebrows raised high, mouth open"
Quadro: no K: fills 60 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 35 centimeters from the lens
Câmera: phone held at his eye level, standard 1x lens, straight-on, light handheld
Pose: the husband stares straight ahead in total shock, eyebrows raised high, mouth open
Lista fechada: marido, casas e árvores atrás, bandeira
Frame 0: Start frame: the husband is caught mid-sentence, lips naturally parted, animated expression, frozen in shock.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "eyebrows raised high, mouth open" |
| F2 quanto do quadro | OK | "fills 60 percent of the frame" |
| F3 distancia da lente | OK | "about 35 centimeters from the lens" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "the husband stares straight ahead in total shock, eyebrows" |
| F6 lista fechada | OK | "No props" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K13
Frame: `input/frames_modelo/K13_modelo.png`
Take: T13
Herói: o marido incrédulo, mãos abertas
Termos de forma: "hands open in disbelief"
Quadro: no K: filling 60 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 100 centimeters from the lens
Câmera: phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld
Pose: the husband faces the neighbor, hands open in disbelief
Lista fechada: marido, borda da vizinha, galhos da cerca, calçada, casas, bandeira
Frame 0: Start frame: the husband is caught mid-sentence, lips naturally parted, animated expression, amazed.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "hands open in disbelief" |
| F2 quanto do quadro | OK | "filling 60 percent of the frame" |
| F3 distancia da lente | OK | "about 100 centimeters from the lens" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "the husband faces the neighbor, hands open in" |
| F6 lista fechada | OK | "Hedge branches in the lower foreground" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K14
Frame: `input/frames_modelo/K14_modelo.png`
Take: T14
Herói: a vizinha com os galhos podados e o saco de lixo, contando o segredo
Termos de forma: "freshly cut hedge branches" · "open black garbage bag"
Quadro: no K: filling 60 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 80 centimeters from the lens
Câmera: phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld
Pose: the neighbor faces the husband, holding up the cut branches and the garbage bag
Lista fechada: vizinha com galhos e saco preto, mão do marido, casas, árvore, bandeira
Frame 0: Start frame: the neighbor is caught mid-sentence, lips naturally parted, animated expression, casual.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "freshly cut hedge branches" · "open black garbage bag" |
| F2 quanto do quadro | OK | "filling 60 percent of the frame" |
| F3 distancia da lente | OK | "about 80 centimeters from the lens" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "the neighbor faces the husband, holding up the cut branches" |
| F6 lista fechada | OK | "A bunch of freshly cut hedge branches in the neighbor's right gloved hand and an open black garbage bag held in her left gloved hand" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K15
Frame: `input/frames_modelo/K15_modelo.png`
Take: T15
Herói: o marido ouvindo calado
Termos de forma: "listens in silence, mouth closed"
Quadro: no K: fill 65 percent of the frame (medido no frame do modelo, mesmo enquadramento)
Distância da lente: about 35 centimeters from the lens
Câmera: phone held at his eye level, standard 1x lens, straight-on, light handheld
Pose: the husband listens in silence, mouth closed, slowly taking it in
Lista fechada: marido, casas e árvores atrás, bandeira
Frame 0: Start frame: mouth closed, a slow blink.
Desvio (acabamento ou avatar fixo): rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com textura (gate); bandeira na varanda (gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "listens in silence, mouth closed" |
| F2 quanto do quadro | OK | "fill 65 percent of the frame" |
| F3 distancia da lente | OK | "about 35 centimeters from the lens" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "the husband listens in silence, mouth closed, slowly taking" |
| F6 lista fechada | OK | "No props" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "overcast pale grey with visible soft cloud texture" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | N/A | take sem fala (B-ROLL mudo ou reação de choque sem palavra) |

## K16
Frame: `input/frames_modelo/K16_modelo.png`
Take: T16
Herói: a própria Brandon, mãos espalmadas na mesa preta (pose da âncora)
Termos de forma: "both hands resting flat on it"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills 60 percent of the frame (piso de proximidade do gate)
Distância da lente: about 60 centimeters from her
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon stands behind the black table, both hands resting flat on it, shoulders square to the lens
Lista fechada: avatar, mesa preta vazia, neon, quadro branco, bandeira
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, calm and sure.
Desvio (acabamento ou avatar fixo): apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box (avatar fixo da conta)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "both hands resting flat on it" |
| F2 quanto do quadro | OK | "fills 60 percent of the frame" |
| F3 distancia da lente | OK | "about 60 centimeters from her" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon stands behind the black table, both hands" |
| F6 lista fechada | OK | "the black table is empty" |
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
Herói: copo de água morna e meio limão erguidos na altura do peito
Termos de forma: "clear drinking glass of warm water" · "half a lemon with its cut side facing the lens"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills the lower 30 percent of the frame (piso de proximidade do gate)
Distância da lente: about 25 centimeters from the glass and the lemon
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the glass and the lemon half out toward the lens, the lemon tilted above the glass
Lista fechada: copo de água, meio limão, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, about to squeeze the lemon into the glass.
Desvio (acabamento ou avatar fixo): apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box (avatar fixo da conta); prop mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "clear drinking glass of warm water" · "half a lemon with its cut side facing the lens" |
| F2 quanto do quadro | OK | "fills the lower 30 percent of the frame" |
| F3 distancia da lente | OK | "about 25 centimeters from the glass and the lemon" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the glass and the lemon half out toward" |
| F6 lista fechada | OK | "A clear drinking glass of warm water in her left hand and half a lemon with its cut side facing the lens in her right hand" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K18
Frame: `input/frames_modelo/K18_modelo.png`
Take: T18
Herói: copo e meio limão lado a lado na altura do peito
Termos de forma: "clear drinking glass of warm water" · "half a lemon with its cut side facing the lens"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills the lower 30 percent of the frame (piso de proximidade do gate)
Distância da lente: about 25 centimeters from the glass and the lemon
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the glass and the lemon half side by side at chest height
Lista fechada: copo de água, meio limão, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, lively and certain.
Desvio (acabamento ou avatar fixo): apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box (avatar fixo da conta); prop mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "clear drinking glass of warm water" · "half a lemon with its cut side facing the lens" |
| F2 quanto do quadro | OK | "fills the lower 30 percent of the frame" |
| F3 distancia da lente | OK | "about 25 centimeters from the glass and the lemon" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the glass and the lemon half side by" |
| F6 lista fechada | OK | "A clear drinking glass of warm water in her left hand and half a lemon with its cut side facing the lens in her right hand" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K19
Frame: `input/frames_modelo/K19_modelo.png`
Take: T19
Herói: copo e meio limão um pouco mais baixos, antes da troca de prop
Termos de forma: "clear drinking glass of warm water" · "half a lemon with its cut side facing the lens"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills the lower 25 percent of the frame (piso de proximidade do gate)
Distância da lente: about 30 centimeters from the glass and the lemon
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the glass and the lemon half a little lower, about to put them down
Lista fechada: copo de água, meio limão, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, raising one eyebrow, turning a point.
Desvio (acabamento ou avatar fixo): apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box (avatar fixo da conta); prop mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "clear drinking glass of warm water" · "half a lemon with its cut side facing the lens" |
| F2 quanto do quadro | OK | "fills the lower 25 percent of the frame" |
| F3 distancia da lente | OK | "about 30 centimeters from the glass and the lemon" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the glass and the lemon half a little" |
| F6 lista fechada | OK | "A clear drinking glass of warm water in her left hand and half a lemon with its cut side facing the lens in her right hand" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K20
Frame: `input/frames_modelo/K20_modelo.png`
Take: T20
Herói: a tigelinha de vidro com a mistura cremosa amarelo-clara, dois dedos tocando a mistura
Termos de forma: "pale creamy yellow mixture of apple cider vinegar and coconut oil"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills the lower 25 percent of the frame (piso de proximidade do gate)
Distância da lente: about 25 centimeters from the bowl
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the bowl toward the lens and dips two fingers into the mixture
Lista fechada: tigelinha com a mistura, mãos, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, explaining, focused.
Desvio (acabamento ou avatar fixo): apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box (avatar fixo da conta); prop mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "pale creamy yellow mixture of apple cider vinegar and coconut oil" |
| F2 quanto do quadro | OK | "fills the lower 25 percent of the frame" |
| F3 distancia da lente | OK | "about 25 centimeters from the bowl" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the bowl toward the lens and dips two" |
| F6 lista fechada | OK | "A small clear glass bowl with a pale creamy yellow mixture of apple cider vinegar and coconut oil" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K21
Frame: `input/frames_modelo/K21_modelo.png`
Take: T21
Herói: a tigelinha da máscara nas duas mãos
Termos de forma: "pale creamy yellow mixture of apple cider vinegar and coconut oil"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills the lower 25 percent of the frame (piso de proximidade do gate)
Distância da lente: about 25 centimeters from the bowl
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the bowl in both hands toward the lens
Lista fechada: tigelinha com a mistura, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, confident, a little conspiratorial at the end.
Desvio (acabamento ou avatar fixo): apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box (avatar fixo da conta); prop mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "pale creamy yellow mixture of apple cider vinegar and coconut oil" |
| F2 quanto do quadro | OK | "fills the lower 25 percent of the frame" |
| F3 distancia da lente | OK | "about 25 centimeters from the bowl" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the bowl in both hands toward the" |
| F6 lista fechada | OK | "A small clear glass bowl with a pale creamy yellow mixture of apple cider vinegar and coconut oil" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K22
Frame: `input/frames_modelo/K22_modelo.png`
Take: T22
Herói: a tigelinha nas duas mãos, ela inclinada para a lente
Termos de forma: "pale creamy yellow mixture of apple cider vinegar and coconut oil"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills the lower 22 percent of the frame (piso de proximidade do gate)
Distância da lente: about 30 centimeters from the bowl
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the bowl in both hands, leaning slightly toward the lens
Lista fechada: tigelinha com a mistura, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, serious and reassuring.
Desvio (acabamento ou avatar fixo): apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box (avatar fixo da conta); prop mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "pale creamy yellow mixture of apple cider vinegar and coconut oil" |
| F2 quanto do quadro | OK | "fills the lower 22 percent of the frame" |
| F3 distancia da lente | OK | "about 30 centimeters from the bowl" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the bowl in both hands, leaning slightly" |
| F6 lista fechada | OK | "A small clear glass bowl with a pale creamy yellow mixture of apple cider vinegar and coconut oil" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K23
Frame: `input/frames_modelo/K23_modelo.png`
Take: T23
Herói: o pote de vidro largo cheio de sea moss seco, fios dourados e bege embaraçados
Termos de forma: "dried raw Irish sea moss" · "tangled pale golden and beige seaweed strands"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills the lower 35 percent of the frame (piso de proximidade do gate)
Distância da lente: about 25 centimeters from the jar
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the jar of dried sea moss in both hands, pushed toward the lens
Lista fechada: pote de sea moss seco, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, emphatic, this is the important one.
Desvio (acabamento ou avatar fixo): pote de fibra em pó branca do modelo → pote de sea moss seco (troca obrigatória do nº 3)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "dried raw Irish sea moss" · "tangled pale golden and beige seaweed strands" |
| F2 quanto do quadro | OK | "fills the lower 35 percent of the frame" |
| F3 distancia da lente | OK | "about 25 centimeters from the jar" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the jar of dried sea moss in both hands," |
| F6 lista fechada | OK | "A wide clear glass jar filled with dried raw Irish sea moss: tangled pale golden and beige seaweed strands with a light frosty sea-salt coating" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K24
Frame: `input/frames_modelo/K24_modelo.png`
Take: T24
Herói: o pote de sea moss seco nas duas mãos
Termos de forma: "dried raw Irish sea moss"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills the lower 35 percent of the frame (piso de proximidade do gate)
Distância da lente: about 25 centimeters from the jar
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the jar of dried sea moss in both hands at chest height
Lista fechada: pote de sea moss seco, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warm and proud.
Desvio (acabamento ou avatar fixo): apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box (avatar fixo da conta); prop mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "dried raw Irish sea moss" |
| F2 quanto do quadro | OK | "fills the lower 35 percent of the frame" |
| F3 distancia da lente | OK | "about 25 centimeters from the jar" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the jar of dried sea moss in both hands" |
| F6 lista fechada | OK | "A wide clear glass jar filled with dried raw Irish sea moss: tangled pale golden and beige seaweed strands with a light frosty sea-salt coating" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K25
Frame: `input/frames_modelo/K25_modelo.png`
Take: T25
Herói: o pote de sea moss seco numa mão, a outra explicando
Termos de forma: "dried raw Irish sea moss"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills the lower 30 percent of the frame (piso de proximidade do gate)
Distância da lente: about 30 centimeters from the jar
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the jar in her left hand and explains with her right hand open
Lista fechada: pote de sea moss seco, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, serious, explaining.
Desvio (acabamento ou avatar fixo): apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box (avatar fixo da conta); prop mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "dried raw Irish sea moss" |
| F2 quanto do quadro | OK | "fills the lower 30 percent of the frame" |
| F3 distancia da lente | OK | "about 30 centimeters from the jar" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the jar in her left hand and explains" |
| F6 lista fechada | OK | "A wide clear glass jar filled with dried raw Irish sea moss: tangled pale golden and beige seaweed strands with a light frosty sea-salt coating" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K26
Frame: `input/frames_modelo/K26_modelo.png`
Take: T26
Herói: a tigelinha com a colherada de gel de sea moss bege-claro, o indicador apontando
Termos de forma: "smooth pale beige sea moss gel, glossy and jelly-like"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills the lower 25 percent of the frame (piso de proximidade do gate)
Distância da lente: about 25 centimeters from the bowl
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the small bowl toward the lens and points at the gel with her right index finger
Lista fechada: tigelinha com gel de sea moss, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, calm and reassuring.
Desvio (acabamento ou avatar fixo): tigelinha de fibra do modelo → gel de sea moss

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "smooth pale beige sea moss gel, glossy and jelly-like" |
| F2 quanto do quadro | OK | "fills the lower 25 percent of the frame" |
| F3 distancia da lente | OK | "about 25 centimeters from the bowl" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the small bowl toward the lens and" |
| F6 lista fechada | OK | "A small clear glass bowl holding a spoonful of smooth pale beige sea moss gel" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K27
Frame: `input/frames_modelo/K27_modelo.png`
Take: T27
Herói: a tigelinha com o gel nas duas mãos
Termos de forma: "smooth pale beige sea moss gel, glossy and jelly-like"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills the lower 25 percent of the frame (piso de proximidade do gate)
Distância da lente: about 25 centimeters from the bowl
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the small bowl of gel in both hands
Lista fechada: tigelinha com gel de sea moss, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warm, telling a story.
Desvio (acabamento ou avatar fixo): apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box (avatar fixo da conta); prop mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "smooth pale beige sea moss gel, glossy and jelly-like" |
| F2 quanto do quadro | OK | "fills the lower 25 percent of the frame" |
| F3 distancia da lente | OK | "about 25 centimeters from the bowl" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds the small bowl of gel in both" |
| F6 lista fechada | OK | "A small clear glass bowl holding a spoonful of smooth pale beige sea moss gel" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K28
Frame: `input/frames_modelo/K28_modelo.png`
Take: T28
Herói: a Brandon mais perto, apoiada na mesa, sem prop
Termos de forma: "leans on the black table with both hands"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fill the upper 60 percent of the frame (piso de proximidade do gate)
Distância da lente: about 45 centimeters from her face
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon leans on the black table with both hands, closer to the lens
Lista fechada: avatar, mesa vazia, neon, quadro branco, bandeira
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, indignant, lowering her voice.
Desvio (acabamento ou avatar fixo): apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box (avatar fixo da conta); prop mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "leans on the black table with both hands" |
| F2 quanto do quadro | OK | "fill the upper 60 percent of the frame" |
| F3 distancia da lente | OK | "about 45 centimeters from her face" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon leans on the black table with both hands," |
| F6 lista fechada | OK | "the black table is empty" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K29
Frame: `input/frames_modelo/K29_modelo.png`
Take: T29
Herói: a Brandon apoiada na mesa, firme
Termos de forma: "leans on the black table with both hands"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fill the upper 60 percent of the frame (piso de proximidade do gate)
Distância da lente: about 45 centimeters from her face
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon leans on the black table with both hands, closer to the lens, one hand lifting slightly
Lista fechada: avatar, mesa vazia, neon, quadro branco, bandeira
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, firm.
Desvio (acabamento ou avatar fixo): apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box (avatar fixo da conta); prop mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "leans on the black table with both hands" |
| F2 quanto do quadro | OK | "fill the upper 60 percent of the frame" |
| F3 distancia da lente | OK | "about 45 centimeters from her face" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon leans on the black table with both hands," |
| F6 lista fechada | OK | "the black table is empty" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K30
Frame: `input/frames_modelo/K30_modelo.png`
Take: T30
Herói: uma tigelinha em cada mão: açúcar cristal e pó branco de enchimento
Termos de forma: "heaped with white granulated sugar" · "heaped with a fine white powder"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills the lower 35 percent of the frame (piso de proximidade do gate)
Distância da lente: about 25 centimeters from the two bowls
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds one small bowl in each hand, out toward the lens
Lista fechada: tigelinha de açúcar, tigelinha de pó branco, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warning, a little disgusted.
Desvio (acabamento ou avatar fixo): apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box (avatar fixo da conta); prop mais perto da lente que no modelo (piso do gate)

| Item | Status | Evidência (trecho literal do K) |
|---|---|---|
| F1 forma do heroi | OK | "heaped with white granulated sugar" · "heaped with a fine white powder" |
| F2 quanto do quadro | OK | "fills the lower 35 percent of the frame" |
| F3 distancia da lente | OK | "about 25 centimeters from the two bowls" |
| F4 camera | OK | "standard 1x lens" |
| F5 pose do avatar | OK | "Brandon holds one small bowl in each hand, out toward" |
| F6 lista fechada | OK | "A small clear glass bowl heaped with white granulated sugar in her left hand and a small clear glass bowl heaped with a fine white powder in her right hand" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence, lips naturally parted" |

## K31
Frame: `input/frames_modelo/K31_modelo.png`
Take: T31
Herói: o frasco Natural Rems Sea Moss baixo na mão direita, rótulo de frente
Termos de forma: "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills the lower right 20 percent of the frame (piso de proximidade do gate)
Distância da lente: about 35 centimeters from the jar
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the jar low in her right hand, about to raise it beside her face
Lista fechada: frasco Natural Rems Sea Moss, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, proud, about to show it.
Desvio (acabamento ou avatar fixo): o produto do modelo (pote de fibra) → frasco Natural Rems Sea Moss, já na mão para nascer da foto real

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

## K32
Frame: `input/frames_modelo/K32_modelo.png`
Take: T32
Herói: o frasco Natural Rems Sea Moss parado ao lado do rosto, rótulo de frente e legível
Termos de forma: "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills 20 percent of the frame (piso de proximidade do gate)
Distância da lente: about 30 centimeters from the jar
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the jar still beside her right cheek, label toward the lens
Lista fechada: frasco Natural Rems Sea Moss, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, lively, listing.
Desvio (acabamento ou avatar fixo): frasco do modelo ao lado do ombro → Natural Rems um pouco mais perto da lente, rótulo legível (passo 1 da marca)

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

## K33
Frame: `input/frames_modelo/K33_modelo.png`
Take: T33
Herói: o frasco Natural Rems Sea Moss parado ao lado do rosto, rótulo de frente e legível
Termos de forma: "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills 20 percent of the frame (piso de proximidade do gate)
Distância da lente: about 30 centimeters from the jar
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the jar still beside her right cheek, label toward the lens
Lista fechada: frasco Natural Rems Sea Moss, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warm and certain.
Desvio (acabamento ou avatar fixo): frasco do modelo ao lado do ombro → Natural Rems um pouco mais perto da lente, rótulo legível (passo 1 da marca)

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

## K34
Frame: `input/frames_modelo/K34_modelo.png`
Take: T34
Herói: o frasco Natural Rems Sea Moss parado ao lado do rosto, rótulo de frente e legível
Termos de forma: "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills 20 percent of the frame (piso de proximidade do gate)
Distância da lente: about 30 centimeters from the jar
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the jar still beside her right cheek, label toward the lens
Lista fechada: frasco Natural Rems Sea Moss, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, inviting, smiling on yes.
Desvio (acabamento ou avatar fixo): frasco do modelo ao lado do ombro → Natural Rems um pouco mais perto da lente, rótulo legível (passo 1 da marca)

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

## K35
Frame: `input/frames_modelo/K35_modelo.png`
Take: T35
Herói: o frasco Natural Rems Sea Moss parado ao lado do rosto, rótulo de frente e legível
Termos de forma: "short wide jar of dark amber plastic with a black screw cap" · "Sea Moss Gummies"
Quadro: no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; no K: fills 20 percent of the frame (piso de proximidade do gate)
Distância da lente: about 30 centimeters from the jar
Câmera: phone at her chest height, straight-on, standard 1x lens, light handheld
Pose: Brandon holds the jar still beside her right cheek, label toward the lens
Lista fechada: frasco Natural Rems Sea Moss, avatar, mesa vazia
Frame 0: Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, clear and slow on the brand name.
Desvio (acabamento ou avatar fixo): frasco do modelo ao lado do ombro → Natural Rems um pouco mais perto da lente, rótulo legível (passo 1 da marca)

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

