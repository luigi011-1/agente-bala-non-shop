# 03 — Processo de Produção Passo a Passo (as 7 Fases)

> Lembrete: todo o processo produz vídeos de **avatares de IA (pessoas que não existem)**.

Este é o fluxo operacional completo, do recebimento do vídeo de referência até o vídeo final pronto pra postar. São 7 fases. Siga na ordem.

---

## FASE 1 — Ingestão (juntar os insumos)

Você precisa de **três coisas** para começar:

1. O **vídeo de referência** (`.mp4`) — o vencedor que vai ser clonado.
2. O **roteiro / copy** — a fala do vídeo (o texto que o avatar vai dizer). Às vezes vem transcrito, às vezes você extrai do próprio vídeo.
3. O **avatar** — a foto de referência do personagem de IA que vai protagonizar (ex.: `melody_carter_.png`).

**Regra:** sempre entregue o `.mp4` e o roteiro **juntos**. O roteiro sozinho não basta (você precisa ver a estrutura visual); o vídeo sozinho também não (você precisa da fala exata).

**Insight importante:** se você recebeu o vídeo de referência, significa que **aquele vídeo já foi gerado e passou** pelas ferramentas. Isso tem uma consequência crucial para restrições (ver Fase 7 e documento 06): **a fala nunca será o problema**, porque aquela fala já foi gerada uma vez.

---

## FASE 2 — Decomposição (analisar o vídeo FRAME A FRAME)

Esta é a fase mais importante e a mais fácil de fazer mal feito. **Nunca "bata o olho" e presuma a estrutura.** Analise quadro a quadro.

### Como decompor tecnicamente

1. **Extraia frames** do `.mp4` em intervalos densos (a cada 1 a 2 segundos, e mais denso ainda no hook — a cada 0,3 a 0,5s). Ferramenta: `ffmpeg`.
   - Exemplo de comando (extrair 1 frame por segundo dos primeiros segundos): 
     ```
     ffmpeg -ss [SEGUNDO] -i "video.mp4" -frames:v 1 -q:v 3 frame_[SEGUNDO].png -y
     ```
2. **Monte "contact sheets"** (grades de miniaturas) pra ver a evolução do vídeo de uma vez. Ferramenta: `montage` (do ImageMagick).
   - Exemplo: `montage frame_0.png frame_1.png ... -tile 5x2 -geometry 240x427+3+3 -background white -title "Parte 1" sheet1.png`
3. **Olhe cada frame com atenção real.** Em especial o hook: extraia frames MUITO densos (0,3s) porque o detalhe herói costuma estar num movimento rápido.

### O que mapear (beat a beat)

Para cada beat/cena, anote numa tabela:

| Campo | O que anotar |
|-------|--------------|
| **Timestamp** | Quando começa/termina |
| **Esqueleto visual** | O que se vê na tela (composição, ação) |
| **Nº de pessoas** | 1 (solo) ou 2+ (tem segunda pessoa? é herói?) |
| **Props** | Objetos em cena (tigela, copo, luvas, livro, modelo anatômico...) |
| **Fala** | O que é dito (resumo) |
| **Label (função)** | HOOK / MECANISMO / RECEITA / PROTOCOLO / RESULTADO / PROVA / CTA |

### O que NUNCA deve passar batido

- **Qual é o herói do hook exatamente** (não presuma — veja a seção 2.3 e os casos de erro no doc 06).
- **Se há segunda pessoa** e qual o papel dela (cliente? é o herói?).
- **O que muda entre os takes** (cor de roupa? tamanho de algo? ângulo?).
- **Props que dão credibilidade** (luvas, livro, modelo anatômico).
- **Cenário do original** (pra decidir a adaptação ao cenário do avatar).
- **Onde exatamente algo acontece** (ex.: a água cai NO ponto X, não no Y).

> **Regra registrada em memória:** *ao decompor um `.mp4`, analise frame a frame com grades densas e considere cada detalhe (props, segunda pessoa, o que muda entre takes, enquadramento, elemento herói) antes de construir qualquer coisa. Não faça pattern-matching / não presuma a estrutura.* Um erro histórico: ler um hook onde o herói era o braço de uma cliente com a gordura encolhendo take a take (roupa mudando de cor só pra fingir dias diferentes) como se fosse "uma mulher bebendo um líquido com continuidade". Foi preciso reanálise frame a frame pra corrigir.

---

## FASE 3 — Definição da Variável

Com a estrutura mapeada, defina o que muda:

- **Qual a variável** a ser trocada (o novo ingrediente/produto/problema)?
- Cada beat mantém a **mesma função** com o conteúdo novo?
- Há **congruência** com o avatar escolhido (cenário, gênero, registro, idade)? Ajuste o ângulo (ex.: "coach que prescreve") sem mexer na estrutura.
- Se for testemunho/transformação **sem variável óbvia**, mantenha 100% fiel e diferencie pelo avatar/cliente.

---

## FASE 4 — Roteiro Final

Escreva o roteiro final adaptado, respeitando:

- **Takes de ~8 segundos** cada (quebre falas longas em takes).
- **Sem em dash** (travessão "—"). Use frases curtas.
- **Registro do avatar** (masculino/feminino/caloroso).
- **Keyword sempre "yes"** no CTA (`comment "yes" below` / `type "yes" below`), sobrepondo a palavra do original.
- **Ajustes de congruência** na fala (idade, "coach que prescreve", remover "dear" se não combina com avatar masculino, etc.).
- **Estrutura idêntica** à do original — só a variável muda.

Marque cada take como **TALKING** (avatar fala) ou **B-ROLL** (insert sem rosto falando).

---

## FASE 5 — Prompts de Imagem (o frame inicial de cada take)

Para cada take, escreva um prompt de imagem que gera o **frame inicial** (o estado inicial da cena). Detalhes completos no documento 04. Pontos-chave:

- Gera-se **o estado INICIAL** do take, não o meio nem o fim. A transformação (líquido dissolvendo, água lavando) acontece depois, na FASE 7 (vídeo), não na imagem.
- **Nunca gere before/durante/depois como imagens separadas de uma transformação dentro do mesmo take** — só o estado inicial. (Exceção: os "estágios" do antes/depois disfarçado, que são takes diferentes — ver doc 02, seção 4.)
- **Zero texto na imagem** (sempre no negative: "no text, no captions, no words on screen").
- A **foto do avatar é a âncora** de identidade/roupa/cenário, mas **não** dita pose/câmera (isso você controla no prompt).

---

## FASE 6 — Geração de Imagem

- Gere no **Nano Banana 2** (volume) ou **Pro** (frames-herói).
- **Trave a segunda pessoa primeiro:** se há cliente/segunda pessoa, gere ela primeiro, aprove o rosto, e reuse esse rosto como referência nos outros takes pra manter consistência. Isso é o que faz ou quebra vídeos de antes/depois.
- **Estágios de transformação** (braço encolhendo, etc.): gere o estágio 1, aprove, e gere os demais **por edição a partir do estágio 1 original** (nunca em cascata), mantendo enquadramento idêntico.
- **Frames-herói** (hook): gere várias variações até acertar. O hook é o que mais paga; vale o retrabalho.
- Revise cada imagem: o modelo/prop saiu certo? (ver caso do modelo anatômico virando coração, no doc 06.)

---

## FASE 7 — Geração de Vídeo (animar a imagem)

Cada imagem (frame inicial) vira um clipe de ~8s no **Veo 3.1 via Flow** (ou Lite/Lower Priority pra não gastar crédito). Você dá a imagem + um prompt de vídeo. Formato do prompt de vídeo (detalhado no doc 04):

```
o avatar (homem/mulher) fala em inglês fluente a seguinte frase: "[FALA EXATA DO TAKE]"

o que acontece no vídeo: [ação fiel ao frame, ENXUTA — só o que de fato acontece]

câmera: [movimento simples]

som ambiente: [ambiente + "sem música"]
```

Regras da Fase 7:
- **Takes TALKING** levam a linha `o avatar fala...` com a fala exata.
- **Takes B-ROLL / insert** NÃO levam fala (a locução entra como voz-over na edição). Marque "(sem fala no take)".
- **A fala vai sempre inteira no prompt** — nunca a retire para tentar destravar restrição (ver doc 06, a regra é crítica).
- **Descrição da ação enxuta:** só o que acontece de fato, sem exagero de ângulo/posição/adjetivo (ajuda a não disparar restrição).

---

## PÓS-PRODUÇÃO (edição final — fora das 7 fases, mas essencial)

- Junte os takes na ordem.
- Adicione as **legendas grandes** (estilo Captions.ai Prism Pro) — inclusive a keyword "yes" no CTA.
- Onde um take foi gerado **sem fala** (b-roll ou take que travou no gerador), adicione a **locução** (gravada ou TTS) + legenda por cima.
- Adicione a **trilha/música** na edição (os prompts de vídeo pedem "sem música" justamente pra você controlar a trilha depois).
- Exporte 9:16.

---

## Resumo visual do fluxo

```
[.mp4 + roteiro + avatar]
        ↓  FASE 1 Ingestão
[frames extraídos + contact sheets]
        ↓  FASE 2 Decomposição (frame a frame!)
[tabela beat a beat + herói identificado]
        ↓  FASE 3 Variável definida
[roteiro final, keyword yes, takes 8s]
        ↓  FASE 4 Roteiro
[prompts de imagem, 1 por take, sem texto]
        ↓  FASE 5 Prompts de imagem
[imagens geradas, avatar consistente, 2ª pessoa travada]
        ↓  FASE 6 Geração de imagem
[prompts de vídeo Fase 7, fala intacta, ação enxuta]
        ↓  FASE 7 Geração de vídeo
[takes de ~8s]
        ↓  Pós-produção
[VÍDEO FINAL 9:16 com legenda, locução onde preciso, música]
```
