---
name: auraly-cenario-novo-character-sheet
description: "SÓ AURALY APP (Luigi, 2026-10-04): CENÁRIO E ÂNGULO DE CÂMERA = OS DO VÍDEO MODELO, quase 100% fiéis, nunca inventados; orgânico, NADA sobrenatural; só o acabamento do GATE_VISUAL muda (luz neutra, céu/janela com cor, herói colado na lente, foco, realismo). Anexo de todo K = CHARACTER SHEET (identidade e roupa) + frame do modelo. 'Cenário do modelo:' em cada K da FICHA_FRAMES e 'Scenario:' no CHECKPOINT. Revoga só no Auraly o cenário fixo da âncora. FitWell, Sea Moss e Body Hacks NÃO mudam."
metadata:
  type: feedback
---

Em 2026-10-04 o Luigi gerou os character sheets dos quatro avatares do Auraly com o prompt universal
(`producao/_ancoras/PROMPT_CHARACTER_SHEET_AURALY_2026-10-04.md`) e decidiu, em duas mensagens:

1. *"quero que os prompts sejam detalhando bem o ambiente para esses avatares, porque eu quero
   diversificar o cenário e não me prender a somente um que não está validado [...] somente para as
   produções do Auraly App."*
2. Logo depois, refinando: *"quero que seja o mais orgânico possível, não quero que seja nada
   sobrenatural; puxe bastante do cenário do vídeo que está sendo modelado, não inventa muita moda em
   questão de cenário; só coloca as regras padrões para ter um nível de realismo [...] herói do hook
   perto da câmera, as regras do céu nublado etc. Mas o ângulo e o cenário têm que ser quase 100% fiéis
   ao vídeo que a gente está modelando. Isso é muito importante."*

**Why:** o cenário fixo da âncora nunca foi validado por resultado. O que viralizou foi o vídeo modelo
inteiro, cenário e ângulo incluídos; copiar esses dois é a forma de variar o cenário sem inventar e
sem perder o que fez o modelo funcionar. Cenário inventado e efeito sobrenatural afastam do orgânico,
que é o que performa.

**How to apply (só Auraly; fonte do processo: `WORKFLOW_AURALY.md`, bloco de 2026-10-04):**
1. **Cenário = o do vídeo modelo**, quase 100%: mesmo tipo de lugar, disposição, móveis, superfícies,
   cores, janela ou parede atrás e objetos de fundo. Não inventar cenário. Cada modelo traz o seu.
2. **Ângulo de câmera = o do vídeo modelo**, quase 100%: altura, distância, lente, inclinação, selfie
   ou apoiado, enquadramento. Medido no frame (ficha F4). Não adaptar a câmera ao cenário da âncora.
3. **Só o acabamento do `GATE_VISUAL.md` Partes 1 a 3 muda**: luz neutra de dia nublado, céu ou janela
   com cor e textura (nunca branco), herói do gancho colado na lente (nunca mais longe que no modelo),
   foco total, trecho de realismo, 2 a 3 âncoras de fundo (as do modelo), bandeira discreta (IA:
   obrigatória; orgânico: opcional), sem texto. Cada mudança vai como desvio na ficha.
4. **Orgânico, nada sobrenatural**: sem brilho mágico, aura, luz saindo de objeto, partícula, objeto
   flutuando, fumaça mística ou VFX. Efeito só se o PRÓPRIO modelo tiver, copiado como no modelo.
5. **Anexos de todo K**: 1) `producao/_ancoras/character_sheets/<avatar>_character_sheet.jpg`
   (identidade e roupa; Avery Knox, Devon Price, Jordan Vale, Morgan Vance); 2) o frame do modelo do
   mesmo código (cenário, ângulo, enquadramento). Proibido no K: `the same lived-in room as the
   reference`, `as the reference, unchanged`, `own setting`.
6. **Ficha e checkpoint**: cada `## Kxx` da `FICHA_FRAMES.md` tem `Cenário do modelo:` e o `scene` sai
   dela; `Scenario:` no `CHECKPOINT.md`; linha em `producao/_ancoras/CENARIOS_AURALY.md` (histórico por
   conta, nunca vence a fidelidade ao modelo).
7. **Roupa**: a do character sheet, até o Luigi decidir outra coisa.
8. **Trava de máquina**: `checar_entrega.py`, check `cenario`, reprova produção Auraly nova sem
   `Scenario:`, sem `Cenário do modelo:` em algum K da ficha, sem character sheet no K ou com frase que
   prende o cenário à âncora. Legado em `controle/cenario_auraly_legado.json`. Flow v18. Hook de
   roteamento repete a regra a cada mensagem.
9. **Não vale fora do Auraly:** FitWell (Ângulos 2 e 4) e Sea Moss (Ângulo 1) seguem com avatar fixo
   por conta, roupa e cenário da âncora ([[checklist-envio-prompt]] B8).

Ver [[avatares-fichas]] (nomes = arquivos do Luigi), [[ficha-do-frame-placar]] e
[[feedback-fingerprint-cenario-por-gancho-auraly]] (histórico).
