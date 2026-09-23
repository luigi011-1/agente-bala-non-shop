---
name: prompts-video-fase7
description: "Formato do prompt de vídeo Veo 3.1/Flow (Fase 7) + regras invioláveis — fala inteira+intacta, ação enxuta, TALKING vs B-ROLL, sem música, sotaque americano explícito, voz 'demanding to be heard', lip sync + última palavra inteira, ~2 linhas de fala por take (filler se curto), braço parado quando handheld/selfie, exemplos reais."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 246ef273-2f24-4b5d-8e5e-51929be93030
  modified: 2026-08-19T02:51:02.932Z
---

# Prompts de Vídeo — Fase 7 (Veo 3.1 via Flow)

Depois da imagem pronta, ela é animada no Flow/Veo. O prompt é **texto simples** (não JSON), em formato validado.

## Formato validado

**Take TALKING (avatar fala):**
```
o avatar (homem/mulher) fala em inglês com sotaque americano, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvido(a), a seguinte frase: "[FALA EXATA DO TAKE, EM INGLÊS]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação fiel ao frame, ENXUTA — só o que de fato acontece]. O avatar age naturalmente, faz movimentos dinâmicos e rápidos, mantendo o vídeo engajante. Estilo TikTok nativo, UGC.

câmera: [movimento simples, ex.: fixa / leve push-in / leve handheld natural]

som ambiente: [ambiente do cenário], sem música, sem ruído de fundo
```

**Quando câmera é HANDHELD/SELFIE (braço estendido):**
Adicionar: "o avatar não move o braço que está estendido para [esquerda/direita] do quadro porque a mão está segurando a câmera que captura o vídeo."

**Take B-ROLL / INSERT (sem fala):**
```
(sem fala no take: a fala [N] do roteiro entra como voz-over na edição)

o que acontece no vídeo: [ação do insert]

câmera: [macro fixa / top-down fixa]

som ambiente: [ambiente], sem música
```

## Regras de ouro (invioláveis)

1. **A FALA SEMPRE VAI INTEIRA NO PROMPT.** Nunca tire, altere ou remova a fala pra tentar destravar restrição. Se o vídeo original foi gerado, aquela fala já passou uma vez e vai passar de novo. Regra mais importante do documento, aprendida errando. Ver [[restricoes-protocolo]].

2. **Descrição da ação ENXUTA.** Só o que acontece de fato — sem exagero de ângulo, posição, região-alvo, adjetivos dramáticos. Excesso é o que dispara restrição de conteúdo. Preferir "o homem despeja água de um regador e olha para a câmera enquanto fala" a um parágrafo detalhando ângulo, região do corpo atingida, etc.

3. **"sem música" sempre** no som ambiente. A trilha entra na edição pra você controlar + evitar strike de copyright.

4. **Marcar TALKING vs B-ROLL.** Inserts não levam linha "o avatar fala"; locução deles entra na edição.

5. **Câmera simples.** "fixa", "leve push-in", "leve handheld", "top-down fixa". Nada rebuscado.

6. **Bater a ação com o frame inicial.** O que acontece no vídeo = continuação natural do estado inicial da imagem. Ex.: imagem = "colher de canela sobre o abacaxi"; vídeo = "vira a colher e a canela cai".

7. **A fala de cada take tem que CABER em 8s, e é cópia exata do roteiro.** (Regra corrigida em 2026-08-18 pelo Luigi, substitui a orientação antiga de "adicionar frase filler".)
   - **NUNCA adicionar frase filler, nunca inventar palavra, nunca parafrasear.** O roteiro final é a fonte única de verdade.
   - A forma de resolver take curto ou take longo é **quebrar o roteiro em trechos diferentes**, sempre cortando em fim de frase, não mexendo nas palavras.
   - Referência de tamanho: ~3,3 palavras por segundo. Logo **8s ≈ 26 palavras**. Alvo seguro por take: 13 a 29 palavras.
   - Take que passar de ~26 palavras: dividir em dois. Take curto demais: aceitar e cortar o silêncio no CapCut, nunca preencher com texto inventado.

8. **Última palavra inteira.** Sempre colocar no prompt "says the last word whole, doesn't cut it at the end" e "doesn't skip any words". Veo tende a cortar a última sílaba.

9. **Braço do celular (selfie/handheld).** Quando a câmera simula handheld, o avatar NÃO deve mover o braço que "segura o celular". Especificar no prompt qual braço fica parado. Não incluir essa instrução quando a câmera NÃO é handheld.

10. **Sotaque específico.** Usar "English with an American accent of a black man/woman" (ajustar ao avatar). Especificar o sotaque melhora lip sync e naturalidade.

## Exemplos reais

**Take talking com demo (canela no abacaxi, Melody):**
```
o avatar (homem) fala em inglês fluente a seguinte frase: "Put cinnamon on pineapple and just watch what happens."

o que acontece no vídeo: o [avatar] inclina o saleiro de canela sobre a tigela com abacaxi em cubos; a canela cai sobre o abacaxi; ele olha da tigela pra câmera.

câmera: fixa, leve handheld, plano médio levemente de cima

som ambiente: ambiente de garagem, sem música
```

**Take b-roll (insert reveal nojento — camarão):**
```
(sem fala no take: a fala 2 do roteiro entra como voz-over na edição)

o que acontece no vídeo: close extremo do camarão na água quente; finos vermes brancos começam a sair da carne e se contorcem na água fumegante.

câmera: macro fixa, leve tremor

som ambiente: água fervente, sem música
```

**Take CTA (follow-gate, keyword yes):**
```
o avatar (homem) fala em inglês fluente a seguinte frase: "Comment yes below and I'll send it to you, but make sure you're following me, or it won't let me reach you."

o que acontece no vídeo: o [avatar] aponta pra câmera ao dizer "comment yes", inclina-se levemente, expressão direta no fim.

câmera: fixa, leve push-in

som ambiente: ambiente de garagem, sem música
```

## Quando um take trava por restrição
Protocolo completo em [[restricoes-protocolo]]. Resumo: nunca é a fala, enxugar a ação, neutralizar o alvo, e se persistir separar elementos em takes diferentes (juntar no corte, nunca no mesmo prompt).

Relacionadas: [[faixa-palavras-take]].
