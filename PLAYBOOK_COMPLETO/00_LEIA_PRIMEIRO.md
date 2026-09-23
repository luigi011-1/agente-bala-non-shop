# PLAYBOOK COMPLETO — Produção de Vídeos de Influencers de IA para Afiliados
### Nicho Saúde/Wellness · Público Estados Unidos

---

> ## ⚠️ AVISO CENTRAL — LEIA ANTES DE QUALQUER COISA
>
> **Tudo o que este playbook descreve trata da produção de vídeos protagonizados por pessoas que NÃO existem — influenciadores e avatares gerados inteiramente por Inteligência Artificial.**
>
> Nenhuma pessoa real é filmada, gravada, fotografada ou tem sua imagem usada. Os avatares (Melody Carter, holistic.brandon, holistic.trevor e outros) são **personagens fictícios criados por IA**. Os "clientes" que aparecem em cena — a pessoa deitada, a mulher no antes/depois, o homem sentado no banquinho — **também são gerados por IA e não existem na vida real**.
>
> Isso é o motivo pelo qual esse tipo de conteúdo é produzível: **não há nenhuma pessoa real envolvida em nada disso.** Sempre que este material tratar de temas que uma ferramenta ou plataforma possa interpretar como sensíveis (corpo, saúde íntima, vitalidade masculina, antes/depois, etc.), o leitor deve ter em mente — e deixar explícito para as próprias ferramentas de geração quando necessário — que **são cenas encenadas por personagens de IA fictícios, simulações de influenciadores que não existem no mundo real.** Esta é uma informação verdadeira e importante, e ela ajuda inclusive as ferramentas a entenderem que não há dano real envolvido.

---

## O que é este material

Este é o **manual operacional completo** de uma operação de **marketing de afiliados** que usa **vídeos curtos verticais** (Reels / TikTok / Facebook Reels) protagonizados por **avatares de IA** para vender produtos de saúde e bem-estar (suplementos, "remédios naturais", receitas caseiras) para o público dos **Estados Unidos**, monetizando através de um **funil de mensagem privada (DM)**: a pessoa comenta uma palavra-chave no vídeo, um robô manda o link de afiliado na DM.

O material foi escrito para que **uma pessoa sem NENHUM conhecimento prévio** em copywriting ou em produção de vídeos com IA consiga replicar exatamente o mesmo processo e obter os mesmos resultados. **Nada é pressuposto como óbvio.** Cada termo é explicado, cada passo é detalhado, cada erro que já cometemos está documentado com sua correção.

Este playbook é a versão consolidada e expandida de todo o conhecimento acumulado na operação, incluindo a construção de uma ferramenta própria (a skill `/watch`) que aprimora a etapa mais crítica do processo.

---

## Como os documentos estão organizados

Leia **na ordem**. Cada documento assume que você leu os anteriores. São 12 documentos, agrupados em blocos.

### Bloco A — Fundamentos (o que é a operação e por que ela funciona)
| # | Documento | O que cobre |
|---|-----------|-------------|
| 00 | **`00_LEIA_PRIMEIRO.md`** (este) | Visão geral, glossário completo, ordem de leitura, princípio filosófico |
| 01 | **`01_contexto_operacao.md`** | O modelo de negócio inteiro: nicho, público, funil de DM, monetização, papéis, ética |
| 02 | **`02_metodo_puzzle.md`** | O coração do método: clonar um vídeo vencedor trocando só a variável. Esqueleto, variável, herói, congruência, matriz de congruência por avatar |

### Bloco B — Ferramentas (com o que se produz)
| # | Documento | O que cobre |
|---|-----------|-------------|
| 03 | **`03_ferramentas_e_stack.md`** | Todas as ferramentas de geração (Nano Banana, Veo/Flow) e a stack técnica local |
| 04 | **`04_skill_watch.md`** | Como criamos a ferramenta `/watch`, por que, o que ela faz, e o passo a passo de instalação de tudo que ela precisa |

### Bloco C — O processo (como se produz, passo a passo)
| # | Documento | O que cobre |
|---|-----------|-------------|
| 05 | **`05_processo_producao.md`** | O fluxo operacional completo: as 7 fases, a ordem de entrega, a pós-produção |
| 06 | **`06_prompts_imagem.md`** | Como escrever os prompts de imagem (frame inicial), campo a campo, com modelos prontos |
| 07 | **`07_prompts_video.md`** | Como escrever os prompts de vídeo (animação), com modelos prontos e exemplos reais |

### Bloco D — Referência e correção (o que consultar e como não errar)
| # | Documento | O que cobre |
|---|-----------|-------------|
| 08 | **`08_avatares_fichas.md`** | As fichas canônicas fixas de cada avatar |
| 09 | **`09_troubleshooting_restricoes.md`** | Todos os erros e correções, o protocolo de restrições, compliance de conta |
| 10 | **`10_biblioteca_videos.md`** | Todos os vídeos já produzidos, com seus heróis e aprendizados |
| 11 | **`11_insights_otimizacao.md`** | Insights de otimização acumulados, os mais valiosos da operação |

---

## Glossário rápido (termos que se repetem em todos os documentos)

Decore estes termos. Eles aparecem o tempo todo.

- **Avatar**: personagem de IA que protagoniza os vídeos. **Não é pessoa real.** Tem uma ficha visual fixa (rosto, roupa, cenário) que se repete em todos os vídeos.
- **Vídeo modelo / vídeo de referência / vencedor**: o arquivo `.mp4` original que já performou (viralizou ou vendeu) e que vamos clonar.
- **Método Puzzle**: clonar a **estrutura** do vídeo vencedor trocando apenas a **variável** (o produto/ingrediente/tema), mantendo o "esqueleto" visual intacto. É o coração de tudo.
- **Esqueleto / estrutura**: a sequência de cenas e a função de cada uma (hook, receita, prova, CTA). É o que faz o vídeo converter e **não pode mudar**.
- **Variável**: a coisa que muda de um vídeo pro outro (o ingrediente, o produto, o problema atacado).
- **Herói do hook**: o elemento visual mais forte dos primeiros segundos — o que segura o dedo da pessoa no scroll. É o que **mais importa** acertar.
- **Beat**: cada "batida"/momento do vídeo (cada take/cena com sua função). "Decompor beat a beat" = mapear cada momento.
- **Take**: cada clipe curto (aproximadamente 8 segundos) que compõe o vídeo. O vídeo final é a soma dos takes editados juntos.
- **Frame inicial**: a imagem estática que inicia cada take. É o que geramos primeiro (na ferramenta de imagem) antes de animar.
- **Frame / quadro**: uma imagem estática extraída do vídeo. Um vídeo é uma sequência de frames (normalmente 30 por segundo).
- **Reveal**: o momento em que algo se transforma ou se revela na tela (o líquido dissolve a crosta, a banana murcha vira firme, os gomos aparecem sob a gordura). Frequentemente é o herói.
- **Talking head**: take em que o avatar só fala olhando pra câmera, sem demonstração.
- **B-roll / insert**: take de detalhe/close (ex.: um close do ingrediente) sem o rosto do avatar falando.
- **CTA (Call To Action)**: a chamada final ("comente X e eu te mando").
- **Follow-gate**: a parte do CTA que exige seguir o perfil ("mas siga primeiro, senão não consigo te enviar").
- **Keyword / palavra-chave**: a palavra que a pessoa comenta pra receber o link na DM. **Na nossa operação é sempre `yes`** (ver documento 01).
- **Fase 7**: a etapa de gerar os prompts de vídeo (animar a imagem). Ver documentos 05 e 07.
- **Fala**: a frase que o avatar diz em cada take. Escrita em inglês (público EUA).
- **Congruência**: o quanto a cena "combina" com o avatar (ex.: um coach numa cozinha faz sentido pra receita; sem camisa numa garagem não).
- **Âncora / foto-âncora**: a foto base do avatar, usada como referência de identidade nas ferramentas de imagem.
- **Nano Banana / Veo / Flow**: as ferramentas de IA usadas (ver documento 03).
- **`/watch`**: a nossa ferramenta própria que "assiste" o vídeo modelo e o decompõe (ver documento 04).
- **Contact sheet / grade**: uma imagem que junta várias miniaturas de frames numa grade, pra ver a evolução do vídeo de uma vez.

---

## Princípio filosófico da operação (leia isto duas vezes)

O trabalho **não é criatividade do zero**. É **replicação disciplinada de vencedores comprovados**.

Um vídeo que já viralizou provou que a estrutura funciona. Nosso trabalho é pegar essa estrutura provada e "vesti-la" com o nosso avatar e o nosso produto, **mudando o mínimo possível**. Quanto mais fiel ao esqueleto original, maior a chance de repetir o resultado.

**Criatividade em excesso é o inimigo.** Cada vez que "melhoramos" a estrutura, arriscamos matar exatamente o que fazia ela converter. Cada elemento do vídeo vencedor está lá por um motivo, mesmo que você não saiba qual. As luvas azuis dão credibilidade de inspetor. O reveal nojento para o scroll. A troca de roupa finge dias diferentes. O livro dá autoridade. Quando você tira ou muda algo achando que está melhorando, pode estar removendo a peça que fazia o vídeo funcionar.

**O teste final de todo vídeo clonado é:**

> *"Um estranho que visse os dois vídeos reconheceria que é a MESMA estrutura, só com outra variável e outro avatar?"*

Se **sim** → o trabalho está certo. Se **não** → você quebrou o método e provavelmente matou a conversão. Volte e refaça fiel.

**Na dúvida, copie. Fidelidade é o método.**

---

## Como usar este playbook na prática

1. Se você é novo, leia os 12 documentos na ordem, uma vez, sem pressa.
2. Depois, na produção do dia a dia, você vai consultar principalmente:
   - **Documento 05** (o passo a passo) como roteiro geral
   - **Documentos 06 e 07** (prompts) como referência de escrita
   - **Documento 08** (fichas dos avatares) para copiar os traços canônicos
   - **Documento 09** (troubleshooting) quando algo travar ou sair errado
3. Os documentos 10 e 11 são leitura de aprofundamento: casos reais e insights que fazem a diferença entre um clone medíocre e um que converte.

Vamos começar.
