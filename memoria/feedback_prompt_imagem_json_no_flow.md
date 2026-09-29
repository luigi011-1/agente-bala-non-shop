---
name: feedback-prompt-imagem-json-no-flow
description: "Prompt de IMAGEM entregue ao Luigi (bloco do Flow, chat e ENTREGA_<AVATAR>.md) sai em JSON, nunca em texto corrido. Regras de conteudo identicas. Contrato do Flow v17 (Luigi, 2026-09-25), todos os angulos."
metadata:
  type: feedback
---

Em 2026-09-25, na producao `fitywell_growth_froyo_bites`, o Luigi pediu: *"quero que os prompts que
me mandar de imagem sejam em formato json para obter um resultado melhor e a IA poder compreender
melhor, mantenha exatamente as mesmas regras que ja seguimos para producao de imagens"*.

**Why:** ele acredita que o Nano Banana 2 entende melhor cada parte separada num campo (identidade,
cena, heroi, luz, realismo, negative) do que num paragrafo unico. Revoga o "texto corrido" do bloco
do Flow de 2026-09-09; o JSON ja era a fonte interna, agora e tambem a versao de execucao.

**How to apply:**
- Todo `K__` e `REF-P` entregue (chat, `FLOW_<AVATAR>.md`, `ENTREGA_<AVATAR>.md`, Auraly) = o codigo
  sozinho numa linha e, logo abaixo, UM objeto JSON em ingles, de `{` a `}`.
- Campos, nesta ordem: `format` ("IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."),
  `fiction_note`, `reference_use`, `identity_main`, `wardrobe`, `scene`, `prop`, `posture`,
  `composition`, `camera`, `lighting`, `state`, `realism`, `aspect_ratio`, `negative`. **Sem
  `shot_id`** (metadata; o bloco do Flow continua sem metadata).
- **Nada mais muda:** autossuficiencia, [[realismo-anti-cara-de-ia]] e `GATE_VISUAL.md`, heroi colado
  na lente, trecho de realismo, negative sem termo sensivel, `no captions`, bandeira, um K = um V,
  [[checklist-envio-prompt]]. Prompt de VIDEO continua texto simples nos 5 blocos.
- O executor do Flow cola o objeto inteiro (`producao/_flow/INSTRUCOES_AGENTE_FLOW.md` v17), e o `{`
  inicial virou a marca mecanica de K contra V.
- Gerador de pacote: `texto_flow()` vira `json.dumps` do JSON interno sem `shot_id` e com `format`
  na frente. Gabarito: `producao/fitywell_growth_froyo_bites/gerar_pacote.py`.

Relacionado: [[prompts-imagem-json]], [[feedback-blocos-imagem-video-separados]], [[workflow-entrega-gabarito]]
