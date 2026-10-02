---
name: prompts-imagem-json
description: "Estrutura JSON dos prompts de imagem (frame inicial) para Nano Banana — campos, blocos padrão (realismo expandido com zero-blur/hair-strands/reflections, negative com no-blur/no-artificial-lighting, anti-skin-shift pra edições), templates de demo/talking/insert/edição, dicas de ouro (prop, volume, âncora, tamanho do produto ~10cm, zero blur sempre)."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 246ef273-2f24-4b5d-8e5e-51929be93030
  modified: 2026-09-04T00:44:17.143Z
---

# Prompts de Imagem (Frame Inicial) — JSON

> ♻️ **2026-09-25 (Luigi): o JSON agora vai tambem para o Flow**, nao so para o arquivo interno. O bloco
> de imagem entregue deixou de ser texto corrido. Ver [[feedback-prompt-imagem-json-no-flow]].

Cada take começa com uma imagem estática (frame inicial). Nano Banana usa a **foto do avatar como âncora** + prompt em JSON.

## Regra de TÍTULO do prompt (pedido do Luigi, 2026-08-15)
Todo prompt de imagem entregue tem um **título que já diz a AÇÃO DE GERAÇÃO**, pra ele bater o olho e saber o que fazer sem ler o JSON:
- **GERAR DO ZERO** (+ quais referências anexar: foto base do avatar, gerar 2ª pessoa, product.png, etc.), OU
- **EDITAR do T_** (mantém tudo idêntico, muda só X).
Ex.: "T3 · CENA 1 · EDITAR do T1 (muda só o gesto)" · "T6 · GERAR DO ZERO (ref: base Melody + gerar o paciente)". Entregar também um "índice de geração" (lista dos takes com a ação de cada um) junto do pacote de prompts. Ver [[ordem-entrega-padrao]].

### As REFERÊNCIAS vão DENTRO do título, nunca embaixo (pedido do Luigi, 2026-08-21)
Quais imagens anexar é a informação que ele mais precisa bater o olho e ver, então ela vai **no próprio título, em caixa alta**, não numa linha de legenda embaixo.

**Sempre que o take mostrar o PRODUTO, o título tem que deixar explícito que são DUAS referências:**
```
## IMAGEM D · T20 a T22 · GERAR DO ZERO · ÂNCORA MELODY + PRODUCT.PNG
```
E quando for só o avatar:
```
## IMAGEM C · T8 a T19 · GERAR DO ZERO · ÂNCORA MELODY
```

**Why:** antes eu punha "Anexar: âncora Melody + product.png" em itálico pequeno embaixo do título. Ele produz take a take e arrisca anexar referência errada no prompt certo, que é justamente o erro que [[feedback-prompts-na-conversa]] existe pra evitar. Referência escondida em legenda não cumpre essa função.

### 📎 O TÍTULO NÃO BASTA: BLOCO VISUAL DE ANEXO ACIMA DE CADA PROMPT (Luigi, 2026-09-03)
**Esta regra ESTENDE a de 2026-08-21, não a substitui.** O título em caixa alta continua obrigatório.

O Luigi: *"estou começando a me perder se quando vou usar o seu prompt na IA anexo alguma imagem ou não,
deixe isso mais visual."* **Ele está certo e o erro é meu:** eu vinha escrevendo uma linha descritiva de
cena acima de cada prompt ("K02, o prato sobe e domina o primeiro plano"), que descreve a IMAGEM e não a
AÇÃO DE PRODUÇÃO. Quem está gerando take a take não precisa que eu descreva a cena, ela está no JSON
logo abaixo. Precisa saber **o que arrastar para o campo de anexo**.

**Formato obrigatório, em citação, logo abaixo do título e acima do bloco de código:**
```
> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA <AVATAR>** `caminho/da/ancora.jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO
```
```
> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K01 já aprovado**
>
> ### ✏️ EDITAR, muda só <o que muda>
```
```
> ### 📎 ANEXAR: **NADA**
>
> ### 🆕 GERAR DO ZERO
```

**As três regras do bloco:**
1. **Sempre diz o NÚMERO de imagens**, em negrito. É o que ele confere de relance.
2. **Cada imagem numerada com o caminho ou o nome do keyframe de origem.** Nunca "a âncora" solta.
3. **Onde houver risco de cascata, o bloco carrega o aviso:** `🚫 NUNCA anexar o K07 aqui`.

**E o índice de geração passa a ter coluna própria de anexo**, com a regra de bolso escrita embaixo:
GERAR DO ZERO anexa âncora mais REF, EDITAR anexa uma imagem só, o keyframe de origem.

A linha descritiva de cena, se existir, vem **depois** do bloco de anexo, nunca no lugar dele.

## Campos do JSON e função de cada um

| Campo | Função |
|-------|--------|
| `shot_id` | Nome do take (ex.: `S1_hook_initial`) |
| `reference_use` | **CRUCIAL:** diz pra usar a foto SÓ pra rosto/identidade/roupa/cenário, NÃO copiar pose/enquadramento |
| `identity_main` | Descreve o avatar ("EXACT man/woman from the attached reference image" + traços canônicos) |
| `second_person` | Descreve 2ª pessoa se houver |
| `wardrobe` | Roupa e acessórios (puxar da ficha canônica — [[avatares-fichas]]) |
| `scene` | Cenário — "SAME [cenário] as the reference image: [detalhes]" |
| `posture` | Postura (usar pra corrigir foto-âncora, ex.: "standing upright, NOT the seated slouch") |
| `composition` | Disposição no quadro; herói no "lower foreground" quando for demo |
| `camera` | Ângulo/altura ("eye level, straight-on" / "chest level, slightly high toward the bowl") |
| `state` | **ESTADO INICIAL** do take (sempre começo da ação, nunca fim) |
| `lighting` | Luz (bater com cenário do avatar) |
| `realism` | Trava de realismo UGC (bloco padrão abaixo) |
| `aspect_ratio` | Sempre `"9:16 vertical"` |
| `negative` | O que NÃO pode aparecer (bloco padrão abaixo) |

## Blocos padrão (colar sempre)

**Realismo:**
```
"realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details."
```

**Negative base:**
```
"negative": "no text, no captions, no words on screen, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting"
```

**Anti-skin-shift (adicionar nos prompts de EDIÇÃO):**
```
"Do not make their skin darker, yellowish or orangish. Do not make the colors more saturated."
```

Adaptações do negative:
- Se cenário tem copo/vidro que não deve ser "decorativo de beber": `no glass drinking cup`
- Se foto-âncora sentada e você quer em pé: `no seated slouch` + `posture` em pé explícito
- Estágio de transformação: negative do estado errado (`no toned arm in this frame` no estágio gordo, `no big belly in this frame` no estágio magro)

## Template — TAKE DE DEMO (com prop/herói)
```json
{
  "shot_id": "S1_hook_initial",
  "reference_use": "Use the attached image ONLY for [AVATAR]'s face, identity, wardrobe, and the [CENÁRIO] scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT [man/woman] from the attached reference image ([AVATAR]): [TRAÇOS CANÔNICOS].",
  "wardrobe": "[ROUPA + ACESSÓRIOS].",
  "scene": "SAME [garagem/cozinha/box] as [AVATAR]'s reference image: [DETALHES].",
  "posture": "[postura, corrigindo foto se preciso].",
  "composition": "Waist-up. [PROP/HERÓI] sits in the lower foreground. [O que o avatar faz com o prop].",
  "camera": "chest level, slightly high toward the [prop]",
  "state": "Start frame: [o instante inicial da ação].",
  "lighting": "[luz do cenário].",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no text, no captions, no words on screen, no studio, no plastic skin, no extra fingers, no supernatural lighting"
}
```

## Template — TALKING HEAD (sem prop)
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

## Template — INSERT / B-ROLL (close sem rosto)
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

## Template — COMANDO DE EDIÇÃO (gerar estágio a partir de imagem existente)
Uso: quando já tem imagem aprovada e quer mudar SÓ 1-2 elementos (estágios de braço, cor de roupa).

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep [pessoas] exactly the same: same faces, same hair, same tattoos, same body positions, same [prop], same pose. Keep the SAME background exactly: [detalhes], same lighting, same camera angle and framing.",
  "change_1": "[a primeira mudança, ex.: reduzir a gordura embaixo do braço pela metade]. Do not change [o que não muda].",
  "change_2": "[a segunda mudança, ex.: mudar a cor da blusa de branco pra azul].",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing.",
  "negative": "do not change the faces, do not change identities, do not change the background, do not change the [posição travada], do not change the camera angle, no text, no captions, no plastic skin, no extra fingers"
}
```

## Dicas de ouro (todas vieram de erros reais)

1. **Descreva FORMATO, não só o nome do prop.** "Modelo anatômico do aparelho reprodutor feminino" vira coração ou crânio porque a IA defaulta pro mais comum. Escreva: "pink plastic model shaped like a uterus with two curved fallopian tubes branching to the sides and a central canal below" + negative "no heart model, no skull, no brain model".

2. **Volume e cobertura precisam ser explicitados.** Quer MUITO de algo (montanha de cristais na barriga)? Escreva "THICK, TALL, HEAPED MOUND... piled high with 3D volume, so much that almost no bare skin is visible" + negative "no thin scattered layer, no flat sauce-like coating". Senão sai camada fininha.

3. **Enquadramento herói:** herói no "lower foreground", câmera "slightly high toward it" ou "close to it". Puxar câmera pra perto do que importa.

4. **Corrigir foto-âncora:** foto sentado/relaxado e quer em pé? "standing upright, NOT the seated slouch of the reference photo, no legs or lap in frame" + negative "no seated slouch".

5. **Travar 2ª pessoa:** gerar primeiro, aprovar rosto, e nas próximas usar "Use [imagem]'s [pessoa] face as reference so it is clearly the SAME [person]".

6. **Gerar estágios SEMPRE a partir do estágio 1 original**, nunca em cascata (senão a pessoa "deriva" a cada geração).

7. **Tamanho do produto no prompt.** Especificar o tamanho real do frasco (ex.: "The product is about 10 cm in height") pra evitar que o gerador faça tamanho errado. O Korella tem ~10cm.

8. **Zero blur, sempre.** "No blur anywhere, everything in perfectly sharp focus" incluindo fundo, paredes, mobília. Phone camera tem profundidade de campo ampla = tudo nítido. Isso reforça o look UGC e evita cara de IA.

Relacionadas: [[feedback-prompt-completo-sempre]].
