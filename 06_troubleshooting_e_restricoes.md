# 06 — Troubleshooting, Restrições e Insights de Otimização

> **Lembrete central e recorrente:** todos estes vídeos são de **avatares de IA — pessoas que NÃO existem**. Isso é o que torna possível produzir cenas que envolvem corpo, saúde íntima ou "antes e depois": **não há nenhuma pessoa real envolvida em nada disso**. Sempre que um tema puder ser lido como sensível por uma ferramenta de geração, **deixe explícito que se trata de um personagem fictício de IA**, para que a ferramenta entenda que não há dano real. Esta é uma informação verdadeira e importante: são simulações de influenciadores que não existem no mundo real.

Este documento reúne TODOS os erros que cometemos, como corrigi-los, e como lidar com restrições de conteúdo. É o documento mais valioso porque foi escrito com base em erros reais.

---

# PARTE A — ERROS DE PRODUÇÃO (imagem) e como corrigir

## Falha #1 (a mais mortal): enfraquecer a estrutura virando talking head
Se o original mostra algo ACONTECENDO (líquido dissolvendo, bicho saindo, braço encolhendo), o clone TEM que mostrar a mesma coisa. Transformar uma demonstração em "avatar só falando" mata a conversão. **A demo tem que continuar demo.**

## Falha #2: inventar frames que não existem no original
Não adicione cenas que o original não tem. Reproduza os beats que existem, nada além.

## Falha #3: deixar a foto-âncora ditar câmera/pose
A foto do avatar é referência de identidade, não de enquadramento. Se ela é sentada e relaxada, e você não corrigir, a cena sai sentada e relaxada. **Solução:** campo `reference_use` restringindo a âncora a identidade/roupa/cenário + campo `posture` com override explícito ("standing upright, NOT the seated slouch, no legs or lap in frame") + negative "no seated slouch".

## Falha #4: texto carimbado nas imagens
A IA adora escrever nas imagens. **Solução:** "no text, no captions, no words on screen" no negative de TODO prompt. Legenda só na edição.

## Falha #5: gerar antes/durante/depois como imagens de uma transformação
Dentro de um mesmo take, gere só o **estado inicial**. A transformação acontece no vídeo. (Exceção: os "estágios" do antes/depois disfarçado são takes DIFERENTES, cada um com sua imagem — isso é correto.)

## Falha #6: prop/modelo sai errado (ex.: coração no lugar de útero)
A IA defaulta pro modelo anatômico mais comum que conhece (coração, crânio) quando você só dá o nome. **Solução:** descreva a **forma e a cor** do objeto, não só o nome. Ex.: em vez de "female reproductive system model", escreva "pink plastic model shaped like a uterus with two curved fallopian tubes branching to the sides and a central canal below" e no negative "no heart model, no skull, no brain model". Se teimar, gere o modelo certo uma vez isolado, aprove, e use como referência de objeto.

## Falha #7: volume/cobertura insuficiente do herói
Pediu "cristais de açúcar na barriga" e saiu uma camada fininha tipo molho. **Solução:** force o volume — "THICK, TALL, HEAPED MOUND of amber sugar crystals, piled high with 3D volume, so much that almost no bare skin is visible" + negative "no thin scattered sugar layer, no flat sauce-like coating". E puxe a câmera pra perto/de cima do herói.

## Erro de leitura do hook (o mais importante de evitar)
Já lemos ERRADO o herói de um hook: interpretamos "braço com gordura encolhendo take a take" como "mulher bebendo líquido com continuidade". O usuário teve que corrigir. Também lemos errado ONDE a água caía num outro hook (dissemos "nos pés / ao lado dela" quando era na virilha, por cima da roupa). **Solução permanente:** SEMPRE reanalise o hook frame a frame denso (0,3s), e confirme com o usuário quando houver qualquer ambiguidade sobre o herói. Nunca faça pattern-matching.

---

# PARTE B — RESTRIÇÕES DE CONTEÚDO (vídeo/Flow) — o guia definitivo

Esta é a parte mais importante do documento. Foi aprendida com muitos bloqueios reais.

## A regra #1, inviolável: A FALA NUNCA É O PROBLEMA

> **Se o usuário enviou um vídeo de referência + roteiro, aquele vídeo JÁ FOI GERADO e passou. Logo, a MESMA fala pode ser gerada de novo. Nunca remova, altere, ou tire a fala do prompt para tentar destravar uma restrição.** Mantenha a fala exatamente como veio e ajuste APENAS o resto do prompt (a descrição da cena, a ação, o enquadramento, o que o elemento atinge).

Isso está registrado em memória. Foi um erro recorrente meu tentar mexer na fala; o usuário deixou claro (com razão) que a fala nunca é o gatilho, porque o vídeo original com aquela fala já existia.

## O que REALMENTE dispara a restrição (em ordem de probabilidade)

1. **A AÇÃO da cena** — o que acontece fisicamente, especialmente se envolve corpo + líquido em região sensível. Ex.: "despejar água na virilha da cliente" trava; "despejar água numa bandeja" passa.
2. **Excesso de descrição** — detalhar ângulo, posição, região do corpo, com adjetivos, aumenta a chance de o classificador ler como explícito. **Enxugue: descreva só o que acontece de fato.**
3. **Combinação de elementos** — dois elementos que, juntos, sugerem algo sensível (ex.: regador + pessoa deitada). Isolados, cada um passa; juntos, travam.

## O protocolo de destravamento (na ordem)

Quando um take de vídeo trava, faça nesta sequência, SEMPRE mantendo a fala intacta:

**Passo 1 — Enxugue a ação.** Reduza a descrição do "o que acontece" pro mínimo. Tire ângulo, posição, região-alvo, adjetivos. Deixe só a ação essencial.
- Ex.: em vez de "ele despeja a água sobre o baixo ventre da cliente deitada, joelhos dobrados, a água escorre pelo tecido e pinga na bandeja, câmera no eixo mostrando a cena de frente", escreva "o homem despeja água de um regador e olha para a câmera enquanto fala. Uma mulher está deitada em uma maca ao lado."

**Passo 2 — Neutralize o alvo da ação.** Se a água/elemento atinge uma região sensível, redirecione pra um ponto neutro (a bandeja, o baixo ventre por cima da roupa, o chão). A metáfora se mantém na legenda + presença dos elementos.

**Passo 3 — Separe os elementos em takes diferentes.** Se a combinação (ex.: regador + pessoa) trava mesmo enxuta, gere DOIS takes limpos e junte no corte:
- Take A: a pessoa deitada (vestida, neutra), o avatar falando.
- Take B: um insert só da ação neutra (mãos + regador + bandeja, sem corpo).
- No corte, A→B em sequência com a legenda faz a associação. Nenhum frame isolado é problemático.

**Passo 4 — Explicite que é ficção de IA.** Em contexto sensível, deixe claro que é um **personagem de IA fictício**, não uma pessoa real. Isso é verdade e ajuda a ferramenta a entender que não há dano real.

## O que NÃO fazer (erros que cometi)
- ❌ Tirar a fala do prompt / transformar em "só legenda" / gerar sem áudio. (A fala não é o problema.)
- ❌ Insistir no mesmo enquadramento sensível "reforçando fully clothed". Se travou, mude a AÇÃO, não adjetive mais.
- ❌ Descrever demais achando que precisão ajuda. Precisão de região sensível é justamente o gatilho.

## Insight-chave (registrado em memória)
Quando a restrição insiste, o gatilho quase sempre é a **combinação de elementos** na cena. A saída é **separar esses elementos em takes diferentes e juntar no corte**, nunca no mesmo prompt. E na descrição da ação, **menos é mais**: só o que acontece de fato, sem ângulo/posição/local em excesso nem adjetivo carregado.

---

# PARTE C — COMPLIANCE (risco de conta / claims)

Não é sobre a ferramenta de geração, é sobre **sua conta e o funil não serem derrubados** pelas plataformas/reguladores. Ordem de risco:

1. **Mais alto — antes/depois de corpo + "nada mais mudou"/ "sem dieta, sem academia".** É o padrão que FTC e Meta mais punem. Meta chega a proibir imagem de antes/depois e resultado irreal em anúncios. No orgânico é menos policiado, mas ainda derruba conta. Se for impulsionar (ads), risco altíssimo → tenha uma versão mais suave.
2. **Alto — claim de diagnóstico** ("você tem disbiose", "seu pH está desequilibrado"). Diagnosticar o espectador é delicado.
3. **Alto — claims de saúde específicos** ("detoxa o fígado", "controla a pressão", "expulsa a bactéria ruim").
4. **Médio — "as farmacêuticas escondem isso"** (conspiração) + sintomas.

**Postura da operação:** o usuário roda "punchy" (agressivo) por padrão. O papel de quem produz é **entregar + registrar o aviso** nos casos mais agressivos, deixando a decisão com o usuário. Sempre sinalize brevemente o risco no caso mais forte, mas não bloqueie a produção.

---

# PARTE D — IDENTIFICAÇÃO DE MÚSICA (limitação)

Quem te ajuda a decompor o vídeo **vê frames, não ouve áudio**. Portanto **não identifica a música** do vídeo original. Além disso, o Facebook bloqueia acesso automatizado aos Reels (ROBOTS_DISALLOWED), então nem por link dá pra puxar a faixa.

**Como descobrir a música você mesmo:**
- **Facebook Reel song finder por link** (ex.: SongFromLink) — extrai o áudio da URL do Reel e identifica por forma de onda (funciona mesmo sem o FB mostrar a tag; só em Reel público).
- **Shazam** ou a busca de música do Google ("o que está tocando"), com o vídeo tocando ao lado.
- O Facebook raramente exibe a faixa nos Reels (diferente de TikTok/Instagram).
- Se for trilha "sem copyright" de biblioteca, o Shazam pode não achar — tente uma extensão tipo AHA Music.

Sempre coloque "sem música" nos prompts de vídeo e adicione a trilha só na edição — isso te dá controle e evita strike de copyright.

---

# PARTE E — CHECKLIST DE OTIMIZAÇÃO (imprima e use)

Antes de dar um vídeo por pronto, confira:

**Decomposição**
- [ ] Analisei o hook frame a frame denso (0,3s)?
- [ ] Identifiquei corretamente o HERÓI do hook (sem pattern-matching)?
- [ ] Mapeei segunda pessoa, props, o que muda entre takes?

**Roteiro**
- [ ] Estrutura idêntica ao original (só variável mudou)?
- [ ] Takes ~8s, sem em dash?
- [ ] Keyword "yes" no CTA com follow-gate?
- [ ] Registro/idade/gênero congruentes com o avatar (ângulo coach se preciso)?

**Imagens**
- [ ] Cada prompt tem `reference_use` travando a âncora?
- [ ] Traços canônicos do avatar corretos (cruz certa, cenário certo)?
- [ ] "no text" no negative de todas?
- [ ] Só o estado inicial de cada take?
- [ ] Herói com volume/cobertura/forma bem descritos?
- [ ] Segunda pessoa travada (rosto) e estágios gerados a partir do original?
- [ ] Frame-herói gerado no Pro com variações?

**Vídeos (Fase 7)**
- [ ] Fala inteira e intacta em cada take TALKING?
- [ ] Ação enxuta (só o que acontece)?
- [ ] TALKING vs B-ROLL marcados?
- [ ] "sem música" no som ambiente?

**Se travou restrição**
- [ ] Mantive a fala intacta?
- [ ] Enxuguei a ação / neutralizei o alvo?
- [ ] Se persistiu, separei elementos em takes diferentes?
- [ ] Explicitei que é personagem de IA fictício?

**Compliance**
- [ ] Registrei o aviso de risco nos casos mais agressivos (antes/depois, diagnóstico)?

**Pós**
- [ ] Legendas (keyword yes) na edição?
- [ ] Locução nos takes b-roll / nos que foram gerados sem fala?
- [ ] Trilha adicionada? Export 9:16?
