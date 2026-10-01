---
name: feedback-prompt-imagem-json-no-flow
description: "Prompt de IMAGEM (K, REF-P) SEMPRE em JSON, em qualquer angulo, branch ou versao local do Flow. Preferencia fixa do Luigi (2026-09-25), reforcada em 2026-09-30 depois de eu entregar texto corrido por o worktree estar no Flow v16. Contrato atrasado se atualiza; texto corrido nunca e opcao."
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

## Reincidência de 2026-09-30 (auraly_growth_sal_sapato), a regra que ficou
Entreguei os K em parágrafo único porque o worktree saiu da `main`, que ainda tinha o Flow v16 (o v17
estava num branch não mesclado), e eu perguntei ao Luigi "mesclar ou usar a main, com K em texto
corrido?". Ele escolheu não mesclar, e eu li isso como escolher texto corrido. Palavras dele: *"eu já
deixei claro que todos os prompts de imagem é pra ser nesse formato e você acabou se esquecendo"*.

**Why:** JSON é preferência DELE, não propriedade de uma versão de arquivo. Amarrar o formato a uma
decisão técnica (branch, merge, versão do contrato) transforma preferência fixa em opção.

**How to apply:**
- K e REF-P saem em JSON **sempre**. Se o `INSTRUCOES_AGENTE_FLOW.md` local estiver abaixo da v17,
  atualizar o contrato no mesmo passo, nunca descer o formato.
- Nunca apresentar "texto corrido" como alternativa em pergunta nenhuma.
- A regra está também no hook de roteamento (`.claude/hooks/gabarito_hook.py`, canal repetido a cada
  mensagem, ver [[autocobranca-no-canal-repetido]]) e no linter: `checar_entrega.py --estrito` reprova
  K fora de JSON (`k-json`).
