# PRODUCTION STATE
Production: `fitywell_growth_froyo_bites`
Angle: 2, FityWell · Objective: GROWTH · Origin: ORGANIC · Round: VALIDATION
Reference video: `input/reference_video.mp4`
Current stage: PRODUCTION_COMPLETE
Next action: Luigi gera a mídia no Flow com os `ENTREGA_<AVATAR>.md`; depois da postagem, rodar o P10
(log de rotação, biblioteca, `gerenciar_operacao.py registrar --origem REAL`).

## Decisões do Luigi (2026-09-25)
- Ângulo 2, FityWell (respondido no intake). Objetivo GROWTH e origem orgânica (declarados na mensagem).
- Fila: os 6 avatares anexados, na ordem recebida.
- Roteiro aprovado: "aprovado A" (frase da cirurgia literal, primeira pessoa).
- CTA: pedir para seguir e não perder as próximas receitas saudáveis. T12 virou "Save this one, and
  follow me so you don't miss my next healthy recipes. Why is it so good?" (19 palavras, ~6s).

## Log
- 2026-09-25: intake, 6 âncoras conferidas uma a uma contra `producao/_ancoras/`, ângulo perguntado.
- 2026-09-25: `/watch` rodado (13,8s, 36 cortes, 6 segmentos de fala, tudo voz-over). Receita:
  framboesa, mirtilo, chia, xarope, iogurte grego; bandeja, congelar, banho de iogurte, corte.
- 2026-09-25: roteiro v1 com 12 takes, um por passo da receita (jump cuts do mesmo passo saem do
  mesmo clipe). Voz em T1, T8 e T12. `checar_frases.py`: nada repetido da conta fitywell.
- 2026-09-25: roteiro aprovado (A) com o follow no CTA. `gerar_pacote.py` e `montar_entrega.py`
  (adaptados de `fitywell_growth_dentes_agua`) geraram 6 pacotes, 12 K + 12 V cada, com o frame do
  modelo de cada passo em `input/frames_modelo/` como referência de composição. Linter 0 FALHAS nos 6.
  Eva Dall ACTIVE, colada no chat.
- 2026-09-25: Luigi pediu o pacote do restante dos avatares. Os 5 `ENTREGA_<AVATAR>.md` (Ivy Carl, Jamie Voss,
  Lais Collins, Robert Alves, Roberta Carvalho) enviados como arquivo. Fila com 6 DONE: PRODUCTION COMPLETE.
- 2026-09-25: Luigi pediu os prompts de imagem em JSON, com as mesmas regras. Contrato do Flow subiu para
  v17 (K = objeto JSON, sem shot_id, `format` na frente). CLAUDE.md, WORKFLOW_AURALY.md, PLAYBOOK_FITYWELL.md,
  GATE_VISUAL.md, guia do Flow e memoria atualizados. Os 6 ENTREGA/FLOW regenerados, linter 0 FALHAS, reenviados.
