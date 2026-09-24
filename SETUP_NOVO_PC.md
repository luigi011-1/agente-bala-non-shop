# Montar a operação num PC novo

Como sair de um computador limpo, **Windows ou Mac**, e chegar na MESMA experiência: mesmo repo,
mesma memória viva, mesmas skills, mesmos gates de máquina, mesmo grafo.

> **No Mac (2026-09-24):** cada passo abaixo tem a versão Mac logo embaixo da do Windows. O Mac usa
> `restaurar_memoria.sh`, `sync_memoria.sh` e `.claude/skills/watch/scripts/setup_mac.sh` /
> `run_watch.sh`, que funcionam no bash 3.2 que vem no macOS e também de dentro de uma worktree.

O clone do GitHub traz o repositório. Ele **não** traz três coisas que ficam fora dele e que são
exatamente as que fazem o agente ser esse agente: a **memória viva**, o **grafo** e o
**ambiente Python**. Os passos 3, 5 e 6 existem por causa disso.

---

## Passo 0 · O caminho importa, e muito

Clonar em `C:\Users\luigi\Desktop\AGENTE NON-SHOP`, com o usuário do Windows chamado `luigi`.

Não é preciosismo. Duas coisas dependem literalmente desse caminho:

1. **A memória viva.** O Claude Code deriva a pasta do projeto do caminho, trocando `:` `\` e espaço
   por `-`. Este caminho vira `C--Users-luigi-Desktop-AGENTE-NON-SHOP`. Outro caminho, outra pasta,
   memória vazia.
2. **O `.claude/settings.json`.** Os dois hooks apontam para caminhos absolutos: o
   `gabarito_hook.py` dentro do projeto e o `graphify.EXE` em `C:/Users/luigi/.local/bin/`.

Se o usuário do Windows tiver que ser outro, ver a seção **Usuário diferente** no fim.

**No Mac** o caminho pode ser qualquer um (o daqui é `~/Desktop/agente-bala-non-shop-main`). Os
scripts `.sh` e o `memoria_lib.py` derivam o slug do caminho real do checkout principal, e o
`settings.json` já usa `$CLAUDE_PROJECT_DIR`, então nada tem caminho fixo de usuário.

---

## Passo 1 · Clonar

```
cd %USERPROFILE%\Desktop
git clone https://github.com/luigi011-1/agente-bala-non-shop.git "AGENTE NON-SHOP"
```

Mac:

```bash
cd ~/Desktop && git clone https://github.com/luigi011-1/agente-bala-non-shop.git agente-bala-non-shop-main
```

O clone pesa cerca de 1 GB, quase tudo imagem de produção e frames de watch.

## Passo 2 · Ligar os gates de máquina

```
git config core.hooksPath .githooks
```

Uma vez por clone. Sem isso o `pre-commit` não roda e volta a depender de alguém lembrar dos
linters, que é a doença que eles curam.

## Passo 3 · Restaurar a memória viva

```
powershell -ExecutionPolicy Bypass -File restaurar_memoria.ps1
python checar_memoria.py
```

Mac:

```bash
bash restaurar_memoria.sh
python3 checar_memoria.py
```

**É o passo que ninguém adivinha.** A pasta `memoria/` do repo é só o espelho. A memória que o
agente lê vive em `~/.claude/projects/<slug>/memory/`, fora do repo, e num PC novo nasce vazia.
Pular este passo dá um agente que tem o processo inteiro e não tem copy, rota, obstáculo, ficha de
avatar nem banco nenhum.

O script deriva o slug sozinho, nunca apaga nada no destino e nunca sobrescreve arquivo divergente
sem `-Force` (no Mac, `--force`). São 65 arquivos em 2026-09-24.

Depois deste passo o sentido volta a ser o normal: a fonte de verdade é a memória viva, e
`sync_memoria.ps1` (no Mac, `bash sync_memoria.sh`) é que roda antes de cada commit que mexe em memória.

## Passo 4 · Python, FFmpeg e a skill `/watch`

```
powershell -ExecutionPolicy Bypass -File .claude\skills\watch\scripts\setup_windows.ps1
```

Instala Python 3.12 e FFmpeg via winget se faltarem, cria o `.venv` do projeto e instala o
`faster-whisper`, que é quem transcreve o vídeo modelo.

Mac (precisa do Homebrew, <https://brew.sh>):

```bash
bash .claude/skills/watch/scripts/setup_mac.sh
bash .claude/skills/watch/scripts/run_watch.sh "CAMINHO/DO/VIDEO.mp4"
```

O `setup_mac.sh` instala `ffmpeg` e `python@3.12` pelo Homebrew se faltarem (o `python3` que vem
no macOS é o 3.9, velho demais para as versões fixadas) e cria o `.venv` com os pacotes de
`.claude/skills/watch/requirements.txt`. O `run_watch.sh` é o equivalente do `run_watch.ps1`.

## Passo 5 · Dependências Python

```
.venv\Scripts\pip install -r requirements.txt
```

FastAPI, uvicorn, httpx e Pillow, usadas só pelo Auraly Studio, arquivado em 2026-09-22. Os scripts da raiz não têm dependência externa, então este passo é opcional.

## Passo 6 · graphify e o grafo

```
uv tool install graphifyy
python grafo_memoria.py
python grafo_producao.py
```

O pacote chama `graphifyy` com dois `y` e entrega os executáveis `graphify` e `graphify-mcp`, mais a
skill global em `~/.claude/skills/graphify/`. Se o `uv` não existir, instalar primeiro em
<https://docs.astral.sh/uv/>.

O `graphify-out/` é ignorado pelo git de propósito, porque é regenerável. Os dois scripts o
reconstroem. Só nós e arestas: comunidades e `GRAPH_REPORT.md` pedem passada semântica, que custa
subagentes.

## Passo 7 · O CLAUDE.md global

Criar `%USERPROFILE%\.claude\CLAUDE.md` com:

```
# graphify
- **graphify** (`~/.claude/skills/graphify/SKILL.md`) - any input to knowledge graph. Trigger: `/graphify`
When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.
```

O `CLAUDE.md` do projeto já vem no clone e carrega sozinho.

---

## O que NÃO vem no clone, e por quê

| O que | Tamanho | Por quê |
|---|---|---|
| `entradas/` e todo `.mp4` / `.wav` | 4 GB | vídeos modelo e áudio, acima do que o GitHub aceita. Inclui o `input/reference_video.mp4` de cada produção |
| `_arquivo/` | ~1 GB | material descartado (Ângulo 3 antigo, Auraly Studio), fora do workflow |
| `.venv/` | 365 MB | ambiente de máquina, o passo 4 recria |
| `graphify-out/` e `grafos/` | 10 MB | regenerável, o passo 6 recria |
| `.claude/settings.local.json` | mínimo | permissões locais, o Claude Code recria ao aprovar |
| `Rei/` | mínimo | vault pessoal, não é da operação |

As **âncoras dos avatares vêm no clone**, em `producao/_ancoras/`. Os vídeos modelo não. Para
produzir a partir de um vídeo antigo é preciso copiar o `.mp4` na mão, ou usar um novo.

---

## Conferir que ficou igual

```
python checar_memoria.py
python checar_entrega.py producao/fitywell_pernas
graphify query "metodo puzzle"
```

O primeiro prova que a memória chegou inteira. O segundo prova que os gates rodam, e o
`fitywell_pernas` é o gabarito vivo, então fecha com zero falhas. O terceiro prova que o grafo
subiu.

Um teste final que vale mais que os três: abrir o Claude Code na pasta e pedir algo que **só** a
memória responde, como qual é a keyword do Ângulo 3. Se vier `222`, está tudo no lugar.

---

## Usuário diferente do `luigi`

Se o Windows do PC novo usa outro nome, três ajustes:

1. **`.claude/settings.json`**: nada a fazer desde que ele passou a usar `$CLAUDE_PROJECT_DIR` e a
   achar o `graphify` pelo PATH. O caminho `C:/Users/luigi/...` só sobra como plano B no Windows.
2. **A memória**: nada a fazer. O `restaurar_memoria.ps1` deriva o slug do caminho real, então já
   escreve na pasta certa daquele PC.
3. **O espelho**: o `sync_memoria.ps1` tem fallback e acha a pasta de memória sozinho quando o
   caminho derivado não existe, desde que só exista um projeto com `MEMORY.md`. O `sync_memoria.sh`
   e o `memoria_lib.py` também aceitam `MEMORIA_VIVA=<pasta>` para apontar na mão.

O caminho da pasta pode mudar sem problema. O que não pode é a memória viva ficar apontando para
um slug e o `settings.json` para outro.
