# Devon Price | Auraly Taylon Branigan (sal na carteira) | Pacote de Prompts

pipeline: auraly

Vídeo modelo: `producao/auraly_taylon_branigan/input/taylon_branigan.mp4` (87 s, avatar IA)

Character sheet: `producao/_ancoras/character_sheets/devon_price_character_sheet.jpg`

Funil: growth, 222 antes da metade + save + double tap + follow. Rodada de validação, cenário e ângulo do modelo.

## Índice de geração

| Take | Keyframe | Anexar | Ação |
|---|---|---|---|
| T1 | K01 | CHARACTER SHEET DEVON PRICE + FRAME DO MODELO (K01) | GERAR DO ZERO |
| T2 a T18 | K02 | CHARACTER SHEET DEVON PRICE + FRAME DO MODELO (K02) | GERAR DO ZERO |

## Trava de identidade e continuidade

- Identidade (character sheet): The exact fictional AI character Devon Price: white American woman around fifty-two, closely shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, fine lines and no makeup.
- Roupa (character sheet): Light-wash denim shirt worn open with the cuffs rolled over a fitted black crew-neck T-shirt, dark blue jeans, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar.
- Cenário do gancho (do vídeo modelo): The front porch of an ordinary American suburban house seen from just above a sturdy wooden bench with visible grain that fills the bottom of the frame: a white painted porch column in the middle behind the hands, a dark wood door frame and a stained wooden front door with a glass pane at the right edge, a woven doormat on the porch floor, a white flowering shrub in a dark pot at the left, and green garden shrubs and flagstone paving behind. A small American flag is tucked into the shrubs at the left, discreet but visible and in focus.
- Cenário do corpo (do vídeo modelo): The open front doorway of an ordinary American house seen from the porch: the avatar sits on the wooden threshold of the open front door, the dark wood door jamb at the left with green ivy climbing the white porch column at the far left, the open stained-wood front door at the right edge with a black iron lever handle, and behind the avatar through the doorway a living room with a window showing green trees outside and a table lamp switched off beside it, a framed map of the United States on the cream wall at the upper right above a wooden bookshelf full of books, and below the threshold a gray stone step and a woven doormat. A small American flag is tucked into the ivy on the column at the left, discreet but visible and in focus.
- Luz: Neutral overcast daylight outdoors, cool and even, soft light on the hands and the wallet, no harsh shadows and no dappled sun patches on the bench. / Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.
- Voz (mesmo timbre em todos os V): voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, sotaque americano de Chicago.
- Sem 2ª pessoa.

## Trava do prop herói

- O saleiro: a navy blue cylindrical salt shaker with a plain white perforated lid and no label.
- A carteira: a brown leather bifold wallet, plain, no logo, open with its card slots and inner pocket visible.

## Trava da 2ª pessoa (REF-A)

- Não se aplica: não há 2ª pessoa.

## Prompts de imagem

## K01 · T1 · GERAR DO ZERO · CHARACTER SHEET DEVON PRICE + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ CHARACTER SHEET DEVON PRICE** `producao/_ancoras/character_sheets/devon_price_character_sheet.jpg`
> **2️⃣ FRAME DO MODELO, cenário e ângulo** `input/frames_modelo/K01_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: gancho, saleiro despejando sal na carteira aberta, macro das mãos na varanda.

```json
{
  "shot_id": "K01_devon_price",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image (character sheet) only for Devon Price's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.",
  "identity_main": "The exact fictional AI character Devon Price: white American woman around fifty-two, closely shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, fine lines and no makeup. Only the hands and forearms appear in this shot.",
  "wardrobe": "Light-wash denim shirt worn open with the cuffs rolled over a fitted black crew-neck T-shirt, dark blue jeans, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar.",
  "scene": "The front porch of an ordinary American suburban house seen from just above a sturdy wooden bench with visible grain that fills the bottom of the frame: a white painted porch column in the middle behind the hands, a dark wood door frame and a stained wooden front door with a glass pane at the right edge, a woven doormat on the porch floor, a white flowering shrub in a dark pot at the left, and green garden shrubs and flagstone paving behind. A small American flag is tucked into the shrubs at the left, discreet but visible and in focus.",
  "prop": "In one of her freckled fair hands with bare fingers, the cuffs of a light-wash denim shirt rolled on the forearms, a navy blue cylindrical salt shaker with a plain white perforated lid and no label is tipped, a thin stream of coarse white salt pouring from its lid into a brown leather bifold wallet, plain, no logo, open with its card slots and inner pocket visible, which the other hand holds open from the right edge of the frame, thumb on the wallet's edge, a small pile of salt already at the bottom of the wallet.",
  "posture": "Only Devon Price's hands and forearms are in the frame, entering from the right edge: one hand tips the shaker from the upper left, the other holds the wallet open in the lower middle. No face is visible.",
  "composition": "Macro of the hands. The wallet is in the lower middle of the frame, very close to the lens, about 12 inches from the lens, taking up about 10 percent of the frame; the navy shaker is in the upper left, about 10 inches from the lens, about 8 percent of the frame, the salt stream falling between them; both are the hero, large in frame, nothing else competing with them. The bench fills the bottom of the frame. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "handheld phone at upper-chest height about 14 inches from the hands, 1x lens, tilted downward about 35 degrees, steady",
  "lighting": "Neutral overcast daylight outdoors, cool and even, soft light on the hands and the wallet, no harsh shadows and no dappled sun patches on the bench.",
  "state": "Start frame: the salt is already pouring in a thin stream from the shaker into the open wallet.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no brand name or logo on the shaker or the wallet, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no sun flares, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no tarot cards, no candles, no magic effects, no face, no second person, no salt spilled on the bench"
}
```

## K02 · T2 a T18 · GERAR DO ZERO · CHARACTER SHEET DEVON PRICE + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ CHARACTER SHEET DEVON PRICE** `producao/_ancoras/character_sheets/devon_price_character_sheet.jpg`
> **2️⃣ FRAME DO MODELO, cenário e ângulo** `input/frames_modelo/K02_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: corpo, sentado na soleira da porta aberta com a carteira nas mãos.

```json
{
  "shot_id": "K02_devon_price",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image (character sheet) only for Devon Price's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.",
  "identity_main": "The exact fictional AI character Devon Price: white American woman around fifty-two, closely shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, fine lines and no makeup.",
  "wardrobe": "Light-wash denim shirt worn open with the cuffs rolled over a fitted black crew-neck T-shirt, dark blue jeans, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar.",
  "scene": "The open front doorway of an ordinary American house seen from the porch: the avatar sits on the wooden threshold of the open front door, the dark wood door jamb at the left with green ivy climbing the white porch column at the far left, the open stained-wood front door at the right edge with a black iron lever handle, and behind the avatar through the doorway a living room with a window showing green trees outside and a table lamp switched off beside it, a framed map of the United States on the cream wall at the upper right above a wooden bookshelf full of books, and below the threshold a gray stone step and a woven doormat. A small American flag is tucked into the ivy on the column at the left, discreet but visible and in focus.",
  "prop": "Devon Price holds a brown leather bifold wallet, plain, no logo, open with its card slots and inner pocket visible, empty, open in both hands at belly height, held forward toward the lens. A navy blue cylindrical salt shaker with a plain white perforated lid and no label stands upright on the wooden threshold at the lower left.",
  "posture": "Devon Price sits on the wooden threshold of the open front door, leaning slightly forward with the elbows near the knees, holding the open wallet in both hands, looking straight into the lens.",
  "composition": "The open wallet is in the lower middle of the frame, about 30 inches from the lens, taking up about 4 percent of the frame, closer to the camera than her face, nothing else competing with it; the navy salt shaker stands at the lower left. Devon Price is framed from the top of the head to mid-thigh, her face in the upper third. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone resting at chest height about 3.5 feet off the porch floor and about four feet from the doorway, 1x lens, level, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "state": "Start frame: Devon Price caught mid-sentence, lips naturally parted, serious intrigued expression, wallet held open.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no brand name or logo on the shaker or the wallet, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no sun flares, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no tarot cards, no candles, no magic effects, no salt on the wallet yet, no salt on the floor"
}
```

# Prompts de vídeo

### V01 · T1 · usa K01

```text
narração em off: a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, tom baixo e confidencial, como quem conta um segredo, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Put salt inside your wallet before you leave the house." Ninguém aparece falando em quadro, só as mãos.

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Sem lip sync: a fala é narração em off e nenhum rosto aparece no quadro.

o que acontece no vídeo: plano único contínuo, já em andamento: a mão de Devon Price inclina o saleiro azul-escuro e o sal grosso cai em fio dentro da carteira marrom aberta, segurada pela outra mão; o fio de sal diminui e para perto do fim, deixando um montinho de sal no fundo da carteira, e as duas mãos ficam paradas até o fim.

câmera: plano único, sem cortes, câmera parada na altura do peito olhando para baixo

som ambiente: varanda residencial silenciosa, som do sal grosso caindo na carteira, sem música
```

### V02 · T2 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, séria e intrigante, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I know it sounds ridiculous, but you'll thank me for the rest of your life."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V03 · T3 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, convicta e intensa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Keep your mouth shut after you watch this. Do not tell anyone. Not everyone is going to see this before this month ends."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V04 · T4 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, urgente e direta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I do not know your name, but do not scroll. Because if this reached you today, it reached you as a final warning."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price aponta para a lente com a mão livre. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V05 · T5 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, solene e firme, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "A powerful wave of prosperity, love and money is heading your way. Don't tell anyone, but the abundance portal has opened."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V06 · T6 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, aliviada e firme, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The worst is finally over. I see a lot of money, prosperity and someone incredibly wonderful walking into your life."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price abre a mão livre com a palma para cima, aliviada. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V07 · T7 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, direta e urgente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Type 222 in the comments right now, that's how this gets tied to your name. Then stay with me until the end."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price aponta para baixo, para os comentários, e depois para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V08 · T8 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, intensa e solene, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Before you scroll, close your right hand and listen until the end. This video isn't for everyone. The universe chose you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price fecha a mão livre devagar em punho, mantém e solta. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V09 · T9 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, séria, em tom de aviso, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If you skip right now, the energy breaks. I feel something very unusual happening to you right now."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price balança a mão livre de um lado para o outro, como quem manda parar. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V10 · T10 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, intensa e baixa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I see the chains that were keeping you trapped in scarcity being broken."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V11 · T11 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, calorosa e firme, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The love that was being held back from you is finally coming straight to you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V12 · T12 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, séria e urgente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "In the next seven minutes, the energy of scarcity that was following you is going to be destroyed forever."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V13 · T13 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, rápida e prática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "So send this video to yourself right now, because in seven minutes you're going to come back to confirm the energetic shift for yourself."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V14 · T14 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme e confiante, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Now open your hand and save this video. That will be your first seal."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price abre a mão livre para a lente, com a palma aberta. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V15 · T15 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, rápida e prática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Double tap quickly on your screen. That will be your second seal. And if you haven't typed 222 yet, do it now so I can see you did everything."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price toca o ar duas vezes com o dedo indicador, como quem toca a tela, e aponta para baixo, para os comentários. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V16 · T16 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, calorosa e animada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If you did everything right, tomorrow at 11:11 a.m. you're going to receive some incredibly good news. But pay close attention."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V17 · T17 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, séria e baixa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "This energy is highly sensitive, and other people's envy can completely break it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price fala mais baixo, com o dedo indicador erguido. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V18 · T18 · usa K02

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, próxima e urgente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "So follow me right now, so this stays open, because the second part of this sign is coming to you next."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Devon Price aponta para a lente com a mão livre. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

## Montagem no CapCut

1. Clipes numerados na ordem: V01 a V18.
2. V01 (gancho, voz-over): usar só os primeiros ~3,1 s, com a narração inteira; deixar o fim da frase ("the house") vazar meio segundo sobre o começo do V02.
3. Entre V01 e V02, corte seco, sem flash (o modelo corta seco aos 3,12 s).
4. V02 a V18: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / Keep Vocal. Todos saem do mesmo frame (K02), então a troca de clipe fica no mesmo enquadramento, como no plano único do modelo.
5. Legenda karaokê em caixa alta, palavra atual em amarelo ou vermelho, no meio-baixo do quadro, do V01 ao V18.
6. O pedido de 222 está no V07 (antes da metade); o lembrete no V15. Sem seta para a foto de perfil: o CTA do fim é follow.
7. Sem Voice Changer: a voz vem do prompt de cada V.
8. Música só depois do gancho (a partir do V02), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
9. Rótulo pequeno `AI-generated` num canto do vídeo.

