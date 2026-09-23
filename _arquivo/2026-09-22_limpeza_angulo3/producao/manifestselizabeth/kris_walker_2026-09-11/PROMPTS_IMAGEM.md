# Prompts de imagem | manifestselizabeth | KRIS WALKER | Angulo 3 (Auraly)

## Cabecalho

- **Video modelo:** `C:\Users\luigi\Downloads\manifestselizabeth.mp4` , 48,946s, uma cena continua
- **Avatar:** **Kris Walker**, 24 anos, `ACTIVE` na fila de `AVATAR_QUEUE.md` desde 2026-09-11
- **Ancora:** `producao/_ancoras/Kris.Walker_us .jpeg`
- **Avatar anterior:** Robin Matthews, `DONE`, pacote arquivado em `PROMPTS_IMAGEM_ROBIN_MATTHEWS.md`
- **Roteiro:** `ROTEIRO.md`, 7 takes. **O T2 muda de redacao nesta avatar**, ver a secao de congruencia
- **Ganchos escolhidos pelo Luigi:** os mesmos cinco da Robin, com a mesma acao e a mesma hierarquia visual
- **Funil:** video, selo (`222` + save + follow), Stories, botao do link

## Indice de geracao

| Take | Keyframe | Cena | Acao de geracao | Anexo |
|---|---|---|---|---|
| T1 | **K01** | HOOK A A PEDRA QUE ABRE | GERAR DO ZERO | ancora KRIS |
| T1 | **K02** | HOOK B A AGUA QUE SALTA | GERAR DO ZERO | ancora KRIS |
| T1 | **K03** | HOOK C A TOALHA PUXADA | GERAR DO ZERO | ancora KRIS |
| T1 | **K04** | HOOK D A FLOR QUE ABRE NA AGUA | GERAR DO ZERO | ancora KRIS |
| T1 | **K05** | HOOK E O GLOBO SACUDIDO | GERAR DO ZERO | ancora KRIS |
| T2 | **K06** | BODY CARTA NA MAO | GERAR DO ZERO | ancora KRIS |
| T3 | **K07** | BODY CARTA NA MAO | EDITAR do K06 | o K06 ja aprovado |
| T4 | **K08** | BODY CARTA NA MAO | EDITAR do K06 | o K06 ja aprovado |
| T5 | **K09** | BODY CARTA NA MAO | EDITAR do K06 | o K06 ja aprovado |
| T6 | **K10** | CTA | EDITAR do K06 | o K06 ja aprovado |
| T7 | **K11** | CTA | EDITAR do K06 | o K06 ja aprovado |

**Regra de bolso:** `GERAR DO ZERO` anexa a ancora, `EDITAR` anexa uma imagem so, o keyframe de
origem. **K07 a K11 saem todos do K06 aprovado, nunca em cascata de uma edicao ja editada.**

## O que muda em relacao a Robin, e por que

Esqueleto, takes, ganchos, ordem de K e V e logica de movimento sao os mesmos, aprovados uma vez para
a producao inteira. Muda identidade, cenario e **uma linha de copy**.

| | Robin Matthews | Kris Walker |
|---|---|---|
| Idade | 72 | 24 |
| Autoridade | decadas de leitura | certeza calma, de quem repete algo que ja sabe ser verdade |
| Cenario | cozinha de armarios de carvalho | quarto de dia, cama de colcha floral e jiboia |
| Cartas da mesa | cavalete de madeira | tres viradas para cima em fila |
| Bandeira US | pequena em suporte no peitoril | grande esticada na parede a esquerda |
| Joia | cruz de prata mais alianca de ouro | cruz de prata e argolas pequenas de prata |
| Maos | manchas de idade | unhas curtas naturais, sem esmalte e sem alongamento |

**A unica mudanca de copy e o T2.** Na Robin a fala fecha com `honey`, que e natural na boca de uma
mulher de setenta e dois anos e soa emprestado na de uma mulher de vinte e quatro. Em Kris o fecho
vira `I am telling you`, que carrega a mesma certeza no registro dela.

- **Robin, T2:** "And the face of the person you are actually meant for came through this morning. It is already in motion, honey." (21 palavras)
- **Kris, T2:** "And the face of the person you are actually meant for came through this morning. It is already in motion, I am telling you." (24 palavras)

**T1, T3, T4, T5, T6 e T7 ficam identicos.** O T1 e o take do gancho e a fala dele carrega o hook, e
do T3 em diante e mecanica de funil, que nao tem idade nem registro.

## Trava de identidade e continuidade (bloco unico, vale para os onze)

Kris Walker e **MULHER**, 24 anos, e o nome e ambiguo em ingles, entao todo `identity_main` comeca com
`The EXACT woman`. Tracos fixos: box braids na altura do peito, castanho escuro com mechas mel, risca
ao meio e presas para tras, pele marrom profunda com brilho natural na testa e nas macas, sinais
escuros pequenos na testa, na bochecha e acima do labio, zero maquiagem, **unhas curtas e naturais**,
camiseta canelada marrom, argolas pequenas de prata e cruz de prata.

**Kris e de DIA.** A ancora saiu com luz de janela e sem LED, e o Luigi confirmou em 2026-09-03 que
fica assim. `no coloured LED light` entra no negative dos onze prompts, porque o print de referencia
original dela tinha LED magenta e o gerador tende a puxar de volta.

Cenario fixo: quarto de dia, mesa de madeira clara no terco inferior, tres cartas classicas de borda
branca viradas para cima em fila, fluorita verde, torre de selenita, prato de ceramica com incenso
aceso, tres velas rechaud apagadas, bandeira dos EUA grande esticada na parede a esquerda, crucifixo
de madeira ao centro, quadro do sol e da lua e quadro da carta natal a direita, janela a esquerda,
cama de colcha floral atras e comoda com jiboia a direita.

## Trava do prop heroi: a carta SOULMATE

A carta e descrita por inteiro dentro de cada prompt que a mostra. **O brilho e propriedade impressa
do objeto, nunca luz de cena.** O baralho da mesa dela e classico de borda branca e a carta que ela
segura e holografica, aceito de proposito: a leitura e que ela puxou uma carta especial. **Nunca
escrever que a carta saiu daquele baralho.**

Nos onze prompts o negative **nao leva** `no words overlaid on the image`, e o campo `prop` diz que o
unico texto da imagem e a palavra impressa na faixa da carta.

## Trava da 2a pessoa (REF-A)

**Nao existe segunda pessoa nesta producao.** `no second person` entra no negative dos onze prompts.


## K01 | T1 | HOOK A A PEDRA QUE ABRE | GERAR DO ZERO | ANCORA KRIS

> ### ANEXAR: **1 IMAGEM**
> **1. ANCORA KRIS** `producao/_ancoras/Kris.Walker_us .jpeg`
>
> ### GERAR DO ZERO

Pedra cinza fechada no primeiro plano, martelinho encostado nela, carta SOULMATE ao lado.

```json
{
  "shot_id": "K01_hook_stone_initial",
  "reference_use": "Use the attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real bedroom. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 24-year-old Black American woman with deep brown skin, visible pores, a natural sheen on her forehead and cheekbones, and small dark beauty marks on her forehead, on her cheek and above her lip. Her hair is in chest length box braids, dark brown with honey coloured strands mixed through, parted in the centre and pushed back. She has dark brown eyes, full lips, natural eyebrows and no makeup at all. Her fingernails are short and natural, with no polish and no extensions. She is clearly a woman and clearly in her twenties.",
  "wardrobe": "The same brown ribbed short sleeve top, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "prop": "A plain dull grey stone the size of a fist sits on the light wooden table top in the lower foreground, completely whole and closed, with one hairline seam running across its middle. Kris's right hand holds a small steel hammer whose head has just touched the top of the stone. A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card lies face up on the table beside the stone.",
  "scene": "The SAME real American bedroom in daylight as the reference image, lived in and unchanged, with the window on her left, the floral quilt bed behind her and the wooden dresser with a trailing pothos in a terracotta pot on the right. The table group in the lower foreground holds three classic white bordered tarot cards laid face up in a row, a chunk of green fluorite, a white selenite tower, a ceramic dish with a tall incense stick and a visible thread of smoke, and three unlit white tea lights. The wall group behind her holds a large United States flag pinned flat on the left, a wooden crucifix in the centre and two framed prints, one of a stylised sun and moon and one of a printed birth chart wheel, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Kris sits upright at the light wooden table, forearms resting on the wood, leaning slightly forward, her eyes on the object in front of her and then toward the lens. Both hands stay anatomically clear and fully visible, with short natural nails.",
  "composition": "EXTREME CLOSE foreground emphasis. The closed grey stone and the hammer head fills the lower foreground and is much closer to the lens than Kris's face. Kris is chest-up in the upper portion of the frame. Nothing competes with it.",
  "camera": "table height, slightly high toward the stone, pushed in very close",
  "state": "Start frame: the stone is still whole and closed and the hammer head has just made contact with it, before any strike and before anything opens.",
  "lighting": "Soft neutral daylight from the window on her left, cool and even on her face, with no warm cast. The tea lights are unlit and light nothing, and there is no coloured LED anywhere in the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no skin smoothing, no makeup, no long nails, no nail polish, no coloured LED light, no change of identity, no change of wardrobe"
}
```

## K02 | T1 | HOOK B A AGUA QUE SALTA | GERAR DO ZERO | ANCORA KRIS

> ### ANEXAR: **1 IMAGEM**
> **1. ANCORA KRIS** `producao/_ancoras/Kris.Walker_us .jpeg`
>
> ### GERAR DO ZERO

Tigela rasa de agua parada no primeiro plano, bastao de madeira encostado na borda.

```json
{
  "shot_id": "K02_hook_bowl_initial",
  "reference_use": "Use the attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real bedroom. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 24-year-old Black American woman with deep brown skin, visible pores, a natural sheen on her forehead and cheekbones, and small dark beauty marks on her forehead, on her cheek and above her lip. Her hair is in chest length box braids, dark brown with honey coloured strands mixed through, parted in the centre and pushed back. She has dark brown eyes, full lips, natural eyebrows and no makeup at all. Her fingernails are short and natural, with no polish and no extensions. She is clearly a woman and clearly in her twenties.",
  "wardrobe": "The same brown ribbed short sleeve top, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "prop": "A shallow wide cream ceramic bowl half filled with clear water sits on the light wooden table top in the lower foreground, and the water surface is completely still and flat like a mirror. Kris's right hand holds a short wooden striker resting against the outer rim of the bowl. A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card lies face up on the table beside the bowl.",
  "scene": "The SAME real American bedroom in daylight as the reference image, lived in and unchanged, with the window on her left, the floral quilt bed behind her and the wooden dresser with a trailing pothos in a terracotta pot on the right. The table group in the lower foreground holds three classic white bordered tarot cards laid face up in a row, a chunk of green fluorite, a white selenite tower, a ceramic dish with a tall incense stick and a visible thread of smoke, and three unlit white tea lights. The wall group behind her holds a large United States flag pinned flat on the left, a wooden crucifix in the centre and two framed prints, one of a stylised sun and moon and one of a printed birth chart wheel, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Kris sits upright at the light wooden table, forearms resting on the wood, leaning slightly forward, her eyes on the object in front of her and then toward the lens. Both hands stay anatomically clear and fully visible, with short natural nails.",
  "composition": "EXTREME CLOSE foreground emphasis. The bowl of still water and the wooden striker fills the lower foreground and is much closer to the lens than Kris's face. Kris is chest-up in the upper portion of the frame. Nothing competes with it.",
  "camera": "table height, slightly high toward the bowl, pushed in very close",
  "state": "Start frame: the water is perfectly still and the striker has just touched the rim, before any sound and before the surface moves.",
  "lighting": "Soft neutral daylight from the window on her left, cool and even on her face, with no warm cast. The tea lights are unlit and light nothing, and there is no coloured LED anywhere in the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no skin smoothing, no makeup, no long nails, no nail polish, no coloured LED light, no change of identity, no change of wardrobe"
}
```

## K03 | T1 | HOOK C A TOALHA PUXADA | GERAR DO ZERO | ANCORA KRIS

> ### ANEXAR: **1 IMAGEM**
> **1. ANCORA KRIS** `producao/_ancoras/Kris.Walker_us .jpeg`
>
> ### GERAR DO ZERO

Toalha esticada com os objetos em pe em cima, as duas maos fechadas na barra.

```json
{
  "shot_id": "K03_hook_tablecloth_initial",
  "reference_use": "Use the attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real bedroom. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 24-year-old Black American woman with deep brown skin, visible pores, a natural sheen on her forehead and cheekbones, and small dark beauty marks on her forehead, on her cheek and above her lip. Her hair is in chest length box braids, dark brown with honey coloured strands mixed through, parted in the centre and pushed back. She has dark brown eyes, full lips, natural eyebrows and no makeup at all. Her fingernails are short and natural, with no polish and no extensions. She is clearly a woman and clearly in her twenties.",
  "wardrobe": "The same brown ribbed short sleeve top, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "prop": "A plain cream linen tablecloth covers the light wooden table in the lower foreground. Standing upright on the cloth are the white selenite tower and the chunk of green fluorite. A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card stands propped upright on the cloth between them. Both of Kris's hands grip the near hem of the cloth, knuckles tight, the fabric pulled taut.",
  "scene": "The SAME real American bedroom in daylight as the reference image, lived in and unchanged, with the window on her left, the floral quilt bed behind her and the wooden dresser with a trailing pothos in a terracotta pot on the right. The table group in the lower foreground holds three classic white bordered tarot cards laid face up in a row, a chunk of green fluorite, a white selenite tower, a ceramic dish with a tall incense stick and a visible thread of smoke, and three unlit white tea lights. The wall group behind her holds a large United States flag pinned flat on the left, a wooden crucifix in the centre and two framed prints, one of a stylised sun and moon and one of a printed birth chart wheel, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Kris sits upright at the light wooden table, leaning forward, both hands closed on the near hem of the tablecloth, her eyes on the objects standing on it. Both hands stay anatomically clear, with short natural nails.",
  "composition": "EXTREME CLOSE foreground emphasis. The taut tablecloth with the objects standing on it fills the lower foreground and is much closer to the lens than Kris's face. Kris is chest-up in the upper portion of the frame. Nothing competes with it.",
  "camera": "table height, slightly high toward the cloth, pushed in very close",
  "state": "Start frame: every object is standing still and upright on the cloth and her hands are closed on the hem, before the pull begins.",
  "lighting": "Soft neutral daylight from the window on her left, cool and even on her face, with no warm cast. The tea lights are unlit and light nothing, and there is no coloured LED anywhere in the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no skin smoothing, no makeup, no long nails, no nail polish, no coloured LED light, no change of identity, no change of wardrobe"
}
```

## K04 | T1 | HOOK D A FLOR QUE ABRE NA AGUA | GERAR DO ZERO | ANCORA KRIS

> ### ANEXAR: **1 IMAGEM**
> **1. ANCORA KRIS** `producao/_ancoras/Kris.Walker_us .jpeg`
>
> ### GERAR DO ZERO

Tigela de vidro com agua e a bolinha de papel dobrada acima dela.

```json
{
  "shot_id": "K04_hook_paper_initial",
  "reference_use": "Use the attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real bedroom. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 24-year-old Black American woman with deep brown skin, visible pores, a natural sheen on her forehead and cheekbones, and small dark beauty marks on her forehead, on her cheek and above her lip. Her hair is in chest length box braids, dark brown with honey coloured strands mixed through, parted in the centre and pushed back. She has dark brown eyes, full lips, natural eyebrows and no makeup at all. Her fingernails are short and natural, with no polish and no extensions. She is clearly a woman and clearly in her twenties.",
  "wardrobe": "The same brown ribbed short sleeve top, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "prop": "A wide clear glass bowl of water sits on the light wooden table top in the lower foreground. Kris's fingers hold a small tightly folded paper pellet just above the water surface, dry and closed, the folds sharp and visible. A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card lies face up on the table beside the bowl.",
  "scene": "The SAME real American bedroom in daylight as the reference image, lived in and unchanged, with the window on her left, the floral quilt bed behind her and the wooden dresser with a trailing pothos in a terracotta pot on the right. The table group in the lower foreground holds three classic white bordered tarot cards laid face up in a row, a chunk of green fluorite, a white selenite tower, a ceramic dish with a tall incense stick and a visible thread of smoke, and three unlit white tea lights. The wall group behind her holds a large United States flag pinned flat on the left, a wooden crucifix in the centre and two framed prints, one of a stylised sun and moon and one of a printed birth chart wheel, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Kris sits upright at the light wooden table, forearms resting on the wood, leaning slightly forward, her eyes on the object in front of her and then toward the lens. Both hands stay anatomically clear and fully visible, with short natural nails.",
  "composition": "EXTREME CLOSE foreground emphasis. The clear bowl of water and the folded paper pellet above it fills the lower foreground and is much closer to the lens than Kris's face. Kris is chest-up in the upper portion of the frame. Nothing competes with it.",
  "camera": "table height, slightly high toward the bowl, pushed in very close",
  "state": "Start frame: the paper pellet is still dry, closed and held above the water, before it is dropped and before anything opens.",
  "lighting": "Soft neutral daylight from the window on her left, cool and even on her face, with no warm cast. The tea lights are unlit and light nothing, and there is no coloured LED anywhere in the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no skin smoothing, no makeup, no long nails, no nail polish, no coloured LED light, no change of identity, no change of wardrobe"
}
```

## K05 | T1 | HOOK E O GLOBO SACUDIDO | GERAR DO ZERO | ANCORA KRIS

> ### ANEXAR: **1 IMAGEM**
> **1. ANCORA KRIS** `producao/_ancoras/Kris.Walker_us .jpeg`
>
> ### GERAR DO ZERO

Globo de neve erguido perto da lente, flocos assentados, figuras moldadas sem rosto.

```json
{
  "shot_id": "K05_hook_globe_initial",
  "reference_use": "Use the attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real bedroom. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 24-year-old Black American woman with deep brown skin, visible pores, a natural sheen on her forehead and cheekbones, and small dark beauty marks on her forehead, on her cheek and above her lip. Her hair is in chest length box braids, dark brown with honey coloured strands mixed through, parted in the centre and pushed back. She has dark brown eyes, full lips, natural eyebrows and no makeup at all. Her fingernails are short and natural, with no polish and no extensions. She is clearly a woman and clearly in her twenties.",
  "wardrobe": "The same brown ribbed short sleeve top, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "prop": "A small glass snow globe on a dark wooden base is held in Kris's raised right hand in the lower foreground, very close to the lens. Inside the globe two small figures stand side by side under a plain arch, moulded as smooth featureless silhouettes with no facial detail at all, and the white flakes lie settled on the floor of the globe. A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card lies face up on the table below her hand.",
  "scene": "The SAME real American bedroom in daylight as the reference image, lived in and unchanged, with the window on her left, the floral quilt bed behind her and the wooden dresser with a trailing pothos in a terracotta pot on the right. The table group in the lower foreground holds three classic white bordered tarot cards laid face up in a row, a chunk of green fluorite, a white selenite tower, a ceramic dish with a tall incense stick and a visible thread of smoke, and three unlit white tea lights. The wall group behind her holds a large United States flag pinned flat on the left, a wooden crucifix in the centre and two framed prints, one of a stylised sun and moon and one of a printed birth chart wheel, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Kris sits upright at the light wooden table, her right forearm lifted so the snow globe is held close to the lens, her left hand flat on the wood, her eyes on the globe and then toward the lens. Both hands stay anatomically clear, with short natural nails.",
  "composition": "EXTREME CLOSE foreground emphasis. The snow globe in her hand fills the lower foreground and is much closer to the lens than Kris's face. Kris is chest-up in the upper portion of the frame. Nothing competes with it.",
  "camera": "table height, slightly high toward the globe, pushed in very close",
  "state": "Start frame: the globe is held still and the flakes are settled at the bottom, before the shake begins.",
  "lighting": "Soft neutral daylight from the window on her left, cool and even on her face, with no warm cast. The tea lights are unlit and light nothing, and there is no coloured LED anywhere in the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no skin smoothing, no makeup, no long nails, no nail polish, no coloured LED light, no change of identity, no change of wardrobe"
}
```

## K06 | T2 | BODY CARTA NA MAO | GERAR DO ZERO | ANCORA KRIS

> ### ANEXAR: **1 IMAGEM**
> **1. ANCORA KRIS** `producao/_ancoras/Kris.Walker_us .jpeg`
>
> ### GERAR DO ZERO

Carta SOULMATE erguida ao lado do rosto, mao esquerda apoiada na mesa.

```json
{
  "shot_id": "K06_body_card_held_initial",
  "reference_use": "Use the attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real bedroom. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 24-year-old Black American woman with deep brown skin, visible pores, a natural sheen on her forehead and cheekbones, and small dark beauty marks on her forehead, on her cheek and above her lip. Her hair is in chest length box braids, dark brown with honey coloured strands mixed through, parted in the centre and pushed back. She has dark brown eyes, full lips, natural eyebrows and no makeup at all. Her fingernails are short and natural, with no polish and no extensions. She is clearly a woman and clearly in her twenties.",
  "wardrobe": "The same brown ribbed short sleeve top, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "prop": "A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card is held upright in Kris's right hand in the lower foreground, fully visible and closer to the lens than her face.",
  "scene": "The SAME real American bedroom in daylight as the reference image, lived in and unchanged, with the window on her left, the floral quilt bed behind her and the wooden dresser with a trailing pothos in a terracotta pot on the right. The table group in the lower foreground holds three classic white bordered tarot cards laid face up in a row, a chunk of green fluorite, a white selenite tower, a ceramic dish with a tall incense stick and a visible thread of smoke, and three unlit white tea lights. The wall group behind her holds a large United States flag pinned flat on the left, a wooden crucifix in the centre and two framed prints, one of a stylised sun and moon and one of a printed birth chart wheel, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Kris sits upright at the light wooden table, holding the card steady beside her cheek and looking directly into the lens. Her left hand rests flat and still on the table. Both hands stay anatomically clear, with short natural nails.",
  "composition": "Tight chest-up talking frame. The SOULMATE card occupies the lower foreground and Kris's face fills the upper third. The bedroom stays recognizable without competing with the card.",
  "camera": "eye level, straight-on, close phone-camera distance",
  "state": "Start frame: Kris already holds the card upright beside her face and looks into the lens, her expression calm and certain, before speaking.",
  "lighting": "Soft neutral daylight from the window on her left, cool and even on her face, with no warm cast. The tea lights are unlit and light nothing, and there is no coloured LED anywhere in the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no skin smoothing, no makeup, no long nails, no nail polish, no coloured LED light, no change of identity, no change of wardrobe"
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
  "reference_use": "Use the attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real bedroom. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 24-year-old Black American woman with deep brown skin, visible pores, a natural sheen on her forehead and cheekbones, and small dark beauty marks on her forehead, on her cheek and above her lip. Her hair is in chest length box braids, dark brown with honey coloured strands mixed through, parted in the centre and pushed back. She has dark brown eyes, full lips, natural eyebrows and no makeup at all. Her fingernails are short and natural, with no polish and no extensions. She is clearly a woman and clearly in her twenties.",
  "wardrobe": "The same brown ribbed short sleeve top, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "prop": "A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card is held upright in Kris's right hand in the lower foreground, fully visible and closer to the lens than her face.",
  "scene": "The SAME real American bedroom in daylight as the reference image, lived in and unchanged, with the window on her left, the floral quilt bed behind her and the wooden dresser with a trailing pothos in a terracotta pot on the right. The table group in the lower foreground holds three classic white bordered tarot cards laid face up in a row, a chunk of green fluorite, a white selenite tower, a ceramic dish with a tall incense stick and a visible thread of smoke, and three unlit white tea lights. The wall group behind her holds a large United States flag pinned flat on the left, a wooden crucifix in the centre and two framed prints, one of a stylised sun and moon and one of a printed birth chart wheel, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Kris sits upright at the light wooden table, holding the card steady beside her cheek and looking directly into the lens. Her left index finger rests on the edge of the table. Both hands stay anatomically clear, with short natural nails.",
  "composition": "Tight chest-up talking frame. The SOULMATE card occupies the lower foreground and Kris's face fills the upper third. The bedroom stays recognizable without competing with the card.",
  "camera": "eye level, straight-on, close phone-camera distance",
  "state": "Start frame: Kris already holds the card upright beside her face and looks into the lens, her expression firm and warning, before speaking.",
  "lighting": "Soft neutral daylight from the window on her left, cool and even on her face, with no warm cast. The tea lights are unlit and light nothing, and there is no coloured LED anywhere in the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no skin smoothing, no makeup, no long nails, no nail polish, no coloured LED light, no change of identity, no change of wardrobe"
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
  "reference_use": "Use the attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real bedroom. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 24-year-old Black American woman with deep brown skin, visible pores, a natural sheen on her forehead and cheekbones, and small dark beauty marks on her forehead, on her cheek and above her lip. Her hair is in chest length box braids, dark brown with honey coloured strands mixed through, parted in the centre and pushed back. She has dark brown eyes, full lips, natural eyebrows and no makeup at all. Her fingernails are short and natural, with no polish and no extensions. She is clearly a woman and clearly in her twenties.",
  "wardrobe": "The same brown ribbed short sleeve top, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "prop": "A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card is held upright in Kris's right hand in the lower foreground, fully visible and closer to the lens than her face.",
  "scene": "The SAME real American bedroom in daylight as the reference image, lived in and unchanged, with the window on her left, the floral quilt bed behind her and the wooden dresser with a trailing pothos in a terracotta pot on the right. The table group in the lower foreground holds three classic white bordered tarot cards laid face up in a row, a chunk of green fluorite, a white selenite tower, a ceramic dish with a tall incense stick and a visible thread of smoke, and three unlit white tea lights. The wall group behind her holds a large United States flag pinned flat on the left, a wooden crucifix in the centre and two framed prints, one of a stylised sun and moon and one of a printed birth chart wheel, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Kris sits upright at the light wooden table, holding the card steady beside her cheek and looking directly into the lens. Her left hand is open and turned toward the lens. Both hands stay anatomically clear, with short natural nails.",
  "composition": "Tight chest-up talking frame. The SOULMATE card occupies the lower foreground and Kris's face fills the upper third. The bedroom stays recognizable without competing with the card.",
  "camera": "eye level, straight-on, close phone-camera distance",
  "state": "Start frame: Kris already holds the card upright beside her face and looks into the lens, her expression direct and instructive, before speaking.",
  "lighting": "Soft neutral daylight from the window on her left, cool and even on her face, with no warm cast. The tea lights are unlit and light nothing, and there is no coloured LED anywhere in the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no skin smoothing, no makeup, no long nails, no nail polish, no coloured LED light, no change of identity, no change of wardrobe"
}
```

## K09 | T5 | BODY CARTA NA MAO | EDITAR do K06

> ### ANEXAR: **1 IMAGEM**
> **1. O K06 ja aprovado**
>
> NUNCA anexar K07, K08, K09 ou K10 aqui
>
> ### EDITAR, muda so gesto, expressao e distancia

Mesmo setup, mao esquerda de volta na mesa, expressao firme e certa.

```json
{
  "shot_id": "K09_body_card_held_initial",
  "reference_use": "Use the attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real bedroom. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 24-year-old Black American woman with deep brown skin, visible pores, a natural sheen on her forehead and cheekbones, and small dark beauty marks on her forehead, on her cheek and above her lip. Her hair is in chest length box braids, dark brown with honey coloured strands mixed through, parted in the centre and pushed back. She has dark brown eyes, full lips, natural eyebrows and no makeup at all. Her fingernails are short and natural, with no polish and no extensions. She is clearly a woman and clearly in her twenties.",
  "wardrobe": "The same brown ribbed short sleeve top, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "prop": "A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card is held upright in Kris's right hand in the lower foreground, fully visible and closer to the lens than her face.",
  "scene": "The SAME real American bedroom in daylight as the reference image, lived in and unchanged, with the window on her left, the floral quilt bed behind her and the wooden dresser with a trailing pothos in a terracotta pot on the right. The table group in the lower foreground holds three classic white bordered tarot cards laid face up in a row, a chunk of green fluorite, a white selenite tower, a ceramic dish with a tall incense stick and a visible thread of smoke, and three unlit white tea lights. The wall group behind her holds a large United States flag pinned flat on the left, a wooden crucifix in the centre and two framed prints, one of a stylised sun and moon and one of a printed birth chart wheel, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Kris sits upright at the light wooden table, holding the card steady beside her cheek and looking directly into the lens. Her left hand has lowered back onto the table. Both hands stay anatomically clear, with short natural nails.",
  "composition": "Tight chest-up talking frame. The SOULMATE card occupies the lower foreground and Kris's face fills the upper third. The bedroom stays recognizable without competing with the card.",
  "camera": "eye level, straight-on, close phone-camera distance",
  "state": "Start frame: Kris already holds the card upright beside her face and looks into the lens, her expression steady and sure, before speaking.",
  "lighting": "Soft neutral daylight from the window on her left, cool and even on her face, with no warm cast. The tea lights are unlit and light nothing, and there is no coloured LED anywhere in the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no skin smoothing, no makeup, no long nails, no nail polish, no coloured LED light, no change of identity, no change of wardrobe"
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
  "reference_use": "Use the attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real bedroom. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 24-year-old Black American woman with deep brown skin, visible pores, a natural sheen on her forehead and cheekbones, and small dark beauty marks on her forehead, on her cheek and above her lip. Her hair is in chest length box braids, dark brown with honey coloured strands mixed through, parted in the centre and pushed back. She has dark brown eyes, full lips, natural eyebrows and no makeup at all. Her fingernails are short and natural, with no polish and no extensions. She is clearly a woman and clearly in her twenties.",
  "wardrobe": "The same brown ribbed short sleeve top, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "prop": "A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card is held upright in Kris's right hand in the lower foreground, fully visible and closer to the lens than her face.",
  "scene": "The SAME real American bedroom in daylight as the reference image, lived in and unchanged, with the window on her left, the floral quilt bed behind her and the wooden dresser with a trailing pothos in a terracotta pot on the right. The table group in the lower foreground holds three classic white bordered tarot cards laid face up in a row, a chunk of green fluorite, a white selenite tower, a ceramic dish with a tall incense stick and a visible thread of smoke, and three unlit white tea lights. The wall group behind her holds a large United States flag pinned flat on the left, a wooden crucifix in the centre and two framed prints, one of a stylised sun and moon and one of a printed birth chart wheel, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Kris sits upright at the light wooden table, holding the card steady beside her face and looking straight into the lens. Her left index finger enters from the lower edge and points directly toward the lens. Both hands stay anatomically clear, with short natural nails.",
  "composition": "The TIGHTEST frame of the whole video, about twenty percent closer than the talking frames. Kris's face and the SOULMATE card are the only dominant elements. The bedroom is reduced by framing alone and everything still in frame stays in sharp focus.",
  "camera": "eye level, straight-on, pushed in closer than any other frame",
  "state": "Start frame: Kris already holds the card upright beside her face and looks into the lens, her expression urgent and direct, before speaking.",
  "lighting": "Soft neutral daylight from the window on her left, cool and even on her face, with no warm cast. The tea lights are unlit and light nothing, and there is no coloured LED anywhere in the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no skin smoothing, no makeup, no long nails, no nail polish, no coloured LED light, no change of identity, no change of wardrobe"
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
  "reference_use": "Use the attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real bedroom. Preserve that same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a 24-year-old Black American woman with deep brown skin, visible pores, a natural sheen on her forehead and cheekbones, and small dark beauty marks on her forehead, on her cheek and above her lip. Her hair is in chest length box braids, dark brown with honey coloured strands mixed through, parted in the centre and pushed back. She has dark brown eyes, full lips, natural eyebrows and no makeup at all. Her fingernails are short and natural, with no polish and no extensions. She is clearly a woman and clearly in her twenties.",
  "wardrobe": "The same brown ribbed short sleeve top, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "prop": "A single physical tarot card printed on thick card stock, showing an elegant adult couple joined by a soft ribbon of light, surrounded by roses, small stars and a crescent moon, in saturated sapphire, magenta, ruby and teal. A wide mirrored silver metallic border with engraved arabesque corners catches the light as printed foil, never as glow. A metallic title band at the bottom reads SOULMATE in large serif letters. The only text anywhere in the image is that printed word on the card. The card is held upright in Kris's right hand in the lower foreground, fully visible and closer to the lens than her face.",
  "scene": "The SAME real American bedroom in daylight as the reference image, lived in and unchanged, with the window on her left, the floral quilt bed behind her and the wooden dresser with a trailing pothos in a terracotta pot on the right. The table group in the lower foreground holds three classic white bordered tarot cards laid face up in a row, a chunk of green fluorite, a white selenite tower, a ceramic dish with a tall incense stick and a visible thread of smoke, and three unlit white tea lights. The wall group behind her holds a large United States flag pinned flat on the left, a wooden crucifix in the centre and two framed prints, one of a stylised sun and moon and one of a printed birth chart wheel, all clearly visible and in sharp focus. Preserve the established room and do not invent a different location.",
  "posture": "Kris sits upright at the light wooden table, holding the card steady beside her face and looking straight into the lens. Her left hand stays below the frame edge. Both hands stay anatomically clear, with short natural nails.",
  "composition": "The TIGHTEST frame of the whole video, about twenty percent closer than the talking frames. Kris's face and the SOULMATE card are the only dominant elements. The bedroom is reduced by framing alone and everything still in frame stays in sharp focus.",
  "camera": "eye level, straight-on, pushed in closer than any other frame",
  "state": "Start frame: Kris already holds the card upright beside her face and looks into the lens, her expression certain and quietly warm, before speaking.",
  "lighting": "Soft neutral daylight from the window on her left, cool and even on her face, with no warm cast. The tea lights are unlit and light nothing, and there is no coloured LED anywhere in the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no skin smoothing, no makeup, no long nails, no nail polish, no coloured LED light, no change of identity, no change of wardrobe"
}
```

## Mapa de ancoras

| Keyframe | Referencias a anexar | Modelo |
|---|---|---|
| K01 a K06 | ancora KRIS | Nano Banana 2, 9:16 |
| K07 a K11 | o K06 aprovado | Nano Banana 2, 9:16 |

No bloco de execucao do Flow o anexo e **so a ancora KRIS** nos onze.

## Montagem no CapCut

- Timeline 1080 x 1920, 30 fps. Cortar o silencio inicial, a fala comeca no primeiro frame.
- **Um gancho por versao final.** Cinco ganchos geram cinco videos.
- Marca d'agua `222` fixa no canto superior direito o video inteiro, herdada do modelo.
- Caixa branca de texto do 0s ao 8s, com a frase escolhida pelo Luigi. Nunca gerada na imagem.
- Legenda karaoke de duas ou tres palavras, branca com destaque vermelho.
- **Seta vermelha grande apontando para a foto de perfil** entrando junto do T6 e ficando ate o fim.
- Nao cobrir a carta SOULMATE com legenda. Manter o `222` isolado visualmente no T4.
- Sem musica, ou trilha em -19 a -20 dB. Conferir lip sync e a ultima palavra de cada take.

## Gates de qualidade

1. `identity_main` dos onze comeca com `The EXACT woman`, e ela tem 24 anos em todos.
2. `no coloured LED light` no negative dos onze. Kris e de DIA.
3. Unhas curtas e naturais escritas em todo prompt que mostra as maos.
4. Bandeira dos EUA no campo `scene` dos onze, grande e esticada na parede a esquerda.
5. Heroi no lower foreground, mais perto da lente que o rosto, nos onze.
6. K10 e K11 sao o plano mais fechado do video inteiro.
7. So o estado inicial em cada imagem. A transformacao acontece no clipe.
8. Nenhum rosto de alma gemea legivel. As figuras do globo sao moldadas sem rosto.
9. Zero fogo aceso em quadro nos onze.
10. `no captions` no negative dos onze, e nenhum termo sensivel listado la.
11. Produto nunca em quadro. Sem app, sem quiz, sem celular, sem preco.
12. `python checar_entrega.py producao/manifestselizabeth` sem nenhuma FALHA.

