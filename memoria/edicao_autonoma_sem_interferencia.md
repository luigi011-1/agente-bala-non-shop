---
name: edicao-autonoma-sem-interferencia
description: "Edição automática roda do take ao vídeo entregue no Desktop SEM depender do Luigi (2026-10-13): um orquestrador único em segundo plano (nohup), fila sequencial, exceções de escuta automáticas, entrega e STATUS sozinhos; nunca reescrever roteiro a partir de transcrição"
metadata:
  type: feedback
---

Luigi, 2026-10-13: *"não quero que você fique parado caso eu não fique te observando, quero que você seja capaz de
realizar todo o processo de edição automática sem nenhuma interferência minha"*.

**Why:** no lote Sea Moss notícia (5 vídeos) a fila travou várias vezes esperando eu agir: scripts de fila
espalhados, Monitor que expira em 30 min e MATA o comando que ele executa, cópia para o Desktop manual, e eu
reescrevendo roteiro a partir de transcrição (o whisper corta a ponta do take: "inflammation from the", "one thing
I keep"), o que fez o editor cortar fala real e custou ~20 min de reedição cada.

**How to apply:**
- Um orquestrador só, lançado com `nohup` (nunca como comando do Monitor): fila sequencial (disco do Mac), para cada
  pasta roda o editor, trata a falha de fala sozinho e entrega `~/Desktop/<pasta>/<vNN_tema_avatar>_editado.mp4`
  (recomprimido crf 20) + linha em `STATUS_EDICAO.md` da produção. O Monitor só faz `tail -f` do log.
- Erro de escuta (palavra que o whisper pequeno ouve errado ou não ouve): exceção no `--excecoes-fala` com
  `user_authorization`, presa ao arquivo e ao sha256. NUNCA trocar o roteiro pelo que o whisper ouviu sem conferir
  o trecho; fala que a avatar realmente não disse só sai do roteiro depois de ouvir o take em trechos.
- Repetição dentro do take NÃO vai para exceção (exceção mantém o áudio inteiro e a repetição fica): cortar o take
  (original em `_originais/`) e reeditar.
- Avisar o Luigi a cada vídeo pronto, sem pedir nada; só parar para perguntar se a decisão for dele (take para
  regerar no Flow quando ele não autorizou "do jeito que tá").
Relacionado: [[edicao-licoes-teste]], [[edicao-prioridade-hyperframes]].
