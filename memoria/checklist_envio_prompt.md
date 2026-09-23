---
name: checklist-envio-prompt
description: "CHECKLIST DE ENVIO BLOQUEANTE, todos os angulos (Luigi, 2026-09-22). Bloco A inclui A10-A14 da skill gancho-verbal. Insights do curso Lib Korella (22 abas, 23 Looms, Brand DNA, Hooks Masterclass) viraram 5 blocos de itens: gancho, imagem K, video V, montagem e marca. Nenhum prompt, gancho ou pacote sai para o Luigi sem 100% dos itens aplicaveis aprovados; reprovou, corrige e roda de novo antes de enviar. Toda entrega leva a linha 'Checklist de envio: X/X aprovados' fora dos blocos copiaveis."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 002f42b5-43f4-4b0f-8298-5e42c359e57f
  modified: 2026-09-22T22:43:21.537Z
---

# Checklist de envio: nenhum prompt sai sem 100% aprovado

**Regra do Luigi, 2026-09-22:** os insights tirados dos documentos da Korella (curso Lib Korella:
22 abas, 23 transcrições de Loom, Brand DNA com 3 ângulos, Hooks Masterclass e o documento de
roteiros adaptados) valem para **todos os ângulos** (Korella, FitWell, Auraly e qualquer ângulo
futuro) como **checklist obrigatório de todo prompt enviado**. *"Se não estiver com todos os pontos
aprovados, você nem chega a me enviar o prompt."*

**Why:** o curso mostrou, com números, onde o vídeo de IA perde: gancho genérico (6k contra 150k no
mesmo roteiro), cara de IA, voz trocando de clipe para clipe, pessoa errada falando, avatar
repetido entre contas derrubando o alcance. Regra lembrada de vez em quando não segura isso. Checklist
rodado antes de todo envio segura.

**How to apply:**
1. **Quando rodar:** antes de enviar QUALQUER coisa que vire geração ou publicação: lista de
   ganchos, prompt de imagem `K__`, prompt de vídeo `V__`, pacote completo, prompt avulso ou
   correção de um único prompt. Correção de um prompt roda o checklist naquele prompt inteiro.
2. **Como:** passar item por item. Item que não se aplica vira `N/A` (ex.: selfie num take sem
   selfie). Qualquer item **reprovado** obriga corrigir o prompt e rodar o checklist de novo.
   **Nunca enviar com ressalva**, nunca "envio agora e ajusto depois".
3. **O que o Luigi vê:** uma linha fora dos blocos copiáveis, antes deles:
   `Checklist de envio: X/X aprovados (N/A: ...)`. Nunca com item reprovado.
4. Este checklist **soma** com o `GATE_VISUAL.md` (Partes 1 a 4) e com o `checar_entrega.py`; não
   substitui nenhum dos dois. O linter pega o que é mecânico, o checklist pega o resto.

---

## A · GANCHO (copy e visual do T1, antes de mandar o gancho fiel ou as 10 variações, e reconferido no prompt)

- [ ] **A1 Filtra:** o gancho nomeia o público no primeiro segundo (idade, condição, quem ele é).
- [ ] **A2 Tensão por contradição:** existe um "mas" que não faz sentido. Ex.: *"He was 60, BUT his
  soldier never stood down"*, *"tem 78 e anda como se tivesse 30"*.
- [ ] **A3 O desejo do cliente está dentro da tensão**, não só a curiosidade. Relevância é o valor.
- [ ] **A4 Específico, nunca genérico:** zero "feeling off", "not yourself", "lose weight". Sintoma
  concreto e observável: *"can't walk up the stairs without losing their breath"*, *"lost 220
  pounds"*. Termo duvidoso passa pelo teste *"é assim que o cliente fala? 5 sinônimos melhores"*.
- [ ] **A5 Coerência visual e verbal, sem redundância:** o que a fala ou o texto de tela diz aparece
  na imagem, mas o texto não narra o que a imagem já mostra (imagem = problema, texto = resultado,
  ou o contrário).
- [ ] **A6 Gancho e corpo falam da mesma coisa.** O gancho não promete um tema que o roteiro abandona.
- [ ] **A7 Emoção crua no rosto e na voz** (raiva, frustração, vergonha, espanto). Expressão neutra
  de banco de imagem reprova.
- [ ] **A8 Rodada certa** (`GATE_VISUAL.md` Parte 4, Luigi 2026-09-23). **Validação** (produção nova):
  o gancho é o do modelo, fiel, com cada desvio declarado; aqui refazer o viral igual é o objetivo, e
  os itens de A que obrigariam mudar o gancho do modelo viram `N/A (fiel ao modelo)`. **Variação**
  (só com vídeo já validado): Puzzle com degrau, peça viral preservada, um degrau, HOOK 1 controle,
  uma variável por hook, e aí refazer o vencedor igual reprova.
- [ ] **A9 Autoridade do avatar legível em 3 segundos** (cenário, figurino, postura). Se não lê, refaz.
- [ ] **A10 Teste de troca:** trocando o produto, a frase do gancho morre. Se serve pra qualquer
  produto, é genérica (skill `gancho-verbal`, 2026-09-22; ver [[ganchos-variacao-puzzle]]).
- [ ] **A11 Teste de leitura errada:** a frase não pode ser lida como ronco, treino, tombo, refeição
  ou carinho. Nível 3: estado, contagem, medida ou duração nomeados (pela metáfora da marca na fala).
- [ ] **A12 Sincronia com o roteiro:** o topo do arquivo de ganchos tem tese, sintoma-alvo e banco
  verbal com 5 frases literais; o texto de tela tem no máximo 9 palavras e repete uma frase do banco.
- [ ] **A13 Direção:** quem vence é o sujeito do produto (Korella: ele; FitWell: ela, causa externa;
  Auraly: ela faz o gesto e o universo responde). Mecanismo fica fora do gancho.
- [ ] **A14 Sem frase banida:** sentimental (`I cried`, `you're back`), eufemística (`kept me up all
  night`) ou de enfeite (`his secret`, `what changed`, `the reason`). O `checar_entrega.py` varre.

## B · PROMPT DE IMAGEM (`K__`)

- [ ] **B1 `GATE_VISUAL.md` Partes 1 a 3 aprovadas:** luz neutra, céu com cor e textura, **sem
  golden hour**, sem tom quente, herói colado na lente, 2 ou 3 âncoras de fundo, sem blur, trecho de
  realismo fechando o prompt.
- [ ] **B2 Composição partindo do real:** a posição e o enquadramento vêm do print do 1º frame do
  vídeo modelo (anexo junto com a âncora). Prompt sozinho não reproduz posição.
- [ ] **B3 Rosto nítido e limpo:** sem sombra dura no rosto; janela nunca estourada (`the outside is
  clearly visible through the window`); céu nunca branco.
- [ ] **B4 Fundo crível e sem poluição:** nada que o olho estranhe como IA, nenhum objeto inventado
  sem função. Referência do curso: festival lotado ao fundo reprova, fundo isolado aprova.
- [ ] **B5 Roupa que passa na política:** pele demais trava o Flow. Quando houver risco, `fully
  covered clothing` descrito no positivo.
- [ ] **B6 K de fala com boca entreaberta:** `caught mid-sentence, lips naturally parted, animated
  expression`.
- [ ] **B7 Sinal de EUA:** bandeira discreta e visível sempre; cenário americano icônico quando couber.
- [ ] **B8 Avatar varia por vídeo, nunca por conta:** muda roupa, fundo ou detalhe entre vídeos da
  mesma conta; **o mesmo rosto nunca roda em duas contas** (violação de conteúdo original).
- [ ] **B9 Sem figura médica explícita no AVATAR que vende:** nada de jaleco, estetoscópio, crachá
  ou "Dr." no avatar ou na autoridade que recomenda o nosso produto. Médico como avatar dá banimento
  no link-in-bio (curso, jul/2026). ✅ **Médico como personagem de cena é liberado** (Luigi,
  2026-09-23), desde que não seja quem vende ou recomenda o produto: ex. o médico que falha no
  movie style de venda (*"your labs look fine"*).
- [ ] **B10 Autossuficiente e no formato do Flow:** `K__` sozinho na linha, prompt completo, sem
  texto auxiliar, sem depender de outro prompt.

## C · PROMPT DE VÍDEO (`V__`)

- [ ] **C1 A fala cabe em 8 s sem acelerar:** 13 a 29 palavras, de preferência 1 ou 2 frases
  inteiras, cópia literal do roteiro.
- [ ] **C2 Voz descrita no prompt, para CADA personagem que fala** (Luigi, 2026-09-23): timbre,
  idade aparente, sotaque e a entonação/emoção daquela fala (enthusiasm, anger, urgency). Voz neutra
  sai robótica. Personagem que fala em mais de um clipe usa a MESMA descrição de timbre em todos os
  V (a emoção muda por fala, o timbre não), porque é o prompt que segura a voz, não a edição.
- [ ] **C3 Quem fala está escrito** quando há mais de uma pessoa em quadro, e quem cala também
  (`the man behind stays silent`). Pessoa errada falando é o bug nº 1 do Veo.
- [ ] **C4 Selfie:** `the hand holding the phone never moves; only the other hand gestures`.
- [ ] **C5 Frase curta repetida ganha palavras** (ex.: "High cortisol. High cortisol." sozinho trava
  a geração).
- [ ] **C6 Cena atuada com várias pessoas:** câmera `moves as if someone from the audience is
  filming`, com reação e troca de plano. Talking head segue fixo ou handheld leve.
- [ ] **C7 Motion control:** vídeo de referência enviado **sem som** (com música trava por política)
  e o prompt diz `use the background from the image`.
- [ ] **C8 Os 5 blocos da Fase 7** presentes, `sem música` no som ambiente.

## D · MONTAGEM (seção de CapCut da entrega, fora dos blocos)

- [ ] **D1 Sem Voice Changer na montagem.** ♻️ A regra antiga (passar o vídeo inteiro no
  ElevenLabs com a voz fixa do avatar) foi **retirada pelo Luigi em 2026-09-23**. A consistência de
  voz agora vem do prompt de vídeo (item C2). D1 confere só que a seção de CapCut não manda usar
  Voice Changer.
- [ ] **D2 Zero tempo morto:** todo clipe começa já falando; `Isolate Voice / Keep Vocal` no áudio.
- [ ] **D3 Música só no corpo,** nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do
  TikTok (risco de vídeo mutado).
- [ ] **D4 Rótulo pequeno de conteúdo gerado por IA** (`AI-generated` ou `Synthetic performer`) num
  canto do vídeo.
- [ ] **D5 Clipes numerados na ordem** (1, 2, 3...) para a montagem não embaralhar.

## E · MARCA (o princípio é universal, a lista é de cada ângulo)

- [ ] **E1 Vocabulário proibido da marca varrido** em fala, texto de tela e prompt. Korella:
  `mood`, `calm`, `calmer`, `serotonin`, `dopamine`, `flatness`, `happy`, `feeling better`,
  `erectile dysfunction`, e no ângulo rosto `skincare`, `glow`, `moon face`; no ângulo próstata `BPH`,
  `incontinence`. FitWell e Auraly: as travas já escritas em [[angulo2-copy-fitywell]] e
  [[angulo3-copy-auraly]].
- [ ] **E2 Uma única raiz ou mecanismo revelado por vídeo.** Na Korella é sempre cortisol; o resto
  (testosterona, fluxo, inflamação) entra só como efeito.
- [ ] **E3 Um único resultado final e uma única emoção dominante** conduzem o roteiro.
- [ ] **E4 Nenhum substantivo de sintoma repetido em sequência** no mesmo vídeo (regra de variedade
  do Brand DNA).

---

Fonte: curso Lib Korella (Google Doc de 22 abas, lido na íntegra em 2026-09-22, com as 23
transcrições de Loom e os documentos ligados). Relacionado: [[realismo-anti-cara-de-ia]],
[[checklist-composicao-visual]], [[ganchos-variacao-puzzle]], [[prompts-video-fase7]],
[[regras-universais]], [[autocobranca-no-canal-repetido]].
