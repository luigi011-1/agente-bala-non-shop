# 05 — O Processo de Produção Passo a Passo

> **Lembrete:** todo o processo produz vídeos de **avatares de IA — pessoas que não existem**.

Este é o fluxo operacional completo, do recebimento do vídeo modelo até o vídeo final pronto pra postar. São **7 fases** mais a pós-produção. Siga na ordem. Cada fase tem seus documentos de apoio (prompts em 06 e 07, correções em 09).

---

## Visão geral do fluxo

```
[.mp4 modelo + foto do avatar (+ roteiro se houver)]
        │  FASE 1 — Ingestão
        ▼
[/watch: frames densos + transcrição + grades]
        │  FASE 2 — Decomposição (frame a frame!)
        ▼
[tabela beat a beat + herói identificado]
        │  FASE 3 — Definição da variável
        ▼
[TRANSCRIÇÃO COMPLETA + ROTEIRO CENA A CENA]  ← ponto de validação com o operador
        │  FASE 4 — Roteiro final
        ▼
[prompts de imagem, 1 por take, sem texto]
        │  FASE 5 — Prompts de imagem
        ▼
[imagens geradas, avatar consistente, 2ª pessoa travada]
        │  FASE 6 — Geração de imagem
        ▼
[prompts de vídeo, fala intacta, ação enxuta]
        │  FASE 7 — Geração de vídeo
        ▼
[takes de ~8s]
        │  PÓS-PRODUÇÃO
        ▼
[VÍDEO FINAL 9:16 com legenda, locução, música]
```

---

## FASE 1 — Ingestão (juntar os insumos)

Você precisa de **três coisas** para começar:

1. O **vídeo modelo** (`.mp4`) — o vencedor que vai ser clonado.
2. A **foto do avatar** — a foto base do personagem de IA que vai protagonizar (Melody, Brandon ou Trevor).
3. Opcional: o **roteiro / copy** — a fala do vídeo. Se você não tiver, a `/watch` transcreve do próprio vídeo.

**Regra:** sempre entregue o `.mp4` e a foto do avatar juntos. Se tiver o roteiro, mande também (serve de conferência cruzada com a transcrição).

**Nota técnica:** o vídeo precisa estar **salvo no computador como arquivo**. A `/watch` roda `ffmpeg` sobre o arquivo, então é preciso o caminho real em disco (ex.: `C:\Users\...\Downloads\video.mp4`), não só o anexo visual. A foto do avatar pode ser vista inline e é salva numa pasta de avatares.

**Insight importante sobre restrições:** se o vídeo modelo foi **gerado por IA** e passou pelas ferramentas, isso tem uma consequência para a Fase 7 — a fala daquele vídeo já foi gerada uma vez e vai passar de novo. **MAS** se o vídeo modelo é **filmagem real** (pessoas reais, cozinha real, etc.), essa garantia **não vale** — a fala nunca passou por um gerador, e uma palavra específica pode travar. Sempre verifique qual é o caso. (Detalhes no documento 09.)

---

## FASE 2 — Decomposição (analisar o vídeo FRAME A FRAME)

Esta é a fase mais importante e a mais fácil de fazer mal feito. **Nunca "bata o olho" e presuma a estrutura.** Analise quadro a quadro.

Rode a `/watch` (documento 04):

```
powershell -File ".claude/skills/watch/scripts/run_watch.ps1" -Video "CAMINHO.mp4" -OutDir "entradas/nome_watch"
```

Depois, com a saída em mãos:

1. **Leia a transcrição** (`audio/transcript.txt`) — a fala beat a beat com timestamps.
2. **Leia a grade de cenas** (`overview_scenes_*`) — entenda o arco: quantos takes, o que é cada um.
3. **Varra as grades de timeline** (`overview_timeline_*`) em sequência — atenção máxima ao hook (primeiros 6-8s), mas varra corpo e CTA procurando **mudanças dentro de um mesmo take** (algo derretendo, encolhendo, saindo, sendo lavado).
4. **Dê zoom em resolução cheia** nos frames de qualquer reveal suspeito.
5. Se precisar de mais densidade, re-extraia o intervalo a 15 fps.

### O que mapear (beat a beat)

Para cada beat/cena, anote:

| Campo | O que anotar |
|-------|--------------|
| **Timestamp** | Quando começa/termina |
| **Esqueleto visual** | O que se vê na tela (composição, ação) |
| **Nº de pessoas** | 1 (solo) ou 2+ (tem segunda pessoa? é herói?) |
| **Props** | Objetos em cena (tigela, copo, luvas, livro, modelo anatômico, tanque...) |
| **Fala** | O que é dito (da transcrição) |
| **Função (label)** | HOOK / MECANISMO / RECEITA / PROTOCOLO / RESULTADO / PROVA / UPSELL / CTA |
| **Delta** | O que muda em relação ao take anterior (cor de roupa? tamanho de algo? ângulo?) |

### O que NUNCA deve passar batido

- **Qual é o herói do hook exatamente** (não presuma — é onde mais se erra).
- **Se há segunda pessoa** e qual o papel dela (cliente? é o herói?).
- **O que muda entre os takes** (cor de roupa, tamanho de algo, ângulo).
- **Reveals dentro de um take** (transformações que a extração esparsa perderia).
- **Props que dão credibilidade** (luvas, livro, modelo anatômico, sacolas de mercado).
- **Cenário do original** (pra decidir a adaptação ao cenário do avatar).
- **Onde exatamente algo acontece** (ex.: a água cai NO ponto X, não no Y).

> **Regra dura:** não faça pattern-matching. A primeira leitura de um hook costuma ser a errada. Se houver qualquer ambiguidade sobre o herói, **confirme com o operador antes de seguir.**

---

## FASE 3 — Definição da Variável

Com a estrutura mapeada, defina o que muda:

- **Qual a variável** a ser trocada (o novo ingrediente/produto/problema)?
- Cada beat mantém a **mesma função** com o conteúdo novo?
- Há **congruência** com o avatar escolhido (cenário, gênero, registro, idade)? Aplique a matriz de congruência (documento 02, seção 3.1). Ajuste o ângulo (ex.: "coach que prescreve") sem mexer na estrutura.
- Há **segunda pessoa** que precisa ser mantida ou pode ser removida? (Ex.: no vídeo da Brandon, a segunda pessoa do original — um praticante de medicina tradicional — foi removida porque não cabia no cenário dela, e a autoridade dele já estava codificada no cenário da Brandon.)
- Se for testemunho/transformação **sem variável óbvia**, mantenha 100% fiel e diferencie pelo avatar/cliente.

---

## FASE 4 — Roteiro Final + ORDEM DE ENTREGA

> **REGRA DE ENTREGA OBRIGATÓRIA:** antes de enviar **qualquer** prompt de imagem ou de vídeo ao operador, entregue nesta ordem:
>
> 1. **A transcrição completa** do vídeo modelo (com timestamps, integral, não resumida).
> 2. **O roteiro final quebrado cena a cena**, com: número do take, função do beat, a fala exata em inglês, e a marcação TALKING ou B-ROLL.
> 3. **Só então** os prompts.
>
> **Por quê:** o operador precisa validar a fala e a estrutura ANTES de gastar geração em imagem/vídeo. Prompt gerado em cima de roteiro não aprovado é retrabalho garantido. Este é o ponto de checagem entre a Fase 4 e a Fase 5.

Escreva o roteiro final adaptado, respeitando:

- **Takes de ~8 segundos** cada (quebre falas longas em takes).
- **Sem em dash** (travessão "—"). Use frases curtas.
- **Registro do avatar** (masculino/feminino/caloroso).
- **Keyword sempre `yes`** no CTA (`comment "yes" below` / `type "yes" below`), sobrepondo a palavra do original.
- **Ajustes de congruência** na fala (idade, "coach que prescreve", etc.).
- **Estrutura idêntica** à do original — só a variável muda.

Marque cada take como **TALKING** (avatar fala) ou **B-ROLL** (insert sem rosto falando).

### Checagem do roteiro antes de entregar

- [ ] Estrutura idêntica ao original (só variável mudou)?
- [ ] Nenhuma demonstração virou talking head?
- [ ] Takes ~8s, sem em dash?
- [ ] Keyword `yes` no CTA com follow-gate?
- [ ] Registro/idade/gênero congruentes com o avatar (ângulo coach se preciso)?

---

## FASE 5 — Prompts de Imagem (o frame inicial de cada take)

Para cada take, escreva um prompt de imagem que gera o **frame inicial** (o estado inicial da cena). Detalhes completos no documento 06. Pontos-chave:

- Gera-se **o estado INICIAL** do take, não o meio nem o fim. A transformação acontece depois, na Fase 7 (vídeo).
- **Nunca gere before/durante/depois como imagens separadas de uma transformação dentro do mesmo take** — só o estado inicial. (Exceção: os "estágios" do antes/depois disfarçado, que são takes diferentes — ver documento 02, seção 4.)
- **Zero texto na imagem** (sempre no negative: "no text, no captions, no words on screen").
- A **foto do avatar é a âncora** de identidade/roupa/cenário, mas **não** dita pose/câmera (isso você controla no prompt).
- Junto com os prompts, entregue o **mapa de âncoras**: qual imagem cada take usa como referência e em que ordem gerar. Takes que compartilham um prop derivam do mesmo take aprovado.

> **Regra de escrita:** quando um prompt for quase igual a outro, **NÃO** escreva "igual ao anterior, exceto X". Escreva o prompt **inteiro**, trocando apenas o que muda. Isso evita erro na hora de gerar.

---

## FASE 6 — Geração de Imagem

- Gere no **Nano Banana 2** (volume) ou **Pro** (frames-herói).
- **Siga a ordem de âncoras** do mapa: gere as imagens base primeiro, as derivadas depois.
- **Trave a segunda pessoa primeiro:** se há cliente/segunda pessoa, gere ela primeiro, aprove o rosto, e reuse esse rosto como referência nos outros takes pra manter consistência. Isso é o que faz ou quebra vídeos com duas pessoas.
- **Estágios de transformação** (braço encolhendo, banana, crosta, manequim): gere o estágio 1, aprove, e gere os demais **por edição a partir do estágio 1 original** (nunca em cascata), mantendo enquadramento idêntico.
- **Frames-herói** (hook): gere várias variações até acertar. O hook é o que mais paga; vale o retrabalho.
- Revise cada imagem: o modelo/prop saiu com a **forma certa**? (A IA defaulta pra formas comuns — ver documento 09.)
- Mande o resultado ao operador; compare com o original quadro a quadro antes de aprovar.

---

## FASE 7 — Geração de Vídeo (animar a imagem)

Cada imagem (frame inicial) vira um clipe de ~8s no **Veo 3.1 via Flow** (ou Lite/Lower Priority pra não gastar crédito). Você dá a imagem + um prompt de vídeo. Detalhes no documento 07. Formato:

```
o avatar (homem/mulher) fala em inglês fluente a seguinte frase: "[FALA EXATA DO TAKE]"

o que acontece no vídeo: [ação fiel ao frame, ENXUTA — só o que de fato acontece]

câmera: [movimento simples]

som ambiente: [ambiente + "sem música"]
```

Regras da Fase 7:
- **Takes TALKING** levam a linha `o avatar fala...` com a fala exata.
- **Takes B-ROLL / insert** NÃO levam fala (a locução entra como voz-over na edição). Marque "(sem fala no take)".
- **A fala vai sempre inteira no prompt.**
- **Descrição da ação enxuta:** só o que acontece de fato, sem exagero de ângulo/posição/adjetivo (ajuda a não disparar restrição).
- **"sem música" sempre** no som ambiente.
- Entregue cada prompt com um **título identificador** (ex.: "TAKE 3 — REVEAL HERÓI · crosta desaba e revela os vasos limpos") para facilitar na hora de gerar.

---

## PÓS-PRODUÇÃO (edição final)

- Junte os takes na ordem do roteiro, com **cortes secos** (sem transições — transições matam a ilusão de continuidade nos antes/depois disfarçados).
- Adicione as **legendas grandes** (estilo Captions.ai Prism Pro), palavra por palavra, imitando o estilo/cor do original — inclusive a keyword `yes` no CTA.
- Onde um take foi gerado **sem fala** (b-roll ou take que travou no gerador), adicione a **locução** (gravada ou TTS) + legenda por cima.
- Adicione a **trilha/música** na edição (os prompts de vídeo pedem "sem música" justamente pra você controlar a trilha depois e evitar strike de copyright).
- Exporte **9:16 vertical**.

Próximos documentos: **06 — Prompts de Imagem** e **07 — Prompts de Vídeo**, com os modelos prontos.
