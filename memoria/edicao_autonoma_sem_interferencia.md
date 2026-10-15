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

**Lote Sea Moss receitas (2026-10-14, 12 vídeos, Luigi ausente: "resolva tudo e não me peça auxílio"):**
o `auto.py` do lote (`producao/seamoss_receitas_lote_2026_10_13/edicao_scripts/`) resolve sozinho, nesta ordem:
erro de escuta (medium.en no take inteiro + trechos) → exceção; fala inventada/repetida → corta o take no trecho
da fala do roteiro (original em `_originais/`), NUNCA exceção (a invenção ficaria no vídeo); ponta da frase cortada
pelo Flow → fala termina na vírgula/ponto anterior (ou na última palavra ouvida se a vírgula jogar fora >3 palavras,
nunca terminando em palavra solta "one/than/of/with"); palavra inicial faltando (1-2) → fala começa no take.
Nunca perde Natural Rems, Amazon, yes, follow, stories (a bio pode cair). Toda fala ajustada vira OVR em textos.py.
- Take mudo com som ambiente: o whisper "ouve" fala no ruído e o editor casa o take com uma fala. Tirar a trilha
  de áudio do take mudo (`-an`) antes de editar; renomear para `tNN_` também.
- Desktop do Mac é iCloud com disco cheio: takes e editados ficam `dataless` e a leitura falha no meio. `brctl
  download` + leitura completa antes de editar; vídeo entregue pode virar dataless depois (abre normal pelo Finder).
- Conferência de silêncio com ressalva não bloqueia entrega se a fala passou (mesma prática do lote anterior).
- Auditar a lista de OVR no fim: a regra de encurtar já gerou "Dicing." e "with less than one." antes de ser
  corrigida. Olhar `legendas.png` de cada vídeo antes de dizer pronto.

Erros e acertos do lote inteiro (roteiro, pacote, Flow e edição) em [[producao-licoes-lote-1014]].
