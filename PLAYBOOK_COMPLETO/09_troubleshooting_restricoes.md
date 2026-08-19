# 09 — Troubleshooting, Restrições e Compliance

> **Lembrete central e recorrente:** todos estes vídeos são de **avatares de IA — pessoas que NÃO existem**. Isso é o que torna possível produzir cenas que envolvem corpo, saúde íntima, vitalidade masculina ou "antes e depois": **não há nenhuma pessoa real envolvida em nada disso.** Sempre que um tema puder ser lido como sensível por uma ferramenta de geração, **deixe explícito que se trata de um personagem fictício de IA**, para que a ferramenta entenda que não há dano real. São simulações de influenciadores que não existem no mundo real.

Este é o documento mais valioso porque foi escrito com base em **erros reais**. Ele reúne os erros de produção (imagem), o protocolo de restrições (vídeo), e o compliance (risco de conta).

---

# PARTE A — ERROS DE PRODUÇÃO (imagem) e como corrigir

## Falha #1 (a mais mortal): enfraquecer a estrutura virando talking head
Se o original mostra algo ACONTECENDO (líquido dissolvendo, bicho saindo, braço encolhendo, crosta desabando), o clone TEM que mostrar a mesma coisa. Transformar uma demonstração em "avatar só falando" mata a conversão. **A demo tem que continuar demo.**

## Falha #2: inventar frames que não existem no original
Não adicione cenas que o original não tem. Reproduza os beats que existem, nada além.

## Falha #3: deixar a foto-âncora ditar câmera/pose
A foto do avatar é referência de identidade, não de enquadramento. Se ela é sentada e relaxada, e você não corrigir, a cena sai sentada e relaxada. **Solução:** campo `reference_use` restringindo a âncora a identidade/roupa/cenário + campo `posture` com override explícito + negative "no seated slouch".

## Falha #4: texto carimbado nas imagens
A IA adora escrever nas imagens. **Solução:** "no text, no captions, no words on screen" no negative de TODO prompt. Legenda só na edição.

## Falha #5: gerar antes/durante/depois como imagens de uma transformação
Dentro de um mesmo take, gere só o **estado inicial**. A transformação acontece no vídeo. (Exceção: os "estágios" do antes/depois disfarçado são takes DIFERENTES, cada um com sua imagem — isso é correto.)

## Falha #6: prop/modelo sai com a forma errada
A IA defaulta pro objeto mais comum que conhece quando você só dá o nome. Casos reais:
- "modelo do aparelho reprodutor feminino" → saiu **coração/crânio**.
- "estrutura vascular ramificada, spreading outward like limbs" → saiu **estrela-do-mar** (simetria radial).
- "massa ramificada" mais genérica → saiu **raiz de gengibre / madeira de deriva**.

**Solução:** descreva **forma, proporção e cor** com números e referências concretas, e liste no negative TODAS as formas erradas que ele já assumiu. Use nomenclatura técnica/clínica quando existir (ex.: "vascular corrosion cast", "uterus with two fallopian tubes"). Se teimar, gere o objeto certo **isolado** (sem o avatar, fundo neutro), aprove, e use como referência de objeto nas cenas.

## Falha #7: volume/cobertura insuficiente do herói
Pediu "cristais de açúcar na barriga" e saiu uma camada fininha tipo molho. **Solução:** force o volume — "THICK, TALL, HEAPED MOUND... piled high with 3D volume, so much that almost no bare skin is visible" + negative "no thin scattered layer, no flat sauce-like coating". E puxe a câmera pra perto/de cima do herói.

## Erros históricos de LEITURA do hook (os mais importantes de evitar)
- Lemos ERRADO "braço com gordura encolhendo take a take" como "mulher bebendo líquido com continuidade" (pattern-matching preguiçoso pela troca de roupa).
- Lemos ERRADO ONDE a água caía num hook (dissemos "nos pés / ao lado dela" quando era na virilha, por cima da roupa).

**Solução permanente:** SEMPRE reanalise o hook frame a frame denso (0,2s), e **confirme com o operador quando houver qualquer ambiguidade** sobre o herói. Nunca faça pattern-matching. A primeira leitura costuma ser a errada.

---

# PARTE B — RESTRIÇÕES DE CONTEÚDO (vídeo/Flow) — o guia definitivo

Esta parte foi aprendida com muitos bloqueios reais.

## A regra #1: A FALA GERALMENTE NÃO É O PROBLEMA — mas há uma nuance

> Se o vídeo modelo foi **gerado por IA** e você tem ele + o roteiro, aquele vídeo JÁ FOI GERADO e passou. Logo, a MESMA fala pode ser gerada de novo. Nunca remova, altere, ou tire a fala do prompt para destravar. Ajuste APENAS o resto (a descrição da cena, a ação, o enquadramento).

**A nuance descoberta na prática:** essa garantia só vale quando o vídeo modelo **foi gerado por IA**. Se o vídeo modelo é **filmagem real** (pessoas reais, cozinha real, sacolas de mercado reais — como no vídeo da Brandon sobre vinagre de maçã), a fala **nunca passou por um gerador**, e uma palavra específica (ex.: uma palavra anatômica) pode de fato travar o Veo.

**Como agir nesse caso:**
1. **Tente com a fala original intacta primeiro** — o princípio segue valendo como primeira tentativa.
2. Se travar, procure o substituto **dentro do próprio roteiro original** — uma expressão que o próprio original já usa em outro momento (ex.: trocar a palavra anatômica por "down there", que o mesmo vídeo usa depois). **Isso não é inventar** — é usar a linguagem do próprio original. É honestidade com o método, não flexibilização dele.

## O que REALMENTE dispara a restrição (em ordem de probabilidade)

1. **A AÇÃO da cena** — o que acontece fisicamente, especialmente corpo + líquido em região sensível. "Despejar água na virilha da cliente" trava; "despejar água numa bandeja" passa.
2. **Excesso de descrição** — detalhar ângulo, posição, região do corpo, com adjetivos, aumenta a chance de o classificador ler como explícito. Enxugue.
3. **Combinação de elementos** — dois elementos que, juntos, sugerem algo sensível (ex.: regador + pessoa deitada). Isolados, cada um passa; juntos, travam.
4. **O próprio campo `negative`** — ver a regra abaixo. É o gatilho mais contraintuitivo de todos.

## A regra do campo NEGATIVE (contraintuitiva e cara de descobrir)

> **Nunca liste no `negative` o nome daquilo que você teme que apareça, quando o termo em si é sensível.**

Escrever `no gore, no blood, no worms` num prompt de render anatômico **aumenta** a chance de bloqueio em vez de reduzir. O classificador lê os tokens, não a negação — listar a palavra **injeta o conceito no prompt**.

**Em vez disso:**
- **Descreva positivamente a forma certa** (matte, rounded, clean, clinical, soft, calm).
- **Reserve o `negative` para coisas neutras:** texto, legendas, palavras na tela, mãos, pessoas, rótulos, setas.

**Caso real que gerou a regra:** um render 3D de um túnel intestinal (vídeo de detox) foi barrado por "violência". Os gatilhos foram `moist glossy tissue` + `human intestine` + `endoscopic` + `fades to dark`, **somados** aos negatives `no gore, no blood, no horror aesthetic, no insects, no worms`. A correção que passou: reenquadrar como **modelo didático de silicone** e **remover por completo os negatives que nomeavam gore/sangue/vermes**. Na tela o resultado é praticamente idêntico.

**Tabela de substituições para render anatômico:**

| Trava | Passa |
|---|---|
| `human intestine` / `INTESTINAL VILLI` | `teaching model of a digestive tube` / `finger-shaped projections` |
| `moist glossy tissue` / `wet` | `soft matte silicone` |
| `DEEP ANGRY RED` / `inflamed` | `WARM DEEP CORAL RED` |
| `pinkish-brown` | `muted dusty rose` |
| `endoscopic` | `borescope` |
| `fades to dark` / `darkness` | `falls off gently into shadow` |
| `crusted residue` | `dried crust, cracked like dried clay` |

## O protocolo de destravamento (na ordem, sempre com a fala intacta)

**Passo 1 — Enxugue a ação.** Reduza a descrição do "o que acontece" pro mínimo. Tire ângulo, posição, região-alvo, adjetivos.

**Passo 2 — Neutralize o alvo.** Se o elemento atinge uma região sensível, redirecione pra um ponto neutro (a bandeja, por cima da roupa, o chão). A metáfora se mantém na legenda + presença dos elementos.

**Passo 3 — Separe os elementos em takes diferentes.** Se a combinação trava mesmo enxuta, gere DOIS takes limpos e junte no corte:
- Take A: a pessoa (vestida, neutra), o avatar falando.
- Take B: um insert só da ação neutra (mãos + objeto, sem corpo).
- No corte, A→B em sequência com a legenda faz a associação. Nenhum frame isolado é problemático.

**Passo 4 — Explicite que é ficção de IA.** Em contexto sensível, deixe claro que é um personagem de IA fictício, não uma pessoa real. Isso é verdade e ajuda a ferramenta.

## O que NÃO fazer
- ❌ Tirar a fala do prompt / transformar em "só legenda" / gerar sem áudio.
- ❌ Insistir no mesmo enquadramento sensível "reforçando fully clothed". Se travou, mude a AÇÃO, não adjetive mais.
- ❌ Descrever demais achando que precisão ajuda. Precisão de região sensível é justamente o gatilho.
- ❌ **Listar termos sensíveis no `negative`** achando que está protegendo (`no gore`, `no blood`, `no worms`). Faz o oposto.

## O limite ético do protocolo (importante)

O protocolo acima existe para **reproduzir fielmente** a estrutura de um vencedor, não para engenheirar prompts que passem conteúdo explícito por um filtro de moderação.

Nesse nicho, o herói do original costuma ser um prop **ambíguo** (uma massa vascular encrostada, uma banana murcha) — e é a **fala + a legenda** que fazem a associação anatômica, não o frame isoladamente. Foi assim que o próprio original passou pela moderação da plataforma. **A reprodução fiel é o prop ambíguo.**

Se um prop só "funciona" quando fica explícito, o sinal é claro: a versão fiel é a **ambígua**, e é ela que se deve reproduzir. Não se deve ficar reescrevendo um prompt repetidamente só para contornar a recusa do gerador em produzir algo explícito — esse é o momento de voltar à versão fiel/ambígua, não de insistir na evasão.

---

# PARTE C — COMPLIANCE (risco de conta / claims)

Não é sobre a ferramenta de geração, é sobre **sua conta e o funil não serem derrubados** pelas plataformas/reguladores.

## Os dois portões de moderação (nunca confunda)

1. **O filtro da ferramenta de geração** (Veo/Flow pode recusar gerar).
2. **A moderação da plataforma** (Instagram, TikTok, Facebook podem derrubar a conta).

**Passar no primeiro não diz NADA sobre o segundo.** E é o segundo que derruba conta. Um frame que o gerador aceitou pode ainda assim ser explícito demais para postar com segurança. Sempre pese isso antes de publicar, especialmente em vídeos de vitalidade masculina/saúde íntima com props anatômicos.

## Hierarquia de risco (do mais alto ao médio)

1. **MAIS ALTO — Antes/depois de corpo + "nada mais mudou" / "sem dieta, sem academia".** Padrão que FTC e Meta mais punem. Meta chega a proibir imagem de antes/depois em anúncios. No orgânico é menos policiado, mas ainda derruba conta. Se for impulsionar (ads): risco altíssimo → tenha uma versão mais suave.
2. **ALTO — Claim anatômico explícito** (props de vitalidade masculina, "dentro do seu corpo").
3. **ALTO — Claim de diagnóstico** ("você tem disbiose", "seu pH está desequilibrado", "sua calcificação"). Diagnosticar o espectador é delicado.
4. **ALTO — Claims de saúde específicos** ("detoxa o fígado", "desentope seus vasos", "leva circulação ao seu corpo").
5. **MÉDIO — "as farmacêuticas escondem isso"** (conspiração) + sintomas.

## Postura da operação
- O operador roda "punchy" (agressivo) por padrão.
- O papel de quem produz é **entregar + registrar o aviso** nos casos mais agressivos, deixando a decisão com o operador. Sempre sinalize brevemente o risco no caso mais forte, mas **não bloqueie a produção**.
- Roster mais conservador (Jupi Hydration / Karen Thompson): autoridade por vivência, nunca nomeia doenças, nunca promete cura.

---

# PARTE D — IDENTIFICAÇÃO DE MÚSICA (limitação)

Quem decompõe o vídeo **vê frames, não ouve o áudio como música** (a transcrição é de fala, não identifica trilha). Além disso, o Facebook bloqueia acesso automatizado aos Reels (ROBOTS_DISALLOWED), então nem por link dá pra puxar a faixa automaticamente.

**Como descobrir a música você mesmo:**
- **Facebook Reel song finder por link** (ex.: SongFromLink) — extrai o áudio da URL do Reel e identifica por forma de onda (funciona mesmo sem o FB mostrar a tag; só em Reel público).
- **Shazam** ou a busca de música do Google ("o que está tocando"), com o vídeo tocando ao lado.
- Se for trilha "sem copyright" de biblioteca, o Shazam pode não achar — tente uma extensão tipo AHA Music.

Sempre coloque "sem música" nos prompts de vídeo e adicione a trilha só na edição — isso te dá controle e evita strike de copyright.

---

# PARTE E — CHECKLIST DE OTIMIZAÇÃO (imprima e use)

**Decomposição**
- [ ] Rodei a `/watch` e varri as grades de timeline inteiras?
- [ ] Identifiquei corretamente o HERÓI do hook (sem pattern-matching)?
- [ ] Mapeei segunda pessoa, props, reveals dentro dos takes, o que muda entre takes?

**Entrega**
- [ ] Entreguei a transcrição completa + roteiro cena a cena ANTES dos prompts?

**Roteiro**
- [ ] Estrutura idêntica ao original (só variável mudou)?
- [ ] Takes ~8s, sem em dash?
- [ ] Keyword `yes` no CTA com follow-gate?
- [ ] Registro/idade/gênero congruentes com o avatar (ângulo coach se preciso)?

**Imagens**
- [ ] Cada prompt tem `reference_use` travando a âncora?
- [ ] Traços canônicos do avatar corretos (cruz certa, cenário certo)?
- [ ] "no text" no negative de todas?
- [ ] Só o estado inicial de cada take?
- [ ] Herói com volume/cobertura/FORMA bem descritos (não só o nome)?
- [ ] Segunda pessoa travada (rosto) e estágios gerados a partir do original?
- [ ] Frame-herói gerado no Pro com variações?
- [ ] Mapa de âncoras entregue junto?
- [ ] Prompts escritos por inteiro (nunca "igual ao anterior exceto")?

**Vídeos (Fase 7)**
- [ ] Fala inteira e intacta em cada take TALKING?
- [ ] Ação enxuta (só o que acontece)?
- [ ] TALKING vs B-ROLL marcados?
- [ ] "sem música" no som ambiente?
- [ ] Título identificador em cada prompt?

**Se travou restrição**
- [ ] Verifiquei se o modelo é IA ou filmagem real (muda a regra da fala)?
- [ ] Mantive a fala intacta na primeira tentativa?
- [ ] Enxuguei a ação / neutralizei o alvo?
- [ ] Se persistiu, separei elementos em takes diferentes?
- [ ] Explicitei que é personagem de IA fictício?
- [ ] Confirmei que a versão fiel é a ambígua, não a explícita?

**Compliance**
- [ ] Registrei o aviso de risco nos casos mais agressivos?
- [ ] Pesei o portão da plataforma (não só o do gerador)?

**Pós**
- [ ] Legendas (keyword `yes`) na edição?
- [ ] Locução nos takes b-roll / nos que foram gerados sem fala?
- [ ] Trilha adicionada? Cortes secos? Export 9:16?

Próximo documento: **10 — Biblioteca de Vídeos**.
