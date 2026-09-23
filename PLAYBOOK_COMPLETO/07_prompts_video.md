# 07 — Guia Completo de Prompts de Vídeo (Fase 7)

> **Lembrete:** todos os prompts animam cenas de **avatares de IA — pessoas que não existem**. Em tema sensível, deixe claro para a ferramenta que é um personagem fictício de IA.

Depois que a imagem (frame inicial) está pronta e aprovada, você a anima no Flow/Veo. O prompt de vídeo é em **texto simples** (não JSON), num formato validado por muitas gerações. Este documento traz o formato, as regras de ouro, exemplos reais e como lidar com travas.

---

## 1. Formato validado (copie a estrutura)

**Take TALKING (avatar fala):**
```
o avatar (homem/mulher) fala em inglês com sotaque americano, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvido(a), a seguinte frase: "[FALA EXATA DO TAKE, EM INGLÊS]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação fiel ao frame, ENXUTA — só o que de fato acontece]. O avatar age naturalmente, faz movimentos dinâmicos e rápidos, mantendo o vídeo engajante. Estilo TikTok nativo, UGC.

câmera: [movimento simples, ex.: fixa / leve push-in / leve handheld natural]

som ambiente: [ambiente do cenário], sem música, sem ruído de fundo
```

**Quando a câmera é HANDHELD/SELFIE (braço estendido):**
Adicionar ao prompt: "o avatar não move o braço que está estendido para [esquerda/direita] do quadro porque a mão está segurando a câmera que captura o vídeo." Não incluir quando a câmera NÃO é handheld.

**Take B-ROLL / INSERT (sem fala):**
```
(sem fala no take: a fala [N] do roteiro entra como voz-over na edição)

o que acontece no vídeo: [ação do insert]

câmera: [macro fixa / top-down fixa]

som ambiente: [ambiente], sem música
```

**Título identificador:** entregue cada prompt precedido de um título curto que diz o que é o take, para facilitar na hora de gerar. Ex.:
> ### TAKE 3 — REVEAL HERÓI · crosta desaba e revela os vasos limpos

---

## 2. Regras de ouro (leia com atenção)

### Regra 1 — A FALA VAI SEMPRE INTEIRA NO PROMPT

Nunca tire, altere ou remova a fala pra tentar destravar uma restrição.

- **Se o vídeo modelo foi gerado por IA:** aquela fala já passou uma vez pelo gerador e vai passar de novo. A fala não é o gatilho.
- **Se o vídeo modelo é filmagem real:** essa garantia não existe (a fala nunca passou por um gerador). Nesse caso uma palavra específica pode de fato travar. Mesmo assim, **tente com a fala intacta primeiro**, e só se travar procure o substituto **dentro do próprio roteiro original** (uma expressão que o próprio original usa em outro momento), sem inventar. Ver documento 09.

### Regra 2 — Descrição da ação ENXUTA

Descreva **só o que acontece de fato**, sem exagero de ângulo, posição ou adjetivos dramáticos. Excesso de descrição de local/posição/região-do-corpo é o que costuma disparar restrição de conteúdo.

- ❌ "ele despeja a água sobre o baixo ventre da cliente deitada, joelhos dobrados, a água escorre pelo tecido e pinga na bandeja, câmera no eixo mostrando a cena de frente"
- ✅ "o homem despeja água de um regador e olha para a câmera enquanto fala. Uma mulher está deitada em uma maca ao lado."

### Regra 3 — "sem música" sempre

Sempre coloque "sem música" no som ambiente. A trilha entra na edição, pra você controlar (e evitar strike de copyright de música).

### Regra 4 — Marque TALKING vs B-ROLL

Inserts não levam a linha "o avatar fala"; a locução deles entra na edição como voz-over.

### Regra 5 — Câmera simples

"fixa", "leve push-in", "leve handheld", "top-down fixa". Nada rebuscado.

### Regra 6 — Bata a ação com o frame inicial

O que acontece no vídeo deve ser a continuação natural do estado inicial da imagem. Ex.: imagem = "colher de canela sobre o abacaxi"; vídeo = "vira a colher e a canela cai".

### Regra 7 — ~2 linhas cheias de fala por take

O Veo funciona melhor com cerca de 2 linhas cheias de texto falado por clipe. Se a fala do take for muito curta (1 frase só), adicione uma **frase filler** pra completar ~2 linhas. Isso mantém o clipe dinâmico e rápido. Depois no CapCut, corte o trecho do filler. Nunca gere um take com fala muito curta (sai lento/arrastado).

### Regra 8 — Última palavra inteira

Sempre coloque no prompt: "says the last word whole, doesn't cut it at the end" e "doesn't skip any words". O Veo tende a cortar a última sílaba do clipe.

### Regra 9 — Braço parado no modo selfie/handheld

Quando a câmera simula selfie/handheld, o avatar está "segurando o celular" com um braço. Esse braço NÃO deve se mover. Especifique qual braço fica parado no prompt. Só inclua esta instrução quando a câmera é handheld.

### Regra 10 — Sotaque específico

Use "English with an American accent of a black man/woman" (ajuste ao avatar e ao gênero). Especificar o sotaque melhora o lip sync e a naturalidade da voz.

---

## 3. Exemplos reais de prompts de vídeo

**Take talking com demo (canela no abacaxi):**
```
o avatar (homem) fala em inglês fluente a seguinte frase: "Put cinnamon on pineapple and just watch what happens."

o que acontece no vídeo: o avatar inclina o saleiro de canela sobre a tigela com abacaxi em cubos; a canela cai sobre o abacaxi; ele olha da tigela pra câmera.

câmera: fixa, leve handheld, plano médio levemente de cima

som ambiente: ambiente de garagem, sem música
```

**Take b-roll (insert de reveal nojento):**
```
(sem fala no take: a fala 2 do roteiro entra como voz-over na edição)

o que acontece no vídeo: close extremo do camarão na água quente; finos vermes brancos começam a sair da carne e se contorcem na água fumegante.

câmera: macro fixa, leve tremor

som ambiente: água fervente, sem música
```

**Take de reveal herói (crosta que desaba — vídeo da Brandon):**
```
o avatar (mulher) fala em inglês fluente a seguinte frase: "Because this is what it does to the calcification destroying your performance."

o que acontece no vídeo: a crosta branca desaba em pedaços e cai no vinagre, revelando os vasos vermelhos e azuis limpos e brilhantes escorrendo líquido; Brandon olha direto pra câmera.

câmera: fixa, leve push-in

som ambiente: ambiente de galpão, líquido pingando, sem música
```

**Take CTA (com follow-gate, keyword yes):**
```
o avatar (mulher) fala em inglês fluente a seguinte frase: "Comment yes and I'll send you the complete protocol. Make sure you're following me, otherwise I won't be able to reach you."

o que acontece no vídeo: Brandon segura a jarra dourada à altura do peito e aponta o indicador pra câmera ao dizer "comment yes"; expressão firme no fim.

câmera: fixa, leve push-in

som ambiente: ambiente de galpão, sem música
```

---

## 4. Como lidar quando um take de vídeo trava por restrição

Ver o documento 09 inteiro para o protocolo completo. Resumo, sempre mantendo a fala intacta:

1. **Enxugue a ação** — reduza a descrição do "o que acontece" ao mínimo. Tire ângulo, posição, região-alvo, adjetivos.
2. **Neutralize o alvo** — se o elemento atinge uma região sensível, redirecione pra um ponto neutro (a bandeja, o chão, por cima da roupa). A metáfora se mantém pela legenda + presença dos elementos.
3. **Separe os elementos em takes diferentes** — se a combinação de dois elementos trava mesmo enxuta, gere dois takes limpos e junte no corte. Nenhum frame isolado fica problemático.
4. **Explicite que é ficção de IA** — em contexto sensível, deixe claro que é um personagem de IA fictício, não uma pessoa real. Isso é verdade e ajuda a ferramenta a entender que não há dano real.

> **Limite importante:** o objetivo do protocolo acima é **reproduzir fielmente** a estrutura do vídeo modelo, não engenheirar prompts para passar conteúdo explícito por um filtro. Nos vídeos desse nicho, o herói do original costuma ser um prop **ambíguo** (uma massa vascular, uma banana) — é a **fala + a legenda** que fazem a associação anatômica, não o frame isoladamente. A reprodução fiel é o prop ambíguo, e isso normalmente resolve tanto o gerador quanto a moderação da plataforma. Se um prop só "funciona" ficando explícito, esse é o sinal de que a reprodução fiel é a versão ambígua, não a versão explícita.

---

## 5. Checklist da Fase 7 (antes de dar os prompts por prontos)

- [ ] Fala inteira e intacta em cada take TALKING?
- [ ] Ação enxuta (só o que acontece de fato)?
- [ ] TALKING vs B-ROLL marcados?
- [ ] "sem música" no som ambiente de todos?
- [ ] Cada prompt tem um título identificador?
- [ ] Câmera simples?
- [ ] A ação bate com o frame inicial da imagem?

Próximo documento: **08 — Fichas dos Avatares**.
