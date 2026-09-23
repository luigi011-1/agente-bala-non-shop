# Melody Carter | Ângulo 1 (Korella Saffron) | Pacote de Prompts

Vídeo modelo: `Joseph&Coco_Comment _BIG_ and I will_2004575490207097_1080p_20260822.mp4`

Âncora de identidade: `C:\Users\luigi\Desktop\AVATARES NON-SHOP\melody carter .png`

Referência de produto: `C:\Users\luigi\Desktop\B-ROLL PRODUTOS\product.png`

Funil: comment `yes` -> DM -> deep link Amazon

> ⚠️ **MELODY É HOMEM.** Escrever `The EXACT man / male adult` em todo `identity_main`.
>
> ⚠️ **AQUI ELE FICA SENTADO, e isso é de propósito.** A regra padrão manda corrigir a pose sentada da foto-âncora, mas o original tem o pitchman sentado à mesa e é o que dá o registro de autoridade. O que se corrige é a **postura**: sentado ereto e inclinado pra frente, nunca o encosto relaxado da foto.
>
> ⚠️ **O Melody NÃO aparece na varanda.** A parte 1 é só com os dois figurantes (REF-A e REF-B).

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| ref | REF-A | GERAR DO ZERO o homem idoso (~73). Aprovar rosto antes do K01. |
| ref | REF-B | GERAR DO ZERO a mulher jovem (~28). Aprovar rosto antes do K01. |
| T1 | K01 | GERAR DO ZERO (ref: REF-A + REF-B). **Frame herói.** Pro, com variações. |
| T2 a T6 | K02 | GERAR DO ZERO (ref: REF-A + REF-B). Plano lateral próximo. |
| T7 a T24 | K03 | GERAR DO ZERO (ref: âncora Melody). Sentado à bancada, sem prop. |
| T25 a T31 | K04 | GERAR DO ZERO (ref: âncora Melody + product.png). Frasco na mão. Pro. |

Total: 2 referências + 4 keyframes para 31 takes.

---

## Trava de identidade e continuidade

**Escrita aqui uma vez, não repetir inteira dentro de cada JSON.**

**Melody (K03 e K04):**
- Rosto do Melody, **homem** negro, cavanhaque e barba aparada, musculoso.
- Longas tranças box braids escuras caindo na frente dos ombros.
- Tatuagem ornamental de manga no braço direito, pequenas tatuagens no peito.
- Regata branca canelada. **Corrente fina de PRATA com cruz de PRATA. Nunca ouro.**
- **Sentado ereto à bancada**, inclinado levemente pra frente. Nunca encostado e relaxado.
- Garagem dele, com **duas âncoras visuais apenas**: o neon vermelho e a bandeira vintage dos EUA. **Nunca inventariar o fundo.**
- Luz quente e baixa de garagem à noite. Zero blur, tudo nítido. Cara de iPhone, nunca polimento de IA.

**Varanda (K01 e K02):**
- Varanda de casa americana de subúrbio, corrimão branco, cadeira de vime.
- Mesma hora do dia e mesma luz nos dois keyframes.
- **O K01 é o único plano largo do vídeo. Ver a seção do gate abaixo.**

## Trava do produto (usar no K04)

```text
A white supplement bottle with a purple and white label, about 10 cm tall, held upright in his hand with the label facing the camera. The bottle keeps the exact same size, proportions and label layout as the attached product reference image.
```

## Trava da 2ª pessoa · REF-A · o homem idoso · gerar e aprovar ANTES do K01

```text
IMPORTANT: THIS IS DOORBELL CAMERA FOOTAGE. Vertical 9:16 real security camera still. An ordinary American man around seventy three years old sits in a wicker chair on a suburban front porch. He has a white baseball cap, short white hair at the sides, a trimmed white beard, deeply lined skin, age spots on his forearms and no retouching. He wears a plain orange ribbed tank top and dark trousers. His hands rest on his knees and his expression is calm and unbothered. Flat daylight, sharp focus everywhere, no blur. He looks like a real ordinary old man, not a model. No captions, no subtitles, no words overlaid on the image, no studio lighting, no plastic skin, no beauty smoothing.
```

## Trava da 2ª pessoa · REF-B · a mulher jovem · gerar e aprovar ANTES do K01

```text
IMPORTANT: THIS IS DOORBELL CAMERA FOOTAGE. Vertical 9:16 real security camera still. An ordinary American woman around twenty eight years old stands on a suburban front porch, facing slightly to her left. She has long straight dark blonde hair past her shoulders, warm medium skin, visible pores, natural facial asymmetry and light everyday makeup. She wears a plain fitted light blue summer dress. Her arms are relaxed at her sides and her expression is open and a little nervous. Flat daylight, sharp focus everywhere, no blur. She looks like a real ordinary neighbour, not a model. No captions, no subtitles, no words overlaid on the image, no studio lighting, no plastic skin, no beauty smoothing.
```

Gerar os dois, aprovar os rostos, e usar como referência no K01 e no K02.

---

## GATE DE COMPOSIÇÃO VISUAL (rodado ANTES dos prompts abaixo)

```
HEROI
[x] 1. Heroi no LOWER FOREGROUND mais perto que o rosto  -> so no K04 (o frasco). VER EXCECAO 1
[x] 2. Nada compete com o heroi
[-] 3. Volume e cobertura                                 -> nao se aplica, nao ha heroi volumetrico

DISTANCIA
[x] 4. "Da pra estar mais perto?"                         -> K02, K03, K04 sim. K01 NAO. VER EXCECAO 1
[x] 5. Pessoas em peito pra cima                          -> K02, K03, K04
[x] 6. O take mais fechado do video e o do CTA            -> K04

FUNDO
[x] 7. Cenario reconhecivel, nunca inventariado           -> 2 ancoras na garagem, 2 na varanda
[x] 8. Fundo reduzido por enquadramento, nunca por blur
[x] 9. Menos elementos = mais qualidade

2a PESSOA
[x] 10. 2a pessoa cortada pelo quadro                     -> K02 sim. K01 NAO. VER EXCECAO 2
```

### As duas exceções deste vídeo, e por que são legítimas

**EXCEÇÃO 1, no K01: o plano fica LARGO de propósito.**
Em todos os outros vídeos o herói é um prop físico e a regra manda colar a câmera nele. Aqui **não existe prop.** O herói do hook é o **formato de câmera de campainha somado à legenda**. Fechar o plano destrói a leitura de vazamento de segurança, que é justamente o que faz o vídeo não parecer anúncio. **O enquadramento largo É o herói.** Fechar aqui seria o mesmo erro que cortar um reveal contínuo em dois takes.

**EXCEÇÃO 2, no K01: os dois figurantes aparecem de corpo inteiro.**
Câmera de campainha enquadra a varanda inteira. Cortar a mulher pela borda contradiz o formato e denuncia que é cena montada.

**As duas exceções valem SÓ no K01.** Do K02 em diante a regra normal volta a valer integralmente, e o K02 já entra bem mais fechado que o original.

---

# Prompts de imagem

## K01 · T1 · HOOK · GERAR DO ZERO (Nano Banana **Pro**, várias variações) · REF-A + REF-B

```json
{
  "shot_id": "K01_porch_wide",
  "context": "Fictional AI-generated characters. No real people are being filmed or depicted.",
  "reference_use": "Use the first attached image ONLY for the old man's face and identity. Use the second attached image ONLY for the young woman's face and identity, so they are clearly the SAME two people. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT old man from the first reference image: American man around seventy three, white baseball cap, trimmed white beard, orange ribbed tank top, dark trousers. He sits in a wicker chair, hands on his knees, calm and unbothered.",
  "second_person": "The EXACT young woman from the second reference image: American woman around twenty eight, long dark blonde hair, fitted light blue summer dress. She stands facing him, one hand raised mid-gesture as she speaks.",
  "scene": "The front porch of an American suburban house. White railing, a wicker chair, a lawn and a parked car far behind. Nothing else competes for attention.",
  "composition": "WIDE HIGH ANGLE, exactly like real doorbell camera footage. The camera is mounted high on the wall looking down across the whole porch. BOTH people are fully visible head to foot, the old man seated on the left, the woman standing on the right. This wide framing is deliberate and must not be tightened.",
  "camera": "high mounted wall angle looking down, wide, slight fisheye distortion at the edges like a security lens",
  "state": "Start frame: she is mid-sentence with one hand raised, he is seated looking up at her.",
  "lighting": "Flat mid-afternoon daylight, slightly washed out and low contrast, exactly like a security camera sensor.",
  "realism": "Real doorbell camera footage look, slightly soft and compressed like a security feed, real skin texture, natural imperfection, no cinematic grading, no AI polish, no beauty smoothing, no blur.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no timestamp, no studio, no plastic skin, no extra fingers, no cinematic lighting, no shallow depth of field, no third person"
}
```

## K02 · T2 a T6 · VARANDA DE PERTO · GERAR DO ZERO · REF-A + REF-B

```json
{
  "shot_id": "K02_porch_close",
  "reference_use": "Use the first attached image ONLY for the old man's face and identity. Use the second attached image ONLY for the young woman's face and identity. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT old man from the first reference image: American man around seventy three, white baseball cap, trimmed white beard, orange ribbed tank top. Seated in the wicker chair, turned toward her.",
  "second_person": "The EXACT young woman from the second reference image: American woman around twenty eight, long dark blonde hair, fitted light blue summer dress. She has moved closer and now stands right beside his chair, leaning slightly toward him.",
  "scene": "SAME suburban front porch as K01, same wicker chair, same white railing, same daylight.",
  "composition": "TIGHT chest-up two-shot from the side, much closer than K01. His head and shoulders fill the left of frame, hers fill the right, and she is CROPPED by the right edge from the shoulder down. The porch behind is barely readable, just enough to recognise the place.",
  "camera": "chest level, side angle, close, handheld phone distance",
  "state": "Start frame: the two of them mid-conversation, he is listening, she is speaking.",
  "lighting": "SAME flat mid-afternoon daylight as K01.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no timestamp, no studio, no plastic skin, no extra fingers, no blur, no third person, no high security camera angle"
}
```

## K03 · T7 a T24 · A VENDA · GERAR DO ZERO · ÂNCORA MELODY

```json
{
  "shot_id": "K03_melody_talking",
  "reference_use": "Use the attached image ONLY for Melody's face, identity, hair, tattoos and clothing. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT MAN from the reference image (Melody Carter), a male adult: Black man, muscular build, long dark box braids falling in front of the shoulders, trimmed goatee and beard, ornamental tattoo sleeve on his right arm, small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "scene": "SAME garage as the reference image, with only two visible anchors: the red neon sign on the wall and the vintage American flag beside it. A plain wooden workbench in front of him. Nothing else competes for attention.",
  "posture": "SEATED UPRIGHT at the workbench, leaning slightly forward toward the camera, forearms resting on the wood, chin level. NOT the relaxed slouch of the reference photo.",
  "composition": "TIGHT chest-up framing, close to the lens, his head and shoulders filling most of the frame, cropped at the top of his head. NOTHING in his hands and nothing on the bench. His hands come up into the bottom of frame in a natural open gesture.",
  "camera": "chest level, straight-on, close",
  "state": "Start frame: speaking directly into the lens, calm and direct.",
  "lighting": "Warm low garage light with the red glow of the neon on the wall behind him.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no relaxed slouch, no second person, no props on the bench"
}
```

## K04 · T25 a T31 · PRODUTO E CTA · GERAR DO ZERO (Nano Banana **Pro**) · ÂNCORA MELODY + PRODUCT.PNG

```json
{
  "shot_id": "K04_melody_product",
  "reference_use": "Use the first attached image ONLY for Melody's face, identity, hair, tattoos and clothing. Use the second attached image ONLY for the exact shape, size, proportions and label layout of the bottle. Do NOT copy the pose or framing of either reference. This must be the CLOSEST framing of the entire video.",
  "identity_main": "The EXACT MAN from the first reference image (Melody Carter), a male adult: Black man, muscular build, long dark box braids falling in front of the shoulders, trimmed goatee and beard, ornamental tattoo sleeve on his right arm, small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "product": "The EXACT white supplement bottle from the second reference image, with its purple and white label, about 10 cm tall. He holds it upright in his right hand at chest height, label turned squarely toward the lens, closer to the camera than his own face and clearly the hero of the frame.",
  "scene": "SAME garage as K03, same red neon and vintage flag behind him, same workbench.",
  "posture": "SEATED UPRIGHT at the workbench, leaning further toward the camera than in K03. NOT the relaxed slouch of the reference photo.",
  "composition": "TIGHT chest-up close-up, the tightest framing in the whole video. His head and shoulders fill the upper frame and the bottle sits in the lower foreground, closer to the lens than his face.",
  "camera": "chest level, straight-on, very close, angled slightly toward the bottle",
  "state": "Start frame: bottle already raised and steady, speaking straight into the lens.",
  "lighting": "SAME warm low garage light and red neon glow as K03.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no relaxed slouch, no second bottle, no second person"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Colar em todo prompt:

```text
o personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

Estilo TikTok nativo, UGC. Preservar exatamente a identidade, o rosto, a roupa, o cenário, a iluminação e o enquadramento do frame inicial. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

**Parte 1 (V01 a V06):** manter o look de câmera de campainha, imagem levemente lavada e comprimida.
**Parte 2 (V07 a V31):** o Melody permanece sentado e ereto o tempo todo, nunca se recosta.

---

### V01 · T1 · usa K01

```text
a mulher jovem fala em inglês com sotaque americano, voz nervosa e sussurrada, como quem está dizendo algo que não deveria, a seguinte frase: "Baby, I know you are seventy three, and I know I have a husband, but the way you carry yourself."

ela diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela gesticula com uma mão enquanto fala e dá um passo curto na direção dele. O homem idoso continua sentado, imóvel, apenas olhando pra ela.

câmera: fixa, alta, sem movimento, como câmera de campainha

som ambiente: rua de subúrbio ao ar livre, pássaros ao longe, sem música
```

### V02 · T2 · usa K02

```text
a mulher jovem fala em inglês com sotaque americano, voz baixa e urgente, a seguinte frase: "I just cannot control myself anymore. I need you to pin me down right now."

ela diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela se inclina um pouco mais na direção dele e encosta a mão no encosto da cadeira. Ele permanece parado.

câmera: fixa, leve handheld natural

som ambiente: rua de subúrbio ao ar livre, sem música
```

### V03 · T3 · usa K02

```text
o homem idoso fala em inglês com sotaque americano, voz calma e firme, sem se alterar, a seguinte frase: "Not happening. But I will tell your man exactly what to do to make you forget you ever said that."

ele diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele balança a cabeça uma vez, devagar, e depois olha pra ela com uma expressão tranquila.

câmera: fixa, leve handheld natural

som ambiente: rua de subúrbio ao ar livre, sem música
```

### V04 · T4 · usa K02

```text
a mulher jovem fala em inglês com sotaque americano, voz baixa e envergonhada, a seguinte frase: "He is fifty two, and his winner has not worked in months. Tell me everything."

ela diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela desvia o olhar por um instante ao falar e depois volta a olhar pra ele na última frase.

câmera: fixa, leve handheld natural

som ambiente: rua de subúrbio ao ar livre, sem música
```

### V05 · T5 · usa K02

```text
o homem idoso fala em inglês com sotaque americano, voz calma e confiante, a seguinte frase: "I took the advice of one American coach who does nothing but this."

ele diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele levanta um dedo enquanto fala e mantém o olhar nela.

câmera: fixa, leve handheld natural

som ambiente: rua de subúrbio ao ar livre, sem música
```

### V06 · T6 · usa K02

```text
o homem idoso fala em inglês com sotaque americano, voz calma e direta, a seguinte frase: "Over ten years helping men over fifty get their hard winners back. Tell him to watch this right now."

ele diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pra frente com o queixo na última frase e a mulher assente devagar.

câmera: fixa, leve handheld natural

som ambiente: rua de subúrbio ao ar livre, sem música
```

### V07 · T7 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, como se exigisse ser ouvido, a seguinte frase: "I have spent over ten years fixing winners for American men over fifty."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro pra garagem. ele está sentado ereto na bancada e abre a mão direita na altura do peito enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V08 · T8 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "And in ten years I have never once seen a winner fail because of age."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele balança a cabeça devagar de um lado pro outro enquanto diz a última parte.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V09 · T9 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "Every single time it is the same thing. One hormone running completely unchecked. That hormone is cortisol, your stress hormone."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele levanta um dedo e o mantém parado no ar ao dizer o nome do hormônio.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V10 · T10 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "Here is what is actually happening inside you right now."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele se inclina um pouco mais pra frente sobre a bancada e abre as duas mãos.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V11 · T11 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "When cortisol stays elevated year after year, it goes to war with your testosterone every single night while you sleep."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele bate os punhos um contra o outro devagar ao dizer que vai à guerra.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V12 · T12 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "It starves your winner of everything it needs to grow full, rise hard, and stay there."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele fecha a mão devagar até virar um punho apertado enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V13 · T13 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "It strips your drive completely and locks your whole body in survival mode, where your winner is the last priority."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele faz um gesto de trancar com as duas mãos, uma sobre a outra, e depois abaixa os braços.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V14 · T14 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "That is why the blue pills from Walgreens stopped working. That is why the boosters from GNC did nothing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele conta dois itens nos dedos enquanto fala e depois descarta os dois com um gesto curto de mão.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V15 · T15 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "That is why every diet change made zero difference. None of it worked."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele abre as duas mãos vazias na frente do corpo na última frase.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V16 · T16 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "You were treating what you could see while cortisol kept destroying everything underneath, every single night."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pra cima com uma mão e pra baixo com a outra, mostrando as duas camadas.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V17 · T17 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz mais baixa e mais grave, quase confidencial, a seguinte frase: "And while you kept trying the wrong fixes, she kept feeling more and more alone in that bed."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele para de gesticular completamente e apenas olha pra câmera enquanto fala.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V18 · T18 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz baixa e grave, quase confidencial, a seguinte frase: "Reaching for a man who used to show up every single time, wondering if he is ever coming back."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele mantém o olhar fixo na câmera e apenas fecha os lábios no fim da frase.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V19 · T19 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz firme e encorajadora, a seguinte frase: "He is still in there, brother. But cortisol is running the show."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pra câmera na primeira frase e depois abre a mão na segunda.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V20 · T20 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz firme, a seguinte frase: "And cortisol has to be shut down at the source, not patched from the outside."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele faz um gesto de cortar com a mão na horizontal ao dizer a primeira parte.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V21 · T21 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz que abre e fica mais leve, a seguinte frase: "Here is the good news. There is one ancient remedy that hunts cortisol down before it ever touches your testosterone."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a expressão dele abre e ele levanta um dedo ao falar do remédio.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V22 · T22 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica e confiante, a seguinte frase: "It is saffron. Men have been using it for this since before your grandfather's grandfather was born."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele para por um instante depois de dizer a primeira palavra e depois continua.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V23 · T23 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz de alerta, a seguinte frase: "But you can swallow the right dose and still get nothing, because most of it passes straight through you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele faz um gesto de algo passando reto com a mão, da esquerda pra direita.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V24 · T24 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz firme, a seguinte frase: "The form matters more than the milligrams. That is what nobody tells you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele bate o dedo indicador na bancada duas vezes ao dizer a primeira frase.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V25 · T25 · usa K04

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica e confiante, a seguinte frase: "Korella Saffron is the only one I trust, and the only one I put my clients on."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele ergue o frasco na direção da câmera ao dizer o nome do produto e o mantém firme.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V26 · T26 · usa K04

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "Pure extract, eighty eight point five milligrams, in the form that actually gets through."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pro rótulo com o dedo enquanto fala e depois volta a segurar o frasco firme.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V27 · T27 · usa K04

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz mais leve, quase divertida, a seguinte frase: "Men come back to me around week three saying the same thing. They went all night. And she did not know what hit her."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele abre um sorriso curto na última frase e balança a cabeça devagar.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V28 · T28 · usa K04

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz mais leve, a seguinte frase: "One of them told me he felt twenty five again, and that he had forgotten what that even felt like."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele encolhe os ombros de leve e mantém o frasco erguido.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V29 · T29 · usa K04

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz firme e conclusiva, a seguinte frase: "It is on Amazon. And it is the one thing that finally takes cortisol off your testosterone."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele ergue o frasco um pouco mais alto e o mantém parado até o fim da frase.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V30 · T30 · usa K04

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz direta, a seguinte frase: "Comment yes and I will send you the link straight to your messages."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pra baixo, na direção dos comentários, mantendo o frasco na outra mão.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

### V31 · T31 · usa K04

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz firme no começo e mais baixa na última frase, a seguinte frase: "But follow me first, brother, or it will not let me reach you. And she cannot wait much longer."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta uma vez pra câmera e depois baixa a mão e segura o olhar até o fim.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa à noite, sem música, sem ruído de fundo
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-A | nenhuma, gerar do zero | Nano Banana 2, regenerar até rosto de idoso crível |
| REF-B | nenhuma, gerar do zero | Nano Banana 2, regenerar até rosto crível |
| K01 | REF-A + REF-B aprovados | Nano Banana **Pro**, várias variações |
| K02 | REF-A + REF-B aprovados | Nano Banana 2 |
| K03 | âncora Melody | Nano Banana 2 |
| K04 | **âncora Melody + product.png** | Nano Banana **Pro** (o rótulo precisa sair legível) |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps. Cortes duros entre todos os takes.
- **O corte que mais importa é V06 para V07**, a virada da varanda pra garagem. Corte seco, sem transição.
- **A parte 1 leva overlay de câmera de campainha na EDIÇÃO**, não na geração: timestamp no canto superior, etiqueta de local, e um leve vinheta de lente grande angular. Foi deixado fora dos prompts de imagem de propósito, porque texto gerado sai errado.
- **Legendas são obrigatórias neste vídeo, não opcionais.** O hook depende do texto na tela: a fala do T1 sozinha não segura sem a legenda reforçando "seventy three" e "I have a husband".
- Cortar o silêncio inicial de cada clipe.
- **Segurar um beat de silêncio depois de "It is saffron" no V22.** É o pagamento do loop aberto lá no V08.
- Legendas grandes estilo Captions.ai Prism Pro, palavra destacada em vermelho, na altura do peito. Nunca cobrir o rótulo do frasco de V25 em diante.
- Manter `YES` isolado na tela no CTA.
- **Duas texturas de imagem diferentes:** a parte 1 fica mais lavada e comprimida, a parte 2 fica quente e nítida. Não igualar as duas no color grading, o contraste entre elas é parte do efeito.
- Color grading da parte 2: temp +4, tint 0, saturação -4, exposição -3, contraste +14, highlight -30, shadow +20, fade +4.

## Gates de qualidade

1. **Melody é HOMEM em todos os clipes da parte 2.**
2. Melody é o mesmo homem em todos, com a cruz de **PRATA** sempre, nunca ouro.
3. As box braids estão iguais em todos os planos.
4. **Melody está SENTADO ERETO em todos os takes**, nunca recostado e relaxado.
5. REF-A e REF-B são as mesmas duas pessoas no K01 e no K02.
6. **O K01 é o único plano largo do vídeo e continua largo.** Se ele saiu fechado, regenerar.
7. **O K01 parece câmera de campainha**, imagem levemente lavada e de baixo contraste. Se saiu cinematográfico, regenerar.
8. Nenhuma legenda, timestamp ou texto foi gerado dentro da imagem. Tudo isso entra na edição.
9. **O frasco do K04 bate com o product.png** em tamanho, proporção e layout, e aparece de T25 a T31.
10. **O K04 é o plano mais fechado do vídeo inteiro.**
11. O frasco está mais perto da lente que o rosto dele no K04.
12. Fundo reconhecível e não inventariado: duas âncoras na garagem, duas na varanda.
13. Nenhuma imagem tem fundo desfocado.
14. Mãos com cinco dedos, sem fusão com o frasco nem com a bancada.
15. `yes` e o follow gate estão os dois no CTA final.
