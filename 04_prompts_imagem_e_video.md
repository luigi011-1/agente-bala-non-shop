# 04 — Guia Completo de Prompts (Imagem e Vídeo)

> Lembrete: todos os prompts geram cenas com **avatares de IA — pessoas que não existem**. Quando um prompt tratar de tema sensível, deixe claro para a ferramenta que é um personagem fictício de IA.

Este documento é o mais técnico. Ele ensina, campo a campo, como escrever os dois tipos de prompt: **imagem (frame inicial)** e **vídeo (Fase 7)**. Traz modelos prontos para copiar.

---

# PARTE A — PROMPTS DE IMAGEM (frame inicial)

Cada take começa com uma imagem estática (o "frame inicial"). Geramos essa imagem no Nano Banana usando a foto do avatar como âncora + um prompt em **JSON** (estruturado por campos). O JSON ajuda a ferramenta a separar identidade, cenário, composição, etc.

## Os campos do JSON de imagem (o que cada um faz)

| Campo | Função | Dica |
|-------|--------|------|
| `shot_id` | Nome do take (ex.: `S1_hook_initial`) | Só organização |
| `reference_use` | **Instrução crucial:** diz pra usar a foto do avatar SÓ pra rosto/identidade/roupa/cenário e **NÃO copiar pose/enquadramento** | Sempre inclua. Impede que a pose da foto de referência "vaze" pra cena |
| `identity_main` | Descreve o avatar (o "EXACT man/woman from the attached reference image" + traços) | Repita os traços canônicos do avatar (ver doc 05) |
| `second_person` | Descreve a segunda pessoa, se houver (cliente etc.) | Só quando o beat tem 2ª pessoa |
| `wardrobe` | Roupa e acessórios do avatar | Puxe da ficha canônica (cruz de prata/ouro/sem cruz, tank, henley...) |
| `scene` | O cenário (o mesmo do avatar: garagem, cozinha, box) | "SAME [cenário] as the reference image: [detalhes]" |
| `posture` | Postura do avatar | Use pra corrigir a foto-âncora (ex.: "standing upright, NOT the seated slouch of the reference photo") |
| `composition` | Como os elementos se dispõem no quadro; onde está o prop/herói | Coloque o herói no "lower foreground" quando for demo |
| `camera` | Ângulo/altura da câmera | "eye level, straight-on" / "chest level, slightly high toward the bowl" |
| `state` | **O ESTADO INICIAL** do take (o instante que a imagem representa) | Sempre o começo da ação, nunca o fim |
| `lighting` | Luz | "warm garage light with red neon glow matching the reference image" / "natural kitchen daylight" |
| `realism` | Trava de realismo UGC | Ver bloco padrão abaixo |
| `aspect_ratio` | Sempre `"9:16 vertical"` | Fixo |
| `negative` | O que NÃO pode aparecer | Ver bloco padrão abaixo |

## Blocos padrão (copie sempre)

**Bloco de realismo (cole em todo prompt):**
```
"realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing."
```

**Bloco negative base (adapte por caso):**
```
"negative": "no text, no captions, no words on screen, no studio, no plastic skin, no extra fingers, no supernatural lighting"
```

- Se o cenário tiver copo/vidro que não deve ser "copo de beber decorativo": adicione `no glass drinking cup`.
- Se a foto-âncora é sentada e você quer o avatar em pé: adicione `no seated slouch` e explicite a postura em pé.
- Se é um estágio de transformação: adicione o negative do estado errado (ex.: `no toned arm in this frame` no estágio "gordo", `no big belly in this frame` no estágio "magro").

## Modelo pronto — TAKE DE DEMO (com prop/herói)

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

## Modelo pronto — TAKE TALKING HEAD (sem prop)

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

## Modelo pronto — INSERT / B-ROLL (close sem rosto)

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

## Modelo pronto — COMANDO DE EDIÇÃO (gerar estágio a partir de imagem existente)

Use quando já tem uma imagem aprovada e quer mudar SÓ um ou dois elementos (ex.: estágios do braço, cor de roupa).

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep [pessoas] exactly the same: same faces, same hair, same tattoos, same body positions, same [prop], same pose. Keep the SAME background exactly: [detalhes], same lighting, same camera angle and framing.",
  "change_1": "[a primeira mudança, ex.: reduzir a gordura embaixo do braço pela metade]. Do not change [o que não muda, ex.: the arm position].",
  "change_2": "[a segunda mudança, ex.: mudar a cor da blusa de branco pra azul].",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing.",
  "negative": "do not change the faces, do not change identities, do not change the background, do not change the [posição travada], do not change the camera angle, no text, no captions, no plastic skin, no extra fingers"
}
```

## Dicas de ouro para imagens

1. **Descreva formatos, não só nomes.** "Modelo anatômico do aparelho reprodutor feminino" pode virar um coração ou um crânio, porque o gerador defaulta pro modelo mais comum. Descreva a **forma e a cor**: "pink plastic model shaped like a uterus with two curved fallopian tubes branching to the sides and a central canal below" + no negative "no heart model, no skull, no brain model".
2. **Volume e cobertura precisam ser explicitados.** Se você quer MUITO de algo (ex.: montanha de cristais de açúcar), diga "THICK, TALL, HEAPED MOUND... so much that almost no bare skin is visible" e no negative "no thin scattered layer, no flat sauce-like coating". Senão a IA faz uma camada fininha.
3. **Enquadramento herói:** ponha o herói no "lower foreground" e a câmera "slightly high toward it" ou "close to it". Puxe a câmera pra perto do que importa.
4. **Corrija a foto-âncora:** se a foto do avatar é sentado/relaxado e você quer em pé/próximo, escreva "standing upright, NOT the seated slouch of the reference photo, no legs or lap in frame" + negative "no seated slouch".
5. **Trave a 2ª pessoa:** gere primeiro, aprove o rosto, e nas próximas use "Use [imagem]'s [pessoa] face as reference so it is clearly the SAME [person]".
6. **Gere estágios sempre a partir do estágio 1 original**, nunca em cascata (senão a pessoa "deriva" a cada geração).

---

# PARTE B — PROMPTS DE VÍDEO (Fase 7)

Depois que a imagem está pronta, você a anima no Flow/Veo. O prompt de vídeo é em **texto simples** (não JSON), num formato validado.

## Formato validado (copie a estrutura)

**Take TALKING (avatar fala):**
```
o avatar (homem/mulher) fala em inglês fluente a seguinte frase: "[FALA EXATA DO TAKE, EM INGLÊS]"

o que acontece no vídeo: [ação fiel ao frame, ENXUTA — só o que de fato acontece]

câmera: [movimento simples, ex.: fixa / leve push-in / leve handheld]

som ambiente: [ambiente do cenário], sem música
```

**Take B-ROLL / INSERT (sem fala):**
```
(sem fala no take: a fala [N] do roteiro entra como voz-over na edição)

o que acontece no vídeo: [ação do insert]

câmera: [macro fixa / top-down fixa]

som ambiente: [ambiente], sem música
```

## Regras de ouro para prompts de vídeo (LEIA COM ATENÇÃO)

1. **A FALA SEMPRE VAI INTEIRA NO PROMPT.** Nunca tire, altere ou tire-para-fora a fala pra tentar destravar uma restrição. Se o vídeo de referência foi gerado, a fala já passou uma vez e vai passar de novo. (Ver documento 06 — esta é a regra mais importante e foi aprendida errando.)

2. **Descrição da ação ENXUTA.** Descreva **só o que acontece de fato**, sem exagero de ângulo, posição ou adjetivos dramáticos. Excesso de descrição de local/posição/o-que-a-ação-atinge é o que costuma disparar restrição de conteúdo. Prefira "o homem despeja água de um regador e olha para a câmera enquanto fala" a um parágrafo detalhando ângulo, região do corpo atingida, etc.

3. **"sem música" sempre** no som ambiente — a trilha entra na edição, pra você controlar (e evitar strike de copyright de música).

4. **Marque TALKING vs B-ROLL.** Inserts não levam a linha "o avatar fala"; a locução deles entra na edição.

5. **Câmera simples.** "fixa", "leve push-in", "leve handheld", "top-down fixa". Nada rebuscado.

6. **Bata a ação com o frame inicial.** O que acontece no vídeo deve ser a continuação natural do estado inicial da imagem (ex.: imagem = "colher de canela sobre o abacaxi"; vídeo = "vira a colher e a canela cai").

## Exemplos reais de prompts de vídeo

**Take talking com demo (canela no abacaxi):**
```
o avatar (homem) fala em inglês fluente a seguinte frase: "Put cinnamon on pineapple and just watch what happens."

o que acontece no vídeo: o [avatar] inclina o saleiro de canela sobre a tigela com abacaxi em cubos; a canela cai sobre o abacaxi; ele olha da tigela pra câmera.

câmera: fixa, leve handheld, plano médio levemente de cima

som ambiente: ambiente de garagem, sem música
```

**Take b-roll (insert de reveal nojento):**
```
(sem fala no take: a fala 2 do roteiro entra como voz-over na edição)

o que acontece no vídeo: close extremo do camarão na água quente; finos vermes brancos começam a sair da carne e se contorcem na água fumegante.

câmera: macro fixa, leve tremor

som ambiente: água fervente, sem música
```

**Take CTA (com follow-gate, keyword yes):**
```
o avatar (homem) fala em inglês fluente a seguinte frase: "Comment yes below and I'll send it to you, but make sure you're following me, or it won't let me reach you."

o que acontece no vídeo: o [avatar] aponta pra câmera ao dizer "comment yes", inclina-se levemente, expressão direta no fim.

câmera: fixa, leve push-in

som ambiente: ambiente de garagem, sem música
```

## Como lidar quando um take de vídeo trava por restrição

Ver o documento 06 inteiro. Resumo:
- **Nunca é a fala.** Não mexa nela.
- Enxugue a **descrição da ação** (só o que acontece).
- Se persistir, o gatilho costuma ser a **combinação de elementos** na cena (ex.: regador + pessoa deitada). Separe esses elementos em **takes diferentes** e junte no corte — nunca no mesmo prompt.
- Deixe claro no contexto que é um **personagem de IA fictício** quando o tema for sensível.
