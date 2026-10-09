---
name: edicao
description: Edição dopaminérgica de takes já gravados ou gerados (Veo/Flow): jump cuts tirando pausas, zoom alternado, legenda grande palavra por palavra com destaque, pop-ups de lista, barra de progresso, flash e SFX, música com ducking. Use quando o produtor mandar uma pasta de takes e pedir "edição", "editar", "montar o vídeo", "edição dopaminérgica", "estilo TikTok/Reels", ou quando os takes do Flow estiverem prontos e faltar a pós-produção. O agente edita e renderiza no HyperFrames; o produtor não abre o CapCut.
---

# Edição dopaminérgica

Validado em 2026-10-09 (5 takes de 10s da holistic.brandon, bebida matinal). Motor em `template/`.
Casos em `docs/pos-producao-casos.md`.

## Fluxo
1. `watch` em cada take (`--model small --step 0.5`) e contact sheet de todos: entenda o herói de cada take.
2. Tempo por palavra: `whisper-cli -m <modelo>/ggml-small.en.bin -l en -ml 1 -sow -ojf`
   (PT: `ggml-small.bin -l pt`). Saída em `words/tN.json`.
3. Monte `edit.json` a partir de `template/`:
   - `segmentos` `[take, início, fim]`: corte toda pausa > ~0,35s. **No take-herói visual (o reveal),
     corte pouco**: a transformação é o que segura.
   - `destaques`: palavras da dor, do ingrediente, do resultado e do CTA (viram amarelo).
   - `hook`: frase curta de 3-5 palavras no topo do 1º take.
   - `ingredientes` / `beneficios`: [palavra falada, rótulo] → pop-ups numerados / com check no momento da fala.
   - `impacto`: palavra que ganha tremor de câmera + boom (o fim do reveal).
4. `node edit.mjs` → lint → snapshots → render. Ele gera o `index.html` e o `assets/mix.wav`
   (voz em loudnorm -15, música com sidechain/ducking, SFX).

## Linguagem (o que é "dopaminérgico" aqui)
- Um estímulo novo a cada 1-2s: corte, zoom (1,0 ↔ 1,17, punch de 0,22s), legenda trocando, pop-up, SFX.
- Legenda: Inter 900 caixa-alta, contorno preto grosso (`-webkit-text-stroke` + `paint-order`), 1-3 palavras
  por página, palavra-chave em amarelo e 12% maior **com margem** (sem margem ela encosta nas vizinhas).
- Flash branco + whoosh na troca de take; pop baixinho em cada jump cut; ding nos checks; riser antes
  do resultado; boom + tremor no reveal.
- Barra de progresso amarela no topo (retenção).
- CTA: selo "LINK IN CAPTION ↓" e botão "+ FOLLOW" pulsando no tempo da fala.

## Onde NÃO pôr texto
Nada sobre rosto e nada sobre o herói visual. Selos na altura do peito (top ~1060px); legenda a
~330px do fim. **No take do reveal, suba legenda e gancho para entre o rosto do avatar e o objeto**
(classe `cap up`). Confira por snapshot em cada take antes do render.

## Música
Peça a trilha ao produtor. Lo-fi funciona, mas "dopaminérgico" pede algo mais animado: se ele mandar
outra, troque em `../sfx/` e o ponto de entrada (`-ss` no tempo forte medido).

## v2 — o estilo aprovado como referência (Holistic Brandon) · `template/edit_ritmo.mjs`
A v1 (pop-ups, zoom, SFX, legenda amarela) foi reprovada: "os cortes precisa tirar os silêncios, a
velocidade da fala, a edição também pode melhorar". A referência do produtor é **sóbria e rápida**:
- **Zero silêncio:** corte pelos silêncios reais (`silencedetect=noise=-35dB:d=0.15`, padding 0,03/0,07s).
  O whisper estica cada palavra até a seguinte e esconde as pausas: não use ele para cortar.
- **Fala acelerada ~1,12x** (`atempo` + `setpts`) → ~3,7 palavras/s (referência: 3,5).
- **Legenda serifada branca, minúscula, estática, centro da tela** (Merriweather 900, sombra suave),
  2-3 palavras, quebra no ponto final e na troca de take. Sem animação por palavra, sem cor.
  Transcreva o vídeo JÁ cortado para a legenda e corrija erros de escuta pelo roteiro.
- Cortes secos; **light leak laranja** (screen) só em 1-2 trocas de take; música bem baixa com ducking.
- Overlay em tela cheia começa com `opacity: 0` no CSS (lint `gsap_fullscreen_overlay_starts_visible`).
Antes de editar, peça uma referência do estilo: "dopaminérgico" quer dizer coisas diferentes para cada um.

## Lições da v2 (2026-10-09) — aprovada ("show de bola"), com travadas que ficaram

**Deu certo:** referência do produtor antes de editar; corte pelo silêncio real; 1,12x; legenda
serifada estática no centro; transcrever o vídeo já cortado; corrigir escuta pelo roteiro
("simmer for a cup" → "pour a cup"); legenda quebrando no ponto final e na troca de take.

**Deu errado (não refeito, a pedido):** pequenas **travadas** na imagem. Causas prováveis, corrigir
na próxima:
1. **Segmentos curtos demais** (< 0,4s): viram um piscar. Junte ilhas de fala com menos de 0,4s
   à vizinha em vez de cortar.
2. **Corte no meio da fala** com padding curto (0,07s): sílaba final some e o rosto "pula". Use
   0,10-0,12s no fim e 0,05s no início.
3. **Take de 24fps convertido para 30fps** com `setpts` acelerado: duplica quadros irregularmente.
   Mantenha 24fps no `base` (ou `fps=30` com `-r` depois do `setpts`, mais `minterpolate` só se preciso).
4. **`-ss` antes do `-i`** corta no keyframe mais próximo: troque por `-ss` depois do `-i`
   (preciso, mais lento) ou `trim` no filtro.
5. Confira o resultado com `silencedetect` (sem pausas) **e** com contact sheet a 10fps nos cortes
   para ver pulos antes de entregar.
