# Prompts de imagem | manifestselizabeth | ROBIN MATTHEWS | Angulo 3 (Auraly)

## Cabecalho

- **Video modelo:** `C:\Users\luigi\Downloads\manifestselizabeth.mp4` , 48,946s, uma cena continua
- **Avatar:** **Robin Matthews**, 72 anos, `ACTIVE` na fila de `AVATAR_QUEUE.md`
- **Ancora:** `producao/_ancoras/Robin.Matthewsus .jpeg`
- **Roteiro:** `ROTEIRO.md`, 7 takes, 153 palavras
- **Ganchos escolhidos pelo Luigi:** a pedra que abre, a agua que salta, a toalha puxada, a flor que abre na agua, o globo sacudido
- **Funil:** video, selo (`222` + save + follow), Stories, botao do link
- **Este arquivo e a fonte de verdade INTERNA.** Os blocos limpos entregues ao agente do Flow sao a
  versao de execucao: la cada prompt e autossuficiente, nao existe `EDITAR do K__` e a carta e
  descrita por escrito dentro de cada prompt, porque o Flow recebe so a ancora mais o texto.

## Indice de geracao

| Take | Keyframe | Cena | Acao de geracao | Anexo |
|---|---|---|---|---|
| T1 | **K01** | HOOK A A PEDRA QUE ABRE | GERAR DO ZERO | ancora ROBIN |
| T1 | **K02** | HOOK B A AGUA QUE SALTA | GERAR DO ZERO | ancora ROBIN |
| T1 | **K03** | HOOK C A TOALHA PUXADA | GERAR DO ZERO | ancora ROBIN |
| T1 | **K04** | HOOK D A FLOR QUE ABRE NA AGUA | GERAR DO ZERO | ancora ROBIN |
| T1 | **K05** | HOOK E O GLOBO SACUDIDO | GERAR DO ZERO | ancora ROBIN |
| T2 | **K06** | BODY CARTA NA MAO | GERAR DO ZERO | ancora ROBIN |
| T3 | **K07** | BODY CARTA NA MAO | EDITAR do K06 | o K06 ja aprovado |
| T4 | **K08** | BODY CARTA NA MAO | EDITAR do K06 | o K06 ja aprovado |
| T5 | **K09** | BODY CARTA NA MAO | EDITAR do K06 | o K06 ja aprovado |
| T6 | **K10** | CTA | EDITAR do K06 | o K06 ja aprovado |
| T7 | **K11** | CTA | EDITAR do K06 | o K06 ja aprovado |

**Regra de bolso:** `GERAR DO ZERO` anexa a ancora, `EDITAR` anexa uma imagem so, o keyframe de
origem. **K07 a K11 saem todos do K06 aprovado, nunca em cascata de uma edicao ja editada.**

## Trava de identidade e continuidade (bloco unico, vale para os onze)

Robin Matthews e **MULHER**, 72 anos, e o nome e ambiguo em ingles, entao todo `identity_main` comeca
com `The EXACT woman`. A idade e o ativo dela: `no de-aging`, `no skin smoothing` e `no makeup` entram
no negative dos onze prompts. Tracos fixos: bob branco-prateado logo abaixo da orelha com risca de
lado, manchas de idade na testa, nas macas e nas costas das maos, oculos de leitura de aro dourado
fino apoiados baixos no nariz, cardiga cinza sobre blusa branca, cruz de prata e **alianca de ouro
lisa**, que e o traco que so ela tem no roster. Cenario fixo: cozinha de armarios de carvalho com duas
janelas, mesa de madeira no terco inferior, baralho **classico de borda branca** no cavalete, esfera
de quartzo rosa, drusa de citrino, queimador de latao com fumaca, duas velas brancas apagadas, quadro
lunar, crucifixo e a bandeirinha dos EUA no peitoril da janela esquerda.

## Trava do prop heroi: a carta SOULMATE

A carta e descrita por inteiro dentro de cada prompt que a mostra, com borda metalica espelhada, arte
saturada de casal, arco de rosas, lua crescente e a faixa de titulo com a palavra impressa.
**O brilho e propriedade impressa do objeto, nunca luz de cena**, e a luz da cozinha continua neutra.

O baralho da mesa dela e classico de borda branca e a carta que ela segura e holografica. E aceito de
proposito, a leitura e que ela puxou uma carta especial. **Nunca escrever que a carta saiu daquele
baralho e nunca mostrar a carta sendo tirada do maco.**

Nos onze prompts o negative **nao leva** `no words overlaid on the image`, e o campo `prop` diz
explicitamente que o unico texto da imagem e a palavra impressa na faixa da carta. Sem isso o negative
padrao apaga o titulo e a carta deixa de ler como carta de taro.

## Trava da 2a pessoa (REF-A)

**Nao existe segunda pessoa nesta producao.** O modelo tem uma pessoa so em quadro do primeiro ao
ultimo frame. `no second person` entra no negative dos onze prompts.


## K01 | T1 | HOOK A A PEDRA QUE ABRE | GERAR DO ZERO | ANCORA ROBIN

> ### ANEXAR: **1 IMAGEM**
> **1. ANCORA ROBIN** `producao/_ancoras/Robin.Matthewsus .jpeg`
>
> ### GERAR DO ZERO

Pedra cinza fechada no primeiro plano, martelinho encostado nela, carta SOULMATE ao lado.

```json
{
  "shot_id": "K01_hook_stone_initial",
  "reference_use": "Use the attached image ONLY for Robin's exact face, identity, hair, skin texture, wardrobe and the identity of her real kitchen. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 72-year-old white American woman with a small build, straight silver white hair in a bob cut just below the ear with a side part, pale weathered skin with many age spots across her forehead, cheeks and the backs of her hands, deep lines on the forehead and around the mouth, heavy crow lines at the eyes, a soft jawline, light eyes behind thin gold rimmed reading glasses resting low on her nose, and no makeup at all. She is clearly a woman and clearly in her seventies.",
  "wardrobe": "The same heather grey cardigan over a white open collar blouse, a thin silver chain with a small silver cross pendant, and a plain gold wedding band on her left hand.",
  "prop": "A plain dull grey stone the size of a fist sits on the wooden table top in the lower foreground, completely whole and closed, with one hairline seam running across its middle. Robin's right hand holds a small steel hammer whose head has just touched the top of the stone. A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card lies face up on the table beside the stone.",
  "scene": "The SAME real American oak kitchen as the reference image, with two windows and the sink on the right. The table group in the lower foreground holds her classic white bordered tarot deck standing in a small wooden easel, a rose quartz sphere on a stand, a citrine cluster, a pierced brass incense burner with a thin thread of smoke rising and two thin unlit white candles in brass holders. The wall group behind her holds a framed printed lunar chart, a wooden crucifix and a small United States flag on a black desk stand on the left window sill, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Robin sits upright at the kitchen table, forearms resting on the wood, leaning slightly forward, her eyes on the object in front of her and then toward the lens. Both hands stay anatomically clear and fully visible.",
  "composition": "EXTREME CLOSE foreground emphasis. The closed grey stone and the hammer head fills the lower foreground and is much closer to the lens than Robin's face. Robin is chest-up in the upper portion of the frame. Nothing competes with it.",
  "camera": "table height, slightly high toward the stone, pushed in very close",
  "state": "Start frame: the stone is still whole and closed and the hammer head has just made contact with it, before any strike and before anything opens.",
  "lighting": "Soft neutral diffuse daylight from the two kitchen windows, cool and even on her face, with no warm cast. The candles are unlit and light nothing.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no de-aging, no skin smoothing, no makeup, no change of identity, no change of wardrobe"
}
```

## K02 | T1 | HOOK B A AGUA QUE SALTA | GERAR DO ZERO | ANCORA ROBIN

> ### ANEXAR: **1 IMAGEM**
> **1. ANCORA ROBIN** `producao/_ancoras/Robin.Matthewsus .jpeg`
>
> ### GERAR DO ZERO

Tigela rasa de agua parada no primeiro plano, bastao de madeira encostado na borda.

```json
{
  "shot_id": "K02_hook_bowl_initial",
  "reference_use": "Use the attached image ONLY for Robin's exact face, identity, hair, skin texture, wardrobe and the identity of her real kitchen. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 72-year-old white American woman with a small build, straight silver white hair in a bob cut just below the ear with a side part, pale weathered skin with many age spots across her forehead, cheeks and the backs of her hands, deep lines on the forehead and around the mouth, heavy crow lines at the eyes, a soft jawline, light eyes behind thin gold rimmed reading glasses resting low on her nose, and no makeup at all. She is clearly a woman and clearly in her seventies.",
  "wardrobe": "The same heather grey cardigan over a white open collar blouse, a thin silver chain with a small silver cross pendant, and a plain gold wedding band on her left hand.",
  "prop": "A shallow wide cream ceramic bowl half filled with clear water sits on the wooden table top in the lower foreground, and the water surface is completely still and flat like a mirror. Robin's right hand holds a short wooden striker resting against the outer rim of the bowl. A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card lies face up on the table beside the bowl.",
  "scene": "The SAME real American oak kitchen as the reference image, with two windows and the sink on the right. The table group in the lower foreground holds her classic white bordered tarot deck standing in a small wooden easel, a rose quartz sphere on a stand, a citrine cluster, a pierced brass incense burner with a thin thread of smoke rising and two thin unlit white candles in brass holders. The wall group behind her holds a framed printed lunar chart, a wooden crucifix and a small United States flag on a black desk stand on the left window sill, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Robin sits upright at the kitchen table, forearms resting on the wood, leaning slightly forward, her eyes on the object in front of her and then toward the lens. Both hands stay anatomically clear and fully visible.",
  "composition": "EXTREME CLOSE foreground emphasis. The bowl of still water and the wooden striker fills the lower foreground and is much closer to the lens than Robin's face. Robin is chest-up in the upper portion of the frame. Nothing competes with it.",
  "camera": "table height, slightly high toward the bowl, pushed in very close",
  "state": "Start frame: the water is perfectly still and the striker has just touched the rim, before any sound and before the surface moves.",
  "lighting": "Soft neutral diffuse daylight from the two kitchen windows, cool and even on her face, with no warm cast. The candles are unlit and light nothing.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no de-aging, no skin smoothing, no makeup, no change of identity, no change of wardrobe"
}
```

## K03 | T1 | HOOK C A TOALHA PUXADA | GERAR DO ZERO | ANCORA ROBIN

> ### ANEXAR: **1 IMAGEM**
> **1. ANCORA ROBIN** `producao/_ancoras/Robin.Matthewsus .jpeg`
>
> ### GERAR DO ZERO

Toalha esticada com os objetos em pe em cima, as duas maos fechadas na barra.

```json
{
  "shot_id": "K03_hook_tablecloth_initial",
  "reference_use": "Use the attached image ONLY for Robin's exact face, identity, hair, skin texture, wardrobe and the identity of her real kitchen. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 72-year-old white American woman with a small build, straight silver white hair in a bob cut just below the ear with a side part, pale weathered skin with many age spots across her forehead, cheeks and the backs of her hands, deep lines on the forehead and around the mouth, heavy crow lines at the eyes, a soft jawline, light eyes behind thin gold rimmed reading glasses resting low on her nose, and no makeup at all. She is clearly a woman and clearly in her seventies.",
  "wardrobe": "The same heather grey cardigan over a white open collar blouse, a thin silver chain with a small silver cross pendant, and a plain gold wedding band on her left hand.",
  "prop": "A plain cream linen tablecloth covers the kitchen table in the lower foreground. Standing upright on the cloth are her classic white bordered tarot deck in its small wooden easel and the rose quartz sphere on its stand. A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card stands propped upright on the cloth between them. Both of Robin's hands grip the near hem of the cloth, knuckles tight, the fabric pulled taut.",
  "scene": "The SAME real American oak kitchen as the reference image, with two windows and the sink on the right. The table group in the lower foreground holds her classic white bordered tarot deck standing in a small wooden easel, a rose quartz sphere on a stand, a citrine cluster, a pierced brass incense burner with a thin thread of smoke rising and two thin unlit white candles in brass holders. The wall group behind her holds a framed printed lunar chart, a wooden crucifix and a small United States flag on a black desk stand on the left window sill, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Robin sits upright at the kitchen table, leaning forward, both hands closed on the near hem of the tablecloth, her eyes on the objects standing on it. Both hands stay anatomically clear.",
  "composition": "EXTREME CLOSE foreground emphasis. The taut tablecloth with the objects standing on it fills the lower foreground and is much closer to the lens than Robin's face. Robin is chest-up in the upper portion of the frame. Nothing competes with it.",
  "camera": "table height, slightly high toward the cloth, pushed in very close",
  "state": "Start frame: every object is standing still and upright on the cloth and her hands are closed on the hem, before the pull begins.",
  "lighting": "Soft neutral diffuse daylight from the two kitchen windows, cool and even on her face, with no warm cast. The candles are unlit and light nothing.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no de-aging, no skin smoothing, no makeup, no change of identity, no change of wardrobe"
}
```

## K04 | T1 | HOOK D A FLOR QUE ABRE NA AGUA | GERAR DO ZERO | ANCORA ROBIN

> ### ANEXAR: **1 IMAGEM**
> **1. ANCORA ROBIN** `producao/_ancoras/Robin.Matthewsus .jpeg`
>
> ### GERAR DO ZERO

Tigela de vidro com agua e a bolinha de papel dobrada acima dela.

```json
{
  "shot_id": "K04_hook_paper_initial",
  "reference_use": "Use the attached image ONLY for Robin's exact face, identity, hair, skin texture, wardrobe and the identity of her real kitchen. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 72-year-old white American woman with a small build, straight silver white hair in a bob cut just below the ear with a side part, pale weathered skin with many age spots across her forehead, cheeks and the backs of her hands, deep lines on the forehead and around the mouth, heavy crow lines at the eyes, a soft jawline, light eyes behind thin gold rimmed reading glasses resting low on her nose, and no makeup at all. She is clearly a woman and clearly in her seventies.",
  "wardrobe": "The same heather grey cardigan over a white open collar blouse, a thin silver chain with a small silver cross pendant, and a plain gold wedding band on her left hand.",
  "prop": "A wide clear glass bowl of water sits on the wooden table top in the lower foreground. Robin's fingers hold a small tightly folded paper pellet just above the water surface, dry and closed, the folds sharp and visible. A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card lies face up on the table beside the bowl.",
  "scene": "The SAME real American oak kitchen as the reference image, with two windows and the sink on the right. The table group in the lower foreground holds her classic white bordered tarot deck standing in a small wooden easel, a rose quartz sphere on a stand, a citrine cluster, a pierced brass incense burner with a thin thread of smoke rising and two thin unlit white candles in brass holders. The wall group behind her holds a framed printed lunar chart, a wooden crucifix and a small United States flag on a black desk stand on the left window sill, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Robin sits upright at the kitchen table, forearms resting on the wood, leaning slightly forward, her eyes on the object in front of her and then toward the lens. Both hands stay anatomically clear and fully visible.",
  "composition": "EXTREME CLOSE foreground emphasis. The clear bowl of water and the folded paper pellet above it fills the lower foreground and is much closer to the lens than Robin's face. Robin is chest-up in the upper portion of the frame. Nothing competes with it.",
  "camera": "table height, slightly high toward the bowl, pushed in very close",
  "state": "Start frame: the paper pellet is still dry, closed and held above the water, before it is dropped and before anything opens.",
  "lighting": "Soft neutral diffuse daylight from the two kitchen windows, cool and even on her face, with no warm cast. The candles are unlit and light nothing.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no de-aging, no skin smoothing, no makeup, no change of identity, no change of wardrobe"
}
```

## K05 | T1 | HOOK E O GLOBO SACUDIDO | GERAR DO ZERO | ANCORA ROBIN

> ### ANEXAR: **1 IMAGEM**
> **1. ANCORA ROBIN** `producao/_ancoras/Robin.Matthewsus .jpeg`
>
> ### GERAR DO ZERO

Globo de neve erguido perto da lente, flocos assentados, figuras moldadas sem rosto.

```json
{
  "shot_id": "K05_hook_globe_initial",
  "reference_use": "Use the attached image ONLY for Robin's exact face, identity, hair, skin texture, wardrobe and the identity of her real kitchen. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 72-year-old white American woman with a small build, straight silver white hair in a bob cut just below the ear with a side part, pale weathered skin with many age spots across her forehead, cheeks and the backs of her hands, deep lines on the forehead and around the mouth, heavy crow lines at the eyes, a soft jawline, light eyes behind thin gold rimmed reading glasses resting low on her nose, and no makeup at all. She is clearly a woman and clearly in her seventies.",
  "wardrobe": "The same heather grey cardigan over a white open collar blouse, a thin silver chain with a small silver cross pendant, and a plain gold wedding band on her left hand.",
  "prop": "A small glass snow globe on a dark wooden base is held in Robin's raised right hand in the lower foreground, very close to the lens. Inside the globe two small figures stand side by side under a plain arch, moulded as smooth featureless silhouettes with no facial detail at all, and the white flakes lie settled on the floor of the globe. A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card lies face up on the table below her hand.",
  "scene": "The SAME real American oak kitchen as the reference image, with two windows and the sink on the right. The table group in the lower foreground holds her classic white bordered tarot deck standing in a small wooden easel, a rose quartz sphere on a stand, a citrine cluster, a pierced brass incense burner with a thin thread of smoke rising and two thin unlit white candles in brass holders. The wall group behind her holds a framed printed lunar chart, a wooden crucifix and a small United States flag on a black desk stand on the left window sill, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Robin sits upright at the kitchen table, her right forearm lifted so the snow globe is held close to the lens, her left hand flat on the wood, her eyes on the globe and then toward the lens. Both hands stay anatomically clear.",
  "composition": "EXTREME CLOSE foreground emphasis. The snow globe in her hand fills the lower foreground and is much closer to the lens than Robin's face. Robin is chest-up in the upper portion of the frame. Nothing competes with it.",
  "camera": "table height, slightly high toward the globe, pushed in very close",
  "state": "Start frame: the globe is held still and the flakes are settled at the bottom, before the shake begins.",
  "lighting": "Soft neutral diffuse daylight from the two kitchen windows, cool and even on her face, with no warm cast. The candles are unlit and light nothing.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no de-aging, no skin smoothing, no makeup, no change of identity, no change of wardrobe"
}
```

## K06 | T2 | BODY CARTA NA MAO | GERAR DO ZERO | ANCORA ROBIN

> ### ANEXAR: **1 IMAGEM**
> **1. ANCORA ROBIN** `producao/_ancoras/Robin.Matthewsus .jpeg`
>
> ### GERAR DO ZERO

Carta SOULMATE erguida ao lado do rosto, mao esquerda apoiada na mesa.

```json
{
  "shot_id": "K06_body_card_held_initial",
  "reference_use": "Use the attached image ONLY for Robin's exact face, identity, hair, skin texture, wardrobe and the identity of her real kitchen. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 72-year-old white American woman with a small build, straight silver white hair in a bob cut just below the ear with a side part, pale weathered skin with many age spots across her forehead, cheeks and the backs of her hands, deep lines on the forehead and around the mouth, heavy crow lines at the eyes, a soft jawline, light eyes behind thin gold rimmed reading glasses resting low on her nose, and no makeup at all. She is clearly a woman and clearly in her seventies.",
  "wardrobe": "The same heather grey cardigan over a white open collar blouse, a thin silver chain with a small silver cross pendant, and a plain gold wedding band on her left hand.",
  "prop": "A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card is held upright in Robin's right hand in the lower foreground, fully visible and closer to the lens than her face.",
  "scene": "The SAME real American oak kitchen as the reference image, with two windows and the sink on the right. The table group in the lower foreground holds her classic white bordered tarot deck standing in a small wooden easel, a rose quartz sphere on a stand, a citrine cluster, a pierced brass incense burner with a thin thread of smoke rising and two thin unlit white candles in brass holders. The wall group behind her holds a framed printed lunar chart, a wooden crucifix and a small United States flag on a black desk stand on the left window sill, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Robin sits upright at the kitchen table, holding the card steady beside her cheek and looking directly into the lens. Her left hand rests flat and still on the table. Both hands stay anatomically clear.",
  "composition": "Tight chest-up talking frame. The SOULMATE card occupies the lower foreground and Robin's face fills the upper third. The kitchen stays recognizable without competing with the card.",
  "camera": "eye level, straight-on, close phone-camera distance",
  "state": "Start frame: Robin already holds the card upright beside her face and looks into the lens, her expression confiding and certain, before speaking.",
  "lighting": "Soft neutral diffuse daylight from the two kitchen windows, cool and even on her face, with no warm cast. The candles are unlit and light nothing.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no de-aging, no skin smoothing, no makeup, no change of identity, no change of wardrobe"
}
```

## K07 | T3 | BODY CARTA NA MAO | EDITAR do K06

> ### ANEXAR: **1 IMAGEM**
> **1. O K06 ja aprovado**
>
> NUNCA anexar K07, K08, K09 ou K10 aqui
>
> ### EDITAR, muda so gesto, expressao e distancia

Mesmo setup, dedo esquerdo na borda da mesa, expressao de aviso.

```json
{
  "shot_id": "K07_body_card_held_initial",
  "reference_use": "Use the attached image ONLY for Robin's exact face, identity, hair, skin texture, wardrobe and the identity of her real kitchen. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 72-year-old white American woman with a small build, straight silver white hair in a bob cut just below the ear with a side part, pale weathered skin with many age spots across her forehead, cheeks and the backs of her hands, deep lines on the forehead and around the mouth, heavy crow lines at the eyes, a soft jawline, light eyes behind thin gold rimmed reading glasses resting low on her nose, and no makeup at all. She is clearly a woman and clearly in her seventies.",
  "wardrobe": "The same heather grey cardigan over a white open collar blouse, a thin silver chain with a small silver cross pendant, and a plain gold wedding band on her left hand.",
  "prop": "A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card is held upright in Robin's right hand in the lower foreground, fully visible and closer to the lens than her face.",
  "scene": "The SAME real American oak kitchen as the reference image, with two windows and the sink on the right. The table group in the lower foreground holds her classic white bordered tarot deck standing in a small wooden easel, a rose quartz sphere on a stand, a citrine cluster, a pierced brass incense burner with a thin thread of smoke rising and two thin unlit white candles in brass holders. The wall group behind her holds a framed printed lunar chart, a wooden crucifix and a small United States flag on a black desk stand on the left window sill, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Robin sits upright at the kitchen table, holding the card steady beside her cheek and looking directly into the lens. Her left index finger rests on the edge of the table. Both hands stay anatomically clear.",
  "composition": "Tight chest-up talking frame. The SOULMATE card occupies the lower foreground and Robin's face fills the upper third. The kitchen stays recognizable without competing with the card.",
  "camera": "eye level, straight-on, close phone-camera distance",
  "state": "Start frame: Robin already holds the card upright beside her face and looks into the lens, her expression firm and warning, before speaking.",
  "lighting": "Soft neutral diffuse daylight from the two kitchen windows, cool and even on her face, with no warm cast. The candles are unlit and light nothing.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no de-aging, no skin smoothing, no makeup, no change of identity, no change of wardrobe"
}
```

## K08 | T4 | BODY CARTA NA MAO | EDITAR do K06

> ### ANEXAR: **1 IMAGEM**
> **1. O K06 ja aprovado**
>
> NUNCA anexar K07, K08, K09 ou K10 aqui
>
> ### EDITAR, muda so gesto, expressao e distancia

Mesmo setup, mao esquerda aberta para a lente, expressao instrutiva.

```json
{
  "shot_id": "K08_body_card_held_initial",
  "reference_use": "Use the attached image ONLY for Robin's exact face, identity, hair, skin texture, wardrobe and the identity of her real kitchen. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 72-year-old white American woman with a small build, straight silver white hair in a bob cut just below the ear with a side part, pale weathered skin with many age spots across her forehead, cheeks and the backs of her hands, deep lines on the forehead and around the mouth, heavy crow lines at the eyes, a soft jawline, light eyes behind thin gold rimmed reading glasses resting low on her nose, and no makeup at all. She is clearly a woman and clearly in her seventies.",
  "wardrobe": "The same heather grey cardigan over a white open collar blouse, a thin silver chain with a small silver cross pendant, and a plain gold wedding band on her left hand.",
  "prop": "A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card is held upright in Robin's right hand in the lower foreground, fully visible and closer to the lens than her face.",
  "scene": "The SAME real American oak kitchen as the reference image, with two windows and the sink on the right. The table group in the lower foreground holds her classic white bordered tarot deck standing in a small wooden easel, a rose quartz sphere on a stand, a citrine cluster, a pierced brass incense burner with a thin thread of smoke rising and two thin unlit white candles in brass holders. The wall group behind her holds a framed printed lunar chart, a wooden crucifix and a small United States flag on a black desk stand on the left window sill, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Robin sits upright at the kitchen table, holding the card steady beside her cheek and looking directly into the lens. Her left hand is open and turned toward the lens. Both hands stay anatomically clear.",
  "composition": "Tight chest-up talking frame. The SOULMATE card occupies the lower foreground and Robin's face fills the upper third. The kitchen stays recognizable without competing with the card.",
  "camera": "eye level, straight-on, close phone-camera distance",
  "state": "Start frame: Robin already holds the card upright beside her face and looks into the lens, her expression direct and instructive, before speaking.",
  "lighting": "Soft neutral diffuse daylight from the two kitchen windows, cool and even on her face, with no warm cast. The candles are unlit and light nothing.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no de-aging, no skin smoothing, no makeup, no change of identity, no change of wardrobe"
}
```

## K09 | T5 | BODY CARTA NA MAO | EDITAR do K06

> ### ANEXAR: **1 IMAGEM**
> **1. O K06 ja aprovado**
>
> NUNCA anexar K07, K08, K09 ou K10 aqui
>
> ### EDITAR, muda so gesto, expressao e distancia

Mesmo setup, mao esquerda de volta na mesa, expressao calorosa e certa.

```json
{
  "shot_id": "K09_body_card_held_initial",
  "reference_use": "Use the attached image ONLY for Robin's exact face, identity, hair, skin texture, wardrobe and the identity of her real kitchen. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 72-year-old white American woman with a small build, straight silver white hair in a bob cut just below the ear with a side part, pale weathered skin with many age spots across her forehead, cheeks and the backs of her hands, deep lines on the forehead and around the mouth, heavy crow lines at the eyes, a soft jawline, light eyes behind thin gold rimmed reading glasses resting low on her nose, and no makeup at all. She is clearly a woman and clearly in her seventies.",
  "wardrobe": "The same heather grey cardigan over a white open collar blouse, a thin silver chain with a small silver cross pendant, and a plain gold wedding band on her left hand.",
  "prop": "A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card is held upright in Robin's right hand in the lower foreground, fully visible and closer to the lens than her face.",
  "scene": "The SAME real American oak kitchen as the reference image, with two windows and the sink on the right. The table group in the lower foreground holds her classic white bordered tarot deck standing in a small wooden easel, a rose quartz sphere on a stand, a citrine cluster, a pierced brass incense burner with a thin thread of smoke rising and two thin unlit white candles in brass holders. The wall group behind her holds a framed printed lunar chart, a wooden crucifix and a small United States flag on a black desk stand on the left window sill, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Robin sits upright at the kitchen table, holding the card steady beside her cheek and looking directly into the lens. Her left hand has lowered back onto the table. Both hands stay anatomically clear.",
  "composition": "Tight chest-up talking frame. The SOULMATE card occupies the lower foreground and Robin's face fills the upper third. The kitchen stays recognizable without competing with the card.",
  "camera": "eye level, straight-on, close phone-camera distance",
  "state": "Start frame: Robin already holds the card upright beside her face and looks into the lens, her expression warm and sure, before speaking.",
  "lighting": "Soft neutral diffuse daylight from the two kitchen windows, cool and even on her face, with no warm cast. The candles are unlit and light nothing.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no de-aging, no skin smoothing, no makeup, no change of identity, no change of wardrobe"
}
```

## K10 | T6 | CTA | EDITAR do K06

> ### ANEXAR: **1 IMAGEM**
> **1. O K06 ja aprovado**
>
> NUNCA anexar K07, K08, K09 ou K10 aqui
>
> ### EDITAR, muda so gesto, expressao e distancia

Plano mais fechado do video, dedo esquerdo apontando para a lente.

```json
{
  "shot_id": "K10_cta_card_held_initial",
  "reference_use": "Use the attached image ONLY for Robin's exact face, identity, hair, skin texture, wardrobe and the identity of her real kitchen. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 72-year-old white American woman with a small build, straight silver white hair in a bob cut just below the ear with a side part, pale weathered skin with many age spots across her forehead, cheeks and the backs of her hands, deep lines on the forehead and around the mouth, heavy crow lines at the eyes, a soft jawline, light eyes behind thin gold rimmed reading glasses resting low on her nose, and no makeup at all. She is clearly a woman and clearly in her seventies.",
  "wardrobe": "The same heather grey cardigan over a white open collar blouse, a thin silver chain with a small silver cross pendant, and a plain gold wedding band on her left hand.",
  "prop": "A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card is held upright in Robin's right hand in the lower foreground, fully visible and closer to the lens than her face.",
  "scene": "The SAME real American oak kitchen as the reference image, with two windows and the sink on the right. The table group in the lower foreground holds her classic white bordered tarot deck standing in a small wooden easel, a rose quartz sphere on a stand, a citrine cluster, a pierced brass incense burner with a thin thread of smoke rising and two thin unlit white candles in brass holders. The wall group behind her holds a framed printed lunar chart, a wooden crucifix and a small United States flag on a black desk stand on the left window sill, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Robin sits upright at the kitchen table, holding the card steady beside her face and looking straight into the lens. Her left index finger enters from the lower edge and points directly toward the lens. Both hands stay anatomically clear.",
  "composition": "The TIGHTEST frame of the whole video, about twenty percent closer than the talking frames. Robin's face and the SOULMATE card are the only dominant elements. The kitchen is reduced by framing alone and everything still in frame stays in sharp focus.",
  "camera": "eye level, straight-on, pushed in closer than any other frame",
  "state": "Start frame: Robin already holds the card upright beside her face and looks into the lens, her expression urgent and direct, before speaking.",
  "lighting": "Soft neutral diffuse daylight from the two kitchen windows, cool and even on her face, with no warm cast. The candles are unlit and light nothing.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no de-aging, no skin smoothing, no makeup, no change of identity, no change of wardrobe"
}
```

## K11 | T7 | CTA | EDITAR do K06

> ### ANEXAR: **1 IMAGEM**
> **1. O K06 ja aprovado**
>
> NUNCA anexar K07, K08, K09 ou K10 aqui
>
> ### EDITAR, muda so gesto, expressao e distancia

Plano mais fechado do video, carta ao lado do rosto, mao esquerda fora de quadro.

```json
{
  "shot_id": "K11_cta_card_held_initial",
  "reference_use": "Use the attached image ONLY for Robin's exact face, identity, hair, skin texture, wardrobe and the identity of her real kitchen. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 72-year-old white American woman with a small build, straight silver white hair in a bob cut just below the ear with a side part, pale weathered skin with many age spots across her forehead, cheeks and the backs of her hands, deep lines on the forehead and around the mouth, heavy crow lines at the eyes, a soft jawline, light eyes behind thin gold rimmed reading glasses resting low on her nose, and no makeup at all. She is clearly a woman and clearly in her seventies.",
  "wardrobe": "The same heather grey cardigan over a white open collar blouse, a thin silver chain with a small silver cross pendant, and a plain gold wedding band on her left hand.",
  "prop": "A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card is held upright in Robin's right hand in the lower foreground, fully visible and closer to the lens than her face.",
  "scene": "The SAME real American oak kitchen as the reference image, with two windows and the sink on the right. The table group in the lower foreground holds her classic white bordered tarot deck standing in a small wooden easel, a rose quartz sphere on a stand, a citrine cluster, a pierced brass incense burner with a thin thread of smoke rising and two thin unlit white candles in brass holders. The wall group behind her holds a framed printed lunar chart, a wooden crucifix and a small United States flag on a black desk stand on the left window sill, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Robin sits upright at the kitchen table, holding the card steady beside her face and looking straight into the lens. Her left hand stays below the frame edge. Both hands stay anatomically clear.",
  "composition": "The TIGHTEST frame of the whole video, about twenty percent closer than the talking frames. Robin's face and the SOULMATE card are the only dominant elements. The kitchen is reduced by framing alone and everything still in frame stays in sharp focus.",
  "camera": "eye level, straight-on, pushed in closer than any other frame",
  "state": "Start frame: Robin already holds the card upright beside her face and looks into the lens, her expression certain and almost tender, before speaking.",
  "lighting": "Soft neutral diffuse daylight from the two kitchen windows, cool and even on her face, with no warm cast. The candles are unlit and light nothing.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no de-aging, no skin smoothing, no makeup, no change of identity, no change of wardrobe"
}
```

## Mapa de ancoras

| Keyframe | Referencias a anexar | Modelo |
|---|---|---|
| K01 a K06 | ancora ROBIN | Nano Banana 2, 9:16 |
| K07 a K11 | o K06 aprovado | Nano Banana 2, 9:16 |

No bloco de execucao do Flow o anexo e **so a ancora ROBIN** nos onze, porque la todo prompt e
autossuficiente e a carta vai descrita por escrito.

## Montagem no CapCut

- Timeline 1080 x 1920, 30 fps. Cortar o silencio inicial, a fala comeca no primeiro frame.
- **Um gancho por versao final.** Cinco ganchos geram cinco videos: K01 mais o corpo comum, K02 mais o
  corpo comum, e assim por diante.
- Marca d'agua `222` fixa no canto superior direito o video inteiro, herdada do modelo.
- Caixa branca de texto do 0s ao 8s, com a frase escolhida pelo Luigi. Nunca gerada na imagem.
- Legenda karaoke de duas ou tres palavras, branca com destaque vermelho, como o modelo.
- **Seta vermelha grande apontando para a foto de perfil** entrando junto do T6 e ficando ate o fim.
- Nao cobrir a carta SOULMATE com legenda. Manter o `222` isolado visualmente no T4.
- Sem musica, ou trilha em -19 a -20 dB. Conferir lip sync e a ultima palavra de cada take.

## Gates de qualidade

1. `identity_main` dos onze comeca com `The EXACT woman`, e ela tem 72 anos em todos.
2. `no de-aging`, `no skin smoothing` e `no makeup` no negative dos onze.
3. Bandeira dos EUA no campo `scene` dos onze, discreta, visivel e em foco.
4. Heroi no lower foreground, mais perto da lente que o rosto, nos onze.
5. K10 e K11 sao o plano mais fechado do video inteiro.
6. So o estado inicial em cada imagem. Pedra fechada, agua parada, papel dobrado, flocos assentados,
   toalha esticada. A transformacao acontece no clipe.
7. Nenhum rosto de alma gemea legivel em lugar nenhum. As figuras do globo sao moldadas sem rosto,
   que e propriedade fisica do objeto e nao desfoque.
8. Zero fogo aceso em quadro nos onze, o que tira o gatilho de moderacao que ja travou antes.
9. `no captions` no negative dos onze, e nenhum termo sensivel listado la.
10. Cenario descrito em dois grupos, mesa e parede, nunca item a item solto.
11. Produto nunca em quadro. Sem app, sem quiz, sem celular, sem preco.
12. `python checar_entrega.py producao/manifestselizabeth` sem nenhuma FALHA.

