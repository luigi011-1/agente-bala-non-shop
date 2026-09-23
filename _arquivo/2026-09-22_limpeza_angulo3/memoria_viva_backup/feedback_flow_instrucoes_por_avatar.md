---
name: feedback-flow-instrucoes-por-avatar
description: "O bloco INSTRUÇÕES PARA A MEMÓRIA DO AGENTE — GOOGLE FLOW AI vai colado inteiro no topo do pacote de CADA avatar da fila, não só no primeiro"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37f5dc01-94f1-4f0f-ac54-6fbe3c922eec
  modified: 2026-09-14T17:54:51.683Z
---

Em 2026-09-14, na produção `oliviamadison671` (6 avatares), colei o bloco do Flow só no pacote do primeiro avatar e no segundo e terceiro escrevi "o bloco é o mesmo já colado". Luigi cobrou: "faltou você me enviar as instruções do agente do flow ai".

**Why:** ele usa cada pacote de avatar como unidade independente, e a memória do agente Flow é preenchida do zero. Mesmo motivo da regra de 2026-09-08 que revogou o atalho de "permanece a mesma".

**How to apply:** em produção multi-avatar, todo pacote de avatar começa pelo bloco inteiro de `producao/_flow/INSTRUCOES_AGENTE_FLOW.md`, sem exceção e sem "igual ao anterior". Ver [[workflow-entrega-gabarito]].
