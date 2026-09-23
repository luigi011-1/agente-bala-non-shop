# Kendra Collins | Ângulo 3 (Auraly) | Pacote de Prompts

Vídeo modelo: `snapinsta-1787767048118.mp4` (círculo de sal e os três selos, 50,5s, abertura muda)

Âncora de identidade: `producao/_ancoras/KENDRA COLLINS .jpeg`

Funil: comentar `222` -> DM -> mensagem com o rosto -> link do quiz

> ⚠️ **ÂNGULO 3: o produto NUNCA aparece.** Sem app, sem celular, sem quiz, sem preço. O objeto de desejo é **o rosto da alma gêmea**, e ele só existe na DM.
>
> 🚫 **O ROSTO NUNCA É REVELADO NO VÍDEO.** No gancho B o retrato fica ilegível **pelo próprio gelo**, que é propriedade física do objeto. Nunca descrever como blur de câmera, senão colide com o `no blur` do negative.
>
> ⚠️ **O T1 É MUDO.** A abertura não tem fala em nenhuma das cinco variações. O hook mora no texto que entra no CapCut.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| REF | **REF-CARTA** | GERAR DO ZERO e **aprovar ANTES de tudo**. Anexada em todas as gerações seguintes |
| T1 | **K01A** | GERAR DO ZERO · âncora Kendra + REF-CARTA · gancho **vela**. Pro |
| T1 | **K01B** | GERAR DO ZERO · âncora Kendra · gancho **gelo**. Pro |
| T1 | **K01C** | GERAR DO ZERO · âncora Kendra + REF-CARTA · gancho **mel**. Pro |
| T1 | **K01D** | GERAR DO ZERO · âncora Kendra + REF-CARTA · gancho **terra**. Pro |
| T1 | **K01E** | GERAR DO ZERO · âncora Kendra · gancho **espelho**. Pro |
| T2 a T10 | **K02** | GERAR DO ZERO · âncora Kendra + REF-CARTA. **Atende 9 takes e as 5 variações** |
| T11, T12 | **K03** | **EDITAR do K02** (fecha o plano, a carta sobe junto ao peito) |

**Uma REF, cinco K01 e dois keyframes de corpo.** O corpo inteiro (K02 e K03) **serve as cinco variações sem regerar**, então cada gancho novo custa **1 keyframe + 1 clipe**.

---

## Trava de identidade e continuidade

**Escrita aqui uma vez, não repetir inteira dentro de cada JSON.**

- **KENDRA COLLINS É MULHER.** Mulher negra americana, uns sessenta anos, pele marrom média com sardas visíveis nas maçãs do rosto e no nariz, linhas de expressão reais.
- **Cabelo grisalho raspado bem curto**, quase colado à cabeça.
- **Brincos ovais grandes, brancos foscos**, um em cada orelha.
- **Vestido de linho terracota** de alças largas e decote quadrado.
- **Corrente fina de PRATA com pingente pequeno de cruz de PRATA.** Nunca ouro.
- **Pulseiras de miçangas coloridas no punho esquerdo** e **aliança de prata lisa** no anelar direito.
- **Cenário: a sala dela, com DUAS âncoras visuais apenas: a cruz de madeira escura na parede bege atrás dela e a prateleira de livros de lombada ROXA.** Os potes de ervas, os cristais, a bandeira de mesa, as velas e o sofá ficam **fora de quadro**. Nunca inventariar a sala.
- **Mesa de madeira clara** ocupando o terço inferior do quadro.
- **Luz natural difusa de dia nublado** vindo da janela lateral fora de quadro. **Sem luz sobrenatural, sem brilho dourado, sem partícula flutuando.**
- Zero blur, tudo em foco nítido. Cara de vídeo de celular, nunca polimento de IA.
- **Sempre sentada à mesa, ereta**, ombros abertos, olhando na lente.

## Trava do prop herói (REF-CARTA)

**Gerar UMA vez, aprovar, e anexar em todas as gerações que tiverem a carta.** Igual o Ângulo 1 faz com o `product.png`.

```text
A single illustrated tarot-style card, about 12 by 20 cm, portrait orientation, printed on
thick matte cardstock with slightly worn edges. The illustration shows a couple embracing,
drawn in clean warm line art. The word SOULMATE is printed in small capital letters along the
bottom edge. Palette is PALE and LIGHT ONLY: cream, soft gold, pale blush pink and light blue.
No dark card, no black, no heavy shadow art.
```

**Trava de cor obrigatória do ângulo:** cartas sempre em **dourado, branco, rosa claro ou azul claro**. Carta escura ou de arte sombria colide com a lei do registro.

**Não há 2ª pessoa neste vídeo, então não há REF-A.**

---

## GATE DE COMPOSIÇÃO VISUAL (rodado ANTES dos prompts abaixo)

```
HEROI
[x] 1. Heroi no LOWER FOREGROUND mais perto que o rosto
       -> K01A a K01E: o prop do gancho. K02/K03: a carta na mao
[x] 2. Nada compete com ele
[x] 3. Volume e cobertura explicitados
       -> anel de sal FECHADO e continuo, bloco de gelo GROSSO, fio de mel CONTINUO,
          monte de terra ALTO, espelho TOTALMENTE embacado

DISTANCIA
[x] 4. "Da pra estar mais perto?"   -> todos fecham mais que o original
[x] 5. Peito pra cima               -> K02 e K03
[x] 6. Take mais fechado e o do CTA -> K03

FUNDO
[x] 7. Cenario reconhecivel         -> 2 ancoras: a cruz de madeira e os livros de lombada roxa
[x] 8. Fundo por enquadramento, nunca blur
[x] 9. Menos elementos

2a PESSOA
[-] 10. Nao se aplica, video sem 2a pessoa
```

## GATE DE REALISMO (rodado junto)

```
[x] 1. Heroi isolado, 2 ancoras de fundo
[x] 2. Camera puxada perto, o prop enche o terco inferior
[x] 3. Luz NEUTRA de dia nublado pela janela. Sem luz sobrenatural
[x] 4. Negative carrega no warm orange color cast, no yellow tint, no golden glow
[x] 5. Fundo especifico e nunca borrado
[x] 6. Prop teimoso: a CARTA. Por isso ela e REF-CARTA, gerada isolada e aprovada antes
[x] 7. Bloco de realismo padrao colado por inteiro em todo prompt
```

**Duas escolhas deliberadas.**

**A carta virou REF-PROP.** É o objeto mais teimoso do ângulo: a IA tende a inventar arte de tarô escura, com luas, olhos e simbologia pesada, que é exatamente o que a lei do registro proíbe. Gerar isolada, aprovar, e anexar sempre resolve de vez, e é o item 6 do gate de realismo.

**A sala dela convida inventário.** Potes de ervas, cristais, geodos, velas, bandeira, sofá, janela, livros. Ficaram **duas âncoras**: a cruz na parede e os livros de lombada roxa. Já lê como o cenário dela e nada mais compete.

## ⚠️ NOTA DE RESTRIÇÃO E DE REGISTRO

Risco de geração **baixo**. Sem anatomia, sem região sensível, sem 2ª pessoa. Os cuidados aqui são de **registro**, não de classificador:

1. **Nenhum prompt diz proteção, feitiço, ritual, bruxa, escudo ou círculo de proteção.** O sal é descrito como `a closed ring of white salt`, e ponto.
2. **Nenhuma luz sobrenatural, nenhuma partícula, nenhum brilho mágico.** O ângulo perde credibilidade na hora que vira efeito.
3. **A carta é clara.** Escura colide com a lei.
4. **No gancho B, o rosto é ilegível pelo GELO**, descrito como propriedade do objeto, e o negative **não** menciona rosto.

---

# Prompts de imagem

## REF-CARTA · GERAR E APROVAR ANTES DE TUDO · SEM REFERÊNCIA

```json
{
  "shot_id": "REF_CARTA_soulmate",
  "reference_use": "Standalone object reference. No person in frame.",
  "identity_main": "No person. A single illustrated card lying flat on a plain light wooden surface, shot from directly above, filling most of the frame.",
  "prop": "A single illustrated tarot-style card, about 12 by 20 cm, portrait orientation, printed on thick matte cardstock with slightly worn edges. The illustration shows a couple embracing, drawn in clean warm line art. The word SOULMATE is printed in small capital letters along the bottom edge. Palette is PALE and LIGHT ONLY: cream, soft gold, pale blush pink and light blue.",
  "scene": "Plain light wooden table surface, nothing else in frame.",
  "composition": "Straight top-down, the card fills most of the frame, edges fully visible.",
  "camera": "top-down, close",
  "state": "Start frame: the card lying still and flat.",
  "lighting": "Flat neutral diffuse daylight, like an overcast day.",
  "realism": "Real matte cardstock texture with visible paper grain and slightly worn edges, realistic soft shadow under the card, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no dark card, no black card, no heavy shadow illustration, no moons, no eyes, no skulls, no zodiac wheel, no glowing edges, no sparkles, no blur, no studio, no warm orange color cast, no yellow tint, no golden glow"
}
```

**O único texto que pode aparecer nesta carta é a palavra SOULMATE na base.** Se vier com mais palavra nenhuma, regenerar.

---

## K01A · T1 · GANCHO VELA · GERAR DO ZERO (Nano Banana **Pro**) · ÂNCORA KENDRA + REF-CARTA

```json
{
  "shot_id": "K01A_hook_vela",
  "reference_use": "TWO references attached. Use the FIRST image ONLY for Kendra's face, identity, hair, earrings, clothing and the living room scene. Use the SECOND image for the EXACT card on the table, matching its illustration, its pale palette and its proportions. Do NOT copy the framing of either reference. Frame her much closer than the reference.",
  "identity_main": "The EXACT WOMAN from the first reference image (Kendra Collins), a Black American woman of about sixty, medium brown skin with visible freckles across her cheeks and nose, real expression lines, very short cropped grey hair, large oval matte white earrings.",
  "wardrobe": "Terracotta linen dress with wide straps and a square neckline, thin SILVER chain with a small SILVER cross pendant, colourful beaded bracelets on her left wrist, plain silver band on her right ring finger.",
  "prop": "On the light wooden table in front of her: a CLOSED, CONTINUOUS ring of coarse white salt, about 40 cm across, with the SOULMATE card from the second reference lying flat at its centre, and a short white pillar candle standing just beside the card. Her right hand holds a lit wooden match, lowered toward the wick, the flame still small on the match. The candle wick is NOT lit yet.",
  "scene": "SAME living room as the first reference image, with only two visible anchors: a dark wooden cross on the beige wall behind her and a shelf of books with PURPLE spines. Everything else out of frame.",
  "posture": "Seated upright at the table, shoulders squared, leaning slightly forward over the ring, looking down at the candle.",
  "composition": "TIGHT. The salt ring and the card fill the lower third of the frame and sit much closer to the lens than her face. Her face is smaller in the upper third.",
  "camera": "chest level from the other side of the table, close, angled slightly down toward the ring",
  "state": "Start frame: the candle is UNLIT, the match flame is still on the match and has not touched the wick.",
  "lighting": "Flat neutral diffuse daylight from a side window out of frame, like an overcast day. No supernatural light.",
  "realism": "UGC realism, real skin texture with visible pores and freckles, individual hair strands, real expression lines, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no second person, no lit candle yet, no broken ring, no glowing light, no sparkles, no floating particles, no smoke yet, no dark card, no warm orange color cast, no yellow tint, no golden glow"
}
```

## K01B · T1 · GANCHO GELO · GERAR DO ZERO (Nano Banana **Pro**) · ÂNCORA KENDRA

```json
{
  "shot_id": "K01B_hook_gelo",
  "reference_use": "Use the attached image ONLY for Kendra's face, identity, hair, earrings, clothing and the living room scene. Do NOT copy its framing. Frame her much closer than the reference.",
  "identity_main": "The EXACT WOMAN from the attached reference image (Kendra Collins), a Black American woman of about sixty, medium brown skin with visible freckles across her cheeks and nose, real expression lines, very short cropped grey hair, large oval matte white earrings.",
  "wardrobe": "Terracotta linen dress with wide straps and a square neckline, thin SILVER chain with a small SILVER cross pendant, colourful beaded bracelets on her left wrist, plain silver band on her right ring finger.",
  "prop": "On the light wooden table in front of her: a THICK solid block of clear ice, about 15 cm tall, standing on a shallow metal tray. Frozen deep inside the ice there is a small framed portrait photograph, turned toward the camera. THE ICE IS CLOUDY AND THICK, and the photograph is completely unreadable through it: only a vague dark shape is visible where the figure would be. Both her hands rest flat on the table on either side of the tray. The block is dry and has not started melting.",
  "scene": "SAME living room as the attached reference image, with only two visible anchors: a dark wooden cross on the beige wall behind her and a shelf of books with PURPLE spines. Everything else out of frame.",
  "posture": "Seated upright at the table, shoulders squared, looking straight into the lens over the top of the ice block.",
  "composition": "TIGHT. The block of ice fills the lower third of the frame and sits much closer to the lens than her face. Her face is smaller in the upper third.",
  "camera": "chest level from the other side of the table, close, angled slightly down toward the ice",
  "state": "Start frame: the ice is still dry and solid, no water on the tray yet.",
  "lighting": "Flat neutral diffuse daylight from a side window out of frame, like an overcast day. No supernatural light.",
  "realism": "UGC realism, real skin texture with visible pores and freckles, individual hair strands, real expression lines, real cloudy ice texture with internal fractures, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no second person, no clear transparent ice, no readable photograph, no water pooled yet, no glowing light, no sparkles, no floating particles, no warm orange color cast, no yellow tint, no golden glow"
}
```

> **A trava do rosto é o GELO, não a câmera.** A ilegibilidade vem de `THE ICE IS CLOUDY AND THICK` e do negative `no clear transparent ice, no readable photograph`. **Não existe a palavra rosto no negative**, e não pode existir.

## K01C · T1 · GANCHO MEL · GERAR DO ZERO (Nano Banana **Pro**) · ÂNCORA KENDRA + REF-CARTA

```json
{
  "shot_id": "K01C_hook_mel",
  "reference_use": "TWO references attached. Use the FIRST image ONLY for Kendra's face, identity, hair, earrings, clothing and the living room scene. Use the SECOND image for the EXACT card in the dish, matching its illustration, its pale palette and its proportions. Do NOT copy the framing of either reference. Frame her much closer than the reference.",
  "identity_main": "The EXACT WOMAN from the first reference image (Kendra Collins), a Black American woman of about sixty, medium brown skin with visible freckles across her cheeks and nose, real expression lines, very short cropped grey hair, large oval matte white earrings.",
  "wardrobe": "Terracotta linen dress with wide straps and a square neckline, thin SILVER chain with a small SILVER cross pendant, colourful beaded bracelets on her left wrist, plain silver band on her right ring finger.",
  "prop": "On the light wooden table in front of her: a wide shallow clear glass dish with the SOULMATE card from the second reference lying flat inside it, fully visible and dry. Her right hand holds a wooden honey dipper raised above the dish, with a single thick thread of amber honey just starting to fall from it. The card is still completely uncovered.",
  "scene": "SAME living room as the attached reference image, with only two visible anchors: a dark wooden cross on the beige wall behind her and a shelf of books with PURPLE spines. Everything else out of frame.",
  "posture": "Seated upright at the table, shoulders squared, leaning slightly forward over the dish, looking down at it.",
  "composition": "TIGHT. The glass dish and the card fill the lower third of the frame and sit much closer to the lens than her face. Her face is smaller in the upper third.",
  "camera": "chest level from the other side of the table, close, angled slightly down toward the dish",
  "state": "Start frame: the card is dry and fully visible, the honey thread has not reached it yet.",
  "lighting": "Flat neutral diffuse daylight from a side window out of frame, like an overcast day. No supernatural light.",
  "realism": "UGC realism, real skin texture with visible pores and freckles, individual hair strands, real expression lines, real viscous honey with realistic refraction, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no second person, no drinking glass, no card already covered, no glowing light, no sparkles, no floating particles, no dark card, no warm orange color cast, no yellow tint, no golden glow"
}
```

## K01D · T1 · GANCHO TERRA · GERAR DO ZERO (Nano Banana **Pro**) · ÂNCORA KENDRA + REF-CARTA

```json
{
  "shot_id": "K01D_hook_terra",
  "reference_use": "TWO references attached. Use the FIRST image ONLY for Kendra's face, identity, hair, earrings, clothing and the living room scene. Use the SECOND image for the EXACT card that is buried under the soil, so that the small uncovered corner matches its palette and cardstock. Do NOT copy the framing of either reference. Frame her much closer than the reference.",
  "identity_main": "The EXACT WOMAN from the first reference image (Kendra Collins), a Black American woman of about sixty, medium brown skin with visible freckles across her cheeks and nose, real expression lines, very short cropped grey hair, large oval matte white earrings.",
  "wardrobe": "Terracotta linen dress with wide straps and a square neckline, thin SILVER chain with a small SILVER cross pendant, colourful beaded bracelets on her left wrist, plain silver band on her right ring finger.",
  "prop": "On the light wooden table in front of her: a shallow wooden tray holding a TALL, HEAPED MOUND of loose dark brown soil, piled high with real 3D volume. The SOULMATE card from the second reference is buried under it, with only ONE SMALL PALE CORNER of the card showing at the edge of the mound. Both her hands rest flat on the table on either side of the tray.",
  "scene": "SAME living room as the attached reference image, with only two visible anchors: a dark wooden cross on the beige wall behind her and a shelf of books with PURPLE spines. Everything else out of frame.",
  "posture": "Seated upright at the table, shoulders squared, leaning forward toward the mound, lips slightly parted as if about to blow.",
  "composition": "TIGHT. The mound of soil fills the lower third of the frame and sits much closer to the lens than her face. Her face is smaller in the upper third.",
  "camera": "chest level from the other side of the table, close, angled slightly down toward the tray",
  "state": "Start frame: the mound is intact and undisturbed, only one small pale corner of the card showing.",
  "lighting": "Flat neutral diffuse daylight from a side window out of frame, like an overcast day. No supernatural light.",
  "realism": "UGC realism, real skin texture with visible pores and freckles, individual hair strands, real expression lines, real loose soil texture with individual crumbs, realistic shadows, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no second person, no thin scattered layer of soil, no card fully visible, no glowing light, no sparkles, no floating particles, no dark card, no warm orange color cast, no yellow tint, no golden glow"
}
```

## K01E · T1 · GANCHO ESPELHO · GERAR DO ZERO (Nano Banana **Pro**) · ÂNCORA KENDRA

```json
{
  "shot_id": "K01E_hook_espelho",
  "reference_use": "Use the attached image ONLY for Kendra's face, identity, hair, earrings, clothing and the living room scene. Do NOT copy its framing. Frame her much closer than the reference.",
  "identity_main": "The EXACT WOMAN from the attached reference image (Kendra Collins), a Black American woman of about sixty, medium brown skin with visible freckles across her cheeks and nose, real expression lines, very short cropped grey hair, large oval matte white earrings.",
  "wardrobe": "Terracotta linen dress with wide straps and a square neckline, thin SILVER chain with a small SILVER cross pendant, colourful beaded bracelets on her left wrist, plain silver band on her right ring finger.",
  "prop": "On the light wooden table in front of her: an oval hand mirror with a plain wooden handle, lying face up and tilted toward the lens. Its glass is COMPLETELY FOGGED OVER with even white condensation, edge to edge, showing no reflection at all and no writing on it yet. Her right index finger is raised just above the glass, about to touch it.",
  "scene": "SAME living room as the attached reference image, with only two visible anchors: a dark wooden cross on the beige wall behind her and a shelf of books with PURPLE spines. Everything else out of frame.",
  "posture": "Seated upright at the table, shoulders squared, leaning slightly forward over the mirror, looking down at it.",
  "composition": "TIGHT. The hand mirror fills the lower third of the frame and sits much closer to the lens than her face. Her face is smaller in the upper third.",
  "camera": "chest level from the other side of the table, close, angled slightly down toward the mirror",
  "state": "Start frame: the glass is fully fogged and blank, her finger has not touched it yet.",
  "lighting": "Flat neutral diffuse daylight from a side window out of frame, like an overcast day. No supernatural light.",
  "realism": "UGC realism, real skin texture with visible pores and freckles, individual hair strands, real expression lines, real condensation with fine water droplets on the glass, realistic shadows, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no second person, no reflection in the mirror, no clear glass, no writing on the glass yet, no glowing light, no sparkles, no floating particles, no warm orange color cast, no yellow tint, no golden glow"
}
```

> **Atenção no K01E:** o negative diz `no writing on the glass yet` porque o `222` é escrito **dentro do clipe**, no V01E. Se a imagem já vier com o número, o gancho perde a ação.

---

## K02 · T2 a T10 · O CORPO · GERAR DO ZERO · ÂNCORA KENDRA + REF-CARTA

**Este keyframe atende NOVE takes e as CINCO variações de gancho.** É o que mais paga regeneração do pacote inteiro.

```json
{
  "shot_id": "K02_corpo_carta",
  "reference_use": "TWO references attached. Use the FIRST image ONLY for Kendra's face, identity, hair, earrings, clothing and the living room scene. Use the SECOND image for the EXACT card she is holding, matching its illustration, its pale palette and its proportions. Do NOT copy the framing of either reference. Frame her closer than the reference.",
  "identity_main": "The EXACT WOMAN from the first reference image (Kendra Collins), a Black American woman of about sixty, medium brown skin with visible freckles across her cheeks and nose, real expression lines, very short cropped grey hair, large oval matte white earrings.",
  "wardrobe": "Terracotta linen dress with wide straps and a square neckline, thin SILVER chain with a small SILVER cross pendant, colourful beaded bracelets on her left wrist, plain silver band on her right ring finger.",
  "prop": "The EXACT SOULMATE card from the second reference, held upright in her right hand, resting on the light wooden table, face turned toward the camera and fully readable. The table is otherwise completely empty.",
  "scene": "SAME living room as the first reference image, with only two visible anchors: a dark wooden cross on the beige wall behind her and a shelf of books with PURPLE spines. Everything else out of frame.",
  "posture": "Seated upright at the table, back straight, shoulders squared, chin level, looking straight into the lens with calm direct eye contact.",
  "composition": "TIGHT chest-up. Her head and shoulders fill the upper two thirds. The card sits in the lower third of the SAME frame, closer to the lens than her face. Her left hand rests open on the table beside it.",
  "camera": "chest level from the other side of the table, straight-on, close",
  "state": "Start frame: card held steady, speaking directly to camera.",
  "lighting": "Flat neutral diffuse daylight from a side window out of frame, like an overcast day. No supernatural light.",
  "realism": "UGC realism, real skin texture with visible pores and freckles, individual hair strands, real expression lines, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no second person, no salt, no candle, no ice, no honey, no soil, no mirror, no clutter on the table, no glowing light, no sparkles, no floating particles, no dark card, no warm orange color cast, no yellow tint, no golden glow"
}
```

> O negative lista os cinco props dos ganchos de propósito: **a mesa do corpo tem que estar vazia**, senão o K02 deixa de servir as cinco variações.

## K03 · T11, T12 · CTA · EDITAR do K02

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same freckles, same short grey hair, same white oval earrings, same terracotta linen dress, same SILVER cross, same beaded bracelets, same seated posture. Keep the SAME background exactly: dark wooden cross on the beige wall, shelf of purple-spined books, same neutral daylight, same camera angle. Keep the card EXACTLY the same illustration and palette.",
  "change_1": "Crop in much tighter. This must be the CLOSEST framing of the entire video: her head and shoulders now fill the frame.",
  "change_2": "She now holds the card raised up against her chest with both hands, face of the card turned toward the camera and fully readable.",
  "change_3": "She looks straight into the lens with direct personal eye contact.",
  "realism": "UGC realism, real skin texture with visible pores and freckles, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the card illustration, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no blur, no glowing light, no sparkles, no warm orange color cast, no yellow tint"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Colar em todo prompt:

```text
a avatar (MULHER) fala em inglês com sotaque americano, voz calma, grave e de autoridade por vivência, sem pressa e sem tom de novela.

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

Estilo TikTok nativo, UGC. Preservar exatamente a identidade da Kendra, rosto, sardas, cabelo grisalho curto, brincos brancos ovais, vestido de linho terracota, cruz de PRATA, a sala, a luz neutra e o enquadramento do frame inicial. Sem legenda, sem texto gerado, sem música, sem pessoas extras, sem luz sobrenatural.
```

**A câmera é FIXA do outro lado da mesa em todo o vídeo.** Não é handheld de selfie, então não incluir a instrução de braço parado.

---

## Os cinco clipes de gancho (T1) · TODOS MUDOS

### V01A · T1 · usa K01A · GANCHO VELA · B-ROLL

```text
(sem fala no take: a abertura do original é muda e o texto entra na edição)

o que acontece no vídeo: ela encosta o fósforo no pavio, a vela acende e a chama sobe e fica firme, iluminando a carta que está no centro do anel de sal. Ela olha da chama para a lente.

câmera: fixa

som ambiente: sala silenciosa, o estalo do fósforo, sem música
```

### V01B · T1 · usa K01B · GANCHO GELO · B-ROLL

```text
(sem fala no take: a abertura do original é muda e o texto entra na edição)

o que acontece no vídeo: o bloco de gelo começa a derreter. Gotas escorrem pelas laterais e se juntam na bandeja embaixo. O retrato lá dentro continua embaçado pelo gelo o tempo inteiro. Ela olha para a lente.

câmera: fixa

som ambiente: sala silenciosa, gotas pingando, sem música
```

### V01C · T1 · usa K01C · GANCHO MEL · B-ROLL

```text
(sem fala no take: a abertura do original é muda e o texto entra na edição)

o que acontece no vídeo: o fio de mel cai na carta e se espalha devagar por cima dela, cobrindo a ilustração até quase sumir sob o âmbar. Ela olha da tigela para a lente.

câmera: fixa

som ambiente: sala silenciosa, sem música, sem ruído de fundo
```

### V01D · T1 · usa K01D · GANCHO TERRA · B-ROLL

```text
(sem fala no take: a abertura do original é muda e o texto entra na edição)

o que acontece no vídeo: ela sopra o monte de terra e a terra se abre e voa para os lados, descobrindo a carta que estava embaixo. Ela olha da carta para a lente.

câmera: fixa

som ambiente: sala silenciosa, o sopro, sem música
```

### V01E · T1 · usa K01E · GANCHO ESPELHO · B-ROLL

```text
(sem fala no take: a abertura do original é muda e o texto entra na edição)

o que acontece no vídeo: o dedo dela escreve o número 222 no vapor do espelho, e as três marcas ficam limpas e nítidas no vidro embaçado. Ela tira a mão e olha para a lente.

câmera: fixa

som ambiente: sala silenciosa, sem música, sem ruído de fundo
```

---

## Os clipes do corpo (servem as cinco variações)

### V02 · T2 · usa K02

```text
a avatar (MULHER) fala em inglês com sotaque americano, voz calma e baixa, como quem conta um segredo, a seguinte frase: "When this blessing reaches you, keep it to yourself. This one is not for everybody."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro, a mesa está vazia e ela segura a carta. ela se inclina um pouco pra frente e baixa o tom.

câmera: fixa, leve push-in

som ambiente: sala silenciosa, sem música, sem ruído de fundo
```

### V03 · T3 · usa K02

```text
a avatar (MULHER) fala em inglês com sotaque americano, voz calma e de certeza, a seguinte frase: "If you are still here, that is not a coincidence. Out of everyone scrolling tonight, it stopped on you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta devagar para a lente ao dizer a última palavra.

câmera: fixa

som ambiente: sala silenciosa, sem música, sem ruído de fundo
```

### V04 · T4 · usa K02

```text
a avatar (MULHER) fala em inglês com sotaque americano, voz mais firme, quase de aviso, a seguinte frase: "But do not scroll away now. If you leave before the end, you hand it back and it goes to somebody else."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela levanta a palma da mão livre num gesto de pare na primeira frase e depois abre a mão para o lado na última.

câmera: fixa, leve push-in

som ambiente: sala silenciosa, sem música, sem ruído de fundo
```

### V05 · T5 · usa K02 · **A PONTE PRO ROSTO**

```text
a avatar (MULHER) fala em inglês com sotaque americano, voz mais baixa e íntima, a seguinte frase: "A blessing is already moving toward you, and it is wearing a face. Tonight I can show you whose."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela ergue um pouco a carta ao dizer a palavra face e fica olhando fixo pra lente na última frase.

câmera: fixa, leve push-in

som ambiente: sala silenciosa, sem música, sem ruído de fundo
```

### V06 · T6 · usa K02

```text
a avatar (MULHER) fala em inglês com sotaque americano, voz séria, a seguinte frase: "This is the universe answering, so take it seriously. What comes next is not what you are expecting."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela assente uma vez, devagar, na primeira frase e para de se mexer na segunda.

câmera: fixa

som ambiente: sala silenciosa, sem música, sem ruído de fundo
```

### V07 · T7 · usa K02

```text
a avatar (MULHER) fala em inglês com sotaque americano, voz mais quente e pessoal, a seguinte frase: "The ones who stay to the end always write me back. They all say the same thing. They knew."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela abre um sorriso curto na segunda frase e para na última.

câmera: fixa

som ambiente: sala silenciosa, sem música, sem ruído de fundo
```

### V08 · T8 · usa K02 · **PRIMEIRO SELO**

```text
a avatar (MULHER) fala em inglês com sotaque americano, voz direta e de instrução, a seguinte frase: "Comment two two two right now. That is the first seal, and it is how you claim something that already has your name on it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta pra baixo com a mão livre, na direção dos comentários, ao dizer o número, e depois ergue um dedo ao dizer first seal.

câmera: fixa, leve push-in

som ambiente: sala silenciosa, sem música, sem ruído de fundo
```

### V09 · T9 · usa K02 · **SEGUNDO SELO, O FOLLOW GATE**

```text
a avatar (MULHER) fala em inglês com sotaque americano, voz direta, a seguinte frase: "Follow me. That is your second seal, and without it I have no way to reach you when it comes."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela ergue dois dedos da mão livre ao dizer second seal.

câmera: fixa

som ambiente: sala silenciosa, sem música, sem ruído de fundo
```

### V10 · T10 · usa K02 · **TERCEIRO SELO**

```text
a avatar (MULHER) fala em inglês com sotaque americano, voz calma e de conselho, a seguinte frase: "Save this. That is your third seal, and you will want it again on the day their face shows up."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela ergue três dedos da mão livre ao dizer third seal e depois olha firme pra lente.

câmera: fixa

som ambiente: sala silenciosa, sem música, sem ruído de fundo
```

### V11 · T11 · usa K03

```text
a avatar (MULHER) fala em inglês com sotaque americano, voz mais baixa e íntima, a seguinte frase: "The second half of this reading is their face, and I am sending it straight to your messages."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro, o plano está bem mais fechado e ela segura a carta junto ao peito com as duas mãos, virada pra lente.

câmera: fixa, leve push-in

som ambiente: sala silenciosa, sem música, sem ruído de fundo
```

### V12 · T12 · usa K03

```text
a avatar (MULHER) fala em inglês com sotaque americano, voz direta e de instrução, a seguinte frase: "Two two two. Go put it in the comments before you scroll, and watch your messages tonight."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta uma vez pra baixo ao dizer o número e termina com um aceno curto de cabeça, ainda com a carta junto ao peito.

câmera: fixa, leve push-in

som ambiente: sala silenciosa, sem música, sem ruído de fundo
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| **REF-CARTA** | nenhuma | Nano Banana 2. **Gerar e aprovar ANTES de tudo** |
| K01A | âncora Kendra + **REF-CARTA** | Nano Banana **Pro**, várias variações |
| K01B | âncora Kendra | Nano Banana **Pro**, várias variações |
| K01C | âncora Kendra + **REF-CARTA** | Nano Banana **Pro**, várias variações |
| K01D | âncora Kendra + **REF-CARTA** | Nano Banana **Pro**, várias variações |
| K01E | âncora Kendra | Nano Banana **Pro**, várias variações |
| K02 | âncora Kendra + **REF-CARTA** | Nano Banana 2. **Atende 9 takes e as 5 variações**, vale insistir |
| K03 | **K02 aprovado** | Nano Banana 2, comando de edição |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps. Cortes duros entre todos os takes.
- **Cinco versões do vídeo.** Só o primeiro clipe muda: V01A, V01B, V01C, V01D ou V01E. Do V02 ao V12 é o mesmo arquivo nas cinco.
- **O texto do T1 é obrigatório e é o hook.** Caixa branca ou legenda no topo da metade de cima, e o texto muda por variação:
  - A e C: `DO NOT TELL ANYONE WHAT HAPPENS NEXT`
  - B: `DO NOT TELL ANYONE WHOSE FACE THIS IS`
  - D: `IT WAS BURIED UNDER YOUR NAME`
  - E: `WRITE IT BEFORE IT FADES`
- **Dois cortes de peso:** V01x para V02 (some o prop do gancho, entra a carta na mão) e V10 para V11 (o plano fecha).
- Cortar o silêncio inicial de cada clipe.
- **Segurar um beat extra de silêncio no fim do V05**, depois de "show you whose". É a ponte pro rosto e é o beat que faz ela comentar.
- Legendas grandes estilo karaokê com destaque amarelo, na altura do peito.
- **Gráfico flutuante `222` fixo no canto superior**, do V08 em diante.
- **Manter `222` isolado na tela nos V08 e V12.**
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +10, highlight -30, shadow +15, fade +6.

## Gates de qualidade

1. Kendra é **MULHER**, a mesma em todos os clipes, com a cruz de **PRATA** sempre, nunca ouro.
2. As sardas, o cabelo grisalho raspado e os brincos brancos ovais estão iguais em todos os planos.
3. **A REF-CARTA foi gerada e aprovada ANTES de tudo**, e é a mesma carta em todos os keyframes.
4. **A carta é CLARA**: creme, dourado suave, rosa claro ou azul claro. Carta escura ou de arte sombria, regenerar. É lei do ângulo.
5. **A única palavra na carta é SOULMATE.** Qualquer outra, regenerar.
6. **O T1 é MUDO nas cinco variações.** Se algum clipe de gancho vier com fala, refazer.
7. **K01A:** a vela sai **APAGADA** e o anel de sal está **fechado e contínuo**. Vela já acesa, regenerar.
8. **K01B:** o gelo é **opaco e grosso** e o retrato é **ilegível**. Se der pra reconhecer o rosto, regenerar. **A trava é o gelo, nunca blur.**
9. **K01C:** a carta está **seca e visível**, o mel ainda não encostou.
10. **K01D:** o monte de terra é **alto e com volume**, e só um cantinho claro da carta aparece.
11. **K01E:** o espelho está **totalmente embaçado e sem o número**. O `222` é escrito dentro do clipe.
12. **A mesa do K02 está VAZIA**, sem sal, vela, gelo, mel, terra nem espelho. Senão ele deixa de servir as cinco variações.
13. **O K03 é o plano mais fechado do vídeo inteiro.**
14. Fundo não inventariado: **duas âncoras apenas**, a cruz de madeira e os livros de lombada roxa.
15. **Nenhuma luz sobrenatural, nenhuma partícula flutuando, nenhum brilho mágico** em nenhum frame.
16. **A cena não está banhada de laranja nem de dourado.** Luz neutra de dia nublado.
17. Nenhuma imagem com fundo desfocado.
18. Mãos com cinco dedos, sem fusão com a carta.
19. Ela **não larga a carta** do V02 ao V12.
20. **`222` é falado como "two two two"** nos V08 e V12. Se o Veo ler "two hundred twenty two", refazer.
21. **Nenhum take diz proteção, feitiço, ritual, escudo, bruxa nem círculo de proteção.**
22. **Nenhum take mostra app, celular, tela, quiz ou preço.**
23. `222` e o follow gate estão os dois no vídeo, nos V08 e V09.
