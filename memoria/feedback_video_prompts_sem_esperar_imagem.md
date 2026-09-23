---
name: feedback-video-prompts-sem-esperar-imagem
description: "No Angulo 3 (Auraly), mandar os prompts de video (V__) na mesma mensagem que os prompts de imagem (K__) do avatar ativo, sem esperar selecao/aprovacao de imagem (WAITING_IMAGE_SELECTION deixou de pausar)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2334fe24-13cf-4026-af72-dfc2d1cf3e3f
  modified: 2026-09-17T03:44:56.776Z
---

Luigi pediu em 2026-09-17, numa producao Auraly (arquivada em 2026-09-22): "manda os prompts de video logo
após mandar os prompts de imagem sempre, não precisa pedir aprovação."

**Why:** ele não quer parar o fluxo pra aguardar seleção de imagem antes de ver os prompts de vídeo
do mesmo avatar. Quer os dois pacotes (K e V) entregues juntos, de uma vez, por avatar.

**How to apply:** no pipeline do [[pipeline-auraly-separacao]] / `WORKFLOW_AURALY.md`, o estado
`WAITING_IMAGE_SELECTION` não pausa mais a resposta — depois de entregar os `K__` do avatar ativo,
seguir imediatamente pros `V__` do mesmo avatar na mesma mensagem, sem perguntar "aprova as imagens?".
As outras esperas do fluxo (`WAITING_SCRIPT_APPROVAL`, `WAITING_HOOK_SELECTION`) continuam normais,
essa é a única revogada. Já refletido no próprio `WORKFLOW_AURALY.md`, seção "Regra de estado".
