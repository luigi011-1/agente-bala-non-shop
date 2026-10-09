# ENTREGA | Jordan Vale | Auraly Venda Prosperidade v1 (SALE)

Produção `auraly_venda_prosperidade_v1` · Ângulo 3 · SALE (dinheiro e prosperidade) · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY

## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI

Colar inteiro na memória do agente antes do K01 (versão só desta produção: `AGENTE_FLOW.md`).

```text
# Agente do Flow, produção atual: Auraly App

Você é o executor do Google Flow. Você só gera imagens e vídeos a partir de prompts prontos. Você não cria, não edita e não melhora prompt.

## Produção atual
- Conta: Auraly App, vídeo de venda sobre dinheiro e prosperidade: "3 sinais de uma casa abençoada".
- Esta produção tem 1 imagem (K01) e 15 vídeos (V01 a V15). Todo V usa a imagem escolhida do K01.
- Avatares: Avery Knox, Devon Price e Jordan Vale. Um avatar por vez, o que o operador disser que está ativo.

## O que é anexado (só isto, nada mais)
- IMAGEM (K): você recebe o character sheet do avatar ativo. Anexe só ele e cole o prompt.
- VÍDEO (V): você recebe a imagem que o operador escolheu daquele K. Anexe só ela e cole o prompt de vídeo.
- Não existe frame modelo, anchor, referência de cenário nem segunda imagem. O cenário, a pose, a câmera e a ação já estão escritos dentro de cada prompt. Se algo no pacote falar de frame modelo, ignore e siga. Pare só se faltar o character sheet (K) ou a imagem escolhida (V).

## Imagem (código K01)
1. Modelo: Nano Banana 2.1 (no menu: Pro, 2 Lite e 2.1; use só o 2.1). Formato: 9:16 vertical.
2. Gere 4 variações por prompt. Confira o 4 e o 9:16 antes de CADA K, porque a tela volta sozinha para 1.
3. Cole o prompt inteiro, de `{` até `}`, sem o código K01, sem resumir, sem alterar uma palavra.
4. Nomeie as quatro: `K01-1`, `K01-2`, `K01-3`, `K01-4`.
5. Se saírem menos de 4, ou formato diferente de 9:16, gere de novo com o MESMO prompt e o MESMO character sheet até existirem 4 em 9:16.
6. Gere o K01 do avatar e PARE. Avise: "K01 pronto, 4 imagens. Aguardando sua escolha." Não escolha, não apague e não gere vídeo.
7. O operador apaga 3 de cada K e deixa 1 escolhida a dedo. Nunca questione e nunca recrie uma imagem apagada.

## Vídeos (códigos V01, V02...)
1. Só começa quando o operador mandar. Todos os V (V01 a V15) usam a imagem que sobrou do K01. Se o K01 tiver mais de uma imagem ou nenhuma, pare e pergunte qual.
2. Modelo: Veo 3.1 - Lite (use só esse). Duração: 8 segundos. Formato: 9:16. Imagem entra como INITIAL FRAME, nunca como ingredient ou elemento.
3. Gere 1 variação por V. Confira o 1 antes de cada V.
4. O campo de texto recebe só o prompt V, inteiro, sem alterar uma palavra. Antes de enviar, confirme que ele contém `o que acontece no vídeo:`, `câmera:` e `som ambiente:`. Se faltar, é prompt de imagem: pare e avise.
5. Todos os V desta produção são de fala: cada um traz uma frase entre aspas, que é literal.
6. No máximo 7 V por vez (lotes: V01 a V07, V08 a V14, V15). Terminou o lote, relate e espere o operador dizer `prossiga`.

## Falhou, censura ou bloqueio
- Se a geração falhar, cair na censura, der erro ou o prompt for bloqueado: refaça com o MESMO prompt, sem trocar, cortar ou suavizar uma palavra, e tente de novo até aquele item sair.
- Não pare e não passe para o próximo item sem avisar qual está pendente. Se precisar seguir, diga: "K01 ainda pendente, tentativas: N."
- Você nunca reescreve prompt, mesmo que ache que ajudaria. Só o operador altera.
- Se a interface não permitir 9:16, 4 variações (imagem) ou 1 variação (vídeo), avise antes de mudar qualquer configuração.

## Relatório de status
Depois de cada K ou V, diga: avatar, código, resultado (pronto, tentando de novo, pendente) e quantas tentativas. No fim do lote, liste concluídos e pendentes. Geração de um avatar não conclui a fila: espere o operador dizer qual é o próximo avatar e anexe o novo character sheet. Nunca misture avatares.

## Regras gerais
- Não adicione música, legenda, texto ou tradução.
- A fala do prompt é literal. Não corrija nem complete.
- Em caso de dúvida real (pacote incompleto, código duplicado, anexo faltando), pare e pergunte em uma linha.
```

Checklist de envio: 32/32 aprovados (N/A: A1 a A4 e A10 fiéis ao modelo, hook fiel da validação; C3 a C7 sem segunda pessoa, selfie, frase curta repetida, cena atuada ou motion control)

Ficha: 1/1 K conferido contra o frame do modelo, placar 14/14 (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos e mapa

- **Imagem (K01):** anexar SÓ o character sheet de Jordan Vale (`producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg`) e colar o prompt. 4 variações, 9:16.
- **Vídeo (V):** anexar SÓ a imagem escolhida do K01 e colar o prompt. 1 variação, 9:16.

```text
MAPA K/V
V01: K01
V02: K01
V03: K01
V04: K01
V05: K01
V06: K01
V07: K01
V08: K01
V09: K01
V10: K01
V11: K01
V12: K01
V13: K01
V14: K01
V15: K01
```

## 2. PROMPT DE IMAGEM

### K01 · T1 a T15 · anexar SÓ o CHARACTER SHEET

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached character sheet only for Jordan Vale's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. The setting, camera angle, pose and framing are described in full in the scene, camera and composition fields; no other image is attached.",
  "identity_main": "The exact fictional AI character Jordan Vale, explicitly male: white American man around sixty-eight, slim, full silver-white hair swept back, round thin gold-rimmed glasses, light blue-grey eyes, fair skin with freckles, age spots and deep forehead lines, light grey stubble.",
  "wardrobe": "Cream dinner jacket with peak lapels over a white dress shirt with a black bow tie, black tuxedo trousers, a gold wristwatch on the left wrist and a gold ring on the left hand.",
  "scene": "The grand salon of a luxury mansion, the reference video's living room made grander: on the left a floor-to-ceiling arched window with a dark steel frame looking out over a manicured estate garden with a tall dark-green cypress and a stone fountain under a clear blue sky with soft white clouds, with tall green potted palms in front of the window; behind the person on the right a floor-to-ceiling built-in dark wooden bookcase with a rolling library ladder, full of closed hardcover books with blank spines; polished cream marble floor with an inlaid patterned border and the edge of a cream silk sofa with a gold cushion at the far left. In the lower right foreground stands a polished dark-wood console table with a cream marble top and carved gilded legs; on it a large gold embossed planter shaped like an urn holds a green leafy plant with a small American flag (discreet but visible and in focus) tucked into the soil, next to a stack of two closed hardcover books with blank spines.",
  "prop": "Nothing is held in either hand. The left hand of Jordan Vale, his slim, freckled hand with a gold ring, rests flat on the polished top of the console table beside the gold planter.",
  "posture": "Jordan Vale stands upright and relaxed, slightly left of center, facing the lens, the right hand raised in a loose fist at chest height (on the viewer's left), the left hand resting flat on the console table (on the viewer's right), looking straight into the lens.",
  "composition": "The polished console table is very close to the lens in the lower right foreground, its near end about 28 inches from the lens, about 20 percent of the frame, closer to the camera than his face, nothing else competing with it. Jordan Vale stands about 4 feet behind it, framed from the top of the head (about 12 percent from the top edge) to mid-thigh, his face in the upper third, about 5 feet from the lens. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone fixed on a tripod at chest height about 4.5 feet above the floor, about 5 feet from the person, 1x lens, pointing level, fixed",
  "lighting": "Neutral overcast daylight coming in from the arched window on the left, cool and even, the sky outside a clear blue with soft white cloud texture, never white or blown out, the lamps switched off, soft even light on the face and body with no harsh shadows.",
  "state": "Start frame: Jordan Vale caught mid-sentence, lips naturally parted, calm confident expression, the fist at the chest held still.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no letters or writing anywhere in the room, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no glowing objects, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no religious symbols, no framed text on the wall, no candles, no tarot cards, no hand holding anything, no shoes visible, no text on the books"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · anexar SÓ a imagem escolhida do K01

```text
V01
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom firme e protetor, voz autêntica, dinâmica e emocional, a seguinte frase: "If your home has one of these three signs, don't sell it. And no, it's not about how big the house is. Don't even think about moving, my friend."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando fixo para a lente e ergue o indicador da mão direita, apontando para a lente na frase 'don't sell it'. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

### V02 · T2 · anexar SÓ a imagem escolhida do K01

```text
V02
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom confessional e baixo, voz autêntica, dinâmica e emocional, a seguinte frase: "I used to tell people to chase prosperity: new job, tighter budget, longer prayers. I did all of it. Then I learned it was never about chasing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale balança a cabeça de leve, como quem se arrepende, olhando para a lente. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

### V03 · T3 · anexar SÓ a imagem escolhida do K01

```text
V03
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom sério e comovido, voz autêntica, dinâmica e emocional, a seguinte frase: "My aunt Loretta, sixty-four, played by every rule. Two jobs, no vacations, four hundred dollars set aside each month, and each month it disappeared. Eleven years of that."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com um pequeno aceno de cabeça no fim de cada frase curta. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

### V04 · T4 · anexar SÓ a imagem escolhida do K01

```text
V04
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom reflexivo e honesto, voz autêntica, dinâmica e emocional, a seguinte frase: "One day she said, I've heard every teacher, every prayer, every plan. Why is this different? I couldn't answer. So I sat down and asked Archangel Jophiel."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale faz uma pausa curta antes de 'I couldn't answer' e depois olha para a lente com firmeza. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

### V05 · T5 · anexar SÓ a imagem escolhida do K01

```text
V05
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom revelador e calmo, voz autêntica, dinâmica e emocional, a seguinte frase: "What came back wasn't about her money. It was about her house. Most people look for prosperity outside, never realizing they already live where it was sent."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale abre a mão direita com a palma para cima e depois aponta para baixo, como quem mostra a casa. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

### V06 · T6 · anexar SÓ a imagem escolhida do K01

```text
V06
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom caloroso e sereno, voz autêntica, dinâmica e emocional, a seguinte frase: "Sign one: the plants in your home grow with ease, whether it's one small pot or a whole garden. When life blooms inside a house, opportunity blooms too."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale ergue um dedo da mão direita na primeira frase, o sinal um. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

### V07 · T7 · anexar SÓ a imagem escolhida do K01

```text
V07
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom caloroso e sereno, voz autêntica, dinâmica e emocional, a seguinte frase: "Sign two: your home gets good light during the day. Light brings clarity, joy and movement. A house full of light keeps prosperity's door open."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale ergue dois dedos da mão direita na primeira frase, o sinal dois. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

### V08 · T8 · anexar SÓ a imagem escolhida do K01

```text
V08
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom sereno e acolhedor, voz autêntica, dinâmica e emocional, a seguinte frase: "Sign three: nature comes close to your home. Birds, butterflies, even bees keep showing up, because they recognize a place where there is harmony. Peace, and blessing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale ergue três dedos da mão direita na primeira frase, o sinal três. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

### V09 · T9 · anexar SÓ a imagem escolhida do K01

```text
V09
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom baixo, de segredo, voz autêntica, dinâmica e emocional, a seguinte frase: "What nobody teaches: three signs prove the blessing is in your house, not that it stays. The problem isn't that it never arrives. It's that nothing holds it."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale se inclina um pouco para a lente e baixa a voz no segredo, com o indicador da mão direita levantado. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

### V10 · T10 · anexar SÓ a imagem escolhida do K01

```text
V10
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom calmo e didático, voz autêntica, dinâmica e emocional, a seguinte frase: "It comes in, nothing closes behind it, and it drains out. Like a bathtub with the stopper out: run the faucet eleven years and it never fills."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale desenha no ar uma linha descendente com a mão direita, como a água escorrendo, enquanto fala. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

### V11 · T11 · anexar SÓ a imagem escolhida do K01

```text
V11
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom solene e firme, voz autêntica, dinâmica e emocional, a seguinte frase: "Jophiel called it the Sunrise Seal. One minute, at first light, inside your home. No new job, no tighter budget, no longer prayers. It closes what was always open."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala devagar, olhando fixo para a lente, e fecha a mão direita em punho solto no peito na última frase. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

### V12 · T12 · anexar SÓ a imagem escolhida do K01

```text
V12
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom aliviado e carinhoso, voz autêntica, dinâmica e emocional, a seguinte frase: "Loretta did it. She stopped checking her bank app at night. She sleeps till morning now. I only wish I had known it eleven years sooner, for her sake."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale sorri de leve ao falar de Loretta e depois fica sério na última frase. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

### V13 · T13 · anexar SÓ a imagem escolhida do K01

```text
V13
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom firme e direto, voz autêntica, dinâmica e emocional, a seguinte frase: "If you follow every rule and the money still leaves, comment 222 and tell me how many signs your home has. That ties this seal to your name."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale aponta para baixo, para os comentários, e depois para a lente. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

### V14 · T14 · anexar SÓ a imagem escolhida do K01

```text
V14
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom sério e urgente, voz autêntica, dinâmica e emocional, a seguinte frase: "Like and save this, so the blessing holds stronger. Loretta's drain stayed open eleven years, and all she earned ran out. Follow me, so you don't lose what's next."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, a mão direita no peito, e ergue o dedo ao dizer 'Follow me'. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

### V15 · T15 · anexar SÓ a imagem escolhida do K01

```text
V15
o avatar Jordan Vale (homem) fala em inglês com sotaque americano refinado da Costa Leste, voz masculina grave, polida e calma de um homem rico de sessenta e oito anos, em tom acolhedor e próximo, voz autêntica, dinâmica e emocional, a seguinte frase: "Now tap my profile picture and open my stories. The Sunrise Seal is waiting for you there, and getting there takes a few seconds. Blessings, my friend."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale se inclina um pouco para a lente e aponta para ela com a mão direita, sorrindo de leve no 'Blessings, my friend'. A mão esquerda continua apoiada na console e a sala atrás não muda.

câmera: fixa, sem movimento

som ambiente: sala de mansão silenciosa, leve eco natural da voz, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V15.
2. Zero tempo morto: todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / Keep Vocal. Todos saem do mesmo frame (K01), então a troca de clipe fica no mesmo enquadramento, como no modelo (plano único).
3. Legenda karaokê branca em caixa alta com contorno preto, uma palavra por vez, no centro-baixo do quadro, do V01 ao V15, como o modelo.
4. Texto de tela do gancho no V01 (CapCut, nunca no K): "These three signs? Don't even think about moving."
5. No V15, seta apontando para a foto de perfil.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Som ambiente baixo, sem música por baixo da fala.
8. Rótulo pequeno `AI-generated` num canto do vídeo.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | If your home has one of these three signs, don't sell it. And no, it's not about how big the house is. Don't even think about moving, my friend. | Se a sua casa tem um destes três sinais, não a venda. E não, não é sobre o tamanho da casa. Nem pense em se mudar, meu amigo. |
| T2 | I used to tell people to chase prosperity: new job, tighter budget, longer prayers. I did all of it. Then I learned it was never about chasing. | Eu costumava dizer às pessoas para correrem atrás de prosperidade: emprego novo, orçamento mais apertado, orações mais longas. Eu fiz tudo isso. Aí aprendi que nunca foi sobre correr atrás. |
| T3 | My aunt Loretta, sixty-four, played by every rule. Two jobs, no vacations, four hundred dollars set aside each month, and each month it disappeared. Eleven years of that. | Minha tia Loretta, de sessenta e quatro anos, seguiu todas as regras. Dois empregos, sem férias, quatrocentos dólares guardados por mês, e todo mês sumiam. Onze anos disso. |
| T4 | One day she said, I've heard every teacher, every prayer, every plan. Why is this different? I couldn't answer. So I sat down and asked Archangel Jophiel. | Um dia ela disse: já ouvi todo professor, toda oração, todo plano. Por que isto seria diferente? Eu não soube responder. Então me sentei e pedi ao Arcanjo Jophiel. |
| T5 | What came back wasn't about her money. It was about her house. Most people look for prosperity outside, never realizing they already live where it was sent. | O que veio de volta não era sobre o dinheiro dela. Era sobre a casa dela. A maioria das pessoas procura prosperidade lá fora, sem perceber que já vive onde ela foi enviada. |
| T6 | Sign one: the plants in your home grow with ease, whether it's one small pot or a whole garden. When life blooms inside a house, opportunity blooms too. | Sinal um: as plantas da sua casa crescem com facilidade, seja um vasinho ou um jardim inteiro. Quando a vida floresce dentro de uma casa, as oportunidades também florescem. |
| T7 | Sign two: your home gets good light during the day. Light brings clarity, joy and movement. A house full of light keeps prosperity's door open. | Sinal dois: a sua casa recebe boa luz durante o dia. A luz traz clareza, alegria e movimento. Uma casa cheia de luz mantém a porta da prosperidade aberta. |
| T8 | Sign three: nature comes close to your home. Birds, butterflies, even bees keep showing up, because they recognize a place where there is harmony. Peace, and blessing. | Sinal três: a natureza se aproxima da sua casa. Pássaros, borboletas, até abelhas aparecem sempre, porque reconhecem um lugar onde existe harmonia. Paz e bênção. |
| T9 | What nobody teaches: three signs prove the blessing is in your house, not that it stays. The problem isn't that it never arrives. It's that nothing holds it. | O que ninguém ensina: três sinais provam que a bênção está na sua casa, não que ela fica. O problema não é que ela nunca chega. É que nada a segura. |
| T10 | It comes in, nothing closes behind it, and it drains out. Like a bathtub with the stopper out: run the faucet eleven years and it never fills. | Ela entra, nada fecha atrás dela, e ela escorre pelo ralo. Como uma banheira com o tampão fora: deixe a torneira aberta onze anos e ela nunca enche. |
| T11 | Jophiel called it the Sunrise Seal. One minute, at first light, inside your home. No new job, no tighter budget, no longer prayers. It closes what was always open. | Jophiel chamou isso de Selo do Amanhecer. Um minuto, na primeira luz, dentro da sua casa. Nada de emprego novo, orçamento mais apertado, orações mais longas. Ele fecha o que sempre esteve aberto. |
| T12 | Loretta did it. She stopped checking her bank app at night. She sleeps till morning now. I only wish I had known it eleven years sooner, for her sake. | A Loretta fez. Parou de olhar o app do banco de noite. Dorme até de manhã agora. Só queria ter sabido onze anos antes, por ela. |
| T13 | If you follow every rule and the money still leaves, comment 222 and tell me how many signs your home has. That ties this seal to your name. | Se você segue todas as regras e o dinheiro ainda vai embora, comente 222 e me diga quantos sinais a sua casa tem. Isso amarra este selo ao seu nome. |
| T14 | Like and save this, so the blessing holds stronger. Loretta's drain stayed open eleven years, and all she earned ran out. Follow me, so you don't lose what's next. | Curta e salve, para a bênção ficar mais forte. O ralo da Loretta ficou aberto onze anos, e tudo que ela ganhou escorreu. Me siga, para não perder o que vem. |
| T15 | Now tap my profile picture and open my stories. The Sunrise Seal is waiting for you there, and getting there takes a few seconds. Blessings, my friend. | Agora toque na minha foto de perfil e abra meus stories. O Selo do Amanhecer está esperando por você lá, e chegar lá leva poucos segundos. Bênçãos, meu amigo. |

## 6. Roteiro final em inglês

1. If your home has one of these three signs, don't sell it. And no, it's not about how big the house is. Don't even think about moving, my friend.
2. I used to tell people to chase prosperity: new job, tighter budget, longer prayers. I did all of it. Then I learned it was never about chasing.
3. My aunt Loretta, sixty-four, played by every rule. Two jobs, no vacations, four hundred dollars set aside each month, and each month it disappeared. Eleven years of that.
4. One day she said, I've heard every teacher, every prayer, every plan. Why is this different? I couldn't answer. So I sat down and asked Archangel Jophiel.
5. What came back wasn't about her money. It was about her house. Most people look for prosperity outside, never realizing they already live where it was sent.
6. Sign one: the plants in your home grow with ease, whether it's one small pot or a whole garden. When life blooms inside a house, opportunity blooms too.
7. Sign two: your home gets good light during the day. Light brings clarity, joy and movement. A house full of light keeps prosperity's door open.
8. Sign three: nature comes close to your home. Birds, butterflies, even bees keep showing up, because they recognize a place where there is harmony. Peace, and blessing.
9. What nobody teaches: three signs prove the blessing is in your house, not that it stays. The problem isn't that it never arrives. It's that nothing holds it.
10. It comes in, nothing closes behind it, and it drains out. Like a bathtub with the stopper out: run the faucet eleven years and it never fills.
11. Jophiel called it the Sunrise Seal. One minute, at first light, inside your home. No new job, no tighter budget, no longer prayers. It closes what was always open.
12. Loretta did it. She stopped checking her bank app at night. She sleeps till morning now. I only wish I had known it eleven years sooner, for her sake.
13. If you follow every rule and the money still leaves, comment 222 and tell me how many signs your home has. That ties this seal to your name.
14. Like and save this, so the blessing holds stronger. Loretta's drain stayed open eleven years, and all she earned ran out. Follow me, so you don't lose what's next.
15. Now tap my profile picture and open my stories. The Sunrise Seal is waiting for you there, and getting there takes a few seconds. Blessings, my friend.

If your home has one of these three signs, don't sell it. And no, it's not about how big the house is. Don't even think about moving, my friend. I used to tell people to chase prosperity: new job, tighter budget, longer prayers. I did all of it. Then I learned it was never about chasing. My aunt Loretta, sixty-four, played by every rule. Two jobs, no vacations, four hundred dollars set aside each month, and each month it disappeared. Eleven years of that. One day she said, I've heard every teacher, every prayer, every plan. Why is this different? I couldn't answer. So I sat down and asked Archangel Jophiel. What came back wasn't about her money. It was about her house. Most people look for prosperity outside, never realizing they already live where it was sent. Sign one: the plants in your home grow with ease, whether it's one small pot or a whole garden. When life blooms inside a house, opportunity blooms too. Sign two: your home gets good light during the day. Light brings clarity, joy and movement. A house full of light keeps prosperity's door open. Sign three: nature comes close to your home. Birds, butterflies, even bees keep showing up, because they recognize a place where there is harmony. Peace, and blessing. What nobody teaches: three signs prove the blessing is in your house, not that it stays. The problem isn't that it never arrives. It's that nothing holds it. It comes in, nothing closes behind it, and it drains out. Like a bathtub with the stopper out: run the faucet eleven years and it never fills. Jophiel called it the Sunrise Seal. One minute, at first light, inside your home. No new job, no tighter budget, no longer prayers. It closes what was always open. Loretta did it. She stopped checking her bank app at night. She sleeps till morning now. I only wish I had known it eleven years sooner, for her sake. If you follow every rule and the money still leaves, comment 222 and tell me how many signs your home has. That ties this seal to your name. Like and save this, so the blessing holds stronger. Loretta's drain stayed open eleven years, and all she earned ran out. Follow me, so you don't lose what's next. Now tap my profile picture and open my stories. The Sunrise Seal is waiting for you there, and getting there takes a few seconds. Blessings, my friend.
