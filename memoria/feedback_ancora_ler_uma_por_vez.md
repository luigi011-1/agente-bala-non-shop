---
name: feedback-ancora-ler-uma-por-vez
description: "Ao casar imagem de âncora com nome de arquivo, abrir e nomear UMA imagem por vez, nunca casar pela ordem de uma leitura em lote"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37f5dc01-94f1-4f0f-ac54-6fbe3c922eec
  modified: 2026-09-14T19:26:33.124Z
---

Em 2026-09-14, numa produção Auraly (arquivada em 2026-09-22), li 10 arquivos de `Desktop/AVATARES/avatares appyon/` numa leitura em lote e casei nome com rosto pela ordem em que os resultados vieram. Três nomes saíram trocados entre si (dois homens e uma mulher), e o Luigi gerou imagem com a identidade errada. Os avatares daquela produção foram descartados em 2026-09-22.

**Why:** numa leitura em lote, a ordem das respostas não garante qual arquivo gerou qual imagem, e o erro fica invisível até alguém gerar.

**How to apply:** pra montar fila de avatares, abrir cada arquivo individualmente e escrever o nome junto da descrição logo depois de cada leitura. Antes de entregar o pacote de um avatar, reabrir a âncora daquele caminho exato e conferir com a descrição do prompt. Quando o Luigi disser que o nome está errado, reabrir o arquivo em vez de defender o mapa. Ver [[avatares-fichas]].

**2026-10-04, o nome vem do caminho do arquivo:** as imagens anexadas no chat da nuvem chegam como `1.jpg`, `2.jpg`... sem o nome original. O nome do avatar é o do arquivo do Luigi (ex.: `avery.knox_ .jpeg` = Avery Knox), nunca o nome da âncora do repositório com o mesmo conteúdo. Se o caminho não veio em texto, pedir os caminhos em texto ANTES do roteiro, junto da pergunta de ângulo, e não depois do pacote pronto. Mapa atual em [[avatares-fichas]].
