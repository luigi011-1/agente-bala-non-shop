# Guia completo: produção de vídeos com o agente do Google Flow

Versão de 2026-09-23. Vale para as instruções do agente **v13**.

Este documento explica, do zero, como a operação transforma um **pacote de prompts** em vídeos
prontos usando o **agente do Google Flow**. Depois de ler, você consegue:

1. configurar o agente do Flow para trabalhar do nosso jeito;
2. entender cada parte do pacote que você recebe;
3. gerar as imagens e os vídeos na ordem certa, sem trocar uma imagem pelo vídeo errado;
4. aprovar ou reprovar cada imagem e cada vídeo com os mesmos critérios de qualidade que usamos;
5. destravar um prompt que caiu na censura;
6. escrever um prompt novo no mesmo padrão, se precisar.

Você não precisa conhecer nada da operação antes. Tudo que é necessário está aqui, inclusive o
texto que vai na memória do agente (Apêndice A).

---

## 1. O processo em um minuto

```
PACOTE DE PRODUÇÃO (texto)
   │
   ├─ 1. Instruções do agente ──────────► colar na MEMÓRIA do agente do Flow (toda produção)
   ├─ 2. Referências (âncora / REF-P) ──► anexar nas imagens, conforme o mapa
   ├─ 3. Bloco de IMAGEM (K01, K02...) ─► Nano Banana 2 gera 1 imagem por K
   │                                          │
   │                                     você APROVA cada imagem
   │                                          │
   ├─ 4. Bloco de VÍDEO (V01, V02...) ──► Veo 3.1 Lite anima cada imagem aprovada
   │                                      (a imagem do K entra como INITIAL FRAME do V)
   │                                          │
   │                                     você APROVA cada clipe
   │                                          │
   └─ 5. Montagem ──────────────────────► CapCut junta os clipes, corta, põe card e exporta
```

A regra que sustenta tudo: **cada imagem tem um código `K` e cada vídeo tem um código `V`, e o
código diz qual imagem vira qual vídeo.** O agente nunca adivinha pela aparência, pela ordem da
galeria ou pela ordem de anexo. Ele lê o código.

---

## 2. Vocabulário

| Termo | O que é |
|---|---|
| **Pacote** | O conjunto de textos de uma produção: instruções do agente, blocos de prompts, mapas, montagem e roteiro. |
| **T01, T02...** | Take: um trecho do roteiro (uma fala ou uma ação). Aparece no roteiro, **nunca** dentro dos blocos. |
| **K01, K02...** | Keyframe: um prompt de **imagem**. Gera a imagem parada que abre o clipe. |
| **V01, V02...** | Um prompt de **vídeo**. Anima uma imagem aprovada e gera um clipe de 8 segundos. |
| **REF-...** | Referência auxiliar. `REF-P1`, `REF-P2`... são **character sheets** (folha de personagem) de cada personagem principal numa cena atuada. |
| **Âncora** | A foto oficial do avatar da conta. É a referência de identidade anexada nas imagens. |
| **INITIAL FRAME** | O modo em que a imagem aprovada entra como o **primeiro quadro** do vídeo. É o único modo que usamos. |
| **Perfil** | A configuração da produção: **CLÁSSICO** ou **AURALY**. Muda quantas imagens por K, quantas variações por V e como K casa com V. |
| **MAPA K/V** | A tabela que diz qual K serve de INITIAL FRAME para cada V. |
| **MAPA DE ANEXOS** | A tabela que diz quais imagens anexar em cada K (âncora, REF-P, frame de composição). |
| **Lote** | Grupo de no máximo 7 códigos V executados de uma vez. |
| **B-roll** | Clipe sem fala: inserto de mão, objeto, reação. A voz entra por cima na edição. |

---

## 3. O que você precisa antes de começar

- **Conta no Google Flow** com acesso ao **Nano Banana 2** (imagem) e ao **Veo 3.1 Lite** (vídeo),
  incluindo a opção **Lower Priority** (fila mais lenta, sem consumir créditos, em 720p).
- **O agente do Flow** (o assistente movido a Gemini dentro do Flow), com um campo de
  **instruções ou memória** onde você cola texto que ele segue durante toda a sessão. O nome exato
  do campo pode variar conforme a versão da interface; é o lugar das instruções permanentes do
  agente.
- **O pacote da produção**, recebido em texto (chat ou arquivo `.md`).
- **Os arquivos de referência** citados no pacote: a âncora do avatar e, quando houver, os frames
  de composição.
- **CapCut** (ou outro editor) para a montagem.
- Uma **pasta por produção** no seu computador, para salvar tudo com o código no nome
  (seção 8.4).

O agente do Flow **gera**. Ele não assiste vídeos, não analisa referência e não escreve copy. Tudo
isso já chega pronto no pacote.

---

## 4. O pacote: o que chega e em que ordem

O pacote sempre chega nesta ordem. Nunca pule item.

| # | Parte | O que fazer com ela |
|---|---|---|
| 1 | **Instruções para a memória do agente** | Colar **inteiro** na memória do agente. Toda produção, toda vez. |
| 2 | **Fichas do elenco e MAPA DE ANEXOS** (cena atuada) ou âncora do avatar | Ler. Diz o que anexar em cada K. **Fica fora dos blocos.** |
| 3 | **Bloco de IMAGEM** | Um bloco único com todos os `REF-P` (se houver) e todos os `K`. É o que vai para o agente. |
| 4 | **Bloco de VÍDEO** | Um bloco único com todos os `V`. É o que vai para o agente. |
| 5 | **MAPA K/V** | Diz qual imagem abre cada vídeo. **Fica fora dos blocos.** |
| 6 | **Montagem no CapCut** | Ordem dos clipes, cortes, card final, exportação. |
| 7 | **Transcrição e roteiro final** | A fala exata de cada take, em inglês e português, para conferir o vídeo. |

Fora dos blocos também vem uma linha `Checklist de envio: X/X aprovados`: é a prova de que o
pacote passou pelo controle de qualidade antes de chegar a você.

### 4.1 Como o bloco é construído, e por que isso importa

Dentro dos blocos de imagem e de vídeo existe **só** o código sozinho numa linha, seguido do prompt
completo:

```
K01
[prompt completo da imagem 1]

K02
[prompt completo da imagem 2]
```

```
V01
[prompt completo do vídeo 1]

V02
[prompt completo do vídeo 2]
```

**Não existe nada além disso dentro do bloco:** nenhum título, descrição, número de take, nota,
caminho de arquivo, configuração de modelo ou "use a imagem K01". Isso é proposital. O agente do
Flow é um executor: se houver texto auxiliar dentro do bloco, ele cola esse texto no campo de
prompt como se fosse parte da imagem. Já aconteceu, e por isso toda informação auxiliar vive nos
mapas, fora dos blocos.

**Cada prompt é autossuficiente.** Um K descreve sozinho a identidade das pessoas, a roupa, o
cenário, a luz, o enquadramento, os objetos e a expressão, mesmo que isso se repita em todos os K.
Um V descreve sozinho a fala, a voz, a ação, a câmera e o som. Nada de "igual ao anterior". O
motivo: o Flow recebe só os anexos mais aquele prompt, e não lembra do prompt anterior.

---

## 5. Passo 1: carregar as instruções na memória do agente

1. Abra o agente do Flow e o campo de instruções/memória dele.
2. Apague o que houver de uma produção anterior.
3. Cole o bloco **"Instruções para a memória do agente"** do pacote, **inteiro**, sem editar.
   (O texto de referência está no Apêndice A.)
4. Confirme que a versão é a mesma do pacote (hoje, **v13**).

**Por que toda vez:** a memória do agente é preenchida do zero a cada rodada, e a configuração
muda entre produções (perfil, número de variações, regras de anexo). Um pacote nunca diz "a memória
continua a mesma". Se o bloco não veio no pacote, peça antes de começar.

**Nunca cole essas instruções dentro de um prompt K ou V.** Elas são regras do executor, não
descrição de imagem.

---

## 6. Passo 2: registrar o perfil da produção

O agente precisa saber o perfil antes de gerar qualquer coisa. O pacote diz qual é.

| Configuração | CLÁSSICO (FityWell, Korella e cena atuada) | AURALY |
|---|---|---|
| Modelo de imagem | Nano Banana 2 | Nano Banana 2 |
| Formato | 9:16 vertical | 9:16 vertical |
| Imagens por K | **1 imagem final** | **4 candidatas**, você escolhe 1 |
| Modelo de vídeo | Veo 3.1 Lite | Veo 3.1 Lite |
| Prioridade | Lower Priority | Lower Priority |
| Duração por clipe | 8 segundos | 8 segundos |
| Variações por V | **1** | **3** |
| Como a imagem vira vídeo | INITIAL FRAME | INITIAL FRAME |
| Como K casa com V | pelo número (regra do maior K ≤ V) | **só pelo MAPA K/V explícito** |
| Lote de vídeo | até 7 códigos V por vez | até 7 códigos V por vez |

Se o perfil não veio, ou se os códigos recebidos não batem com o perfil, **pare e pergunte**. O
agente nunca escolhe o perfil sozinho.

---

## 7. Passo 3: as referências (o que anexar em cada imagem)

Existem três tipos de imagem de referência. O MAPA DE ANEXOS (ou o índice do pacote) diz qual
entra em cada K, **e em que ordem**.

### 7.1 Âncora do avatar
A foto oficial do avatar da conta. Nas produções com avatar, ela vai **em todo K** em que o avatar
aparece. Regras:
- **Registrar o nome do arquivo** e confirmar qual avatar está ativo antes da primeira geração.
- **Nunca casar nome com rosto pela ordem de anexo.** Abra a âncora e confira o rosto.
- **Um avatar por vez.** Ao trocar de avatar (`finalizamos, vamos para o próximo avatar`), tire a
  âncora anterior da seleção e espere a nova. As identidades nunca se misturam.
- Quando o K pede cenário ou roupa diferentes da âncora, o próprio texto do K diz "use a âncora só
  para a identidade". Siga o texto e ignore roupa, fundo e objetos da âncora.

### 7.2 Character sheets `REF-P` (cenas atuadas)
Nas cenas com vários personagens (short form e movie style), cada **personagem principal** (quem
aparece em mais de um clipe) ganha uma folha de personagem: a mesma pessoa de frente, de três
quartos, de perfil e em close do rosto, sobre fundo cinza liso.
- Os `REF-P` vêm **no início do bloco de imagem**, antes dos K.
- Gere cada `REF-P` **do zero, sem anexo**, uma imagem final.
- **Aprove todos os `REF-P` antes do primeiro K.** Se um personagem sair errado aqui, ele sai
  errado no vídeo inteiro.
- Depois, cada K anexa os `REF-P` listados no MAPA DE ANEXOS, **na ordem da lista**. A ordem
  importa: o prompt diz "the stepmother is the person in the first character sheet", então a
  primeira imagem anexada tem que ser a dela.
- Personagem que aparece uma vez só e figurante não têm sheet. Eles são descritos por escrito
  dentro do K.

### 7.3 Frame de composição
Um print do vídeo de referência, usado **só** para posição de câmera e das pessoas. Entra **por
último**, depois dos sheets. O prompt manda copiar só o enquadramento, nunca rosto, corpo, roupa ou
cenário. Se o frame mostrar um rosto grande, o pacote pode entregar uma versão com o rosto coberto
por uma caixa cinza (isso evita bloqueio por semelhança com pessoa real).

---

## 8. Passo 4: gerar as imagens

### 8.1 Como o agente localiza cada prompt de imagem
1. Recebe o bloco de imagem inteiro.
2. Identifica cada código: **uma linha que contém só `K` + número** (ou `REF-P` + número) marca o
   início de um prompt. Tudo até o próximo código é o prompt daquele código.
3. **Conta os códigos e confere duplicatas** antes de gerar. Se o pacote diz 7 K e o agente achou
   6, algo foi colado errado: parar.
4. Reconhece que é um prompt de **imagem** pelo formato (seção 10.1): um parágrafo único em inglês,
   que começa com `IMPORTANT: THIS IS IPHONE FOOTAGE`, `Edit the attached image` ou
   `CHARACTER SHEET`.

### 8.2 Como gerar
Para cada código, na ordem:
1. Anexar as referências do MAPA DE ANEXOS para aquele código, na ordem indicada.
2. Colar **só o prompt** (sem a linha do código) no campo de prompt do Nano Banana 2.
3. Formato 9:16.
4. Gerar a quantidade do perfil (1 no clássico, 4 no Auraly).
5. Salvar com o código no nome (seção 8.4).

**Colar o prompt literalmente.** Não traduzir, não resumir, não "melhorar". Cada palavra está lá
por um motivo de qualidade ou de censura.

### 8.3 Ordem de geração
`REF-P` (se houver) → aprovação dos sheets → `K01`, `K02`... em ordem numérica. No perfil
clássico, gere todos os K e **espere o pacote de vídeo** antes de passar para os vídeos.

### 8.4 Nome dos arquivos
Sempre `<produção>_<avatar ou elenco>_<código>_<variação>`. Exemplos:
`madrasta_elenco_K03_1.png`, `pernas_lynn_K06_2.png`, `pernas_lynn_V06_1.mp4`.
O código no nome é o que garante que, na hora do vídeo, a imagem certa vai para o V certo.

---

## 9. Passo 5: aprovar as imagens

Uma imagem só é aprovada se passar **em todos** os itens. Regenerar é normal: realismo é volume
de tentativas, não prompt mágico.

**Identidade**
- [ ] O rosto é o da âncora / do character sheet, sem derivar entre imagens.
- [ ] Roupa, cabelo e acessórios iguais aos descritos (e iguais entre todos os K).
- [ ] A idade não foi suavizada (rugas, linhas e pele real continuam lá).

**Realismo (anti cara de IA)**
- [ ] Luz **neutra de dia nublado**. Nenhum tom amarelo, laranja ou "pôr do sol".
- [ ] Céu, quando aparece, com cor e textura de nuvem. **Céu branco ou estourado reprova.**
- [ ] Janela mostra o lado de fora; nunca um branco estourado.
- [ ] **Tudo em foco**, inclusive o fundo. Fundo borrado reprova (não se conserta depois).
- [ ] Pele com poros e textura; nada de pele de plástico ou "beauty filter".
- [ ] Mãos com cinco dedos, sem deformação.

**Composição**
- [ ] O **objeto herói** (o que o prompt chama de hero) está no primeiro plano, perto da lente,
      maior que o rosto, quando o prompt pede.
- [ ] No máximo duas ou três coisas chamando atenção no fundo.
- [ ] **Bandeira dos EUA** visível, discreta e em foco (em todo K com cenário).
- [ ] Nenhum texto, legenda ou marca escrita na imagem.

**Fala**
- [ ] No K que abre um take falado, a boca de quem fala primeiro está **entreaberta** (ajuda o
      lip sync do vídeo).

**Produto**
- [ ] Nos ângulos que não mostram produto (FityWell e Auraly), nenhum frasco, app ou tela aparece.

---

## 10. Passo 6: gerar os vídeos

### 10.1 Como o agente distingue um prompt de IMAGEM de um prompt de VÍDEO
Esta é a regra mais importante do guia, porque o erro mais caro que já tivemos foi o agente colar o
**prompt da imagem** no campo de texto do **vídeo**.

A diferença é mecânica, não de julgamento:

| | Prompt de IMAGEM (K) | Prompt de VÍDEO (V) |
|---|---|---|
| Idioma | inglês | português (a fala entre aspas fica em inglês) |
| Forma | um parágrafo único e denso | cinco partes em linhas separadas |
| Começa com | `IMPORTANT: THIS IS IPHONE FOOTAGE`, `Edit the attached image` ou `CHARACTER SHEET` | `o avatar ... fala`, `falas no take` ou `(sem fala no take: ...)` |
| Contém | nunca contém `câmera:` nem `som ambiente:` | **sempre** contém `o que acontece no vídeo:`, `câmera:` e `som ambiente:` |

**Checagem obrigatória antes de cada vídeo:** o texto que vai no campo do vídeo tem que conter, ao
pé da letra, as três marcas `o que acontece no vídeo:`, `câmera:` e `som ambiente:`. Se faltar
uma, **parar**: o texto colado é um prompt de imagem.

### 10.2 Como o agente sabe qual imagem abre cada vídeo
O vídeo `V__` **nunca** escolhe a imagem pela aparência. Existem só duas regras, e o perfil diz qual
vale:

**CLÁSSICO: pelo número.** O `V` usa o **maior K cujo número não passa o do V**.
- Com K01 a K07 e V01 a V07: V01 usa K01, V02 usa K02, e assim por diante.
- Com K01, K03 e K06: V01 e V02 usam K01; V03, V04 e V05 usam K03; V06 usa K06.
- Se não existe K menor ou igual ao V, parar.
- O pacote também traz o MAPA K/V escrito (`V01: K01 · V02: K02...`) para conferência.

**AURALY: só pelo MAPA K/V explícito.** Vários V podem usar o mesmo K (por exemplo, quatro takes
de corpo partindo do mesmo frame):
```
MAPA K/V
V06: K06
V07: K06
V08: K06
V09: K06
```
Isso é reutilização proposital, não imagem faltando. Cada V precisa ter exatamente um K no mapa, e
esse K precisa ter uma candidata **aprovada por você**. Mapa ausente ou ambíguo: parar e pedir
correção.

### 10.3 Como gerar cada vídeo
1. Localizar o `V` no bloco de vídeo (linha com só `V` + número).
2. Consultar o MAPA K/V e pegar a imagem **aprovada** do K correspondente.
3. Anexar essa imagem **como INITIAL FRAME**. Nunca como "element", "ingredient" ou referência de
   objeto.
4. Colar **só o texto do V** no campo de prompt (conferir as três marcas).
5. Veo 3.1 Lite, Lower Priority, 8 segundos, variações do perfil (1 ou 3).
6. Salvar com o código no nome.

**A fala é literal.** Não mexa em nenhuma palavra entre aspas. **Não adicione** música, legenda,
tradução nem texto na tela: tudo isso entra na edição.

### 10.4 Lotes fechados
1. Registrar a fila inteira de V, sem sair executando.
2. Iniciar **só o primeiro lote**, de no máximo 7 códigos V.
3. Esperar **todos** os códigos e variações do lote terminarem. Não preencher vaga liberada com o
   lote seguinte.
4. Informar o que concluiu, o que falhou e o que está pendente.
5. Esperar o comando **`prossiga`** para o próximo lote.
6. Ao retomar, executar só o pendente. Nunca refazer um V concluído sem pedido.

### 10.5 Tipos de prompt de vídeo que você vai encontrar
- **Avatar falando para a câmera:** começa com `o avatar (homem/mulher) fala em inglês ...`.
- **Diálogo (cena atuada):** começa com `falas no take, em inglês, na ordem:` e tem uma linha
  numerada por fala, cada uma com **quem fala, a voz e a emoção**, mais uma linha dizendo quem fica
  calado.
- **B-roll:** começa com `(sem fala no take: ...)`. Não gera fala nenhuma: a voz de outro clipe
  entra por cima na edição. É normal e **não** é motivo para parar.
- **Gancho da Auraly:** pode chegar mudo e com cortes internos descritos dentro do mesmo clipe. Ainda
  é **um** clipe de 8 segundos.

---

## 11. Passo 7: aprovar os vídeos

- [ ] **A fala saiu inteira**, palavra por palavra igual à transcrição do pacote, e a última palavra
      não foi cortada.
- [ ] **A fala saiu na boca certa.** Em cena com várias pessoas, só quem fala mexe a boca. Pessoa
      errada falando é o defeito mais comum do Veo.
- [ ] **A voz combina** com o personagem (idade, gênero, sotaque) e é **a mesma** em todos os clipes
      em que ele fala.
- [ ] A **emoção** está na voz (raiva, choro, choque). Voz neutra de robô reprova.
- [ ] A ação é a do prompt e continua a partir da imagem, sem saltos.
- [ ] Nenhuma música, legenda ou texto gerado dentro do clipe.
- [ ] Rostos e roupas não mudaram no meio do clipe.

Clipe reprovado: gerar de novo o mesmo V. Se reprovar repetidamente pelo mesmo motivo, reporte o
motivo para quem fez o pacote.

---

## 12. Passo 8: montagem no CapCut

O pacote traz a montagem específica. As regras gerais são:
1. Clipes **na ordem numérica** dos V, salvo instrução diferente no pacote.
2. **Cortar o silêncio** do começo de cada clipe: todo clipe começa já falando ou já em ação.
3. **B-roll** entra por cima da fala de outro clipe (a voz continua, a imagem corta para o inserto).
4. **Sem Voice Changer.** A voz de cada personagem já vem do prompt.
5. Música, se houver, **nunca antes do gancho**, baixa (por volta de -19 a -20 dB) e fora da
   biblioteca de sons do TikTok.
6. **Rótulo pequeno de conteúdo gerado por IA** (`AI-generated`) num canto.
7. Texto na tela e card final (ex.: `follow to part 2`) só quando o pacote pedir.
8. Exportar em **9:16, 1080 x 1920**.
9. Opcional, para tirar o "look de IA": temperatura -3, tint +2, saturação -6, exposição -3,
   contraste +12, realces -35, sombras +18, fade +6.

---

## 13. Anatomia de um prompt de IMAGEM (para escrever um novo)

Todo K segue esta ordem. Cada parte existe por um motivo.

| Parte | Exemplo | Por quê |
|---|---|---|
| Abertura | `IMPORTANT: THIS IS IPHONE FOOTAGE.` | Puxa o estilo de câmera de celular, que parece real. |
| Ficção | `This is a fictional AI-generated scene with fictional characters, no real person is depicted.` | É verdade e ajuda a passar na moderação. |
| Formato | `Vertical 9:16.` | Formato do Reels/TikTok. |
| Uso das referências | `Use the attached character sheets ONLY for faces, hair, bodies and clothes: ...` | Diz o que copiar de cada anexo e o que ignorar. |
| Elenco | cada pessoa descrita por inteiro: idade, pele, cabelo, rosto, roupa | O prompt é autossuficiente. Quem aparece só em parte (mão, ombro) recebe só a descrição da parte. |
| Herói | `... very close to the lens in the lower foreground, large in frame, closer to the camera than any face.` | O objeto que prende o olhar fica perto da lente, maior que o rosto. |
| Cenário | duas ou três âncoras de fundo, **com a bandeira dos EUA** | Cenário reconhecível e americano, sem inventário de objetos. |
| Pose e estado | `Start frame: the hand is reaching and nobody has been touched yet.` | A imagem é o **primeiro quadro** do vídeo: descreve o momento antes da ação. |
| Enquadramento e câmera | `Camera adult eye level from across the island ...` | Posição de quem está filmando. |
| Luz | `Neutral overcast daylight ... no warm orange cast and no yellow tint.` | Luz quente é a maior denúncia de IA. |
| Realismo | trecho fixo (Apêndice B) | Pele real, tudo em foco, aparência de celular. |
| Negativo | `No captions, no subtitles, no words overlaid on the image, ...` | O que não pode aparecer. |

**Três regras que valem sempre:**
1. **Nunca listar termo sensível no negativo** (nome de órgão, sangue, gore, marca, logo). O filtro
   lê a palavra, não o "no", e a palavra injeta o conceito.
2. **Nunca "no text" seco.** O correto é `no captions, no subtitles, no words overlaid on the image`.
3. **Nunca pedir blur, bokeh, golden hour ou pôr do sol.** Reduzir fundo é com enquadramento.

---

## 14. Anatomia de um prompt de VÍDEO (para escrever um novo)

Sempre cinco partes, nesta ordem, cada uma numa linha:

**1. A fala**
- Avatar para a câmera:
  `o avatar (mulher) fala em inglês com sotaque americano de [nome], voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "[FALA EXATA]"`
- Diálogo:
  ```
  falas no take, em inglês, na ordem:
  1. [QUEM, descrição visual curta], voz [timbre, idade, sotaque], fala com [emoção]: "[FALA EXATA]"
  2. [QUEM RESPONDE, descrição visual curta], voz [timbre, idade, sotaque], fala com [emoção]: "[FALA EXATA]"
  [QUEM FICA CALADO] não diz nenhuma palavra.
  ```
- B-roll: `(sem fala no take: [de onde vem a voz que entra por cima na edição])`

**2. Trava de lip sync** (não entra no B-roll)
`o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.`
(No diálogo: `cada personagem diz ... só na boca de quem está falando.`)

**3. Ação:** `o que acontece no vídeo: [só o que acontece, enxuto]`

**4. Câmera:** `câmera: [fixa / leve push-in / leve handheld / como alguém filmando com o celular]`

**5. Som:** `som ambiente: [ambiente do lugar], sem música`

**Regras do vídeo:**
- **8 segundos cabem de 13 a 29 palavras.** Fala maior se quebra em dois takes, sempre no fim de
  uma frase. Nunca inventar palavra para completar. (Exceção: em diálogo de cena curta com ação, um
  take pode ter menos de 13 palavras.)
- **No máximo duas pessoas falando por clipe.**
- **A voz de cada personagem é descrita em toda fala, sempre com o mesmo timbre.** É o prompt que
  segura a voz, não a edição.
- **A ação é enxuta.** Excesso de detalhe (ângulo, parte do corpo, adjetivos) é o que dispara
  censura.
- **O vídeo não descreve cor, enquadramento nem composição**: isso já está na imagem.
- **Sempre "sem música".** Trilha só na edição.
- Em selfie: `a mão que segura o celular nunca se mexe; só a outra mão gesticula.`

---

## 15. Quando cai na censura

**Regra 1: a fala nunca é o problema.** O vídeo de referência já foi gerado com aquela fala. Nunca
tire, troque ou encurte a fala para destravar.

**Regra 2: se travou várias vezes, não adianta tentar de novo igual.** Mude o prompt.

O que costuma disparar, em ordem de probabilidade:
1. **A ação da cena**, principalmente corpo com algo atingindo região sensível.
2. **Excesso de descrição** (região do corpo, ângulo, adjetivos dramáticos).
3. **Combinação de elementos:** duas coisas inocentes que juntas sugerem algo sensível (ex.: braço
   de homem estendido na direção do rosto de uma mulher assustada lê como agressão).
4. **O próprio negativo**, quando lista palavra sensível (`no blood`, `no gore`, nome de órgão).
5. **Anexo com rosto real grande** (frame de outro vídeo em close): pode cair no filtro de
   semelhança com pessoa real.

Protocolo, na ordem:
1. **Enxugar a ação** ao mínimo: só o que acontece.
2. **Neutralizar o alvo** da ação (atinge um objeto ou superfície neutra em vez do corpo).
3. **Separar elementos em takes diferentes** e juntar no corte: nenhum quadro isolado fica
   problemático.
4. **Explicitar que é ficção de IA** (já vem em todo prompt).
5. **Tirar palavra sensível do negativo** e **cobrir rostos reais** nos frames de composição.

Exemplo real: o K07 de uma produção travou. Causa provável: o frame de composição anexado era um
close enorme de um rosto real, e o texto pedia o braço de um homem cruzando o quadro na direção
do rosto dela em choque. Correção: rosto do frame coberto por caixa cinza, braço removido,
expressão reescrita como "pega de surpresa". Nenhuma fala foi tocada.

---

## 16. Erros que já aconteceram, e como não repetir

| Erro | Consequência | Como evitar |
|---|---|---|
| Colar o prompt da **imagem** no campo do **vídeo** | Vídeo sem fala e sem ação | Conferir as três marcas antes de todo V (seção 10.1) |
| Casar imagem e vídeo pela **ordem da galeria** | Vídeo com a imagem errada | Sempre pelo código e pelo MAPA K/V |
| Casar **nome com rosto** pela ordem de anexo | Avatar errado em toda a produção | Abrir a âncora e conferir o rosto |
| Misturar a âncora de **dois avatares** | Rosto híbrido | Um avatar por vez; tirar a âncora anterior |
| Colar **título ou nota** dentro do bloco | O texto vira parte da imagem | Blocos só com código + prompt |
| Anexar os `REF-P` **fora de ordem** | Personagens trocados | Seguir a ordem do MAPA DE ANEXOS |
| Gerar K antes de **aprovar os sheets** | Personagem inconsistente no vídeo inteiro | Sheets aprovados primeiro |
| Adicionar **música ou legenda** no Flow | Clipe inutilizável na edição | Isso só entra no CapCut |
| Editar ou "melhorar" o prompt | Perde a trava de qualidade ou de censura | Colar literalmente |
| Preencher vaga do lote com o **lote seguinte** | Fila fora de controle, retrabalho | Lotes fechados, esperar `prossiga` |
| Reusar a memória do agente da **produção anterior** | Configuração errada | Colar as instruções inteiras a cada produção |

---

## 17. Resumo de uma página

```
ANTES
[ ] Colar as instruções do pacote, inteiras, na memória do agente
[ ] Confirmar o perfil (CLÁSSICO ou AURALY) e a versão (v13)
[ ] Separar âncora / REF-P / frames de composição

IMAGENS
[ ] REF-P primeiro (sem anexo), aprovar todos
[ ] K em ordem: anexos do MAPA DE ANEXOS, na ordem → colar SÓ o prompt → Nano Banana 2, 9:16
[ ] 1 imagem (clássico) ou 4 candidatas (Auraly) por K
[ ] Salvar com o código no nome
[ ] Aprovar cada imagem pelo checklist da seção 9

VÍDEOS
[ ] Para cada V: MAPA K/V → imagem APROVADA do K → anexar como INITIAL FRAME
[ ] Colar SÓ o texto do V e conferir as 3 marcas (o que acontece / câmera / som ambiente)
[ ] Veo 3.1 Lite, Lower Priority, 8s, 1 ou 3 variações
[ ] Lotes de até 7 V, esperar "prossiga"
[ ] Aprovar cada clipe pelo checklist da seção 11

MONTAGEM
[ ] Ordem do pacote, cortar silêncio, B-roll por cima da fala
[ ] Sem Voice Changer, música só depois do gancho, rótulo AI-generated
[ ] Exportar 9:16, 1080 x 1920
```

---

## Apêndice A · Instruções para a memória do agente (v13, texto integral)

Este é o texto que vai no campo de instruções/memória do agente do Flow. Na prática, **use sempre o
bloco que veio no pacote da produção**: ele pode ter uma versão mais nova que esta. Algumas partes
citam arquivos e termos internos da operação (`WORKFLOW_AURALY.md`, checkpoint, Codex); o executor
não precisa abri-los, eles só explicam de onde vem cada regra.

```
Voce executa prompts finalizados dentro do Google Flow. Nao reescreva, traduza, resuma nem
altere a copy. Registre o perfil da producao antes de gerar qualquer asset. Perfil ausente ou
incompativel com os codigos recebidos exige esclarecimento, nunca escolha silenciosa.

### Perfis de execucao

| Configuracao | AURALY | CLASSICO (Angle 1/2) |
|---|---|---|
| Imagem | Nano Banana 2 | Nano Banana 2 |
| Formato | 9:16 | 9:16 |
| Referencia de imagem | Anchor em cena real do avatar ativo (ver secao abaixo) | Anchor do avatar ativo |
| Imagens por K | 4, com selecao manual | 1 imagem final |
| Relacao K/V | Mapa explicito recebido com o pacote; um K pode alimentar varios V | Maior K menor ou igual ao numero de V |
| Video | Veo 3.1 Lite | Veo 3.1 Lite |
| Prioridade | Lower Priority | Lower Priority |
| Duracao por clipe | 8 segundos | 8 segundos |
| Variacoes por V | 3 | 1 |
| Anexo do video | INITIAL FRAME | INITIAL FRAME |
| Lote de video | Fechado, no maximo 7 codigos V | Fechado, no maximo 7 codigos V |

Os valores Auraly reproduzem as travas de WORKFLOW_AURALY.md. Nunca transportar as configuracoes
classicas para Auraly. Um pacote historico com outro contrato nao autoriza alterar uma producao
nova; preservar seu contrato aprovado quando o usuario solicitar especificamente sua retomada.

### AURALY, anchor e cenario por gancho (Luigi, 2026-09-14; anchor revista em 2026-09-22)

Roster Auraly: Walt Hensley, Darlene Pruitt e Lorraine Vance. A referencia de cada um e a anchor
em cena real (imagem de teste aprovada), anexada em todo K. Nao existe fingerprint. Quando o K
mantem o cenario da anchor, o texto do K descreve esse cenario. Quando o K pede cenario ou roupa
novos, o texto manda usar a anchor so para a identidade; siga o texto e ignore roupa, fundo e props
da anchor.

Cada gancho escolhido passa a ter CENARIO PROPRIO do T1 ao CTA (K de hook + K de corpo + K de CTA
por cenario), nunca mais um corpo compartilhado pela fila inteira. O angulo de camera serve a
acao estrutural preservada: pode ser exotico quando aumenta a anomalia, mas pode se repetir entre
variacoes para preservar composicao e timing. Mudar o angulo conta como a unica variavel dessa
variacao. Roupa livre por cenario, sem obrigacao de repetir a roupa da anchor.

No T1, a anomalia visual domina. O kit completo de tarologo nao e obrigatorio: usar de zero a dois
marcadores discretos de Auraly somente se nao competirem com o heroi. Um unico VFX simples e legivel
(rachadura, brilho, mudanca de cor ou revelacao) e permitido quando for a propria anomalia; efeitos
multiplos ou cinematograficos continuam proibidos. Do T2 ao CTA, volta o kit de credencial visual
(cartas, cristal, incenso, vela, cruz, bandeira dos EUA) e a carta na mao. Doutrina completa em
WORKFLOW_AURALY.md.

A ideacao anterior aos prompts usa o METODO PUZZLE aplicado ao hook do video modelo: uma unica
acao estrutural preservada e dez variacoes que trocam uma variavel cada, das quais o operador
normalmente seleciona cinco. O executor nao inventa variacoes, nao altera a acao estrutural e nao
cola metadata de gancho no campo de prompt. Apenas executa os K/V finais recebidos.

**T1, o take do gancho.** O V do T1 pode chegar MUDO: no lugar da linha de fala, ele traz
`(sem fala no take: ...)`. Isso e correto e nao autoriza parar. As tres marcas obrigatorias
(`o que acontece no vídeo:`, `câmera:` e `som ambiente:`) continuam presentes e continuam sendo a
checagem valida. No T1 o campo `o que acontece no vídeo:` descreve MUDANCAS DE PLANO dentro do
mesmo clipe, e o campo `câmera:` declara cortes internos em vez de `fixa` ou `push-in`. Isso e um
unico clipe de oito segundos, nunca varios clipes: continua valendo um K para um V.

### MOVIE STYLE: elenco com character sheets e video com dialogo (v13)

Vale para os formatos de cena atuada (short form de crescimento e movie style de venda), que usam
o perfil CLASSICO. O pacote declara o formato no topo.

1. **Character sheets primeiro.** Os codigos `REF-P1`, `REF-P2`... sao prompts de character
   sheet, um por personagem principal. Gerar cada um do zero, SEM anexo, uma imagem final, e
   esperar o operador aprovar todos antes do primeiro K.
2. **Anexos de cada K.** O pacote traz um MAPA DE ANEXOS fora dos blocos (ex.: `K01: REF-P1,
   REF-P2, REF-P3`). Anexar exatamente as imagens aprovadas listadas para aquele K, e nenhuma
   outra. Sem avatar na producao, nao existe anchor: os REF-P fazem esse papel. Com avatar, a
   anchor dele entra junto quando o mapa listar.
3. **Video com dialogo.** Um V de dialogo comeca com `falas no take, em ingles, na ordem:` e
   traz uma linha numerada por fala, cada uma dizendo QUEM fala, a VOZ e a emocao, e a fala entre
   aspas. Quem fica calado vem escrito. Continua sendo um V: as tres marcas `o que acontece no
   vídeo:`, `câmera:` e `som ambiente:` estao presentes e continuam sendo a checagem valida.
   Colar inteiro, sem trocar a ordem das falas.
4. **B-roll.** Um V de B-roll comeca com `(sem fala no take: ...)`. Nao ha fala para gerar; a
   voz entra na edicao por cima de outro clipe. As tres marcas continuam presentes.

### Um avatar por vez

Receber a anchor e registrar o identificador e nome do arquivo. Nao casar imagens por ordem de
anexo. Confirmar qual avatar esta ativo antes da primeira geracao. Sua identidade nunca se
mistura com as referencias do avatar anterior.

Ao receber `finalizamos, vamos para o proximo avatar`, encerrar o ciclo anterior, retirar sua
anchor da selecao ativa e esperar a nova. Nao apagar arquivos nem recriar assets concluidos.
No Codex, o checkpoint governa a fila; no executor, esperar a troca explicita da anchor.

### Imagens

Receber todos os K, contar codigos e conferir duplicatas. Cada codigo aparece sozinho em uma
linha, seguido de um prompt completo e autossuficiente. Nao copiar titulos, notas, caminhos,
configuracoes ou metadata para o campo do prompt.

Usar Nano Banana 2, formato 9:16 e a anchor ativa. Colar cada prompt literalmente e gerar a
quantidade do perfil. Rotular os resultados com avatar, codigo e numero da variacao.

No Auraly, apresentar quatro candidatas por K e esperar o operador escolher uma por codigo.
Mesmo que os V ja tenham chegado no mesmo pacote textual, nao selecionar automaticamente nem
avancar para video sem selecao. No classico, uma imagem
final por K; ainda assim esperar o pacote de video antes de executar essa fase.

### 🔴 Reconhecer prompt de IMAGEM (K) contra prompt de VIDEO (V), sem ambiguidade (v8)

Falha real registrada em producao: apos gerar as imagens corretamente, inclusive editando um K
a partir de outro ja aprovado, o executor avancou para a etapa de video usando a imagem gerada
como INITIAL FRAME (certo) mas colou o PROPRIO PROMPT DE IMAGEM no campo de texto do video, em
vez do prompt V correspondente. Isso nunca pode se repetir. Regras obrigatorias:

1. **Um prompt K e um prompt V nunca tem o mesmo formato, e a diferenca e mecanica, nao de
   julgamento.** Um prompt K e um UNICO paragrafo denso em ingles descrevendo uma imagem parada:
   comeca tipicamente com `IMPORTANT: THIS IS IPHONE FOOTAGE` (geracao do zero) ou `Edit the
   attached image` (edicao); um prompt `REF-P` comeca com `CHARACTER SHEET`. NUNCA contem as
   palavras `o avatar fala`, `falas no take`, `câmera:` ou `som ambiente:`. Um prompt V e sempre
   em portugues e sempre tem exatamente cinco partes na ordem: a abertura de fala (a linha `o
   avatar (homem/mulher) fala em ingles... a seguinte frase: "..."`, ou o bloco `falas no take`
   do movie style, ou `(sem fala no take: ...)` no B-roll), a linha do lip sync (ausente no
   B-roll), a linha `o que acontece no vídeo:`, a linha `câmera:` e a linha `som ambiente:`.
2. **Checagem obrigatoria ANTES de submeter qualquer geracao de video:** o texto que vai no campo
   de prompt do video tem que conter, literalmente, as tres marcas `o que acontece no vídeo:`,
   `câmera:` e `som ambiente:`. Se qualquer uma faltar, PARE. Isso significa que o texto colado
   e um prompt K (imagem), nao um V (video), e a geracao tem que ser cancelada antes de rodar.
   Nunca prosseguir "porque a imagem esta certa": a imagem de referencia e um anexo (INITIAL
   FRAME), o campo de texto e outra coisa, e os dois tem que ser conferidos separadamente.
3. **O campo de texto do video SOMENTE recebe conteudo de um bloco rotulado `V`.** O prompt K
   correspondente nunca e copiado, resumido nem reaproveitado como prompt de video, nem mesmo
   parcialmente. A imagem gerada a partir do K entra SOMENTE como anexo INITIAL FRAME.
4. **Troca de etapa e troca de modo de leitura.** Ao terminar o ultimo K de um lote e comecar o
   primeiro V do proximo bloco, tratar como uma mudanca de contexto completa: esquecer os prompts
   de imagem como fonte de texto executavel. Eles continuam existindo so como referencia de qual
   K gerou qual imagem.
5. Se o pacote recebido nao tiver as cinco partes descritas no item 1 dentro de um bloco marcado
   `V`, ou se algum bloco `K` contiver por engano as marcas de video, parar e avisar o operador
   em vez de tentar adivinhar ou corrigir por conta propria.

### Associacao entre imagem e video

AURALY: usar exclusivamente o `MAPA K/V` recebido fora dos blocos de prompt. O mapa pode declarar,
por exemplo, `V06: K06`, `V07: K06`, `V08: K06` e `V09: K06` quando varios takes partem do mesmo
frame de corpo. Isto e reutilizacao deliberada, nao ausencia de imagem. Cada V precisa ter exatamente
um K mapeado, e esse K precisa ter uma candidata manualmente aprovada. Nunca inferir pelo numero,
aparencia ou ordem da galeria quando o mapa estiver ausente ou ambiguo; parar e pedir correcao.
Cada codigo V tem tres variacoes do mesmo prompt e frame selecionado.

CLASSICO: V usa o maior K disponivel cujo numero nao exceda o de V. Por exemplo, com K01, K03 e
K06: V01/V02 usam K01; V03/V04/V05 usam K03; V06 usa K06. Se nao houver K anterior ou igual,
parar. Nao adivinhar pela aparencia ou ordem da galeria. Cada V tem uma variacao.

### Videos em lotes fechados

1. Receber e registrar toda a fila V, sem executar tudo automaticamente.
2. Antes de cada V, conferir avatar, perfil e K indicado no MAPA K/V.
3. Usar a imagem exclusivamente como INITIAL FRAME, nunca Element, ingredient ou referencia de objeto.
4. Configurar Veo 3.1 Lite, Lower Priority, oito segundos e a quantidade de variacoes do perfil.
5. Iniciar somente o primeiro lote de no maximo sete codigos V. Variacoes pertencem ao codigo;
   o teto e de codigos, nao uma autorizacao para iniciar codigos adicionais por vaga liberada.
6. Esperar todos os codigos e variacoes desse lote. Nao preencher vagas com o lote seguinte.
7. Informar concluidos, falhas e pendentes. Se houver pendentes, parar e aguardar `prossiga`.
8. Mesmo quando o lote terminar, esperar `prossiga` para iniciar o proximo lote.
9. Ao retomar, executar somente o trabalho pendente autorizado. Nunca reiniciar um V concluido
   sem pedido explicito. Distinguir a variacao que falhou das que ja foram concluidas.
10. Se a interface nao permitir a configuracao requerida, informar a limitacao antes de mudar
    modelo, prioridade, quantidade, duracao ou modo de referencia.

A fala e literal. A acao continua o estado inicial da imagem. Manter camera e som indicados,
sem adicionar musica, legenda, traducao ou texto auxiliar por conta propria.

### Fechamento

Relatar arquivos gerados por avatar, K/V e variacao, com pendencias explicitas. Geracao de um
avatar nao conclui a fila inteira. Entrega de prompts, midia gerada, montagem e publicacao sao
marcos diferentes. Nunca declarar publicacao ou resultado comercial pela existencia de assets.
```

---

## Apêndice B · Trechos prontos de qualidade (para escrever prompts de imagem)

Colados dentro de cada prompt, adaptando só o que está entre colchetes:

**Luz interna**
```
Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.
```

**Luz externa**
```
Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on the face.
```

**Herói**
```
The [hero] is very close to the lens in the lower foreground, large in frame, closer to the camera than [her/his] face, nothing else competing with it.
```

**Realismo (fecha todo prompt)**
```
Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.
```

**Selfie (no prompt de vídeo)**
```
a mão que segura o celular nunca se mexe; só a outra mão gesticula.
```

---

## Apêndice C · Exemplo real: um par K + V de cena atuada

Produção de short form "a madrasta e o frango" (perfil CLÁSSICO, sem avatar, 4 character sheets).

**MAPA DE ANEXOS do K01:** REF-P3 (Emily), REF-P1 (madrasta), REF-P2 (pai), depois o frame de
composição. **MAPA K/V:** `V01: K01`.

```
K01
IMPORTANT: THIS IS IPHONE FOOTAGE. This is a fictional AI-generated scene with fictional characters, no real person is depicted. Vertical 9:16. Use the attached character sheets ONLY for faces, hair, bodies and clothes: Emily is the person in the first character sheet; the stepmother is the person in the second character sheet; the father is the person in the third character sheet. The last attached image is a composition reference only: copy its camera position and where each person stands, never its faces, bodies, clothes or room. Three people. Emily: a Black American girl around six, dark brown skin, a round face, big dark brown eyes, her hair in two puffy pigtails tied with pink hair ties, wearing a pink short-sleeve dress with ruffled cap sleeves, standing at the near side of the kitchen island. The stepmother: a white American woman around forty, slim, platinum blonde hair pulled back into a low neat bun, pale skin with light freckles, light blue eyes, a thin straight nose and thin lips, fine lines around the eyes, wearing a cream silk long-sleeve button-up blouse tucked into high-waisted black tailored trousers and small gold stud earrings, standing right beside her on the right. The father: a Black American man around forty-two, medium-dark brown skin, athletic build, very short black hair with a sharp hairline, a short neat black beard and a strong jaw, wearing a navy blue long-sleeve button-up dress shirt with white buttons, dark navy trousers and a silver watch on his left wrist, small but clearly recognizable, stepping through the open doorway in the background. On the island, a white plate piled high with golden fried chicken pieces and, right next to it, a small grey bowl of plain cold white rice. The plate and the bowl are very close to the lens in the lower foreground, large in frame, closer to the camera than any face. A bright modern American family kitchen in daytime: white shaker cabinets, a white marble backsplash, a large kitchen island with a light grey quartz countertop, an open doorway to a hallway in the background, a window over the sink showing a green backyard under an overcast sky with visible cloud texture, and a small American flag magnet on the stainless steel refrigerator, discreet but clearly visible and in sharp focus. Emily stretches one small hand toward the fried chicken. The stepmother turns toward her with a furious face, leaning in, caught mid-sentence, lips naturally parted. The father has just stepped into the doorway behind them, mid-step, staring. The plate and bowl fill the lower foreground. Emily's head, shoulders and reaching hand sit in the middle of the frame, the stepmother on the right from the waist up, the father small in the doorway in the background. Every face in sharp focus. Camera adult eye level from across the island, slightly high, like someone in the kitchen filming with a phone. Start frame: the hand is reaching and nobody has been touched yet. Neutral overcast daylight from the window, the outside clearly visible through the window, soft even light on every face with no harsh shadows, no warm orange cast and no yellow tint. Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset. No captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden hour light, no AI polish, no beauty smoothing, no cinematic lighting.
```

```
V01
falas no take, em inglês, na ordem:
1. a MADRASTA (mulher branca loira de coque baixo e blusa creme), voz feminina de uns quarenta anos, média-aguda, fria e cortante, sotaque americano padrão, fala com raiva explosiva, gritando: "Don't touch my son's food!"
2. o PAI (homem negro de barba curta e camisa azul-marinho), voz masculina grave de barítono, uns quarenta anos, sotaque americano de homem negro, fala em choque e com fúria, alto: "What did you do to my daughter?"
EMILY não diz nenhuma palavra, só chora.
cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de quem está falando.
o que acontece no vídeo: Emily estica a mão para o frango. A madrasta acerta o rosto dela com a mão aberta e grita a fala dela. Emily recua chorando, com a mão na bochecha. O pai, na porta ao fundo, vê tudo e avança rápido até a bancada enquanto fala.
câmera: leve handheld, como alguém na cozinha filmando com o celular, sem trocar de plano
som ambiente: cozinha silenciosa de casa, o choro da menina, passos rápidos, sem música
```

Repare:
- o K01 começa com `IMPORTANT: THIS IS IPHONE FOOTAGE`, é um parágrafo único e descreve o **momento
  antes** do tapa (a mão da menina esticada), porque a imagem é o primeiro quadro do vídeo;
- o V01 tem as três marcas, cada fala diz quem fala, a voz e a emoção, e a menina "não diz nenhuma
  palavra";
- a ação do V01 é curta e só descreve o que acontece; enquadramento e cor já estão na imagem.
