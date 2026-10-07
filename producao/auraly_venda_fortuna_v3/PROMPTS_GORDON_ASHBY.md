# Gordon Ashby | Auraly Venda Fortuna v3 | Pacote de Prompts

pipeline: auraly

Vídeo modelo: `input/modelo.mp4` (102,2 s, careca abrindo o painel do rodapé com notas de $100)

Character sheet: `producao/_ancoras/character_sheets/gordon_ashby_character_sheet.jpg`

Funil: venda, dinheiro e fortuna. Selos + `222`, depois foto de perfil e Stories. Rodada de validação.

## Índice de geração

| Take | Keyframe | Anexar | Ação |
|---|---|---|---|
| T1 | K01 | CHARACTER SHEET GORDON ASHBY | GERAR DO ZERO |
| T2 a T14 | K02 | CHARACTER SHEET GORDON ASHBY | GERAR DO ZERO |

## Trava de identidade e continuidade

- Identidade: The exact fictional AI character Gordon Ashby, explicitly male: white American man aged about 68, slim and upright, full thick silver-white hair combed back, thin gold-rimmed round glasses, light blue-grey eyes with heavy lids, narrow face, long straight nose, deep forehead lines, crow's feet, sun spots on temples and cheeks, real aged skin, clean-shaven.
- Roupa (a do character sheet): Cream off-white tailored dinner jacket over a white dress shirt with a black silk bow tie, black dress trousers, black polished leather oxford shoes, a slim gold wristwatch on the left wrist and a plain gold ring on the left ring finger.
- Cenário (cozinha de mansão), gancho: The kitchen of a luxury mansion, the same layout as the model: custom white cabinetry with solid brass pulls, a huge Calacatta marble island end with bold grey veining and a squared waterfall edge on the left of the frame, large polished cream marble floor tiles, a marble backsplash at the top of the frame, and a small American flag in a brass holder on a counter far behind. The wooden toe-kick panel at the base of the white cabinet is tilted out of its slot.
- Cenário (cozinha de mansão), corpo: The kitchen of a luxury mansion, the same layout as the model: custom dark walnut cabinetry with solid brass pulls, a huge Calacatta marble island corner with bold grey veining on the left edge of the frame, a cream marble backsplash with a professional range hood behind, large polished cream marble floor tiles at the bottom of the frame, and a small American flag in a brass holder on the far counter.
- Luz: Neutral overcast daylight from a tall window on the right, the sky outside showing grey-blue cloud texture, never white or blown out, soft even light on the face and hands with no harsh shadows and no warm cast.
- Voz (mesmo timbre em todos os V): voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo, sotaque americano.
- Sem 2ª pessoa.

## Trava do prop herói

- Nota: a crisp US one-hundred-dollar bill, pale green-blue with a blue security ribbon, a portrait in the oval and a large gold-green 100 in the lower corner, about six inches long, with no readable serial number or text.
- Maços: tight stacks of US one-hundred-dollar bills, each stack held by a yellow paper band, piled in rows to the top of the cavity.

## Trava da 2ª pessoa (REF-A)

- Não se aplica: não há 2ª pessoa.

## Prompts de imagem

## K01 · T1 · GERAR DO ZERO · CHARACTER SHEET GORDON ASHBY

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ CHARACTER SHEET GORDON ASHBY** `producao/_ancoras/character_sheets/gordon_ashby_character_sheet.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: gancho mudo, painel do rodapé aberto com maços de notas de $100.

```json
{
  "shot_id": "K01_gordon_ashby",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached character sheet only for Gordon Ashby's exact identity (face, skin, hair, body), wardrobe and jewelry; ignore its grey studio background. The setting, camera angle, pose and action are fully described in this prompt.",
  "identity_main": "The exact fictional AI character Gordon Ashby, explicitly male: white American man aged about 68, slim and upright, full thick silver-white hair combed back, thin gold-rimmed round glasses, light blue-grey eyes with heavy lids, narrow face, long straight nose, deep forehead lines, crow's feet, sun spots on temples and cheeks, real aged skin, clean-shaven.",
  "wardrobe": "Cream off-white tailored dinner jacket over a white dress shirt with a black silk bow tie, black dress trousers, black polished leather oxford shoes, a slim gold wristwatch on the left wrist and a plain gold ring on the left ring finger.",
  "scene": "The kitchen of a luxury mansion, the same layout as the model: custom white cabinetry with solid brass pulls, a huge Calacatta marble island end with bold grey veining and a squared waterfall edge on the left of the frame, large polished cream marble floor tiles, a marble backsplash at the top of the frame, and a small American flag in a brass holder on a counter far behind. The wooden toe-kick panel at the base of the white cabinet is tilted out of its slot.",
  "prop": "The wooden toe-kick panel, about 30 inches wide and 5 inches tall, is tilted out of the base of the cabinet and held by Gordon Ashby's right hand at its lower edge. In the dark cavity behind it are tight stacks of US one-hundred-dollar bills, each stack held by a yellow paper band, piled in rows to the top of the cavity, clearly visible. Nothing else is in the cavity or in the hands.",
  "posture": "Gordon Ashby kneels on his right knee on the floor tiles beside the marble island end, his left arm stretched out and the left hand resting flat on the marble edge for balance, head lowered, looking down at the open cavity with a focused expression; his aged hands with a plain gold ring on the left ring finger and a slim gold wristwatch below the cream cuff.",
  "composition": "Gordon Ashby fills the frame from the top of the head, about 12 percent from the top edge, down to the floor at the bottom edge, placed in the right two thirds of the frame. The open cavity with the stacks of bills and the tilted panel take up about 30 percent of the frame in the lower left, about 28 inches from the lens, and are closer to the camera than his face. The marble edge runs along the left side. Nothing else is in frame. The background is reduced by framing, never by blur.",
  "camera": "phone camera at about knee height, 1x lens looking slightly down toward the cavity, handheld with a slight natural shake",
  "lighting": "Neutral overcast daylight from a tall window on the right, the sky outside showing grey-blue cloud texture, never white or blown out, soft even light on the face and hands with no harsh shadows and no warm cast.",
  "state": "Start frame: the panel has just been tilted out and Gordon Ashby's eyes are on the stacks of bills.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no numbers overlaid on the image, no glowing numbers, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no glowing aura, no sparkles, no light coming out of the money, no floating bills, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, no second person in frame, no face turned to the lens, no other props, no bills outside the cavity"
}
```

## K02 · T2 a T14 · GERAR DO ZERO · CHARACTER SHEET GORDON ASHBY

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ CHARACTER SHEET GORDON ASHBY** `producao/_ancoras/character_sheets/gordon_ashby_character_sheet.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: corpo, ajoelhado com o braço na quina de mármore e a nota de $100 na mão.

```json
{
  "shot_id": "K02_gordon_ashby",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached character sheet only for Gordon Ashby's exact identity (face, skin, hair, body), wardrobe and jewelry; ignore its grey studio background. The setting, camera angle, pose and action are fully described in this prompt.",
  "identity_main": "The exact fictional AI character Gordon Ashby, explicitly male: white American man aged about 68, slim and upright, full thick silver-white hair combed back, thin gold-rimmed round glasses, light blue-grey eyes with heavy lids, narrow face, long straight nose, deep forehead lines, crow's feet, sun spots on temples and cheeks, real aged skin, clean-shaven.",
  "wardrobe": "Cream off-white tailored dinner jacket over a white dress shirt with a black silk bow tie, black dress trousers, black polished leather oxford shoes, a slim gold wristwatch on the left wrist and a plain gold ring on the left ring finger.",
  "scene": "The kitchen of a luxury mansion, the same layout as the model: custom dark walnut cabinetry with solid brass pulls, a huge Calacatta marble island corner with bold grey veining on the left edge of the frame, a cream marble backsplash with a professional range hood behind, large polished cream marble floor tiles at the bottom of the frame, and a small American flag in a brass holder on the far counter.",
  "prop": "In his right hand, held low in the lower foreground at about 12 inches from the lens, Gordon Ashby holds a crisp US one-hundred-dollar bill, pale green-blue with a blue security ribbon, a portrait in the oval and a large gold-green 100 in the lower corner, about six inches long, with no readable serial number or text. Nothing else is held in either hand.",
  "posture": "Gordon Ashby kneels very near the lens on his right knee, leaning forward, his left forearm resting on the squared marble corner at the left of the frame with the hand hanging over the edge, head tilted slightly, looking straight into the lens, caught mid-sentence, lips naturally parted; his aged hands with a plain gold ring on the left ring finger and a slim gold wristwatch below the cream cuff.",
  "composition": "Gordon Ashby fills the frame from the top of the head, about 8 percent from the top edge, down to the thighs at the bottom edge, centered slightly right. The bill is held in the lower foreground left of center, tilted toward the lens, about 12 inches from the lens, closer to the camera than his face, and takes up about 8 percent of the frame. The marble corner runs down the left edge and the cabinets and backsplash fill the rest. Nothing else is in frame. The background is reduced by framing, never by blur.",
  "camera": "phone camera at about waist height of the kneeling person, roughly two feet above the floor, 1x lens tilted slightly up toward the face, fixed with a slight natural handheld shake",
  "lighting": "Neutral overcast daylight from a tall window on the right, the sky outside showing grey-blue cloud texture, never white or blown out, soft even light on the face and hands with no harsh shadows and no warm cast.",
  "state": "Start frame: Gordon Ashby is already looking into the lens, caught mid-sentence, the bill held low and tilted.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no numbers overlaid on the image, no glowing numbers, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no glowing aura, no sparkles, no light coming out of the money, no floating bills, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, no second person in frame, no second bill, no stack of bills in frame, no face covered by the hand"
}
```

# Prompts de vídeo

### V01 · T1 · usa K01

```text
(sem fala no take: gancho mudo, ninguém fala, sem voz)

o que acontece no vídeo: plano 1, Gordon Ashby ajoelhado inclina o painel de madeira do rodapé para o lado com a mão direita e o deixa cair no piso, e os maços de notas de $100 com cintas amarelas ficam à vista dentro do vão. Corte para plano 2, close do vão: a mão de Gordon Ashby tira uma nota de $100 do topo do maço e a levanta, com a nota e os dedos em foco no instante em que sai do maço. Corte para plano 3, Gordon Ashby de frente, em pé na cozinha, segurando a nota diante do peito e girando a nota para a lente, olhar sério.

câmera: cortes internos ao clipe, três planos, mão livre com leve tremor natural: plano 1 baixo, na altura do joelho; plano 2 em close, no vão do rodapé; plano 3 frontal na altura do peito

som ambiente: cozinha silenciosa, madeira raspando no piso, farfalhar de notas de papel, sem música
```

### V02 · T2 · usa K02

```text
o avatar Gordon Ashby (homem) fala em inglês com sotaque americano de Gordon Ashby, voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, baixo e confidencial, como quem conta um segredo, a seguinte frase: "If this video found you tonight, say nothing once it ends. Not a word to your family, not a word to your friends, not a word to anyone."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Gordon Ashby fala baixo e confidencial olhando para a lente, a nota de $100 parada na mão direita, o braço esquerdo apoiado na quina de mármore, e balança a cabeça de leve na última frase.

câmera: fixa, na altura da cintura de quem está ajoelhado, com leve tremor natural de celular

som ambiente: cozinha silenciosa, leve eco natural da voz, ruído suave de roupa, sem música
```

### V03 · T3 · usa K02

```text
o avatar Gordon Ashby (homem) fala em inglês com sotaque americano de Gordon Ashby, voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, sério e direto, quase sussurrando no começo, a seguinte frase: "Listen closely, because the biggest money change you will ever see is about to start, and it has been hiding closer to you than you think."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Gordon Ashby inclina a cabeça um pouco para a lente e ergue a nota de $100 alguns centímetros na última frase, o braço esquerdo apoiado na quina de mármore.

câmera: fixa, na altura da cintura de quem está ajoelhado, com leve tremor natural de celular

som ambiente: cozinha silenciosa, leve eco natural da voz, ruído suave de roupa, sem música
```

### V04 · T4 · usa K02

```text
o avatar Gordon Ashby (homem) fala em inglês com sotaque americano de Gordon Ashby, voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, firme, em tom de alerta, a seguinte frase: "Scroll past this and the same energy that was heading to your hands can turn around and drain what you already have."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Gordon Ashby fica sério e firme, olha direto para a lente e mexe a nota de $100 de leve na mão direita, o braço esquerdo apoiado na quina de mármore.

câmera: fixa, na altura da cintura de quem está ajoelhado, com leve tremor natural de celular

som ambiente: cozinha silenciosa, leve eco natural da voz, ruído suave de roupa, sem música
```

### V05 · T5 · usa K02

```text
o avatar Gordon Ashby (homem) fala em inglês com sotaque americano de Gordon Ashby, voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, calmo e certo, a seguinte frase: "Most people who find this video will never reach the end. Whoever you are, do not swipe up and do not swipe down."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Gordon Ashby olha firme para a lente, balança a cabeça de leve em negativa duas vezes nas palavras finais, a nota de $100 parada na mão direita.

câmera: fixa, na altura da cintura de quem está ajoelhado, com leve tremor natural de celular

som ambiente: cozinha silenciosa, leve eco natural da voz, ruído suave de roupa, sem música
```

### V06 · T6 · usa K02

```text
o avatar Gordon Ashby (homem) fala em inglês com sotaque americano de Gordon Ashby, voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, calmo e seguro, com pausa curta no começo, a seguinte frase: "Wealth and prosperity are walking into your home, and this message comes straight from Archangel Raphael, the angel who opens doors to abundance."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Gordon Ashby faz uma pausa curta, respira e fala com calma e certeza para a lente, a nota de $100 parada na mão direita, o braço esquerdo apoiado na quina de mármore.

câmera: fixa, na altura da cintura de quem está ajoelhado, com leve tremor natural de celular

som ambiente: cozinha silenciosa, leve eco natural da voz, ruído suave de roupa, sem música
```

### V07 · T7 · usa K02

```text
o avatar Gordon Ashby (homem) fala em inglês com sotaque americano de Gordon Ashby, voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, sério, como quem anuncia algo importante, a seguinte frase: "But he also brings a warning. Nothing in your finances stays the same after tonight. A powerful blessing is coming at you with incredible force."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Gordon Ashby fica solene, aponta a nota de $100 de leve em direção à lente na última frase, o braço esquerdo apoiado na quina de mármore.

câmera: fixa, na altura da cintura de quem está ajoelhado, com leve tremor natural de celular

som ambiente: cozinha silenciosa, leve eco natural da voz, ruído suave de roupa, sem música
```

### V08 · T8 · usa K02

```text
o avatar Gordon Ashby (homem) fala em inglês com sotaque americano de Gordon Ashby, voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, firme e em tom de alerta, a seguinte frase: "Confirm this message is yours, but keep watching, because that same energy can turn against you before it ever reaches you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Gordon Ashby olha para a lente em tom de alerta, inclina o corpo um pouco para a frente, a nota de $100 parada na mão direita.

câmera: fixa, na altura da cintura de quem está ajoelhado, com leve tremor natural de celular

som ambiente: cozinha silenciosa, leve eco natural da voz, ruído suave de roupa, sem música
```

### V09 · T9 · usa K02

```text
o avatar Gordon Ashby (homem) fala em inglês com sotaque americano de Gordon Ashby, voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, firme e convicto, a seguinte frase: "This is the last message the universe is sending you about this, so take it seriously and do exactly what I say next."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Gordon Ashby fecha os olhos por um instante e volta a olhar para a lente com firmeza, a nota de $100 parada na mão direita.

câmera: fixa, na altura da cintura de quem está ajoelhado, com leve tremor natural de celular

som ambiente: cozinha silenciosa, leve eco natural da voz, ruído suave de roupa, sem música
```

### V10 · T10 · usa K02

```text
o avatar Gordon Ashby (homem) fala em inglês com sotaque americano de Gordon Ashby, voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, firme e solene em cada selo, a seguinte frase: "Tap the heart. That is your first seal, and it makes the blessing coming to you stronger. Now save this post. That is your second seal."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Gordon Ashby faz um aceno firme com a cabeça em cada selo, a nota de $100 parada na mão direita, o braço esquerdo apoiado na quina de mármore.

câmera: fixa, na altura da cintura de quem está ajoelhado, com leve tremor natural de celular

som ambiente: cozinha silenciosa, leve eco natural da voz, ruído suave de roupa, sem música
```

### V11 · T11 · usa K02

```text
o avatar Gordon Ashby (homem) fala em inglês com sotaque americano de Gordon Ashby, voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, firme e muito sério, a seguinte frase: "Now send this video to yourself. That is your third seal. Then comment 222 so this money gets tied to your name and nobody else's."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Gordon Ashby aponta a nota de $100 para a lente na palavra final, olhar sério, o braço esquerdo apoiado na quina de mármore.

câmera: fixa, na altura da cintura de quem está ajoelhado, com leve tremor natural de celular

som ambiente: cozinha silenciosa, leve eco natural da voz, ruído suave de roupa, sem música
```

### V12 · T12 · usa K02

```text
o avatar Gordon Ashby (homem) fala em inglês com sotaque americano de Gordon Ashby, voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, grave e solene, em tom de aviso, a seguinte frase: "Skip even one seal and the panel stays sealed. The money stays hidden inside your own walls, out of your reach."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Gordon Ashby fica grave e solene, sem sorrir, inclina o corpo um pouco para a lente e segura a nota de $100 firme na mão direita.

câmera: fixa, na altura da cintura de quem está ajoelhado, com leve tremor natural de celular

som ambiente: cozinha silenciosa, leve eco natural da voz, ruído suave de roupa, sem música
```

### V13 · T13 · usa K02

```text
o avatar Gordon Ashby (homem) fala em inglês com sotaque americano de Gordon Ashby, voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, calmo e certo, a seguinte frase: "By tomorrow morning, check your phone and your mailbox. News about money is headed your way, and the universe never forgets a sealed message."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Gordon Ashby olha para a lente com certeza tranquila e balança a cabeça de leve uma vez ao fim da frase, a nota de $100 parada na mão direita.

câmera: fixa, na altura da cintura de quem está ajoelhado, com leve tremor natural de celular

som ambiente: cozinha silenciosa, leve eco natural da voz, ruído suave de roupa, sem música
```

### V14 · T14 · usa K02

```text
o avatar Gordon Ashby (homem) fala em inglês com sotaque americano de Gordon Ashby, voz masculina baixa, calma e pausada, de homem de sessenta e oito anos com autoridade tranquila de dinheiro antigo, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, próximo e urgente, olhando direto para a lente, a seguinte frase: "Now tap my profile picture and open my stories, because what comes next is waiting there. Do it now, before it disappears."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Gordon Ashby se inclina um pouco para a lente e aponta a nota de $100 para baixo e para a lente na palavra final, olhar direto.

câmera: fixa, na altura da cintura de quem está ajoelhado, com leve tremor natural de celular

som ambiente: cozinha silenciosa, leve eco natural da voz, ruído suave de roupa, sem música
```

## Montagem no CapCut

1. Clipes numerados na ordem: V01 a V14.
2. V01 (gancho mudo): usar ~5,4 s, do painel caindo até a nota girando para a lente. Tarja fixa no topo, branca com contorno escuro: "If you need urgent and unexpected money:". Flash curto de transição para o V02.
3. V02 a V14: jump cut a cada take, todos saem do mesmo frame, então o enquadramento não muda, como no modelo. Cortar logo depois da última palavra. Isolate Voice / Keep Vocal no áudio.
4. Legenda karaokê branca, palavra atual em amarelo, no centro do quadro, do V02 ao V14.
5. Números `444` com emoji de dinheiro no canto superior esquerdo e `11:11` no canto superior direito, só no CapCut, do V02 ao V14. Emojis (coração, olho, saco de dinheiro) sobre a nota no V03, como no modelo. Nunca dentro do K.
6. Sem Voice Changer: a voz vem do prompt de cada V. Música só a partir do V02, baixa, fora da biblioteca do TikTok.
7. Rótulo pequeno `AI-generated` num canto do vídeo.

