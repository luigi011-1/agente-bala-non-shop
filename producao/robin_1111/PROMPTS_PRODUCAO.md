# Robin Matthews | Ângulo 3 (Auraly) | Pacote de Prompts

Vídeo modelo: `scarlletmorgantarot (1).mp4` · 83,916s · zero cortes de cena

Âncora de identidade: `producao/_ancoras/Robin.Matthewsus .jpeg`
**Atenção ao nome do arquivo:** tem espaço antes da extensão e o `Matthewsus` não tem ponto nem underline.

Funil: vídeo → comentário `222` → DM com o rosto → link · mais o Stories como degrau 2

**Cinco ganchos escolhidos pelo Luigi em 2026-09-04:** o das velas acesas com o fósforo, o do sopro nas
velas, o da mão que vira a carta, o do mel e o do vapor da chaleira. **A copy é a mesma nos cinco**, só
o T1 muda, então são cinco keyframes de Setup A e um único Setup B reaproveitado.

---

## Índice de geração

| Take | Keyframe | Ação de geração | 📎 Anexar |
|---|---|---|---|
| prop | REF-CARTA | 🆕 GERAR DO ZERO | **NADA** |
| T1 · gancho das velas e do fósforo | K01 | 🆕 GERAR DO ZERO | ÂNCORA ROBIN + REF-CARTA |
| T1 · gancho do sopro nas velas | K02 | ✏️ EDITAR do K01 | só o K01 aprovado |
| T1 · gancho da mão que vira a carta | K03 | 🆕 GERAR DO ZERO | ÂNCORA ROBIN + REF-CARTA |
| T1 · gancho do mel | K04 | 🆕 GERAR DO ZERO | ÂNCORA ROBIN + REF-CARTA |
| T1 · gancho do vapor da chaleira | K05 | 🆕 GERAR DO ZERO | ÂNCORA ROBIN + REF-CARTA |
| T2, T3, T4 | K06 | 🆕 GERAR DO ZERO | ÂNCORA ROBIN + REF-CARTA |
| T5, T6, T7, T8 | K07 | ✏️ EDITAR do K06 | só o K06 aprovado |
| T9, T10, T11, T12 | K08 | ✏️ EDITAR do K06 | só o K06 aprovado |

**Regra de bolso do anexo:** `GERAR DO ZERO` anexa âncora mais REF. `EDITAR` anexa **uma imagem só**,
o keyframe de origem.
🚫 **Nunca anexar o K07 na geração do K08.** Os dois saem do K06, nunca em cascata um do outro.

Total: 1 referência de prop + 8 keyframes para 12 takes, sendo 5 deles variações do mesmo T1.
Rodando um gancho só, são 4 keyframes.

---

## Trava de identidade e continuidade

Aplicar em toda imagem e todo clipe:

- Preservar exatamente o rosto da Robin: mulher branca americana de setenta e dois anos, porte pequeno, rosto arredondado com papada suave, nariz curto e reto, sobrancelhas finas e claras, olhos claros.
- **Bob branco-prateado logo abaixo da orelha, risca de lado**, liso, preso atrás de uma orelha.
- **Óculos de leitura de aro dourado fino, apoiados baixos no nariz.** Nunca tirar dos takes de fala.
- Pele clara e castigada, com **manchas de idade na testa, nas maçãs do rosto e nas costas das mãos**, linhas profundas na testa e ao redor da boca, pés de galinha. **ZERO maquiagem.** A idade é o ativo dela: nunca rejuvenescer, nunca alisar a pele, nunca apagar as manchas.
- Cardigã cinza mescla sobre blusa branca de gola aberta. **Corrente fina de PRATA com pingente pequeno de cruz de prata.** **Aliança de ouro lisa** na mão esquerda.
- Mesma cozinha de armários de carvalho em todos os planos: mesa de madeira no terço inferior, pia e janela à direita, segunda janela à esquerda.
- **Kit de tarólogo em dois grupos, nunca listado solto.** Grupo da mesa: baralho clássico de borda branca em cavalete de madeira, esfera de quartzo rosa em suporte, drusa de citrino, queimador de latão com tampa vazada soltando um fio fino de fumaça, duas velas finas brancas em castiçais de latão. Grupo da parede: quadro emoldurado LUNAR CALENDAR e crucifixo de madeira.
- **Bandeira dos EUA pequena em suporte preto no peitoril da janela, sempre visível e em foco.**
- Luz natural neutra de dia nublado pelas duas janelas, fria e uniforme no rosto. Nunca dominante quente.
- Zero blur, tudo em foco nítido incluindo armários, quadro e bandeira. Cara de vídeo de iPhone, nunca polimento de IA.

---

## Trava do prop herói (a carta SOULMATE)

Gerar **uma vez** como `REF-CARTA`, aprovar, e anexar como referência de objeto em todo keyframe que a
mostre. Sem isso a arte muda de take pra take.

```text
Modern foil tarot card with rounded corners and a clean printed surface. Wide mirrored silver metallic border with a rainbow holographic sheen, engraved arabesque and a flourish in each corner. Roman numeral in serif capitals at the top. Title band at the bottom carrying the word SOULMATE in spaced serif capitals. Two figures in timeless flowing robes facing each other in flat symbolic style with fine ink hatching, a luminous white heart between their heads, rays of light behind them and an arch of roses framing the pair. Saturated palette: carmine and pink roses, lavender, warm gold and white light. The shine is printed foil ink catching the light, never a glow.
```

⚠️ **O baralho da MESA dela é clássico de borda branca, e não é este.** A leitura é que ela puxou uma
carta especial. **Nunca escrever que a carta saiu daquele maço**, e nunca mostrar ela tirando do maço.

---

## Trava da 2ª pessoa (REF-A)

**Não existe 2ª pessoa neste vídeo.** O modelo é uma pessoa só, do primeiro ao último frame, e o clone
mantém isso. Nenhum keyframe leva REF-A, e o negative de todos carrega `no second person`.

---

# Prompts de imagem

## REF-CARTA · PROP HERÓI · GERAR DO ZERO

> ### 📎 ANEXAR: **NADA**
>
> ### 🆕 GERAR DO ZERO

Carta de tarô sozinha, deitada, ocupando o quadro. É a única imagem do pacote **sem cenário e sem
bandeira**, de propósito: cenário aqui contaminaria todo keyframe que anexasse esta referência.

```json
{
  "shot_id": "REF_CARTA_soulmate",
  "task": "Generate one single tarot card lying flat and filling the frame, shot straight down on a plain neutral grey surface.",
  "card_object": "A modern foil tarot card with rounded corners and a clean printed surface. A wide mirrored silver metallic border with a rainbow holographic sheen runs around the whole card, with an engraved arabesque and a small flourish in each corner. A Roman numeral in serif capitals sits at the top. A title band across the bottom carries the word SOULMATE in spaced serif capitals.",
  "card_art": "Two figures in timeless flowing robes face each other, drawn in a flat symbolic style with fine ink hatching, never rounded cartoon faces. A luminous white heart sits between their heads, rays of light rise behind them, and an arch of roses frames the pair. Behind them a celestial motif: a stylised sun, a crescent moon and five pointed stars.",
  "palette": "Saturated and vivid: carmine and pink roses, lavender, warm gold and white light, printed over the mirrored metallic border. The shine is printed foil ink catching the light, a property of the printed object.",
  "lighting": "Flat neutral overcast daylight, even across the whole card.",
  "realism": "Real printed cardstock texture with slight surface grain, realistic reflections of the foil as printed ink, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no cartoon style, no children's book illustration, no cute rounded faces, no modern clothing, no plain white border, no comic art, no 3d render, no skulls, no ravens, no snakes, no swords, no inverted symbols, no sigils, no captions, no subtitles, no watermark, no words overlaid on the image. The only text anywhere is the single word inside the title band at the bottom of the card."
}
```

## K01 · T1 · GANCHO DAS VELAS E DO FÓSFORO · GERAR DO ZERO · ÂNCORA ROBIN + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA ROBIN** `producao/_ancoras/Robin.Matthewsus .jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO

A carta em pé entre os dois castiçais no primeiro plano, ela com o fósforo aceso descendo pro primeiro pavio.

```json
{
  "shot_id": "K01_hook_candles",
  "reference_use": "Use the first attached image ONLY for Robin's face, identity, glasses, hair, wardrobe and the oak kitchen scene. Use the second attached image ONLY for the exact art, border and title band of the tarot card she has on the table. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Robin): white American woman of seventy two, small frame, silver-white bob cut just below the ears parted at the side, thin gold-rimmed reading glasses sitting low on her nose, pale eyes, rounded face with soft jowls, deep lines across the forehead and around the mouth, crow's feet, age spots on her cheeks and on the backs of her hands, no makeup at all.",
  "wardrobe": "Heather-grey cardigan over a plain white collared blouse, thin silver chain with a small silver cross pendant, plain gold wedding band on her left hand.",
  "prop": "The tarot card from the second reference image stands upright on the wooden table, leaning against a small wooden stand, its title band and couple illustration facing the camera and fully readable. A tall white taper candle in a brass holder stands on each side of it, both wicks still unlit. In her right hand she holds a lit wooden match, the small flame steady.",
  "scene": "SAME oak-cabinet home kitchen as the reference image. On the wooden table beside the candles: a classic white-bordered tarot deck in a wooden card stand, a polished rose quartz sphere on its stand, a rough citrine cluster and a brass incense burner with a pierced lid releasing a thin thread of smoke. On the wall behind her a framed lunar calendar print and a plain wooden cross. A small United States flag on a black stand sits on the windowsill above the sink, clearly visible and in sharp focus.",
  "posture": "Seated upright at her own kitchen table, shoulders square to the camera, leaning slightly forward over the candles.",
  "composition": "The two brass candlesticks and the standing card sit in the lower foreground, closer to the lens than her face, and they dominate the bottom two thirds of the frame. Robin is visible from the chest up in the upper part of the frame, the top of her head cropped by the top edge. The kitchen behind is recognisable but not inventoried.",
  "camera": "chest level, straight-on, camera pushed in close over the table, tight framing",
  "state": "Start frame: the lit match is coming down toward the first wick and has not touched it yet. Both candles are still unlit. She is looking down at the wick.",
  "lighting": "Flat neutral overcast daylight coming through the two kitchen windows, cool and even on her face.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the cabinets, the framed print and the flag.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no makeup, no second person, no lit candles in this frame"
}
```

## K02 · T1 · GANCHO DO SOPRO NAS VELAS · EDITAR do K01

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K01 já aprovado**
>
> ### ✏️ EDITAR, muda só as chamas e as mãos dela

As duas velas já acesas, o fósforo sumiu, e ela junta as mãos perto da boca pra soprar.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Robin exactly the same: same face, same seventy-two-year-old skin with the same age spots and lines, same silver-white bob, same gold-rimmed glasses low on the nose, same grey cardigan and white blouse, same silver cross, same gold wedding band. Keep the SAME tarot card standing between the candles with the same art, border and title band. Keep the SAME background exactly: oak kitchen, table, tarot deck in its wooden stand, rose quartz sphere, citrine cluster, brass incense burner with its thin thread of smoke, framed lunar calendar print, wooden cross, the small United States flag on the windowsill, same neutral daylight, same camera angle and framing.",
  "change_1": "Both taper candles are now lit, each with a small steady flame on the wick. The wooden match is gone from her hand.",
  "change_2": "She now leans a little further forward with both hands brought together in front of her mouth, palms almost touching, about to blow toward the lens. Her eyes are on the candles.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the card, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no second person"
}
```

## K03 · T1 · GANCHO DA MÃO QUE VIRA A CARTA · GERAR DO ZERO · ÂNCORA ROBIN + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA ROBIN** `producao/_ancoras/Robin.Matthewsus .jpeg`
> **2️⃣ REF-CARTA** já aprovada, aqui **só pelo verso e pela espessura da carta**
>
> ### 🆕 GERAR DO ZERO

A mão de setenta e dois anos entra cortada pela borda e encosta na carta virada pra baixo.

```json
{
  "shot_id": "K03_hook_hand",
  "reference_use": "Use the first attached image ONLY for Robin's face, identity, glasses, hair, wardrobe and the oak kitchen scene. Use the second attached image ONLY for the physical card object, its mirrored holographic back, its thickness and its rounded corners. The printed face of that card is NOT visible in this frame. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Robin): white American woman of seventy two, small frame, silver-white bob cut just below the ears parted at the side, thin gold-rimmed reading glasses sitting low on her nose, pale eyes, deep lines across the forehead and around the mouth, crow's feet, heavy age spots on her cheeks and on the backs of her hands, no makeup at all.",
  "wardrobe": "Heather-grey cardigan over a plain white collared blouse, thin silver chain with a small silver cross pendant, plain gold wedding band on her left hand.",
  "prop": "A single tarot card lies face down on the wooden table in the lower foreground, showing only its mirrored silver holographic back. Her right hand enters the frame from the right edge and is cropped by it, with two fingertips resting on the near corner of the card. The hand is the most detailed thing in the frame: heavy age spots, raised veins, short unpainted nails, the gold wedding band clearly visible.",
  "scene": "SAME oak-cabinet home kitchen as the reference image. On the table around the card: a classic white-bordered tarot deck in a wooden card stand, a polished rose quartz sphere on its stand, a rough citrine cluster and a brass incense burner with a pierced lid releasing a thin thread of smoke. On the wall behind her a framed lunar calendar print and a plain wooden cross. A small United States flag on a black stand sits on the windowsill above the sink, clearly visible and in sharp focus.",
  "posture": "Seated at her own kitchen table, leaning forward over the table so her hand reaches the card easily.",
  "composition": "The wooden table and the face-down card fill the lower two thirds of the frame and sit much closer to the lens than her face. Her hand entering from the right edge is the hero of the frame. Robin's face is visible smaller in the upper part of the frame, watching the lens rather than the card.",
  "camera": "low chest level, angled slightly down toward the table, camera pushed in close to the card",
  "state": "Start frame: her fingertips have just landed on the corner of the face-down card. The card has not moved yet.",
  "lighting": "Flat neutral overcast daylight coming through the two kitchen windows, cool and even.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the cabinets, the framed print and the flag.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no makeup, no second person, no face-up card in this frame"
}
```

## K04 · T1 · GANCHO DO MEL · GERAR DO ZERO · ÂNCORA ROBIN + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA ROBIN** `producao/_ancoras/Robin.Matthewsus .jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO

A carta deitada numa tigela rasa de vidro e o mel prestes a cair em cima dela.

```json
{
  "shot_id": "K04_hook_honey",
  "reference_use": "Use the first attached image ONLY for Robin's face, identity, glasses, hair, wardrobe and the oak kitchen scene. Use the second attached image ONLY for the exact art, border and title band of the tarot card lying in the bowl. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Robin): white American woman of seventy two, small frame, silver-white bob cut just below the ears parted at the side, thin gold-rimmed reading glasses sitting low on her nose, pale eyes, deep lines across the forehead and around the mouth, crow's feet, age spots on her cheeks and on the backs of her hands, no makeup at all.",
  "wardrobe": "Heather-grey cardigan over a plain white collared blouse, thin silver chain with a small silver cross pendant, plain gold wedding band on her left hand.",
  "prop": "The tarot card from the second reference image lies face up in a shallow clear glass bowl on the wooden table, its title band and couple illustration fully readable through the glass. Her right hand holds a wooden honey dipper loaded with thick amber honey, held above the bowl. A small open glass honey jar sits beside the bowl.",
  "scene": "SAME oak-cabinet home kitchen as the reference image. On the table behind the bowl: a classic white-bordered tarot deck in a wooden card stand, a polished rose quartz sphere on its stand, a rough citrine cluster and a brass incense burner with a pierced lid releasing a thin thread of smoke. On the wall behind her a framed lunar calendar print and a plain wooden cross. A small United States flag on a black stand sits on the windowsill above the sink, clearly visible and in sharp focus.",
  "posture": "Seated upright at her own kitchen table, leaning slightly forward over the bowl.",
  "composition": "The glass bowl with the card inside sits in the lower foreground, closer to the lens than her face, and fills the bottom of the frame. The loaded dipper is held just above it. Robin is visible from the chest up in the upper part of the frame, the top of her head cropped by the top edge.",
  "camera": "chest level, angled slightly down toward the bowl, camera pushed in close",
  "state": "Start frame: the honey on the dipper has gathered into a single hanging thread that has not touched the card yet. The card is still completely clean and dry.",
  "lighting": "Flat neutral overcast daylight coming through the two kitchen windows, cool and even. The amber colour belongs to the honey only, never to the light in the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the cabinets, the framed print and the flag.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no makeup, no second person, no honey on the card in this frame"
}
```

## K05 · T1 · GANCHO DO VAPOR DA CHALEIRA · GERAR DO ZERO · ÂNCORA ROBIN + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA ROBIN** `producao/_ancoras/Robin.Matthewsus .jpeg`
> **2️⃣ REF-CARTA** já aprovada, aqui só pela carta em pé no cavalete ao fundo
>
> ### 🆕 GERAR DO ZERO

A caneca fumegante subindo no primeiro plano, a chaleira apitando no fogão atrás.

```json
{
  "shot_id": "K05_hook_steam",
  "reference_use": "Use the first attached image ONLY for Robin's face, identity, glasses, hair, wardrobe and the oak kitchen scene. Use the second attached image ONLY for the exact art, border and title band of the tarot card standing on the table. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Robin): white American woman of seventy two, small frame, silver-white bob cut just below the ears parted at the side, thin gold-rimmed reading glasses sitting low on her nose, pale eyes, deep lines across the forehead and around the mouth, crow's feet, age spots on her cheeks and on the backs of her hands, no makeup at all.",
  "wardrobe": "Heather-grey cardigan over a plain white collared blouse, thin silver chain with a small silver cross pendant, plain gold wedding band on her left hand.",
  "prop": "Both her hands hold a plain white ceramic mug of hot tea, raised toward the lens at chest height, with a thick column of white steam rising from it and spreading upward across the frame. On the stove behind her an old stainless steel kettle is steaming as well. The tarot card from the second reference image stands upright on the table beside her, leaning on a small wooden stand, its title band readable.",
  "scene": "SAME oak-cabinet home kitchen as the reference image. On the table beside the card: a classic white-bordered tarot deck in a wooden card stand, a polished rose quartz sphere on its stand, a rough citrine cluster and a brass incense burner with a pierced lid releasing a thin thread of smoke. On the wall behind her a framed lunar calendar print and a plain wooden cross. A small United States flag on a black stand sits on the windowsill above the sink, clearly visible and in sharp focus.",
  "posture": "Seated upright at her own kitchen table, both forearms lifted, bringing the mug forward toward the camera.",
  "composition": "The mug and its column of steam sit in the lower foreground, closer to the lens than her face, and the steam already covers part of the bottom of the frame. Robin is visible from the chest up in the upper part of the frame, the top of her head cropped by the top edge.",
  "camera": "chest level, straight-on, camera pushed in close to the mug",
  "state": "Start frame: the mug has just been raised and the steam is rising in front of her but has not reached the lens yet.",
  "lighting": "Flat neutral overcast daylight coming through the two kitchen windows, cool and even on her face.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the cabinets, the framed print and the flag.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no makeup, no second person, no steam covering her face in this frame"
}
```

## K06 · T2, T3, T4 · SETUP B · GERAR DO ZERO · ÂNCORA ROBIN + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA ROBIN** `producao/_ancoras/Robin.Matthewsus .jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO

Ela falando pra lente com a carta em pé na mão esquerda, apoiada na borda da mesa.

⚠️ **Os castiçais ficam FORA do quadro aqui, de propósito.** É o que faz este mesmo keyframe servir aos
cinco ganchos: se as velas aparecessem, o take contradiria o gancho que acabou de acendê-las ou apagá-las.

```json
{
  "shot_id": "K06_setup_b_talking",
  "reference_use": "Use the first attached image ONLY for Robin's face, identity, glasses, hair, wardrobe and the oak kitchen scene. Use the second attached image ONLY for the exact art, border and title band of the tarot card in her hand. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Robin): white American woman of seventy two, small frame, silver-white bob cut just below the ears parted at the side and tucked behind one ear, thin gold-rimmed reading glasses sitting low on her nose, pale eyes, rounded face with soft jowls, deep lines across the forehead and around the mouth, crow's feet, age spots on her cheeks and on the backs of her hands, no makeup at all. Her expression is warm and matter-of-fact, the look of a woman who has said this a hundred times and still means it.",
  "wardrobe": "Heather-grey cardigan over a plain white collared blouse, thin silver chain with a small silver cross pendant, plain gold wedding band on her left hand.",
  "prop": "She holds the tarot card from the second reference image upright in her left hand, its lower edge resting on the wooden table, the title band and the couple illustration facing the camera and fully readable.",
  "scene": "SAME oak-cabinet home kitchen as the reference image, seen tighter. On the table beside her hand: a classic white-bordered tarot deck in a wooden card stand and a brass incense burner with a pierced lid releasing a thin thread of smoke. On the wall behind her a framed lunar calendar print and a plain wooden cross. A small United States flag on a black stand sits on the windowsill, clearly visible and in sharp focus.",
  "posture": "Seated upright at her own kitchen table, shoulders square to the camera, forearms resting on the table, looking straight into the lens and talking to the viewer.",
  "composition": "Tight framing from the chest up, her face filling a large part of the frame with the top of her head cropped by the top edge. The card in her left hand sits in the lower foreground, closer to the lens than her face, and stays fully readable. The two brass candlesticks are out of frame. Little of the kitchen is visible, just enough to recognise the room.",
  "camera": "chest level, straight-on, phone propped on the table, close framing",
  "state": "Start frame: she is looking into the lens, about to speak, the card steady in her hand.",
  "lighting": "Flat neutral overcast daylight coming through the kitchen windows, cool and even on her face.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the cabinets, the framed print and the flag.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no makeup, no second person, no candles in frame"
}
```

## K07 · T5, T6, T7, T8 · EDITAR do K06

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K06 já aprovado**
>
> ### ✏️ EDITAR, muda só a mão direita e a expressão

Mesma cena, mão direita aberta no gesto de quem explica.

```json
{
  "task": "edit the attached image, keep everything identical except the change listed",
  "keep_identical": "Keep Robin exactly the same: same face, same seventy-two-year-old skin with the same age spots and lines, same silver-white bob, same gold-rimmed glasses low on the nose, same grey cardigan and white blouse, same silver cross, same gold wedding band. Keep the SAME tarot card upright in her left hand with the same art, border and title band, in the same position resting on the table. Keep the SAME background exactly: oak kitchen, tarot deck in its wooden stand, brass incense burner with its thin thread of smoke, framed lunar calendar print, wooden cross, the small United States flag on the windowsill, same neutral daylight, same camera angle and framing.",
  "change_1": "Her right hand now comes up into the bottom of the frame at chest height, palm open and turned upward in a calm explaining gesture. Her eyebrows are slightly raised and her expression is a little more emphatic.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the card, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no second person"
}
```

## K08 · T9, T10, T11, T12 · CTA · EDITAR do K06

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K06 já aprovado**
> 🚫 **NUNCA anexar o K07 aqui.** Os dois saem do K06, nunca em cascata.
>
> ### ✏️ EDITAR, muda só a distância de câmera e a expressão

O take mais fechado do vídeo inteiro, que por regra é o do CTA.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Robin exactly the same: same face, same seventy-two-year-old skin with the same age spots and lines, same silver-white bob, same gold-rimmed glasses low on the nose, same grey cardigan and white blouse, same silver cross, same gold wedding band. Keep the SAME tarot card upright in her left hand with the same art, border and title band. Keep the SAME background exactly: oak kitchen, tarot deck in its wooden stand, brass incense burner with its thin thread of smoke, framed lunar calendar print, wooden cross, the small United States flag on the windowsill, same neutral daylight, same camera height and angle.",
  "change_1": "Push the camera closer so the framing tightens by about twenty percent. Her face and the card become the only two things that matter in the frame, and the card stays fully readable in the lower foreground.",
  "change_2": "Her expression is more urgent and direct, with strong eye contact into the lens, like someone giving an instruction she does not want repeated.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the card, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no second person"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Colar em todo prompt:

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca de setenta e dois anos, voz autêntica, calorosa e emocional, ritmo pausado, como se exigisse ser ouvida.

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

Estilo TikTok nativo, UGC. Preservar exatamente a identidade da Robin, rosto de setenta e dois anos com as manchas de idade, bob branco-prateado, óculos de leitura de aro dourado, cardigã cinza, cruz de prata, aliança de ouro, a cozinha de carvalho, a iluminação e o enquadramento do frame inicial. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

A câmera é **fixa em todos os takes**, porque o modelo é um celular apoiado na mesa. Não existe braço
estendido segurando aparelho, então a trava de braço parado não entra em nenhum prompt deste pacote.

---

### V01A · T1 · usa K01

```text
(sem fala no take: o take é mudo, exatamente como no modelo)

o que acontece no vídeo: a avatar encosta o fósforo aceso no primeiro pavio, acende a segunda vela, e depois sopra o fósforo na direção da lente. A fumaça branca sobe e cobre o quadro.

câmera: fixa

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

### V01B · T1 · usa K02

```text
(sem fala no take: o take é mudo, exatamente como no modelo)

o que acontece no vídeo: a avatar se inclina para a frente e sopra as duas chamas de uma vez na direção da lente. As duas colunas de fumaça branca sobem juntas e cobrem o quadro.

câmera: fixa

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

### V01C · T1 · usa K03

```text
(sem fala no take: o take é mudo, exatamente como no modelo)

o que acontece no vídeo: a avatar vira a carta com dois dedos e a ilustração do casal aparece. Ela levanta a mão em direção à lente e a mão cobre o quadro.

câmera: fixa

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

### V01D · T1 · usa K04

```text
(sem fala no take: o take é mudo, exatamente como no modelo)

o que acontece no vídeo: o mel cai do cabo de madeira sobre a carta dentro da tigela e escorre devagar por cima dela até cobrir a ilustração. A avatar olha da tigela para a lente.

câmera: fixa

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

### V01E · T1 · usa K05

```text
(sem fala no take: o take é mudo, exatamente como no modelo)

o que acontece no vídeo: a avatar traz a caneca para a frente e o vapor branco sobe e cobre a lente inteira. A chaleira solta vapor no fogão atrás dela.

câmera: fixa

som ambiente: cozinha de casa em silêncio, uma chaleira apitando baixo, sem música
```

### V02 · T2 · usa K06

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca de setenta e dois anos, voz autêntica, calorosa e emocional, ritmo pausado, como se exigisse ser ouvida, a seguinte frase: "I don't know your name. But this video didn't land on you by accident today, and I'm going to tell you why."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar olha direto para a lente e fala com a carta parada na mão esquerda, apoiada na mesa. Ela balança a cabeça de leve na segunda frase.

câmera: fixa

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

### V03 · T3 · usa K06

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca de setenta e dois anos, voz autêntica, calorosa e emocional, ritmo pausado, como se exigisse ser ouvida, a seguinte frase: "The eleven eleven portal opened this morning. Before you scroll past an old woman at her kitchen table, hear what that means for you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar fala para a lente e ergue de leve o queixo ao dizer a segunda frase, mantendo a carta parada na mão esquerda.

câmera: fixa

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

### V04 · T4 · usa K06

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca de setenta e dois anos, voz autêntica, calorosa e emocional, ritmo pausado, como se exigisse ser ouvida, a seguinte frase: "Something started moving toward you this morning that has been still for years. Don't you dare skip this video."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar endurece a expressão na última frase e olha fixo para a lente, sem tirar a carta da mão.

câmera: fixa

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

### V05 · T5 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca de setenta e dois anos, voz autêntica, calorosa e emocional, ritmo pausado, como se exigisse ser ouvida, a seguinte frase: "Not everybody gets sent this video. And what's coming for you isn't money, honey. It's a person."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar faz um pequeno gesto de descarte com a mão direita ao dizer que não é dinheiro, e depois para a mão no ar na última palavra.

câmera: fixa

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

### V06 · T6 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca de setenta e dois anos, voz autêntica, calorosa e emocional, ritmo pausado, como se exigisse ser ouvida, a seguinte frase: "How do I know? I've read these cards for forty years, and they don't open like this for just anybody."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar levanta de leve a carta que está na mão esquerda ao falar dos quarenta anos, e volta a apoiar na mesa.

câmera: fixa

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

### V07 · T7 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca de setenta e dois anos, voz autêntica, calorosa e emocional, ritmo pausado, como se exigisse ser ouvida, a seguinte frase: "Tomorrow morning at eleven eleven, something reaches you that splits your life into a before and an after."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar marca a hora com dois toques curtos do indicador na mesa e depois abre a mão direita.

câmera: fixa

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

### V08 · T8 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca de setenta e dois anos, voz autêntica, calorosa e emocional, ritmo pausado, como se exigisse ser ouvida, a seguinte frase: "So tomorrow when you wake up, reach for your phone first. What's sitting there is their face, and you'll know it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar aponta de leve para a lente na última frase e sustenta o olhar depois de terminar de falar.

câmera: fixa

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

### V09 · T9 · usa K08

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca de setenta e dois anos, voz autêntica, calorosa e emocional, ritmo pausado, como se exigisse ser ouvida, a seguinte frase: "Two two two. Type it right under this video. That's you claiming it out loud. Then send this to yourself, and save it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar aponta para baixo com o indicador ao dizer os números e depois conta as duas ações com dois toques curtos do dedo na mesa.

câmera: fixa

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

### V10 · T10 · usa K08

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca de setenta e dois anos, voz autêntica, calorosa e emocional, ritmo pausado, como se exigisse ser ouvida, a seguinte frase: "The minute you comment, I put their face straight into your messages myself. That's where the reveal happens, not out here."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar leva a mão ao próprio peito ao dizer que é ela mesma quem manda, e na última frase faz um pequeno gesto de negação para o lado.

câmera: fixa

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

### V11 · T11 · usa K08

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca de setenta e dois anos, voz autêntica, calorosa e emocional, ritmo pausado, como se exigisse ser ouvida, a seguinte frase: "But follow me first, or it won't let me reach you. Tomorrow at eleven eleven, open your messages before anything else."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar levanta o indicador na primeira frase e depois baixa a mão, mantendo o olhar fixo na lente.

câmera: fixa

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

### V12 · T12 · usa K08

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca de setenta e dois anos, voz autêntica, calorosa e emocional, ritmo pausado, como se exigisse ser ouvida, a seguinte frase: "One last thing. Tap my picture and watch my stories before they're gone. The proof that this person is real is sitting in there."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar aponta para o canto de cima do quadro ao falar dos stories e termina com a mão parada e o olhar direto na lente.

câmera: fixa, leve push-in

som ambiente: cozinha de casa em silêncio, um relógio de parede ao fundo, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-CARTA | nenhuma, gerar do zero | Nano Banana **Pro**, regenerar até a borda holográfica e a faixa de título saírem limpas |
| K01 | ÂNCORA ROBIN + REF-CARTA | Nano Banana **Pro**, várias variações |
| K02 | K01 aprovado | Nano Banana 2, comando de edição |
| K03 | ÂNCORA ROBIN + REF-CARTA | Nano Banana **Pro**, várias variações. A mão é o herói, regenerar até os dedos saírem certos |
| K04 | ÂNCORA ROBIN + REF-CARTA | Nano Banana **Pro** |
| K05 | ÂNCORA ROBIN + REF-CARTA | Nano Banana **Pro** |
| K06 | ÂNCORA ROBIN + REF-CARTA | Nano Banana **Pro**, é o keyframe que sustenta 11 dos 12 takes |
| K07 | K06 aprovado | Nano Banana 2, comando de edição |
| K08 | K06 aprovado (**nunca a partir do K07**) | Nano Banana 2, comando de edição |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps. **O vídeo inteiro tem que parecer um take só**, como o modelo.
- A única emenda visível é a do T1 para o T2. Cortar exatamente no frame em que a fumaça, a mão, o mel ou o vapor cobrem mais o quadro, que é onde o modelo esconde a dele.
- Cortar o silêncio inicial de cada clipe para a fala começar imediatamente.
- **Faixa branca no topo, do 36º segundo até o fim:** `Check out the surprise in my Stories ⭐`. É o que o corte novo do modelo faz.
- **Dois selos falsos de comentário fixos no canto inferior esquerdo:** `222` e `Amen`, sumindo nos últimos segundos.
- **Círculo animado no selo `222`** durante o V09, copiando o destaque que o modelo faz no selo dele.
- **Confete animado `222`** subindo pelo quadro do V09 até o fim.
- **Seta apontando pro canto da foto de perfil** durante o V12.
- Legenda karaokê de 2 a 3 palavras, centralizada acima da carta. **Nunca cobrir a carta.**
- Manter `222` isolado na tela no CTA.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

---

## Gates de qualidade

1. Robin é a mesma mulher em todos os clipes, com os óculos de aro dourado e a cruz de PRATA em todos.
2. **A idade está preservada em todos os frames:** manchas, linhas e papada intactas. Nenhum frame rejuvenescido, alisado ou maquiado.
3. A aliança de ouro está na mão esquerda em todos os planos.
4. A carta SOULMATE tem a mesma arte, a mesma borda holográfica e a mesma faixa de título em K01, K03, K04, K05, K06, K07 e K08.
5. A bandeira dos EUA aparece pequena, no peitoril, visível e em foco, em todos os keyframes com cenário.
6. O kit da mesa é o mesmo em todos os planos, e o baralho da mesa continua sendo o clássico de borda branca, nunca o holográfico da REF-CARTA.
7. Nenhuma legenda ou palavra foi gerada dentro da imagem. A única palavra em quadro é `SOULMATE` na faixa da carta.
8. Mãos com cinco dedos, sem fusão com a carta, com a caneca nem com a tigela.
9. **Nenhum celular em quadro em nenhum take**, inclusive no T8, que fala de telefone.
10. **Nenhum rosto de alma gêmea aparece em lugar nenhum.** A única ilustração de casal é a da carta, que é arte impressa e não fotografia.
11. A luz é neutra de dia nublado em todos os planos. No K04 o âmbar existe só no mel, nunca na luz da cozinha.
12. O K08 é o plano mais fechado do vídeo inteiro.
13. `222` e o follow gate estão os dois no CTA, e o CTA de Stories vem **depois** dos dois.
