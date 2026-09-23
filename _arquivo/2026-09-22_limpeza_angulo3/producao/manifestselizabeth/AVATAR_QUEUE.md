# PRODUCTION AVATAR QUEUE

**Vídeo modelo:** `C:\Users\luigi\Downloads\manifestselizabeth.mp4`
**Produção:** `producao/manifestselizabeth/` · Ângulo 3 (Auraly) · aberta em 2026-09-11

Os avatares foram identificados pelas imagens enviadas junto do `.mp4`, na ordem em que vieram.
A fila é estado obrigatório e não depende do histórico da conversa.

| Ordem | Avatar | Âncora | Status |
|---:|---|---|---|
| 1 | **Robin Matthews** (72) | `producao/_ancoras/Robin.Matthewsus .jpeg` | DONE, 2026-09-11 |
| 2 | **Kris Walker** (24) | `producao/_ancoras/Kris.Walker_us .jpeg` | DONE, 2026-09-11 |
| 3 | **Casey Harrisson** (21) | `producao/_ancoras/casey.harrisson_us .jpeg` | DONE, 2026-09-12 |
| 4 | **Shelby Turner** (meados dos 20) | `producao/_ancoras/ShelbyTurner.us .jpeg` | ACTIVE, desde 2026-09-12 |
| 5 | **Mark Collins** (fim dos 30) | `producao/_ancoras/MARK COLLINS .jpeg` | PENDING |

**Ampliação de 2026-09-12.** O Luigi reenviou o mesmo `.mp4` com quatro âncoras: Casey, Shelby, Mark e
Kris, nesta ordem. A Kris já tinha pacote completo em `kris_walker_2026-09-11/`, então ela passa a
`DONE` e a fila segue pelas três inéditas, na ordem em que as âncoras chegaram.
**Roteiro, ganchos, K e V continuam fixos.** Nada disso reabre.

## Como a fila anda

1. Entregar o pacote completo do avatar `ACTIVE`.
2. Marcar ele como `DONE`.
3. Promover o próximo `PENDING` a `ACTIVE` automaticamente e entregar o pacote dele.
4. Só declarar `PRODUCTION COMPLETE` quando não houver nenhum `PENDING` nem `ACTIVE`.

## Elementos bloqueados para toda a produção

Aprovados uma única vez, valem para os cinco avatares:

- Roteiro de 7 takes, 153 palavras (`ROTEIRO.md`)
- Os ganchos visuais escolhidos pelo Luigi
- Ordem e associação de `K__` e `V__`
- Lógica de movimento e enquadramento (plano único, mesa no terço inferior, Setup A/B/C)
- Overlays do CapCut (`222 ✨`, caixa branca do hook, karaokê, seta vermelha)

## O que varia por avatar

- Identidade, idade, cabelo, pele, roupa, joia
- Cenário canônico e arranjo do kit de tarólogo da âncora dela
- Registro de voz no prompt de vídeo
- **Ajuste de congruência da copy** nos takes T1, T2 e T3, conforme as notas do `ROTEIRO.md`.
  T4 a T7 são idênticos, porque mecânica de funil não tem idade nem registro.

## Separação obrigatória em quadro (as cinco não podem parecer a mesma conta)

| | Idade | Marca do rosto | Cabelo | Onde senta | Cartas da mesa |
|---|---|---|---|---|---|
| **Robin Matthews** | 72 | manchas de idade, óculos de aro dourado | bob branco-prateado | mesa de **cozinha** | **cavalete**, clássico |
| **Kris Walker** | 24 | sinais escuros no rosto | **box braids com mechas mel** | mesa de quarto | **três em fila**, clássico |
| **Casey Harrisson** | 21 | **acne ativa** | liso escuro, **money piece loiro** | **chão, baú** | leque, **holográfico** |
| **Shelby Turner** | meados dos 20 | **tatuagem de lua no pulso**, marcas de acne | loiro-mel ondulado, sem franja | **chão, caixote** | empilhado, **holográfico** |
| **Mark Collins** | fim dos 30 | **sardas, pele de sol** | loiro ondulado, franja cortina | mesa de leitura | leque sob as mãos, clássico |

Cozinha e óculos são só da Robin. Box braids são só da Kris. Sentar no chão é só da Casey e da Shelby,
e elas separam por **baú contra caixote**, por idade e por cabelo. **Tatuagem é só da Shelby.**
Estante alta de livros é só da Shelby, pisca-pisca branco frio é só da Casey.

**A REF-CARTA que as cinco seguram é holográfica.** Na Robin, na Kris e na Mark isso diverge do baralho
clássico da mesa delas, e é de propósito: a leitura é que ela puxou uma carta especial.
**Nunca escrever que a carta saiu daquele baralho.**

## A regra do arquivo, que existe por causa do linter

O `checar_entrega.py` compara a fala de todo `PROMPTS_VIDEO_FLOW.md` da produção contra o `ROTEIRO.md`,
e o `ROTEIRO.md` é um só. Como a copy muda por congruência entre avatares, os dois não cabem vivos ao
mesmo tempo.

- **O `ROTEIRO.md` carrega sempre a fala do avatar `ACTIVE`.** Hoje o T2 está na versão da Shelby.
- **O `PROMPTS_IMAGEM.md` da raiz é sempre o do `ACTIVE`.** O anterior vira `PROMPTS_IMAGEM_<NOME>.md`.
- **Ao fechar um avatar, o `PROMPTS_VIDEO_FLOW.md` dele é renomeado para
  `PROMPTS_VIDEO_FLOW_<NOME>.md`** dentro da pasta dele. Nada se apaga, o arquivo continua no disco e
  o linter para de cobrar aquele pacote contra um roteiro que já virou de outra pessoa.

Estado atual:

| Avatar | Pasta | Arquivos |
|---|---|---|
| Robin Matthews, `DONE` | `robin_matthews_2026-09-11/` | `PROMPTS_IMAGEM.md`, `PROMPTS_VIDEO_FLOW_ROBIN_MATTHEWS.md`, os dois blocos do Flow |
| Kris Walker, `DONE` | `kris_walker_2026-09-11/` | `PROMPTS_IMAGEM.md`, `PROMPTS_VIDEO_FLOW_KRIS_WALKER.md`, os dois blocos do Flow |
| Casey Harrisson, `DONE` | `casey_harrisson_2026-09-12/` | `PROMPTS_IMAGEM.md`, `PROMPTS_VIDEO_FLOW_CASEY_HARRISSON.md`, os dois blocos do Flow |
| Shelby Turner, `ACTIVE` | `shelby_turner_2026-09-12/` | `PROMPTS_IMAGEM.md`, `PROMPTS_VIDEO_FLOW.md`, os dois blocos do Flow |
| Mark Collins, `PENDING` | ainda não aberta | |

**A diferença de copy entre elas é uma linha só, o fecho do T2:** `honey` na Robin,
`I am telling you` na Kris, `right this second` na Casey e `I can feel it` na Shelby.
Todo o resto é idêntico.
