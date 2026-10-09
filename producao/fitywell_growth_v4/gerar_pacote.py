import re, sys, os
D = os.path.dirname(os.path.abspath(__file__))

ID = ("Match the attached image exactly for the woman's identity and outfit: a woman in her early thirties with long cornrow braids "
      "ending in wooden beads, freckles across her nose and cheeks, natural skin, a thin gold chain with a small cross, a floral tattoo sleeve "
      "on her right forearm, a white ribbed fitted tank top and black athletic shorts.")
SET = ("She stands in her gym behind a black padded bench: light grey cinder-block wall, a red neon sign reading TRAIN PRAY REPEAT on the left and a small "
       "American flag on the wall at the right, both in sharp focus.")
CAM = "Vertical smartphone shot, camera at chest height about one meter from the bench, level, front facing."
END = "Soft neutral even lighting, true neutral colors, real skin texture, smartphone footage look, everything in sharp focus, 9:16 vertical."

def K(hero): return f"{ID} {SET} {hero} {CAM} {END}"

T = [
 # code, beat, pt scene, EN line, PT line, hero (K), silent action (V) or None
 ("T1","Gancho 1: marcas de meia",
  "Duas panturrilhas com pés sobre o banco, coladas na lente; a da esquerda com a marca vermelha da meia, a da direita lisa; ela atrás, apontando para a marca.",
  "If your socks leave marks like this, and you want them smooth like this,",
  "Se a sua meia deixa marcas assim, e você quer a perna lisa assim,",
  "Hero: two calves with ankles and feet, standing upright on the black bench in the lower foreground, very close to the lens, large in frame and closer to the camera than her face. The left ankle has a faint red ring from a sock elastic, the right ankle is smooth. Her face and shoulders appear between and behind the legs; she looks down and points at the mark with her right index finger, lips slightly parted as if mid-sentence.",None),
 ("T2","Gancho 2: jeans que apertam",
  "Dois troncos de jeans cortados no peito, colados na lente: um jeans apertado, outro folgado; ela no meio apontando.",
  "your jeans dig into you like this, and you want them loose like this,",
  "se o seu jeans aperta assim, e você quer ele folgado assim,",
  "Hero: two people stand close on either side of her, shown from the chest to the thighs and cropped by the frame edges, very close to the lens. Both wear fitted navy tops tucked into blue jeans: the jeans on the left are tight and press into the waistband, the jeans on the right are loose and comfortable. She stands between them looking at the camera and points at the tight waistband with her right index finger, mid-sentence.",None),
 ("T3","Gancho 3: queixo",
  "Duas cabeças de manequim coladas na lente, uma de cada lado do rosto dela; queixo mais caído à esquerda, definido à direita.",
  "or your chin sags like this, and you want it defined like this,",
  "ou o seu queixo cai assim, e você quer ele definido assim,",
  "Hero: two realistic bald female display mannequin heads on neck stands, one on each side of her face, very close to the lens, large in frame and closer to the camera than her face. The left mannequin has a soft rounded chin line, the right mannequin has a sharp defined jawline. She leans slightly between them, looks at the camera and points at the left mannequin's chin with her right index finger, mid-sentence.",None),
 ("T4","Presta atenção",
  "Mesmas duas cabeças de manequim, um pouco mais atrás; ela olha direto para a câmera com um dedo levantado.",
  "pay attention, because this is the part most people never hear about.",
  "presta atenção, porque essa é a parte que a maioria das pessoas nunca ouve falar.",
  "Hero: the same two bald display mannequin heads on neck stands, one on each side of her, close to the lens and cropped by the frame edges. She stands between them looking straight at the camera with her right index finger raised near her chin, serious focused expression, mid-sentence.",None),
 ("T5","Reenquadre: não é gordura",
  "Ela ao lado de um quadro branco com seis desenhos de linha, apontando com um bastão de madeira.",
  "This is not fat, and it is not what you eat. They will say eat less and move more, but none of that touches what is causing it.",
  "Isso não é gordura, e não é o que você come. Vão dizer pra comer menos e se mexer mais, mas nada disso toca no que causa isso.",
  "Hero: a large white rolling whiteboard stands to the right of the bench, close to the lens, with six simple black marker line drawings and small handwritten labels ANKLES, SWELLING, BELLY, BLOATING, JAW, PUFFY. She turns her upper body slightly toward it, holds a wooden pointer stick against the BELLY drawing with her left hand and looks at the camera, mid-sentence.",None),
 ("T6","Receita: gengibre",
  "Panela de aço com água em primeiro plano; ela segura uma colher com gengibre ralado sobre a panela.",
  "In a pot with two cups of water, add one teaspoon of ginger,",
  "Numa panela com duas xícaras de água, coloque uma colher de chá de gengibre,",
  "Hero: a stainless steel pot with water on a portable burner on the bench, in the lower foreground, very close to the lens, large in frame. She holds a metal spoon of freshly grated ginger above the pot with her right hand and looks at the camera, mid-sentence.",None),
 ("T7","Receita: pimenta (voz-over)",
  "Macro da panela com gengibre; uma mão solta uma pitada de pimenta preta.",
  "and a pinch of black pepper,",
  "e uma pitada de pimenta preta,",
  "Hero: a stainless steel pot of water with grated ginger floating in it fills the lower two thirds of the frame, very close to the lens, seen from a high angle. A hand with a floral tattoo sleeve holds a pinch of black pepper just above the water. Above the pot the grey wall with the red neon sign and the American flag is visible. Her face is out of frame.",
  "(no speech) The hand lets a pinch of black pepper fall into the pot; a little steam rises."),
 ("T8","Receita: limão (voz-over)",
  "Macro da panela; uma mão espreme meio limão sobre a água.",
  "then squeeze in the juice of half a lemon.",
  "depois esprema o suco de meio limão.",
  "Hero: a stainless steel pot of water with grated ginger and black pepper fills the lower two thirds of the frame, very close to the lens, seen from a high angle. A hand with a floral tattoo sleeve holds half a lemon just above the water, ready to squeeze. Above the pot the grey wall with the red neon sign and the American flag is visible. Her face is out of frame.",
  "(no speech) The hand squeezes the half lemon over the pot; juice drips in; a little steam rises."),
 ("T9","Ferver",
  "Ela atrás da panela, olhando para a câmera.",
  "Boil for ten minutes,",
  "Ferva por dez minutos,",
  "Hero: the stainless steel pot with simmering water on the portable burner sits in the lower foreground, close to the lens. She stands behind it with both hands resting on the bench, looking at the camera with a calm confident expression, mid-sentence.",None),
 ("T10","Beber em jejum + gengibre",
  "Caneca de vidro com bebida âmbar fumegando, gengibre inteiro e meio limão na bancada; ela inclinada, apontando para a caneca.",
  "and drink it warm on an empty stomach every morning. The ginger helps wake up a digestion that has been sluggish for years.",
  "e beba morna em jejum toda manhã. O gengibre ajuda a acordar uma digestão que está lenta há anos.",
  "Hero: a steaming clear glass mug of amber ginger drink on the bench at the left in the lower foreground, close to the lens, with a whole ginger root and half a lemon at the right. She leans on her forearms behind the bench, looks at the camera and points down at the mug with her right index finger, mid-sentence.",None),
 ("T11","Aqui está o ponto",
  "Mesma bancada, plano mais fechado; ela gesticula com a mão aberta.",
  "Here is the thing. If your gut has been backed up for years, ginger and lemon alone cannot undo that. A morning drink moves what is already there.",
  "Aqui está o ponto. Se o seu intestino está travado há anos, gengibre e limão sozinhos não desfazem isso. Uma bebida da manhã move o que já está lá.",
  "Hero: the steaming glass mug of amber ginger drink, a whole ginger root and half a lemon on the bench in the lower foreground, close to the lens. She stands behind the bench, chest up, looks at the camera with an earnest expression and gestures with her right hand open, mid-sentence.",None),
 ("T12","Por que o inchaço volta",
  "Mesma bancada; ela com as duas mãos abertas, explicando.",
  "It does not put back the bacteria your gut needs to process food, which is why the bloating creeps back by afternoon.",
  "Ela não repõe as bactérias que o seu intestino precisa pra processar a comida, e é por isso que o inchaço volta de tarde.",
  "Hero: the steaming glass mug of amber ginger drink at the left of the bench in the lower foreground, close to the lens. She stands behind the bench, chest up, looks at the camera and holds both hands open in front of her chest as if explaining, mid-sentence.",None),
 ("T13","Solução: rotina de comida",
  "Na bancada: iogurte natural, kimchi e um copo d'água; ela com as duas mãos abertas.",
  "What rebuilds it is what you feed your gut every day: fiber, plain yogurt, kimchi, and plenty of water.",
  "O que reconstrói isso é o que você dá pro intestino todo dia: fibra, iogurte natural, kimchi e bastante água.",
  "Hero: on the bench in the lower foreground, close to the lens, a white bowl of plain yogurt, a small bowl of kimchi and a tall glass of water. She stands behind it, chest up, looks at the camera and holds both hands open in front of her chest, mid-sentence.",None),
 ("T14","Fechamento do mecanismo",
  "Mesma bancada, ela mais próxima da câmera, mãos abertas.",
  "Keep doing that, and the afternoon bloat starts to ease, because you are working on the cause, not just flushing the symptom.",
  "Continue fazendo isso, e o inchaço da tarde começa a aliviar, porque você trabalha a causa, não só descarrega o sintoma.",
  "Hero: on the bench in the lower foreground, close to the lens, a white bowl of plain yogurt, a small bowl of kimchi and a tall glass of water. She leans slightly toward the camera, chest up, looks straight at it and spreads both hands apart, mid-sentence.",None),
 ("T15","CTA + follow",
  "Só ela atrás do banco, sem objeto, olhando para a câmera com leve sorriso.",
  "Tap the link in my caption and I will show you the exact daily gut plate I eat with this. And follow me so it reaches you.",
  "Toque no link da minha legenda e eu te mostro o prato diário exato que eu como com isso. E me segue pra isso chegar até você.",
  "Hero: only her, chest up, standing close behind the black bench with both hands resting on it, no objects on the bench, looking straight at the camera with a warm slight smile, mid-sentence.",None),
]

def vprompt(t):
    if t[6]: return t[6]+"\nFixed camera. No music."
    return f'The person in the image speaks in American English, looking at the camera: "{t[3]}"\nFixed camera. Natural lip sync, no music.'

hdr = """# ENTREGA | Avatar FitWell (tranças) | FitWell Growth vídeo 4

producao: fitywell_growth_v4 · Ângulo 2 · GROWTH · rodada de VALIDAÇÃO (clone fiel) · formato mínimo de prompt do Flow

## Qual vídeo é este

**Vídeo 4: bebida de gengibre, limão e pimenta contra o inchaço (gancho das 3 comparações).**

**O que acontece:** a coach mostra 3 comparações (meia que marca, jeans que aperta, queixo caído) e diz que isso não é gordura nem o que você come. Ensina a bebida de gengibre, pimenta e limão fervida 10 min e bebida morna em jejum. Explica que a bebida sozinha não desfaz anos de intestino travado e por isso o inchaço volta de tarde, e fecha com a rotina de comida (fibra, iogurte, kimchi, água) e pede para tocar o link da legenda e seguir.

**Gancho:** abertura falada "If your socks leave marks like this, and you want them smooth like this," com duas panturrilhas coladas na lente, uma com a marca vermelha da meia, e o rosto dela entre as pernas apontando para a marca.

## 1. Anexos e mapa

- **Imagem (K):** anexar SÓ a imagem do avatar (`holistic brandon.jpg`) e colar o prompt. 4 variações, 9:16. Nada de frame modelo.
- **Vídeo (V):** anexar SÓ a imagem escolhida daquele K e colar o prompt de vídeo. 1 variação, 9:16.
- Bloco do agente Flow desta produção: `AGENTE_FLOW.md`.

```text
MAPA K/V
""" + "\n".join(f"V{i:02d}: K{i:02d}" for i in range(1,16)) + "\n```\n\n"
out = hdr + "## 2. PROMPTS DE IMAGEM (um bloco por K)\n\n"
checks=[]
for i,t in enumerate(T,1):
    k = K(t[5])
    checks.append((t[0], len(k), len(re.findall(r"\b(no|never|without|not)\b", k, re.I)), "American flag" in k, "9:16" in k))
    out += f"### K{i:02d} · {t[0]}, {t[1]} · anexar SÓ a imagem do avatar\n\nCena: {t[2]}\n\n```text\nK{i:02d}\n{k}\n```\n\n"
out += "## 3. PROMPTS DE VÍDEO (um bloco por V)\n\n"
for i,t in enumerate(T,1):
    out += f"### V{i:02d} · {t[0]}, {t[1]} · anexar SÓ a imagem escolhida do K{i:02d}\n\nCena: {t[2]}\n\n```text\nV{i:02d}\n{vprompt(t)}\n```\n\n"
out += "## 4. Transcrição final\n\n| Take | English | Português |\n|---|---|---|\n" + "\n".join(f"| {t[0]} | {t[3]} | {t[4]} |" for t in T)
out += "\n\n**EN corrido:** " + " ".join(t[3] for t in T) + "\n\n**PT corrido:** " + " ".join(t[4] for t in T) + "\n"
open(os.path.join(D,"ENTREGA_AVATAR_FITWELL.md"),"w").write(out)
ok=all(c[1]<=1900 and c[2]<=2 and c[3] and c[4] for c in checks)
for c in checks: print(c)
print("OK" if ok else "FALHA")
