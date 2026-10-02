---
name: short-form-growth
description: "SHORT FORM de growth (drama atuado de 13 a 30s, sem produto, sem avatar fixo): transgressão FALADA no segundo 0, escada de WTF (quantos o modelo tiver), corte no pico ou na sentença, follow para a parte 2. Medido em 12 virais validados em 2026-09-22. Formato SEPARADO do movie style de venda; nunca misturar os dois."
metadata:
  node_type: memory
  type: reference
  originSessionId: b1a67cc7-fb1f-4b5c-ac0c-c14be840eb2b
  modified: 2026-09-23T02:51:44.211Z
---

# Short form (growth): o formato, pelos 12 virais validados

Fonte: 12 virais que o Luigi mandou em 2026-09-22 (AkuaWrites, Escarleth Drama, USA Relate Tales,
USA Story). Análise completa em
`producao/_swipe_movie_style/rodada_2026_09_22/SHORT_FORM_GROWTH.md`; critério de separação em
`README.md` da mesma pasta.

🔴 **É OUTRO FORMATO, não um pedaço do movie style de venda** ([[movie-style-integral]]).
Classificar antes de tudo: tem produto, marca, link ou keyword = venda; não tem = growth. Growth
segue [[feedback-growth-video-sem-venda]]: zero bloco de venda.

## O que os 12 mostram
- **Uma situação, um cenário, 2 a 4 personagens, 13 a 30s** (mediana 17s). Elenco muda a cada
  vídeo; nenhum personagem fixo.
- **Esqueleto:** transgressão falada (0 a 2s) → escada de WTF → corte (último 1 a 3s).
- **O gancho é FALA, e não abre mudo:** 11 de 12 falam antes de 1s. Frase com alvo explícito,
  verbo de exclusão e **motivo banal** (refrigerante, ingresso, foto). A desproporção é o motor.
  A regra do T1 mudo é do gancho ritual da Auraly e não vale aqui.
- **WTF: contar TODOS, nunca fixar número** (Luigi, 2026-09-23). Na decomposição, listar cada
  momento WTF do vídeo modelo com segundo, quem provoca, tipo e se é falado ou visual. Na amostra
  foram 3 a 5 por vídeo, numa ESCADA (cada um maior que o anterior, a cada 3 a 5s), sempre abrindo
  com a transgressão moral nos 2 primeiros segundos. Na modelagem nenhum WTF do modelo some.
- **Dois finais, ambos validados:** ABERTO (8 de 12) corta na promessa de consequência, antes da
  reação, e é o que carrega o `follow for part 2`; FECHADO (4 de 12) entrega a sentença numa frase.
- **Situações que se repetem:** evento com plateia (casamento, formatura, aniversário, Ação de
  Graças), família recomposta, criança como juiz moral, traição, vítima o menor possível.

## Como o Luigi roda (2026-09-22)
Sem avatar fixo, corte no pico, `follow to part 2` na tela via CapCut. Isso é o uso dele hoje e
não apaga o final fechado, que também está nos virais ([[feedback-virais-validados-sao-a-fonte]]). Teste futuro: variar o
avatar conforme a história, só quando ele pedir e com os avatares que ele mandar
([[avatar-so-o-que-o-luigi-mandar]]).

## Produção (Luigi, 2026-09-23)
- **Character sheet (`REF-P`) de cada personagem principal**, o que aparece em mais de um clipe:
  gerado e aprovado antes de qualquer K. Personagem de uma aparição e figurante não ganham sheet.
- **Voz descrita no prompt de vídeo, para cada personagem** (timbre fixo + emoção da fala). Sem
  Voice Changer ([[checklist-envio-prompt]] C2 e D1).
- **Parte 2 só sob pedido:** ele reenvia o vídeo e pede. É produção própria, abre onde a parte 1
  cortou e reaproveita os `REF-P` da parte 1.
- **Infra pronta (2026-09-23):** linter lê diálogo com rótulo e o bloco `falas no take`, cobra voz
  em cada fala e isenta o piso de palavras em DIÁLOGO; Flow v13 com `REF-P` e V de diálogo.
  Primeira produção e gabarito: `producao/sf_madrasta_frango/` (prompts gerados por
  `gerar_pacote.py`, fonte única do JSON e do bloco do Flow).
- **Workflow APROVADO (2026-09-23)** em `producao/_swipe_movie_style/PROPOSTA_WORKFLOW_MOVIE_STYLE.md`.

## Também é estudo de gancho
Ação estrutural Puzzle: *[AGRESSOR] diz a [VÍTIMA], em [EVENTO COM PLATEIA], uma frase de exclusão
por [MOTIVO BANAL]; [VÍTIMA ou ALIADO] vira o status.* Lições de gancho para outros formatos
(motivo banal, cortar na promessa de consequência, confissão no lugar da negação) entram pelo
método de cada formato, nunca colando estrutura de short form em vídeo de venda.
Ver [[ganchos-variacao-puzzle]].
