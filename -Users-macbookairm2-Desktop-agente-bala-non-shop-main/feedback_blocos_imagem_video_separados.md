---
name: feedback-blocos-imagem-video-separados
description: "ARQUIVO de entrega por avatar (2026-09-24): UM bloco copiável por K e por V, título fora do bloco. No chat, entregar os prompts em só DOIS blocos prontos pra copiar: um bloco de prompts de IMAGEM (todos os K seguidos) e um bloco de prompts de VIDEO (todos os V seguidos). Nada de cabecalho por cenario/setup dentro do bloco, nada de tabela ou comentario no meio"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2334fe24-13cf-4026-af72-dfc2d1cf3e3f
  modified: 2026-09-24T00:00:00.000Z
---

Luigi pediu em 2026-09-17, numa producao Auraly (arquivada em 2026-09-22): "sempre me mande tudo aqui no
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
- Isso NAO muda o que fica salvo como fonte interna (`PROMPTS_IMAGEM.md` / `PROMPTS_<AVATAR>.md`
  continuam com titulo/indice/anexo por K, ver [[prompts-imagem-json]]).

## Arquivo de entrega por avatar (Luigi, 2026-09-24)

Pedido dele em `fitywell_growth_dentes_agua`, quando pediu todos os avatares de uma vez em arquivos:
*"nos arquivos que me manda da producao dos avatares quero que me mande os prompts em blocos de texto
separados prontos pra copiar, no mesmo formato K e V que voce ja envia"*.

**Why:** no arquivo ele copia prompt a prompt, e o bloco unico com os 7 K obrigava a selecionar texto
na mao.

**How to apply:** no `ENTREGA_<AVATAR>.md`, cada K e cada V vai no PROPRIO bloco ```text, com o
codigo sozinho na primeira linha e o prompt completo embaixo (mesmo formato de sempre). Titulo curto
(take, cena, o que anexar) fica FORA do bloco, numa linha `###` acima dele. Todos os K primeiro,
depois todos os V. Gabarito: `producao/fitywell_growth_dentes_agua/montar_entrega.py`.

## Formato do K dentro do bloco (Luigi, 2026-09-25)
O codigo continua sozinho na linha; o prompt embaixo agora e um objeto JSON, nao texto corrido.
Ver [[feedback-prompt-imagem-json-no-flow]].
