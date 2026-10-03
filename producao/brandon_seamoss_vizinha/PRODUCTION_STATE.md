# PRODUCTION STATE
Production: `brandon_seamoss_vizinha`
Angle: 1, Natural Rems Sea Moss · Objective: SALE · Round: VALIDATION
Reference video: `input/reference_video.mp4`
Current stage: PRODUCTION_COMPLETE
Next action: Luigi gera a mídia no Flow com `ENTREGA_BRANDON.md` (REF-P1 a REF-P3 primeiro, aprovar, depois
K01 a K35, seleção manual, V no Omni Flash); quando mandar o K02 gerado (o close de choque do gancho),
pontuar F1 a F6 contra o frame do modelo; depois da postagem, rodar o P10 (log de rotação: rota 6;
biblioteca; resultados.json).

## Decisões do Luigi (2026-10-03)
- Ângulo 1, Natural Rems Sea Moss Gummies, VENDA, avatar holistic.brandon (imagem da âncora na mensagem).
- Link do CTA **na legenda** do post ("mandando para o link da legenda"; reconfirmado: "seguindo o que
  eu disse na mensagem anterior"). Registrado na memória `angulo1-copy-seamoss` e aceito no linter.
- Roteiro v1 aprovado com ajustes ("continue usando argumentos de copy como esse... adiciona um cta de
  comentário e follow sempre também... me manda o roteiro atualizado e prossiga"): mais desvalorização
  do sea moss genérico com diferencial verificado (feito nos EUA, selvagem irlandês, <1 g de açúcar,
  16 em 1, volume de compra, prova social das clientes) e comment `yes` + follow sempre, antes da
  Amazon. As duas regras viraram doutrina em `angulo1-copy-seamoss` (seção 4 e 5.1).

## Log
- 2026-10-03: vídeo enviado por upload na sessão da nuvem; `/watch` rodado (small.en, 20 cenas no
  limiar padrão, cortes finos com limiar 0,06). Origem: avatar IA. Falantes da esquete conferidos por
  tom de voz (o "literally everything" é a vizinha em off sobre o close do marido).
- 2026-10-03: P1: esqueleto novo na biblioteca (movie style família B + listicle de 3 receitas + produto
  Amazon); nunca rodou na conta `brandon`.
- 2026-10-03: roteiro v1 (32 takes; esquete T1 a T15 no tempo do modelo, 10 CENA CURTA e 3 B-ROLL;
  Brandon T16 a T32). Trocas obrigatórias: indicação "holistic coach", credencial de coach no lugar de
  "91 years... without doctors", nº 3 vira sea moss pelo estresse, prova social sem prazo, CTA da marca
  com link na legenda, Facebook e follow gate cortados. `checar_frases.py`: nada repetido da conta.
  Linter: 0 falhas de copy (a única FALHA é o `PROMPTS_PRODUCAO.md`, que só nasce depois da aprovação).
- 2026-10-03: roteiro v2 (35 takes): bloco de venda T31 a T35 (produto com breakdown contra o genérico,
  diferencial 16 em 1 + volume, prova social da coach, comentário + follow, CTA da marca). "Tested and
  approved in the USA" não entrou: não está no rótulo nem verificado na página.
- 2026-10-03: pacote gerado por `gerar_pacote.py` + `montar_entrega.py`: 3 REF-P (vizinha, marido, esposa),
  35 K e 35 V, FICHA_FRAMES.md com 35 frames do modelo e placar completo (evidência conferida por assert),
  ENTREGA_BRANDON.md (Flow v17). Linter normal e --estrito: 0 FALHAS (1 aviso esperado de GERAR DO ZERO).
  Checklist de envio 35/35 (N/A: A1, A10, A12, A13, A14, C4, C7). Fila: holistic.brandon DONE.
  PRODUCTION COMPLETE (entrega de prompts).
- 2026-10-03: Luigi confirmou "roteiro aprovado, prossiga" depois da entrega; prompts colados no chat em lotes (REF-P + K, depois V).
