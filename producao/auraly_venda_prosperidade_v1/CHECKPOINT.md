# PRODUCTION CHECKPOINT

Production: auraly_venda_prosperidade_v1
Angle: 3 (Auraly)
Objective: SALE
Round: VALIDATION
Reference video: producao/auraly_venda_prosperidade_v1/input/modelo.mp4 (upload snapinsta-1791485391460.mp4, 103,4s, 720x1280, 30fps, espanhol; o .mp4 fica fora do git)
Scenario: sala de estar de mansao de luxo com janela em arco alta a esquerda (colinas de pedra clara e ciprestes), estante de livros escura atras a direita, palmeiras e plantas em vasos, borda de um sofa creme com almofada dourada, tapete persa, console de madeira lustrada onde o avatar apoia a mao direita (do video modelo, sem o painel hebraico da parede); Jordan Vale em salao de mansao de maximo luxo

Current stage: PRODUCTION_COMPLETE
Current avatar: NONE
Next action: quando o Luigi confirmar a postagem, registrar com python3 gerenciar_operacao.py registrar (controle/README.md)

## Avatar queue
[DONE] Avery Knox
[DONE] Jordan Vale
[DONE] Devon Price

Anchors (character sheets):
- Avery Knox: producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg
- Jordan Vale: producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg
- Devon Price: producao/_ancoras/character_sheets/devon_price_character_sheet.jpg

## Approved script
status: APPROVED (Luigi, 2026-10-08, "roteiro aprovado")
file: ROTEIRO.md

## Selected hooks
status: APPROVED (hook fiel aprovado junto com o roteiro, 2026-10-08)
hooks: HOOK 1 - FIEL - A casa que ja tem os sinais
formato: fiel-validacao
acao estrutural: avatar de pe numa sala de luxo, plano unico, abre falando a promessa dos tres sinais da casa
eixos de troca: n/a (validacao)

## Current avatar assets
image prompts: PROMPTS_<AVATAR>.md + FLOW_<AVATAR>.md (K01, um por avatar), ficha em FICHA_FRAMES.md
video prompts: PROMPTS_<AVATAR>.md + FLOW_<AVATAR>.md (V01 a V15, todos usam K01); entrega completa em ENTREGA_<AVATAR>.md; bloco do agente Flow em AGENTE_FLOW.md

## Completed
- Intake: video + 3 character sheets (Avery Knox, Jordan Vale, Devon Price); a skill /watch rodou em _watch/ (manifest, transcricao, grades de cenas)
- ANALYSIS: origem avatar IA (rabino gerado), plano unico de 103,4s sem corte, fala em espanhol desde o segundo 0, tres sinais de casa abencoada, sem venda no modelo
- SCRIPT_MODELLING: ROTEIRO.md (15 takes) + GANCHOS_VISUAIS.md; checklist de copy de venda A 14/14, B 5/5, D 8/8; checar_frases sem frase queimada

- Roteiro aprovado pelo Luigi (2026-10-08); FICHA_FRAMES.md (1 K, placar 14/14); pacotes dos tres avatares e AGENTE_FLOW.md; linter --estrito 0 falhas

## Pending
- Geracao no Flow, montagem e postagem (marcos do Luigi)

## User decisions
- Decision: modelar este video para o Auraly app como VENDA de dinheiro e prosperidade, com o checklist de copy de venda
  Reason: Luigi, 2026-10-08: "vamos modelar esses videos para o auraly app com foco em dinheiro e prosperidade (serao videos de venda), ja vamos aplicar o novo checklist de copy de venda"
  Operational consequence: SALE organico (222 + Stories), tres avatares, roteiro passa pelo CHECKLIST_COPY_VENDA.md antes de ir ao Luigi

## Next response format
- Nenhuma: producao entregue
