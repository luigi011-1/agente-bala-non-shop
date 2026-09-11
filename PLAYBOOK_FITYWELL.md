# PLAYBOOK FITYWELL

Documento operacional da marca **FITYWELL**, que cobre o **Ângulo 2** (app FityWell, quiz, mulheres
40+) e o **Ângulo 4** (Body Hacks for Men 40+, homens 40+). É o equivalente do
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
| Avatares | Dana Morrison, Jamie Anderson, Lynn Parker | os mesmos três |
| Posição do avatar | **COACH**, sempre | **PAR**, 1ª pessoa liberada |
| Keyword | `yes` | `yes` |
| Produto em quadro | **não** | **sim**, livro físico |
| Crivo extra | nunca culpar ela, rodado **duas vezes** porque quem fala é homem | nunca culpar a masculinidade dele |

Fichas, âncoras e travas visuais dos três avatares em `avatares-fichas`, seção ROSTER FITYWELL.

---

## 2. Ordem do workflow

`.mp4` + âncoras → P1 → análise → transcrição → método Puzzle → P2 → roteiro → **aprovação do
Luigi** → **10 variações de gancho** → **escolha dele** → pacote por avatar → P9 → P10.

Nenhuma etapa pula. O roteiro não vira prompt sem aprovação explícita.

---

## 3. Variação de gancho: aqui é Puzzle, não invenção

Regra fixada em 2026-09-10, detalhe em `ganchos-variacao-puzzle`.

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
  `K01` casa com `V01` pelo número.
- **Uma imagem, um vídeo.** Dois takes no mesmo setup viram dois `K__` com prompts próprios, que é
  por que a `fitywell_pernas` tem doze de cada para oito takes mais quatro ganchos alternativos.
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
