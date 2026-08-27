---
name: regras-universais
description: "10 regras fixas que valem para TODA produção — keyword por ângulo (yes nos ângulos 1 e 2, **222 no ângulo 3**), zero texto, reference_use, sem copo de vidro decorativo, realismo UGC, takes ~8s sem em dash, fala nunca é o problema, frame a frame denso, só estado inicial, trocar só o do avatar entre versões."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 246ef273-2f24-4b5d-8e5e-51929be93030
  modified: 2026-08-21T23:51:52.145Z
---

# Regras Universais Fixas (valem para TODOS os vídeos)

**Why:** cada uma foi consolidada por erros repetidos ou pela necessidade de padronizar automação (ex.: keyword única). Ignorar uma delas costuma custar retrabalho ou matar a conversão.

**How to apply:** checar TODAS antes de fechar cada roteiro/imagem/prompt de vídeo. Ver [[erros-recorrentes]] pros casos que geraram cada regra.

## 1. Keyword do CTA = depende do ANGULO (regra editada em 2026-08-24)
**Angulos 1 e 2 (Korella, FityWell): `yes`.** **Angulo 3 (Auraly, alma gemea): `222`.**
Regra original de 2026-08-07 era "sempre yes em qualquer avatar/nicho". **Foi substituida em 2026-08-24 por decisao do Luigi**, que fixou `222` como keyword permanente do Angulo 3 (o numero e congruente com o universo de sinais e numeros repetidos que o proprio quiz sonda: 11:11, 444).
Vale sempre **ignorando a palavra que o video original usa** (tea, book, drink, pure...). Aparece como `comment "222" below` ou `type "222" below`. Variar a forma da frase pra nao ficar mecanico.

## 2. Zero texto SOBREPOSTO nas imagens geradas
Negative correto, e a formulação importa:
```
no captions, no subtitles, no words overlaid on the image
```
**NÃO usar `"no text"` seco.** Isso apaga a sinalização canônica do cenário, que é parte da identidade do avatar: o neon `TRAIN PRAY REPEAT` da Brandon, o quadro branco `STAY READY. STAY DISCIPLINED.`, a placa da garagem do Melody. Essa sinalização **deve continuar existindo**. O que não pode é legenda ou palavra sobreposta por cima da imagem. Legenda de vídeo entra só na edição.

Corrigido em 2026-08-21 na auditoria de conflito: a memória dizia `"no text"` enquanto o gabarito real em `producao/brandon_angle2/` usava a formulação estreita e correta.

## 3. Âncora controla identidade/roupa/cenário, NÃO câmera/pose
Sempre incluir campo `reference_use` restringindo isso explicitamente. Sem essa trava, a pose da foto de referência vaza pra cena. Ver [[erros-recorrentes]] falha #3.

## 4. Sem copos de vidro de beber decorativos
Quando não fizer sentido → preferir mason jar, cerâmica, ou tigela transparente (bowls transparentes OK para demos onde se precisa ver o conteúdo).

## 5. Realismo UGC sempre
Poros, pele real, cara de vídeo de iPhone. NUNCA "cara de IA" polida. Bloco padrão de realismo em [[prompts-imagem-json]].

## 6. Takes de ~8 segundos, sem em dash
Falas longas quebradas em takes. Nunca usar travessão "—". Frases curtas.

## 6B. Fala no prompt de video = copia exata do roteiro final
O texto entre aspas dentro de cada prompt de video deve ser copia IDENTICA, palavra por palavra, do trecho correspondente no roteiro final. NUNCA reescrever, parafrasear ou "melhorar" a fala ao montar o prompt. Processo correto: escrever o roteiro final primeiro como fonte unica de verdade, depois copiar cada trecho para o prompt correspondente.

**Inclui NAO adicionar frase filler** (reforcado pelo Luigi em 2026-08-18, depois que eu inventei uma frase pra encher um take curto). Se a fala nao couber em 8s ou ficar curta demais, a solucao e **requebrar o roteiro em trechos**, cortando em fim de frase. Alvo: 13 a 25 palavras por take (~3,3 palavras/segundo, 8s ≈ 26 palavras). Detalhe em [[prompts-video-fase7]] regra 7.

## 7. A fala NUNCA é o problema em restrições
Nunca altere a fala pra destravar. Se o vídeo original foi gerado, aquela fala já passou uma vez. Ajustar APENAS a descrição da cena/ação. Regra inviolável. Ver [[restricoes-protocolo]].

## 8. Analisar o .mp4 frame a frame denso ANTES de montar
Nunca presumir estrutura. Nunca pattern-matching. Grades densas (0,3-0,5s no hook, 1-2s no geral), cada detalhe (props, 2ª pessoa, o que muda entre takes, enquadramento, herói). Ver [[processo-7-fases]] Fase 2.

## 9. Gerar SÓ o estado inicial de cada take
A transformação (líquido dissolvendo, água lavando, etc.) acontece no vídeo (Fase 7), não em imagens separadas. Exceção: os "estágios" do antes/depois disfarçado são takes DIFERENTES, cada um com sua imagem (correto).

## 10. Ao produzir o mesmo vídeo para vários avatares
Trocar SÓ o que é do avatar (cenário, cruz, registro, gênero da fala). Manter esqueleto e props idênticos.

## Regras específicas por avatar (memória rápida)
- **Brandon:** cruz de OURO (não force prata)
- **Trevor:** SEM cruz (a menos que peça); melhor pra cozinha
- **Melody:** cruz de prata; corrigir pose sentada da foto-âncora
- **Luvas azuis de nitrila:** manter em vídeos de inspeção de comida (credibilidade)

Ver fichas completas em [[avatares-fichas]].

## 🇺🇸 BANDEIRA DOS EUA EM TODO PROMPT DE IMAGEM (Luigi, 2026-08-26)

**Todo prompt de imagem leva a bandeira dos EUA no cenário. Discreta, porém VISÍVEL e em foco.**

Discreta = pequena e periférica (bandeirinha de mesa em suporte, patch na roupa, adesivo no canto
de um espelho). **Nunca desfocada, nunca cortada pela borda, nunca só implícita.**

Escrever dentro do campo `scene` do JSON, contando como uma das âncoras de fundo. O teto do
[[realismo-anti-cara-de-ia]] continua sendo **3 âncoras**, então a bandeira ocupa uma das três e
o cenário fica cheio: nada mais entra depois dela.

**Única exceção:** prompt de REF de prop isolado (REF-CARTA, `product.png` e afins), que não tem
cenário nenhum. Colocar bandeira ali contamina o objeto de referência e ela vazaria para todo
keyframe que anexasse aquela REF.

Isso já valia como "bandeira US sutil" nas fichas do Ângulo 3 ([[avatares-fichas]]). **A regra
agora é geral, vale para os três ângulos, e é obrigatória e não estética.**
