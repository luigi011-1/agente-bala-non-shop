---
name: feedback-um-arquivo-por-cenario
description: "Pacote multi-cenário sai em UM ARQUIVO POR CENÁRIO, cada um com K01-K09 e V01-V09 reiniciando a numeração"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a57eabc7-682d-471a-8296-79e1d8b2ea95
  modified: 2026-09-18T19:46:15.569Z
---

Quando um avatar tem vários vídeos (um cenário por vídeo, mesma copy), entregar um arquivo por cenário (`CENARIO_<n>_<slug>.md`), cada um com todos os K e depois todos os V daquele cenário, numeração reiniciando em K01/V01, sem cabeçalho dentro. Mesmo contrato do agente Flow.

**Why:** Luigi, 2026-09-18 (produção Auraly arquivada): quer usar cada cenário isolado no Flow, com as mesmas instruções. Um bloco único K01-K45 não serve pra ele.
**How to apply:** em toda produção multi-cenário, para todos os avatares da fila. Enviar os arquivos via SendUserFile. Ver [[feedback-blocos-imagem-video-separados]].

**🔴 TODA entrega de pacote (inclusive redistribuição em arquivos, correção ou reenvio) FECHA com a transcrição colada no chat:** tabela Take | English | Português + roteiro final em inglês por take + versão corrida. Nunca "a copy não mudou, é a mesma de antes". Esqueci duas vezes em 2026-09-18 e o Luigi explodiu.
