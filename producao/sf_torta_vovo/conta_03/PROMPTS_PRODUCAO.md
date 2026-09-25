# Conta 3 | Short form de crescimento | Pacote de Prompts

Vídeo modelo: `Sweet Treats with Gr_A pequena surpresa de co_2818305955232419_720p_20260923.mp4`

Âncora: **nenhuma** (dupla descrita por escrito, decisão do Luigi, 2026-09-23). Anexo único do K:
`REF-COMPOSICAO` = `producao/sf_torta_vovo/REF_COMPOSICAO_frame_2s.jpg`, só para câmera e disposição.

Funil: nenhum, crescimento puro. HOOK 3 · variável: DOCE: pink cupcake.

---

## Índice de geração

| Take | Keyframe | Anexar | Ação de geração |
|---|---|---|---|
| T1, T2, T3 | K01 | REF-COMPOSICAO | GERAR DO ZERO |

Os três V partem do mesmo K01 (perfil clássico do Flow: V01, V02 e V03 usam o maior K disponível,
que é o K01).

## Trava de identidade e continuidade

- Avó: A Latina American grandmother around sixty-five, olive tan skin, dark grey hair pulled into a low bun, dark brown eyes, laugh lines and a small mole on her cheek. Roupa: a coral short-sleeved blouse under a beige apron, small gold hoop earrings.
- Neta: a Latina American girl about three years old, light tan skin, big dark eyes, wavy dark brown hair in a high ponytail with a red bow. Roupa: a white cotton dress with small red flowers, barefoot.
- Dupla exclusiva desta conta, nunca reaproveitada em outra (checklist B8).
- Luz neutra de dia nublado, zero blur, tudo em foco.

## Trava do prop herói

The quantity is absurd, like a small bakery inside a home: the whole kitchen island is covered edge to edge with baking trays of mini cupcakes with tall swirls of pink frosting in white paper liners, hundreds of them, with more trays stacked on two-tier metal stands and the back counter also lined with full trays. The nearest trays are very close to the lens in the lower foreground, large in frame, closer to the camera than the grandmother's face, nothing else competing with them.

## Trava da 2ª pessoa

A neta está descrita por escrito dentro do K01 e aparece de corpo inteiro, como no original. Sem REF.

# Prompts de imagem

## K01 · T1, T2, T3 · GERAR DO ZERO · REF-COMPOSICAO

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-COMPOSICAO** · `producao/sf_torta_vovo/REF_COMPOSICAO_frame_2s.jpg` (só câmera e disposição)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K01_conta03_pedido",
  "reference_use": "Use the attached reference frame ONLY for camera height, camera angle and the layout of the table and the two people. Do NOT copy the people, faces, hair, skin tone, clothing, desserts or room from it.",
  "fiction_note": "Both people are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "A Latina American grandmother around sixty-five, olive tan skin, dark grey hair pulled into a low bun, dark brown eyes, laugh lines and a small mole on her cheek, standing behind the kitchen island, her age fully visible and never smoothed.",
  "identity_second": "A small granddaughter: a Latina American girl about three years old, light tan skin, big dark eyes, wavy dark brown hair in a high ponytail with a red bow, standing on the ground in front of the right end of the kitchen island, so small that her head only reaches the edge of the kitchen island.",
  "wardrobe": "Grandmother: a coral short-sleeved blouse under a beige apron, small gold hoop earrings. Granddaughter: a white cotton dress with small red flowers, barefoot.",
  "prop": "The quantity is absurd, like a small bakery inside a home: the whole kitchen island is covered edge to edge with baking trays of mini cupcakes with tall swirls of pink frosting in white paper liners, hundreds of them, with more trays stacked on two-tier metal stands and the back counter also lined with full trays. The nearest trays are very close to the lens in the lower foreground, large in frame, closer to the camera than the grandmother's face, nothing else competing with them.",
  "scene": "A bright American home kitchen with white shaker cabinets and a large window behind the grandmother letting in neutral overcast daylight, the backyard trees and a grey-blue cloudy sky clearly visible through the window, never white or blown out, a light wood floor, and a small American flag standing in a mason jar on the windowsill, discreet but clearly visible and in sharp focus.",
  "posture": "The grandmother stands behind the kitchen island with both hands resting on its edge, leaning slightly forward and looking down at her granddaughter with an amused smile. The granddaughter stands on her tiptoes at the right end of the kitchen island stretching one arm up toward one of the pink cupcakes on the nearest tray, her face turned up to her grandmother.",
  "composition": "The trays of pink cupcakes fill the lower left and lower middle of the frame, closest to the lens. The grandmother is seen from the waist up behind them in the upper middle. The granddaughter is seen head to toe at the lower right.",
  "camera": "phone held high at adult head height, angled slightly down, straight-on across the kitchen island, as in the reference frame",
  "state": "Start frame: the granddaughter is already reaching and already asking, caught mid-sentence, lips naturally parted, eager pleading expression with wide eyes; the grandmother is holding back a laugh.",
  "lighting": "Neutral overcast daylight, soft even light on both faces with no harsh shadows, no warm orange cast and no yellow tint.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry on both faces, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no night scene, no dark windows, no beauty smoothing, no de-aging, no third person, no people copied from the reference frame"
}
```

## Bloco global de vídeo

```text
[quem fala: a neta ou a avó] fala em inglês com sotaque americano, [voz do personagem], [emoção da fala], a seguinte frase: "[FALA EXATA DO ROTEIRO]"

[quem fala] diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. [quem fica calado]

o que acontece no vídeo: [ação ENXUTA]

câmera: fixa, na mão de alguém da família, com leve tremor natural de celular

som ambiente: cozinha de casa silenciosa, sem música
```

# Prompts de vídeo

### V01 · T1 · usa K01

```text
a neta (menina de uns três anos, a criança na frente da bancada) fala em inglês com sotaque americano, voz infantil aguda e animada de menina de uns três anos, falando devagar, manhosa, pedindo com muita vontade, a seguinte frase: "Grandma, please let me eat that pink cupcake now. I really want it."

a neta diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. A avó fica calada enquanto a neta fala.

o que acontece no vídeo: a neta estica a mão para um dos doces da bandeja mais próxima olhando para a avó enquanto pede; quando a neta termina, a avó joga a cabeça para trás e solta uma risada alta, com a mesma voz dela (voz de avó americana de uns sessenta e cinco anos, cheia e calorosa, com leve sotaque hispânico).

câmera: fixa, na mão de alguém da família, com leve tremor natural de celular

som ambiente: cozinha de casa silenciosa, sem música
```

### V02 · T2 · usa K01

```text
a avó (a senhora atrás da bancada) fala em inglês com sotaque americano, voz de avó americana de uns sessenta e cinco anos, cheia e calorosa, com leve sotaque hispânico, ainda rindo e em tom de brincadeira, olhando para a câmera, a seguinte frase: "Okay, if people comment yes and follow this page, you can choose first."

a avó diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. A neta fica calada, só olhando para a avó.

o que acontece no vídeo: a avó tira os olhos da neta, vira o rosto para a câmera e fala com quem está assistindo, no fim aponta de leve para a neta; a neta continua com a mão perto da bandeja, olhando para cima para a avó.

câmera: fixa, na mão de alguém da família, com leve tremor natural de celular

som ambiente: cozinha de casa silenciosa, sem música
```

### V03 · T3 · usa K01

```text
a neta (menina de uns três anos, a criança na frente da bancada) fala em inglês com sotaque americano, voz infantil aguda e animada de menina de uns três anos, falando devagar, manhosa, implorando com os olhos arregalados, a seguinte frase: "Please comment yes and follow. I want to choose this pink cupcake right now."

a neta diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. A avó fica calada, só sorrindo.

o que acontece no vídeo: a neta vira de frente para a câmera, junta as duas mãos na frente do peito em súplica e dá pulinhos no lugar enquanto pede; a avó sorri atrás da bancada.

câmera: fixa, na mão de alguém da família, com leve tremor natural de celular

som ambiente: cozinha de casa silenciosa, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | REF-COMPOSICAO (`producao/sf_torta_vovo/REF_COMPOSICAO_frame_2s.jpg`) | Nano Banana 2, 9:16, 1 imagem final |

Vídeo: Veo 3.1 Lite, Lower Priority, 8 segundos, 1 variação, K01 como INITIAL FRAME de V01, V02 e V03.

---

## Montagem no CapCut

1. Ordem: clipe 1 = V01, clipe 2 = V02, clipe 3 = V03.
2. V02 e V03 começam na mesma pose do K01: cortar o início até o primeiro movimento, para a
   emenda parecer contínua. Todo clipe começa já falando; `Isolate Voice` no áudio.
3. Cortar a risada do fim do V01 se o vídeo passar de 20s.
4. Texto de tela só no T1: `Grandma, please let me eat that pink cupcake`.
5. Legenda da fala nos três clipes.
6. Sem música e sem Voice Changer.
7. Rótulo pequeno `AI-generated` num canto.
8. Exportar em 9:16, 1080 por 1920.

---

## Gates de qualidade

1. [ ] As bandejas de pink cupcake estão no lower foreground, mais perto da lente que o rosto da avó.
2. [ ] Escala de confeitaria: bancada coberta de ponta a ponta e bandejas em suportes de dois andares.
3. [ ] A bandeira dos EUA aparece e está em foco.
4. [ ] A dupla não lembra o vídeo modelo nem as duplas das outras contas.
5. [ ] Luz neutra de dia nublado, janela ou céu com cor, zero tom quente, zero blur.
6. [ ] Rostos nítidos, sem sombra dura, boca da neta entreaberta.
7. [ ] Em V02 só a avó fala; em V01 e V03 só a neta fala.
8. [ ] A fala de cada V bate palavra por palavra com o `ROTEIRO.md`.
9. [ ] `python3 checar_entrega.py producao/sf_torta_vovo/conta_03` fechou sem FALHA.
