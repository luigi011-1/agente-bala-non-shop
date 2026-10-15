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
**Vale também para o AURALY** (Luigi, 2026-10-10: "quero esse mesmo estilo de edição automática para os vídeos de
Auraly também"): mesmo acabamento e rodízio; no Auraly a opção `padrao` do rodízio é a legenda de referência dele
(palavra por palavra empilhada), os selos 777/222 ficam por cima, o flash da saída do gancho vem do catálogo e o
pico nunca cai no take mudo do gancho nem no CTA de `222`/Stories.
Ver [[edicao-licoes-teste]].

♻️ **2026-10-13 (Luigi): rodar a edição automática USANDO as skills HyperFrames instaladas** (`npx skills add
heygen-com/hyperframes -g`, 21 skills em `~/.agents/skills/`): a habilidade pronta das skills + as regras da operação.
O que a skill cobre (render, workers, `--gpu` VideoToolbox, `clean`, catálogo, legendas, áudio) vem dela; o que ela
não cobre (conferência palavra por palavra, corte de silêncio, ritmo, exceções de fala) segue no `editar.py`.
Toda troca de configuração de render é medida (tempo e visual) num vídeo já editado antes de virar padrão.
Medido em 2026-10-13 (camada de picos de 121s, webm com alfa): HyperFrames 0.8.144 = 466s, 0.8.153 = 254s, imagem
idêntica (SSIM 1,000). `acabamento.py` e `legendas_hf.py` passaram para 0.8.153. `--workers auto` e
`HF_CAPTURE_PARALLEL_STREAM=true` NÃO servem para webm com alfa no Mac: grava cada quadro em disco (~30 GB para 2 min).
♻️ **2026-10-13 (Luigi, velocidade acima de tudo): SEM palavra de pico atrás do avatar** (`acabamento.PALAVRA_ATRAS =
False`), **zoom nos picos MANTIDO** (a cada 5s, centrado na cabeça), **legenda PADRÃO** (Pillow, sem render HyperFrames;
o rodízio de legendas do catálogo saiu). Acabamento caiu de ~20 min para ~4 min por vídeo. Para voltar, `PALAVRA_ATRAS
= True` e `--legenda auto`.
♻️ **2026-10-13 (Luigi): SEM efeito sonoro** (repetitivo): `acabamento.SEM_SFX = True` e `--sfx nenhum` no editar; fica só a música de fundo a -18 dB.
♻️ **2026-10-13 (Luigi): legenda DINÂMICA por padrão** (`editar.LEGENDA_DINAMICA = True`, `motor.png_dinamica`): Montserrat 900 caixa alta, branca com contorno preto grosso, a palavra falada em amarelo e 15% maior, troca no tempo da fala; desenhada pelo editor (Pillow), sem render HyperFrames. A serifada "padrao" fica como alternativa.
