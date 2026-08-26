---
name: stack-ferramentas
description: "Ferramentas usadas na produção — Nano Banana 2 e Pro (imagem), Veo 3.1 via Flow (vídeo), ffmpeg + ImageMagick (decomposição), limitações do Agent do Flow, identificação de música, color grading de referência no CapCut (temp -3 / tint +2 / sat -6 / exp -3 / contrast +12 / highlight -35 / shadow +18 / fade +6)."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 246ef273-2f24-4b5d-8e5e-51929be93030
  modified: 2026-08-15T14:56:26.637Z
---

# Stack de Produção

## Geração de imagem (frame inicial de cada take)
- **Nano Banana 2** — modelo padrão para volume. Recebe foto do avatar como âncora de identidade + prompt descrevendo a cena.
- **Nano Banana Pro** — versão superior, para **frames-herói** (hook, momento chave) onde qualidade precisa ser máxima. Fluxo: volume no 2, herói no Pro.
- Ambos aceitam **comandos de edição** — pega imagem gerada e pede "mude só X, mantenha o resto idêntico". Essencial para estágios de transformação (braço encolhendo etc.).

## Geração de vídeo (animar imagem → clipe falado)
- **Veo 3.1 via Flow** — image-to-video. Imagem (frame inicial) + prompt (ação + fala) → clipe de ~8s.
- **Veo 3.1 Lite / Lower Priority** — roda **sem consumir créditos** (fila mais lenta, 720p). Ideal para volume/testes.
- **"Agent" do Flow** (movido a Gemini) — feito pra **geração**, não análise. Usa "Agent Instructions" como ficha de personagem persistente + marcar assets com @ pra manter consistência. **NÃO serve para assistir/analisar vídeos.**
- Alternativas de vídeo citadas pelo mentor: **OmniHuman**, **SeaDance** (às vezes mais realista que OmniHuman), **Kling**. Regra: dar **instruções detalhadas do movimento** que o avatar faz (o que faz ou "deriva" pra genérico).

## REALISMO — como não sair com "cara de IA" (aula do mentor, ataca o gargalo de qualidade)
Aplicar SEMPRE ao escrever prompt de imagem e ao gerar vídeo:
- **Close-up + POUCOS elementos = mais qualidade E mais realismo.** Cena poluída faz o gerador (ChatGPT ou Nano Banana) estragar a qualidade. **Isolar é a alavanca nº1** — mesma lição do hook, pela ótica técnica. Menos elementos → o image-gen e o video-gen seguram a qualidade.
- **Nano Banana 2 > ChatGPT** em realismo de avatar hoje; **regenerar várias vezes** até a imagem perfeita (não é questão de prompt mágico, é volume de tentativas).
- **Ativo mais importante: imagem de referência do avatar MUITO realista.** Nada compensa uma âncora ruim.
- Pessoas secundárias na cena (2ª pessoa, movie style): **referência de rosto REAL do Pinterest** → evita cara genérica de IA. Referências devem ser orgânicas (tiradas direto do TikTok, iluminação boa).
- **Cores quentes (amarelo/marrom/laranja) deixam mais "cara de IA"; céu branco/claro SEMPRE denuncia IA.** Preferir céu nublado; cenas em **golden hour** (fim de tarde) melhoram realismo.
- **Fundo borrado não se conserta editando** — acertar na 1ª geração: descrição de fundo muito específica + **imagem de referência real** (casa/rua/bairro de Pinterest/Pexels/Google). Ou screenshot de fundo real com a pessoa falando na frente.
- Realismo avançado ("método Frankie"): gerar elementos SEPARADOS (céu, árvores, casas, rosto) e mesclar num frame só mantendo a qualidade de cada.
- Reforça a regra de composição do hook em [[metodo-puzzle]] (close-up, foco no herói) — aqui pelo lado da qualidade da geração, lá pelo lado da retenção.

## Decomposição de vídeo de referência
- Quem analisa **vê frames, NÃO ouve áudio**. Extrai quadros do `.mp4` e olha imagens.
- **Consequência:** áudio/música do original não são identificáveis pela IA (ver a seção de identificação de música abaixo).
- Ferramentas: `ffmpeg` (extrair frames) + `montage` do ImageMagick (contact sheets). Ver [[processo-7-fases]] Fase 2 para comandos.

## Edição final
- Referência de estilo de legenda: **Captions.ai Prism Pro**.
- Montagem final (juntar takes, legenda, locução, trilha) em editor de vídeo padrão.
- Export 9:16.

## Color Grading de referência no CapCut (valores do doc de prompt templates)
Aplicar no vídeo final pra remover o "look IA" e dar realismo UGC/iPhone. Ajustar se ficar escuro/cinza demais:
- **temp -3** (esfria, remove o amarelado típico de IA)
- **tint +2**
- **saturation -6** (dessatura o hiper-real)
- **exposure -3** (escurece levemente)
- **contrast +12** (contraste natural)
- **highlight -35** (puxa highlights pra baixo, remove brilho excessivo)
- **shadow +18** (levanta sombras, mostra detalhes)
- **fade +6** (leve fade = look iPhone/UGC)

Lógica: temp negativo + saturation negativa = remove warmth e oversaturation (os dois maiores denunciadores de IA). Highlight -35 é o ajuste mais agressivo: IA tende a gerar highlights estourados. Shadow +18 compensa a perda de detalhe nas sombras. Fade dá o look orgânico de câmera de celular.

## Identificação de música do original
Como quem decompõe não ouve áudio, e o Facebook bloqueia acesso automatizado a Reels (ROBOTS_DISALLOWED), você mesmo descobre:
- **SongFromLink** ou similares (Facebook Reel song finder por URL) — extrai áudio e identifica por forma de onda; funciona em Reel público mesmo sem tag no FB.
- **Shazam** ou busca de música do Google, com o vídeo tocando ao lado.
- Trilha "sem copyright" de biblioteca → Shazam pode não achar; tentar extensão tipo AHA Music.
- FB raramente exibe a tag (diferente de TikTok/IG).

Sempre "sem música" nos prompts de vídeo — trilha só na edição, para controle + evitar strike.
