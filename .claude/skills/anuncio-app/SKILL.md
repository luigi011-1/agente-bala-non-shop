---
name: anuncio-app
description: Anúncio animado de app (motion de app) no Flow, sem avatar — telas reais do app dentro de um celular animado, títulos curtos, fechamento com marca e CTA. Use quando o produtor pedir vídeo animado do FityWell ou de outro app, "motion do app", anúncio pago mostrando o app, ou mandar gravações de tela do app para virar vídeo.
---

# Anúncio animado de app

Formato validado em 2026-10-08 com o FitWell (Ângulo 2). Regras técnicas de quadro inicial/final e
tela de celular: `docs/pos-producao-flow-frames.md`. Casos: `docs/pos-producao-casos.md`.
**Copy, claim e CTA seguem a doutrina do ângulo** (`PLAYBOOK_FITYWELL.md`, memórias do ângulo): esta
skill cuida só da forma do vídeo.

## 1. Entender o app pelas gravações

Rode a `watch` nas gravações de tela (`--no-audio --step 0.5`). Saia com:
- o **momento mágico** (no FityWell: foto do prato → alimentos com gramas e kcal);
- 3 ou 4 telas fortes, cada uma virando um beat;
- o slogan e o tom do próprio app (FityWell: "Simple meals, clear numbers, no guesswork");
- **bugs visíveis na gravação** — avise o produtor antes de usar a tela (ex.: "20.400000000000002g").

Extraia as telas como PNG para o produtor anexar e deixe numa pasta fácil de achar
(`~/Downloads/<app>_telas/`). Ele não sabe onde ficam os arquivos do projeto: diga o caminho
e abra a pasta (`open`).

## 2. Estrutura (~14s, 9:16, inglês)

| Take | Função | Quadros |
|---|---|---|
| V1 | Hook: o momento mágico acontecendo (scan no prato, etiquetas de kcal) | A → B |
| V2 | O resultado entra no app (etiquetas voam, celular levanta, tela real) | B → C |
| V3 | Segunda função do app ganhando vida (figura anatômica sai da tela e faz o exercício) | D |
| V4 | Fechamento: logo, slogan, botão do CTA, celular subindo | E → E |

Um título curto por beat, dentro da imagem: "Snap your plate." · "Get clear numbers." ·
"Workouts that fit your week." Paleta tirada da tela (FityWell: off-white #F6F4F0, verde
escuro #0C413E, verde-menta nos botões).

## 3. Regras

1. **Toda tela real está num quadro** (início ou fim). Tela pedida "por referência" é inventada.
2. **Texto dentro do keyframe** (Nano Banana Pro escreve certo). Imagem B = edição da A.
3. **Fechamento com a mesma imagem no início e no fim**, para o texto não deformar.
4. Movimento descrito passo a passo, nunca só o nome do exercício.
5. Rótulos que o app errou na gravação não entram no anúncio (o app chamou batata-doce de
   "Eggplant"; o anúncio diz "Sweet potato").
6. Anúncio pago **mostra a marca**. Orgânico de curiosidade esconde.
7. Sem locução por padrão; SFX no Veo, música na montagem.
8. Gere 2 de cada, baixe em 1080p.

## 4. QA e montagem

Rode a `watch` no resultado e procure: etiquetas duplicadas quando voam, tela branca nas
transições, figura parada, grafia nos últimos quadros. Montagem-alvo: V1 ~3,5s, V2 ~3s,
V3 ~4,5s, V4 ~3s. Trecho com texto embaralhando em movimento: acelere 2x. Tela vazia: corte.
O agente pode montar com ffmpeg (ou HyperFrames, instalado como plugin) se o produtor não
quiser abrir o CapCut.

## 5. O que não fazer

- **Omni em plano único** quando as telas precisam ser fiéis: só a imagem inicial é respeitada.
- Prompt de vídeo que pede tela rolando com texto legível.

## 6. Quando NÃO é esta skill

Referência com texto palavra por palavra + locução (manifesto de marca, institucional)
vai para a skill **`manifesto`** (HyperFrames). Esta skill é para vídeo gerado no Flow com telas reais.
