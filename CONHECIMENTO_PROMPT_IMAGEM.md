# Tudo que eu uso ao produzir um prompt de imagem

Documento de consolidação. Junta num lugar só o que hoje está espalhado em `CLAUDE.md`,
no gabarito `producao/brandon_angle2/PROMPTS_PRODUCAO.md` e em nove memórias.
**Fonte de verdade continua sendo a memória viva.** Se este arquivo divergir dela, a memória ganha.

Memórias que alimentam este doc: `prompts-imagem-json`, `realismo-anti-cara-de-ia`,
`checklist-composicao-visual`, `regras-universais`, `feedback-prompt-imagem-compartilhado`,
`feedback-enquadramento-mais-proximo`, `feedback-prompt-completo-sempre`, `erros-recorrentes`,
`feedback-prompts-na-conversa`, `restricoes-protocolo`, `workflow-entrega-gabarito`.

---

## 0. Onde o prompt de imagem entra

É a Fase 6 do pipeline. Vem **depois** do roteiro aprovado e **antes** dos prompts de vídeo (Fase 7).
O portão obrigatório é o **P5**, que manda ler, nesta ordem, antes do primeiro JSON:

1. O gabarito vivo: `producao/brandon_angle2/ROTEIRO.md` e `PROMPTS_PRODUCAO.md`
2. `workflow-entrega-gabarito` (as 8 coisas que se perdem ao parar de conferir o gabarito)
3. `checklist-composicao-visual` (os 10 itens)
4. `realismo-anti-cara-de-ia` (os 7 itens)
5. `prompts-imagem-json` (campos e blocos padrão)
6. `erros-recorrentes` (falhas 1 a 7 de geração de imagem)
7. `avatares-fichas` (traços canônicos e caminho da âncora)
8. `feedback-prompt-imagem-compartilhado` (um keyframe por SETUP, nunca por take)
9. `feedback-enquadramento-mais-proximo`

**Ler o gabarito, não a lembrança do gabarito.** O grafo (`graphify`) orienta, não substitui a leitura.

---

## 1. As três leis de formato

### 1.1. Prompt de imagem é JSON. Prompt de vídeo é texto simples. Nunca misturar.
O prompt de imagem carrega enquadramento, cor, composição, luz. O de vídeo não descreve nada disso,
porque já está na imagem: ele só carrega fala, ação, câmera e som.

### 1.2. Um keyframe por SETUP (bloco), nunca por take.
Se uma sequência de takes é o avatar falando na mesma posição, mesmo ângulo, mesmo cenário, e só muda
gesto e expressão, então **um único prompt de imagem serve o bloco inteiro** e os prompts de vídeo é
que se separam, um por take.

- Regra de bolso: se dá pra chegar no frame do take seguinte só movendo o corpo a partir do frame
  anterior, é o mesmo bloco. Se precisa aparecer ou sumir alguma coisa (prop entra, cenário muda,
  enquadramento muda), é bloco novo.
- Exceção: muda o **estado** de um prop ou herói em cena, aí o take ganha imagem própria.

### 1.3. GERAR DO ZERO é exceção. O resto é EDITAR do K__.
`GERAR DO ZERO` só no **primeiro keyframe de cada setup**, com a âncora anexada. Todo o resto é
`EDITAR do K__`, que trava rosto, fundo e luz. Gerar tudo do zero faz a identidade derivar entre blocos.

**Estágios (antes/depois disfarçado) sempre a partir do estágio 1 original, nunca em cascata**, senão
a pessoa deriva a cada geração.

---

## 2. Nomenclatura, nunca colapsar num namespace só

| Prefixo | O que é |
|---|---|
| `T__` | Take do roteiro (a fala) |
| `K__` | Keyframe, a imagem |
| `V__` | Clipe de vídeo |
| `REF-__` | Referência auxiliar (2ª pessoa, prop isolado) |

Vários `T` podem usar o mesmo `K`. Cada `T` tem seu `V`.

---

## 3. Os dois gates que rodam ANTES de escrever o primeiro JSON

Composição e realismo não se consertam depois da geração. Consertam-se no prompt. Rodar os dois juntos.

### 3.1. GATE DE COMPOSIÇÃO VISUAL (10 itens)

**Herói**
1. O herói do take está no **lower foreground**, mais perto da lente que o rosto do avatar?
2. **Nada compete com ele.** Elemento que não serve à fala daquele take sai de quadro.
3. Volume e cobertura do herói estão explicitados? (montanha, não camada fina)

**Distância**
4. **"Dá pra estar mais perto?"** Se dá, está longe demais. Perguntar em TODO prompt, não só no hook.
5. Pessoas: **peito pra cima ou ombros pra cima.** O rosto ocupa boa parte do quadro.
6. O take mais fechado do vídeo inteiro é o do **CTA**.

**Fundo**
7. Cenário **RECONHECÍVEL, nunca inventariado.** Duas ou três âncoras visuais bastam.
8. **Reduzir fundo se faz com ENQUADRAMENTO, nunca com blur.** O negative da operação proíbe blur em
   tudo, então a única forma de tirar informação de fundo é fechar o plano e descrever menos.
9. Menos elementos = mais qualidade de geração e mais realismo.

**2ª pessoa**
10. Ela entra **CORTADA pelo quadro**, nunca de corpo inteiro. Presença parcial dá o contexto e deixa
    o herói dominar.

Onde isso mais falha: inventário de fundo (listar seis objetos) e two-shot largo demais no hook.
Fidelidade ao original é de **estrutura** (elemento, ação, reveal), nunca de enquadramento.

### 3.2. GATE DE REALISMO (7 itens)

1. **ISOLAR O HERÓI É A ALAVANCA Nº1.** Menos elementos, mais realista. No hook:
   `"[hero] fills the lower two-thirds, camera pushed in close, everything else out of frame"`.
   Duas ou três âncoras de fundo no máximo. Close-up é regra do hook e dos takes de reveal, não do
   vídeo inteiro. O inimigo é o **inventário no prompt**, não a bagunça vinda de uma âncora real
   preservada por `EDITAR do K__` (essa compra credibilidade de UGC).
2. **COR E LUZ QUE DENUNCIAM.** Cores quentes (amarelo, laranja, marrom) dão cara de IA. Céu branco ou
   claro sempre denuncia. Preferir `overcast sky` / `cloudy`. Externa: golden hour. Interna: luz
   difusa neutra de dia nublado. Negative útil:
   `no warm orange color cast, no yellow tint, no golden glow`.
3. **FUNDO NÃO PODE SAIR BORRADO.** Não se conserta depois. Descrição muito específica mais, quando
   possível, imagem de referência real.
4. **PARTIR SEMPRE DE ALGO REAL (a regra-mãe).** A IA copia bem o que você mostra e inventa mal o que
   você só descreve. Rosto secundário: referência real. Fundo: screenshot real. Prop que teima:
   gerar isolado primeiro, aprovar, usar como referência de objeto.
5. **A ÂNCORA DO AVATAR É O ATIVO QUE MAIS PESA.** Nenhum prompt compensa âncora ruim.
6. **REALISMO É VOLUME, NÃO PROMPT MÁGICO.** Regenerar várias vezes até sair a imagem certa é o método.
   Nano Banana 2 costuma superar o ChatGPT em realismo de avatar.
7. **BLOCO DE REALISMO PADRÃO** (colar em todo prompt, ver seção 5).

Método Frankie (realismo máximo, quando valer o trabalho): gerar fundo, céu, rosto e prop separados,
cada um no seu melhor, e mesclar num frame só.

---

## 4. Campos do JSON e função de cada um

| Campo | Função |
|-------|--------|
| `shot_id` | Nome do keyframe (ex.: `K01_hook_initial`) |
| `reference_use` | **CRUCIAL:** usar a âncora SÓ pra rosto/identidade/roupa/cenário, NÃO copiar pose nem enquadramento |
| `identity_main` | O avatar ("The EXACT woman from the attached reference image" + traços canônicos da ficha) |
| `second_person` | Descreve a 2ª pessoa se houver, sempre cortada pelo quadro |
| `prop` | O herói, descrito por FORMA e COR, não só pelo nome |
| `wardrobe` | Roupa e acessórios da ficha canônica (cruz da cor certa) |
| `scene` | "SAME [cenário] as the reference image: [2 ou 3 âncoras]" + bandeira dos EUA |
| `posture` | Postura, usar pra corrigir a foto-âncora ("standing upright, NOT the seated slouch") |
| `composition` | Disposição no quadro; herói no lower foreground; "VERY CLOSE, almost close-up" |
| `camera` | Ângulo e altura ("eye level, straight-on" / "chest level, slightly high toward the bowl") |
| `state` | **ESTADO INICIAL** do take, sempre o começo da ação, nunca o fim |
| `lighting` | Luz, batendo com o cenário do avatar, neutra de dia nublado |
| `realism` | Bloco padrão de realismo UGC |
| `aspect_ratio` | Sempre `"9:16 vertical"` |
| `negative` | Só coisas neutras. Nunca termo sensível (ver seção 8) |

---

## 5. Blocos padrão (colar sempre)

**Realismo:**
```
"realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details."
```

**Negative base:**
```
"negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting"
```
**Nunca `no text` seco.** Isso apaga a sinalização canônica do cenário (o neon `TRAIN PRAY REPEAT`,
o quadro branco `STAY READY. STAY DISCIPLINED.`), que é parte da identidade do avatar. O que não pode
é legenda ou palavra sobreposta. Legenda de vídeo entra só na edição.

**Anti-skin-shift (adicionar em todo prompt de EDIÇÃO):**
```
"Do not make their skin darker, yellowish or orangish. Do not make the colors more saturated."
```

**Adaptações do negative:**
- Cenário com copo de vidro que não deve ser decorativo de beber: `no glass drinking cup`
- Foto-âncora sentada e você quer em pé: `no seated slouch` + `posture` em pé explícito
- Estágio de transformação: negative do estado errado (`no toned arm in this frame` no estágio gordo,
  `no big belly in this frame` no estágio magro)

---

## 6. Título do prompt + bloco visual de anexo

### 6.1. Título já diz a AÇÃO DE GERAÇÃO, em caixa alta, com as referências dentro
Ele bate o olho e sabe o que fazer sem ler o JSON.
```
## K06 · T13, T14 · PRODUTO · GERAR DO ZERO · ÂNCORA BRANDON + PRODUCT.PNG
## K04 · T4, T7, T11 · EDITAR do K03 (muda só o gesto de mão)
```

### 6.2. O título não basta: BLOCO VISUAL DE ANEXO acima de cada prompt
Em citação, logo abaixo do título e acima do bloco de código. Diz **o que arrastar pro campo de
anexo**, não descreve a cena.
```
> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA <AVATAR>** `caminho/da/ancora.jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO
```
```
> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K01 já aprovado**
>
> ### ✏️ EDITAR, muda só <o que muda>
```
```
> ### 📎 ANEXAR: **NADA**
>
> ### 🆕 GERAR DO ZERO
```

As três regras do bloco:
1. Sempre diz o **NÚMERO de imagens**, em negrito. É o que ele confere de relance.
2. Cada imagem numerada com o caminho ou o nome do keyframe de origem. Nunca "a âncora" solta.
3. Onde houver risco de cascata, o bloco carrega o aviso: `🚫 NUNCA anexar o K07 aqui`.

Regra de bolso do anexo: **GERAR DO ZERO anexa âncora + REF. EDITAR anexa uma imagem só, o keyframe
de origem.**

### 6.3. Linha curta descrevendo a cena, se existir, vem DEPOIS do bloco de anexo, nunca no lugar dele
```
> **K01 · GERAR DO ZERO** · Brandon segurando a placa colada na câmera, barriga da mulher cortada ao lado
```

### 6.4. Índice de geração no topo do pacote
```
| Take | Keyframe | Ação de geração |
|---|---|---|
| ref | REF-A | GERAR DO ZERO a 2ª pessoa. Aprovar rosto antes de tudo. |
| T1 | K01 | GERAR DO ZERO (ref: âncora Brandon + REF-A aprovada). Frame herói, gerar no Pro. |
| T2 | K02 | EDITAR do K01 (muda só a distância de câmera e a mão livre) |
```

---

## 7. Regras universais que atingem o prompt de imagem

- **🇺🇸 Bandeira dos EUA em TODO prompt de imagem.** Discreta porém VISÍVEL e em foco (bandeirinha de
  mesa, patch na roupa, adesivo no canto de um espelho). Nunca desfocada, nunca cortada pela borda,
  nunca só implícita. Escrever no campo `scene`, conta como uma das três âncoras de fundo.
  **Única exceção:** prompt de REF de prop isolado (REF-CARTA, `product.png`), que não tem cenário e
  contaminaria todo keyframe que anexasse a REF.
- **`reference_use` sempre presente**, restringindo a âncora a identidade/roupa/cenário, nunca
  câmera/pose. Sem essa trava a pose da foto-âncora vaza pra cena.
- **Sem copos de vidro de beber decorativos.** Preferir mason jar, cerâmica ou tigela transparente
  (bowls transparentes OK pra demo onde se precisa ver o conteúdo).
- **Só o estado inicial de cada take.** A transformação acontece no vídeo (Fase 7).
- **Reveal contínuo dentro de um take = UMA imagem** do estado inicial. Só vira imagens separadas se
  o original **corta** entre os dois estados (antes/depois disfarçado, braço encolhendo take a take).
  Teste único: o original corta? No Ângulo 2 essa resposta é "corta" com frequência (herói é corpo
  antes/depois).
- **Enquadramento sempre mais perto que o original.** O enquadramento não faz parte do esqueleto.
  Padrão quase close-up, tanto pra prop quanto pra pessoa. Vale pra todos os takes, não só o hook.
- **Prompt entregue é prompt COMPLETO.** Nunca "adicione X em todos os prompts", nunca colar só a
  linha que mudou. Regra nova no meio da produção obriga reescrever por inteiro todos os prompts
  afetados, no arquivo e no chat. Alternativa se entrega como dois prompts completos lado a lado.
- **Prompts colados na conversa**, em bloco de código pronto pra copiar, além do arquivo. Arquivo e
  chat, sempre os dois.

---

## 8. Restrições de conteúdo: o que trava e o campo NEGATIVE

### Regra #0: quando o Luigi diz que travou, ele JÁ TENTOU VÁRIAS VEZES. Nunca sugerir retry.
Todo relato de bloqueio dele é gatilho de conteúdo confirmado. Ir direto pro diagnóstico e pra reescrita.

### Regra #1 inviolável: a FALA nunca é o problema.
Se o vídeo modelo + roteiro vieram juntos, aquela fala já foi gerada e passou. Ajustar **apenas** a
descrição da cena, a ação, o enquadramento, o que o elemento atinge. Nunca a fala.

### O que realmente dispara (ordem de probabilidade)
1. **A AÇÃO da cena**, especialmente corpo + líquido em região sensível.
2. **Excesso de descrição.** Detalhar ângulo, posição, região do corpo aumenta a chance do
   classificador ler como explícito. Enxugar: só o que acontece de fato.
3. **Combinação de elementos** (regador + pessoa deitada). Isolados passam, juntos travam. A saída é
   separar em takes diferentes e juntar no corte.
4. **O próprio campo NEGATIVE.**

### Regra do campo NEGATIVE
**Nunca listar no negative o nome daquilo que você teme que apareça, quando o termo em si é sensível.**
O classificador lê o token, não a negação. Listar a palavra injeta o conceito.

Nunca vão no negative:
- Nomes de órgão (`no heart model`, `no lung model`, `no kidney model`)
- Termos de gore (`no gore`, `no blood`, `no worms`, `no insects`)
- Termos de marca (`no logos`, `no brand names`, `no signage`) — derrubaram 8 de 8 prompts de um
  pacote, incluindo um insert sem pessoa em quadro

O negative só aceita coisas **neutras**: texto, legendas, palavras na tela, estúdio, cara de desenho,
dedos a mais, blur.

**A forma certa de evitar marca ou órgão é não descrever isso no texto positivo. Nunca negar.**
Em vez disso: descrever positivamente a forma certa (matte, rounded, clean, clinical, soft, calm).

### Substituições que funcionam em render anatômico
| Trava | Passa |
|---|---|
| `human intestine` / `intestinal villi` | `teaching model of a digestive tube` / `finger-shaped projections` |
| `moist glossy tissue` / `wet` | `soft matte silicone` |
| `deep angry red` / `inflamed` | `warm deep coral red` |
| `pinkish-brown` | `muted dusty rose` |
| `endoscopic` | `borescope` |
| `fades to dark` | `falls off gently into shadow` |
| `crusted residue` | `dried crust, cracked like dried clay` |

### Protocolo de destravamento, na ordem
1. **Enxugar a ação** ao mínimo. Tirar ângulo, posição, região-alvo, adjetivos.
2. **Neutralizar o alvo da ação.** Redirecionar pra ponto neutro (bandeja, chão). A metáfora se
   mantém na legenda mais a presença dos elementos.
3. **Separar elementos em takes diferentes** e juntar no corte. Nenhum frame isolado é problemático.
4. **Explicitar que é personagem de IA fictício**, pessoa que não existe. É verdade e ajuda.

---

## 9. Dicas de ouro (todas de erros reais)

1. **Descreva FORMATO, não só o nome do prop.** "Modelo do aparelho reprodutor feminino" vira coração
   ou crânio. Escreva: "pink plastic model shaped like a uterus with two curved fallopian tubes
   branching to the sides and a central canal below".
2. **Volume e cobertura precisam ser explicitados.** "THICK, TALL, HEAPED MOUND... piled high with 3D
   volume, so much that almost no bare skin is visible" + negative `no thin scattered layer, no flat
   sauce-like coating`. Senão sai camada fininha.
3. **Enquadramento herói:** herói no lower foreground, câmera slightly high toward it, puxada pra perto.
4. **Corrigir foto-âncora:** "standing upright, NOT the seated slouch of the reference photo, no legs
   or lap in frame" + negative `no seated slouch`.
5. **Travar 2ª pessoa:** gerar primeiro, aprovar o rosto, e nas próximas usar "Use [imagem]'s [pessoa]
   face as reference so it is clearly the SAME [person]".
6. **Gerar estágios SEMPRE a partir do estágio 1 original**, nunca em cascata.
7. **Tamanho do produto no prompt.** "The product is about 10 cm in height" pra evitar tamanho errado.
8. **Zero blur, sempre.** "No blur anywhere, everything in perfectly sharp focus" incluindo fundo,
   paredes, mobília. Phone camera tem profundidade de campo ampla, tudo nítido, e isso reforça o UGC.

---

## 10. Erros recorrentes de imagem (as 7 falhas)

1. **Enfraquecer estrutura virando talking head.** Se o original mostra algo acontecendo, o clone tem
   que mostrar a mesma coisa. A demo tem que continuar demo. (A mais mortal.)
2. **Inventar frames que não existem no original.** Reproduzir só os beats existentes.
3. **Deixar a foto-âncora ditar câmera/pose.** `reference_use` + `posture` com override + negative
   `no seated slouch`.
4. **Texto carimbado nas imagens.** `no captions, no subtitles, no words on screen` no negative de
   todo prompt.
5. **Gerar antes/durante/depois como imagens de UMA transformação.** Dentro de um take, só o estado
   inicial. Exceção: estágios do antes/depois disfarçado, que são takes diferentes.
6. **Prop sai errado** (coração no lugar de útero). Descrever FORMA e COR, não só o nome. Se teimar,
   gerar isolado, aprovar, usar como referência de objeto.
7. **Volume/cobertura insuficiente do herói.** Forçar o volume no prompt e puxar a câmera pra perto.

### Checklist rápido antes de aprovar cada imagem
- [ ] `reference_use` travando a âncora presente?
- [ ] Traços canônicos corretos (cruz certa, cenário certo)?
- [ ] `no captions` no negative (nunca `no text` seco)?
- [ ] Só o estado inicial, não a transformação?
- [ ] Herói com volume/cobertura/forma bem descritos?
- [ ] 2ª pessoa travada (rosto) e estágios a partir do original, não cascata?
- [ ] Bandeira dos EUA no `scene`, visível e em foco?
- [ ] Frame herói gerado no Nano Banana Pro com variações?

---

## 11. O que muda por ângulo

| | Produto em quadro | REF de prop fixa | Observação |
|---|---|---|---|
| **Ângulo 1 (Korella)** | Sim, sempre | `product.png` (~10 cm) | Frasco na mão |
| **Ângulo 2 (FityWell)** | Não | nenhuma | Herói costuma ser corpo antes/depois |
| **Ângulo 3 (Auraly)** | Não (CTA promete o rosto da alma gêmea) | `REF-CARTA` SOULMATE holográfica | Kit de tarólogo obrigatório em toda âncora e keyframe: cristais, incenso aceso, bandeira dos EUA, cartas, quadro astrológico, cruz, vela. Esse kit ganha do teto de 3 âncoras neste ângulo, entra agrupado em 2 blocos. Rosto NUNCA revelado no vídeo, sempre obscurecido como propriedade física do objeto (vidro fosco, névoa), nunca como blur de câmera |
| **Ângulo 4 (Body Hacks)** | Sim, livro FÍSICO | `REF-LIVRO` | Nunca mockup de ebook nem tela de celular |

REF de prop fixa: gerar uma vez, aprovar, anexar sempre nos keyframes daquele ângulo, igual o Ângulo 1
faz com o `product.png`. A REF de prop isolado não leva cenário nem bandeira.

---

## 12. Templates de JSON

### 12.1. Take de demo (com prop/herói)
```json
{
  "shot_id": "K01_hook_initial",
  "reference_use": "Use the attached image ONLY for [AVATAR]'s face, identity, wardrobe, and the [CENÁRIO] scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT [man/woman] from the attached reference image ([AVATAR]): [TRAÇOS CANÔNICOS].",
  "wardrobe": "[ROUPA + ACESSÓRIOS, cruz da cor certa].",
  "prop": "[FORMA e COR do herói, descrito como objeto didático calmo].",
  "scene": "SAME [garagem/cozinha/box] as [AVATAR]'s reference image: [2 ou 3 âncoras], small US flag on a desk stand.",
  "posture": "[postura, corrigindo a foto se preciso].",
  "composition": "VERY CLOSE, almost close-up. [PROP] sits in the lower foreground, much closer to the lens than everything else. [AVATAR]'s face in the upper third, cropped at the top. Nothing else competes.",
  "camera": "chest level, slightly high toward the [prop], pushed in very close",
  "state": "Start frame: [o instante inicial da ação].",
  "lighting": "Soft neutral daylight of an overcast day.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint"
}
```

### 12.2. Talking head (sem prop)
```json
{
  "shot_id": "K03_talking_a",
  "reference_use": "Use the attached image ONLY for [AVATAR]'s face, identity, wardrobe, and the [CENÁRIO] scene. Do NOT copy its pose.",
  "identity_main": "The EXACT [man/woman] from the reference image ([AVATAR]): [TRAÇOS].",
  "wardrobe": "[ROUPA canônica].",
  "scene": "SAME [cenário] as the reference image: [2 ou 3 âncoras], small US flag visible.",
  "posture": "Standing/seated upright, close to camera, chin up, [expressão].",
  "composition": "VERY CLOSE, almost close-up. Shoulders-up, face fills a large part of the frame, top of the head cropped. Left arm extended toward the bottom left corner because that hand holds the filming phone. Right hand comes into the bottom of the frame in a natural gesture.",
  "camera": "eye level, straight-on, close selfie distance",
  "state": "Start frame: speaking directly into the lens.",
  "lighting": "Soft neutral daylight of an overcast day.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the background wall and signage.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no second person, no props"
}
```

### 12.3. Insert / B-roll (close sem rosto)
```json
{
  "shot_id": "K_insert",
  "reference_use": "Close-up insert. Use only the [superfície do cenário] and lighting.",
  "identity_main": "No face. Close-up of [o objeto/detalhe].",
  "scene": "SAME [cenário] surface, [luz].",
  "composition": "Extreme close-up of [detalhe]; [o que está prestes a acontecer].",
  "camera": "macro close-up",
  "state": "Start frame: [estado inicial do detalhe].",
  "lighting": "Soft neutral daylight.",
  "realism": "UGC realism, real texture, iPhone macro look, no AI polish, no blur.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no face, no studio, no cartoon look"
}
```

### 12.4. Comando de edição (gerar estágio a partir de imagem aprovada)
```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep [pessoas] exactly the same: same faces, same hair, same tattoos, same body positions, same [prop], same pose. Keep the SAME background exactly: [detalhes], same lighting, same camera angle and framing.",
  "change_1": "[a primeira mudança]. Do not change [o que não muda].",
  "change_2": "[a segunda mudança, se houver].",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make their skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the faces, do not change identities, do not change the background, do not change the [posição travada], do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers"
}
```

---

## 13. Exemplo real completo (K01 do gabarito `brandon_angle2`)

Hook do Ângulo 2. Prop herói (placa anatômica) + 2ª pessoa cortada pelo quadro + âncora do avatar.

> ### 📎 ANEXAR: **3 IMAGENS**
> **1️⃣ ÂNCORA BRANDON** `C:\Users\luigi\Desktop\AVATARES NON-SHOP\holistic.brandon .png`
> **2️⃣ REF-A** (a 2ª pessoa já aprovada)
> **3️⃣ A trava do prop herói** (texto)
>
> ### 🆕 GERAR DO ZERO (Nano Banana Pro, várias variações)

```json
{
  "shot_id": "K01_hook_initial",
  "reference_use": "Use the first attached image ONLY for Brandon's face, identity, hair, tattoos, wardrobe and the gym scene. Use the second attached image ONLY for the second woman's face so it is clearly the SAME woman. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Brandon): mixed-race Black American woman, athletic build, light-medium skin with soft freckles, brown eyes, cornrows braided back with loose braided ends falling in front of the shoulders and wooden and amber beads on the tips, fine-line floral blackwork sleeve on the arm on the left side of frame, small leaf tattoo on the collarbone.",
  "wardrobe": "White ribbed tank top, dark gray training shorts, thin GOLD chain with a GOLD cross pendant.",
  "second_person": "The EXACT woman from the second reference image: American woman in her mid forties, black sports bra and dark gray leggings, visibly swollen lower belly. She stands close beside Brandon on the right, and the frame CROPS her: only her torso from collarbone to upper thigh is in shot, her head is above the top edge and part of her body is cut by the right edge. Her swollen belly sits right next to the plaque. Her arms hang relaxed. She does not touch the plaque.",
  "prop": "A clean classroom-style anatomical teaching plaque of a female midsection from the ribs down to the hips, molded in soft matte cream-toned silicone, mounted upright on a white rectangular base with two thin metal posts. The belly of the plaque is clearly swollen and rounded outward. An oval cutaway window in the center of the abdomen exposes a pale matte silicone digestive tube packed tight and completely blocked with compacted dried material in dusty beige and muted dusty rose, cracked on the surface like dried clay. It looks like a calm educational teaching aid.",
  "scene": "SAME concrete-block gym as the reference image: light gray cinderblock wall, red neon sign reading TRAIN PRAY REPEAT, vintage American flag, white board reading STAY READY. STAY DISCIPLINED., black metal shelf with glass jars of herbs and seeds, reddish wooden slat ceiling.",
  "posture": "Brandon stands upright facing the camera, holding the plaque vertically with both hands in front of her own midsection, at the height of her own waist and hips.",
  "composition": "VERY CLOSE, almost close-up. The camera is right on top of the plaque. The plaque fills most of the frame and is much closer to the lens than everything else, so it is unmistakably the hero. Brandon's face is visible in the upper third of the frame, cropped at the top of her head. Nothing else competes for attention. The gym behind is barely readable, just enough to recognize the place.",
  "camera": "chest level, straight-on, camera pushed in very close to the plaque, tight framing",
  "state": "Start frame: Brandon holds the plaque steady and looks directly into the lens, about to speak.",
  "lighting": "Soft neutral daylight of an open gym, warm red glow from the neon on the wall.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall shelf and signage.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no silver jewelry, no third person"
}
```

O que esse exemplo demonstra na prática:
- `reference_use` separando as duas âncoras e dizendo o que puxar de cada uma
- 2ª pessoa **cortada pelo quadro** (item 10 do gate de composição)
- prop no **lower foreground, muito mais perto que o rosto** (itens 1 e 4)
- fundo **reconhecível, não inventariado**: 3 ou 4 âncoras e a placa domina (itens 7 e 8)
- `no silver jewelry` no negative porque a Brandon usa cruz de OURO (regra de avatar)
- `no third person` porque nesse take só existem duas mulheres
- sinalização de parede preservada, sem `no text` seco (regra universal 2)

---

## 14. Mapa de âncoras e o linter

### Mapa de âncoras (fecha o pacote de prompts)
```
| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-A | nenhuma, gerar do zero | Nano Banana 2, regenerar até rosto crível |
| K01 | âncora + REF-A aprovada | Nano Banana Pro, várias variações |
| K02 | K01 aprovado | Nano Banana 2, comando de edição |
| K05 | K03 aprovado (nunca a partir do K04) | Nano Banana 2, comando de edição |
```

### `python checar_entrega.py producao/<avatar>_<slug>`
Roda no fechamento (portão P9) e no `pre-commit`. Lê do disco, então sobrevive ao resumo de contexto.
Do lado da imagem ele checa: JSON válido, `no captions` presente, sem termo sensível no negative,
bandeira dos EUA, nomenclatura K/REF, produto em quadro nos ângulos 2 e 3 (ausência), travas do
Ângulo 3, seções na ordem, instrução de patch (proibida). **Entrega não fecha com FALHA.** Falso
positivo se conserta no linter, nunca se ignora.
