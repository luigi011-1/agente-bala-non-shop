# Devon Price | Auraly Venda Cofre Cama (growth) | Pacote de Prompts

pipeline: auraly

Vídeo modelo: `producao/auraly_venda_cofre_cama/input/modelo.mp4` (87,7 s, avatar IA)

Character sheet: `producao/_ancoras/character_sheets/devon_price_character_sheet.jpg`

Funil: growth, `222` no T5 + like + save + envio + follow. Rodada de validação, cenário e ângulo do modelo.

## Índice de geração

| Take | Keyframe | Anexar | Ação |
|---|---|---|---|
| T1 | K01 | CHARACTER SHEET DEVON PRICE + FRAME DO MODELO (K01) | GERAR DO ZERO |
| T2 | K02 | CHARACTER SHEET DEVON PRICE + FRAME DO MODELO (K02) | GERAR DO ZERO |
| T3 a T11 | K03 | CHARACTER SHEET DEVON PRICE + FRAME DO MODELO (K03) | GERAR DO ZERO |

## Trava de identidade e continuidade

- Identidade (character sheet): The exact fictional AI character Devon Price: white American woman around fifty-two, closely shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, fine lines and no makeup.
- Roupa (character sheet, descalço como no modelo): Light-wash denim shirt worn open with the cuffs rolled over a fitted black crew-neck T-shirt, dark blue jeans, barefoot, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar.
- Cenário (do vídeo modelo), quarto: The ordinary American master bedroom of the reference video: a charcoal-grey upholstered storage bed with a tufted headboard, made with a light grey-white duvet, a dark wooden nightstand on each side of the bed with a table lamp switched off, cream-beige walls and wall-to-wall beige carpet. On the right nightstand, next to the lamp, a small American flag (discreet but visible and in focus) stands in a small glass.
- Cenário, escada: The hidden cellar shaft of the reference video, seen from the bedroom above: a narrow wooden staircase of plain plank treads going down between rough brown earth walls held by dark wooden beams, with a bare white bulb hanging below and, at the top, the underside of the lifted grey bed platform with its wooden slats. On a wooden beam beside the stairs, a small American flag (discreet but visible and in focus) is pinned.
- Cenário, cofre: The underground cellar vault of the reference video: rough brown earth walls, dark wooden posts and ceiling beams, a string of bare white bulbs hanging overhead, and behind the person plain wooden shelves holding stacks of hundred-dollar bills. On the wooden post at the left, a small American flag (discreet but visible and in focus) is pinned.
- Luz do quarto: Neutral overcast daylight coming in from a window just out of frame on the left, cool and even, the bedside lamps switched off, soft even light on the face and body with no harsh shadows.
- Luz do cofre: Neutral cool white light as flat and even as overcast daylight, from the bare bulbs overhead and from the open hatch above, no orange or amber glow on the walls or the skin, soft even light on the face with no harsh shadows.
- Voz (mesmo timbre em todos os V): voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, sotaque americano de Chicago.
- Sem 2ª pessoa.

## Trava do prop herói

- A cama: charcoal-grey upholstered storage bed with a tufted headboard.
- O maço: a stack of hundred-dollar bills, thick, held together by an orange-tan paper strap around the middle, the top bill showing a portrait and the number 100.

## Trava da 2ª pessoa (REF-A)

- Não se aplica: não há 2ª pessoa.

## Prompts de imagem

## K01 · T1 · GERAR DO ZERO · CHARACTER SHEET DEVON PRICE + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ CHARACTER SHEET DEVON PRICE** `producao/_ancoras/character_sheets/devon_price_character_sheet.jpg`
> **2️⃣ FRAME DO MODELO, cenário e ângulo** `input/frames_modelo/K01_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: gancho mudo, a cama de baú estofada colada na lente e o avatar prestes a levantá-la.

```json
{
  "shot_id": "K01_devon_price",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image (character sheet) only for Devon Price's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.",
  "identity_main": "The exact fictional AI character Devon Price: white American woman around fifty-two, closely shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, fine lines and no makeup.",
  "wardrobe": "Light-wash denim shirt worn open with the cuffs rolled over a fitted black crew-neck T-shirt, dark blue jeans, barefoot, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar.",
  "scene": "The ordinary American master bedroom of the reference video: a charcoal-grey upholstered storage bed with a tufted headboard, made with a light grey-white duvet, a dark wooden nightstand on each side of the bed with a table lamp switched off, cream-beige walls and wall-to-wall beige carpet. On the right nightstand, next to the lamp, a small American flag (discreet but visible and in focus) stands in a small glass.",
  "prop": "The only object is the charcoal-grey upholstered storage bed, closed and made, with nothing visible underneath it. Devon Price rests one of her freckled fair hands with bare fingers on the edge of the duvet; the other hand hangs at her side.",
  "posture": "Devon Price stands upright beside the bed on the right side, one hand resting on the edge of the duvet, looking at the lens, mouth closed, about to lift the bed.",
  "composition": "The charcoal-grey upholstered storage bed with its tufted headboard is very close to the lens in the lower left foreground, about 40 percent of the frame, its near corner about 30 inches from the lens, closer to the camera than her face, nothing else competing with it. Devon Price is framed from the top of the head to the feet. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone fixed on a tripod about four feet above the carpet, about eight feet from the bed, 1x lens, pointing level, fixed",
  "lighting": "Neutral overcast daylight coming in from a window just out of frame on the left, cool and even, the bedside lamps switched off, soft even light on the face and body with no harsh shadows.",
  "state": "Start frame: Devon Price stands with one hand on the duvet, the bed still closed, mouth closed.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no glowing objects, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no tarot cards, no candles, no open hatch, no staircase yet, no money, no shoes, no socks"
}
```

## K02 · T2 · GERAR DO ZERO · CHARACTER SHEET DEVON PRICE + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ CHARACTER SHEET DEVON PRICE** `producao/_ancoras/character_sheets/devon_price_character_sheet.jpg`
> **2️⃣ FRAME DO MODELO, cenário e ângulo** `input/frames_modelo/K02_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: descida, a escada de tábuas escondida vista de costas entre paredes de terra.

```json
{
  "shot_id": "K02_devon_price",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image (character sheet) only for Devon Price's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.",
  "identity_main": "The exact fictional AI character Devon Price: white American woman around fifty-two, closely shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, fine lines and no makeup.",
  "wardrobe": "Light-wash denim shirt worn open with the cuffs rolled over a fitted black crew-neck T-shirt, dark blue jeans, barefoot, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar.",
  "scene": "The hidden cellar shaft of the reference video, seen from the bedroom above: a narrow wooden staircase of plain plank treads going down between rough brown earth walls held by dark wooden beams, with a bare white bulb hanging below and, at the top, the underside of the lifted grey bed platform with its wooden slats. On a wooden beam beside the stairs, a small American flag (discreet but visible and in focus) is pinned.",
  "prop": "The only object is the narrow wooden staircase going down between rough brown earth walls into the cellar shaft. Devon Price is already on it, seen from behind, one of her freckled fair hands with bare fingers on the wooden beam beside the stairs.",
  "posture": "Devon Price descends the staircase with her back to the lens, one foot already on a lower tread, the other hand reaching back toward the lifted bed platform, her head slightly turned down the stairs.",
  "composition": "The narrow wooden staircase fills the lower half of the frame, about 50 percent of the frame, its top tread about 24 inches from the lens, closer to the camera than her back, nothing else competing with it. Devon Price is framed from the top of the head to the hips, from behind. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone held above and behind the person at the top of the stairs, about five feet above the carpet, 1x lens, pointing down the staircase, fixed",
  "lighting": "Neutral overcast daylight coming in from a window just out of frame on the left, cool and even, the bedside lamps switched off, soft even light on the face and body with no harsh shadows.",
  "state": "Start frame: Devon Price one step down the stairs, seen from behind, mid-stride.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no glowing objects, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no tarot cards, no candles, no money yet, no face visible, no shoes, no socks, no smoke"
}
```

## K03 · T3 a T11 · GERAR DO ZERO · CHARACTER SHEET DEVON PRICE + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ CHARACTER SHEET DEVON PRICE** `producao/_ancoras/character_sheets/devon_price_character_sheet.jpg`
> **2️⃣ FRAME DO MODELO, cenário e ângulo** `input/frames_modelo/K03_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: corpo, o avatar de pé no cofre segurando um maço de notas de 100 dólares na lente.

```json
{
  "shot_id": "K03_devon_price",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image (character sheet) only for Devon Price's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.",
  "identity_main": "The exact fictional AI character Devon Price: white American woman around fifty-two, closely shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, fine lines and no makeup.",
  "wardrobe": "Light-wash denim shirt worn open with the cuffs rolled over a fitted black crew-neck T-shirt, dark blue jeans, barefoot, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar.",
  "scene": "The underground cellar vault of the reference video: rough brown earth walls, dark wooden posts and ceiling beams, a string of bare white bulbs hanging overhead, and behind the person plain wooden shelves holding stacks of hundred-dollar bills. On the wooden post at the left, a small American flag (discreet but visible and in focus) is pinned.",
  "prop": "The only object is a stack of hundred-dollar bills, thick, held together by an orange-tan paper strap around the middle, the top bill showing a portrait and the number 100, held up in one of her freckled fair hands with bare fingers toward the lens at chest height; the other hand hangs at her side.",
  "posture": "Devon Price stands inside the cellar vault facing the lens, holding the stack of bills up at chest height on the left of the frame, looking straight into the lens.",
  "composition": "The stack of hundred-dollar bills is very close to the lens in the lower left of the frame, about 15 percent of the frame, about 16 inches from the lens, closer to the camera than her face, nothing else competing with it. Devon Price is framed from the top of the head to the waist, her face in the upper half. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone fixed on a small stand about five feet above the floor of the vault, about three feet from the person, 1x lens, pointing level, fixed",
  "lighting": "Neutral cool white light as flat and even as overcast daylight, from the bare bulbs overhead and from the open hatch above, no orange or amber glow on the walls or the skin, soft even light on the face with no harsh shadows.",
  "state": "Start frame: Devon Price caught mid-sentence, lips naturally parted, serious expression, the stack held still.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no glowing objects, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no tarot cards, no candles, no money on the floor, no bills in the other hand, no shoes, no socks"
}
```

# Prompts de vídeo

### V01 · T1 · usa K01

```text
(sem fala no take: gancho mudo, a avatar fica em silêncio o clipe inteiro, boca fechada)

o que acontece no vídeo: Devon Price aperta a borda do colchão com as duas mãos e levanta a plataforma da cama de baú, que sobe devagar com um pistão e abre por baixo um poço retangular com uma escada de tábuas e uma lâmpada acesa lá no fundo; Devon Price segura a plataforma erguida com uma mão, olha para a lente e passa uma perna para dentro do poço.

câmera: fixa, sem movimento, um plano só, sem cortes

som ambiente: quarto silencioso, o pistão da cama subindo e o ranger leve da madeira, sem música
```

### V02 · T2 · usa K02

```text
(sem fala no take: a avatar fica em silêncio o clipe inteiro, boca fechada)

o que acontece no vídeo: plano 1, Devon Price de costas desce a escada de tábuas entre as paredes de terra; corte seco para o plano 2, o cofre subterrâneo aberto, Devon Price de costas no pé da escada com uma mão na parede, com prateleiras de madeira cheias de pilhas de notas de 100 dólares e um fio de lâmpadas brancas; corte seco para o plano 3, macro das pilhas de notas de 100 dólares com cinta de papel laranja, colado na lente; corte seco para o plano 4, de costas, a mão de Devon Price pega um maço da prateleira e Devon Price se vira para a lente segurando o maço no peito.

câmera: fixa, com três cortes secos internos ao clipe, sem movimento

som ambiente: passos na madeira, o eco leve do cofre e o papel das notas, sem música
```

### V03 · T3 · usa K03

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, baixa, séria e conspiratória, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If you are watching this video today, stay silent after you watch it. No matter what happens, keep this to yourself."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price fala olhando fixo para a lente, com um pequeno aceno de cabeça. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V04 · T4 · usa K03

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, convicta e intensa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Not your sister, not your best friend, not a single soul. Listen closely, because the most transformative day of your life is about to begin."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price balança a cabeça devagar, olhando fixo para a lente. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V05 · T5 · usa K03

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, urgente e direta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Right now, comment 222 on this video, so the blessing knows where to find you. But if you keep scrolling, it could slip right through your fingers."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price aponta para baixo com a mão livre, para os comentários, e depois para a lente. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V06 · T6 · usa K03

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme e reveladora, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Not everyone will see this before the week is over. I can't tell who you are, but I see wealth and prosperity coming into your life."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price fala olhando para a lente, com pequenos gestos naturais da mão livre. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V07 · T7 · usa K03

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, solene e intensa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "This message comes directly from Saint Michael, and it also calls for action. Something is shifting in your favor. A powerful blessing is heading your way with incredible force."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price fala olhando para a lente, com pequenos gestos naturais da mão livre. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V08 · T8 · usa K03

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, séria, em tom de aviso, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Acknowledge that this message is for you. But don't stop watching, or the news could pass you by. One last word from the universe, so take it seriously."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price ergue o dedo indicador da mão livre, como quem pede atenção. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V09 · T9 · usa K03

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, rápida e prática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Tap like on this video, then save it, then send it to yourself. Each one locks this blessing in a little tighter."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price conta nos dedos da mão livre, um, dois, três, enquanto fala. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V10 · T10 · usa K03

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, calma e confiante, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Do all three, and tomorrow, when you wake up, check your phone. You will receive good news."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price fala devagar, com um pequeno aceno de cabeça. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V11 · T11 · usa K03

```text
a avatar Devon Price, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, próxima e urgente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Now pay attention. Follow me before this disappears, because the next part of this message is already on its way to you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Devon Price se inclina um pouco para a lente e aponta para ela com a mão livre. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

## Montagem no CapCut

1. Clipes numerados na ordem: V01 a V11.
2. V01 e V02 (gancho mudo): usar ~5,2 s do V01 e ~4,3 s do V02, emendados no corte da descida, como o modelo (~9,5 s no total). Texto no topo, duas linhas: "I see wealth coming into your life." / "Not a single soul.".
3. V03 a V11: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / Keep Vocal. Todos saem do mesmo frame (K03), então a troca de clipe fica no mesmo enquadramento, como no modelo.
4. Do V03 ao V11, legenda karaokê branca com a palavra falada em amarelo, no meio do quadro, como o modelo.
5. No V11, seta vermelha para baixo no canto inferior esquerdo. Sem seta para a foto de perfil: o CTA é follow.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Som ambiente baixo no V01 e no V02 (pistão, passos); sem música por baixo da fala.
8. Rótulo pequeno `AI-generated` num canto do vídeo.

