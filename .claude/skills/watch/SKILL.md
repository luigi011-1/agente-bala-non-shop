---
name: watch
description: "Assiste" um video .mp4 de referencia de forma completa — extrai cenas, hook denso, timeline densa (pega reveals dentro de um take) e transcreve o audio com Whisper — e entrega a decomposicao beat a beat com o heroi do hook identificado. Use quando o usuario mandar /watch, enviar um .mp4 para modelar/clonar, ou pedir para analisar/decompor/assistir um video de referencia. Substitui a extracao esparsa de frames do processo antigo.
---

# /watch — Assistir e decompor um vídeo de referência

Este é o passo aprimorado da **Fase 2 (Decomposição)** da operação. Objetivo: entender o vídeo-referência **sem deixar nada passar** — em especial o **herói do hook** e qualquer **reveal/transformação que acontece DENTRO de um take** (ex.: cristais derretendo e mostrando os gomos da barriga). O processo antigo (frames esparsos + miniaturas minúsculas) perdia esses momentos. Este não pode.

> O vídeo pode ser de avatar IA ou de **pessoa real (orgânico)**. Classificar a ORIGEM antes da decomposição (desde 2026-09-25): orgânico segue `PERFIL_ORGANICO.md` e ganha a ficha orgânica do passo 6. Ver as memórias `metodo-puzzle`, `processo-7-fases`, `erros-recorrentes`, `restricoes-protocolo`, `formato-organico-real`.

## Dependências e preparação no Windows
- `ffmpeg`/`ffprobe`, Python 3.12 e um ambiente virtual `.venv` na raiz do projeto.
- As versões validadas de `faster-whisper`, `ctranslate2`, `Pillow` e `av` estão fixadas em `requirements.txt`.
- Para preparar ou reparar o ambiente, rode:
  ```
  powershell -ExecutionPolicy Bypass -File ".claude/skills/watch/scripts/setup_windows.ps1"
  ```
- O wrapper `run_watch.ps1` usa primeiro o Python da `.venv` e não depende de caminho de usuário fixo.

## PORTAO P1 — ler ANTES de rodar o pipeline

- `biblioteca-videos` → **este esqueleto ja foi produzido?** Se ja, qual variavel usamos e o que nao repetir
- `erros-recorrentes` → os 3 erros historicos de leitura de hook

## PORTAO P2 — depois da transcricao, ANTES de tocar na copy

**Nada de metodo puzzle antes de reler estes.** Lista completa no PORTAO P2 do `CLAUDE.md`:
`metodo-puzzle` · `feedback-copy-lapida-estrutura` (rodar o CRIVO) · `referencia-frameworks-copy` ·
`congruencia-matriz` · `estilo-copy-sem-travessao` · a memoria do angulo · e, se houver fechamento,
`banco-rotas-argumentativas` com o LOG + `banco-obstaculos` + `feedback-ponte-argumentada`.

So depois disso a copy pode ser modificada e entregue pro Luigi aprovar ou ajustar.

## Passo a passo (siga na ordem)

### 1. Localizar o `.mp4`
Pegue o caminho do vídeo que o usuário enviou/apontou. Se não estiver claro, pergunte o caminho. Peça também o **roteiro**, se ele tiver (a fala do original serve de conferência cruzada com a transcrição).

### 2. Rodar o pipeline
```
powershell -File ".claude/skills/watch/scripts/run_watch.ps1" -Video "CAMINHO_DO_VIDEO.mp4"   # Windows
bash .claude/skills/watch/scripts/run_watch.sh "CAMINHO_DO_VIDEO.mp4"                          # nuvem, macOS, Linux
```
Na nuvem não existe `.venv`: o `run_watch.sh` usa o Python do sistema, onde o `SessionStart` já
instalou tudo e deixou o modelo do Whisper baixando em segundo plano. Desde 2026-10-05 o pipeline
roda as etapas ao mesmo tempo (transcrição num processo próprio, cenas e timeline numa passada só do
ffmpeg, grades em todos os núcleos) e imprime `tempos:` no fim. A saída é a mesma de antes, arquivo
por arquivo. Se o Whisper falhar, frames, grades e manifest saem igual e o aviso diz o motivo.
Opcional: `-Extra "--model medium.en"` para transcrição mais precisa (mais lenta); `-Extra "--timeline-fps 10"` para densidade ainda maior; `-Extra "--scene-threshold 0.15"` para pegar cortes mais sutis.

Isso gera, em `<pasta_do_video>/<nome>_watch/`:
- `frames/scenes/` — 1 frame por corte de cena (mapa de takes)
- `frames/timeline/` — **vídeo inteiro** amostrado a 0,2s (5fps) ← pega reveals dentro de qualquer take: hook, corpo E cta
- `audio/transcript.txt` e `.json` — fala com timestamps
- `overview/` — grades legíveis (visão geral)
- `manifest.json` — índice de tudo com timestamps

### 3. Ler a transcrição
Abra `audio/transcript.txt`. Ela dá a fala beat a beat com tempo. Se o usuário mandou roteiro, confira as duas — divergências indicam onde o áudio/tempo importa.

### 4. Ler as grades de visão geral (em resolução cheia)
🔴 **Ler EM LOTE, nunca uma imagem por vez** (2026-10-05). Várias chamadas `Read` na MESMA
mensagem chegam juntas e cortam a maior parte da espera, sem perder nada: são as mesmas imagens,
na mesma resolução, e quem olha continua sendo você. Lote 1: todas as `overview_scenes_*` mais a
`transcript.txt`. Lote 2: as `overview_timeline_*` do hook (as 2 primeiras cobrem 8s). Depois o
resto da timeline em lotes de até 6 grades. Nunca delegar a leitura das grades a um subagente:
quem escreve a decomposição é quem precisa ter visto o vídeo.

Leia, nesta ordem, as imagens em `overview/`:
1. `overview_scenes_*` — entenda o arco/estrutura (quantos takes, o que é cada um).
2. `overview_timeline_*` — varra o vídeo INTEIRO em sequência (0,2s por frame). Dê **atenção máxima aos primeiros ~6-8s (o hook — aqui mora o herói)**, mas varra também corpo e CTA procurando **mudanças dentro de um mesmo take** (algo derretendo, encolhendo, saindo, sendo lavado).

### 5. Zoom nos momentos-chave (full-res)
Para o hook e para QUALQUER reveal/transformação que você suspeitar nas grades:
- Dê `Read` nos frames **full-res** individuais correspondentes (em `frames/timeline/`, use o timestamp do nome), todos os frames de um momento na mesma mensagem.
- Se precisar de ainda mais densidade num intervalo (ex.: o exato instante do reveal entre t=3,0 e t=4,5), re-extraia ultra-denso só nessa janela:
  ```
  ffmpeg -ss 3.0 -t 1.5 -i "VIDEO.mp4" -vf "fps=15" -qscale:v 2 "SAIDA/zoom_%03d.png"
  ```
  e leia esses frames. **Nunca conclua o herói/reveal sem ver o instante do pico.**

### 6. Montar a decomposição beat a beat
Para cada take, preencha (formato da memória `processo-7-fases`):

| Timestamp | Esqueleto visual | Nº pessoas | Props | Fala (da transcrição) | Label (HOOK/MECANISMO/RECEITA/PROTOCOLO/RESULTADO/PROVA/CTA) | TALKING/B-ROLL | O que muda vs. take anterior |

E responda explicitamente:
- **Qual é o herói do hook** (exato — o que para o scroll). Sem pattern-matching.
- **Há reveal dentro de algum take?** Onde, e o que revela.
- **Qual é a AÇÃO que muda entre os frames?** (o que abre/derrete/encolhe/se move/é lavado). NÃO ler um retrato parado — rastrear a ação. Cruzar com a transcrição literal: se a fala diz opens/melts/moves/clears, achar isso acontecendo na tela. (Erro histórico #3: li "mulher com carrinho" quando o herói era o homem **abrindo a caçamba emperrada com uma mão**; a fala dizia "it never opens".)
- **Movie style: qual é o FEITO físico que dispara a fala de admiração/inveja?** ("strong as you" aponta pra uma ação de força específica — achar qual.)
- **Quem faz o quê e quem tem qual prop?** Rastrear quem chega/segura o quê ao longo dos frames (não presumir dono de prop).
- **Há 2ª pessoa?** Qual o papel (cliente/herói)?
- **O que muda entre takes** (cor de roupa fingindo dias, tamanho de algo, ângulo)?
- **Props de credibilidade** (luvas, livro, modelo anatômico)?

**Se a origem for orgânica (pessoa real), acrescentar a FICHA ORGÂNICA** (`PERFIL_ORGANICO.md`):
- objeto na mão no primeiro segundo, e a que distância da lente (ou "selfie sem objeto, mãos perto da lente")
- câmera: selfie na mão, celular apoiado, tripé, POV; número de cortes e o maior plano em segundos
- a fala começa em que segundo; a primeira frase literal
- molduras verbais: seleção ("meant for you"), prazo ("tomorrow at 11am"), engajamento como condição
- texto de tela fixo (tarja) além da legenda, se houver
- **CTA original literal** e o CTA que o substitui pelo ângulo e objetivo
- palavras que precisam de troca de marca (`spell`, `enchanted`, nome ou @ do criador)

### 7. Confirmar antes de produzir
Se houver **qualquer ambiguidade** sobre o herói do hook ou um reveal, **confirme com o usuário** antes de gerar prompts (regra da memória `erros-recorrentes`: os dois erros históricos foram de leitura de hook). Só depois siga para a definição da variável (Fase 3) e os prompts de imagem (Fase 5).

## Regras que este passo NÃO pode violar
- **Frame a frame denso de verdade** — inclusive dentro dos takes. Se um reveal existe no original, o clone tem que mostrá-lo (memória `erros-recorrentes`, falha #1).
- **Não presumir estrutura / não pattern-matching.** A primeira leitura costuma ser a errada.
- A transcrição é **conferência**, não substitui a análise visual do herói.
