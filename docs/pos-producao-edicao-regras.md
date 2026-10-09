# Edição de takes do Flow: regras fixas (acertos e erros)

Fonte: 1º teste nosso, FitWell growth v2 chá glow, 2026-10-09 (caso 31 em `pos-producao-casos.md`),
aprovado pelo Luigi ("o resultado me agradou muito"). Vale para TODA edição com a skill `edicao`.
O estilo aprovado é o v3: `template/edit_ritmo_v3.mjs`. Nenhum item aqui é opcional.

## Acertos que viram regra (garantir sempre)

### Antes de editar
1. **Confirmar qual vídeo é** pelo conteúdo dos takes (contact sheet) e pelo roteiro da produção,
   antes de qualquer corte. Se não bater com o esperado, avisar o Luigi.
2. **Transcrever cada take** e comparar com a fala literal do roteiro. Fala faltando ou trocada é
   problema do take, avisa antes de editar.

### Cortes e ritmo
3. **Cortar pelos silêncios reais** do áudio (`silencedetect=noise=-35dB:d=0.15`), nunca pelo tempo
   do whisper (ele estica a palavra até a seguinte e esconde a pausa).
4. **Ilha de som sem nenhuma palavra cai** (ruído de fim de take, respiração).
5. **Ilha de fala menor que 0,4s junta com a vizinha**: senão vira um piscar.
6. **Segmentos a menos de 0,05s um do outro viram um só**: corte invisível só cria risco.
7. **Folga de 0,05s antes e 0,11s depois** de cada trecho de fala: a sílaba final não some.
8. **Fala a 1,12x** (alvo 3,5 a 3,7 palavras por segundo; o teste deu 3,64).
9. **No take-herói visual (o reveal), a pausa é ACELERADA 5x, não cortada**: a transformação
   continua sem pulo e a pausa vira ~0,3s. Marcar o take em `RAMP`.
10. **Corte dentro do filtro** (`trim`/`atrim`), nunca `-ss` antes do `-i`.
11. **24→30fps com `minterpolate` POR SEGMENTO**, antes do `concat` (ver erro 1).

### Legenda e acabamento
12. **Tempo da legenda = whisper no vídeo JÁ cortado; texto da legenda = roteiro.** Quando a contagem
    de palavras bate, nenhuma escuta errada vai para a tela. Se não bater, o script avisa: conferir.
13. Merriweather 900, 64px, branca, minúscula, sem animação, sombra suave, 1 a 3 palavras por página,
    quebra no ponto final, na vírgula (com 2+ palavras) e na troca de take.
14. Legenda no centro (top 880px); no take-herói sobe para 760px, entre o rosto e o objeto. Nunca
    sobre o rosto, nunca sobre o herói.
15. Light leak laranja só na entrada de 2 takes. Cortes secos no resto.
16. Voz em `loudnorm I=-14 TP=-1.2`.

### Conferência antes de entregar (bloqueante)
17. `silencedetect` no vídeo final: só pode sobrar a pausa da rampa (~0,3s).
18. Contact sheet a ±0,1s de **cada** corte: procurar quadro fantasma (dois takes misturados) e pulo.
19. Contact sheet do vídeo final com legenda: nenhuma legenda sobre rosto ou herói.
20. `hyperframes lint`: zero erro (os avisos `nested_structure_needs_subcomposition` das legendas são
    inofensivos).

### Entrega
21. Recomprimir o render (`libx264 -crf 19 -preset slow`, AAC 192k, `+faststart`): o render `high`
    deu 49 MB para 25s e o limite de cópia para o Mac é 30 MB. Saiu com 20 MB, sem perda visível.
22. Entregar **anexado na thread** e **gravado na pasta dos takes** do Luigi, nome
    `vNN_<tema>_editado.mp4`. Cópia em `/mnt/project-files/edicao/<produção>/`. Nunca no repo.

## Erros que não podem voltar

| # | Erro | Causa | Trava |
|---|---|---|---|
| 1 | Quadro fantasma na troca T3→T4 (dois takes misturados) | `minterpolate` no vídeo inteiro interpola através do corte | Regra 11 + conferência 18 |
| 2 | Travadas leves na v2 do Pedro | ilhas < 0,4s, folga de 0,07s, `-ss` antes do `-i`, 24→30fps irregular | Regras 5, 7, 10, 11 |
| 3 | Script v2 não rodava na nuvem | dependia de `../words`, `../sfx/lofi.mp3` e de um caminho de modelo whisper do Mac do Pedro | v3 usa `palavras.py` (faster-whisper, já instalado) e não depende de nada fora da pasta |
| 4 | Fonte da legenda não estava no repo | baixada do Google Fonts na hora | `template/fonts/Merriweather900.woff2` agora no repo (licença OFL) |
| 5 | Cortes de 0,01s entre trechos quase colados | folgas de dois trechos se encostando | Regra 6 |
| 6 | Vídeo sem música | não há trilha no repo | Pedir a faixa ao Luigi ou deixar uma trilha padrão no repo (ver sugestão 5) |
| 7 | Primeira base jogada fora (7 min perdidos) | o erro 1 só apareceu na conferência | Regra 11 já no script; conferência 18 continua obrigatória |

### Erros que vêm do Flow (corrigir no prompt, não na edição)
- **Continuidade de objeto:** o bule ganhou tampa de madeira no T4 e não tinha no T3. Todo K e V do
  mesmo objeto descreve o objeto igual (com ou sem tampa).
- **Ação que acontece na pausa:** o T4 começa com o bule no réchaud e ela só levanta na pausa, então
  o corte pula a ação. Prompt de vídeo que começa com o objeto na mão (como o K04) diz isso na ação.
- **Gesto pedido não veio:** o T5 pedia a mão apontando para baixo e ela não aponta. Gesto de CTA vai
  na linha de ação do V, curto ("points down at the caption").

## Sugestões para ficar mais rápido com o mesmo resultado (propostas, aguardam o ok do Luigi)

Tempo deste teste: ~7 min de base (minterpolate) + ~2 min de render + conferência. Sem o retrabalho,
~12 min do envio dos takes até a entrega.

1. **Um comando só** (`edicao.sh <pasta>`): copia os takes, transcreve, confere a fala contra o
   roteiro, monta a base, roda lint, render, as 4 conferências e a recompressão, e devolve um
   relatório passa/falha. Mesmo resultado, sem passo esquecido.
2. **Interpolação em paralelo**: cada trecho num processo separado ao mesmo tempo, em vez de um
   ffmpeg só. Mesmo resultado quadro a quadro; a base cai de ~7 min para ~1-2 min.
3. **Achar o roteiro sozinho**: comparar a transcrição dos takes com todos os roteiros do repo e
   escolher a produção. O Luigi só manda a pasta, sem dizer qual vídeo é.
4. **Conferência automática do quadro fantasma**: medir a semelhança dos quadros em cada corte e
   reprovar sozinho se aparecer quadro misturado. Tira a dependência de olhar contact sheet.
5. **Trilha padrão no repo** (música livre de direitos, bem baixa, com ducking como na v2): o vídeo
   sai com música sem precisar pedir.
6. **Pasta nomeada pela produção** (ex.: `fitywell_growth_v2/`) em vez de `v02/`: identifica o vídeo
   na hora, mesmo sem a sugestão 3.
7. **(Mais rápido, muda um pouco o resultado)** Fala a 1,25x em vez de 1,12x: 24fps × 1,25 = 30fps
   exatos, sem interpolação nenhuma (base em segundos). A fala fica ~4 palavras/s, mais rápida que a
   referência aprovada. Só com teste e ok do Luigi.
