---
name: feedback-roteiro-final
description: "Regra de entrega: sempre enviar o roteiro final completo como última coisa do processo de produção, depois de todos os prompts."
metadata: 
  node_type: memory
  type: feedback
  modified: 2026-08-22T02:56:49.407Z
  originSessionId: 81866996-d947-44ef-87cd-b8b24a37d0e4
---

Depois de entregar todos os prompts (imagem + vídeo + mapa de âncoras), SEMPRE fechar com o **roteiro final completo** como último bloco da entrega.

**Why:** O Luigi precisa do roteiro consolidado como documento de referência final para a produção. Os prompts vêm em pedaços separados e o roteiro é o que amarra tudo. Entregar ele por último garante que reflete qualquer correção feita durante o processo de prompts.

**How to apply:** Depois do mapa de âncoras, adicionar um bloco "ROTEIRO FINAL" com as cenas numeradas e a indicação de qual keyframe corresponde a cada take. É a última coisa antes de perguntar se o usuário quer prosseguir para o próximo vídeo.

## O ROTEIRO FINAL EM INGLÊS É OBRIGATÓRIO (pedido do Luigi, 2026-08-21)
Não basta a tabela bilíngue. Depois de todos os prompts, fechar com **o roteiro final em INGLÊS**, em duas formas:
1. **Numerado por take** (`T1`, `T2`...), que é o que amarra com os prompts `V__`
2. **Corrido, só-fala**, pronto pra colar no gerador de voz

**Why:** o inglês é a fonte de verdade que vai pro TTS e pros prompts de vídeo. A tabela bilíngue serve pra ele revisar a copy, mas na hora de produzir ele precisa do inglês limpo, sem coluna de português no meio e sem rótulo de beat atrapalhando. Ele pediu depois de eu entregar o pacote do supermercado só com a tabela bilíngue e sem a versão em inglês corrida.

**Ordem final da entrega, então:** prompts de imagem → prompts de vídeo → mapa de âncoras → montagem → gates → tabela bilíngue → **roteiro final em inglês (numerado + corrido)**.

Relacionado: [[ordem-entrega-padrao]], [[feedback-cta-produto]]
