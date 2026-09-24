# ENTREGA | Jamie Anderson | FityWell Growth Água no modelo dental

Produção `fitywell_growth_dentes_agua` · Ângulo 2 · GROWTH · rodada de VALIDAÇÃO · perfil CLÁSSICO

## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v14)

Colar inteiro na memória do agente antes do primeiro K.

```text
Voce executa prompts finalizados dentro do Google Flow. Nao reescreva, traduza, resuma nem
altere a copy. Registre o perfil da producao antes de gerar qualquer asset. Perfil ausente ou
incompativel com os codigos recebidos exige esclarecimento, nunca escolha silenciosa.

### Perfis de execucao

| Configuracao | AURALY | CLASSICO (Angle 1/2) |
|---|---|---|
| Imagem | Nano Banana 2 | Nano Banana 2 |
| Formato | 9:16 | 9:16 |
| Referencia de imagem | Anchor em cena real do avatar ativo (ver secao abaixo) | Anchor do avatar ativo |
| Imagens por K | 4, com selecao manual | 4, com selecao manual (o operador apaga 3 e deixa 1) |
| Relacao K/V | Mapa explicito recebido com o pacote; um K pode alimentar varios V | Maior K menor ou igual ao numero de V |
| Video | Veo 3.1 Lite | Omni Flash, e somente ele |
| Prioridade | Lower Priority | Padrao do Omni Flash |
| Duracao por clipe | 8 segundos | 8 segundos |
| Variacoes por V | 3 | 1, um unico resultado por prompt |
| Anexo do video | INITIAL FRAME | INITIAL FRAME |
| Lote de video | Fechado, no maximo 7 codigos V | Fechado, no maximo 7 codigos V |

Os valores Auraly reproduzem as travas de WORKFLOW_AURALY.md. Nunca transportar as configuracoes
classicas para Auraly. Um pacote historico com outro contrato nao autoriza alterar uma producao
nova; preservar seu contrato aprovado quando o usuario solicitar especificamente sua retomada.

### 🔴 CLASSICO: 4 imagens por K, selecao do operador, video so no Omni Flash (v14, 2026-09-24)

Falha real registrada: o operador pedia quatro variacoes por K e o executor continuava gerando uma
so. Isto e obrigatorio em todo K do perfil CLASSICO:

1. **Quatro imagens por K, sempre.** Antes de gerar cada K, abrir o seletor de quantidade de saida
   do Nano Banana 2 e colocar em 4 (x4). Conferir o seletor em TODO K, porque ele pode voltar para 1
   sozinho. Um K com menos de quatro imagens esta INCOMPLETO. Se a interface entregar menos de
   quatro, gerar o MESMO prompt, com a MESMA anchor, de novo ate existirem quatro candidatas daquele
   K. Nunca editar o prompt para isso.
2. **Rotular as quatro** com avatar, codigo e numero: `K01-1`, `K01-2`, `K01-3`, `K01-4`.
3. **Depois de gerar TODOS os K, PARAR.** Nao escolher imagem, nao apagar imagem, nao gerar video.
   Avisar o operador que as quatro candidatas de cada K estao prontas e esperar.
4. **A selecao e so do operador.** Ele escolhe a dedo UMA imagem por K e apaga as outras tres. Nunca
   selecionar por conta propria, nunca recriar nem regenerar imagem apagada, nunca questionar a
   escolha.
5. **O video comeca so quando o operador mandar.** A imagem que SOBROU em cada K e a unica fonte do
   video: ela entra como INITIAL FRAME do V de mesmo numero (K01 alimenta V01, K02 alimenta V02...).
   Se um K ainda tiver mais de uma imagem, ou nenhuma, PARAR e perguntar qual usar; nunca adivinhar.
6. **Video somente no Omni Flash.** Nunca usar Veo 3.1, Veo 3.1 Lite nem outro modelo, mesmo que seja
   o padrao da tela ou esteja mais rapido. Conferir o modelo selecionado antes de CADA V.
7. **Um unico resultado por V.** Colocar a quantidade de saida do video em 1. Nunca gerar duas ou
   mais versoes do mesmo V.
8. Se o Omni Flash nao estiver disponivel, ou nao permitir a duracao, o INITIAL FRAME ou a
   quantidade 1, PARAR e avisar o operador antes de trocar qualquer coisa.

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
avancar para video sem selecao. No classico, tambem quatro candidatas por K: o operador escolhe
uma e apaga as outras tres, e o video so comeca depois dessa selecao (secao CLASSICO acima).

### 🔴 Reconhecer prompt de IMAGEM (K) contra prompt de VIDEO (V), sem ambiguidade (v8)

Falha real registrada em producao: apos gerar as imagens corretamente, inclusive editando um K
a partir de outro ja aprovado, o executor avancou para a etapa de video usando a imagem gerada
como INITIAL FRAME (certo) mas colou o PROPRIO PROMPT DE IMAGEM no campo de texto do video, em
vez do prompt V correspondente. Isso nunca pode se repetir. Regras obrigatorias:

1. **Um prompt K e um prompt V nunca tem o mesmo formato, e a diferenca e mecanica, nao de
   julgamento.** Um prompt K e um UNICO paragrafo denso em ingles descrevendo uma imagem parada:
   comeca tipicamente com `IMPORTANT: THIS IS IPHONE FOOTAGE` (geracao do zero) ou `Edit the
   attached image` (edicao). NUNCA contem as palavras `o avatar fala`, `câmera:` ou `som
   ambiente:`. Um prompt V e sempre em portugues e sempre tem exatamente cinco partes na ordem:
   a linha `o avatar (homem/mulher) fala em ingles... a seguinte frase: "..."`, a linha do lip
   sync (`o avatar diz todas as palavras corretamente...`), a linha `o que acontece no vídeo:`,
   a linha `câmera:` e a linha `som ambiente:`.
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
parar. Nao adivinhar pela aparencia ou ordem da galeria. Cada V tem uma variacao, gerada no Omni
Flash a partir da UNICA imagem que o operador deixou naquele K.

### Videos em lotes fechados

1. Receber e registrar toda a fila V, sem executar tudo automaticamente.
2. Antes de cada V, conferir avatar, perfil e K indicado no MAPA K/V.
3. Usar a imagem exclusivamente como INITIAL FRAME, nunca Element, ingredient ou referencia de objeto.
4. Configurar o modelo do perfil: AURALY em Veo 3.1 Lite, Lower Priority, oito segundos, tres
   variacoes; CLASSICO somente em Omni Flash, oito segundos, um unico resultado por V.
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

Checklist de envio: 32/32 aprovados (N/A: A1, A2, A7 fiéis ao modelo; C3 a C7 sem segunda pessoa, selfie, frase repetida ou motion control; E4 roteiro aprovado literal do modelo)

## Anexos

- **Âncora Jamie Anderson:** `input/ancoras/04_jamie_anderson.jpg` em TODOS os K.
- **Só no K01**, anexar também `input/primeiro_frame_modelo.png` (referência de composição, nada além disso).
- K01 a K07 casam com V01 a V07 pelo número.

| Código | Take |
|---|---|
| K01 / V01 | T1, gancho, a água sobre o modelo dental manchado |
| K02 / V02 | T2, coco entrando na tigela, plano médio |
| K03 / V03 | T3, mãos misturando a pasta, close |
| K04 / V04 | T4, tigela pronta perto da lente, inclinado |
| K05 / V05 | T5, tigela na altura do peito |
| K06 / V06 | T6, tigela na altura do peito, sorriso |
| K07 / V07 | T7, tigela, plano mais fechado do vídeo |

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho, a água sobre o modelo dental manchado · anexar ÂNCORA + FRAME DO MODELO

```text
K01
IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16. This is a fictional AI-generated character, no real person is depicted. Use the attached image only for Jamie Anderson's exact identity, wardrobe and own setting. Do not copy its pose or framing. Use the second attached image only as a composition reference for the low camera, the dental model filling the lower half and the water bottle tilted over it; do not copy its man, his clothes, glasses, room or colors. The exact fictional AI character Jamie Anderson, a beekeeper who grows his own food on his small family farm: Black American man in his mid-fifties, medium brown skin, short low-cut hair heavily grey at the temples and top, short full grey-white beard and grey moustache, high forehead, visible freckles and moles on his cheeks, dark brown eyes, lean athletic build, veined forearms and natural age lines. A worn white zip-front beekeeping jacket with faint work stains, the mesh veil hood lowered behind his head and shoulders, the sleeves pushed up to the forearms, and a pair of reading glasses hooked in the chest pocket. His own small family farm under an overcast sky with visible cloud texture, at the weathered grey wooden picnic table: white wooden beehive boxes on the grass and a weathered red barn with a small American flag on its wall behind him. An oversized plastic dental demonstration model, as big as a serving platter: the complete lower arch of teeth in a horseshoe shape, set in glossy pink plastic gums, lying flat on the weathered grey wooden picnic table. Every tooth is covered in a thick, crusty, uneven layer of brown and yellow stain deposits, with dark brown lines along the gumline and between the teeth, clearly a teaching model and not a real mouth. Jamie Anderson holds a clear plastic water bottle with no label in one hand, tilted over the front teeth, and a thin stream of water is just starting to fall onto them. Jamie Anderson leans in from behind the dental model, looking into the lens over it, the hand with the water bottle reaching over the teeth. The dental model fills the whole lower half of the frame, very close to the lens, large in frame, much closer to the camera than his face. He is clear in the upper half, head and upper chest. Nothing else competes with the dental model. Phone camera low, just above the level of the teeth and very close to them, slight upward angle. Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on the face with no harsh shadows. Start frame: the first thin stream of water is just touching the fully stained front teeth; every tooth is still brown and yellow. Jamie Anderson is caught mid-sentence, lips naturally parted, animated expression. Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing. no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no real human mouth, no small dental model, no toy-sized teeth, no clean white teeth yet, no second person in frame.
```

### K02 · T2, coco entrando na tigela, plano médio · anexar ÂNCORA

```text
K02
IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16. This is a fictional AI-generated character, no real person is depicted. Use the attached image only for Jamie Anderson's exact identity, wardrobe and own setting. Do not copy its pose or framing. The exact fictional AI character Jamie Anderson, a beekeeper who grows his own food on his small family farm: Black American man in his mid-fifties, medium brown skin, short low-cut hair heavily grey at the temples and top, short full grey-white beard and grey moustache, high forehead, visible freckles and moles on his cheeks, dark brown eyes, lean athletic build, veined forearms and natural age lines. A worn white zip-front beekeeping jacket with faint work stains, the mesh veil hood lowered behind his head and shoulders, the sleeves pushed up to the forearms, and a pair of reading glasses hooked in the chest pocket. His own small family farm under an overcast sky: a weathered grey wooden picnic table in front of him; behind him white wooden beehive boxes on the grass, a weathered red barn with a small American flag on its wall at the left, and a small roadside stand with shelves of glass jars of honey at the right, green fields beyond. An empty clear glass mixing bowl stands on the weathered grey wooden picnic table in the lower foreground, very close to the lens, larger in frame than his hands. Beside it on the weathered grey wooden picnic table: a plain clear glass jar of solid white coconut oil with no label, a small plain white cardboard carton of baking soda with no printing on it, and half a fresh yellow lemon. Jamie Anderson holds a metal spoon with a heaped scoop of solid white coconut oil right above the bowl. Jamie Anderson is standing behind the weathered wooden picnic table, leaning in with his forearms resting on its edge. From the waist up, the bowl in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur. Phone camera at chest height, straight on, fixed. Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on the face with no harsh shadows. Start frame: Jamie Anderson is about to drop the coconut oil into the bowl, caught mid-sentence, lips naturally parted, animated expression. Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing. no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no dental model in frame, no second person in frame.
```

### K03 · T3, mãos misturando a pasta, close · anexar ÂNCORA

```text
K03
IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16. This is a fictional AI-generated character, no real person is depicted. Use the attached image only for Jamie Anderson's exact identity, wardrobe and own setting. Do not copy its pose or framing. The exact fictional AI character Jamie Anderson, a beekeeper who grows his own food on his small family farm: Black American man in his mid-fifties, medium brown skin, short low-cut hair heavily grey at the temples and top, short full grey-white beard and grey moustache, high forehead, visible freckles and moles on his cheeks, dark brown eyes, lean athletic build, veined forearms and natural age lines. A worn white zip-front beekeeping jacket with faint work stains, the mesh veil hood lowered behind his head and shoulders, the sleeves pushed up to the forearms, and a pair of reading glasses hooked in the chest pocket. His own small family farm under an overcast sky: a weathered grey wooden picnic table in front of him; behind him white wooden beehive boxes on the grass, a weathered red barn with a small American flag on its wall at the left, and a small roadside stand with shelves of glass jars of honey at the right, green fields beyond. A clear glass mixing bowl with coconut oil, baking soda and a little lemon juice half-mixed into a thick white paste fills the lower half of the frame on the weathered grey wooden picnic table, very close to the lens. Jamie Anderson's hands hold the bowl rim and a metal spoon stirring inside it. Jamie Anderson is standing behind the weathered wooden picnic table, leaning in with his forearms resting on its edge. Close shot of the hands and the bowl, from the chest down, his face cut off by the top edge of the frame. The background is reduced by framing, never by blur. Phone camera close to the bowl, slightly above it, fixed. Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on the face with no harsh shadows. Start frame: the spoon is mid-stir, the mixture streaky and almost a smooth paste. Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing. no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no dental model in frame, no second person in frame.
```

### K04 · T4, tigela pronta perto da lente, inclinado · anexar ÂNCORA

```text
K04
IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16. This is a fictional AI-generated character, no real person is depicted. Use the attached image only for Jamie Anderson's exact identity, wardrobe and own setting. Do not copy its pose or framing. The exact fictional AI character Jamie Anderson, a beekeeper who grows his own food on his small family farm: Black American man in his mid-fifties, medium brown skin, short low-cut hair heavily grey at the temples and top, short full grey-white beard and grey moustache, high forehead, visible freckles and moles on his cheeks, dark brown eyes, lean athletic build, veined forearms and natural age lines. A worn white zip-front beekeeping jacket with faint work stains, the mesh veil hood lowered behind his head and shoulders, the sleeves pushed up to the forearms, and a pair of reading glasses hooked in the chest pocket. His own small family farm under an overcast sky: a weathered grey wooden picnic table in front of him; behind him white wooden beehive boxes on the grass, a weathered red barn with a small American flag on its wall at the left, and a small roadside stand with shelves of glass jars of honey at the right, green fields beyond. Jamie Anderson holds a clear glass bowl full of smooth creamy white paste with both hands, pushed toward the lens, very close to the camera in the lower foreground. On the weathered grey wooden picnic table at the bottom edge: a plain clear glass jar of solid white coconut oil with no label, a small plain white cardboard carton of baking soda with no printing on it, and half a fresh yellow lemon. Jamie Anderson is standing behind the weathered wooden picnic table, leaning in with his forearms resting on its edge. From the chest up, leaning toward the lens, his face clear in the upper half, the bowl in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur. Phone camera at chest height, straight on, fixed. Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on the face with no harsh shadows. Start frame: Jamie Anderson leans forward holding the bowl out, caught mid-sentence, lips naturally parted, animated expression. Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing. no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no dental model in frame, no second person in frame.
```

### K05 · T5, tigela na altura do peito · anexar ÂNCORA

```text
K05
IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16. This is a fictional AI-generated character, no real person is depicted. Use the attached image only for Jamie Anderson's exact identity, wardrobe and own setting. Do not copy its pose or framing. The exact fictional AI character Jamie Anderson, a beekeeper who grows his own food on his small family farm: Black American man in his mid-fifties, medium brown skin, short low-cut hair heavily grey at the temples and top, short full grey-white beard and grey moustache, high forehead, visible freckles and moles on his cheeks, dark brown eyes, lean athletic build, veined forearms and natural age lines. A worn white zip-front beekeeping jacket with faint work stains, the mesh veil hood lowered behind his head and shoulders, the sleeves pushed up to the forearms, and a pair of reading glasses hooked in the chest pocket. His own small family farm under an overcast sky: a weathered grey wooden picnic table in front of him; behind him white wooden beehive boxes on the grass, a weathered red barn with a small American flag on its wall at the left, and a small roadside stand with shelves of glass jars of honey at the right, green fields beyond. Jamie Anderson holds the clear glass bowl of smooth creamy white paste with both hands at chest height, very close to the lens in the lower foreground. On the weathered grey wooden picnic table at the bottom edge: a plain clear glass jar of solid white coconut oil with no label, a small plain white cardboard carton of baking soda with no printing on it, and half a fresh yellow lemon. Jamie Anderson is standing behind the weathered wooden picnic table, leaning in with his forearms resting on its edge. From the chest up, his face clear in the upper half, the bowl in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur. Phone camera at chest height, straight on, fixed. Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on the face with no harsh shadows. Start frame: Jamie Anderson looks into the lens holding the bowl, caught mid-sentence, lips naturally parted, animated expression. Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing. no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no dental model in frame, no second person in frame.
```

### K06 · T6, tigela na altura do peito, sorriso · anexar ÂNCORA

```text
K06
IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16. This is a fictional AI-generated character, no real person is depicted. Use the attached image only for Jamie Anderson's exact identity, wardrobe and own setting. Do not copy its pose or framing. The exact fictional AI character Jamie Anderson, a beekeeper who grows his own food on his small family farm: Black American man in his mid-fifties, medium brown skin, short low-cut hair heavily grey at the temples and top, short full grey-white beard and grey moustache, high forehead, visible freckles and moles on his cheeks, dark brown eyes, lean athletic build, veined forearms and natural age lines. A worn white zip-front beekeeping jacket with faint work stains, the mesh veil hood lowered behind his head and shoulders, the sleeves pushed up to the forearms, and a pair of reading glasses hooked in the chest pocket. His own small family farm under an overcast sky: a weathered grey wooden picnic table in front of him; behind him white wooden beehive boxes on the grass, a weathered red barn with a small American flag on its wall at the left, and a small roadside stand with shelves of glass jars of honey at the right, green fields beyond. Jamie Anderson holds the clear glass bowl of smooth creamy white paste with both hands at chest height, very close to the lens in the lower foreground. On the weathered grey wooden picnic table at the bottom edge: a plain clear glass jar of solid white coconut oil with no label, a small plain white cardboard carton of baking soda with no printing on it, and half a fresh yellow lemon. Jamie Anderson is standing behind the weathered wooden picnic table, leaning in with his forearms resting on its edge. From the chest up, his face clear in the upper half, the bowl in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur. Phone camera at chest height, straight on, fixed. Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on the face with no harsh shadows. Start frame: Jamie Anderson looks into the lens with a warm, confident half smile, caught mid-sentence, lips naturally parted, animated expression. Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing. no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no dental model in frame, no second person in frame.
```

### K07 · T7, tigela, plano mais fechado do vídeo · anexar ÂNCORA

```text
K07
IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16. This is a fictional AI-generated character, no real person is depicted. Use the attached image only for Jamie Anderson's exact identity, wardrobe and own setting. Do not copy its pose or framing. The exact fictional AI character Jamie Anderson, a beekeeper who grows his own food on his small family farm: Black American man in his mid-fifties, medium brown skin, short low-cut hair heavily grey at the temples and top, short full grey-white beard and grey moustache, high forehead, visible freckles and moles on his cheeks, dark brown eyes, lean athletic build, veined forearms and natural age lines. A worn white zip-front beekeeping jacket with faint work stains, the mesh veil hood lowered behind his head and shoulders, the sleeves pushed up to the forearms, and a pair of reading glasses hooked in the chest pocket. His own small family farm under an overcast sky: a weathered grey wooden picnic table in front of him; behind him white wooden beehive boxes on the grass, a weathered red barn with a small American flag on its wall at the left, and a small roadside stand with shelves of glass jars of honey at the right, green fields beyond. Jamie Anderson holds the clear glass bowl of smooth creamy white paste with both hands at chest height, very close to the lens in the lower foreground. Jamie Anderson is standing behind the weathered wooden picnic table, leaning in with his forearms resting on its edge. Tightest shot of the video: from the upper chest up, his face clear in the upper half, the bowl in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur. Phone camera at chest height, straight on, fixed. Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on the face with no harsh shadows. Start frame: Jamie Anderson leans a little toward the lens, smiling, caught mid-sentence, lips naturally parted, animated expression. Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing. no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no dental model in frame, no second person in frame.
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem que você deixou no K01

```text
V01
o avatar Jamie Anderson, homem, fala em inglês com sotaque americano de um homem negro americano, voz média, calma e calorosa de um homem de cinquenta e cinco anos que fala com certeza, entonação confiante e cúmplice, como quem conta um segredo que ninguém mais conta, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Your dentist will never tell you this, because the day you learn it is the day you stop paying for whitening."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jamie Anderson inclina a garrafa e a água cai em fio sobre os dentes manchados do modelo dental; a crosta marrom escorre com espuma e os dentes vão aparecendo brancos, da frente para os lados, até a arcada inteira ficar branca e limpa; ele fala olhando para a câmera o tempo todo.

câmera: fixa, baixa, leve handheld

som ambiente: fazenda tranquila ao ar livre, pássaros ao longe, som da água caindo e borbulhando, sem música
```

### V02 · T2 · frame inicial = a imagem que você deixou no K02

```text
V02
o avatar Jamie Anderson, homem, fala em inglês com sotaque americano de um homem negro americano, voz média, calma e calorosa de um homem de cinquenta e cinco anos que fala com certeza, entonação calma e didática, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Take one tablespoon of coconut oil, half a teaspoon of baking soda, and three drops of lemon juice,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jamie Anderson põe uma colher de óleo de coco na tigela de vidro, depois uma colher de bicarbonato, e espreme três gotas do meio limão dentro dela, enquanto a câmera se aproxima devagar das mãos e da tigela.

câmera: push-in lento, do plano médio até as mãos e a tigela

som ambiente: fazenda tranquila ao ar livre, pássaros ao longe, sem música
```

### V03 · T3 · frame inicial = a imagem que você deixou no K03

```text
V03
o avatar Jamie Anderson, homem, fala em inglês com sotaque americano de um homem negro americano, voz média, calma e calorosa de um homem de cinquenta e cinco anos que fala com certeza, entonação calma e didática, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "and mix it into a paste."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jamie Anderson mexe a mistura com a colher e ela vira uma pasta branca e cremosa. Ele diz a frase em ritmo natural logo no começo e continua mexendo em silêncio até o fim.

câmera: fixa, fechada nas mãos

som ambiente: fazenda tranquila ao ar livre, pássaros ao longe, som leve da colher na tigela, sem música
```

### V04 · T4 · frame inicial = a imagem que você deixou no K04

```text
V04
o avatar Jamie Anderson, homem, fala em inglês com sotaque americano de um homem negro americano, voz média, calma e calorosa de um homem de cinquenta e cinco anos que fala com certeza, entonação calma e didática, sorrindo de leve, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Brush with it every morning for two minutes, then spit it out and rinse with warm water."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jamie Anderson segura a tigela com a pasta branca perto da câmera com as duas mãos, inclinado para a frente, e fala direto para a lente.

câmera: fixa

som ambiente: fazenda tranquila ao ar livre, pássaros ao longe, sem música
```

### V05 · T5 · frame inicial = a imagem que você deixou no K05

```text
V05
o avatar Jamie Anderson, homem, fala em inglês com sotaque americano de um homem negro americano, voz média, calma e calorosa de um homem de cinquenta e cinco anos que fala com certeza, entonação confiante, explicando com clareza, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "The coconut oil pulls the bacteria and build up off your enamel, and the baking soda lifts the surface stains, and the lemon brightens everything up."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jamie Anderson segura a tigela com as duas mãos na altura do peito e fala para a câmera, com pequenos movimentos naturais.

câmera: fixa

som ambiente: fazenda tranquila ao ar livre, pássaros ao longe, sem música
```

### V06 · T6 · frame inicial = a imagem que você deixou no K06

```text
V06
o avatar Jamie Anderson, homem, fala em inglês com sotaque americano de um homem negro americano, voz média, calma e calorosa de um homem de cinquenta e cinco anos que fala com certeza, entonação calorosa e segura, com orgulho tranquilo no fim, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "That yellow starts fading, and the stains disappear like they were never there. In 30 years of working in wellness, this is something I always teach."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jamie Anderson segura a tigela com as duas mãos na altura do peito e fala para a câmera, sorrindo no fim.

câmera: fixa

som ambiente: fazenda tranquila ao ar livre, pássaros ao longe, sem música
```

### V07 · T7 · frame inicial = a imagem que você deixou no K07

```text
V07
o avatar Jamie Anderson, homem, fala em inglês com sotaque americano de um homem negro americano, voz média, calma e calorosa de um homem de cinquenta e cinco anos que fala com certeza, entonação animada e convidativa, sorrindo, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Comment yes if you want more helpful videos like this, and make sure you follow me so you do not miss the next one."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jamie Anderson segura a tigela com as duas mãos, se inclina um pouco para a câmera e fala direto com ela, sorrindo.

câmera: fixa

som ambiente: fazenda tranquila ao ar livre, pássaros ao longe, sem música
```

## 4. Montagem no CapCut

1. Clipes na ordem: V01, V02, V03, V04, V05, V06, V07.
2. Cortar cada clipe no tempo da cena do modelo: V01 0,0 a 5,9 s; V02 5,9 a 11,4 s; V03 11,4 a 13,1 s; V04 13,1 a 17,5 s; V05 17,5 a 25,3 s; V06 25,3 a 32,4 s; V07 32,4 a 37,7 s.
3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. V03 é cena curta: cortar logo depois de "paste".
5. Legenda palavra a palavra em serifa itálica branca no meio do quadro, igual ao modelo, do começo ao fim.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Música só do V02 em diante, nunca no gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
8. Rótulo pequeno `AI-generated` num canto do vídeo.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | Your dentist will never tell you this, because the day you learn it is the day you stop paying for whitening. | Seu dentista nunca vai te contar isso, porque no dia em que você aprender é o dia em que você para de pagar por clareamento. |
| T2 | Take one tablespoon of coconut oil, half a teaspoon of baking soda, and three drops of lemon juice, | Pegue uma colher de sopa de óleo de coco, meia colher de chá de bicarbonato e três gotas de suco de limão, |
| T3 | and mix it into a paste. | e misture até virar uma pasta. |
| T4 | Brush with it every morning for two minutes, then spit it out and rinse with warm water. | Escove com ela toda manhã por dois minutos, depois cuspa e enxágue com água morna. |
| T5 | The coconut oil pulls the bacteria and build up off your enamel, and the baking soda lifts the surface stains, and the lemon brightens everything up. | O óleo de coco puxa as bactérias e o acúmulo do seu esmalte, o bicarbonato levanta as manchas da superfície, e o limão clareia tudo. |
| T6 | That yellow starts fading, and the stains disappear like they were never there. In 30 years of working in wellness, this is something I always teach. | Aquele amarelo começa a sumir, e as manchas desaparecem como se nunca tivessem existido. Em 30 anos trabalhando com bem-estar, isso é algo que eu sempre ensino. |
| T7 | Comment yes if you want more helpful videos like this, and make sure you follow me so you do not miss the next one. | Comente yes se você quer mais vídeos úteis como este, e não deixe de me seguir para não perder o próximo. |

## 6. Roteiro final em inglês

1. Your dentist will never tell you this, because the day you learn it is the day you stop paying for whitening.
2. Take one tablespoon of coconut oil, half a teaspoon of baking soda, and three drops of lemon juice,
3. and mix it into a paste.
4. Brush with it every morning for two minutes, then spit it out and rinse with warm water.
5. The coconut oil pulls the bacteria and build up off your enamel, and the baking soda lifts the surface stains, and the lemon brightens everything up.
6. That yellow starts fading, and the stains disappear like they were never there. In 30 years of working in wellness, this is something I always teach.
7. Comment yes if you want more helpful videos like this, and make sure you follow me so you do not miss the next one.

Your dentist will never tell you this, because the day you learn it is the day you stop paying for whitening. Take one tablespoon of coconut oil, half a teaspoon of baking soda, and three drops of lemon juice, and mix it into a paste. Brush with it every morning for two minutes, then spit it out and rinse with warm water. The coconut oil pulls the bacteria and build up off your enamel, and the baking soda lifts the surface stains, and the lemon brightens everything up. That yellow starts fading, and the stains disappear like they were never there. In 30 years of working in wellness, this is something I always teach. Comment yes if you want more helpful videos like this, and make sure you follow me so you do not miss the next one.
