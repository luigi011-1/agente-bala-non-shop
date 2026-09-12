# Prompts de imagem · `sexta_pessoa` · Auraly soulmate · versão 2

Pacote canônico da seleção atual. Ele preserva `PROMPTS_IMAGEM.md` como histórico de uma seleção anterior e não reutiliza seus keyframes.

```json
{
  "artifact_type": "auraly_soulmate_image_prompt_package",
  "version": 2,
  "created_at": "2026-09-08T14:32:39.373902+00:00",
  "pipeline": "auraly_soulmate",
  "angle": 3,
  "production_id": "sexta_pessoa",
  "source_script": {
    "path": "ROTEIRO.md",
    "sha256": "39eef5572a74789da9cd063021bc1ca8bac26326ad5ad8e36e815737b2cb107c"
  },
  "hook_selection": {
    "sha256": "a78277972ad1b4aba7140ca9633789b51a9eb06858ec0129c45de304336d1045",
    "hook_ids": [
      "user_explicit_card_pull_camera",
      "user_explicit_salt_circle_closing",
      "artifact_option_8"
    ],
    "options_artifact_sha256": "02f9c6f7927deafadd98c51bb69d4949000db08cee12beb1b98f15f6b347a9ea"
  },
  "assets": [
    {
      "asset_id": "K01_hook_card_pull_camera",
      "role": "hook",
      "hook_id": "user_explicit_card_pull_camera",
      "title": "Carta puxada rapidamente para a câmera",
      "takes": [
        "T1"
      ],
      "action": "GERAR DO ZERO"
    },
    {
      "asset_id": "K02_hook_salt_circle_closing",
      "role": "hook",
      "hook_id": "user_explicit_salt_circle_closing",
      "title": "Círculo de sal se fechando ao redor da carta",
      "takes": [
        "T1"
      ],
      "action": "GERAR DO ZERO"
    },
    {
      "asset_id": "K03_hook_honey_over_card",
      "role": "hook",
      "hook_id": "artifact_option_8",
      "title": "Mel sendo derramado sobre a carta",
      "takes": [
        "T1"
      ],
      "action": "GERAR DO ZERO"
    },
    {
      "asset_id": "K04_body_reading_t2_t4",
      "role": "body",
      "hook_id": null,
      "title": "Body / leitura da versão atual do roteiro",
      "takes": [
        "T2",
        "T3",
        "T4"
      ],
      "action": "GERAR DO ZERO"
    },
    {
      "asset_id": "K05_cta_stories_t5",
      "role": "cta",
      "hook_id": null,
      "title": "CTA Stories da versão atual do roteiro",
      "takes": [
        "T5"
      ],
      "action": "EDITAR do K04_body_reading_t2_t4"
    }
  ],
  "supersedes": "PROMPTS_IMAGEM.md"
}
```

## Índice lógico

| Asset | Papel | Takes | Ação |
|---|---|---|---|
| `K01_hook_card_pull_camera` | hook | T1 | GERAR DO ZERO |
| `K02_hook_salt_circle_closing` | hook | T1 | GERAR DO ZERO |
| `K03_hook_honey_over_card` | hook | T1 | GERAR DO ZERO |
| `K04_body_reading_t2_t4` | body | T2, T3, T4 | GERAR DO ZERO |
| `K05_cta_stories_t5` | cta | T5 | EDITAR do K04_body_reading_t2_t4 |

## Regras de execução por avatar

Use a âncora do avatar ativo como primeira referência e a `REF-CARTA` aprovada como segunda referência nos quatro assets GERAR DO ZERO. O CTA edita exclusivamente o K04 aprovado. A âncora é fonte de identidade e cenário; nada no cenário pode mudar. Não gerar imagens por este documento: ele só define os prompts.

## K01_hook_card_pull_camera · HOOK · CARTA PUXADA RAPIDAMENTE PARA A CÂMERA · GERAR DO ZERO

> ### 📎 ANEXAR: **2 IMAGEMENS**
> **1️⃣ ÂNCORA ATIVA DO AVATAR**
> **2️⃣ REF-CARTA SOULMATE aprovada**
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K01_hook_card_pull_camera",
  "reference_use": "Use the first attached image ONLY for the active avatar's exact face, identity, skin, hair, wardrobe and the exact scene. Use the second attached image ONLY for the exact art of the SOULMATE tarot card. Keep the attached avatar scene exactly identical: same room, background anchors, objects, positions, framing and lighting. Do NOT copy the pose of either reference.",
  "identity_main": "The EXACT woman from the first attached anchor image. Preserve her real age cues, skin texture, marks, hair, wardrobe, jewelry and proportions exactly as in the anchor. No beauty treatment, no age change, no identity drift.",
  "prop": "The exact holographic SOULMATE tarot card from the second attachment, held upright in her hand in the lower foreground. The card is much closer to the lens than her face, fully inside frame, large and sharp, its art readable.",
  "scene": "The SAME real scene from the active avatar anchor, unchanged. Keep the US flag visible and in sharp focus, plus only the two most recognizable existing room anchors. Do not invent, add, remove, rearrange or blur background elements.",
  "posture": "Chest-up, facing the camera. Her arm has just started a fast direct pull of the card toward the lens; the start frame freezes the card close and sharp before motion, with direct eye contact above it.",
  "composition": "Single shot, pushed in close. The card is the isolated hero in the lower foreground and fills much of the lower half. Her face remains visible above it. Nothing competes with the card.",
  "camera": "chest level, straight-on, close phone-camera framing",
  "state": "Start frame: the card has just begun moving rapidly toward the camera and is already close to the lens, perfectly sharp and fully framed.",
  "lighting": "Soft neutral daylight of an overcast day, matching the attached room exactly. No warm cast on skin or room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the background walls, furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no phone in frame, no motion blur, no card covering the face"
}
```

## K02_hook_salt_circle_closing · HOOK · CÍRCULO DE SAL SE FECHANDO AO REDOR DA CARTA · GERAR DO ZERO

> ### 📎 ANEXAR: **2 IMAGEMENS**
> **1️⃣ ÂNCORA ATIVA DO AVATAR**
> **2️⃣ REF-CARTA SOULMATE aprovada**
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K02_hook_salt_circle_closing",
  "reference_use": "Use the first attached image ONLY for the active avatar's exact face, identity, skin, hair, wardrobe and the exact scene. Use the second attached image ONLY for the exact art of the SOULMATE tarot card. Keep the attached avatar scene exactly identical: same room, background anchors, objects, positions, framing and lighting. Do NOT copy the pose of either reference.",
  "identity_main": "The EXACT woman from the first attached anchor image. Preserve her real age cues, skin texture, marks, hair, wardrobe, jewelry and proportions exactly as in the anchor. No beauty treatment, no age change, no identity drift.",
  "prop": "The exact holographic SOULMATE tarot card from the second attachment lying flat in the center of a shallow matte ceramic tray on the table. A thick, clearly visible ring of coarse white salt surrounds the card, with one small final gap nearest her fingertips.",
  "scene": "The SAME real scene from the active avatar anchor, unchanged. Keep the US flag visible and in sharp focus, plus only the two most recognizable existing room anchors. Do not invent, add, remove, rearrange or blur background elements.",
  "posture": "Chest-up, facing the camera. One hand is in the lower foreground, fingertips beginning to sweep the final gap of salt closed around the card; the other hand stays relaxed beside the tray.",
  "composition": "Single shot, camera pushed close and slightly high toward the tray. The salt circle and card are the isolated hero in the lower foreground, closer to the lens than her face. The face stays visible above the tray.",
  "camera": "chest level, slightly high toward the ceramic tray, close phone-camera framing",
  "state": "Start frame: the salt ring is almost closed, leaving one unmistakable small gap directly under her fingertips. The card is centered, uncovered and sharp.",
  "lighting": "Soft neutral daylight of an overcast day, matching the attached room exactly. No warm cast on skin or room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the background walls, furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no phone in frame, no glass bowl, no thin scattered salt, no completed closed circle yet"
}
```

## K03_hook_honey_over_card · HOOK · MEL SENDO DERRAMADO SOBRE A CARTA · GERAR DO ZERO

> ### 📎 ANEXAR: **2 IMAGEMENS**
> **1️⃣ ÂNCORA ATIVA DO AVATAR**
> **2️⃣ REF-CARTA SOULMATE aprovada**
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K03_hook_honey_over_card",
  "reference_use": "Use the first attached image ONLY for the active avatar's exact face, identity, skin, hair, wardrobe and the exact scene. Use the second attached image ONLY for the exact art of the SOULMATE tarot card. Keep the attached avatar scene exactly identical: same room, background anchors, objects, positions, framing and lighting. Do NOT copy the pose of either reference.",
  "identity_main": "The EXACT woman from the first attached anchor image. Preserve her real age cues, skin texture, marks, hair, wardrobe, jewelry and proportions exactly as in the anchor. No beauty treatment, no age change, no identity drift.",
  "prop": "The exact holographic SOULMATE tarot card from the second attachment lies flat in a shallow light ceramic bowl on the table. A spoon held by her hand begins pouring one thick amber stream of honey onto the card; the card remains mostly visible and readable at the start frame.",
  "scene": "The SAME real scene from the active avatar anchor, unchanged. Keep the US flag visible and in sharp focus, plus only the two most recognizable existing room anchors. Do not invent, add, remove, rearrange or blur background elements.",
  "posture": "Chest-up, facing the camera. Her hand holds the spoon above the lower-foreground bowl; the honey stream has just started. Her other hand rests naturally beside the bowl.",
  "composition": "Single shot, camera pushed close and slightly high toward the bowl. The ceramic bowl, honey stream and card are the isolated hero in the lower foreground, closer to the lens than her face. The face stays visible above it.",
  "camera": "chest level, slightly high toward the ceramic bowl, close phone-camera framing",
  "state": "Start frame: one thick amber stream has just started falling from the spoon onto the card; the card is not submerged and remains readable.",
  "lighting": "Soft neutral daylight of an overcast day, matching the attached room exactly. The amber color belongs only to the honey, never to the room lighting.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the background walls, furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no phone in frame, no glass bowl, no card already submerged, no room lit by amber or candlelight"
}
```

## K04_body_reading_t2_t4 · BODY · BODY / LEITURA DA VERSÃO ATUAL DO ROTEIRO · GERAR DO ZERO

> ### 📎 ANEXAR: **2 IMAGEMENS**
> **1️⃣ ÂNCORA ATIVA DO AVATAR**
> **2️⃣ REF-CARTA SOULMATE aprovada**
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K04_body_reading_t2_t4",
  "reference_use": "Use the first attached image ONLY for the active avatar's exact face, identity, skin, hair, wardrobe and the exact scene. Use the second attached image ONLY for the exact art of the SOULMATE tarot card. Keep the attached avatar scene exactly identical: same room, background anchors, objects, positions, framing and lighting. Do NOT copy the pose of either reference.",
  "identity_main": "The EXACT woman from the first attached anchor image. Preserve her real age cues, skin texture, marks, hair, wardrobe, jewelry and proportions exactly as in the anchor. No beauty treatment, no age change, no identity drift.",
  "prop": "The exact holographic SOULMATE tarot card from the second attachment, held in her right hand at chest height in the lower foreground, angled toward the lens with its art readable. Her left hand is free for the speaking gestures in T2 through T4.",
  "scene": "The SAME real scene from the active avatar anchor, unchanged. Keep the US flag visible and in sharp focus, plus only the two most recognizable existing room anchors. Do not invent, add, remove, rearrange or blur background elements.",
  "posture": "Chest-up, upright, direct eye contact with the lens. She holds the card steady in the lower foreground while speaking in an intimate, certain reading tone.",
  "composition": "Single continuous Setup B for T2, T3 and T4. Chest-up and closer than the hook frames. The card is closer to the lens than her face but never covers it. The face fills a substantial part of frame; only the required room anchors remain visible.",
  "camera": "chest level, straight-on, close phone-camera framing",
  "state": "Start frame: she has just raised the card and is beginning T2. Her mouth is ready to speak, with the card stable and readable.",
  "lighting": "Soft neutral daylight of an overcast day, matching the attached room exactly. No warm cast on skin or room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the background walls, furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no phone in frame, no card covering the face"
}
```

## K05_cta_stories_t5 · CTA · CTA STORIES DA VERSÃO ATUAL DO ROTEIRO · EDITAR do K04_body_reading_t2_t4

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ K04_body_reading_t2_t4 aprovado**
>
> ### ✏️ EDITAR do K04 aprovado; nunca anexar o CTA a si mesmo

```json
{
  "task": "edit the attached K04 image, keep everything identical except the changes listed",
  "keep_identical": "Keep the active avatar exactly the same: same face, skin texture, hair, wardrobe, jewelry, body position, exact SOULMATE card art, exact room, US flag, existing background anchors, lighting and camera height.",
  "change_1": "Push the framing in by about fifteen percent so this is the tightest frame of the video, chest-up moving toward shoulders-up, with her face dominant and direct eye contact.",
  "change_2": "Lower the SOULMATE card slightly and move it a little to her side while keeping it readable, leaving the lower-left corner clean and open for the edit arrow added later.",
  "change_3": "Give her a more urgent but intimate expression, as she begins T5 and directs the viewer to tap her profile picture and watch Stories.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the background walls, furniture and details. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no phone in frame, no arrow drawn in the image, no card covering the face"
}
```
