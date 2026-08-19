# 06 — Guia Completo de Prompts de Imagem (frame inicial)

> **Lembrete:** todos os prompts geram cenas com **avatares de IA — pessoas que não existem**. Quando um prompt tratar de tema sensível, deixe claro para a ferramenta que é um personagem fictício de IA.

Cada take começa com uma imagem estática — o **frame inicial**. Geramos essa imagem no Nano Banana usando a **foto do avatar como âncora** + um prompt em **JSON** (estruturado por campos). O JSON ajuda a ferramenta a separar identidade, cenário, composição, etc. Este documento ensina campo a campo e traz modelos prontos.

---

## 1. Os campos do JSON de imagem (o que cada um faz)

| Campo | Função | Dica |
|-------|--------|------|
| `shot_id` | Nome do take (ex.: `S1_hook_initial`) | Só organização |
| `reference_use` | **Instrução crucial:** diz pra usar a foto do avatar SÓ pra rosto/identidade/roupa/cenário e **NÃO copiar pose/enquadramento** | Sempre inclua. Impede que a pose da foto de referência "vaze" pra cena |
| `identity_main` | Descreve o avatar ("EXACT man/woman from the attached reference image" + traços) | Repita os traços canônicos do avatar (documento 08) |
| `second_person` | Descreve a segunda pessoa, se houver (cliente etc.) | Só quando o beat tem 2ª pessoa |
| `wardrobe` | Roupa e acessórios do avatar | Puxe da ficha canônica (cruz de prata/ouro/sem cruz, tank, henley...) |
| `scene` | O cenário (o mesmo do avatar: garagem, cozinha, box) | "SAME [cenário] as the reference image: [detalhes]" |
| `props` / `hero_prop_*` | Os objetos em cena, especialmente o herói | Descreva **forma e geometria**, não só o nome (ver seção 4) |
| `posture` | Postura do avatar | Use pra corrigir a foto-âncora (ex.: "standing upright, NOT the seated slouch") |
| `composition` | Como os elementos se dispõem no quadro; onde está o prop/herói | Coloque o herói no "lower foreground" quando for demo |
| `camera` | Ângulo/altura da câmera | "eye level, straight-on" / "chest level, slightly high toward the bowl" |
| `state` | **O ESTADO INICIAL** do take (o instante que a imagem representa) | Sempre o começo da ação, nunca o fim |
| `lighting` | Luz | "warm garage light with red neon glow" / "natural kitchen daylight" |
| `realism` | Trava de realismo UGC | Ver bloco padrão abaixo |
| `aspect_ratio` | Sempre `"9:16 vertical"` | Fixo |
| `negative` | O que NÃO pode aparecer | Ver bloco padrão abaixo |

---

## 2. Blocos padrão (copie sempre)

**Bloco de realismo (cole em todo prompt):**
```
"realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details."
```

**Bloco negative base (adapte por caso):**
```
"negative": "no text, no captions, no words on screen, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting"
```

**Anti-skin-shift (adicionar em prompts de EDIÇÃO):**
```
"Do not make their skin darker, yellowish or orangish. Do not make the colors more saturated."
```

Adaptações comuns do negative:
- Se o cenário tem copo/vidro que não deve ser "copo de beber decorativo": adicione `no glass drinking cup`.
- Se a foto-âncora é sentada e você quer o avatar em pé: adicione `no seated slouch` e explicite a postura em pé.
- Se é um estágio de transformação: adicione o negative do estado errado (ex.: `no toned arm in this frame` no estágio "gordo", `no big belly in this frame` no estágio "magro").
- Se o prop está saindo com forma errada: liste **todas** as formas erradas que ele já assumiu (ex.: `no starfish, no root, no coral, no tree branch`).

---

## 3. Modelos prontos

### 3.1. Modelo — TAKE DE DEMO (com prop/herói)

```json
{
  "shot_id": "S1_hook_initial",
  "reference_use": "Use the attached image ONLY for [AVATAR]'s face, identity, wardrobe, and the [CENÁRIO] scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT [man/woman] from the attached reference image ([AVATAR]): [TRAÇOS CANÔNICOS].",
  "wardrobe": "[ROUPA + ACESSÓRIOS canônicos].",
  "scene": "SAME [garagem/cozinha/box] as [AVATAR]'s reference image: [DETALHES do cenário].",
  "posture": "[postura, corrigindo a foto se preciso].",
  "composition": "Waist-up. [PROP/HERÓI] sits in the lower foreground. [O que o avatar faz com o prop].",
  "camera": "chest level, slightly high toward the [prop]",
  "state": "Start frame: [o instante inicial da ação].",
  "lighting": "[luz do cenário].",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no text, no captions, no words on screen, no studio, no plastic skin, no extra fingers, no supernatural lighting"
}
```

### 3.2. Modelo — TAKE TALKING HEAD (sem prop)

```json
{
  "shot_id": "S_talkinghead_initial",
  "reference_use": "Use the attached image ONLY for [AVATAR]'s face, identity, wardrobe, and the [CENÁRIO] scene. Do NOT copy its pose.",
  "identity_main": "The EXACT [man/woman] from the reference image ([AVATAR]): [TRAÇOS].",
  "wardrobe": "[ROUPA canônica].",
  "scene": "SAME [cenário] as the reference image: [detalhes].",
  "posture": "Standing/seated upright, close to camera, chin up, [expressão].",
  "composition": "Tight waist-up talking head, subject fills the frame, [gesto de mão].",
  "camera": "eye level, straight-on",
  "state": "Start frame: speaking directly to camera.",
  "lighting": "[luz].",
  "realism": "UGC realism, real skin texture, iPhone look, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no text, no captions, no words on screen, no studio, no plastic skin, no extra fingers, no supernatural lighting"
}
```

### 3.3. Modelo — INSERT / B-ROLL (close sem rosto)

```json
{
  "shot_id": "S_insert",
  "reference_use": "Close-up insert. Use only the [superfície do cenário] and lighting.",
  "identity_main": "No face. Close-up of [o objeto/detalhe].",
  "scene": "SAME [cenário] surface, [luz].",
  "composition": "Extreme close-up of [detalhe]; [o que acontece/está prestes a acontecer].",
  "camera": "macro close-up",
  "state": "Start frame: [estado inicial do detalhe].",
  "lighting": "[luz].",
  "realism": "UGC realism, real texture, slightly gross and visceral, iPhone macro look, no AI polish.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no text, no captions, no words on screen, no face, no studio, no cartoon look"
}
```

### 3.4. Modelo — COMANDO DE EDIÇÃO (gerar estágio a partir de imagem existente)

Use quando já tem uma imagem aprovada e quer mudar SÓ um ou dois elementos (estágios de transformação, cor de roupa, prop trocado). Este é o modelo que faz o **antes/depois disfarçado** funcionar.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep [pessoas] exactly the same: same faces, same hair, same tattoos, same body positions, same [prop], same pose. Keep the SAME background exactly: [detalhes], same lighting, same camera angle and framing. [Se houver pedestal/suporte:] Keep the stand/pedestal in the exact same position and size.",
  "change_1": "[a primeira mudança]. Do not change [o que não muda].",
  "change_2": "[a segunda mudança].",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing.",
  "negative": "do not change the faces, do not change identities, do not change the background, do not change the [posição travada], do not change the camera angle, no text, no captions, no plastic skin, no extra fingers"
}
```

---

## 4. Dicas de ouro (todas vieram de erros reais)

### 4.1. Descreva FORMATO e GEOMETRIA, não só o nome

O gerador defaulta pra forma mais comum que conhece quando você só dá o nome. Exemplos reais de defaults ruins:
- "modelo do aparelho reprodutor feminino" → saiu como **coração** ou **crânio**.
- "estrutura vascular ramificada" → saiu como **estrela-do-mar** (por causa de "spreading outward like limbs" — simetria radial lê como coral/estrela).
- "ramificação" mais genérica → saiu como **raiz de gengibre / madeira de deriva**.

**Solução:** descreva a **forma, a proporção e a cor** com números e referências concretas. Exemplos que funcionaram:
- Em vez de "female reproductive system model": *"pink plastic model shaped like a uterus with two curved fallopian tubes branching to the sides and a central canal below"* + negative "no heart model, no skull, no brain model".
- Para uma estrutura vascular que não pode virar estrela: *"a dense fine branching network... one thick trunk that repeatedly subdivides into progressively thinner twigs, four or five levels deep, ending in a hairlike fringe... wider than it is tall"* + negative "no star shape, no radial symmetry, no five arms, no root, no coral, no tree branch".

**Termo técnico que ajuda:** para objetos anatômicos, usar a **nomenclatura clínica padrão** (como fornecedores de material médico catalogam) ancora a forma sem ambiguidade. Ex.: *"vascular corrosion cast"* é um objeto real e fotografado, e puxa a geometria certa.

### 4.2. Volume e cobertura precisam ser explicitados

Se você quer MUITO de algo (ex.: montanha de cristais de açúcar cobrindo uma barriga), diga:
```
"THICK, TALL, HEAPED MOUND of amber sugar crystals, piled high with 3D volume, so much that almost no bare skin is visible"
```
+ no negative: `"no thin scattered sugar layer, no flat sauce-like coating"`.

Senão a IA faz uma camada fininha tipo molho.

### 4.3. Enquadramento herói — close-up e isolamento (dupla função: retenção + qualidade)

Ponha o herói no `"lower foreground"` e a câmera `"slightly high toward it"` ou `"close to it"`. Puxe a câmera pra perto do que importa.

Esta regra tem **duas razões** que se reforçam:
1. **Retenção (hook bom vs ruim):** hook bom = **quase close-up**, foco total no herói, nada competindo → íntimo, para o scroll. Hook ruim = câmera distante + muita coisa na tela → a atenção se dispersa e o cérebro não sabe onde focar. Regra: no T1, o herói **domina** o enquadramento; tudo o mais fica secundário, desfocado ou fora de quadro.
2. **Qualidade da geração:** **quanto menos elementos, mais realista** a imagem sai. Cena poluída faz o gerador (ChatGPT ou Nano Banana) estragar a qualidade. Isolar o herói é a alavanca nº1 de realismo, além de retenção.

Na prática, no campo `composition` do T1: `"[hero] fills the lower two-thirds, camera pushed in close, everything else softly out of focus or out of frame"`.

> Nuance: **close-up é regra do HOOK e dos takes de reveal**, não do vídeo inteiro. Takes de talking-head e de receita podem abrir um pouco pra mostrar o cenário que dá autoridade (a garagem, os potes de ervas).

### 4.3b. Realismo — parta sempre de algo real

Regras que separam "cara de IA" de UGC crível (ver também documento 03, seção 2.5):
- **Céu branco/claro SEMPRE denuncia IA;** cores quentes (amarelo/laranja/marrom) também. Prefira `overcast sky` / `cloudy` e luz de **golden hour**.
- **Fundo não pode sair borrado** — descreva-o de forma **específica** e, quando puder, gere com uma **imagem de referência real** (casa/rua americana de Pinterest/Pexels). Editar depois não conserta; acerte na 1ª geração.
- **Rostos secundários:** referência de **rosto real do Pinterest**, não texto — evita a cara genérica de IA.
- **Âncora do avatar tem que ser muito realista** — é o ativo que mais pesa. Regenere quantas vezes precisar (realismo é volume de tentativas, não prompt mágico).

### 4.4. Corrija a foto-âncora

Se a foto do avatar é sentado/relaxado e você quer em pé/próximo:
```
"posture": "standing upright, NOT the seated slouch of the reference photo, no legs or lap in frame"
```
+ negative `"no seated slouch"`.

### 4.5. Trave a 2ª pessoa

Gere a segunda pessoa primeiro, aprove o rosto, e nas próximas use a imagem aprovada como referência: *"Use [imagem]'s [pessoa] face as reference so it is clearly the SAME [person]."* Repita os traços da segunda pessoa por extenso em cada take onde ela aparece.

### 4.6. Gere estágios sempre a partir do estágio 1 original

Nunca em cascata (estágio 2 a partir do 1, estágio 3 a partir do 2). Sempre **a partir do 1 original**, senão a pessoa "deriva" a cada geração e some a consistência.

### 4.7. O congelamento total no antes/depois disfarçado

No comando de edição do segundo estágio, trave **tudo** menos o que transforma:
- Rosto, identidade, roupa do avatar
- Fundo, iluminação, ângulo e enquadramento da câmera
- **O pedestal/suporte do objeto** (é ele que diz "é o mesmo objeto")
- A posição das mãos e do corpo

E mude **só** o que é a transformação (o objeto liso→musculoso, a banana murcha→firme, a crosta→limpa). É o congelamento que faz a troca ler como transformação e não como corte.

---

## 5. O mapa de âncoras (entregar junto com os prompts)

Sempre entregue uma tabela dizendo, para cada take, **qual imagem ele usa como referência** e **em que ordem gerar**. Exemplo real (vídeo da Brandon):

| Take | Gerar a partir de | Prop principal |
|---|---|---|
| T1 | Foto base do avatar | Peça encrostada + tanque |
| T2 | Edição do T1 | Peça submersa |
| T3 | Edição do T1 | Peça limpa (reveal) |
| T4 | T1 (só rosto/cenário/bancada) | Ingredientes |
| T5–T8 | T4 | Jarra sendo montada |
| T9, T10 | T3 (mostra o modelo limpo) | Modelo limpo |
| T11, T12 | Foto base (talking head puro) | Nenhum |
| T13 (CTA) | T8 (mostra a jarra pronta) | Jarra pronta |

**Regra:** um take que mostra um prop já preparado deve derivar do take que preparou esse prop, não da foto base — senão o prop muda de forma no meio do vídeo. E takes seguidos devem ter enquadramentos parecidos entre si, para o corte não "pular".

Próximo documento: **07 — Prompts de Vídeo (Fase 7)**.
