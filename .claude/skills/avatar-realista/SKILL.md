---
name: avatar-realista
description: Gera prompts de AVATAR REALISTA para o Higgsfield Soul (Soul 2.0) a partir de um briefing de persona, seguindo o framework de 3 blocos validado pela agência (pessoa → pose/figurino/enquadramento → cenário/luz/mood), com as travas de realismo (sem maquiagem, textura de pele real, sinais naturais de idade, mãos baixas e neutras, cara de iPhone footage). Use SEMPRE que o usuário pedir um prompt de avatar, "gerar avatar", "prompt do Soul", "prompt pro Higgsfield", persona/rosto de UGC, talking-head ou personagem realista pra vídeo, ou disser que vai criar a cara de um cliente/especialista/host, MESMO que não use a palavra "avatar" — se o pedido é a descrição de uma pessoa realista pra gerar imagem no Soul, use esta skill. Sai em INGLÊS por padrão (o Soul responde melhor em inglês); explicações com o usuário em português. NÃO inclui bloco de HEX de cores.
---

# Avatar Realista — gerador de prompts para o Higgsfield Soul

Esta skill transforma um briefing de persona (idade, gênero, papel, cenário, emoção, formato) num **prompt de imagem pronto pra colar no Higgsfield Soul 2.0** que gera um rosto realista, consistente e com cara de gravação de celular. É o framework que já validamos gerando dezenas de avatares (médico, host de podcast, filho comprador etc.).

O prompt final sai em **inglês** por padrão, porque o Soul responde melhor em inglês. As conversas e explicações com o usuário são em português.

## Por que este framework funciona

O Soul tende a entregar rosto "de banco de imagem" (plástico, iluminado demais, sorriso comercial) quando o prompt é vago. O realismo vem de empilhar três coisas: **descrição facial específica**, **travas anti-plástico** (sem maquiagem, textura real, sinais de idade) e **linguagem de captação amadora** (celular, iPhone footage). O framework abaixo garante que os três estejam sempre presentes, na ordem que o Soul lê melhor.

## Estrutura obrigatória — 3 blocos, nesta ordem

Escreva o prompt como **três parágrafos corridos** (sem bullet, sem cabeçalho), na sequência abaixo. Cada bloco resolve um problema diferente.

### Bloco 1 — A PESSOA (identidade + realismo do rosto)
Descreve quem é, com detalhe facial suficiente pra travar a identidade, e já mete as travas anti-plástico. Ordem sugerida:

1. Enquadramento de abertura: `A straight-on medium close-up captures a [idade]-year-old [nacionalidade] [man/woman]`
2. Pele, cabelo, olhos: cor e textura concretas (ex.: `light-tan skin, short dark-brown hair with a touch of grey at the temples, warm dark-brown eyes`)
3. Estrutura do rosto: `build` + testa, mandíbula, nariz, maçãs do rosto, sobrancelhas (dá "osso" ao rosto e ajuda a consistência entre cenas)
4. Óculos/barba se houver
5. **Travas de realismo (não pular):** `realistic skin texture`, sinais naturais de idade (`subtle expression lines`, `crow's feet`, `natural signs of age`), e SEMPRE `no makeup, no cosmetic enhancements`
6. Expressão ligada ao roteiro: a emoção certa (`sincere and warm, mildly concerned`, `serious but caring`, etc.) e o traço que ela transmite (`trustworthy, down-to-earth presence`)
7. Âncora de arquétipo: `He resembles a [arquétipo relatable]` (ex.: `a caring, hard-working middle-class Brazilian father who looks after his elderly parents`) — isso puxa o rosto pra uma pessoa comum e crível, não uma celebridade.

### Bloco 2 — POSE, FIGURINO e OLHAR
Onde está sentado, o que veste, o que as mãos fazem e pra onde olha.

- Cenário/assento: `He is seated on a sofa in his own living room` (ou mesa, poltrona, bancada…)
- Figurino: peça e cor específicas (`a casual navy-blue button-up shirt`)
- **Mãos baixas e neutras (trava anti-bug do Soul):** `Both of his hands are naturally lowered and resting out of frame, with a relaxed, neutral posture. He is not waving, gesturing, pointing, or raising either hand.` O Soul erra mão torta com frequência; mão baixa evita isso, e o gesto real entra depois no vídeo.
- **Direção do olhar (depende do formato):**
  - Talking-head / UGC / especialista sozinho: `He looks directly into the camera, talking straight to the viewer.`
  - Podcast / entrevista (duas pessoas): o personagem olha **para o lado**, pra pessoa fora do quadro, nunca pra lente (`He looks slightly to the side, at the person he is talking to, not at the camera.`) — respeita o eixo de 180°.

### Bloco 3 — CENÁRIO, LUZ, COMPOSIÇÃO e MOOD
Fecha com o ambiente e, principalmente, a **linguagem de celular** que dá o realismo.

- Fundo: elementos do cenário levemente desfocados (`a leafy potted plant, a warm table lamp, a blurred framed picture on the wall`)
- Luz: suave, lateral, natural, iluminando o rosto por igual (`soft warm indoor lighting from the side that gently and evenly lights his face`)
- **Composição + iPhone footage (a trava mais importante do realismo):** `The composition is centered, captured at eye level with a smartphone front camera, giving a sharp, casual, real iPhone-footage look.`
- Mood em 3–4 palavras (`sincere, warm, relatable, and trustworthy`)

## Linha de topo recomendada
Quando o objetivo é bater a estética de gravação real, começar o prompt (ou o pedido de regeneração) com a linha em caixa alta ajuda o Soul a segurar a qualidade:

`IMPORTANT: THIS IS IPHONE FOOTAGE!! KEEP THE SAME LIGHTING AND QUALITY.`

## O que NÃO incluir
- **Nada de bloco de HEX de cores.** Versões antigas terminavam com `HEX VALUES: [...]`; não gere isso. A paleta já é descrita em palavras no Bloco 3, que basta.
- Sem maquiagem, sem "flawless/perfect skin", sem "professional studio lighting", sem sorriso de propaganda — tudo isso mata o realismo.

## Fluxo de trabalho
1. Se faltar informação, pergunte só o essencial: idade, gênero, nacionalidade, papel/arquétipo, cenário, emoção/tom, e formato (talking-head ou podcast). Se o usuário já deu o contexto (ou dá pra inferir do projeto), não trave o trabalho perguntando — gere e ofereça ajustes.
2. Monte os 3 blocos como 3 parágrafos corridos, em inglês.
3. Se o usuário pedir **vários avatares** (pra alimentar o algoritmo), gere variações propositais: mude pele, idade, cabelo, cenário e figurino entre eles, mantendo o mesmo arquétipo e as mesmas travas de realismo. Numere-os.
4. Entregue o prompt pronto pra colar. Explique em português só o que for útil (ex.: "olhar pro lado porque é podcast").

## Exemplo completo (talking-head, filho comprador)

**Briefing:** homem brasileiro ~50, papel = filho que cuida dos pais idosos, cenário = cozinha de casa, tom = sério e sincero, formato = talking-head.

**Prompt (colar no Soul):**

> IMPORTANT: THIS IS IPHONE FOOTAGE!! KEEP THE SAME LIGHTING AND QUALITY.
>
> A straight-on medium close-up captures a 50-year-old Brazilian man with medium tan (moreno) skin, short black hair greying at the sides, and dark-brown eyes. He has a solid, healthy build with a rounded-but-fit face, broad forehead, soft square jawline, straight nose, and thick eyebrows. He wears simple rectangular glasses. His skin has a warm complexion with realistic texture, natural forehead lines and crow's feet, and honest signs of age. His expression is serious but caring, the look of a man about to say something important, giving him a grounded, reliable, trustworthy presence. He is clean-shaven with a hint of stubble, no makeup, no cosmetic enhancements. He resembles an everyday middle-class Brazilian son who worries about his aging parents.
>
> He is seated at the counter of his home kitchen. He is wearing a plain grey polo shirt. Both of his hands are naturally lowered and resting out of frame, with a relaxed, neutral posture. He is not waving, gesturing, pointing, or raising either hand. He looks directly into the camera, speaking earnestly to the viewer.
>
> The background features a clean, simple home kitchen with light wooden cabinets, a kettle and a few jars softly out of focus, and daylight from a window creating diffuse, even lighting on his face. The scene's color palette is dominated by warm wood tones, soft grey, cream, and white. The composition is centered, captured at eye level with a smartphone front camera, giving a sharp, casual, real iPhone-footage look. The overall mood is sincere, honest, warm, and trustworthy.

## Nota sobre o filtro de "pessoa famosa" do Google/Flow
Se o avatar for usado depois pra gerar vídeo (Flow/Omni) e cair no filtro de "pessoa famosa", o problema costuma ser o rosto parecer uma celebridade. Para reduzir isso já na criação: reforce o arquétipo de pessoa **comum e anônima** no Bloco 1 (`an ordinary, anonymous middle-class person, not resembling anyone famous`) e evite traços marcantes de celebridade conhecida.
