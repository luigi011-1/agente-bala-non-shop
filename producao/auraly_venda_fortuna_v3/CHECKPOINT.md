# PRODUCTION CHECKPOINT

Production: auraly_venda_fortuna_v3
Angle: 3 (Auraly)
Objective: SALE
Round: VALIDATION
Reference video: input/modelo.mp4 (video2_modelo.mp4)
Scenario: cozinha americana do modelo (armários brancos no gancho, nogueira escura com puxadores dourados no corpo, quina de mármore branco com veios, backsplash creme, piso de lajotas bege); Jordan Vale: a mesma cozinha como cozinha de mansão de luxo (regra do Luigi, 2026-10-07)

Current stage: PRODUCTION_COMPLETE
Current avatar: NONE
Next action: Luigi gera K e V no Flow com o AGENTE_FLOW.md (character sheet do Jordan já gerado por ele, arquivos em producao/auraly_avatares_rico_careca/, PR #35); quando ele confirmar a postagem, registrar com python3 gerenciar_operacao.py registrar

## Avatar queue
[DONE] Jordan Vale: character sheet gerado pelo Luigi em 2026-10-07 (descrição em producao/auraly_avatares_rico_careca/AVATARES_RICO_CARECA.md); caminho esperado `producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg`
[DONE] Avery Knox: producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg
[DONE] Devon Price: producao/_ancoras/character_sheets/devon_price_character_sheet.jpg (antes chamada Celeste Marlow; renomeada pelo Luigi em 2026-10-07; sheet gerado por ele, arquivos em producao/auraly_avatares_rico_careca/)

## Approved script
status: APPROVED (Luigi, 2026-10-07)
file: ROTEIRO.md

## Selected hooks
status: APPROVED (hook fiel aprovado junto com o roteiro, 2026-10-07)
hooks: HOOK 1 - FIEL - Painel do rodapé com notas de $100
formato: fiel-validacao
acao estrutural: avatar ajoelhado abre um painel escondido do rodapé, revela um monte de notas e tira uma para mostrar à lente
eixos de troca: n/a (validacao)

## Current avatar assets
image prompts: FLOW_<AVATAR>.md dos 3 avatares (K01, K02)
video prompts: FLOW_<AVATAR>.md dos 3 avatares (V01 a V14)

## Completed
- Roteiro e hook fiel aprovados pelo Luigi em 2026-10-07
- FICHA_FRAMES.md (K01, K02, placar 14/14) + gerar_pacote.py; pacotes de Jordan Vale, Avery Knox e Devon Price entregues 2026-10-07, AGENTE_FLOW.md só desta produção
- Intake: video2_modelo.mp4, Avery Knox e Jordan Vale (descrição)
- ANALYSIS: /watch em input/modelo_watch/; 102,2s, gancho mudo de 5,4s com cortes, corpo em plano único
- SCRIPT_MODELLING: ROTEIRO.md + GANCHOS_VISUAIS.md

## Pending
- Geração no Flow, montagem e postagem (marcos do Luigi)

## User decisions
- Decision: venda Auraly com dinheiro e fortuna, promessas e consequências agressivas se pular os selos
  Reason: Luigi, 2026-10-06
  Operational consequence: tom agressivo sem mal real e sem valor em dólar garantido
- Decision: K só com character sheet + prompt (sem frame modelo); V só com a imagem escolhida + prompt; 4 variações por K, 1 por V, 9:16
  Reason: Luigi, 2026-10-06
  Operational consequence: cenário, pose e ação do modelo vão por escrito em cada K

- Decision: nomes definidos em 2026-10-07: o ricaço (antes Gordon Ashby) é Jordan Vale e a careca (antes Celeste Marlow) é Devon Price; Avery Knox fica como está
  Reason: Luigi, 2026-10-07
  Operational consequence: nomes, arquivos e sheets (jordan_vale_ e devon_price_character_sheet.jpg) trocados em todo o pacote
- Decision: cenário do ricaço (Jordan Vale) sempre de luxo máximo: dentro de casa = mansão com a mesma ação do modelo; carro = carro de luxo ou esportivo; ao ar livre = lugar de luxo famoso (Paris, Dubai, Marrocos). Avery mantém o cenário original.
  Reason: Luigi, 2026-10-07
  Operational consequence: K do Jordan descrevem cozinha de mansão com o painel do rodapé; Scenario do Jordan registrado à parte do da Avery

## Next response format
- Roteiro bilíngue completo, depois pacote por avatar (MAPA K/V, K, V, transcrição) e o bloco do agente Flow só desta produção
