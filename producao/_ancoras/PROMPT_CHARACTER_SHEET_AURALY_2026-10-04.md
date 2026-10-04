# Prompt de character sheet universal · avatares Auraly (Luigi, 2026-10-04)

Um prompt só para qualquer avatar: anexar UMA imagem do avatar (a âncora em cena real) e colar o JSON
abaixo inteiro. Saída: uma folha 16:9 com um close extremo do rosto à esquerda e quatro vistas de
corpo inteiro à direita (frente, costas, lado esquerdo, lado direito). Nano Banana 2, 4 candidatas,
escolher uma.

Pedido do Luigi: *"nao quero muitos angulos, quero apenas um close extremo no rosto do avatar e mais 4
angulos de diferentes lados do avatar (frente, costas, lado esquerdo e lado direito)"*. Substitui, para
o character sheet, a grade de fingerprint reprovada em 2026-09-22 (muitos ângulos e macro de pele). As
âncoras em cena real continuam sendo a referência oficial dos K até o Luigi decidir outra coisa.

```json
{
  "format": "IMPORTANT: THIS IS A REAL PHOTOGRAPHIC CHARACTER REFERENCE SHEET, NOT AN ILLUSTRATION. Horizontal 16:9.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image as the only source for this person's exact identity: face shape, eyes, eye color, nose, lips, teeth, skin tone, skin texture, every wrinkle, freckle, mole, scar and acne mark, hair color, hairstyle, hairline, facial hair, tattoos, body type, height impression and age. Copy the clothing and jewelry exactly as they appear in the attached image. Ignore its background, props, cards and camera angle.",
  "identity_main": "The exact same person from the attached image, identical in every panel, same age as in the attached image, never younger, never more attractive, never idealized.",
  "wardrobe": "Exactly the outfit and jewelry from the attached image, identical in all five panels. If the attached image does not show the lower body, complete the outfit with plain dark blue jeans and simple everyday shoes that match the visible clothing, and keep that same completion in every panel.",
  "layout": "One single image divided into two areas with thin plain gaps and no borders, no labels. LEFT area, about 40 percent of the width, full height: one extreme close-up of the face, cropped from the top of the forehead to the chin, straight on, eyes looking into the lens, filling the panel edge to edge, every pore and skin detail visible. RIGHT area, about 60 percent of the width: four full-body standing views of the same person side by side in one row, all at exactly the same scale, head-to-toe with the feet fully visible and a little space above the head: panel 1 front view facing the camera, panel 2 back view facing away, panel 3 left side profile, panel 4 right side profile.",
  "posture": "In the four full-body views the person stands upright and relaxed in a neutral pose, arms hanging naturally at the sides with hands visible and empty, feet slightly apart, same posture in all four. In the close-up the face is relaxed and neutral with the mouth closed.",
  "scene": "Plain seamless light grey studio backdrop in every panel, no floor line, no furniture, no objects, no scenery.",
  "prop": "No props. The hands are empty in every panel.",
  "camera": "Close-up: 85mm portrait lens at eye level, straight on. Full-body views: 50mm lens at waist height, straight on, no tilt, no distortion, the same camera distance for all four.",
  "lighting": "Soft even neutral daylight-balanced studio light from the front, like an overcast day, no harsh shadows on the face or body, true natural skin color, the same light in all five panels.",
  "realism": "Real photograph look: real skin with visible pores, irregular texture, natural asymmetry, hair in uneven natural clumps with flyaways, fabric with real wrinkles, low contrast, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "16:9 horizontal",
  "negative": "no captions, no labels, no letters, no numbers, no arrows, no words overlaid on the image, no illustration, no drawing, no 3D render, no cartoon, no anime, no mannequin, no different outfits between panels, no extra people, no second person, no props, no cards, no background scenery, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no harsh shadows, no de-aging, no beauty smoothing, no plastic-looking skin, no makeup changes, no hairstyle changes, no extra fingers, no missing hands, no cropped feet, no cropped head"
}
```
