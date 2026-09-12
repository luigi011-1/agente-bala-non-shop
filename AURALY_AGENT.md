# Auraly Agent

> **ÂNGULO 3 SOMENTE.** Este arquivo define o pipeline de produção exclusivo do ângulo Auraly (app
> de manifestação de alma gêmea). Ângulos 1, 2 e 4 nunca leem este arquivo nem seguem este fluxo.
> Para os outros ângulos, ver o fluxo clássico em `CLAUDE.md`.

## Trigger curto

Luigi pode iniciar uma produção escrevendo apenas `/watch` e mandando os caminhos locais:

```text
/watch
video: C:\caminho\video.mp4
avatares:
- C:\caminho\avatar_1.jpeg
- C:\caminho\avatar_2.jpeg
```

Também vale mandar só uma lista de caminhos: o arquivo `.mp4` é o vídeo modelo, e arquivos de imagem
são os avatares selecionados no momento.

## O que o trigger autoriza

Ao receber `/watch`, o agente pode começar a produção completa sem pedir a frase longa:

1. analisar o vídeo modelo;
2. modelar a copy para a operação atual;
3. escrever roteiro, tabela bilingue, setups e roteiro so-fala;
4. sugerir e ordenar ganchos visuais;
5. preparar prompts de imagem por avatar;
6. gerar e salvar as imagens pelo ChatGPT no Chrome do Luigi (ver "Execução de imagens no Chrome");
7. escrever prompts para Flow / Veo 3.1 / Omni Flash;
8. manter os documentos de produção em `producao/<slug_da_producao>/` e salvar cada lote aprovado
   de assets em `C:\Users\luigi\Downloads\<avatar>_<YYYY-MM-DD>\`.

## Ordem do workflow, gates que travam

O trigger autoriza a produção inteira, mas ela roda em ordem fixa. Cada gate abaixo trava o próximo
passo: nada de imagem antes de copy validada, nada de copy validada antes dos ganchos escolhidos.
Pular etapa aqui foi o erro que mais atrasou a produção quando este fluxo migrou do Codex.

1. **`/watch`**: extração de frames por corte, timeline densa a 0,2s, transcrição Whisper. Rodar o P1
   antes: esse esqueleto já foi produzido?
2. **Análise**: cruzar transcrição, timeline e frames de pico. Fechar o mecanismo criativo, o herói do
   hook e a função de cada beat.
3. **Modelagem de copy pelo método puzzle**: esqueleto preservado, só a variável da promessa troca.
4. **GATE, validação da copy**: entregar o roteiro completo no chat e **esperar Luigi aprovar ou pedir
   ajuste**. Não avançar para ganchos nem imagens antes desse "aprovado".
5. **Sugestões de gancho visual**: 8 a 10 opções, ações chamativas e legíveis no primeiro frame, que
   servem para todos os avatares. Entregar no chat, ordenadas por congruência.
6. **GATE, escolha dos ganchos**: Luigi escolhe 5. Só com os 5 números na mão a produção de imagem
   começa.
7. **Lote de imagem por avatar**: 5 hooks + 1 body + 1 CTA de uma vez, no Chrome (ver seção própria).
8. **GATE, aprovação do lote**: Luigi aprova as 7 imagens de um avatar antes de o próximo lote abrir.
9. **Fechamento do lote**: pasta datada em Downloads + prompts de vídeo no chat, antes do próximo avatar.

O gancho vive no T1. Do T2 em diante a copy é idêntica entre avatares e os takes se reaproveitam, então
cada avatar novo custa pouco: muda identidade, âncora e as ações específicas dos hooks.

## Troca de avatares

Os avatares podem mudar a qualquer momento. Se Luigi mandar novos caminhos de avatar durante a mesma
produção, o agente continua o processo com esses avatares, preservando roteiro, copy e hooks quando
fizer sentido. Ajustar apenas identidade, voz, prompts, imagens e pastas do avatar. Não tratar a troca
como erro e não reiniciar o processo do zero.

## Marcador de pipeline

Todo `ROTEIRO.md` de produção Auraly começa com a linha `pipeline: auraly` (antes de qualquer seção,
sem comentário, sem indentação). Este marcador é lido pelo `checar_entrega.py` para ativar o ramo
`checar_auraly()` e desativar as checagens do pipeline clássico (PROMPTS_PRODUCAO.md, DM.md,
nomenclatura K/V/REF). Sem o marcador, o linter roda o ramo clássico e reprova a produção por
arquivos ausentes. Pasta da produção: `producao/<slug>/`, sem prefixo de avatar — diferente do
clássico `producao/<avatar>_<slug>/`.

## Entrega esperada

Cada produção deve deixar arquivos locais organizados, no mínimo:

```text
producao/<slug_da_producao>/
  ROTEIRO.md              (pipeline: auraly na primeira linha)
  GANCHOS_VISUAIS.md      (8 a 10 opcoes, 5 escolhidas para gerar)
  PROMPTS_IMAGEM.md       (JSON por setup, agrupado por avatar)
  watch/
  MANIFEST.json
  <avatar>_<YYYY-MM-DD>/
    imagens/              (01_hook_*.png ... 06_body.png, 07_cta.png)
    PROMPTS_VIDEO_FLOW.md
```

O chat não substitui os arquivos, e os arquivos não substituem o chat. Entregar os dois.

### Regra de entrega no chat

Todo conteúdo que exige leitura, decisão, aprovação, cópia ou uso por Luigi deve ser enviado integralmente
na conversa, mesmo quando também estiver salvo em `.md`. Nunca responder apenas com link, resumo ou
instrução para abrir um arquivo.

Aplicação por gate:

1. Após `/watch`: enviar no chat a transcrição, a modelagem puzzle e o roteiro completo.
2. Antes de imagens: enviar no chat todas as opções de ganchos visuais e aguardar a escolha.
3. Para cada lote: mostrar no chat as imagens, os prompts relevantes e o resultado da revisão.
4. Ao finalizar: enviar no chat os prompts Flow, roteiro final e copy de Stories.

Os arquivos locais seguem sendo o arquivo-mestre organizado da produção, mas não são pré-requisito para
Luigi acompanhar ou aprovar o trabalho.

## Execução de imagens no Chrome

As imagens não são geradas pela ferramenta interna do chat. São geradas no ChatGPT web, dentro do
Chrome do Luigi. A geração interna só entra com pedido explícito dele.

### Ponto de entrada, sempre este

Abrir o navegador **somente** por este atalho, nunca por outro caminho nem por um Chrome já aberto:

```text
C:\Users\luigi\Desktop\Luigi (Luigi - CARDS MELODY) - Chrome.lnk
```

É o perfil `Luigi - CARDS MELODY`, com a sessão do ChatGPT Plus e a extensão de conexão já instaladas.

### Sequência do lote

1. Abrir o Chrome pelo atalho acima.
2. Abrir o ChatGPT no navegador e criar **uma conversa nova por asset**. Um lote padrão por avatar são
   **7 conversas**: 5 hooks escolhidos + 1 body + 1 CTA. Abrir todas antes de mandar prompt.
3. Em cada conversa, anexar a imagem-âncora do avatar vigente.
4. Colar o prompt específico daquele asset (JSON completo, ver seções abaixo).
5. Disparar as 7 gerações em paralelo, uma por aba.
6. Revisar visualmente cada resultado no navegador.
7. Baixar e salvar o aprovado. Identificar cada arquivo pela URL assinada do próprio ChatGPT e salvar
   já com o nome certo, sem depender dos nomes aleatórios da pasta Downloads.

### Conversa nova por cena, não reaproveitar

Cada geração é uma conversa nova. Reaproveitar a mesma conversa mantém as imagens anteriores no
histórico e isso contamina roupa, cenário e composição do próximo pedido, mesmo anexando só a âncora.
A aba é o espaço do avatar; a conversa dentro dela muda a cada asset.

### Anexar a âncora: colar, não pelo seletor de arquivo

Forma padrão, mais rápida e sem depender de permissão: dar `Ctrl+C` na imagem-âncora e `Ctrl+V`
clicando no campo de chat do ChatGPT. Cola a mesma imagem em todas as 7 abas.

Alternativa, para upload automático pelo seletor: ativar uma vez a permissão da extensão em
`chrome://extensions` → Detalhes da extensão → **Permitir acesso a URLs de arquivo**
(`Allow access to file URLs`). É permanente para o perfil e serve todos os avatares seguintes.

### Trabalhar uma aba por vez

Interagir com uma aba por vez, deixando as gerações já enviadas correndo nas outras. Enviar para a
aba 1, depois a 2, e assim por diante; voltar para revisar e baixar conforme cada uma termina. Isso
evita disputa pelo campo de texto e pelo seletor de anexo. As gerações não precisam terminar juntas.

Antes de cada envio, confirmar três coisas: aba ligada ao avatar certo, conversa nova, âncora
correspondente ao prompt. Se não der para confirmar alguma, pausar aquela fila.

### Fechamento obrigatório de lote aprovado

Ao aprovar um lote, criar a pasta final em `C:\Users\luigi\Downloads\` com o nome normalizado da avatar
e a data no formato `avatar_YYYY-MM-DD`. Copiar para `imagens\` dessa pasta todos os assets baixados e
nomeá-los pelo tipo de take. Em seguida, antes de passar para a próxima avatar, entregar no chat e salvar
na mesma pasta os prompts de vídeo de todos os takes finais, no formato Flow / Veo 3.1 de cinco blocos
definido no `CLAUDE.md`. Para hooks alternativos, escrever um V01 por variação e marcar que apenas um entra
em cada vídeo final. `producao/<slug>/` pode manter cópias de trabalho e documentação, mas Downloads é o
destino final obrigatório dos assets aprovados.

### Recuperação de falha de geração

Se uma geração falhar, manter a aba daquele asset e iniciar uma tentativa completa nela: anexar novamente
a imagem-âncora do avatar vigente e colar novamente o prompt específico daquele hook, body ou CTA. Nunca
reenviar apenas o texto ou acionar uma repetição sem renovar a referência visual.

Sinal de falha: a resposta do ChatGPT `Não consegui gerar a imagem por causa de um erro aqui`.
Isso pode ocorrer pontualmente quando o lote é disparado em paralelo. O erro de uma aba não bloqueia as
outras: deixar as gerações saudáveis terminarem e recuperar somente as abas falhas. A recuperação segue
esta ordem exata: `Adicionar arquivos e mais` → `Enviar do computador` → anexar a âncora novamente →
confirmar que o nome do arquivo aparece no compositor → colar o prompt do asset → clicar em `Enviar
prompt` → verificar que a aba saiu do estado de erro.

## P5 obrigatório: gates antes do prompt de imagem

Antes de escrever ou enviar qualquer prompt de imagem, rodar os dois gates abaixo. Eles são obrigatórios
para cada setup e para cada edição; não existe etapa de geração de imagem que os pule.

### Gate de realismo

1. Partir sempre da imagem-âncora real anexada da avatar vigente.
2. Isolar o herói no lower foreground e descrevê-lo como elemento mais próximo que o rosto; limitar o
   cenário a duas ou três âncoras reconhecíveis.
3. Usar luz diurna neutra, difusa, de dia nublado. Proibir `warm orange color cast` e `yellow tint` no
   campo `negative`; acrescentar `no golden glow` quando aplicável.
4. Evitar céu limpo/azul e paletas quentes que denunciem imagem sintética.
5. Exigir UGC realista: textura de pele, poros, fios individuais, rugas sutis, sombras e reflexos reais,
   aparência de filmagem de iPhone, sem retoque de beleza, sem plasticidade e sem blur.
6. Quando uma variação não atingir o nível, regenerar a partir da mesma referência e do mesmo setup. O
   realismo vem do volume de boas regenerações, não de sorte em uma primeira tentativa.

### Gate de composição visual

Conferir estes dez pontos no prompt e na revisão: (1) herói no lower foreground, mais perto que o rosto;
(2) nada compete com ele; (3) volume/cobertura estão explícitos; (4) perguntar se pode ficar ainda mais
perto; (5) avatar em chest-up ou shoulders-up; (6) CTA é o take mais próximo do vídeo; (7) cenário é
reconhecível, nunca inventariado, com duas ou três âncoras; (8) reduzir o fundo pelo enquadramento, nunca
por blur; (9) menos elementos para melhorar a qualidade; (10) se houver segunda pessoa, ela fica cortada
pelo quadro, nunca em corpo inteiro.

## Padrão obrigatório de prompts de imagem em JSON

Cada pacote começa com um **índice de geração**: take, ação (`GERAR DO ZERO` ou `EDITAR do K__`) e
anexos. Todo prompt enviado ao ChatGPT começa com um título de ação e referências em caixa alta, por
exemplo `## IMAGEM C · T8 A T19 · GERAR DO ZERO · ÂNCORA SHELBY + REF-CARTA`. As referências ficam no
próprio título, nunca escondidas em legenda. Abaixo, incluir o bloco visual `📎 ANEXAR: N IMAGENS`,
listando cada imagem numerada, com caminho ou keyframe de origem. Só então indicar `🆕 GERAR DO ZERO` ou
`✏️ EDITAR`. Em qualquer risco de cascata, inserir no bloco: `🚫 NUNCA anexar o K__ aqui`.

Gerar do zero somente o primeiro keyframe de cada setup. Todos os keyframes seguintes devem ser uma edição
do `K__` anterior para travar rosto, cenário e luz. Edições declaram que tudo deve permanecer idêntico,
listam apenas as mudanças permitidas e proíbem alterar a pele para mais escura, amarela ou alaranjada, bem
como aumentar a saturação.

O JSON de geração deve conter, no mínimo, `shot_id`, `reference_use`, `identity_main`, `wardrobe`,
`scene`, `posture`, `composition`, `camera`, `state`, `lighting`, `realism`, `aspect_ratio` e `negative`.
`reference_use` declara que a imagem anexada guia exclusivamente identidade/rosto/figurino/cenário e não
deve copiar pose ou enquadramento. O prompt deve declarar literalmente que o cenário da imagem-âncora deve
permanecer exatamente o mesmo: mesmos objetos, paredes, posições, enquadramento e luz. Nenhum item de
cenário pode ser removido, acrescentado, trocado ou reposicionado; apenas a ação e o herói visual
explicitamente autorizados podem mudar. Quando necessário, incluir `second_person` com a pessoa cortada pelo
quadro. Usar `"aspect_ratio": "9:16 vertical"`.

O JSON de edição usa `task` com `edit the attached image, keep everything identical except...`,
`keep_identical`, `change_1` e demais mudanças estritamente necessárias, além de `realism` e `negative`.
`keep_identical` sempre inclui cenário, objetos, parede, posições, enquadramento e luz exatamente como na
âncora. Nenhuma edição pode alterar o cenário fora da mudança explicitamente autorizada.
O `negative` parte de `no text, no captions, no words on screen, no studio, no plastic skin, no extra
fingers, no supernatural lighting, no blur, no artificial lighting` e recebe as restrições de cor do Gate
de Realismo.

### Templates canônicos do Claude Code

Usar a estrutura abaixo literalmente; só substituir os campos entre colchetes. Para uma demo/hook com
prop, nenhum campo é omitido:

```json
{
  "shot_id": "[S1_hook_initial]",
  "reference_use": "Use the attached image ONLY for [AVATAR]'s face, identity, wardrobe, and the exact [SCENE] scene. Keep the attached scene exactly identical: same objects, walls, positions, framing and lighting. Do NOT copy its pose or action.",
  "identity_main": "The EXACT [man/woman] from the attached reference image ([AVATAR]): [CANONICAL TRAITS].",
  "wardrobe": "[CANONICAL WARDROBE AND ACCESSORIES].",
  "scene": "SAME [SCENE] as [AVATAR]'s reference image, unchanged: [only two or three grouped anchors].",
  "posture": "[POSTURE].",
  "composition": "Waist-up. [HERO/PROP] sits in the lower foreground, closer than the face. [AVATAR ACTION WITH PROP].",
  "camera": "chest level, slightly high toward the [PROP]",
  "state": "Start frame: [INITIAL INSTANT OF THE ACTION].",
  "lighting": "[LIGHT MATCHING THE ANCHOR SCENE].",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no text, no captions, no words on screen, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow"
}
```

Para talking head, manter exatamente os mesmos campos, mas usar `composition` como `Tight waist-up talking
head, subject fills the frame, [HAND GESTURE]` e `camera` como `eye level, straight-on`. Para insert sem
rosto, usar `reference_use`, `identity_main`, `scene`, `composition`, `camera`, `state`, `lighting`,
`realism`, `aspect_ratio` e `negative`, declarando `No face` e `macro close-up`.

O template de edição canônico é:

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep [PERSON] exactly the same: same face, hair, skin tone, wardrobe, body position and pose. Keep the SAME background exactly: same walls, furniture, objects, positions, framing, lighting and camera angle from the attached image.",
  "change_1": "[THE ONE APPROVED CHANGE]. Do not change [LOCKED ELEMENTS].",
  "change_2": "[OPTIONAL SECOND APPROVED CHANGE].",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "negative": "do not change the face, identity, skin tone, background, object positions, framing, lighting or camera angle. Do not make their skin darker, yellowish or orangish. Do not make the colors more saturated. no text, no captions, no words on screen, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow"
}
```

`anthropic-skills:avatar-realista` fica reservado ao Higgsfield Soul para criação de rosto/avatar. Ele não
substitui estes gates nem o JSON no pipeline de assets para os vídeos.

## Especificação mestre de imagem — CONHECIMENTO_PROMPT_IMAGEM

Fonte operacional: `C:\Users\luigi\Downloads\CONHECIMENTO_PROMPT_IMAGEM.md`. Esta seção substitui
qualquer resumo anterior sobre prompts de imagem quando houver divergência. O gabarito vivo e as memórias
do Claude Code continuam sendo consultados no P5, nesta ordem: `ROTEIRO.md` e `PROMPTS_PRODUCAO.md` do
gabarito, `workflow-entrega-gabarito`, checklist de composição, gate de realismo, `prompts-imagem-json`,
erros recorrentes, ficha canônica do avatar, regra de keyframe por setup e feedback de enquadramento.

### Lei de estrutura

1. Prompt de imagem é JSON completo. Prompt de vídeo é texto simples com fala, ação, câmera e som. Nunca
   misturar as duas linguagens.
2. Um `K__` é criado por setup/bloco, nunca automaticamente por take. Vários `T__` podem usar o mesmo
   `K__`, mas cada `T__` recebe seu próprio `V__`.
3. `GERAR DO ZERO` ocorre somente no primeiro keyframe de um setup. Variações de gesto, estágio ou estado
   usam `EDITAR do K__`; estágios retornam sempre ao K inicial aprovado, nunca encadeiam edições.
4. A nomenclatura não pode colapsar: `T__` é fala, `K__` é imagem, `V__` é clipe e `REF-__` é referência
   auxiliar de pessoa ou prop.
5. Todo pacote começa com índice de geração, trava global de identidade/continuidade, trava do prop e/ou
   segunda pessoa quando existirem, mapa de âncoras, prompts de imagem, prompts de vídeo, montagem e gates
   de aprovação.

### Formato visual de entrega

Todo prompt tem título em caixa alta com keyframe, takes atendidos, ação e referências. Imediatamente
abaixo, vem uma citação com `📎 ANEXAR: **N IMAGENS**`, cada referência numerada com caminho ou nome do
K/REF de origem, seguido de `🆕 GERAR DO ZERO` ou `✏️ EDITAR`. Em risco de cascata, declarar
`🚫 NUNCA anexar o K__ aqui`. A cena curta pode aparecer só depois desse bloco. O JSON inteiro vem em
bloco de código, pronto para copiar. Nunca entregar instrução de patch: ao mudar uma regra, reescrever
cada prompt afetado por inteiro, no chat e no arquivo.

### JSON de geração — campos canônicos

Usar `shot_id`, `reference_use`, `identity_main`, `wardrobe`, `scene`, `posture`, `composition`,
`camera`, `state`, `lighting`, `realism`, `aspect_ratio` e `negative`. Incluir `prop` quando houver
herói e `second_person` quando houver segunda pessoa. `reference_use` restringe cada referência ao que
ela pode emprestar; `prop` descreve forma, material, cor, tamanho e volume, nunca apenas um nome;
`state` é sempre o início da ação. A cena da âncora é preservada como a mesma cena, sem inventar
elementos. Poses e enquadramento são definidos no JSON do setup conforme o gate de composição.

Em toda cena com ambiente, `scene` carrega uma bandeira dos EUA discreta, visível e em foco, como uma das
âncoras do cenário. Exceção: `REF-__` de prop isolado. No Ângulo 3, preservar o kit agrupado de tarólogo:
cristais, incenso aceso, bandeira dos EUA, cartas, quadro astrológico, cruz e vela. O rosto da alma gêmea
nunca aparece no vídeo; se estiver no objeto, fica fisicamente obscurecido, nunca por blur de câmera.

### Blocos obrigatórios e negative

O campo `realism` usa o bloco expandido do documento, com poros, fios individuais, rugas sutis, sombras e
reflexos reais, aparência de iPhone, zero polimento e foco nítido em toda a imagem. `aspect_ratio` é
sempre `9:16 vertical`.

O negative-base é: `no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin,
no extra fingers, no supernatural lighting, no blur, no artificial lighting`. Nunca usar `no text` seco,
pois ele pode apagar sinalização canônica do cenário. Em edição, acrescentar a trava anti-skin-shift. O
negative só pode conter termos neutros; nunca inserir nele órgãos, gore, marcas, logos ou o nome do elemento
sensível que se quer evitar.

### Continuidade, revisão e restrições

O herói fica no lower foreground, mais próximo da lente que o rosto, com volume explícito e nada disputando
atenção. Fundo se reduz com enquadramento, nunca blur. Segunda pessoa é gerada e aprovada como `REF-__`
antes do keyframe principal e entra cortada pelo quadro. Reveal contínuo recebe uma só imagem no estado
inicial; transformações que o original corta usam K separados. Se o prop falhar, gerar o prop isolado,
aprovar como REF e reutilizá-lo.

Antes de aprovar cada imagem, checar: trava de referência, traços canônicos, negative correto, estado
inicial, volume do herói, continuidade da segunda pessoa, bandeira no cenário e ausência de texto
sobreposto. Um relato de bloqueio exige reescrita da ação/cena, nunca alteração da fala; não sugerir retry
cego.
