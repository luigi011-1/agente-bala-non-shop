---
name: feedback-entrega-avatar-completo-auraly
description: "[ANGULO 3 AURALY] Formato de entrega aprovado pelo Luigi em 2026-09-21: TODOS os cenarios de um avatar numa unica mensagem, pronta pra colar. Bloco do Flow, MAPA K/V uma vez, por cenario so K block + V block, depois CapCut, tabela bilingue e roteiro final em ingles uma vez so."
metadata: 
  node_type: memory
  type: feedback
  created: 2026-09-21T00:00:00.000Z
  modified: 2026-09-21T03:13:35.147Z
  originSessionId: 523a7a65-a698-4bbe-8fdb-bfa482ae268a
---

**Vale so no Angulo 3 (Auraly).** Aprovado pelo Luigi em 2026-09-21,
numa produção Auraly (arquivada em 2026-09-22): *"Gostei da maneira que me mandou dessa ultima vez, me mande sempre assim."*

**Why:** ele quer gerar todos os videos de um avatar de uma vez, sem voltar ao chat entre cenarios.
Entregar cenario por cenario obrigava uma mensagem por video.

**How to apply, em toda entrega de pacote de avatar no Auraly:**

1. **Todos os cenarios do avatar ativo na MESMA mensagem**, nunca um por vez.
2. Os arquivos `CENARIO_<n>_<slug>.md` (um por cenario, numeracao reiniciando em K01/V01, ver
   [[feedback-um-arquivo-por-cenario]]) vao todos juntos num unico `SendUserFile`.
3. Ordem da mensagem:
   - uma linha de status (quantos videos, K, V, falhas do linter) e, se houver, a decisao que
     tomei e ele pode reverter, em no maximo duas frases;
   - **bloco do Flow inteiro**, uma vez;
   - **MAPA K/V uma vez**, quando for igual em todos os cenarios, mais a linha do anexo;
   - para cada cenario: titulo curto com a variavel trocada, **BLOCO DE IMAGEM** e **BLOCO DE
     VIDEO**, nada entre os codigos (ver [[feedback-blocos-imagem-video-separados]]);
   - **Montagem no CapCut uma vez**, valendo para todos;
   - **tabela Take | English | Portugues uma vez**, depois **roteiro final em ingles por take** e
     **corrido**, que fecham a mensagem (a fala e a mesma em todos os cenarios);
   - uma linha final com o estado da fila e pendencias.
4. **Gerar os cenarios por script a partir do `ROTEIRO.md` aprovado**, nunca redigitar fala a mao:
   garante copia literal em todos e o linter confere 70 V de uma vez.
5. Rodar `checar_entrega.py` e so entregar com 0 falhas. Marcar o avatar DONE e o proximo ACTIVE
   no checkpoint na mesma rodada.
