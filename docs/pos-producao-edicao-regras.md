# Edição de takes do Flow: regras fixas (acertos e erros)

Fonte: 1º teste nosso, FitWell growth v2 chá glow, 2026-10-09 (caso 31 em `pos-producao-casos.md`),
aprovado pelo Luigi ("o resultado me agradou muito"). Vale para TODA edição, em **todos os ângulos**
(Sea Moss, FitWell, Auraly, Body Hacks e os próximos; venda e growth).
O estilo aprovado é o v3. **Desde 2026-10-09 ele roda num comando só**, que cumpre e confere estes
itens sozinho: `python3 .claude/skills/edicao/template/editar.py <pasta_dos_takes>` (ver o fim deste
arquivo). Nenhum item aqui é opcional.

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
16b. **Música sempre a -25 dB da voz** (Luigi, 2026-10-09; -10 dB ficou alta e atrapalhou a fala): a faixa é normalizada para -14 LUFS (o
    nível da voz) e baixada 25 dB, sem ducking, com 0,3s de entrada e 0,8s de saída; silêncio de
    abertura da faixa é pulado. Faixas do Luigi em `/mnt/project-files/edicao/musicas/` (fora do repo);
    a mesma produção sempre pega a mesma faixa, ou a que o Luigi pedir.

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
| 6 | Vídeo sem música | não havia trilha | 9 faixas do Luigi em `/mnt/project-files/edicao/musicas/`, regra 16b |
| 7 | Primeira base jogada fora (7 min perdidos) | o erro 1 só apareceu na conferência | Regra 11 já no script; conferência 18 continua obrigatória |

### Erros que vêm do Flow (corrigir no prompt, não na edição)
- **Continuidade de objeto:** o bule ganhou tampa de madeira no T4 e não tinha no T3. Todo K e V do
  mesmo objeto descreve o objeto igual (com ou sem tampa).
- **Ação que acontece na pausa:** o T4 começa com o bule no réchaud e ela só levanta na pausa, então
  o corte pula a ação. Prompt de vídeo que começa com o objeto na mão (como o K04) diz isso na ação.
- **Gesto pedido não veio:** o T5 pedia a mão apontando para baixo e ela não aponta. Gesto de CTA vai
  na linha de ação do V, curto ("points down at the caption").

## Comando único (sugestões 1 a 5, aprovadas pelo Luigi em 2026-10-09)

```
python3 .claude/skills/edicao/template/editar.py <pasta_dos_takes> [--producao <slug>] [--musica <nome>] [--ramp 1] [--leaks 2,4] [--up 1]
```

1. **Um comando só** com relatório: transcreve, acha o roteiro, confere a fala, corta, monta, legenda,
   mixa, roda lint e render, recomprime e escreve `RELATORIO.md` com passa/falha das conferências
   17, 18 (automática) e 20, mais `cortes.png` e `legendas.png` para a conferência 19 (olho humano).
   Sai com erro se qualquer conferência falhar; vídeo com FALHA não é entregue.
2. **Trechos em paralelo**: cada trecho é interpolado num processo próprio (um por núcleo) e os
   trechos são juntados sem recodificar. Mesmo filtro do v3, trecho a trecho. O minterpolate engole
   os últimos quadros de cada trecho: o script completa clonando o último quadro e numera os quadros
   de novo, e o áudio do trecho fica com a duração exata do vídeo (sem deriva de lábio).
3. **Roteiro e ORDEM achados pela fala**: a ordem dos takes é a ordem das frases no roteiro, não o
   nome do arquivo (qualquer nome serve; o relatório avisa quando o nome discorda). Take mudo precisa
   do número no nome; frase repetida em dois takes gera aviso. O roteiro sai da comparação da fala
   dos takes com todas as falas entre aspas dos `.md` de
   `producao/` e de `/mnt/project-files/entregas/`. Abaixo de 85% de semelhança, para e pede `--producao`.
4. **Quadro fantasma automático**: em cada corte, um quadro parecido com os DOIS vizinhos de uma troca
   de cena reprova. Testado: acha o erro do caso 31 e passa a versão aprovada.
5. **Música padrão** a -25 dB da voz (regra 16b).

Teste no v02 (2026-10-09): mesmo vídeo aprovado (24,7s, 3,64 palavras/s, mesmos cortes), agora com música, em ~6 min do comando ao arquivo (antes ~12 min mais conferência na mão). A base caiu de ~7 min para ~2,5 min; o render no HyperFrames (~2,5 min) é o que mais pesa agora.

Sugestões que ficaram de fora: pasta com o nome da produção (a 3 resolve) e fala a 1,25x (muda a entrega).
