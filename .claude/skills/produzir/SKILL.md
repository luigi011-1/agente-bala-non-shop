---
name: produzir
description: Executa a producao completa de um video modelado, na ordem travada, do roteiro ate os prompts. Escreve os DOIS arquivos em producao/<avatar>_<slug>/ (ROTEIRO.md e PROMPTS_PRODUCAO.md) com todas as secoes obrigatorias e cola tudo na conversa. No Angulo 3 (Auraly) o processo vive em WORKFLOW_AURALY.md e no CHECKPOINT da producao, sem DM.md. Use quando o usuario mandar /produzir, ou quando um roteiro for aprovado e for hora de gerar o pacote de prompts. Existe porque o formato de entrega se degradou quando dependia de eu lembrar dele.
---

# /produzir — pacote de producao completo

Esta skill existe por um motivo especifico: em 2026-08-21 o formato de entrega se degradou porque eu passei a recompor a entrega de memoria em vez de seguir o gabarito. **Aqui a ordem e travada. Nao improvisar, nao pular secao, nao reinventar formato.**

---

## PASSO 0 — CARREGAR A MEMORIA INTEIRA, de uma vez, antes de tudo

**Executar esta skill NAO substitui ler.** A skill e a ordem, os documentos sao o conteudo.

Ate 2026-08-26 este passo era uma lista de nove memorias pra abrir uma a uma (o PORTAO P5).
Isso falhava por um motivo simples: **eu decidia o que era relevante ANTES de ler**, e errava a
decisao. Regra que eu nao achava relevante era regra que eu nao abria.

**Regra vigente: carregar TUDO. Um comando, uma chamada, antes de qualquer outra coisa.**

```bash
cd ~/.claude/projects/-Users-macbookairm2-Desktop-agente-bala-non-shop-main/memory && for f in *.md; do echo "########## $f ##########"; cat "$f"; done
```

Sao 64 arquivos, ~490 KB, ~150k tokens (contagem de 2026-09-22). Custa segundos e cerca de 1% do orcamento da sessao.
**Nao existe desculpa de custo pra pular.** Nao ler custa retrabalho, que e mais caro.

**Nao filtrar, nao ler por amostragem, nao abrir so os do angulo.** O ponto do passo e
justamente eliminar o julgamento previo de relevancia.

Depois de rodar, os PORTOES P1 a P9 continuam valendo, mas **como roteiro de APLICACAO**,
nao de leitura: eles dizem em que momento cada regra e aplicada, e o conteudo ja esta carregado.

**Ainda ler a parte, porque nao esta na memoria:**

```
[ ] producao/fitywell_pernas/ROTEIRO.md        (o gabarito vivo desde 2026-09-10, esta no repo)
[ ] producao/fitywell_pernas/PROMPTS_PRODUCAO.md
[ ] PLAYBOOK_FITYWELL.md                         (se for FitWell)
[ ] GATE_VISUAL.md                               (Partes 1 a 5, todos os angulos)
[ ] producao/_flow/INSTRUCOES_AGENTE_FLOW.md    (perfil CLASSICO, colado no PASSO 5)
[ ] PLAYBOOK_COMPLETO/11_insights_otimizacao.md secao 3   (antes dos prompts de VIDEO, P6)
```

**Depois da entrega, o PORTAO P10:** escrever no log de rotacao e na biblioteca de videos.

> ⚠️ **Sessao longa:** se o contexto for resumido no meio da producao, o que foi lido aqui pode
> ter sido comprimido. O `checar_entrega.py` do PASSO 7 nao depende disso, porque le do disco.
> Se bater duvida sobre uma regra depois de muitas horas, reabrir o arquivo dela, nao chutar.

---

## PASSO 0-B — O gabarito, o que copiar e o que NAO copiar

Ler os dois arquivos, sempre, mesmo achando que lembra:

- `producao/fitywell_pernas/ROTEIRO.md`
- `producao/fitywell_pernas/PROMPTS_PRODUCAO.md`

O `producao/brandon_angle2/` virou historico junto com a Brandon e nao e mais gabarito.

Copiar dali o **FORMATO**, nunca o conteudo. Duas praticas antigas foram **revogadas** e nao podem ser copiadas de nenhum pacote:
1. **Frase filler** (proibida desde 18/08). Take curto se resolve requebrando o roteiro em fim de frase.
2. **Um keyframe por take** (desde 20/08 e um keyframe por SETUP/BLOCO).

## PASSO 1 — Checar os pre-requisitos

Nao seguir sem os quatro:
- [ ] `/watch` rodado e decomposicao beat a beat feita
- [ ] Heroi do hook identificado sem ambiguidade (rodar o micro-protocolo de 5 perguntas de `erros-recorrentes`)
- [ ] Angulo definido (1 Korella / 2 FityWell / **3 Auraly**, que sai desta skill e vai para `WORKFLOW_AURALY.md`) e avatar confirmado. Angulo ou avatar ja definidos nao se perguntam de novo
- [ ] Roteiro aprovado pelo Luigi

Faltando qualquer um, parar e pedir. Roteiro nao aprovado torna todo prompt retrabalho garantido.


## PASSO 1-B — QUAL AVATAR: o anexo decide

**`.mp4` + imagem de avatar na mesma mensagem = produzir PARA AQUELE AVATAR.** Nao perguntar.
Os avatares sao exatamente os que o Luigi anexou nesta producao: nunca inventar, nunca puxar de
producao antiga. Faltou avatar, perguntar.

**Fila persistente (MULTI-AVATAR PRODUCTION RULE, 2026-09-09):** com N ancoras, registrar logo todos
os avatares num arquivo de fila dentro da pasta da producao, com nome, caminho exato da ancora e
estado `PENDING`, `ACTIVE` ou `DONE`. Roteiro, ganchos escolhidos e ordem de K/V sao aprovados uma
vez so. Fechar um avatar nunca fecha a producao: marcar `DONE`, avancar o proximo `PENDING` e
entregar o pacote dele. `PRODUCTION COMPLETE` so sem `PENDING` nem `ACTIVE`.

**Rodar o mesmo modelo no proximo avatar depois**, com:
- **AJUSTES DE COPY para congruencia**, nunca copia palavra por palavra. Idade, genero e registro
  mudam o que soa crivel na boca de cada avatar. Abrir `congruencia-matriz` antes de portar.
- Ajustes de identidade, cenario, registro de voz e `rt_ad` nos prompts.

> Regra corrigida pelo Luigi em 2026-08-25. Eu tinha gravado que a copy ficava identica entre
> avatares. **A regra vigente e ajustar.**

## PASSO 1-A — SE FOR ANGULO 3 (Auraly), sair desta skill

**Processo, estado, configuracao e formato de resposta do Angulo 3 vivem somente em
`WORKFLOW_AURALY.md` e no `CHECKPOINT.md` da producao** (`CLAUDE.md`, roteamento de 2026-09-14).
Ler o workflow, abrir o checkpoint e executar so a `Next action`, respeitando os estados `WAITING_*`.
Nao reabrir decisao aprovada, nao juntar K/V fora do `MAPA K/V`, nao pular espera.

Esta skill cobre o Angulo 3 so no que e comum aos tres angulos: o PASSO 3-B (ganchos) e o CHECKLIST
DE ENVIO. O resto dela (dois arquivos, `PROMPTS_PRODUCAO.md`, perfil CLASSICO do Flow) nao vale ali.

Contexto criativo que continua valendo, para nao contradizer o workflow:
- Pasta `producao/<slug>/`, sem prefixo de avatar, com o marcador `pipeline: auraly` no `ROTEIRO.md`.
- **Keyword `222`** no lugar de `yes`.
- **Nao mostra produto.** O objeto de desejo do CTA e o **rosto da alma gemea**, que **espera no
  STORIES** e nunca e revelado no video. Ordem do CTA: `222` -> save -> follow -> Stories (P7).
  O video nunca diz quiz, teste, app, plano nem preco.
- **Sem DM nenhuma** desde 2026-09-22 (sem automacao). Sem `DM.md`. O CTA de comentario `222` continua igual.
- **Registro divino, nunca oculto.** Sem feitico, pacto, escudo, circulo de protecao.
- **Avatares:** so os que o Luigi anexou; fichas em `avatares-fichas`.

**Duracao, numero de takes e gramatica visual saem do VIDEO MODELO**, como sempre.

## PASSO 2 — Abrir as memorias de copy do fechamento

Antes de escrever o bloco de venda, abrir:
- `banco-rotas-argumentativas` → **conferir o log de rotacao.** Qual rota o ultimo video desta conta usou? Nao repetir a rota nem as frases. Frase que ja foi ao ar esta queimada.
- `banco-obstaculos` → empilhar um obstaculo de cada rota de fuga
- `feedback-ponte-argumentada` → a ponte e cadeia de 3 a 4 elos, nunca afirmacao
- `angulo2-copy-fitywell` (se for Angulo 2)

- `angulo3-copy-auraly` + `angulo3-swipe-padroes` (se for Angulo 3). No Angulo 3 estas memorias
  atendem o beat de fechamento onde o modelo tiver esse beat, e o CTA de Stories segue o P7.

## PASSO 3 — Criar a pasta e escrever `ROTEIRO.md`

`producao/<avatar>_<slug>/ROTEIRO.md`, nesta ordem, sem pular secao:

1. **Cabecalho**: video modelo, avatar, variavel trocada, funil, enquadramento do avatar
2. **Tabela de esqueleto preservado**: `# | Beat | Original | Adaptado`
3. **Setups de cena**: Setup A, B, C... cada um listando os takes que atende
4. **Roteiro cena a cena**: `### T1 · BEAT · TALKING|B-ROLL · Setup A`
5. **Roteiro so-fala** (ingles corrido, pro TTS)
6. **Notas de producao**: duracao, heroi do hook, compliance, o que cortar se ficar longo

**Contar as palavras de cada take AGORA, nao depois.** 8s = 13 a 29 palavras. Passou de 29, quebrar em fim de frase.
**O take segue a CENA do modelo (Luigi, 2026-09-23):** nunca juntar duas cenas num take e nunca cortar
frase no meio para caber na faixa. Cena curta do modelo = take curto marcado `CENA CURTA` no cabecalho
(o piso de 13 nao vale; o teto de 29 vale sempre).

## PASSO 3-B — TODOS OS ANGULOS: sugestoes de GANCHO VISUAL antes dos prompts

> **Vigente desde 2026-09-22, vale nos TRES angulos (Korella, FitWell e Auraly):** o metodo e o
> Puzzle com degrau (`GATE_VISUAL.md` Parte 4) e a camada verbal (fala do T1, texto de tela) segue a
> skill `gancho-verbal`, modo PRODUCAO. Este passo so espelha as regras; em conflito, `CLAUDE.md`
> P3.5 e P4 e a secao "PASSO EXTRA (TODOS OS ANGULOS desde 2026-09-22)" vencem.

### Primeiro: qual e a rodada? (Luigi, 2026-09-23, `GATE_VISUAL.md` Parte 4 Passo 0)

- **RODADA DE VALIDACAO (padrao de toda producao nova):** UM gancho so, o do video modelo, clonado
  com o maximo de fidelidade de CONTEUDO (acao, heroi, objeto, local, ordem de planos, cortes, timing, abertura
  muda ou falada, texto de tela traduzido). So muda o obrigatorio (identidade, travas do angulo,
  moderacao) e cada desvio vai declarado. **O acabamento nao e fiel ao modelo, e do nosso gate:**
  `GATE_VISUAL.md` Partes 1 a 3 rodam inteiras (heroi colado na lente, zero tom amarelado, luz
  neutra ou ceu nublado, 2 a 3 ancoras de fundo, sem blur, trecho de realismo). Vai descrito no T1 e no `GANCHOS_VISUAIS.md`
  (`Rodada: VALIDACAO`, `HOOK 1 - FIEL`), entregue **junto com o roteiro** e aprovado com ele.
  **Sem 10 variacoes, sem degrau, sem escolha.** Aprovado o roteiro, direto para os prompts. O resto
  deste passo NAO roda.
- **RODADA DE VARIACAO:** so quando o Luigi disser que um video postado performou. Nunca por
  iniciativa propria. A base e o video validado como foi postado (`Rodada: VARIACAO`,
  `Base validada:`), e ai sim roda tudo abaixo.

**Ordem travada na variacao: roteiro validado -> sugestoes de gancho visual -> escolha do Luigi -> so entao prompts.**
Nao entregar prompt nenhum antes de mandar as 10 variacoes e o Luigi escolher (quantidade livre).

A **copy fica identica em todas**, palavra por palavra. So mudam os primeiros segundos: o heroi e a
acao do hook. Cada variacao custa **1 keyframe + 1 clipe, so o T1**.

*Por que existe:* um roteiro validado **no nosso perfil** vira N videos trocando so o hook, e variar UMA coisa por vez e
o que deixa ler qual gancho venceu.

### Metodo: Puzzle com degrau (`GATE_VISUAL.md` Parte 4, ler o arquivo, nao este resumo)

1. **O esqueleto sai do HOOK DO VIDEO MODELO**, nunca de invencao livre nem de familia escolhida no
   banco. Escrever a **acao estrutural** e a **peca viral**. As duas sao intocaveis.
2. **Um degrau no esqueleto**, um so por producao: `DIFICULDADE`, `CONTRADICAO`, `REACAO`, `EUA` ou
   `ESCALA`. Nao toca a peca viral, nunca obriga a reescrever a fala e cabe em 1 K + 1 V. Declarar
   no topo: `Degrau: CATEGORIA - o que foi acrescentado`.
3. **10 variacoes, todas do MESMO esqueleto:**
   - **HOOK 1 = CONTROLE:** o esqueleto original, **sem o degrau**, com uma variavel trocada.
   - **HOOK 2 a 10:** o esqueleto **com o degrau**, **uma variavel trocada em cada**.
   - Trocar duas variaveis ja e gancho novo e sai da etapa.
   - **Marcar em cada variacao qual variavel foi trocada.** E o que prova que ainda e Puzzle.
4. **Checklist de cada variacao** (Parte 4, Passo 4): coerencia visual e verbal sem redundancia, um
   ponto focal colado na lente, acao ja comecada no primeiro frame, emocao crua, sinal de EUA quando
   couber. Mostrar, segurar ou apontar para o objeto reprova.
5. **O vencedor vira a base da proxima rodada**, que sobe outro degrau, de outra categoria.

### Travas por marca

| | **Korella (1) e FitWell (2)** | **Auraly (3)** |
|---|---|---|
| Eixos de troca | **ingrediente e alvo** | objeto, substancia, local, cor, resultado, marcador, alvo |
| Congruencia | **gate com a fala do T1**, variacao que obriga reescrever a copy reprova | trava so na **fala**, nunca no objeto |
| Clickbait puro | **proibido**, quebra o argumento | liberado, no fim e marcado como tal |
| Ordem | por congruencia | por congruencia, clickbait no fim |

- **Korella:** o produto aparece, entao o frasco **nunca** e a variavel trocada nem o degrau. Fica
  fixo em quadro onde o roteiro pede.
- **Auraly:** o degrau aumenta o **constrangimento**, nunca a admiracao; `REACAO` e alguem flagrando
  o ritual. As tres travas do angulo seguem: **rosto nunca revelado**, **carta na mao depois do
  gancho**, **registro divino**. Formato da entrega no `OUTPUT CONTRACT` de `WORKFLOW_AURALY.md`.

### O banco NAO e a fonte da ideia

`producao/_swipe_auraly/BANCO_GANCHOS_VISUAIS.md` serve **so para controle de repeticao** (nao repetir
literalmente objeto, texto de tela ou execucao ja publicados) e padrao de qualidade. Os 13 mecanismos
antigos ficam la como secao HISTORICA, para checar repeticao. A fonte e sempre o video modelo.

### Camada verbal: skill `gancho-verbal`, modo PRODUCAO

O Puzzle decide o que se VE, a skill decide o que se LE e OUVE.
- **No topo, antes das 10:** `Tese`, `Sintoma-alvo`, `Direcao`, `Padrao do modelo` e `Banco verbal`
  com no minimo 5 frases literais do roteiro aprovado.
- **Em cada variacao:** campo `Texto de tela` com **no maximo 9 palavras** e uma frase do banco. A
  frase muda so porque a variavel visual mudou; trocar a estrutura da frase junto e segunda variavel.
  No Auraly sao duas linhas (desejo concreto + selecao ou prazo), cada uma dentro do teto, e sempre
  camada de CapCut, nunca dentro do `K__` (o `no captions` do negative continua).
- Rodar os testes da skill (troca, leitura errada, sincronia, print, direcao).
- **Fechar com `Recomendacao: HOOK X`** e o porque. O Luigi escolhe.

### Auraly: T1 MUDO com cortes internos ao `V__` (`CLAUDE.md` P4)

- **Continua `1 K + 1 V` no gancho.** O `K__` e o primeiro plano da sequencia; o resto nasce dentro
  do `V__`, gerado pelo Veo no mesmo take. Nunca fatiar o T1 em varios K/V.
- `o que acontece no video` carrega, nesta ordem: **acao ja comecada** -> **corte para MACRO das maos
  no instante do payoff** -> **corte de volta para o plano de corpo**. Excecao ao "menos e mais", so
  no T1.
- O bloco `camera` declara que os **cortes sao internos** ao clipe.
- **O T1 nasce MUDO:** `T1 · B-ROLL · MUDO` no `ROTEIRO.md` e o prompt de video abre com
  `(sem fala no take: ...)`. A fala do T1 vira voz-over no T2 ou e cortada.
- **Split vertical liberado so no T1** (rosto em cima, maos e ritual embaixo). **Do T2 em diante o
  plano unico segue obrigatorio**: camera na altura do peito do outro lado da mesa, carta na mao, e
  os takes se reaproveitam entre variacoes.

Nos Angulos 1 e 2 o T1 continua take normal de 8s, 1 K + 1 V.

**Antes de enviar as 10:** rodar o CHECKLIST DE ENVIO (memoria `checklist-envio-prompt`,
`GATE_VISUAL.md` Parte 5) e levar `Checklist de envio: X/X aprovados` fora dos blocos copiaveis.

## PASSO 3.5 — GATE DE COMPOSIÇÃO VISUAL, antes de escrever qualquer prompt

**Fonte unica desde 2026-09-22: `GATE_VISUAL.md` Partes 1 a 3, em todos os angulos.** Os dois
checklists abaixo sao o resumo; em conflito, o `GATE_VISUAL.md` vence.

**Rodar os 10 itens de `checklist-composicao-visual` ANTES de escrever o primeiro JSON, nunca depois.**
Composicao nao se conserta apos a geracao, se conserta no prompt.

```
HEROI
[ ] 1. O heroi esta no LOWER FOREGROUND, mais perto da lente que o rosto?
[ ] 2. Nada compete com ele. Elemento que nao serve a fala do take sai de quadro.
[ ] 3. Volume e cobertura do heroi explicitados (montanha, nao camada fina).

DISTANCIA
[ ] 4. "Da pra estar mais perto?" Se da, esta longe demais. Vale em TODO take.
[ ] 5. Pessoas: peito pra cima ou ombros pra cima. Rosto ocupa boa parte do quadro.
[ ] 6. O take mais fechado do video inteiro e o do CTA.

FUNDO
[ ] 7. Cenario RECONHECIVEL, nunca inventariado. Duas ou tres ancoras visuais bastam.
[ ] 8. Reduzir fundo com ENQUADRAMENTO, nunca com blur (o negative proibe blur).
[ ] 9. Menos elementos = mais qualidade de geracao e mais realismo.

2a PESSOA
[ ] 10. Entra CORTADA pelo quadro, nunca de corpo inteiro.
```

**Onde isso mais falha:** inventario de fundo (listar seis objetos quando bastavam dois) e
two-shot largo demais no hook quando ha 2a pessoa. Nos dois casos a correcao e fechar o plano
e descrever menos.

Este bloco entra no `PROMPTS_PRODUCAO.md` como secao propria **antes dos prompts de imagem**,
e os itens visuais tambem entram nos gates de qualidade do fim.

### E JUNTO COM ELE, O GATE DE REALISMO (memoria `realismo-anti-cara-de-ia`)

```
[ ] 1. Heroi ISOLADO. Duas ou tres ancoras de fundo no maximo, nunca inventario de seis
[ ] 2. Camera puxada pra perto. No hook o heroi enche os dois tercos de baixo
[ ] 3. Luz NEUTRA de dia nublado, nunca quente. Golden hour BANIDA desde 2026-09-22
[ ] 4. Negative carrega: no warm orange color cast, no yellow tint, no golden glow
[ ] 5. Fundo descrito com especificidade, e nunca borrado
[ ] 6. Prop que costuma teimar tem REF-PROP gerado isolado antes
[ ] 7. Bloco de realismo padrao colado por inteiro em todo prompt
[ ] 8. Bandeira dos EUA discreta, visivel e em foco no campo scene (menos em REF de prop isolado)
```

**Regra-mae:** a IA copia bem o que voce mostra e inventa mal o que voce so descreve.
**Realismo e volume de regeneracao, nao prompt magico.** Nano Banana 2 supera o ChatGPT em avatar.

## PASSO 4 — Escrever `PROMPTS_PRODUCAO.md`

Mesma pasta, nesta ordem, sem pular secao:

1. **Cabecalho**: video modelo, caminho da ancora do avatar, funil
2. **Indice de geracao**: tabela `Take | Keyframe | Acao de geracao`
3. **Trava de identidade e continuidade**: bloco unico com rosto, cabelo, tatuagens, roupa, cruz, cenario, luz. Escrito UMA vez e referenciado, nunca repetido dentro de cada JSON
4. **Trava do prop heroi** (se houver)
5. **Trava da 2a pessoa (REF-A)**, gerar e aprovar ANTES de tudo
6. **Prompts de imagem** `K01`, `K02`... em JSON
7. **Bloco global de video** (colar em todo prompt)
8. **Prompts de video** `V01 · T1 · usa K01`, texto simples
9. **Mapa de ancoras**: `Keyframe | Referencias a anexar | Modelo`
10. **Montagem no CapCut**
11. **Gates de qualidade**: checklist numerado


## PASSO 4-A — ANGULO 3: sem `DM.md` (revogado em 2026-09-04)

O terceiro arquivo `DM.md` saiu da entrega Auraly quando o destino virou o STORIES, e em 2026-09-22 a
automacao de DM parou de vez. O mestre antigo esta em `_arquivo/2026-09-22_limpeza_angulo3/dm_auraly/`. Nao escrever `DM.md` em producao nova.

## PASSO 5 — Colar tudo na conversa

Arquivo nao substitui chat. **Ordem, em CADA pacote de avatar:**

1. **`INSTRUCOES PARA A MEMORIA DO AGENTE — GOOGLE FLOW AI`**, colado INTEIRO, de
   `producao/_flow/INSTRUCOES_AGENTE_FLOW.md` (perfil CLASSICO nos Angulos 1 e 2). Nunca "igual ao
   anterior": ele vai para uma memoria de agente nova a cada rodada.
2. **Bloco de imagem limpo para maquina:** `K__` sozinho na linha, seguido so do prompt completo e
   autossuficiente. Sem titulo, descricao, `T__`, metadata, settings, INITIAL FRAME, `usa K__`,
   caminho ou nota dentro do bloco.
3. **Bloco de video limpo para maquina:** `V__` sozinho na linha, mesmas travas. Nunca "same as
   previous" nem "edit K__".
4. **Tabela de transcricao por take** (`Take | English | Português`), fora dos blocos, com as falas
   aprovadas sem parafrase.

Tabela humana de leitura (`K01 = ...`) e a linha curta dizendo o que aparece na cena e quais imagens
anexar ficam **fora** dos blocos copiaveis.

Titulo do prompt de imagem carrega as referencias em CAIXA ALTA:
`## K04 · T20 a T22 · GERAR DO ZERO · ANCORA MELODY + PRODUCT.PNG`

## PASSO 6 — Roteiro final por ultimo, e sempre em INGLES no fim

Depois de TODOS os prompts, fechar com:

1. **Tabela unica bilingue** (`# | Beat | K | English | Portugues`), marcada como a versao que substitui tudo que veio antes.
2. **ROTEIRO FINAL EM INGLES, obrigatorio**, em duas formas:
   - **numerado por take** (`T1`, `T2`...), que e o que amarra com os prompts `V__`
   - **corrido, so-fala**, pronto pra colar no gerador de voz

O ingles e a fonte de verdade que vai pro TTS e pros prompts de video. A tabela bilingue serve pra
ele revisar a copy; na hora de produzir ele precisa do ingles limpo, sem coluna de portugues no meio.
Pedido dele em 2026-08-21.

---

## Regras que quebram a entrega

**Nomenclatura, nunca colapsar:** `T` take do roteiro · `K` keyframe · `V` clipe · `REF` referencia auxiliar. Varios T podem usar o mesmo K. Cada T tem seu V.

**Imagem = JSON. Video = texto simples.** Nunca misturar. Prompt de video nao descreve enquadramento, cor nem composicao, isso ja esta na imagem. Os cinco blocos do video:

```
o avatar (mulher) fala em ingles com sotaque americano de [avatar], voz autentica, dinamica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

o avatar diz todas as palavras corretamente, nao pula nenhuma palavra, e diz a ultima palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o video.

o que acontece no video: [acao ENXUTA, so o que acontece]

camera: [fixa / leve push-in / leve handheld]

som ambiente: [ambiente], sem musica
```

B-ROLL: trocar a primeira linha por `(sem fala no take: a fala N entra como voz-over na edicao)`.

**GERAR DO ZERO** so no primeiro keyframe de cada setup. Todo o resto e **EDITAR do K__**, que trava rosto, fundo e luz. Estagios sempre a partir do original, nunca em cascata.

**Reveal continuo dentro de um take = UMA imagem** do estado inicial. O teste: o original corta entre os dois estados? Nao corta, uma imagem. Corta, imagens separadas.

**Enquadramento sempre mais perto** que o original. Se da pra estar mais perto, esta longe demais.

**Negative:** so termos neutros. Nunca nome de orgao, gore, logo ou brand name. Nunca `"no text"` seco, que apaga a sinalizacao canonica do cenario; usar `no captions, no subtitles, no words overlaid on the image`.

**Se travar restricao:** o Luigi ja tentou varias vezes antes de reportar. Nunca sugerir retry. Ir direto pro protocolo de `restricoes-protocolo`: enxugar a acao, neutralizar o alvo, separar em takes diferentes.

**Keyword por angulo:** `yes` nos Angulos 1 e 2, `222` no Angulo 3. Nunca a palavra do video original. Zero travessao. Angulos 2 e 3 nao mostram produto, Angulo 1 mostra sempre.

---

## PASSO 7 — RODAR O LINTER, antes de colar qualquer coisa na conversa

**Obrigatorio. Nao e opcional e nao substitui os gates a olho, roda junto com eles.**

```bash
python checar_entrega.py producao/<avatar>_<slug>
```

Ele le os arquivos DO DISCO e checa o que da pra checar por maquina: travessao na copy,
keyword do angulo, 13 a 29 palavras por take, **fala do prompt de video igual palavra por
palavra ao roteiro**, JSON valido, bandeira dos EUA em todo keyframe com cenario, `no captions`
no negative, termo sensivel no negative, secoes obrigatorias na ordem, nomenclatura T/K/V/REF,
os 5 blocos do prompt de video, instrucao de patch e produto em quadro nos angulos 2 e 3. Pasta
com `pipeline: auraly` cai no `checar_auraly()`, que nao exige `PROMPTS_PRODUCAO.md` nem `DM.md`.

**Zero FALHAS antes de entregar.** Se sobrar falha, corrigir e rodar de novo. Se a falha for
falso positivo, **consertar o linter**, nao ignorar a saida: linter que se aprende a ignorar
morre em uma semana.

> Existe porque o carregamento do PASSO 0 pode ser comprimido numa sessao longa, e porque
> regra lembrada e regra esquecida. O linter le do disco e nao depende de contexto nenhum.

> O gabarito `producao/fitywell_pernas/` passa com 0 FALHAS (3 avisos em 2026-09-22: conferencia
> de GERAR DO ZERO a olho e o topo da skill `gancho-verbal`, que ele antecede). O antigo
> `producao/brandon_angle2/` falhava de proposito nas praticas revogadas e virou historico.

---

## Gate final, colar preenchido antes de fechar a entrega

```
[ ] BLOQUEANTE: CHECKLIST DE ENVIO (memoria checklist-envio-prompt, GATE_VISUAL.md Parte 5)
    rodado em TODO gancho, K e V deste pacote, 100% aprovado, linha "Checklist de envio: X/X"
    na entrega. Item reprovado = o pacote NAO e enviado
[ ] PORTAO P5 completo: gabarito fitywell_pernas + memoria carregada + GATE_VISUAL.md, lidos NESTA sessao
[ ] Rodada declarada. VALIDACAO: um gancho fiel ao modelo, desvios declarados, aprovado com o
    roteiro, sem 10. VARIACAO: base validada registrada, 10 ganchos entregues e escolhidos ANTES dos prompts
[ ] PORTAO P6 lido antes dos prompts de video
[ ] PORTAO P10 executado ou agendado (log de rotacao + biblioteca)
[ ] Os DOIS arquivos escritos em producao/<avatar>_<slug>/
[ ] Fila de avatares no disco, avatar atual DONE e proximo PENDING avancado
[ ] Tabela de esqueleto preservado presente
[ ] Indice de geracao presente
[ ] Travas globais escritas uma vez, nao repetidas em cada JSON
[ ] Mapa de ancoras / Montagem / Gates de qualidade presentes
[ ] Palavras contadas: todo take entre 13 e 29, ou marcado CENA CURTA quando a cena do modelo e curta; nenhuma cena juntada, nenhuma frase cortada para caber
[ ] Fala do prompt = copia literal do roteiro
[ ] Rota de fechamento diferente da do video anterior (log conferido)
[ ] Bloco do Flow colado inteiro no topo do pacote deste avatar
[ ] Blocos K e V limpos para maquina, sem texto auxiliar dentro
[ ] Transcricao final em INGLES e em PORTUGUES colada, roteiro final em INGLES por ultimo
[ ] ANGULO 3: estado e entrega conferidos contra WORKFLOW_AURALY.md e o CHECKPOINT
[ ] ANGULO 3: keyword 222 na fala e isolada na tela no CTA
[ ] ANGULO 3: CTA na ordem 222 -> save -> follow -> Stories, rosto esperando no STORIES, sem quiz, teste, app nem preco
[ ] ANGULO 3: nenhuma leitura de pacto/feitico; cartas holograficas/foil, arte saturada
```
