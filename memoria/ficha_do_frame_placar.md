---
name: ficha-do-frame-placar
description: "BLOQUEANTE, todos os angulos (Luigi, 2026-09-25): nenhum K sem FICHA_FRAMES.md escrita olhando o frame do modelo e o placar F1-F6 + G1-G8 com o trecho literal do K como evidencia. Modelo manda no conteudo, gate no acabamento e no piso de proximidade. checar_entrega.py reprova sem ela (ficha_frame.py)."
metadata:
  type: feedback
---

Em 2026-09-25 o Luigi gerou o K01 de `fitywell_growth_modelo_intestino` e saiu outro gancho (ver
[[erros-recorrentes]] Falha #8). O prompt passou no linter com 0 falha porque tinha as PALAVRAS da
regra ("very close to the lens") sem a MEDIDA do frame. Ele pediu um jeito de garantir que isso nunca
mais aconteça, em FitWell ou Auraly, e que a conformidade com as regras de fidelidade e com o gate
anti cara de IA seja analisada toda vez que um prompt de imagem sair.

**Why:** regra lembrada falha em sessão longa; adjetivo não é medida; e um placar que eu mesmo marco
sem prova é autodeclaração. A evidência citada que a máquina procura dentro do K fecha essa porta.

**How to apply:**
- Antes do primeiro JSON de qualquer produção nova: `FICHA_FRAMES.md`, uma seção `## Kxx` por K,
  escrita abrindo o frame do modelo daquele take (`input/frames_modelo/Kxx_modelo.png`). Formato e
  itens em `GATE_VISUAL.md` Parte 6.
- Desempate: o frame do modelo manda no CONTEÚDO (forma, quadro, distância, câmera, pose, lista
  fechada, frame 0); o gate manda no ACABAMENTO (luz, céu, foco, pele, texto, bandeira, âncora). A
  proximidade do herói é a MAIS PERTO entre modelo e gate.
- O K se escreve a partir da ficha. Os termos de forma e cada evidência do placar têm que estar
  LITERAIS no K de todos os avatares (sem nome de avatar na evidência).
- `checar_entrega.py` (via `ficha_frame.py`) reprova: ficha ausente, seção faltando, frame
  inexistente, termo ou evidência fora do K, item reprovado ou N/A proibido, composição sem medida de
  quadro, sem distância até a lente, câmera sem lente e altura. Teste em `tests/test_ficha_frame.py`
  com o K01 errado de 2026-09-25, que tem que reprovar.
- Produções antigas estão em `controle/ficha_legado.json`; produção nova nunca entra lá.
- O que a máquina não mede (a ficha descrever o frame certo, a imagem sair igual) é olho: a ficha cita
  o frame, e no K do gancho, quando o Luigi mandar o resultado, pontuar F1 a F6 contra o frame.
- A entrega leva `Ficha: N/N K, placar 14/14 cada` ao lado do checklist ([[checklist-envio-prompt]] B11).

Relacionado: [[realismo-anti-cara-de-ia]], [[checklist-composicao-visual]], [[feedback-prompt-imagem-json-no-flow]]
