# Pacote FityWell, anúncio pago: filha conta da mãe (2026-10-06)

Roteiro aprovado: ROTEIRO.md (v6). Flow: AGENTE_FLOW_FITYWELL_MAE_FILHA.md.

## Mapa de anexos
| Item | Anexar | Modelo | Variações |
|---|---|---|---|
| REF-P2 | imagem da mãe | Nano Banana 2.1 | 4, 9:16 |
| K01 | REF-P2 escolhido | Nano Banana 2.1 | 4, 9:16 |
| K02 | imagem da mãe | Nano Banana 2.1 | 4, 9:16 |
| K03 | REF-P2 escolhido + imagem da mãe | Nano Banana 2.1 | 4, 9:16 |
| V01 (ou V01B) | imagem escolhida do K01 | Omni 1.1 Flash, 8 s | 1, 9:16 |
| V03 a V08 | imagem escolhida do K03 | Omni 1.1 Flash, 8 s | 1, 9:16 |

## Prompts de imagem

Character sheet da filha. Anexo: só a imagem aprovada da mãe (a do treino de ontem).
```
REF-P2
{
  "format": "9:16 vertical photographic character reference sheet, real photo look, not an illustration",
  "fiction_note": "This is a fictional AI-generated scene, no real person is depicted.",
  "reference_use": "The attached image shows the MOTHER. Use it only for family resemblance (face shape, eyes, nose, smile). The person in this sheet is her adult daughter, a different and much younger woman. Do not copy the mother's age, silver hair or body.",
  "identity_main": "A white American woman of about 32, clearly the adult daughter of the older woman: the same oval face shape, the same warm friendly eyes, the same nose and the same smile. Shoulder-length straight dirty-blonde hair with slightly darker roots, parted a little off-center. Light fair skin with light freckles across the nose and cheeks, visible pores and real texture, almost no makeup, just mascara and a tinted lip balm. Slim, healthy average build, a friendly girl-next-door American look.",
  "wardrobe": "Oatmeal cream chunky knit crewneck sweater with the sleeves slightly pushed up, light blue straight-leg jeans, small gold hoop earrings and a thin gold chain necklace. Nothing green on her. White low-top sneakers.",
  "scene": "Plain seamless light grey photo backdrop, nothing else.",
  "prop": "None. Both hands empty.",
  "posture": "Relaxed, neutral, arms down at her sides, soft closed-mouth smile, looking at the camera in the front views.",
  "composition": "Character sheet in two rows on the same light grey backdrop. Top row: three head-and-shoulders portraits of the same woman, front view, three-quarter view and side profile. Bottom row: two full-body standing views, front and three-quarter. Same woman, same outfit and same lighting in all five views, evenly spaced, nothing overlapping.",
  "camera": "Phone main 1x lens at chest height, straight-on, level, sharp",
  "lighting": "Soft neutral daylight, even and cool-grey, gentle shadows, no harsh highlights.",
  "state": "Reference sheet of the daughter, calm and natural.",
  "realism": "Real skin with visible pores, fine lines, irregular texture and soft natural asymmetry, hands with natural knuckles and creases, phone-camera footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, everything in sharp focus including the background, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no captions, no subtitles, no words overlaid on the image, no emoji.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no labels, no emoji, no green clothing, no silver hair, no older woman, no heavy makeup, no blur, no bokeh, no warm color cast, no yellow tint, no plastic skin, no smoothed face, no extra fingers"
}
```

T1, filha no fundo verde apontando para cima. Anexo: só o REF-P2 escolhido.
```
K01
{
  "format": "9:16 vertical, front-camera phone video frame of a woman talking to camera in front of a green screen",
  "fiction_note": "This is a fictional AI-generated scene, no real person is depicted.",
  "reference_use": "The attached character sheet is the woman. Keep her face, hair, freckles and outfit exactly.",
  "identity_main": "A white American woman of about 32, with an oval face, warm friendly eyes and a friendly smile. Shoulder-length straight dirty-blonde hair with slightly darker roots, parted a little off-center. Light fair skin with light freckles across the nose and cheeks, visible pores and real texture, almost no makeup, just mascara and a tinted lip balm. Slim, healthy average build, a friendly girl-next-door American look.",
  "wardrobe": "Oatmeal cream chunky knit crewneck sweater with the sleeves slightly pushed up, light blue straight-leg jeans, small gold hoop earrings and a thin gold chain necklace. Nothing green on her.",
  "scene": "A flat, evenly lit, solid chroma-key green backdrop fills the whole background from edge to edge, smooth, no wrinkles, no shadows on it, no props, no furniture, nothing else in the background.",
  "prop": "None. No phone in her hands.",
  "posture": "She faces the camera mid-sentence with her mouth slightly open and a teasing playful grin, eyebrows raised. Her right hand is raised to the height of her head, a little out to the side, with the index finger pointing slightly upward and slightly back, as if pointing at something behind her above her shoulder. Her left arm hangs relaxed at her side.",
  "composition": "Waist-up framing, she is centered and fills about 70 percent of the frame height, her raised pointing hand fully inside the frame with space around it, green backdrop visible around her head and on both sides. Her face is about 0.8 meters from the lens.",
  "camera": "Phone front camera on a tripod at chest height, 0.8 meters away, level, straight-on, vertical, steady",
  "lighting": "Soft neutral daylight-balanced light from the front, even on her face and on the green backdrop, no green spill on her hair or skin, no hard shadows behind her.",
  "state": "Start frame of a TikTok style green screen video, she is about to roast her mom in a loving, joking way.",
  "realism": "Real skin with visible pores, fine lines, irregular texture and soft natural asymmetry, hands with natural knuckles and creases, phone-camera footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, everything in sharp focus including the background, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no captions, no subtitles, no words overlaid on the image, no emoji.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no emoji, no picture in the background, no green clothing, no green spill on hair, no shadow on the backdrop, no blur, no bokeh, no warm color cast, no yellow tint, no plastic skin, no smoothed face, no extra fingers, no studio look"
}
```

Foto parada da mãe obesa no sofá, entra no lugar do verde no T1. Anexo: só a imagem da mãe.
```
K02
{
  "format": "9:16 vertical, candid phone snapshot taken by a family member about a year ago, ordinary home photo",
  "fiction_note": "This is a fictional AI-generated scene, no real person is depicted.",
  "reference_use": "The attached image is the woman. Keep her face, eyes, smile, short silver-white hair and age exactly. Only her body is different: she is much heavier in this photo.",
  "identity_main": "A woman of about 60 with short cropped silver-white hair brushed to the side, a soft feminine face with warm eyes and visible expression lines at the eyes, mouth and forehead, light fair skin with real texture, visible pores, fine wrinkles and small age spots, not smoothed, not de-aged. She wears one thin silver bracelet on her left wrist and one small silver ring on her left hand. In this photo she is clearly obese in a realistic, everyday way, like a real woman of about 280 pounds: a large round belly, wide hips, heavy upper arms, a fuller round face with a double chin, with natural, believable body proportions, legs in normal proportion to her body.",
  "wardrobe": "Clothes one size too small that look snug and tight on her: a plain faded maroon short-sleeve t-shirt pulling a little across her belly and chest but still covering her stomach completely, and loose-fitting light grey jersey sweatpants slightly tight at the waist. White socks.",
  "scene": "An ordinary American living room in the late afternoon with the lights off, a little gloomy: a plain blue-grey painted wall behind her and a white crown moulding at the ceiling. She sits on a grey fabric couch with a rumpled throw blanket. A small American flag in a jar on a side table next to the couch, small but clearly visible and in focus.",
  "prop": "She holds an open crumpled snack bag of bright orange cheese-dusted tortilla chips in her lap with one hand, a plain unbranded bag with no logo and no text, one chip in her other hand. A little orange cheese dust on her lips and fingertips.",
  "posture": "She sits slumped back on the couch, shoulders dropped, looking down and slightly to the side with a sad, tired, lost expression, as if she does not know what to do anymore. Mouth closed, no smile.",
  "composition": "Sitting on the couch, framed from the top of her head to just below the knees, centered, she fills about 75 percent of the frame height, about 1.8 meters from the lens. Couch behind her, the side table with the flag at the left edge.",
  "camera": "Phone main 1x lens at chest height, 1.8 meters away, slightly tilted, handheld candid snapshot",
  "lighting": "Dim, natural light: only grey overcast daylight from a window outside the frame on the left, lights off, soft and cool, gentle real shadows, the room looks a bit dark and sad but everything is still visible. Not a studio, no dramatic spotlight.",
  "state": "An ordinary sad afternoon a year ago, before she changed, she looks tired and discouraged.",
  "realism": "Real skin with visible pores, fine lines, irregular texture and soft natural asymmetry, hands with natural knuckles and creases, phone-camera footage look, flat natural light, low contrast, slight JPEG compression, slight phone noise from the low light, boring everyday reality, everything in sharp focus including the background, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no captions, no subtitles, no words overlaid on the image, no emoji.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no emoji, no logo, no brand name, no text on the bag, no second person, no bare belly, no exposed stomach, no ripped clothes, no oversized legs, no exaggerated body, no caricature, no cinematic lighting, no blur, no bokeh, no warm color cast, no yellow tint, no plastic skin, no smoothed face, no extra fingers"
}
```

T3 a T8, selfie das duas na sala. Anexos: REF-P2 escolhido + imagem da mãe.
```
K03
{
  "format": "9:16 vertical, front-camera selfie phone video frame",
  "fiction_note": "This is a fictional AI-generated scene, no real person is depicted.",
  "reference_use": "Two people. The attached character sheet is the younger woman (the daughter): keep her face, hair, freckles and outfit exactly. The attached photo of the older woman is the mother: keep her face, short silver-white hair, age and her strong, defined, feminine build exactly.",
  "identity_main": "Younger woman: A white American woman of about 32, clearly the adult daughter of the older woman: the same oval face shape, the same warm friendly eyes, the same nose and the same smile. Shoulder-length straight dirty-blonde hair with slightly darker roots, parted a little off-center. Light fair skin with light freckles across the nose and cheeks, visible pores and real texture, almost no makeup, just mascara and a tinted lip balm. Slim, healthy average build, a friendly girl-next-door American look. Older woman: A woman of about 60 with short cropped silver-white hair brushed to the side, a soft feminine face with warm friendly eyes, a gentle smile and visible expression lines at the eyes, mouth and forehead, light fair skin with real texture, visible pores, fine wrinkles and small age spots, not smoothed, not de-aged. She wears one thin silver bracelet on her left wrist and one small silver ring on her left hand. She is lean, strong, defined and feminine: rounded defined shoulders, toned arms, slim waist, flat toned stomach, never bulky.",
  "wardrobe": "Younger woman: Oatmeal cream chunky knit crewneck sweater with the sleeves slightly pushed up, light blue straight-leg jeans, small gold hoop earrings and a thin gold chain necklace. Nothing green on her. Older woman: plain black short-sleeve fitted cropped athletic t-shirt ending above the navel, plain black seamless high-waisted full-length leggings, barefoot, small silver stud earrings.",
  "scene": "The same ordinary American living room: plain light blue-grey painted wall, white crown moulding along the ceiling, light beige wooden laminate floor. Lived-in and a bit messy: a grey fabric couch behind them with a rumpled throw blanket, pillows askew and a hoodie tossed over the armrest, the tall green leafy plant in a white pot with a grey marble pattern at the right edge, and a small American flag in a jar on a side table by the couch, small but clearly visible and in focus. On the floor right beside the mother's feet: a rolled-out purple yoga mat, two fabric resistance loop bands (one pink, one blue) lying on it, a small white towel and a clear water bottle.",
  "prop": "The younger woman holds the phone (out of frame) with her right arm extended toward the camera; her forearm enters from the lower left edge of the frame.",
  "posture": "Shoulder to shoulder. The daughter is in the left foreground, slightly closer to the lens, talking to the camera with a big grin. The mother stands right beside her on the right, just behind, smiling proudly, slightly out of breath, one hand on her hip.",
  "composition": "Slightly high selfie angle looking down, both women from head to knees, the daughter's face about 0.6 meters from the lens and filling the upper left, the mother's face upper right, the yoga mat, bands and towel clearly visible on the floor at the lower right beside the mother's legs. Couch behind them, plant at the right edge.",
  "camera": "Phone front camera in wide mode held at arm's length, slightly above head height and angled down, 0.6 meters from the daughter, vertical, handheld",
  "lighting": "Soft neutral overcast daylight from a window outside the frame on the left, cool grey tone, flat and even.",
  "state": "The mother just finished her home workout: a visible sheen of sweat on her forehead, neck, chest and arms, silver hair slightly damp at the temples, flushed cheeks, still looking elegant and put-together.",
  "realism": "Real skin with visible pores, fine lines, irregular texture and soft natural asymmetry, hands with natural knuckles and creases, phone-camera footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, everything in sharp focus including the background, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no captions, no subtitles, no words overlaid on the image, no emoji.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no emoji, no third person, no phone visible in frame, no logo text, no gym, no blur, no bokeh, no warm color cast, no yellow tint, no plastic skin, no smoothed face, no extra fingers, no bodybuilder physique, no tidy showroom"
}
```

## Prompts de vídeo

T1, do K01.
```
V01
o avatar (mulher de uns 32 anos) fala em inglês com sotaque americano, voz autêntica de UGC de TikTok, debochada, rindo, tom de zoeira carinhosa com a própria mãe, a seguinte frase: "This bitch was fat as hell not long ago. Then she found an app that's going viral on TikTok right now, and one month later? Look at her."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela fala para a câmera com a mão direita levantada na altura da cabeça, apontando levemente para cima e para trás; em "Look at her" ela abre a mão e aponta para o lado, rindo. O fundo verde continua liso e verde do começo ao fim.

câmera: fixa

som ambiente: quarto silencioso, sem música
```

T1 alternativo ("This lady"), só se o V01 travar. Do K01.
```
V01B
o avatar (mulher de uns 32 anos) fala em inglês com sotaque americano, voz autêntica de UGC de TikTok, debochada, rindo, tom de zoeira carinhosa com a própria mãe, a seguinte frase: "This lady was fat as hell not long ago. Then she found an app that's going viral on TikTok right now, and one month later? Look at her."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela fala para a câmera com a mão direita levantada na altura da cabeça, apontando levemente para cima e para trás; em "Look at her" ela abre a mão e aponta para o lado, rindo. O fundo verde continua liso e verde do começo ao fim.

câmera: fixa

som ambiente: quarto silencioso, sem música
```

T3, do K03.
```
V03
a mulher mais jovem, que segura o celular (mulher de uns 32 anos), fala em inglês com sotaque americano, voz autêntica de UGC de TikTok, animada e sincera, como quem conta a história da própria mãe, a seguinte frase: "She was stressed all day, barely sleeping, craving sugar all night. She did those generic workouts her gym trainer gave her."

a mulher mais jovem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. Só a mulher mais jovem fala. A mulher mais velha não fala em nenhum momento, fica de boca fechada ou só sorri.

o que acontece no vídeo: a filha fala olhando para a lente; a mãe ao lado respira um pouco ofegante, enxuga a testa com o dorso da mão e balança a cabeça concordando.

câmera: selfie na mão da mulher mais jovem, leve handheld natural

som ambiente: sala de casa silenciosa, leve respiração ofegante da mulher mais velha, sem música
```

T4, do K03.
```
V04
a mulher mais jovem, que segura o celular (mulher de uns 32 anos), fala em inglês com sotaque americano, voz autêntica de UGC de TikTok, animada e sincera, como quem conta a história da própria mãe, a seguinte frase: "She stuffed herself with internet supplements promising miracles. She even took Ozempic just to lose weight."

a mulher mais jovem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. Só a mulher mais jovem fala. A mulher mais velha não fala em nenhum momento, fica de boca fechada ou só sorri.

o que acontece no vídeo: a filha fala olhando para a lente e olha de canto para a mãe em "Ozempic"; a mãe ri sem graça e balança a cabeça de leve.

câmera: selfie na mão da mulher mais jovem, leve handheld natural

som ambiente: sala de casa silenciosa, leve respiração ofegante da mulher mais velha, sem música
```

T5, do K03.
```
V05
a mulher mais jovem, que segura o celular (mulher de uns 32 anos), fala em inglês com sotaque americano, voz autêntica de UGC de TikTok, séria e acolhedora, falando direto com outras mães, a seguinte frase: "If you're a mom over forty, tired, stressed, doing everything right, and the scale still won't budge, your problem isn't a lack of willpower."

a mulher mais jovem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. Só a mulher mais jovem fala. A mulher mais velha não fala em nenhum momento, fica de boca fechada ou só sorri.

o que acontece no vídeo: a filha fala séria, olhando direto na lente; a mãe ao lado concorda devagar com a cabeça.

câmera: selfie na mão da mulher mais jovem, leve handheld natural

som ambiente: sala de casa silenciosa, leve respiração ofegante da mulher mais velha, sem música
```

T6, do K03.
```
V06
a mulher mais jovem, que segura o celular (mulher de uns 32 anos), fala em inglês com sotaque americano, voz autêntica de UGC de TikTok, animada e sincera, como quem conta a história da própria mãe, a seguinte frase: "Generic workouts and supplements from some random personal trainer aren't made for your body. What works for one woman won't work for another in most cases."

a mulher mais jovem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. Só a mulher mais jovem fala. A mulher mais velha não fala em nenhum momento, fica de boca fechada ou só sorri.

o que acontece no vídeo: a filha fala olhando para a lente; a mãe ao lado sorri e concorda com a cabeça.

câmera: selfie na mão da mulher mais jovem, leve handheld natural

som ambiente: sala de casa silenciosa, leve respiração ofegante da mulher mais velha, sem música
```

T7, do K03.
```
V07
a mulher mais jovem, que segura o celular (mulher de uns 32 anos), fala em inglês com sotaque americano, voz autêntica de UGC de TikTok, animada e sincera, como quem conta a história da própria mãe, a seguinte frase: "The only thing that works is a plan made just for you. You put your info in the app, and it builds your Belly Melt Plan."

a mulher mais jovem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. Só a mulher mais jovem fala. A mulher mais velha não fala em nenhum momento, fica de boca fechada ou só sorri.

o que acontece no vídeo: a filha fala olhando para a lente e sorri para a mãe no fim; a mãe ajeita o cabelo úmido e sorri orgulhosa.

câmera: selfie na mão da mulher mais jovem, leve handheld natural

som ambiente: sala de casa silenciosa, leve respiração ofegante da mulher mais velha, sem música
```

T8, do K03.
```
V08
a mulher mais jovem, que segura o celular (mulher de uns 32 anos), fala em inglês com sotaque americano, voz autêntica de UGC de TikTok, animada e sincera, como quem conta a história da própria mãe, a seguinte frase: "Tap Learn More below and build your Belly Melt Plan on FityWell. It's the app my mom used, and now she's recommending it to her friends."

a mulher mais jovem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. Só a mulher mais jovem fala. A mulher mais velha não fala em nenhum momento, fica de boca fechada ou só sorri.

o que acontece no vídeo: a filha aponta com a mão livre para baixo, para fora do quadro, enquanto fala; a mãe sorri e acena para a câmera.

câmera: selfie na mão da mulher mais jovem, leve handheld natural

som ambiente: sala de casa silenciosa, leve respiração ofegante da mulher mais velha, sem música
```

## Montagem no CapCut
1. T1: V01 com chroma key no verde; atrás dela, o K02 (mãe obesa) até "not long ago". Em "Then" o fundo some ou vira a sala. Bipe opcional no "bitch".
2. T2: o vídeo da mãe treinando (25,5 s), mudo, com a trilha e o texto de tela de COPY_TELA.md, sem o CTA do fim (o CTA fica no T8).
3. T3 a T8: V03 a V08 em sequência, corte seco.
4. Texto de tela só no CapCut. Botão do anúncio: Learn More / Saiba mais.

## Transcrição por take
| Take | English | Português |
|---|---|---|
| T1 | This bitch was fat as hell not long ago. Then she found an app that's going viral on TikTok right now, and one month later? Look at her. | Essa filha da puta era gorda pra caramba até pouco tempo atrás. Aí ela achou um aplicativo que tá viralizando agora no TikTok e, um mês depois? Olha pra ela. |
| T2 | (sem fala) | (sem fala) |
| T3 | She was stressed all day, barely sleeping, craving sugar all night. She did those generic workouts her gym trainer gave her. | Ela vivia estressada o dia todo, mal dormia e com vontade de doce a noite toda. Fazia aqueles treinos genéricos que o personal da academia passava pra ela. |
| T4 | She stuffed herself with internet supplements promising miracles. She even took Ozempic just to lose weight. | Se entupiu de suplementos da internet com promessas milagrosas. Até tomou Ozempic pra tentar emagrecer. |
| T5 | If you're a mom over forty, tired, stressed, doing everything right, and the scale still won't budge, your problem isn't a lack of willpower. | Se você é mãe, tem mais de quarenta, está cansada, estressada, fazendo tudo certo e a balança continua parada, seu problema não é falta de força de vontade. |
| T6 | Generic workouts and supplements from some random personal trainer aren't made for your body. What works for one woman won't work for another in most cases. | Treino e suplemento genéricos de um personal trainer qualquer não foram feitos para o seu corpo. O que funciona para uma mulher não funciona para outra na maioria dos casos. |
| T7 | The only thing that works is a plan made just for you. You put your info in the app, and it builds your Belly Melt Plan. | A única coisa que funciona é um plano feito só para você. Você coloca suas informações no aplicativo e ele monta o seu Belly Melt Plan. |
| T8 | Tap Learn More below and build your Belly Melt Plan on FityWell. It's the app my mom used, and now she's recommending it to her friends. | Toque em Saiba mais abaixo e monte o seu Belly Melt Plan no FityWell. É o aplicativo que minha mãe usou e já tá recomendando pras amigas. |

## Roteiro final em inglês
T1. This bitch was fat as hell not long ago. Then she found an app that's going viral on TikTok right now, and one month later? Look at her.
T2. (silent insert: mom's workout video)
T3. She was stressed all day, barely sleeping, craving sugar all night. She did those generic workouts her gym trainer gave her.
T4. She stuffed herself with internet supplements promising miracles. She even took Ozempic just to lose weight.
T5. If you're a mom over forty, tired, stressed, doing everything right, and the scale still won't budge, your problem isn't a lack of willpower.
T6. Generic workouts and supplements from some random personal trainer aren't made for your body. What works for one woman won't work for another in most cases.
T7. The only thing that works is a plan made just for you. You put your info in the app, and it builds your Belly Melt Plan.
T8. Tap Learn More below and build your Belly Melt Plan on FityWell. It's the app my mom used, and now she's recommending it to her friends.

This bitch was fat as hell not long ago. Then she found an app that's going viral on TikTok right now, and one month later? Look at her. She was stressed all day, barely sleeping, craving sugar all night. She did those generic workouts her gym trainer gave her. She stuffed herself with internet supplements promising miracles. She even took Ozempic just to lose weight. If you're a mom over forty, tired, stressed, doing everything right, and the scale still won't budge, your problem isn't a lack of willpower. Generic workouts and supplements from some random personal trainer aren't made for your body. What works for one woman won't work for another in most cases. The only thing that works is a plan made just for you. You put your info in the app, and it builds your Belly Melt Plan. Tap Learn More below and build your Belly Melt Plan on FityWell. It's the app my mom used, and now she's recommending it to her friends.
