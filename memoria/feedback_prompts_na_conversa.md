---
name: feedback-prompts-na-conversa
description: "Regra de entrega dos prompts, TODOS OS ÂNGULOS (reforçada pelo Luigi em 2026-10-02 como workflow oficial): no chat, UM bloco de código por prompt, K e V, cada um pronto pra copiar com o código na primeira linha; nunca um bloco único com vários prompts. Antes de cada bloco, fora dele, uma linha curta com a cena e o que anexar. Arquivo E chat, sempre."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f522ec05-bf5e-47fd-b93c-3480612112e4
  modified: 2026-08-19T01:16:24.676Z
---

## 🔴 WORKFLOW OFICIAL, TODOS OS ÂNGULOS (Luigi, 2026-10-02)

*"quero que me mande os prompts sempre em blocos prontos pra copiar, tanto os de imagem como os de video. deixe isso na sua memória como parte do workflow oficial pra qualquer angulo"*

- **No chat, UM bloco de código por prompt**: cada `K__` e cada `V__` no seu próprio bloco, com o código sozinho na primeira linha e o prompt completo logo abaixo, pronto pra copiar de uma vez.
- **Nunca um bloco único com vários prompts** no chat, nem no Ângulo 3 (Auraly). Foi o erro de 2026-10-02 em `brandon_seamoss_coxas`: colei todos os K num bloco só e todos os V em outro, e ele teria que selecionar prompt por prompt na mão. O `FLOW_<AVATAR>.md` com os blocos únicos continua existindo no disco como arquivo de apoio, mas não substitui os blocos individuais no chat.
- A linha curta com a cena e os anexos fica **fora** do bloco, logo acima dele. Dentro do bloco, zero texto auxiliar (GOOGLE FLOW DELIVERY FORMAT continua valendo).
- Vale para imagem (JSON) e vídeo (texto simples dos 5 blocos), em Sea Moss, FitWell, Auraly e Body Hacks.

---

Sempre mandar os prompts **na própria conversa**, em blocos de código prontos pra copiar e colar. Nunca entregar apenas escrevendo num arquivo .md e apontando o caminho.

**Why:** o Luigi trabalha copiando o prompt direto pro Nano Banana / Flow. Ter que abrir um arquivo, achar o bloco e copiar de lá adiciona atrito em cada take. Pedido explícito dele em 2026-08-18.

**How to apply:**
- Escrever o arquivo de produção continua valendo como registro, mas o conteúdo **também** vai colado na resposta.
- Um bloco de código por prompt, na ordem de geração, com um título curto dizendo a ação (GERAR DO ZERO / EDITAR do K_) e quais referências anexar.
- Vale para prompts de imagem (JSON) e de vídeo (texto simples da Fase 7).

## Descrição curta antes de cada prompt (pedido de 2026-08-18)

Todo prompt vem precedido de **uma linha curta, em poucas palavras, dizendo o que aparece na cena**, mais o que anexar. Não é resumo do JSON, é o retrato visual da cena.

Formato:
> **K01 · GERAR DO ZERO** · Brandon segurando a placa colada na câmera, barriga da mulher cortada ao lado
> *Anexar: âncora Brandon + REF-A*

**Why:** ele produz na sequência, take a take, e precisa bater o olho e saber qual cena é aquela e quais imagens anexar sem ter que ler o JSON inteiro. Sem isso ele arrisca anexar a referência errada no prompt certo.

Relacionado: [[ordem-entrega-padrao]], [[prompts-imagem-json]], [[prompts-video-fase7]], [[feedback-roteiro-final]]
