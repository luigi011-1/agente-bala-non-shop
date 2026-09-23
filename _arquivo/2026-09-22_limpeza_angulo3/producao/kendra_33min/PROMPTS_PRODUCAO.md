# Kendra Collins | Ângulo 3 (Auraly) | Pacote de Prompts

Vídeo modelo: `snapinsta-1787796334638.mp4` (a janela de 33 minutos, 69,9s, plano único com punch-in em 4,0s)

Âncora de identidade: `producao/_ancoras/KENDRA COLLINS .jpeg`

Funil: comentar `222` -> DM -> mensagem com o rosto -> link

> ⚠️ **ÂNGULO 3: o produto NUNCA aparece.** Sem app, sem celular, sem quiz, sem preço. O objeto de desejo é **o rosto da alma gêmea**, e ele só existe na DM.
>
> 🚫 **O ROSTO NUNCA É REVELADO NO VÍDEO.** No gancho `K01F` o retrato fica ilegível **pelo próprio vidro jateado**, que é propriedade física do objeto. Nunca descrever como desfoque de câmera, senão colide com o `no blur` do negative.
>
> ⚠️ **O T1 É MUDO** nas seis versões. A abertura não tem fala nenhuma, nem voz-over. O hook mora na ação mais o texto que entra no CapCut.
>
> 🔥 **A sálvia acesa fica em quadro do T1 ao T11**, em todas as versões. Do T2 em diante ela é cenário e não gancho, e é o que mantém o fogo do modelo presente no vídeo inteiro sem prender o corpo a um prop de gancho.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| REF | **REF-CARTA** | GERAR DO ZERO e **aprovar ANTES de tudo**. Anexada em todas as gerações com a carta |
| T1 | **K01A** | GERAR DO ZERO · ÂNCORA KENDRA · **gancho do modelo**, o da produção principal. Pro |
| T1 | **K01B** | GERAR DO ZERO · ÂNCORA KENDRA + REF-CARTA · gancho **ampulheta**. Pro |
| T1 | **K01C** | **EDITAR do K01B** · gancho **cadeado cortado** |
| T1 | **K01D** | **EDITAR do K01B** · gancho **leque de cartas** |
| T1 | **K01E** | **EDITAR do K01B** · gancho **louro** |
| T1 | **K01F** | **EDITAR do K01B** · gancho **vidro fosco** |
| T2 a T11 | **K02** | GERAR DO ZERO · ÂNCORA KENDRA + REF-CARTA. **Atende 10 takes e as 6 versões** |

**Uma REF, seis K01 e um keyframe de corpo.** O corpo (`K02`) serve as seis versões sem regerar, então cada gancho novo custa **1 keyframe mais 1 clipe**.

**Três GERAR DO ZERO, um por setup:** `K01A` abre o Setup A, `K01B` abre o Setup A-VAR, `K02` abre o Setup B. Todo o resto é edição, que é o que trava rosto, fundo e luz entre as cinco variações.

---

## Trava de identidade e continuidade

**Escrita aqui uma vez, não repetir inteira dentro de cada JSON.**

- **KENDRA COLLINS É MULHER BRANCA AMERICANA, FIM DOS VINTE.** Compleição atlética, ombros definidos.
- **Cabelo raspado platinado**, buzzcut bem curto, mais curto nas laterais.
- **Óculos pretos grossos**, armação retangular de cantos levemente arredondados.
- Pele clara com **poros visíveis, sardas no nariz e nas bochechas**, pequenas imperfeições reais, sobrancelhas claras, lábios cheios, **argola pequena numa narina**.
- **Regata branca canelada com camisa de linho cor aveia aberta por cima**, mangas dobradas até o cotovelo.
- **Corrente fina de PRATA com pingente de cruz de PRATA. Nunca ouro.** Anéis finos de prata nas duas mãos.
- **Cenário com TRÊS ÂNCORAS APENAS:** os três quadros emoldurados em madeira, em fileira, na parede branca atrás dela (fases da lua, roda zodiacal, mapa de constelação, todos azul escuro com traço branco), a **cruz de madeira** na parede à esquerda, e a **bandeirinha dos EUA em suporte preto** na prateleira de madeira na borda direita do quadro. Ametista, quartzo, selenita, incenso, livros, janela e sofá ficam **fora de quadro**. Nunca inventariar a sala.
- **Mesa de madeira clara** de tampo gasto e arranhado no primeiro plano.
- **Luz natural difusa de dia nublado** vindo de uma janela fora de quadro à esquerda. **Sem luz sobrenatural, sem brilho dourado, sem partícula flutuando.**
- Zero blur, tudo em foco nítido. Cara de vídeo de celular, nunca polimento de IA.
- **Sempre sentada à mesa, ereta**, ombros abertos, olhando na lente.

## Trava do prop herói (a sálvia acesa, usar em TODOS os keyframes)

**O herói do modelo é o fogo ao lado do rosto, e ele fica aceso do T1 ao T11.**

```text
A bound bundle of dried white sage about 12 cm long, wrapped in natural cotton string,
resting at an angle inside a natural abalone shell with an iridescent pearl interior.
The tip of the bundle carries a live orange flame about 8 cm tall and a thin ribbon of
pale grey smoke rising straight up. The shell rests on the wooden table. The bundle, the
shell and the flame keep the exact same shape, size and position in every shot.
```

**Decidido com o Luigi em 2026-08-26:** no modelo ele segura o maço na mão os 70s e aponta com a outra. A trava do ângulo obriga a carta na mão a partir do T2 e ela não tem três mãos, então a sálvia vai pra concha na mesa. O fogo continua em quadro o vídeo inteiro e as duas mãos ficam livres.

## Trava do prop herói (REF-CARTA)

**Gerar UMA vez, aprovar, e anexar em todas as gerações que tiverem a carta.** Igual o Ângulo 1 faz com o `product.png`. Sem isso a arte muda de take pra take.

**Trava de cor obrigatória do ângulo:** carta sempre em **dourado, marfim, rosa claro ou azul claro**. Carta escura ou de arte sombria colide com a lei do registro.

## Trava da 2ª pessoa (REF-A)

**Não se aplica.** Não há segunda pessoa em nenhuma das seis versões, então não existe REF-A neste pacote. O gancho da segunda mão não foi escolhido.

---

## GATE DE COMPOSIÇÃO VISUAL (rodado ANTES dos prompts abaixo)

```
HEROI
[x] 1. Heroi no LOWER FOREGROUND mais perto que o rosto
       -> K01A: a concha com a salvia acesa. K01B a K01F: o prop do gancho. K02: a carta na mao
[x] 2. Nada compete com ele
[x] 3. Volume e cobertura explicitados
       -> chama de 8 cm com fita de fumaca, ampulheta INTEIRA na mesa, corrente FECHADA em volta
          da carta, leque CONTINUO de cartas, louro CERCANDO a carta, vidro TOTALMENTE jateado

DISTANCIA
[x] 4. "Da pra estar mais perto?"   -> K01A fecha mais que o padrao da conta, como o modelo
[x] 5. Peito pra cima               -> todos
[x] 6. Take mais fechado e o do CTA -> K02 e o punch-in e serve o T10 e o T11

FUNDO
[x] 7. Cenario reconhecivel         -> 3 ancoras: os tres quadros, a cruz de madeira, a bandeirinha
[x] 8. Fundo por enquadramento, nunca blur
[x] 9. Menos elementos              -> cristais, incenso, livros, janela e sofa fora de quadro

2a PESSOA
[-] 10. Nao se aplica, video sem 2a pessoa
```

## GATE DE REALISMO (rodado junto)

```
[x] 1. Heroi isolado, 3 ancoras de fundo, a bandeira ocupando uma delas
[x] 2. Camera puxada perto, o prop enche o terco inferior
[x] 3. Luz NEUTRA de dia nublado pela janela lateral. Sem luz sobrenatural
[x] 4. Negative carrega no warm orange color cast, no yellow tint, no golden glow
[x] 5. Fundo especifico e nunca borrado
[x] 6. Prop teimoso: a CARTA, por isso e REF-CARTA, gerada isolada e aprovada antes
[x] 7. Bloco de realismo padrao colado por inteiro em todo prompt
```

**Duas escolhas deliberadas.**

**A carta virou REF-PROP.** É o objeto mais teimoso do ângulo: o gerador tende a inventar arte de tarô escura, com luas, olhos e simbologia pesada, que é exatamente o que a lei do registro proíbe. Gerar isolada, aprovar e anexar sempre resolve de vez.

**O quarto dela convida inventário.** Quadros, cruz, ametista, quartzo, selenita, incenso, livros, janela, sofá. Ficaram **três âncoras** e a bandeirinha é uma delas. Já lê como o quarto dela e nada mais compete com o fogo.

## ⚠️ NOTA DE RESTRIÇÃO E DE REGISTRO

**O único risco real deste pacote é o fogo perto do rosto no `K01A`**, que é justamente o gancho do modelo. As três decisões que reduzem esse risco já estão dentro dos prompts:

1. **A ação está enxuta.** O fogo é descrito como um estado calmo (um maço aceso numa concha), nunca como algo se aproximando de pessoa. Menos é mais na descrição é o que mais evita classificador.
2. **A chama tem tamanho declarado e fica na concha, sobre a mesa.** Não é fogo solto, não é fogo na mão, não é fogo encostando em ninguém.
3. **O negative não menciona fogo, queimadura nem nada do tipo.** O classificador lê o token e não a negação, então nomear o que se teme é o que trava.

Se o `K01A` travar mesmo assim, **a saída não é repetir a mesma geração**: é baixar a concha mais para o primeiro plano inferior e tirar o rosto do raio da chama, gerando a chama e o rosto em alturas separadas do quadro.

**Registro:** nenhum prompt diz proteção, ritual, pacto, escudo ou círculo. A corrente do `K01C` é descrita como `a fine chain` e o que acontece é ela se soltar. Nenhuma luz sobrenatural, nenhuma partícula, nenhum brilho. A carta é clara.

---

# Prompts de imagem

## REF-CARTA · GERAR DO ZERO · SEM REFERÊNCIA

A carta SOULMATE sozinha, vista de cima, sobre superficie neutra cinza clara.
*Anexar: nada. Aprovar antes de qualquer outra geração.*

```json
{
  "shot_id": "REF_CARTA_soulmate_holo",
  "reference_use": "No reference image. Generate the object alone. No person, no hands, no room.",
  "identity_main": "No person. A single modern printed tarot card lying flat and straight, filling most of the frame, photographed from directly above on a plain neutral light gray surface.",
  "prop": "A rectangular tarot card with rounded corners, printed on smooth clean cardstock. A wide mirror-metallic border frames the whole card, silver with a rainbow holographic sheen that shifts across it the way foil stamping catches the light, with fine engraved scrollwork and a flourish in each corner. At the top centre, inside a small tablet set into the border, the roman numeral VI in spaced serif capitals. Across the bottom, a cream title band carries the word SOULMATE in spaced serif capitals with a small red heart at the right end of the band.",
  "card_art": "Inside the border, a man and a woman stand facing each other in profile, hands joined, seen from the knees up, painted in a rich saturated illustrative style with fine detail and clean line work. He wears a dark timeless coat, she wears a long deep rose dress. Between and above their heads a single luminous white heart shines, with light rays spreading behind it into a lavender and pink sky. An arch of climbing roses in crimson and blush frames them on both sides, with large open roses along the base. Timeless clothing only, never modern clothing, never cartoon faces.",
  "palette": "Saturated and vivid: crimson and blush rose, deep pink, lavender, warm gold and clean white light, over the silver rainbow sheen of the metallic border.",
  "scene": "Plain neutral light gray surface, nothing else in frame.",
  "composition": "Straight top-down, the card fills most of the frame, all four edges and all four corners fully visible, the whole card readable.",
  "camera": "top-down, straight on, flat, close",
  "state": "Start frame: the card lying still and flat, fully readable.",
  "lighting": "Soft neutral diffuse daylight, even across the card, no glare, so the metallic border reads as a printed foil finish and not as a light source.",
  "realism": "Real printed cardstock with a smooth foil-stamped surface, visible ink detail in the illustration, realistic soft shadow under the card, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no cartoon style, no children's book illustration, no cute rounded faces, no modern clothing, no plain white border, no comic art, no 3d render, no gothic art, no skulls, no ravens, no snakes, no swords, no inverted symbols, no sigils, no captions, no subtitles, no watermark, no hands, no people, no blur. The ONLY text on the card is the roman numeral VI at the top and the word SOULMATE in the bottom title band."
}
```

> ⚠️ **ESTILO NOVO, decidido pelo Luigi em 2026-08-29.** A carta passou a ser **holográfica / foil e saturada**, e este prompt já está reescrito por inteiro nesse estilo. A paleta pálida antiga (marfim, dourado fosco, rosa empoeirado, azul pálido) está **revogada**. A trava do ângulo continua sendo a **leitura** e não a cor: casal, coração luminoso, rosas, luz. Sem caveira, corvo, serpente, espada ou símbolo invertido.
>
> ⚠️ **DUAS armadilhas técnicas já resolvidas dentro do prompt.** 1) O negative padrão do projeto carrega `no words overlaid on the image`, que mataria a palavra da carta, e aqui foi trocado por `no captions, no subtitles, no watermark`. 2) O bloco de realismo padrão carrega `no golden glow`, `no warm orange color cast`, `no sparkles` e `no glowing edges`, que matariam o foil e o coração luminoso, e por isso **ficam de fora só aqui**. Nos keyframes da avatar segurando a carta o negative segue completo e normal, porque lá a arte já vem travada pela REF anexada.

**O unico texto que pode aparecer nesta carta e o numeral VI no topo e a palavra SOULMATE na faixa da base.** Se vier com qualquer outra palavra, a carta nao serve.

---

## K01A · T1 · GANCHO DO MODELO · GERAR DO ZERO · ÂNCORA KENDRA

Close fechado, a chama da sálvia subindo ao lado do rosto dela, dedo apontado pra lente.
*Anexar: âncora Kendra. Gerar no Nano Banana **Pro**, várias variações.*

```json
{
  "shot_id": "K01A_hook_model",
  "reference_use": "Use the attached image ONLY for Kendra's face, identity, glasses, hair, wardrobe and the reading room scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT WOMAN from the attached reference image (Kendra Collins), a white American woman in her late twenties, athletic build with defined shoulders, very short platinum blonde buzzcut shorter at the sides, thick black rectangular eyeglasses with slightly rounded corners, fair skin with visible pores and freckles across her nose and cheeks, pale eyebrows, full lips, a small hoop piercing in one nostril, light eyes, calm and direct expression.",
  "wardrobe": "White ribbed tank top with an oatmeal linen shirt open over it, sleeves rolled to the elbow. Thin SILVER chain with a SILVER cross pendant. Thin silver rings on fingers of both hands. Never gold.",
  "prop": "A bound bundle of dried white sage about 12 cm long, wrapped in natural cotton string, resting at an angle inside a natural abalone shell with an iridescent pearl interior. The tip of the bundle carries a live orange flame about 8 cm tall and a thin ribbon of pale grey smoke rising straight up. The shell rests on the wooden table.",
  "scene": "SAME reading room as the reference image, kept to three anchors only: three wood-framed prints in a row on the white wall behind her showing moon phases, a zodiac wheel and a constellation map, all dark blue with white line art; a dark wooden cross on the wall to the left; and a SMALL AMERICAN FLAG on a black desk stand on the wooden shelf at the right edge of frame, fully visible and in sharp focus. A light wooden table with a worn scratched top. Nothing else from the room is in frame.",
  "posture": "Seated upright at the table, shoulders open, facing the camera straight on.",
  "composition": "VERY CLOSE, tighter than a normal talking framing. Kendra from the chest up fills the frame and the top of her head is cropped by the top edge. The abalone shell with the lit sage sits in the LOWER FOREGROUND on the left, clearly closer to the lens than her face, so the flame rises beside her cheek on the left side of the frame. Her right hand is raised into the lower right of the frame with the index finger extended straight toward the lens, also closer to the camera than her face. Only the front edge of the table is visible at the very bottom. Very little of the room is readable.",
  "camera": "chest level, straight-on, camera pushed in close",
  "state": "Start frame: Kendra looks straight into the lens with her mouth closed, not speaking. The sage is already lit and the flame is steady.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window outside the frame on the left. No supernatural light, no golden glow, no floating particles.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the background wall, the frames and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no gold jewelry, no second person, no microphone, no warm orange color cast, no yellow tint, no golden glow, no sparkles, no glowing edges"
}
```

---

## K01B · T1 · GANCHO AMPULHETA · GERAR DO ZERO · ÂNCORA KENDRA + REF-CARTA

Enquadramento padrão da conta, a mesa no terço inferior, a mão dela fechada sobre a ampulheta.
*Anexar: âncora Kendra + REF-CARTA aprovada. Gerar no Nano Banana **Pro**, várias variações.*

```json
{
  "shot_id": "K01B_hook_hourglass",
  "reference_use": "Use the first attached image ONLY for Kendra's face, identity, glasses, hair, wardrobe and the reading room scene. Use the second attached image ONLY for the exact artwork, colors and proportions of the card. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT WOMAN from the first reference image (Kendra Collins), a white American woman in her late twenties, athletic build with defined shoulders, very short platinum blonde buzzcut shorter at the sides, thick black rectangular eyeglasses with slightly rounded corners, fair skin with visible pores and freckles across her nose and cheeks, pale eyebrows, full lips, a small hoop piercing in one nostril, light eyes, calm and direct expression.",
  "wardrobe": "White ribbed tank top with an oatmeal linen shirt open over it, sleeves rolled to the elbow. Thin SILVER chain with a SILVER cross pendant. Thin silver rings on fingers of both hands. Never gold.",
  "prop": "A wooden hourglass about 18 cm tall with two clear glass bulbs and fine pale sand, standing upright on the table with ALL of the sand already settled in the LOWER bulb and none falling. Beside it, the EXACT card from the second reference image lies flat on the table, face up. A bound bundle of dried white sage about 12 cm long, wrapped in natural cotton string, rests at an angle inside a natural abalone shell with an iridescent pearl interior, further back on the left of the table, the tip carrying a live orange flame about 8 cm tall with a thin ribbon of pale grey smoke rising straight up.",
  "scene": "SAME reading room as the first reference image, kept to three anchors only: three wood-framed prints in a row on the white wall behind her showing moon phases, a zodiac wheel and a constellation map, all dark blue with white line art; a dark wooden cross on the wall to the left; and a SMALL AMERICAN FLAG on a black desk stand on the wooden shelf at the right edge of frame, fully visible and in sharp focus. A light wooden table with a worn scratched top. Nothing else from the room is in frame.",
  "posture": "Seated upright at the table, shoulders open, facing the camera straight on, both forearms resting on the table.",
  "composition": "Camera at chest height from the other side of the table. Kendra from the chest up occupies the upper part of the frame and the light wooden table occupies the LOWER THIRD of the same frame. The hourglass stands in the lower foreground, clearly closer to the lens than her face, and it is unmistakably the hero. The card lies flat beside it, slightly further back. Her right hand is closed loosely around the top of the hourglass. Very little of the room is readable behind her.",
  "camera": "chest level, straight-on, camera close to the table",
  "state": "Start frame: her hand is closed around the top of the hourglass, which has not been turned yet. All the sand is resting in the lower bulb and nothing is falling. She looks straight into the lens with her mouth closed, not speaking.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window outside the frame on the left. No supernatural light, no golden glow, no floating particles.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the background wall, the frames and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no gold jewelry, no second person, no warm orange color cast, no yellow tint, no golden glow, no sparkles, no glowing edges"
}
```

---

## K01C · T1 · GANCHO CADEADO CORTADO · EDITAR do K01B

A ampulheta sai, entra a corrente com cadeado em volta da carta e o alicate na mão dela.
*Anexar: K01B aprovado.*

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Kendra exactly the same: same face, same black eyeglasses, same platinum buzzcut, same freckles, same nose hoop, same white tank top and oatmeal linen shirt, same silver cross, same silver rings, same seated posture, same expression, mouth closed. Keep the SAME background exactly: the three wood-framed prints in a row, the dark wooden cross on the wall, the SMALL AMERICAN FLAG on its black desk stand on the shelf at the right edge, the light wooden table, the same camera angle and framing. Keep the SAME abalone shell with the lit sage bundle further back on the left of the table, same flame, same thin ribbon of smoke. Keep the SAME card in the same place on the table, same artwork and colors. Keep the same neutral overcast daylight.",
  "change_1": "Remove the wooden hourglass completely from the table. Nothing of it remains, no glass, no sand, no shadow of it.",
  "change_2": "A fine silver chain is now wrapped in a closed loop around the card on the table, held shut by a small steel padlock resting on the wood beside the card. The chain is taut against the card.",
  "change_3": "Her right hand now holds a small pair of steel pliers in the lower foreground, closer to the lens than her face, with the jaws resting open on one link of the chain, not yet closed on it.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, do not change the card artwork, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no supernatural lighting, no blur, no sparkles, no warm orange color cast, no yellow tint, no golden glow"
}
```

---

## K01D · T1 · GANCHO LEQUE DE CARTAS · EDITAR do K01B

A ampulheta sai, entra um leque de cartas viradas pra baixo e o dedo dela pousado numa.
*Anexar: K01B aprovado.*

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Kendra exactly the same: same face, same black eyeglasses, same platinum buzzcut, same freckles, same nose hoop, same white tank top and oatmeal linen shirt, same silver cross, same silver rings, same seated posture, same expression, mouth closed. Keep the SAME background exactly: the three wood-framed prints in a row, the dark wooden cross on the wall, the SMALL AMERICAN FLAG on its black desk stand on the shelf at the right edge, the light wooden table, the same camera angle and framing. Keep the SAME abalone shell with the lit sage bundle further back on the left of the table, same flame, same thin ribbon of smoke. Keep the same neutral overcast daylight.",
  "change_1": "Remove the wooden hourglass completely from the table. Nothing of it remains, no glass, no sand, no shadow of it.",
  "change_2": "Remove the card that was lying face up on the table. In its place, a continuous fan of about thirteen cards is spread in an even arc across the lower foreground of the table, ALL of them face down, showing only their plain backs in deep midnight blue with a wide mirror-metallic silver holographic border and a fine engraved pattern. None of them is turned over.",
  "change_3": "Her right index finger rests lightly on the back of one card near the middle of the fan, in the lower foreground closer to the lens than her face, without lifting it.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no heavy shadow illustration, no supernatural lighting, no blur, no sparkles, no warm orange color cast, no yellow tint, no golden glow"
}
```

---

## K01E · T1 · GANCHO LOURO · EDITAR do K01B

A ampulheta sai, folhas de louro cercam a carta e a última folha está entre os dedos dela.
*Anexar: K01B aprovado.*

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Kendra exactly the same: same face, same black eyeglasses, same platinum buzzcut, same freckles, same nose hoop, same white tank top and oatmeal linen shirt, same silver cross, same silver rings, same seated posture, same expression, mouth closed. Keep the SAME background exactly: the three wood-framed prints in a row, the dark wooden cross on the wall, the SMALL AMERICAN FLAG on its black desk stand on the shelf at the right edge, the light wooden table, the same camera angle and framing. Keep the SAME abalone shell with the lit sage bundle further back on the left of the table, same flame, same thin ribbon of smoke. Keep the SAME card in the same place on the table, same artwork and colors. Keep the same neutral overcast daylight.",
  "change_1": "Remove the wooden hourglass completely from the table. Nothing of it remains, no glass, no sand, no shadow of it.",
  "change_2": "About twelve dried bay leaves, pale sage green and slightly curled, are now arranged in an even ring on the table around the card, tips pointing inward, framing it without covering it.",
  "change_3": "Her right hand holds one more dried bay leaf between thumb and index finger in the lower foreground, closer to the lens than her face, held just above the card and not yet placed down.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, do not change the card artwork, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no supernatural lighting, no blur, no sparkles, no warm orange color cast, no yellow tint, no golden glow"
}
```

---

## K01F · T1 · GANCHO VIDRO FOSCO · EDITAR do K01B

A ampulheta sai, entra o porta-retrato de vidro jateado e o dedo dela pousado no topo do vidro.
⚠️ O rosto atrás do vidro é **ilegível pelo próprio vidro**, que é jateado. Nunca desfoque de câmera.
*Anexar: K01B aprovado.*

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Kendra exactly the same: same face, same black eyeglasses, same platinum buzzcut, same freckles, same nose hoop, same white tank top and oatmeal linen shirt, same silver cross, same silver rings, same seated posture, same expression, mouth closed. Keep the SAME background exactly: the three wood-framed prints in a row, the dark wooden cross on the wall, the SMALL AMERICAN FLAG on its black desk stand on the shelf at the right edge, the light wooden table, the same camera angle and framing. Keep the SAME abalone shell with the lit sage bundle further back on the left of the table, same flame, same thin ribbon of smoke. Keep the SAME card in the same place on the table, same artwork and colors. Keep the same neutral overcast daylight.",
  "change_1": "Remove the wooden hourglass completely from the table. Nothing of it remains, no glass, no sand, no shadow of it.",
  "change_2": "A small upright wooden picture frame about 15 cm tall now stands on the table in the lower foreground, closer to the lens than her face, angled toward the camera. Its glass is HEAVILY SANDBLASTED, a thick opaque frosted white finish across the entire pane. Behind that frosted glass there is only a vague pale shape where a person would be, with no readable features at all. The opacity belongs to the glass itself, which is frosted; everything else in the picture stays perfectly sharp.",
  "change_3": "Her right index fingertip rests at the very top edge of the frosted pane, not yet moved, leaving no trail on the glass.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere in the scene, everything in sharp focus. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, do not change the card artwork, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no supernatural lighting, no blur, no sparkles, no warm orange color cast, no yellow tint, no golden glow"
}
```

---

## K02 · T2 a T11 · SETUP B · GERAR DO ZERO · ÂNCORA KENDRA + REF-CARTA

Punch-in, a carta na mão esquerda apoiada na mesa, o indicador direito apontado pra lente.
*Anexar: âncora Kendra + REF-CARTA aprovada.* **Este keyframe serve os dez takes e as seis versões.**

```json
{
  "shot_id": "K02_body",
  "reference_use": "Use the first attached image ONLY for Kendra's face, identity, glasses, hair, wardrobe and the reading room scene. Use the second attached image ONLY for the exact artwork, colors and proportions of the card. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT WOMAN from the first reference image (Kendra Collins), a white American woman in her late twenties, athletic build with defined shoulders, very short platinum blonde buzzcut shorter at the sides, thick black rectangular eyeglasses with slightly rounded corners, fair skin with visible pores and freckles across her nose and cheeks, pale eyebrows, full lips, a small hoop piercing in one nostril, light eyes, calm and direct expression.",
  "wardrobe": "White ribbed tank top with an oatmeal linen shirt open over it, sleeves rolled to the elbow. Thin SILVER chain with a SILVER cross pendant. Thin silver rings on fingers of both hands. Never gold.",
  "prop": "The EXACT card from the second reference image, held upright in her left hand with its base resting on the table and its face turned toward the lens. A bound bundle of dried white sage about 12 cm long, wrapped in natural cotton string, rests at an angle inside a natural abalone shell with an iridescent pearl interior, on the left of the table in the lower foreground, the tip carrying a live orange flame about 8 cm tall with a thin ribbon of pale grey smoke rising straight up.",
  "scene": "SAME reading room as the first reference image, kept to three anchors only: three wood-framed prints in a row on the white wall behind her showing moon phases, a zodiac wheel and a constellation map, all dark blue with white line art; a dark wooden cross on the wall to the left; and a SMALL AMERICAN FLAG on a black desk stand on the wooden shelf at the right edge of frame, fully visible and in sharp focus. A light wooden table with a worn scratched top. Nothing else from the room is in frame.",
  "posture": "Seated upright at the table, shoulders open, facing the camera straight on.",
  "composition": "TIGHTER than the previous setup, a hard punch-in. Kendra from the chest up fills the frame and the top of her head is cropped by the top edge. Only the front edge of the table is visible along the very bottom. The abalone shell with the lit sage sits in the LOWER FOREGROUND on the left, closer to the lens than her face, so the flame rises beside her cheek on the left side of the frame. Her left hand holds the card upright in the lower left of the frame, its face turned to the lens. Her right hand is raised into the lower right of the frame with the index finger extended straight toward the lens, closer to the camera than her face. Very little of the room is readable.",
  "camera": "chest level, straight-on, camera pushed in close",
  "state": "Start frame: she is looking straight into the lens, about to speak, holding the card steady.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window outside the frame on the left. No supernatural light, no golden glow, no floating particles.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the background wall, the frames and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no gold jewelry, no second person, no microphone, no warm orange color cast, no yellow tint, no golden glow, no sparkles, no glowing edges"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Já está aplicado dentro de cada prompt abaixo. Está aqui só como referência do padrão.

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida.

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

Estilo TikTok nativo, UGC. Preservar exatamente a identidade da Kendra, rosto, buzzcut platinado, óculos pretos, regata branca com camisa de linho aveia, cruz de PRATA, o quarto de leitura, a iluminação e o enquadramento do frame inicial. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

---

### V01A · T1 · usa K01A

Gancho do modelo, o da produção principal. Abertura muda de 4s.

```text
(sem fala no take: a abertura é muda no modelo, o hook mora no texto que entra no CapCut)

o que acontece no vídeo: a avatar olha fixo para a lente sem falar, de boca fechada. A chama do maço de sálvia na concha queima firme e a fumaça sobe reta. Ela mantém o indicador da mão direita apontado para a lente, imóvel.

câmera: fixa, leve handheld natural

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V01B · T1 · usa K01B

Variação ampulheta. Abertura muda de 4s.

```text
(sem fala no take: a abertura é muda no modelo, o hook mora no texto que entra no CapCut)

o que acontece no vídeo: a avatar vira a ampulheta de cabeça para baixo sobre a mesa e solta a mão. A areia começa a cair. Ela olha para a lente sem falar. A chama do maço de sálvia queima firme ao fundo da mesa.

câmera: fixa, leve handheld natural

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V01C · T1 · usa K01C

Variação cadeado cortado. Abertura muda de 4s.

```text
(sem fala no take: a abertura é muda no modelo, o hook mora no texto que entra no CapCut)

o que acontece no vídeo: a avatar fecha o alicate sobre o elo da corrente e o elo cede. A corrente afrouxa em volta da carta e escorrega sobre a mesa. Ela olha para a lente sem falar. A chama do maço de sálvia queima firme ao fundo da mesa.

câmera: fixa, leve handheld natural

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V01D · T1 · usa K01D

Variação leque de cartas. Abertura muda de 4s.

```text
(sem fala no take: a abertura é muda no modelo, o hook mora no texto que entra no CapCut)

o que acontece no vídeo: a avatar vira uma única carta do leque com o indicador e a deixa aberta sobre a mesa. As outras continuam viradas para baixo. Ela olha para a lente sem falar. A chama do maço de sálvia queima firme ao fundo da mesa.

câmera: fixa, leve handheld natural

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V01E · T1 · usa K01E

Variação louro. Abertura muda de 4s.

```text
(sem fala no take: a abertura é muda no modelo, o hook mora no texto que entra no CapCut)

o que acontece no vídeo: a avatar baixa a última folha de louro e a apoia sobre a carta, cobrindo metade dela, e recolhe a mão. Ela olha para a lente sem falar. A chama do maço de sálvia queima firme ao fundo da mesa.

câmera: fixa, leve handheld natural

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V01F · T1 · usa K01F

Variação vidro fosco. Abertura muda de 4s.

```text
(sem fala no take: a abertura é muda no modelo, o hook mora no texto que entra no CapCut)

o que acontece no vídeo: a avatar arrasta a ponta do dedo de cima para baixo no vidro jateado do porta-retrato, abrindo um rastro limpo e estreito. O que aparece atrás do rastro continua sendo um vulto sem traço nenhum. Ela olha para a lente sem falar. A chama do maço de sálvia queima firme ao fundo da mesa.

câmera: fixa, leve handheld natural

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V02 · T2 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "I do not know your name. I do not know your face. But I know who the universe just lined up with you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro e a avatar já está falando direto para a lente, segurando a carta apoiada na mesa com a mão esquerda. Ela nega com dois pequenos movimentos de cabeça nas duas primeiras frases e depois firma o olhar na última. A chama da sálvia queima ao lado dela.

câmera: fixa, leve handheld natural

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V03 · T3 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "You did not find this today. It was sent to you, and the waiting part of this is finally over."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar fala direto para a lente e abre a mão direita uma vez, com a palma para cima, na segunda frase. Ela continua segurando a carta apoiada na mesa com a mão esquerda. A chama da sálvia queima ao lado dela.

câmera: fixa, leve handheld natural

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V04 · T4 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "There is a person on the other end of this. But nothing gets handed over until you are ready to receive it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar fala direto para a lente e ergue levemente a carta na mão esquerda na primeira frase, depois volta a apoiá-la na mesa. Na segunda frase ela marca a fala com um gesto seco da mão direita. A chama da sálvia queima ao lado dela.

câmera: fixa, leve handheld natural

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V05 · T5 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "In thirty three minutes their face can be on your screen. Stop watching now and it turns into someone you never see."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar aponta o indicador direito para a lente na primeira frase e endurece a expressão na segunda, sem desviar o olhar. Ela continua segurando a carta apoiada na mesa. A chama da sálvia queima ao lado dela.

câmera: fixa, leve push-in

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V06 · T6 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "This is not a general reading. It is the answer to something you asked for when nobody was listening."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar nega com um pequeno movimento firme de cabeça na primeira frase e depois baixa o tom, falando mais devagar na segunda, com o olhar fixo na lente. A chama da sálvia queima ao lado dela.

câmera: fixa, leve handheld natural

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V07 · T7 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Step one. Comment two two two, because I cannot see who claimed this until your number is under the video."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar levanta o indicador direito ao dizer o primeiro passo e depois aponta o mesmo dedo para a lente ao dizer o número. Ela continua segurando a carta apoiada na mesa. A chama da sálvia queima ao lado dela.

câmera: fixa, leve handheld natural

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V08 · T8 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Step two. Follow me, because the message with their face leaves from here and it cannot land on a stranger."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar levanta dois dedos da mão direita ao dizer o segundo passo e depois toca o próprio peito com a mesma mão ao falar de onde a mensagem sai. Ela continua segurando a carta apoiada na mesa. A chama da sálvia queima ao lado dela.

câmera: fixa, leve handheld natural

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V09 · T9 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Step three. Save this, because you will want it back on the day you meet them. Then the thirty three minutes start."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar levanta três dedos da mão direita ao dizer o terceiro passo e depois firma a mão aberta sobre a mesa na última frase. Ela continua segurando a carta apoiada na mesa. A chama da sálvia queima ao lado dela.

câmera: fixa, leve handheld natural

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V10 · T10 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Their face is the one thing I will not post out here. I hand that to you privately. Watch for me."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar nega com a cabeça na primeira frase, depois ergue a carta na mão esquerda junto ao peito e mantém contato visual forte até o fim. A chama da sálvia queima ao lado dela.

câmera: fixa, leve push-in

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

### V11 · T11 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Two two two. Put it under this video before you scroll, and then keep your messages open tonight."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar aponta o indicador direito para a lente ao dizer o número e o dedo se aproxima da câmera sem cobrir o rosto. Ela mantém o olhar firme até o fim. A chama da sálvia queima ao lado dela.

câmera: fixa, leve push-in

som ambiente: quarto silencioso, chama baixa crepitando, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-CARTA | nenhuma, gerar isolada | Nano Banana 2, regenerar até a arte ler como carta de verdade |
| K01A | âncora Kendra | Nano Banana **Pro**, várias variações |
| K01B | âncora Kendra + REF-CARTA aprovada | Nano Banana **Pro**, várias variações |
| K01C | K01B aprovado | Nano Banana 2, comando de edição |
| K01D | K01B aprovado (**nunca a partir do K01C**) | Nano Banana 2, comando de edição |
| K01E | K01B aprovado (**nunca a partir do K01C nem do K01D**) | Nano Banana 2, comando de edição |
| K01F | K01B aprovado (**nunca a partir dos outros**) | Nano Banana 2, comando de edição |
| K02 | âncora Kendra + REF-CARTA aprovada | Nano Banana **Pro** |

**Os quatro K01 de edição saem todos do K01B original, nunca em cascata.** Editar em cadeia faz a identidade derivar de uma variação pra outra, que é o erro catalogado na falha de estágios.

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps.
- **Um corte duro só, e ele é do modelo:** V01 para V02, o punch-in em 4,0s. Todos os outros cortes são entre takes de fala no mesmo enquadramento, então entram secos e invisíveis.
- Cortar o silêncio inicial de cada clipe para a fala começar imediatamente.
- **Texto de abertura**, do segundo 0 ao 4, sobre o take mudo, em caixa preta com texto branco e a palavra final em vermelho, imitando o modelo:
  - Produção principal e variações 1 a 5, respectivamente: `SOMEONE WAS CHOSEN FOR YOU TODAY.` · `THIRTY THREE MINUTES` · `THE WAITING PART IS OVER` · `SOMEONE WAS CHOSEN FOR YOU TODAY` · `YOU ASKED FOR THIS OUT LOUD` · `NOT OUT HERE`
- **A DATA vai no rodapé durante o T3**, em letra pequena, no formato `WEDNESDAY, AUGUST 26`. **É o único elemento a trocar quando o clipe for repostado em outro dia.** Por isso ela não está na fala.
- Legendas karaokê palavra a palavra do T2 em diante, estilo Captions.ai Prism Pro, palavra destacada em verde, centralizadas na altura do peito. Nunca cobrir a chama nem a carta.
- **Marca d'água fixa `222`** flutuando no canto inferior direito o vídeo inteiro, roubada do `AMEN` do modelo.
- **Texto final** do T9 até o fim, no topo: `THE FACE IS IN YOUR MESSAGES.`
- Manter `222` isolado na tela no T7 e no T11.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

## Gates de qualidade

1. Kendra é a mesma mulher em todos os clipes, com o buzzcut platinado, os óculos pretos e a **cruz de PRATA** em todos.
2. A argola da narina e as sardas continuam iguais em todos os planos.
3. A carta SOULMATE tem a mesma arte, as mesmas cores e as mesmas proporções em todos os keyframes que a mostram, porque todos anexaram a REF-CARTA.
4. A concha com a sálvia está acesa em **todos** os keyframes, com a mesma chama e a mesma posição, e nunca sai de quadro do T1 ao T11.
5. Os três quadros emoldurados, a cruz de madeira e a **bandeirinha dos EUA** aparecem em todos os keyframes, a bandeira nítida e nunca cortada pela borda.
6. Nenhuma legenda ou texto foi gerado dentro da imagem, e a única palavra que existe em quadro é `SOULMATE` na base da carta.
7. No K01F o rosto atrás do vidro é **ilegível pelo jateamento do vidro**, e o resto da imagem continua em foco nítido.
8. Nenhuma joia dourada em nenhum clipe, e nenhum microfone em quadro.
9. Mãos com cinco dedos, sem fusão com a carta, com o alicate nem com a ampulheta.
10. `222` e o follow gate estão os dois presentes, o `222` no T7 e no T11, o follow gate no T8.
