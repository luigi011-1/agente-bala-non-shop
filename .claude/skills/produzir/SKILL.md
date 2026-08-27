---
name: produzir
description: Executa a producao completa de um video modelado, na ordem travada, do roteiro ate os prompts. Escreve os DOIS arquivos em producao/<avatar>_<slug>/ (ROTEIRO.md e PROMPTS_PRODUCAO.md), TRES no Angulo 3 (mais DM.md) com todas as secoes obrigatorias e cola tudo na conversa. Use quando o usuario mandar /produzir, ou quando um roteiro for aprovado e for hora de gerar o pacote de prompts. Existe porque o formato de entrega se degradou quando dependia de eu lembrar dele.
---

# /produzir — pacote de producao completo

Esta skill existe por um motivo especifico: em 2026-08-21 o formato de entrega se degradou porque eu passei a recompor a entrega de memoria em vez de seguir o gabarito. **Aqui a ordem e travada. Nao improvisar, nao pular secao, nao reinventar formato.**

---

## PASSO 0 — PORTAO P5: ler ANTES de escrever qualquer coisa

**Executar esta skill NAO substitui ler.** A skill e a ordem, os documentos sao o conteudo.
Ler os nove itens do **PORTAO P5** do `CLAUDE.md`, sempre, mesmo achando que lembra:

```
[ ] producao/brandon_angle2/ROTEIRO.md  (o gabarito vivo)
[ ] producao/brandon_angle2/PROMPTS_PRODUCAO.md
[ ] memoria workflow-entrega-gabarito
[ ] memoria checklist-composicao-visual
[ ] memoria realismo-anti-cara-de-ia
[ ] memoria prompts-imagem-json
[ ] memoria erros-recorrentes (falhas 1 a 7)
[ ] memoria avatares-fichas (tracos canonicos + caminho da ancora)
[ ] memoria feedback-prompt-imagem-compartilhado + feedback-enquadramento-mais-proximo
```

**E antes dos prompts de VIDEO, o PORTAO P6:** `prompts-video-fase7`,
`PLAYBOOK_COMPLETO/11_insights_otimizacao.md` secao 3, e `restricoes-protocolo`.

**Depois da entrega, o PORTAO P10:** escrever no log de rotacao e na biblioteca de videos.

---

## PASSO 0-B — O gabarito, o que copiar e o que NAO copiar

Ler os dois arquivos, sempre, mesmo achando que lembra:

- `producao/brandon_angle2/ROTEIRO.md`
- `producao/brandon_angle2/PROMPTS_PRODUCAO.md`

Copiar dali o **FORMATO**, nunca o conteudo. Duas praticas daquele arquivo foram **revogadas** e nao podem ser copiadas:
1. **Frase filler** (proibida desde 18/08). Take curto se resolve requebrando o roteiro em fim de frase.
2. **Um keyframe por take** (desde 20/08 e um keyframe por SETUP/BLOCO).

## PASSO 1 — Checar os pre-requisitos

Nao seguir sem os quatro:
- [ ] `/watch` rodado e decomposicao beat a beat feita
- [ ] Heroi do hook identificado sem ambiguidade (rodar o micro-protocolo de 5 perguntas de `erros-recorrentes`)
- [ ] Angulo definido (1 Korella / 2 FityWell / **3 Auraly**) e avatar confirmado
- [ ] Roteiro aprovado pelo Luigi

Faltando qualquer um, parar e pedir. Roteiro nao aprovado torna todo prompt retrabalho garantido.


## PASSO 1-B — QUAL AVATAR: o anexo decide

**`.mp4` + imagem de avatar na mesma mensagem = produzir PARA AQUELE AVATAR.** Nao perguntar.
Ciclo completo dele primeiro: roteiro, ganchos, prompts, DM.

**Rodar o mesmo modelo no proximo avatar depois**, com:
- **AJUSTES DE COPY para congruencia**, nunca copia palavra por palavra. Idade, genero e registro
  mudam o que soa crivel na boca de cada avatar. Abrir `congruencia-matriz` antes de portar.
- Ajustes de identidade, cenario, registro de voz e `rt_ad` nos prompts.

> Regra corrigida pelo Luigi em 2026-08-25. Eu tinha gravado que a copy ficava identica entre
> avatares (`kendra_veu` e `kendra_inicial` foram feitos assim). **A regra vigente e ajustar.**

## PASSO 1-A — SE FOR ANGULO 3 (Auraly), o que muda

**O PROCESSO E O MESMO DOS ANGULOS 1 E 2. Nada aqui substitui o fluxo validado.**
Mesmo `/watch`, mesmo metodo puzzle, mesma cabeca de copy, mesma ordem de entrega, mesma estrutura de
prompts, mesmas travas de realismo, mesmos 5 blocos no prompt de video. **So troca o que e do produto.**

Ler `angulo3-copy-auraly` (doutrina) e `angulo3-swipe-padroes` (banco de copy do nicho, o equivalente
ao `angulo2-copy-fitywell`).

O que muda, e so isso:
- **Keyword `222`** no lugar de `yes`.
- **Nao mostra produto.** O objeto de desejo do CTA e o **rosto da alma gemea**, que chega **na DM**.
  O video nunca diz quiz, teste, app, plano nem preco.
- **Angulo de entrada livre, ponte pro rosto obrigatoria.** Um avatar so (Blake Epeterson), entao o
  eixo de variacao e 1 esqueleto x N angulos de entrada.
- **Registro divino, nunca oculto.** Sem feitico, pacto, escudo, circulo de protecao.
- **Ancora do Blake:** `producao/_ancoras/Man_sitting_at_table_4K_202608241610.jpeg`, anexada como
  referencia de identidade e cenario (igual o Angulo 1 anexa o `product.png`).
- **Terceiro arquivo `DM.md`** (ver PASSO 4-A), derivado de `producao/_dm_auraly/DM_PADRAO.md`.

**Duracao, numero de takes e gramatica visual saem do VIDEO MODELO**, como sempre. Nao existe formato
fixo do angulo. Fidelidade de estrutura e a regra de sempre.

## PASSO 2 — Abrir as memorias de copy do fechamento

Antes de escrever o bloco de venda, abrir:
- `banco-rotas-argumentativas` → **conferir o log de rotacao.** Qual rota o ultimo video desta conta usou? Nao repetir a rota nem as frases. Frase que ja foi ao ar esta queimada.
- `banco-obstaculos` → empilhar um obstaculo de cada rota de fuga
- `feedback-ponte-argumentada` → a ponte e cadeia de 3 a 4 elos, nunca afirmacao
- `angulo2-copy-fitywell` (se for Angulo 2)

- `angulo3-copy-auraly` + `angulo3-swipe-padroes` (se for Angulo 3). No Angulo 3 estas memorias
  atendem o beat de fechamento onde ele existir: no video, se o modelo tiver esse beat, e sempre no `DM.md`.

## PASSO 3 — Criar a pasta e escrever `ROTEIRO.md`

`producao/<avatar>_<slug>/ROTEIRO.md`, nesta ordem, sem pular secao:

1. **Cabecalho**: video modelo, avatar, variavel trocada, funil, enquadramento do avatar
2. **Tabela de esqueleto preservado**: `# | Beat | Original | Adaptado`
3. **Setups de cena**: Setup A, B, C... cada um listando os takes que atende
4. **Roteiro cena a cena**: `### T1 · BEAT · TALKING|B-ROLL · Setup A`
5. **Roteiro so-fala** (ingles corrido, pro TTS)
6. **Notas de producao**: duracao, heroi do hook, compliance, o que cortar se ficar longo

**Contar as palavras de cada take AGORA, nao depois.** 8s = 13 a 25 palavras. Passou de 26, quebrar em fim de frase.

## PASSO 3-B — SO NO ANGULO 3: sugestoes de GANCHO VISUAL antes dos prompts

**Ordem travada: roteiro aprovado -> sugestoes de gancho visual -> so entao prompts.**
Nao entregar prompt nenhum antes de mandar as variacoes de gancho e o Luigi escolher.

Derivar as variacoes **do mesmo video modelo**. A **copy fica identica em todas**, palavra por palavra.
So mudam os primeiros segundos, o prop e a acao do hook.

*Por que existe:* neste angulo a copy e o ativo e o gancho visual e descartavel. Ele so para o scroll.
Um roteiro validado vira N videos trocando so o hook. E como o Angulo 3 nao precisa segmentar publico,
gancho de clickbait puro converte, entao isso joga a favor.

**Nao fazer isso nos Angulos 1 e 2**, onde o heroi do hook carrega argumento e nao se troca a toa.

**Entregar de 8 a 10 variacoes**, ordenadas por congruencia com a copy, com as de clickbait puro no fim
e marcadas como tal.

**ANGULO 3: a MAIORIA dos ganchos tem que ter a CARTA em quadro**, de preferencia como alvo da acao.
Congruencia com o quiz da oferta. Artes: SOULMATE e TWINFLAME.

**LIBERDADE TOTAL PARA INVENTAR (Luigi, 2026-08-24).** O banco dos 13 mecanismos e ponto de partida,
nao limite. Sempre misturar **ganchos validados** com **ganchos novos que nunca foram testados**, e
marcar quais sao quais. Se o Luigi nao gostar de um inventado, ele simplesmente nao seleciona.
Nao existe custo em propor demais, existe custo em propor de menos. Banco dos 13 mecanismos em `producao/_swipe_auraly/BANCO_GANCHOS_VISUAIS.md`.

Cada variacao traz: **mecanismo** (qual dos 13 + video de referencia) · **a acao** (o que MUDA em quadro,
nunca objeto parado) · **prop** (existe no cenario ou precisa entrar) · **congruencia** com a copy ·
**texto de tela** · **custo** em keyframes e clipes · **risco** de geracao.

**FORMATO DA CONTA E PLANO UNICO, NUNCA SPLIT SCREEN.** Camera na altura do peito do outro lado da
mesa: o avatar do peito pra cima, a mesa no terco inferior do MESMO quadro, e **ele executa a acao do
gancho com as proprias maos enquanto fala**. Sem close isolado na mesa, sem B-roll separado.
O gancho vive no T1. Do T2 em diante ele segura a carta e os takes se reaproveitam entre variacoes,
entao cada gancho novo custa **1 keyframe + 1 clipe, so o T1**.

## PASSO 3.5 — GATE DE COMPOSIÇÃO VISUAL, antes de escrever qualquer prompt

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
[ ] 3. Luz NEUTRA de dia nublado. Sem "warm and even" como padrao
[ ] 4. Negative carrega: no warm orange color cast, no yellow tint, no golden glow
[ ] 5. Fundo descrito com especificidade, e nunca borrado
[ ] 6. Prop que costuma teimar tem REF-PROP gerado isolado antes
[ ] 7. Bloco de realismo padrao colado por inteiro em todo prompt
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


## PASSO 4-A — SE FOR ANGULO 3, escrever `DM.md`

`producao/<avatar>_<slug>/DM.md`. E onde a venda comeca. Nesta ordem:
1. **Cabecalho**: qual video dispara, keyword `222`, destino do link
2. **A mensagem que promete o rosto**, em ingles, pronta pra colar
3. **Ponte pro link** sem dizer quiz, teste nem app
4. **Obstaculos antecipados** (`banco-obstaculos` + rotas de fuga do publico)
5. **Follow-up** para quem clicou e nao comprou

Travas: nunca dizer "one-time" nem "pagamento unico" (o checkout renova a $29/mes).
Nunca prometer encontro real, data real nem pessoa real. Registro divino, nunca oculto.

## PASSO 5 — Colar tudo na conversa

Arquivo nao substitui chat. Cada prompt vai em bloco de codigo pronto pra copiar, precedido de **uma linha curta** dizendo o que aparece na cena e quais imagens anexar.

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

**Keyword sempre `yes`.** Zero travessao. Angulo 2 nao mostra produto, Angulo 1 mostra sempre.

---

## Gate final, colar preenchido antes de fechar a entrega

```
[ ] PORTAO P5 completo: gabarito + as 7 memorias, lidos NESTA sessao
[ ] PORTAO P6 lido antes dos prompts de video
[ ] PORTAO P10 executado ou agendado (log de rotacao + biblioteca)
[ ] Os DOIS arquivos escritos em producao/<avatar>_<slug>/ (TRES no Angulo 3, com DM.md)
[ ] Tabela de esqueleto preservado presente
[ ] Indice de geracao presente
[ ] Travas globais escritas uma vez, nao repetidas em cada JSON
[ ] Mapa de ancoras / Montagem / Gates de qualidade presentes
[ ] Palavras contadas: nenhum take acima de 26
[ ] Fala do prompt = copia literal do roteiro
[ ] Rota de fechamento diferente da do video anterior (log conferido)
[ ] Roteiro final por ultimo
[ ] ANGULO 3: duracao e numero de takes fieis ao video modelo
[ ] ANGULO 3: keyword 222 na fala e isolada na tela no CTA
[ ] ANGULO 3: CTA promete o ROSTO na DM, sem citar quiz, teste nem app
[ ] ANGULO 3: nenhuma leitura de pacto/feitico; cartas em cor clara
```
