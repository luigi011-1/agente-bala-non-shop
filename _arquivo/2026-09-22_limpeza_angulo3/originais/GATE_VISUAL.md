# GATE VISUAL · realismo, composição e gancho (TODOS OS ÂNGULOS)

Criado em 2026-09-22 a pedido do Luigi. **Fonte única e transversal** das regras que fazem o vídeo de
IA não parecer IA e que fazem o herói do gancho parar o scroll. Vale para Korella, FitWell e Auraly.
**Sem exceção de ângulo:** Ângulo 1 (Korella), Ângulo 2 (FitWell) e Ângulo 3 (Auraly) rodam as quatro
partes. O que muda entre eles são só as travas de marca já escritas em cada seção.

**Por que existe:** as regras viviam só na memória (`realismo-anti-cara-de-ia` e
`checklist-composicao-visual`) e nenhum workflow vigente apontava para elas. Medido em 2026-09-22:
a maioria dos pacotes recentes ainda aplica, mas por hábito, e os furos já aparecem (6 K do
`snapinsta_1789935769670_growth` sem o negative de tom quente, 5 K do Lorenzo sem luz definida).
Regra que depende de lembrança se perde. Por isso ela agora é etapa do workflow e aviso do linter.

**Quando rodar:** as Partes 1 a 3, antes do primeiro `K__` de qualquer pacote. A Parte 4 é o método
de variação de gancho dos três ângulos, antes de entregar as 10. O gate não muda o formato do Flow:
ele define **o que vai dentro** de cada prompt.

Cada regra nova que mudar algo aqui se escreve **aqui**, e as memórias apontam para cá.

---

## PARTE 1 · REALISMO (anti cara de IA)

### 1.1 Cor e luz, o que mais denuncia
- **Nunca tom quente.** Amarelo, laranja e marrom são a assinatura de imagem de IA.
- **Interna:** `neutral overcast daylight from a window`, luz difusa de dia nublado.
- **Externa:** `overcast sky with visible cloud texture` ou `deep blue sky`. Nos avatares de luxo,
  hora azul (`deep blue sky, soft cool ambient light, no orange sunset`).
- **Céu branco, claro ou estourado SEMPRE denuncia.** O céu tem cor e textura escritas no prompt.
- **Janela estourada também:** escrever `the outside is clearly visible through the window`.
- 🚫 **Golden hour BANIDA** (Luigi, 2026-09-22), em todos os ângulos. Revoga o "externa: golden
  hour" do gate antigo, que contradizia o item de tom quente. Pôr do sol, contraluz alaranjado e
  "fim de tarde" entram na mesma proibição. O linter reprova golden hour pedida no positivo.

### 1.2 Rosto e pele
- **Rosto sem sombra dura**, claro e nítido. Sombra no rosto é reprovação.
- Pele real: `visible pores, irregular skin texture, faint redness, fine lines, minor blemishes,
  soft facial asymmetry`. Cabelo em `uneven natural clumps`, nunca fio a fio perfeito.
- **No K de fala:** `caught mid-sentence, lips naturally parted, animated expression`. O frame
  inicial com a boca entreaberta ajuda o lip sync do Veo.

### 1.3 Foco e acabamento
- **Tudo em foco:** `background fully in focus, no bokeh, no blur anywhere`. Fundo borrado não se
  conserta depois.
- **Estética de celular comum:** `iPhone footage, flat natural light, low contrast, slight JPEG
  compression, boring everyday reality, not professional photography, no AI polish, no beauty
  smoothing, no HDR, no cinematic lighting`.

### 1.4 Partir sempre de algo real (regra-mãe)
> A IA copia bem o que você mostra e inventa mal o que você só descreve.
- **Print do primeiro frame do vídeo modelo** como referência de composição, junto com a âncora.
  Prompt sozinho não reproduz posição e enquadramento.
- Rosto de pessoa secundária: referência de rosto real. Prop que teima: gerar isolado primeiro.
- Âncora é o ativo que mais pesa. Nenhum prompt compensa âncora ruim.
- **Realismo é volume:** regenerar é o método, não sinal de prompt errado.
- Baixar a imagem aprovada em 4K e subir de novo antes de animar.

---

## PARTE 2 · COMPOSIÇÃO DO HERÓI

### 2.1 Herói
1. O herói do gancho fica no **lower foreground, mais perto da lente que o rosto**. Escrever:
   `the [hero] is very close to the lens in the lower foreground, large in frame, closer to the
   camera than her face`.
2. **"Dá pra estar mais perto?"** Se dá, está longe. Sempre mais perto do que parece certo.
3. **Nada compete com o herói.** Se um elemento não serve à fala do take, sai de quadro.
4. Volume do herói explícito: montanha, não camada fina; objeto inteiro, não detalhe.

### 2.2 Fundo
5. **Duas ou três âncoras de fundo descritas, no máximo.** O inimigo é o **inventário no prompt**,
   não a bagunça: cenário vivido que vem da âncora se preserva com `the same lived-in room as the
   reference, unchanged`, sem listar item a item.
6. **Reduzir fundo é com enquadramento, NUNCA com blur.**
7. Cenário **reconhecível** e, quando couber, **americano de bate-pronto** (bandeira discreta e
   visível, cozinha americana, fachada de Walmart ou Costco). Teste: em 2 segundos dá pra saber
   que é EUA?

### 2.3 Pessoas e distância
8. Pessoas do **peito pra cima**; o take mais fechado do vídeo é o do CTA.
9. **2ª pessoa entra cortada pelo quadro**, nunca de corpo inteiro.

### 2.4 Exceções que já existem (não mudam aqui)
- **Ângulo 3:** o kit de tarólogo é obrigatório e entra **agrupado em dois blocos** (prateleira +
  parede), que é como o teto de âncoras convive com ele. Fingerprint + cenário próprio por gancho.
- **T1 do Ângulo 3:** cortes internos no `V__`, macro das mãos no payoff e split vertical liberado.
  Do T2 em diante, plano único.
- **Corpo neutro ao gancho:** o prop que muda entre os ganchos fica FORA de quadro no corpo.

---

## PARTE 3 · TRECHOS PRONTOS (texto corrido, para os blocos do Flow)

Colar **dentro** de cada prompt, adaptando só o que está entre colchetes. Os blocos do Flow são
autossuficientes, então isto se repete em todo `K__`, sem exceção.

**Luz interna**
`Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.`

**Luz externa**
`Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on the face.`

**Herói**
`The [hero] is very close to the lens in the lower foreground, large in frame, closer to the camera than [her/his] face, nothing else competing with it.`

**Realismo (fecha todo prompt)**
`Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.`

**Selfie (vale para o `V__`)**
`The hand holding the phone never moves; only the other hand gestures.`

---

## PARTE 4 · GANCHO VISUAL: PUZZLE COM DEGRAU (Luigi, 2026-09-22)

Funde os dois métodos e fica com o mais forte de cada um:

| Vem do **Puzzle** | Vem do **Step up** (curso Lib Korella) |
|---|---|
| a base é o hook do vídeo modelo, que já provou | nunca refazer o viral igual: quem se interessaria já viu |
| a ação estrutural não se toca | subir **um degrau** sobre o que já funcionou |
| **uma variável por variação**, então o resultado se lê | as camadas que mais pagaram: dificuldade diária, contradição, reação |
| 10 variações, 1 keyframe + 1 clipe cada | o vencedor vira a base da rodada seguinte |

**Por que os dois não brigam:** o degrau entra **uma vez, no esqueleto, antes das variações**. Ele
muda a base, não a variação. Cada uma das 10 continua trocando uma única variável, então a leitura
de qual gancho venceu continua limpa. Trocar duas variáveis numa mesma variação segue reprovado.

### Passo 1 · Ação estrutural e peça viral
Escrever a **ação estrutural** do hook do modelo (Puzzle) e a **peça viral**: o que fez aquele vídeo
estourar (o primeiro clipe, o herói, o fundo, o layout ou o roteiro). **As duas são intocáveis.**

### Passo 2 · Um degrau no esqueleto
Acrescentar **UMA** camada que o modelo não tem, escolhida desta escada:

| Degrau | O que acrescenta | Caso medido no curso |
|---|---|---|
| `DIFICULDADE` | o problema num momento concreto do dia | "barriga" → "não consegue entrar no carro": 2k → 180k |
| `CONTRADICAO` | um estado impossível, visível no quadro | "78 anos" → "78 anos **andando** como 30": 6k → 150k |
| `REACAO` | segunda pessoa reagindo, validando ou chocada, cortada pelo quadro | mulheres atrás + homem reagindo à idade |
| `EUA` | cenário americano icônico carregando o take | fora do Costco ou do Walmart |
| `ESCALA` | exagero de volume, quantidade ou tamanho do herói | montanha no lugar de camada fina |

Travas do degrau:
- **Um só por produção.** É ele que a rodada está testando.
- **Não toca a peça viral** e **nunca obriga a reescrever a fala**.
- **Cabe em 1 keyframe + 1 clipe.** Se precisa de clipe extra, é degrau demais.
- **Korella e FitWell:** continua congruente com a fala do T1, e clickbait segue proibido. Na
  Korella o frasco nunca é a variável trocada nem o degrau: o produto fica fixo onde o roteiro pede.
- **Auraly:** o degrau aumenta o **constrangimento**, nunca a admiração, e o rosto da alma gêmea
  continua nunca revelado. `REACAO` aqui é alguém flagrando o ritual, não aplaudindo.

Declarar no topo: `Degrau: CATEGORIA - o que foi acrescentado`.

### Passo 3 · As 10 variações
- **HOOK 1 = CONTROLE:** o esqueleto **original, sem o degrau**, com uma variável trocada. É o que
  mostra se o degrau pagou. Recomendado escolher o controle em pelo menos um avatar.
- **HOOK 2 a 10:** o esqueleto **com o degrau**, uma variável trocada em cada um.
- No Auraly, clickbait puro continua liberado, no fim e marcado.
- **A camada verbal das 10** (fala do T1, texto de tela) segue a skill **`gancho-verbal`**, modo
  PRODUCAO (2026-09-22): no topo, tese, sintoma-alvo, direcao, padrao do modelo e banco verbal com 5
  frases literais do roteiro; em cada variacao, texto de tela de no maximo 9 palavras com uma frase
  do banco; no fim, `Recomendacao: HOOK X`. A frase muda so porque a variavel visual mudou: trocar a
  estrutura da frase junto seria segunda variavel.

### Passo 4 · Checklist de cada variação
1. **Coerência visual e verbal, sem redundância:** o que a fala ou o texto de tela diz aparece na
   imagem, mas o texto não narra o que a imagem já mostra. Mesmo assunto, informação diferente: se
   a imagem mostra o problema, o texto carrega o resultado, ou o contrário (skill `gancho-verbal`).
2. **Um único ponto focal, colado na lente** (Parte 2). Em 1 segundo o olho sabe onde olhar.
3. **Ação já começada** no primeiro frame. Mostrar, segurar ou apontar para o objeto reprova.
4. **Emoção crua** no rosto (raiva, espanto, vergonha), nunca a expressão neutra de banco de imagem.
5. **Sinal de EUA** no quadro quando couber (Parte 2, item 7).

### Passo 5 · Rotação
Quando uma variação vence, **ela vira a base** da próxima produção do mesmo esqueleto, que sobe
**mais um degrau, de outra categoria**, em cima dela. Nunca repetir o mesmo degrau sobre a mesma
base e nunca refazer o vencedor igual. Registrar em `biblioteca-videos`: esqueleto, degrau e
vencedor, para a próxima rodada saber de onde partir.

---

## PARTE 5 · CHECKLIST DE ENVIO (BLOQUEANTE, Luigi, 2026-09-22)

Depois das Partes 1 a 4 e **antes de enviar qualquer coisa** ao Luigi (lista de ganchos, `K__`,
`V__`, pacote ou prompt avulso), rodar o **checklist de envio** da memória `checklist-envio-prompt`:
os insights do curso Lib Korella em cinco blocos (A gancho, B imagem, C vídeo, D montagem, E marca),
válidos em todos os ângulos, presentes e futuros.

- **Item reprovado = o prompt não sai.** Corrige e roda o checklist de novo. Nunca enviar com ressalva.
- Item que não se aplica vira `N/A`, nunca aprovado por omissão.
- A entrega leva, **fora** dos blocos copiáveis: `Checklist de envio: X/X aprovados (N/A: ...)`.
