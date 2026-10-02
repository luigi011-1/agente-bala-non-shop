# PRODUCTION STATE
Production: `brandon_pao_sementes`
Angle: 2, FityWell · Objective: GROWTH · Round: VALIDATION
Reference video: `input/reference_video.mp4`
Current stage: PRODUCTION_COMPLETE
Next action: Luigi gera a mídia no Flow com `ENTREGA_BRANDON.md`; quando mandar o K01 gerado, pontuar
F1 a F6 contra o frame do modelo; depois da postagem, rodar o P10 (log de rotação, biblioteca,
`gerenciar_operacao.py registrar`).

## Decisões do Luigi (2026-09-29)
- Ângulo 2, FityWell, avatar holistic.brandon (âncora aprovada no mesmo dia).
- Roteiro v1 aprovado com o gancho fiel; objetivo confirmado: GROWTH ("roteiro aprovado, é growth, pode prosseguir").

## Log
- 2026-09-29: `/watch` rodado (6 cenas, cortes em 4,63 · 12,33 · 13,63 · 16,63 · 20,27s). Origem:
  avatar IA. CTA do modelo: comment yes + follow para receber a receita, sem produto: classificado
  como GROWTH pelos precedentes `fitywell_cheesecake` e `fitywell_dentes`, pendente de confirmação.
- 2026-09-29: P1: esqueleto inédito na biblioteca e nas produções.
- 2026-09-29: roteiro v1 (6 takes, um por cena, T3 a T5 CENA CURTA) e gancho fiel escritos.
  `checar_frases.py`: nada repetido dos 4 roteiros antigos da conta `brandon`.
- 2026-09-29: checklist de envio, bloco A (gancho fiel): 11/11 aprovados (N/A: A1, A2, A7, fiel ao modelo). Linter: só a FALHA esperada de PROMPTS_PRODUCAO.md, que nasce depois da aprovação.
- 2026-09-29: roteiro aprovado, growth confirmado. FICHA_FRAMES.md (6 K, placar 14/14), gerar_pacote.py
  (JSON, contrato do Flow v17 lido do branch claude/ola-d0d6f0) e montar_entrega.py geraram
  PROMPTS_BRANDON.md, FLOW_BRANDON.md, PROMPTS_PRODUCAO.md e ENTREGA_BRANDON.md.
- 2026-09-29: linter do branch claude/ola-d0d6f0 (com ficha_frame.py): 0 FALHAS, 1 aviso informativo
  (todo K é GERAR DO ZERO, por ser autossuficiente). Linter local: 0 FALHAS; o aviso de realismo dele
  é falso positivo, porque ainda não conhece a FICHA_FRAMES.md.
- 2026-09-29: checklist de envio 34/34 (N/A: A1, A2, A7, C3 a C7). Fila: holistic.brandon DONE.
  PRODUCTION COMPLETE (entrega de prompts).
