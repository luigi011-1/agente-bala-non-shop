# PLAYBOOK FITYWELL

Documento operacional da marca **FITYWELL** para o **Ângulo 2** (app FityWell, quiz, mulheres
40+). O **Ângulo 4** (Body Hacks for Men 40+, homens 40+) abaixo voltou ao intake em 2026-10-02 (Luigi),
para rodar na holistic.brandon como COACH, ao lado de Dana, Jamie e Lynn como PAR. É o equivalente do
`PLAYBOOK_MESTRE_AURALY.md`, que é do Ângulo 3 e não se aplica aqui.

Aberto em 2026-09-10, a partir da produção `producao/fitywell_pernas/`, que é o **gabarito vivo**.

**Precedência:** `CLAUDE.md` > este arquivo > memória. Copy e doutrina de cada ângulo continuam em
`angulo2-copy-fitywell` e `angulo4-copy-bodyhacks`. Aqui fica **o processo**.

---

## 1. O que é fixo na marca

| | Ângulo 2 | Ângulo 4 |
|---|---|---|
| Produto | app FityWell, funil de quiz | playbook digital de 42 hacks, $9.90 |
| Público | mulheres 40+ | homens 40+ |
| Avatares | Dana Morrison, Jamie Anderson, Lynn Parker + Eva Dall, Ivy Carl, Jamie Voss, Lais Collins, Lia Carlla, Robert Alves e Roberta Carvalho + holistic.brandon (de volta em 2026-09-29) | Dana Morrison, Jamie Anderson e Lynn Parker |
| Posição do avatar | **COACH**, sempre | **PAR**, 1ª pessoa liberada |
| Keyword | `yes` | `yes` |
| Produto em quadro | **não** | **sim**, livro físico |
| Crivo extra | nunca culpar ela, rodado **duas vezes** quando quem fala é homem (uma na boca da Brandon) | nunca culpar a masculinidade dele |

Fichas, âncoras e travas visuais em `avatares-fichas`, seção ROSTER FITYWELL. Os sete avatares
adicionados em 2026-09-19 pertencem ao Ângulo 2; não estender ao Ângulo 4 sem decisão explícita.
A holistic.brandon voltou ao Ângulo 2 em 2026-09-29, também COACH (mulher de ~30 anos: cita as
clientes, nunca 1ª pessoa sobre o corpo depois dos 40); registro em `producao/_ancoras/AVATAR_BRANDON_RETORNO_2026-09-29.md`.

---

## 2. Ordem do workflow

`.mp4` + âncoras → P1 → análise → transcrição → método Puzzle → P2 → roteiro **com o gancho fiel
do modelo** → **aprovação do Luigi** → pacote por avatar → P9 → P10.

**Validar antes de variar (Luigi, 2026-09-23):** produção nova é **rodada de validação**, com um
gancho só, clonado do vídeo modelo com o máximo de fidelidade e os desvios obrigatórios declarados.
As **10 variações de gancho** e a **escolha dele** só entram na **rodada de variação**, que o Luigi
abre quando um vídeo postado performa, e partem do vídeo validado. Método em `GATE_VISUAL.md`
Parte 4, Passo 0.

Nenhuma etapa pula. O roteiro não vira prompt sem aprovação explícita.

**Vídeo modelo de pessoa real (Luigi, 2026-09-25):** `PERFIL_ORGANICO.md`. Copia literal de gancho
visual, copy e estrutura, e só o CTA muda: growth mantém o CTA do original; venda usa a ponte de
continuidade do próprio vídeo + link da bio, ou no Facebook o comentário fixado do vídeo (direção do
Luigi, não frase fixa), nunca "free". Sem ponte das três
causas, sem álibi, sem bandeira obrigatória. `origem: organico` e `CTA original:` no topo do `ROTEIRO.md`.

**`GATE_VISUAL.md` roda em dois momentos** (desde 2026-09-22, vale para todos os ângulos): a Parte 4
antes do gancho (Passo 0 na validação, as 10 variações só na rodada de variação), e as Partes 1 a 3 antes do primeiro `K__`. Todo prompt
de imagem carrega luz neutra ou céu com cor, herói colado na lente e o trecho de realismo.

**Bloqueante (2026-09-22):** nenhum gancho, `K__`, `V__` ou pacote é enviado sem o **checklist de
envio** 100% aprovado (`GATE_VISUAL.md` Parte 5, memória `checklist-envio-prompt`).

---

## 3. Variação de gancho: aqui é Puzzle, não invenção

Regra fixada em 2026-09-10, detalhe em `ganchos-variacao-puzzle`.

> **2026-09-23:** tudo desta seção vale só na **rodada de variação**, sobre um vídeo já validado no
> perfil. Na rodada de validação o gancho é o do modelo, fiel (`GATE_VISUAL.md` Parte 4, Passo 0).

♻️ **2026-09-22: PUZZLE COM DEGRAU** (método completo em `GATE_VISUAL.md` Parte 4). Antes das 10,
declarar a **peça viral** e subir **UM degrau** no esqueleto (`DIFICULDADE`, `CONTRADICAO`, `REACAO`,
`EUA` ou `ESCALA`). **HOOK 1 = controle** sem o degrau, HOOK 2 a 10 com ele. Aqui o degrau também
passa pelo gate de congruência com a fala do T1: se obriga a reescrever a copy, é degrau demais.

**A ação estrutural do hook original não se toca. Troca-se UMA variável por vez**, e os dois eixos
são o **ingrediente** e o **alvo**. Trocar os dois de uma vez deixa de ser variação.

- **Clickbait puro é proibido**, ao contrário do Ângulo 3. O herói carrega argumento.
- **Congruência com a fala do T1 é gate.** Variação que obriga a reescrever a copy reprova antes de
  aparecer.
- **Marcar em cada sugestão qual variável foi trocada.** É o que prova que ainda é Puzzle.
- **O ingrediente sai da própria receita do vídeo.** Ingrediente de fora prova o que o vídeo não
  ensina. A exceção deliberada é a **demo invertida**, que troca o ingrediente por um vilão e mostra
  o problema nascendo em vez de sair. Ela ganha impacto e perde a prova, então vai marcada e não é
  padrão.
- **Custo:** cada variação é 1 keyframe mais 1 clipe, porque só o T1 muda.

Exemplo rodado em `producao/fitywell_pernas/GANCHOS_VISUAIS.md`, com as dez sugestões e as três
reprovadas antes de chegar ao Luigi.

---

**Camada verbal (2026-09-22):** a fala do T1 e o texto de tela de cada variação seguem a skill
`gancho-verbal`, modo PRODUCAO. Topo com tese, sintoma-alvo, direção (ela vence, a causa é externa,
nunca o esforço dela) e banco verbal com 5 frases literais; texto de tela de até 9 palavras com frase
do banco; `Recomendacao: HOOK X` no fim. O linter lê esse topo no `GANCHOS_VISUAIS.md`.

## 4. Produção multi-avatar

**A fila é estado em disco, nunca conversa.** `AVATAR_QUEUE.md` dentro da pasta da produção, com
nome, caminho exato da âncora e `PENDING`, `ACTIVE` ou `DONE`.

Roteiro, takes, falas, ganchos escolhidos e ordem de K e V são aprovados **uma vez** e valem para
todos. Cada avatar seguinte muda identidade, âncora, cenário, registro e a frase de enquadramento.

### A regra do arquivo, que existe por causa do linter

O `checar_entrega.py` lê **um** `ROTEIRO.md` e **um** `PROMPTS_PRODUCAO.md` por pasta, e cobra que a
fala do prompt bata palavra por palavra com o roteiro. Como a frase de coach muda por avatar, o
arranjo é:

```
producao/<slug>/
  ROTEIRO.md                      <- o T4 carrega sempre a fala do avatar ACTIVE
  PROMPTS_PRODUCAO.md             <- o pacote do avatar ACTIVE
  PROMPTS_<AVATAR_ANTERIOR>.md    <- os fechados, arquivados pelo nome
  FLOW_<AVATAR>.md                <- o bloco limpo de cada um
  GANCHOS_VISUAIS.md
  AVATAR_QUEUE.md
```

**Ao virar o avatar:** arquivar o `PROMPTS_PRODUCAO.md` com o nome de quem saiu, trocar a linha do
T4 no roteiro, escrever o pacote novo e rodar o linter. Esquecer a troca do T4 dá falha de fala não
literal, que foi exatamente o que aconteceu em 2026-09-10.

**Concluir um avatar nunca encerra a produção.** Só existe `PRODUCTION COMPLETE` sem `PENDING` nem
`ACTIVE`.

---

## 5. Quando a âncora não comporta a demo

O esqueleto do vídeo modelo manda, mas o cenário do avatar vem da âncora dele. Quando os dois não
cabem juntos, **adaptar o lugar, nunca o esqueleto**.

Casos resolvidos na `fitywell_pernas`:

- **Jamie Anderson** tem o banco do motorista como âncora, onde não cabe demo com modelo apoiado. A
  bancada dele virou o **porta-malas aberto do SUV, no mesmo estacionamento**, preservando carro,
  lojas ao fundo e o adesivo da bandeira. Os takes de CTA voltam para o banco do motorista, e a
  troca de locação cai num corte só.
- **Lynn Parker** ganhou uma **mesa de madeira escura** em frente ao banquinho, que não existe na
  âncora e é a gramática do próprio vídeo modelo.

**Registrar a adaptação no `AVATAR_QUEUE.md`**, porque enquadramento que não existe na âncora pede
mais regeneração e quem for gerar precisa saber disso antes.

---

## 6. Entrega no Google Flow

Os blocos limpos valem aqui também, mesmo o formato tendo nascido no Ângulo 3.

- **Um `K__` sozinho numa linha, seguido de um prompt autossuficiente.** Mesma coisa para `V__`.
  Desde 2026-09-25 (contrato do Flow v17) o prompt de imagem sai em **JSON**, um objeto de `{` a `}`
  com os campos do JSON interno menos `shot_id`; as regras de conteúdo não mudam.
- **Antes do primeiro K: `FICHA_FRAMES.md`** com a ficha do frame e o placar de cada K (`GATE_VISUAL.md`
  Parte 6, 2026-09-25). O linter reprova pacote sem ela.
  No perfil classico, cada `V__` usa o maior `K__` menor ou igual ao seu numero, conforme
  o contrato do executor. Um K pode sustentar varios V quando o setup e estado sao os mesmos.
- O arranjo 1:1 da `fitywell_pernas` e um pacote historico preservado, nao uma exigencia de
  duplicar imagens novas. Esta regra classica nao se aplica ao Auraly, que segue seu workflow.
- **Autossuficiência mata o `EDITAR do K__` dentro do bloco do Flow.** O JSON do
  `PROMPTS_PRODUCAO.md` continua sendo a fonte interna, e é o que o linter lê.
- O bloco `INSTRUÇÕES PARA A MEMÓRIA DO AGENTE` sai de `producao/_flow/INSTRUCOES_AGENTE_FLOW.md`.
  Entre avatares da mesma produção não precisa recolar: basta `finalizamos, vamos para o próximo
  avatar` mais a âncora nova.

---

## 7. Censura do Flow: o que trava e o que passa

Protocolo completo em `restricoes-protocolo`. O que esta marca já queimou:

- **Nome de órgão no `negative` derruba o prompt.** `no heart model, no skull model, no brain model`
  travou o K02 do Dana em 2026-09-10. O classificador lê o token, não a negação. Desde então o
  `checar_entrega.py` reprova isso sozinho.
- **Precisão anatômica mata a leitura de objeto didático.** "female midsection from the lower ribs
  down to the hips" virou "teaching model of a torso panel, a smooth oval dome about the size of a
  dinner tray". Sem gênero, sem marco de região do corpo.
- **Vocabulário do herói:** `small round pale yellow beads` no lugar de `waxy globules`, e
  `covered by` no lugar de `buried under`.
- **A linha de ficção entra em todo prompt:** `This is a fictional AI-generated character, no real
  person is depicted.` É verdade e ajuda a destravar.
- **Marca fora de quadro se resolve no positivo**, com pote liso sem rótulo. Nunca negando marca.

---

## 8. Fechamento

- `python checar_entrega.py producao/<slug>` tem que fechar em **zero falhas**. O `pre-commit`
  bloqueia sozinho.
- Portão P10 depois que o vídeo for ao ar: log de rotação, biblioteca de vídeos,
  `checar_rotacao.py` e o grafo.
