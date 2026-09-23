# Analise medida dos ganchos virais (maya.astor e afins) — ANGULO 3 AURALY SOMENTE

Data: 2026-09-20 · Autor: Claude · Escopo: **exclusivamente Angle 3 / Auraly (manifestacao e alma gemea)**.
Nao altera FitWell (Angulos 2 e 4) nem Korella (Angulo 1).

Amostra: 54 arquivos `.mp4` em `~/Downloads`, 53 da conta `maya.astor` mais 1 `snapinsta`.
Metodo: extracao de frames com `ffmpeg` em 0.6s para todos os 54; timelines de 8 frames
(0.1 / 0.7 / 1.4 / 2.2 / 3.2 / 4.5 / 6 / 8s) em amostra; deteccao de corte por `select=gt(scene,N)`;
medicao de volume por `volumedetect` em janelas de 3s.

Esta analise e complementar a `producao/analise_ganchos_virais_maya_astor_2026_09_20/`. Onde
divergir, o criterio e: **o que foi medido tem precedencia sobre o que foi inferido.**

---

## 1. As tres medicoes que mudam a producao

### 1.1 Os primeiros 3 segundos sao MUDOS

Volume medio por janela de 3 segundos:

| video | 0-3s | 3-6s | 6-9s | 20-23s | 40-43s |
|---|---|---|---|---|---|
| 21 (pepino/sal/vaso) | **-31.3 dB** | -22.1 dB | -17.8 dB | -16.1 dB | -17.9 dB |
| 12 (caixa de correio) | **-32.3 dB** | -19.8 dB | -16.7 dB | -17.5 dB | -18.6 dB |
| 38 (saldo bancario) | **-34.3 dB** | -24.3 dB | -17.2 dB | -17.2 dB | -17.2 dB |

Os 3 primeiros segundos estao **14 a 17 dB abaixo** do corpo do video. Isso nao e fala baixa,
e ausencia de fala: e room tone. A voz entra por volta de 3-4s e so atinge nivel pleno em 6s.

**Consequencia:** o scroll-stop e carregado **100% por imagem + texto de tela**. O espectador chega
sem audio util e o cerebro precisa resolver a cena pelo olho, o que prende o olhar. Quando a voz
entra, ela ja encontra alguem que parou.

**Contraste com a nossa producao:** o nosso T1 fala desde o frame zero, com 13 a 29 palavras. Nos
gastamos o primeiro segundo explicando, enquanto eles gastam prendendo.

### 1.2 O gancho e uma RAJADA DE CORTES DENTRO DE UM CLIPE SO, e o corpo e um plano unico

Timestamps de corte, video inteiro, limiar `scene > 0.12`:

- **video 21 (110s de duracao):** cortes em `0.93 · 1.57 · 2.13 · 4.13 · 6.00 · 6.07`
  → 6 cortes nos primeiros 6 segundos, **zero cortes nos 104 segundos seguintes**.
- **video 12 (81s de duracao):** cortes em `1.63 · 2.63 · 3.97 · 4.70 · 4.73 · 4.77 · 4.83`
  → 7 cortes nos primeiros 5 segundos (incluindo uma rajada de 4 cortes em 130ms),
  **zero cortes nos 76 segundos seguintes**.

A densidade de corte do gancho e de aproximadamente **1 corte por segundo**, e a do corpo e **zero**.
Todo o orcamento de edicao do video esta nos primeiros 6 segundos.

**Consequencia:** o gancho deles nao e um plano fixo. E uma sequencia de 5 a 7 planos.

⚠️ **CORRECAO DO LUIGI, 2026-09-20, mesma data:** isso **nao** sao varios clipes. E **UM clipe so**,
com as mudancas de plano **escritas dentro do prompt de video** e geradas pelo Veo no mesmo take.
Logo, **continua `1 K + 1 V`** e o custo do gancho nao muda. O que muda e o que se escreve no bloco
`o que acontece no video`. Toda a secao 6.1 abaixo foi reescrita por causa disto.

**Contraste com a nossa producao:** nosso contrato e `1 K = 1 V = 8 segundos`. Nosso gancho inteiro
e UM plano de 8 segundos. Estamos comparando uma sequencia montada com um plano fixo, e perdendo
pela estrutura, nao pela ideia.

### 1.3 Os videos sao LONGOS

Duracoes medidas: 57, 80, 80, 81, 86, 92, 95, 103, 103, 110, 115, 135 segundos.
Faixa de **57s a 135s**, com a maioria entre 80 e 110s.

Nao sao videos de 30-45 segundos. Sao videos de um minuto e meio com um gancho de 6 segundos
extremamente trabalhado na frente.

---

## 2. A anatomia do gancho, frame a frame

Referencia: video 21 (pepino + sal Morton + vaso sanitario), o caso mais limpo.

| t | plano | o que acontece |
|---|---|---|
| 0.1s | medio, ela agachada ao lado do vaso | ja segura pepino e lata de sal · **texto ja na tela** |
| 0.9s | mesmo plano | crava o pepino dentro do pote de sal (acao ja comecada) |
| 1.6s | **MACRO das maos** | corte fechado no pepino entrando no sal, unhas vermelhas, aneis |
| 2.2s | volta ao medio | pepino agora coberto de sal, ela comeca a falar |
| 4.1s | medio | quebra o pepino ao meio sobre o vaso aberto |
| 6.0s | **flash branco** | transicao com `222` e `11:11` flutuando |
| 8.0s | medio, plano do corpo | legenda karaoke `KEEP YOUR MOUTH [SHUT]` |

Referencia: video 12 (caixa de correio), estrutura narrativa em vez de ritual.

aproxima da caixa → abre → puxa envelope pardo → **MACRO das maos contando dolares** →
volta ao medio com o envelope cheio → fala para a camera com legenda karaoke `DON'T TELL ANYONE`
e seta vermelha circulando uma janela da casa ao fundo.

**O padrao de montagem e sempre o mesmo:** plano de acao → **insert macro exatamente no instante do
payoff** → volta ao plano de corpo → fala. O macro nunca e decorativo: ele cai no frame em que a
acao culmina, e e ele que entrega a recompensa tatil sem entregar a explicacao.

---

## 3. O que o espectador SENTE, na ordem

Isto e o que o Luigi pediu: nao a lista de elementos, e sim a sequencia emocional.

1. **Segundo 0 — constrangimento, nao curiosidade.** Uma mulher careca, agachada ao lado de um vaso
   sanitario, com um pepino e uma lata de sal. A primeira emocao nao e "que interessante", e
   **"o que diabos esta acontecendo aqui"**, com um componente de desconforto e leve vergonha
   alheia. Desconforto e mais forte que curiosidade porque o corpo reage antes do julgamento.
2. **Segundo 0, em paralelo — reconhecimento do desejo.** O texto de tela ja diz
   `When you need urgent and unexpected money`. Ele nao e mistico, e **economico e urgente**.
   O espectador que esta apertado se reconhece antes de entender a cena.
3. **Tensao entre os dois.** Agora existe um desejo nomeado e uma cena absurda, e nenhuma ponte
   entre eles. Essa lacuna e o motor. **Ela nao pode ser fechada no gancho.**
4. **Segundo 1.5 — recompensa tatil.** O macro entrega textura, som implicito, unhas, sal, pele.
   Satisfaz o olho sem satisfazer a mente. Compra mais 2 segundos.
5. **Segundo 4-6 — stakes e prazo.** `Be careful on September 15th`, `this Wednesday`,
   `THIS IS YOUR FINAL WARNING`. A lacuna agora tem **data de vencimento**, o que converte
   curiosidade em urgencia.
6. **Segundo 6-8 — cumplicidade.** `Don't tell anyone`, `SHUT YOUR MOUTH`, dedo na boca.
   O espectador e promovido de audiencia a **insider**. Isso e o que gera o save e o comentario:
   ele nao esta consumindo, esta guardando um segredo.
7. **Resto do video — a voz assume.** Plano unico, sem corte, tom confidencial. Aqui e onde a
   copy trabalha, e por isso ela pode durar 90 segundos.

**O sentimento-alvo em uma frase:** *constrangimento produtivo* — desconforto suficiente para
travar o polegar, com um desejo nomeado do lado para justificar continuar assistindo.

Os nossos ganchos produzem **admiracao** (cofre dourado, moeda dentro da pedra, carta expelida).
Admiracao nao trava o polegar. Admiracao e agradavel, e o agradavel desliza.

---

## 4. As sete alavancas que eles usam e nos nao

### 4.1 A calvicie como fingerprint
A avatar e **careca**, sem sobrancelhas marcadas, em 51 dos 54 videos. Isso e uma anomalia
biologica presente em **todo frame**, de graca, sem custo de producao, sem VFX e sem prop. Ela
resolve simultaneamente scroll-stop, memoria de conta e reconhecimento entre videos.
Nosso roster e de rostos convencionalmente bonitos e intercambiaveis.

### 4.2 Produto de marca real como ancora de realidade
Morton Salt, Arm & Hammer Baking Soda, Tabasco, Vicks VapoRub, Pure Honey, um envelope pardo,
uma caixa de correio americana, um calendario de parede. **A marca e a prova de que a cena e real.**
Objeto generico lê como cenografia; objeto de marca lê como cozinha de alguem.

### 4.3 Objeto no lugar errado, com carga sexual velada
Pepino ao lado do vaso. Calcinha de renda vermelha sobre panela fervendo. Calcinha vermelha
embrulhando um pepino. Perfume nos pes. Bicarbonato no rosto, sem camisa. Salsicha no pao.
A transgressao nao e ocultista, e **domestica e corporal**, que e o que passa na moderacao e ao
mesmo tempo constrange.

### 4.4 Texto de tela que declara DESEJO, nao misterio
`When you need urgent and unexpected money:` aparece em cerca de 30 dos 54. Nao e
`the universe has a message`. E dinheiro, urgente, inesperado. **Segmenta pelo aperto financeiro,
no frame zero, antes de qualquer misticismo.**

### 4.5 Numeros como marca d'agua, nao como CTA
`222`, `11:11`, `444`, `111` ficam flutuando no canto da tela desde o primeiro frame, pequenos,
como se fossem parte da interface. Eles nao sao pedidos ali. Funcionam como **selo de canal** e
como gatilho de reconhecimento para quem ja e do nicho. O pedido vem depois, na fala.

### 4.6 Split vertical: rosto em cima, ritual embaixo
Varios videos dividem o quadro na horizontal: **rosto/busto na metade de cima, maos e ritual na
metade de baixo**, com costura dura visivel. Nao e o nosso plano unico com a mesa no terco inferior.
Sao dois planos empilhados.

### 4.7 O significado nunca fecha no gancho
Em nenhum dos 54 o gancho explica por que aquilo traria dinheiro. A acao fisica resolve
(o pepino foi quebrado, o envelope foi aberto), mas a **consequencia pessoal fica aberta**.
Nos fechamos: apareceu o ouro, a pergunta acabou.

---

## 5. Onde isto colide com as nossas regras vigentes

Registro de colisao. **Nao alterei nenhuma regra**; a decisao e do Luigi.

| regra nossa | onde esta | colisao medida |
|---|---|---|
| `T1` fala com 13 a 29 palavras | `CLAUDE.md`, `checar_entrega.py:230` | os virais sao **mudos** nos 3 primeiros segundos |
| `1 K = 1 V`, take de 8s | `CLAUDE.md` (Google Flow Delivery Format) | o gancho deles tem **5 a 7 planos em 6s** |
| `no captions` no negative | `memoria/regras_universais.md` | **todos** tem texto de tela no frame zero |
| plano unico, nunca split screen | `CLAUDE.md`, secao Angulo 3 | varios usam **split vertical** rosto/ritual |
| kit de tarologo em toda ancora | `memoria/angulo3_copy_auraly.md` | o cenario deles e **banheiro, cozinha, cama, carro, quintal** |
| nunca citar marca | `memoria/restricoes_protocolo.md` | **marca real em quadro** e a ancora de realidade deles |
| bandeira dos EUA em todo K | `CLAUDE.md` | presente em alguns, **ausente na maioria** |

Observacao importante: o take mudo **ja e suportado** pelo linter. `checar_entrega.py:78` e `:254`
reconhecem `B-ROLL`, `MUDO` e `SEM FALA`, e `:138` reconhece `sem fala no take` no prompt de video.
Nao ha conflito tecnico para um T1 mudo; ha conflito de doutrina no `CLAUDE.md`.

O `no captions` no negative **continua correto** e nao precisa mudar: o texto de tela e camada de
**edicao no CapCut**, nunca texto gerado dentro do `K__`. O `WORKFLOW_AURALY.md` ja diz isso.

---

## 6. O que eu proponho na pratica

### 6.1 Os cortes do gancho vao DENTRO do prompt de video
♻️ **Reescrito apos a correcao do Luigi.** A versao anterior desta secao mandava fatiar o T1 em
4 a 6 `K__`/`V__` curtos, e estava errada.

**Continua `1 K + 1 V`.** O `K__` do gancho e o **primeiro plano** da sequencia; o resto nasce
dentro do `V__`, que passa a descrever as mudancas de plano:

```
(sem fala no take: o take do gancho e mudo)

o que acontece no video: [plano medio, acao JA COMECADA] ... corte para MACRO das maos no
instante do payoff ... corte de volta para o plano de corpo

camera: cortes internos ao clipe, [descricao]

som ambiente: [ambiente], sem musica
```

**O custo do gancho nao muda:** 1 keyframe + 1 clipe por variacao, e os `K` do corpo continuam
reaproveitados, exatamente como ja fazemos.

### 6.2 O T1 nasce MUDO por padrao
Marcar `T1 · B-ROLL · MUDO` no `ROTEIRO.md`. A fala do T1 atual vira **voz-over que entra no T2**,
ou e simplesmente cortada. O linter ja aceita.

### 6.3 A camada de texto de tela entra no plano de edicao
Toda variacao de gancho passa a declarar duas linhas, fora do bloco do Flow:
- **linha de desejo**, concreta e nao mistica, no padrao `When you need [desejo urgente]:`
- **linha de selecao/prazo**, no padrao `Be careful on [data]` ou `Don't tell anyone`

### 6.4 Troca de eixo criativo
Parar de perguntar *"qual imagem representa a alma gemea"* e passar a perguntar
*"que acao domestica, fisicamente real e levemente constrangedora, uma mulher faria sozinha em
casa e nao contaria para ninguem?"*. A alma gemea entra **na fala**, nunca no objeto.

### 6.5 Fingerprint com anomalia permanente
Ao construir o proximo roster Auraly, priorizar **um traco anomalo permanente** no avatar, presente
em todo frame sem custo: calvicie, cabelo raspado, despigmentacao, cicatriz visivel, heterocromia.
E a alavanca de maior retorno por menor custo de toda a amostra.

---

## 7. Onde eu concordo e onde eu divirjo do relatorio anterior

**Concordo e confirmo por medicao:**
- anomalia visual imediata no frame zero
- texto de tela com desejo ou perigo
- marcador de selecao pessoal (`222`, `11:11`, data)
- significado adiado
- repeticao modular de esqueletos, com troca de uma variavel

**Divirjo ou acrescento:**
- **`4+3+3` e uma regra de portfolio, nao a descoberta.** A descoberta e a **montagem do gancho**
  (rajada de cortes, macro no payoff, silencio). Repetir familia com o nosso gancho de plano unico
  de 8 segundos vai produzir dez variacoes que flopam juntas, com mais organizacao.
- **"ritual domestico" e consequencia, nao causa.** A causa e o **constrangimento domestico**. O
  ritual e so o veiculo mais barato dele.
- **"VFX simples pode funcionar" e impreciso.** O que funciona e VFX que **nao explica**: o flash
  branco com `222` aos 6s e transicao, nao revelacao. Cofre dourado abrindo explica e por isso mata.
- **O relatorio nao mediu duracao, corte nem audio**, que sao justamente as tres variaveis
  estruturais que separam o formato deles do nosso.

---

## 8. Estado

- Nada foi alterado em `CLAUDE.md`, `WORKFLOW_AURALY.md`, `memoria/`, memoria viva ou linter.
- Este documento e analise, nao decisao.
- Escopo travado em **Angle 3 / Auraly**.
