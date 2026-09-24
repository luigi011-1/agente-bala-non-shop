# PRODUCTION STATE
Production: `fitywell_growth_dentes_agua`
Angle: 2, FityWell · Objective: GROWTH · Round: VALIDATION
Reference video: `input/reference_video.mp4`
Current stage: PRODUCTION_COMPLETE
Next action: Luigi gera a mídia no Flow com os `ENTREGA_<AVATAR>.md`; depois da postagem, rodar o P10
(log de rotação, biblioteca, `gerenciar_operacao.py registrar`).

## Decisões do Luigi (2026-09-24)
- Ângulo 2, FityWell, objetivo GROWTH (declarado na mensagem de intake).
- Fila: os 9 avatares anexados. Lia Carlla não veio.
- Roteiro v1 aprovado com o gancho fiel ("roteiro aprovado, prossiga"). Sem resposta sobre o
  precedente `fitywell_dentes`: seguimos com os 9, como proposto para o caso de não ter sido postado.
- Frase de autoridade: "In all my years" em Ivy Carl, Jamie Voss, Lais Collins e Robert Alves.

## Log
- 2026-09-24: intake, `/watch` rodado (5 cenas, cortes em 5,93 · 11,43 · 13,07 · 17,47s),
  9 âncoras conferidas uma a uma, roteiro v1 (7 takes, um por cena, cena 5 dividida em fim de frase)
  e gancho fiel escritos.
- 2026-09-24: achado de P1: o mesmo esqueleto de receita já rodou em `fitywell_dentes` (2026-09-17)
  para Dana, Jamie Anderson e Lynn. Pergunta aberta ao Luigi.
- 2026-09-24: `checar_frases.py` aponta 11 trechos repetidos de `fitywell_dentes` e 1 de
  `fitywell_pernas`, todos na receita e no protocolo (T2, T3, T4). É o conteúdo do vídeo, que
  growth clona literal; a decisão fica com o Luigi junto com a pergunta do precedente.
- 2026-09-24: checklist de envio, bloco A (gancho fiel): 11/11 aprovados (N/A: A1, A2, A7, fiel ao modelo).
- 2026-09-24: `gerar_pacote.py` (adaptado da canela) gerou 9 pacotes, 7 K + 7 V cada. Linter:
  0 FALHAS nos 9 (T6 conferido na versão de cada avatar). Dana Morrison ACTIVE, colado no chat.
- 2026-09-24: `checar_entrega.py` recebeu o suporte a `CENA CURTA` que já existia sem commit no
  worktree da canela (regra de 2026-09-23), e `water bottle` deixou de contar como produto.
- 2026-09-24: Luigi pediu todo o restante de uma vez, separado por avatar. `montar_entrega.py` gerou
  `ENTREGA_<AVATAR>.md` para os 9 (Flow v12 inteiro, checklist, anexos, K, V, CapCut, transcrição,
  roteiro final em inglês por último). Linter 0 FALHAS. Fila com 9 DONE: PRODUCTION COMPLETE.
- 2026-09-24: Luigi: o Flow gerava 1 imagem por K mesmo pedindo 4. Contrato do Flow subiu para v14
  (perfil CLASSICO: 4 imagens por K com seleção manual, vídeo só no Omni Flash, 1 resultado por V).
  `CLAUDE.md` atualizado. Os 9 `ENTREGA_<AVATAR>.md` regenerados com o bloco v14. Linter 0 FALHAS.
- 2026-09-24: Luigi pediu os prompts dos arquivos em blocos separados. `montar_entrega.py` agora põe
  cada K e cada V no próprio bloco copiável (título fora). 9 arquivos refeitos, linter 0 FALHAS.
