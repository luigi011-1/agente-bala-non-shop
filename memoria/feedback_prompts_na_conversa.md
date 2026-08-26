---
name: feedback-prompts-na-conversa
description: "Regra de entrega dos prompts: SEMPRE colar na própria conversa prontos pra copiar, e SEMPRE preceder cada prompt de uma descrição curta em poucas palavras do que aparece na cena, mais quais imagens anexar."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f522ec05-bf5e-47fd-b93c-3480612112e4
  modified: 2026-08-19T01:16:24.676Z
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
