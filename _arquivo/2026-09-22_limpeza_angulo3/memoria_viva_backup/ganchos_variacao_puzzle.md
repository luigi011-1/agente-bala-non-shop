---
name: ganchos-variacao-puzzle
description: "Como gerar variacoes de gancho visual sem misturar ofertas. Desde 2026-09-22 e PUZZLE COM DEGRAU (GATE_VISUAL.md Parte 4): peca viral intocavel, UM degrau no esqueleto, HOOK 1 controle. Desde 2026-09-20 os DOIS modos viraram UM: METODO PUZZLE aplicado ao hook do video modelo, 10 variacoes do mesmo esqueleto trocando uma variavel cada. O que ainda difere entre Auraly e FityWell sao as travas: clickbait puro e liberado no Auraly e proibido na FityWell, e la a congruencia com a fala do T1 e gate."
metadata:
  node_type: memory
  type: feedback
  modified: 2026-09-22T22:33:18.253Z
  originSessionId: 8ffd9200-71b9-4a43-904b-f69dc4572a00
---

# Variacao de gancho visual: UM metodo, travas diferentes por marca

Aberto em 2026-09-10, correcao do Luigi. **Ele revogou a minha regra de que a etapa de ganchos era
exclusiva do Angulo 3.**

**Why:** eu tinha concluido que, como o heroi do hook da FityWell carrega argumento, o gancho nao
podia ser trocado. A premissa estava certa e a conclusao errada. O heroi carregar argumento nao
impede a variacao, **ele so define o METODO da variacao**: em vez de inventar um gancho novo, aplica-se
o Puzzle ao proprio hook. Boas ideias saem dai, e a etapa e barata porque a copy nao muda.

**How to apply:**

## 2026-09-22: a CAMADA VERBAL tem skill própria

O Puzzle decide o que se VÊ. O que se LÊ e OUVE (fala do T1, texto de tela) segue a skill de projeto
`gancho-verbal` (`.claude/skills/gancho-verbal/SKILL.md`), adaptada da `hook-writer`, modo PRODUCAO:
topo com tese, sintoma-alvo, direção, padrão do modelo e banco verbal; texto de tela até 9 palavras
com frase do banco; recomendação no fim. **A paleta de 10 categorias da skill NÃO vale nas 10 do
Puzzle** (seria segunda variável): só no modo livre, pedido avulso. Ver [[checklist-envio-prompt]] A10-A14.

## ♻️ 2026-09-22: PUZZLE COM DEGRAU (Luigi mandou fundir com o step up)

O Luigi pediu para mesclar o Puzzle com o *step up* do curso Lib Korella, mantendo o mais forte de
cada. **Metodo canonico em `GATE_VISUAL.md` Parte 4**, que e onde se edita daqui pra frente.

**Why:** o curso mediu que refazer o viral igual rende cada vez menos (7k, 1k, 700, 500), porque o
publico interessado ja viu, e que acrescentar UMA camada ao viral mais recente multiplica (barriga
2k contra nao-entra-no-carro 180k). O Puzzle puro troca variavel mas nunca sobe o nivel da base.
O step up puro acumula camadas e perde a leitura de qual mudanca venceu.

**How to apply:** peca viral intocavel + UM degrau no esqueleto (`DIFICULDADE`, `CONTRADICAO`,
`REACAO`, `EUA`, `ESCALA`) + as 10 do Puzzle, com **HOOK 1 = controle sem degrau**. O vencedor vira
a base da proxima rodada, que sobe um degrau de outra categoria. Travas por marca abaixo seguem
valendo. O validador (`auraly_validacao.py`) exige `Peca viral:`, `Degrau:` e um CONTROLE.

**Vale nos TRES angulos, inclusive Korella (Angulo 1)**, por ordem do Luigi em 2026-09-22. A Korella
usa as travas da FityWell (congruencia como gate, clickbait proibido, eixos ingrediente e alvo), e o
frasco nunca e a variavel trocada nem o degrau.

## O metodo e UM SO desde 2026-09-20 (Luigi)

♻️ **Revoga os "dois modos".** E revoga o portfolio `4 + 3 + 3` em tres familias, que durou menos
de um dia. **O Angulo 3 passa a fazer exatamente o que a FityWell faz:** extrair a acao estrutural
do hook do VIDEO MODELO, manter fidelidade quase total e trocar UMA variavel por sugestao.

O que a amostra de 53 virais da Maya Astor provou nao foi que se deve montar tres familias por
lote. Foi que **repetir o proprio esqueleto trocando uma variavel e o que faz a conta escalar**,
e isso ja tinha nome: Puzzle. 81% da amostra sao oito esqueletos repetidos.

| | Angulo 3 (Auraly) | FityWell (angulos 2 e 4) |
|---|---|---|
| Origem da ideia | **Puzzle aplicado ao hook do video modelo** | **Puzzle aplicado ao heroi do hook** |
| O que se preserva | **a acao estrutural do hook do modelo** | **a acao estrutural do hook do modelo** |
| O que muda | **UMA variavel por hook** | **UMA variavel por vez** |
| Eixos de troca | objeto, substancia, local, cor, resultado, marcador, alvo | **ingrediente e alvo** |
| Distribuicao | 1 controle + 9 com degrau, MESMO esqueleto | 1 controle + 9 com degrau, MESMO esqueleto |
| Papel do banco de ganchos | **controle de repeticao**, nunca fonte da ideia | nao se aplica |
| Clickbait puro | **liberado**, vai no fim e marcado | **proibido, quebra o argumento** |
| Congruencia | trava so na **fala**, nunca no objeto do gancho | **gate, reprova antes de mostrar** |
| Fonte | [[metodo-puzzle]] + [[angulo3-swipe-padroes]] | [[metodo-puzzle]] puro |

**Por que as travas diferem:** na FityWell o heroi do hook **carrega argumento**, entao um objeto
incongruente quebra a venda. No Auraly o heroi do gancho nao argumenta nada: ele so para o scroll,
e a alma gemea entra na fala. Por isso clickbait puro converte la e nao aqui.

**Declarar sempre:** a acao estrutural uma vez no topo, e a variavel trocada em cada sugestao.
E o que prova que ainda e Puzzle e nao invencao disfarcada.
Gabarito de formato rodado: `producao/fitywell_pernas/GANCHOS_VISUAIS.md`.
Criterio de qual acao merece virar gancho no Auraly: [[constrangimento-produtivo-auraly]].
Como escrever os cortes do gancho: [[gancho-sequencia-montada-auraly]].

## O exemplo canonico dado pelo Luigi

**Heroi do hook original:** um homem velho joga bicarbonato em cima de um modelo anatomico de intestino.

**A acao estrutural**, que nao se toca: `o avatar joga ALGO em cima de UM MODELO ANATOMICO`.

**As variacoes trocam uma variavel de cada vez:**

1. o avatar joga canela em cima da **propria barriga** (trocou o ALVO)
2. o avatar joga bicarbonato em cima do modelo de **outro orgao**, se houver congruencia (trocou o ALVO)
3. o avatar joga **canela** em cima do modelo de intestino (trocou o INGREDIENTE)
4. o avatar joga **coca-cola** em cima do modelo de intestino (trocou o INGREDIENTE, e o estado
   fisico junto, de po para liquido)

**Os dois eixos sao INGREDIENTE e ALVO.** Trocar os dois de uma vez deixa de ser variacao e vira
gancho novo, o que sai desta etapa.

## As travas

- **Congruencia com a fala do T1 e gate.** Variacao que obriga a reescrever a copy foi longe demais.
  Reprovar em silencio, antes de mostrar.
- **Marcar em cada sugestao QUAL variavel foi trocada.** E o que prova que ainda e Puzzle.
- **Custo:** cada variacao custa 1 keyframe mais 1 clipe, porque so o T1 muda. Igual ao Angulo 3.
- **Risco de plataforma entra na nota.** Modelo anatomico de orgao genital em quadro e prop sensivel
  para o classificador de imagem, e no Angulo 4 o nome clinico do orgao ja e proibido na fala e na
  legenda ([[angulo4-copy-bodyhacks]] secao 8). O prop pode existir, mas entra como **prop ambiguo**,
  frame limpo, e a associacao se faz por fala e legenda. Ver [[compliance-riscos]] e
  [[restricoes-protocolo]].

Relacionado: [[metodo-puzzle]], [[erros-recorrentes]], [[checklist-composicao-visual]],
[[angulo2-copy-fitywell]], [[angulo4-copy-bodyhacks]], [[avatares-fichas]]
