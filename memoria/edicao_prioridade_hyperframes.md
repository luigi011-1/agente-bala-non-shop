---
name: edicao-prioridade-hyperframes
description: "Na edição automática, o que o repositório HyperFrames oferece (assets, catálogo, estilos E regras de edição) tem prioridade sobre os assets e regras próprias do Luigi"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 568a6691-d69f-4cc0-97d9-5e6b568bec6b
  modified: 2026-10-10T07:15:14.947Z
---

Na pós-produção (skill `edicao`), **priorizar em tudo o que o repositório HyperFrames
(github.com/heygen-com/hyperframes, clone em `~/ferramentas/hyperframes`) oferece**: efeitos sonoros da
biblioteca do `media-use` (Pixabay), estilos de legenda `caption-*` do catálogo, efeitos do catálogo (grain,
flash), looks/LUTs do `media-use`, e também as **regras e o estilo de edição** das skills dele
(embedded-captions: rail + embed escasso, cada legenda ≥ 0,5s, rosto nunca coberto, matte em CPU, não graduar a
filmagem fora das reações de plate; hyperframes-studio: safe zones). Os assets e regras próprias do Luigi
(wav do template, Merriweather v3, docs/pos-producao-edicao-regras.md) ficam como alternativa e não valem 100%.

**Why:** Luigi, 2026-10-10, ao pedir o acabamento HyperFrames: "dê prioridade aos elementos que o repositório
que te enviei oferece, não aos que eu te enviei, a nível de tudo" e "isso também serve para o estilo de edição
e regras do repositório, não as minhas regras 100%". Ele achava que o resultado devia ser bem melhor.

**How to apply:** ao decidir padrão de som, legenda, efeito ou regra de corte/legenda na edição, consultar
primeiro a skill HyperFrames correspondente; usar o do Luigi só onde a HyperFrames não cobre ou quando ele
pedir. Conferência palavra por palavra contra o roteiro e o ritmo/corte de silêncio continuam (a HyperFrames
não cobre). Ele também quer **variações disponíveis** (música, SFX, estilo de legenda), mas para **girar de
um vídeo para o outro** (rodízio `auto` do `acabamento.CARDAPIO`), nunca para testar todas em cada vídeo.
Primeiro teste (V02, 2026-10-10): palavra atrás do avatar + legenda `caption-highlight` + cortes = "ficou irado".
**Música a -18 dB da voz** (cama do media-use, 0,12) aprovada no mesmo dia: -25 quase não se ouvia.
Ver [[edicao-licoes-teste]].
