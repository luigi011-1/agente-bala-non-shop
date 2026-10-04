---
name: auraly-cenario-novo-character-sheet
description: "SÓ AURALY APP (Luigi, 2026-10-04): o anexo de todo K é o CHARACTER SHEET do avatar (close do rosto + frente, costas, lados, fundo cinza) e CADA PRODUÇÃO ganha um CENÁRIO NOVO, descrito por inteiro no campo scene, sem repetir producao/_ancoras/CENARIOS_AURALY.md. Roupa continua a do sheet. Revoga só no Auraly a parte de cenário do avatar fixo por conta. FitWell, Sea Moss e Body Hacks NÃO mudam."
metadata:
  type: feedback
---

Em 2026-10-04 o Luigi gerou os character sheets dos quatro avatares do Auraly com o prompt universal
(`producao/_ancoras/PROMPT_CHARACTER_SHEET_AURALY_2026-10-04.md`) e decidiu: *"quero que os prompts
sejam detalhando bem o ambiente para esses avatares, porque eu quero diversificar o cenário e não me
prender a somente um que não está validado. A partir das próximas produções quero que aconteça isso
[...] deixa claro que isso aconteceu somente para as produções do Auraly App."*

**Why:** o cenário fixo da âncora (cozinha de pinho, cozinha branca, varanda, quarto) nunca foi
validado por resultado. Repetir um cenário não validado em todo vídeo prende a conta a uma aposta que
ninguém testou; variar o cenário por produção é o que deixa o resultado dizer qual funciona.

**How to apply (só Auraly; fonte do processo: `WORKFLOW_AURALY.md`, bloco de 2026-10-04):**
1. Anexo de todo K: `producao/_ancoras/character_sheets/<avatar>_character_sheet.jpg`
   (Avery Knox, Devon Price, Jordan Vale, Morgan Vance). A foto em cena real deixa de ser anexo.
2. `reference_use`: usar o sheet só para identidade e roupa, ignorar o fundo cinza; o cenário vem só do texto.
   Proibido no K: `the same lived-in room as the reference`, `as the reference, unchanged`, `own setting`.
3. Cenário NOVO por produção, real e americano, congruente com o vídeo modelo e com o avatar, que não
   repete nenhuma linha da mesma conta em `producao/_ancoras/CENARIOS_AURALY.md`. Todos os K da
   produção no mesmo cenário. `Scenario:` no CHECKPOINT e linha nova no CENARIOS_AURALY.md na entrega.
4. `scene` detalhado nesta ordem: lugar e região dos EUA; arquitetura e materiais com cor; janela ou
   céu com cor e de onde vem a luz; 2 a 3 âncoras de fundo nomeadas com posição; bandeira (formato IA)
   e kit Auraly quando couber. Detalhar não é inventariar: o teto de 2 a 3 âncoras do GATE_VISUAL vale.
5. Roupa: a do character sheet em todo K e todo vídeo da conta, até o Luigi decidir outra coisa.
6. Trava de máquina: `checar_entrega.py` (check `cenario`) reprova produção Auraly nova sem
   `Scenario:`, sem "character sheet" no K ou com frase que prende o cenário à âncora. Legado em
   `controle/cenario_auraly_legado.json`. Instruções do Flow v18. Hook de roteamento lembra a regra.
7. **Não vale fora do Auraly:** FitWell (Ângulos 2 e 4) e Sea Moss (Ângulo 1) seguem com avatar fixo
   por conta, roupa e cenário da âncora ([[checklist-envio-prompt]] B8).

Ver [[avatares-fichas]] (nomes = arquivos do Luigi) e [[feedback-fingerprint-cenario-por-gancho-auraly]] (histórico).
