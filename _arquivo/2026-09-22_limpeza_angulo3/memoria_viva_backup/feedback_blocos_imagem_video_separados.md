---
name: feedback-blocos-imagem-video-separados
description: "No chat, entregar os prompts em só DOIS blocos prontos pra copiar: um bloco de prompts de IMAGEM (todos os K seguidos) e um bloco de prompts de VIDEO (todos os V seguidos). Nada de cabecalho por cenario/setup dentro do bloco, nada de tabela ou comentario no meio"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2334fe24-13cf-4026-af72-dfc2d1cf3e3f
  modified: 2026-09-17T03:55:09.304Z
---

Luigi pediu em 2026-09-17, na producao `wealthy_westbrooks_growth`: "sempre me mande tudo aqui no
chat de conversa em blocos prontos pra eu copiar e colar, separando os prompt apenas por prompts de
imagem e video."

**Why:** ele copia o bloco inteiro direto pro Flow. Cabecalho de setup ("## SETUP A — Hook 1..."),
tabela de indice ou comentario entre os codigos quebra o copiar-e-colar em bloco unico.

**How to apply:**
- No chat: **um bloco continuo com todos os K** (K01, K02, ... KNN, cada um so codigo + prompt),
  depois **um bloco continuo com todos os V** (V01...VNN). Nada de titulo de setup, nota de cenario
  ou tabela ENTRE os codigos dentro do bloco.
- Bloco do agente Flow (quando entra, ver [[feedback-flow-instrucoes-por-avatar]]) fica ANTES dos
  dois blocos, nunca misturado neles.
- Transcricao final, checkpoint e comentario de contexto ficam DEPOIS dos dois blocos, nunca antes
  nem no meio.
- Isso NAO muda o que fica salvo em arquivo (`PROMPTS_IMAGEM.md` continua com titulo/indice/anexo
  por K, ver [[prompts-imagem-json]]) — a regra e so sobre o que aparece no CHAT.
