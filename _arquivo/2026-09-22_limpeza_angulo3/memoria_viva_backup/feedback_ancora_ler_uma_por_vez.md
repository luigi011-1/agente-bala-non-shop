---
name: feedback-ancora-ler-uma-por-vez
description: "Ao casar imagem de âncora com nome de arquivo, abrir e nomear UMA imagem por vez, nunca casar pela ordem de uma leitura em lote"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37f5dc01-94f1-4f0f-ac54-6fbe3c922eec
  modified: 2026-09-14T19:26:33.124Z
---

Em 2026-09-14, na produção `oliviamadison671`, li 10 arquivos de `Desktop/AVATARES/avatares appyon/` numa leitura em lote e casei nome com rosto pela ordem em que os resultados vieram. Três nomes saíram trocados: o homem da selfie na cabana é `Jackiee Ray .png` (eu chamei de Coreyy Shaw), o do sótão é `autus plato .png` (eu chamei de Avery Holt) e o de camiseta vinho é `Avery Holt .png`. `Coreyy Shaw .png` é uma mulher de turbante. Luigi gerou imagens com o pacote de nome errado e reclamou com razão.

**Why:** numa leitura em lote, a ordem das respostas não garante qual arquivo gerou qual imagem, e o erro fica invisível até alguém gerar.

**How to apply:** pra montar fila de avatares, abrir cada arquivo individualmente e escrever o nome junto da descrição logo depois de cada leitura. Antes de entregar o pacote de um avatar, reabrir a âncora daquele caminho exato e conferir com a descrição do prompt. Quando o Luigi disser que o nome está errado, reabrir o arquivo em vez de defender o mapa. Ver [[avatares-fichas]].
