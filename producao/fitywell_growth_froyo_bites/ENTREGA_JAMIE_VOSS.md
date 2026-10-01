# ENTREGA | Jamie Voss | FityWell Growth Froyo bites

Produção `fitywell_growth_froyo_bites` · Ângulo 2 · GROWTH · origem ORGÂNICA · rodada de VALIDAÇÃO · perfil CLÁSSICO

## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v17)

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

### AURALY, anchor e avatar fixo por conta (Luigi, 2026-09-14; anchor revista em 2026-09-22; avatar fixo em 2026-09-25)

Roster Auraly: Walt Hensley, Darlene Pruitt e Lorraine Vance. A referencia de cada um e a anchor
em cena real (imagem de teste aprovada), anexada em todo K. Nao existe fingerprint.

AVATAR FIXO POR CONTA (v16, 2026-09-25): cada conta usa o mesmo avatar com a roupa e o cenario-base
da anchor em todo video e em todo gancho. O texto do K descreve esse cenario e essa roupa. Quando o
video modelo tem uma cena em outro lugar, o texto do K descreve o lugar novo e manda usar a anchor
para identidade e roupa; a pessoa e a roupa nunca mudam. O angulo de camera serve a acao estrutural
preservada: pode ser exotico quando aumenta a anomalia, mas pode se repetir entre variacoes para
preservar composicao e timing. Mudar o angulo conta como a unica variavel dessa variacao.

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

### SHORT FORM DE CRESCIMENTO sem anchor (perfil CLASSICO, v13, 2026-09-23)

Cada conta e um ciclo proprio, tratado como um avatar. Nao existe anchor: os personagens nascem do
texto do K, e cada conta tem uma dupla propria. O unico anexo do K e o frame de composicao
REF-COMPOSICAO, que serve so para altura, angulo da camera e disposicao da cena; nunca copiar dele
pessoas, rostos, roupas, doces ou cenario. Um K por conta alimenta os tres V (V01, V02 e V03 usam o
K01 pela regra do classico). Em V de dialogo, a primeira linha nomeia quem fala (`a neta`, `a avo`)
no lugar de `o avatar` e continua sendo a parte 1 das cinco; a checagem das tres marcas nao muda.

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

**Prompt de imagem em JSON (v17, 2026-09-25).** Desde a v17 todo prompt K (e todo `REF-P`) chega
como UM objeto JSON em ingles: comeca com `{` na linha logo abaixo do codigo e termina com o `}`
que fecha o objeto. Colar o objeto INTEIRO, de `{` ate `}`, literalmente no campo de prompt do
Nano Banana 2, sem o codigo, sem resumir, sem converter para texto corrido e sem apagar campo.
Cada campo e parte do prompt (formato, referencia, identidade, roupa, cena, prop, postura,
composicao, camera, luz, estado, realismo, proporcao e negative), nao metadata. Se o JSON chegar
quebrado ou incompleto (sem o `}` final, aspas abertas), PARAR e avisar o operador. Pacotes
anteriores a v17, com o K em paragrafo unico, continuam validos como foram entregues.

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
   julgamento.** Um prompt K e um objeto JSON em ingles descrevendo uma imagem parada: comeca
   com `{` e termina com `}` (desde a v17; pacotes antigos traziam um paragrafo unico comecando
   com `IMPORTANT: THIS IS IPHONE FOOTAGE`, `Edit the attached image` ou, no `REF-P`, `CHARACTER
   SHEET`). Um prompt V NUNCA comeca com `{`. Um prompt K NUNCA contem as
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

Checklist de envio: 32/32 aprovados (N/A: A2, A7, A9 fiéis ao modelo; B7 pela origem orgânica, bandeira só nos planos de rosto onde a âncora já tem; C3 a C7 sem segunda pessoa, selfie, frase repetida ou motion control)

## Anexos

- **Âncora Jamie Voss:** `input/ancoras/03_jamie_voss.jpg` em TODOS os K.
- **Em cada K**, anexar também o frame do modelo daquele passo (`input/frames_modelo/Kxx_modelo.png`), só como referência de composição.
- K01 a K12 casam com V01 a V12 pelo número. V01, V08 e V12 têm fala; os outros são sem fala.

| Código | Take | Frame do modelo |
|---|---|---|
| K01 / V01 | T1, gancho, as duas metades coladas na lente, falando | `input/frames_modelo/K01_modelo.png` |
| K02 / V02 | T2, gancho, macro do corte roxo na mão | `input/frames_modelo/K02_modelo.png` |
| K03 / V03 | T3, gancho, a mordida grande de olhos fechados | `input/frames_modelo/K03_modelo.png` |
| K04 / V04 | T4, frutas caindo na tigela branca, depois a chia | `input/frames_modelo/K04_modelo.png` |
| K05 / V05 | T5, garfo amassando as frutas com a chia | `input/frames_modelo/K05_modelo.png` |
| K06 / V06 | T6, xarope de bordo escorrendo, depois a mistura | `input/frames_modelo/K06_modelo.png` |
| K07 / V07 | T7, iogurte grego em espiral na pasta roxa | `input/frames_modelo/K07_modelo.png` |
| K08 / V08 | T8, colheradas na assadeira, narração fora de quadro | `input/frames_modelo/K08_modelo.png` |
| K09 / V09 | T9, costas da colher achatando os discos | `input/frames_modelo/K09_modelo.png` |
| K10 / V10 | T10, disco congelado banhado no iogurte | `input/frames_modelo/K10_modelo.png` |
| K11 / V11 | T11, faca corta e as mãos abrem o recheio | `input/frames_modelo/K11_modelo.png` |
| K12 / V12 | T12, CTA, bite mordido na lente, falando | `input/frames_modelo/K12_modelo.png` |

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho, as duas metades coladas na lente, falando · anexar ÂNCORA + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Jamie Voss's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action with the food; do not copy its person, hands, rings, clothes, table, room, colors, hard sunlight or the white caption text.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "His own bright residential kitchen with a white-veined stone counter in front of him, cream upper cabinets and a black-framed window with a small American flag. The counter top is clear, with nothing on it except what he is using.",
  "prop": "Jamie Voss holds up a homemade frozen yogurt bite about the size of a palm: a round, slightly irregular handmade disc with a thick smooth frosty white shell of frozen Greek yogurt, cut in half, each cut face showing a thick dense purple-magenta filling of mashed raspberries, blueberries and black chia seeds, speckled with black seeds and dark blueberry skins, framed by the white yogurt shell. The two halves are stacked one on top of the other, both cut faces turned toward the lens, held in the fingertips of one hand.",
  "posture": "Jamie Voss is leaning on the counter with his forearms, toward the camera.",
  "composition": "The two stacked halves are very close to the lens in the lower foreground, large in frame, closer to the camera than his face, nothing else competing with them. He is clear behind them in the upper half, head and upper chest. The background is reduced by framing, never by blur.",
  "camera": "phone camera resting on the counter at chest height, straight on, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Jamie Voss shows the cut halves to the camera, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no hard sunlight shadows, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no perfect factory-made dessert, no ice cream cone, no popsicle stick"
}
```

### K02 · T2, gancho, macro do corte roxo na mão · anexar ÂNCORA + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Jamie Voss's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action with the food; do not copy its person, hands, rings, clothes, table, room, colors, hard sunlight or the white caption text.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "Jamie Voss's hand close to the lens above his white-veined stone counter, only the edge of the counter visible around it.",
  "prop": "Jamie Voss's hand holds one half of a homemade frozen yogurt bite about the size of a palm: a round, slightly irregular handmade disc with a thick smooth frosty white shell of frozen Greek yogurt, cut in half, each cut face showing a thick dense purple-magenta filling of mashed raspberries, blueberries and black chia seeds, speckled with black seeds and dark blueberry skins, framed by the white yogurt shell.",
  "posture": "Only his fair, slightly hairy hands with the navy henley sleeves at the wrists are in frame, holding the half between thumb and fingers.",
  "composition": "Macro: the cut face of the half fills most of the frame, the purple filling and the white shell sharp and detailed, the fingers at the edges. The background is reduced by framing, never by blur.",
  "camera": "phone camera very close to the hand, straight on, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the cut face is turned straight to the lens, a few crumbs of filling at the edge.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no hard sunlight shadows, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no face in frame, no perfect factory-made dessert, no glossy food-magazine styling"
}
```

### K03 · T3, gancho, a mordida grande de olhos fechados · anexar ÂNCORA + FRAME DO MODELO

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Jamie Voss's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action with the food; do not copy its person, hands, rings, clothes, table, room, colors, hard sunlight or the white caption text.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "His own bright residential kitchen with a white-veined stone counter in front of him, cream upper cabinets and a black-framed window with a small American flag. The counter top is clear, with nothing on it except what he is using.",
  "prop": "Jamie Voss holds a homemade frozen yogurt bite about the size of a palm: a round, slightly irregular handmade disc with a thick smooth frosty white shell of frozen Greek yogurt, whole and uncut, at his mouth.",
  "posture": "Jamie Voss is leaning on the counter with his forearms, toward the camera.",
  "composition": "From the chest up, his face and the hand with the frozen yogurt bite clear in the upper half, his head tilted slightly back. The background is reduced by framing, never by blur.",
  "camera": "phone camera resting on the counter at chest height, straight on, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Jamie Voss's mouth is wide open, the edge of the frozen yogurt bite just touching his lips, eyes starting to close.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no hard sunlight shadows, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no perfect factory-made dessert, no ice cream cone, no popsicle stick"
}
```

### K04 · T4, frutas caindo na tigela branca, depois a chia · anexar ÂNCORA + FRAME DO MODELO

```text
K04
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Jamie Voss's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action with the food; do not copy its person, hands, rings, clothes, table, room, colors, hard sunlight or the white caption text.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "Top-down view of his white-veined stone counter.",
  "prop": "A wide, deep plain white ceramic bowl sits on his white-veined stone counter. A few fresh raspberries and blueberries lie in the bottom of the empty bowl and a handful more are falling into it from Jamie Voss's hand at the top edge of the frame.",
  "posture": "Only his fair, slightly hairy hands with the navy henley sleeves at the wrists enter from the top edge of the frame.",
  "composition": "The white bowl fills most of the frame, very close to the lens, the counter visible around it. The background is reduced by framing, never by blur.",
  "camera": "phone held straight above the bowl, looking down",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the berries are mid-fall above the bowl, the bowl still mostly empty.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no hard sunlight shadows, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no face in frame, no perfect factory-made dessert, no glossy food-magazine styling"
}
```

### K05 · T5, garfo amassando as frutas com a chia · anexar ÂNCORA + FRAME DO MODELO

```text
K05
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Jamie Voss's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action with the food; do not copy its person, hands, rings, clothes, table, room, colors, hard sunlight or the white caption text.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "Top-down view of his white-veined stone counter.",
  "prop": "The wide plain white ceramic bowl on his white-veined stone counter is full of fresh raspberries and blueberries sprinkled with black chia seeds. Jamie Voss's hand holds a black metal fork pressing down into the berries.",
  "posture": "Only his fair, slightly hairy hands with the navy henley sleeves at the wrists enter from the bottom edge of the frame, holding the fork.",
  "composition": "The bowl fills most of the frame, very close to the lens. The background is reduced by framing, never by blur.",
  "camera": "phone held straight above the bowl, looking down",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the fork is pressing the first berries, a few already crushed red with juice.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no hard sunlight shadows, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no face in frame, no perfect factory-made dessert, no glossy food-magazine styling"
}
```

### K06 · T6, xarope de bordo escorrendo, depois a mistura · anexar ÂNCORA + FRAME DO MODELO

```text
K06
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Jamie Voss's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action with the food; do not copy its person, hands, rings, clothes, table, room, colors, hard sunlight or the white caption text.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "Top-down view of his white-veined stone counter.",
  "prop": "The wide plain white ceramic bowl on his white-veined stone counter holds a chunky red mash of raspberries, blueberries and chia seeds. Jamie Voss's hand holds a metal spoon full of amber maple syrup right above the mash, a thin drip just falling.",
  "posture": "Only his fair, slightly hairy hands with the navy henley sleeves at the wrists enter from the bottom edge of the frame.",
  "composition": "The bowl fills most of the frame, very close to the lens. The background is reduced by framing, never by blur.",
  "camera": "phone held straight above the bowl, looking down",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the first thin drip of syrup is falling from the tipped spoon onto the red mash.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no hard sunlight shadows, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no face in frame, no perfect factory-made dessert, no glossy food-magazine styling"
}
```

### K07 · T7, iogurte grego em espiral na pasta roxa · anexar ÂNCORA + FRAME DO MODELO

```text
K07
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Jamie Voss's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action with the food; do not copy its person, hands, rings, clothes, table, room, colors, hard sunlight or the white caption text.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "Close top-down view of his white-veined stone counter.",
  "prop": "The plain white ceramic bowl on his white-veined stone counter is full of a glossy thick deep red-purple paste of mashed berries and chia seeds. A big spoonful of thick white Greek yogurt has just been dropped in the middle, the spoon still touching it in Jamie Voss's hand.",
  "posture": "Only his fair, slightly hairy hands with the navy henley sleeves at the wrists enter from the side of the frame.",
  "composition": "The bowl fills the frame edge to edge, very close to the lens. The background is reduced by framing, never by blur.",
  "camera": "phone held close above the bowl, looking down at a slight angle",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: a clean white dollop of yogurt sits on the purple paste, not mixed yet.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no hard sunlight shadows, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no face in frame, no perfect factory-made dessert, no glossy food-magazine styling"
}
```

### K08 · T8, colheradas na assadeira, narração fora de quadro · anexar ÂNCORA + FRAME DO MODELO

```text
K08
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Jamie Voss's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action with the food; do not copy its person, hands, rings, clothes, table, room, colors, hard sunlight or the white caption text.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "Top-down view of his white-veined stone counter.",
  "prop": "A rimmed metal sheet pan lined with plain brown parchment paper sits on his white-veined stone counter. One heaped mound of lilac berry and yogurt mixture is already on the paper, and Jamie Voss's hand holds a metal spoon depositing a second heaped mound beside it.",
  "posture": "Only his fair, slightly hairy hands with the navy henley sleeves at the wrists enter from the bottom corner of the frame.",
  "composition": "The sheet pan fills most of the frame, very close to the lens, shown diagonally. The background is reduced by framing, never by blur.",
  "camera": "phone held straight above the sheet pan, looking down",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the second mound is sliding off the spoon onto the parchment.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no hard sunlight shadows, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no face in frame, no perfect factory-made dessert, no glossy food-magazine styling"
}
```

### K09 · T9, costas da colher achatando os discos · anexar ÂNCORA + FRAME DO MODELO

```text
K09
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Jamie Voss's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action with the food; do not copy its person, hands, rings, clothes, table, room, colors, hard sunlight or the white caption text.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "Close top-down view of the parchment-lined sheet pan on his white-veined stone counter.",
  "prop": "Several heaped mounds of lilac berry and yogurt mixture sit in a row on plain brown parchment paper. Jamie Voss's hand presses the back of a metal spoon onto one mound, already spreading it into a flat round disc.",
  "posture": "Only his fair, slightly hairy hands with the navy henley sleeves at the wrists enter from the side of the frame.",
  "composition": "The mounds and the spoon fill the frame, very close to the lens. The background is reduced by framing, never by blur.",
  "camera": "phone held close above the sheet pan, looking down",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the back of the spoon rests on the first mound, which is half flattened.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no hard sunlight shadows, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no face in frame, no perfect factory-made dessert, no glossy food-magazine styling"
}
```

### K10 · T10, disco congelado banhado no iogurte · anexar ÂNCORA + FRAME DO MODELO

```text
K10
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Jamie Voss's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action with the food; do not copy its person, hands, rings, clothes, table, room, colors, hard sunlight or the white caption text.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "Top-down view of his white-veined stone counter.",
  "prop": "A wide dark brown ceramic bowl filled to the brim with thick smooth white Greek yogurt sits on his white-veined stone counter. Jamie Voss's hand holds a black metal spoon with a frozen lilac-purple disc of berry mixture on it, just above the yogurt.",
  "posture": "Only his fair, slightly hairy hands with the navy henley sleeves at the wrists enter from the bottom edge of the frame.",
  "composition": "The dark bowl of white yogurt fills most of the frame, very close to the lens. The background is reduced by framing, never by blur.",
  "camera": "phone held straight above the bowl, looking down",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the frozen disc is about to touch the white yogurt, a light frost on its surface.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no hard sunlight shadows, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no face in frame, no perfect factory-made dessert, no glossy food-magazine styling"
}
```

### K11 · T11, faca corta e as mãos abrem o recheio · anexar ÂNCORA + FRAME DO MODELO

```text
K11
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Jamie Voss's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action with the food; do not copy its person, hands, rings, clothes, table, room, colors, hard sunlight or the white caption text.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "Top-down view of plain brown parchment paper on his white-veined stone counter.",
  "prop": "One whole homemade frozen yogurt bite about the size of a palm: a round, slightly irregular handmade disc with a thick smooth frosty white shell of frozen Greek yogurt lies on the parchment, uncut. The blade of a large kitchen knife rests across its center, Jamie Voss's hand on the handle, ready to cut.",
  "posture": "Only his fair, slightly hairy hands with the navy henley sleeves at the wrists are in frame, one on the knife handle, the other resting beside the bite.",
  "composition": "The white frozen yogurt bite sits in the middle of the frame, very close to the lens, the knife crossing it. The background is reduced by framing, never by blur.",
  "camera": "phone held straight above the parchment, looking down",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the knife blade touches the top of the frosty white shell, nothing cut yet.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no hard sunlight shadows, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no face in frame, no perfect factory-made dessert, no glossy food-magazine styling"
}
```

### K12 · T12, CTA, bite mordido na lente, falando · anexar ÂNCORA + FRAME DO MODELO

```text
K12
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Jamie Voss's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action with the food; do not copy its person, hands, rings, clothes, table, room, colors, hard sunlight or the white caption text.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "His own bright residential kitchen with a white-veined stone counter in front of him, cream upper cabinets and a black-framed window with a small American flag. The counter top is clear, with nothing on it except what he is using.",
  "prop": "Jamie Voss holds a homemade frozen yogurt bite about the size of a palm: a round, slightly irregular handmade disc with a thick smooth frosty white shell of frozen Greek yogurt with a big bite taken out of it, the bitten edge showing the purple-magenta berry and chia filling inside the white shell.",
  "posture": "Jamie Voss is leaning on the counter with his forearms, toward the camera.",
  "composition": "The bitten frozen yogurt bite is very close to the lens in the lower foreground, large in frame, closer to the camera than his face, nothing else competing with it. He is clear behind it in the upper half, the tightest shot of the video. The background is reduced by framing, never by blur.",
  "camera": "phone camera resting on the counter at chest height, straight on, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Jamie Voss has just finished chewing and smiles at the camera, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no hard sunlight shadows, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no perfect factory-made dessert, no ice cream cone, no popsicle stick"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem que você deixou no K01

```text
V01
o avatar Jamie Voss (homem) fala em inglês com sotaque americano de um homem branco americano, voz grave e firme de um homem de quarenta e poucos anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, entonação séria e sincera de quem conta algo pessoal, sem drama, ficando mais firme na segunda frase, no mesmo ritmo do vídeo modelo, a seguinte frase: "After brain tumor surgery, sugar spikes aren't an option for me. Inflammation completely stalls healing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jamie Voss segura as duas metades do froyo bite perto da câmera, o corte roxo virado para a lente, e fala olhando para a câmera, com pequenos movimentos naturais da mão.

câmera: fixa, celular apoiado na bancada na altura do peito

som ambiente: cozinha residencial tranquila, sem música
```

### V02 · T2 · frame inicial = a imagem que você deixou no K02

```text
V02
(sem fala no take: a fala do T1 entra como voz-over na edição)

nenhuma voz e nenhuma fala no clipe, só o som ambiente e o som da ação.

o que acontece no vídeo: A mão de Jamie Voss gira devagar a metade do froyo bite, mostrando o recheio roxo com chia de perto.

câmera: fixa, bem perto da mão, leve tremor natural

som ambiente: cozinha residencial tranquila, sem música
```

### V03 · T3 · frame inicial = a imagem que você deixou no K03

```text
V03
(sem fala no take: a fala do T1 entra como voz-over na edição)

nenhuma voz e nenhuma fala no clipe, só o som ambiente e o som da ação.

o que acontece no vídeo: Jamie Voss morde o froyo bite com vontade, fecha os olhos, inclina a cabeça um pouco para trás e mastiga devagar, com prazer.

câmera: fixa, celular apoiado na bancada na altura do peito

som ambiente: cozinha residencial tranquila, som leve da mordida, sem música
```

### V04 · T4 · frame inicial = a imagem que você deixou no K04

```text
V04
(sem fala no take: a fala do T1 entra como voz-over na edição)

nenhuma voz e nenhuma fala no clipe, só o som ambiente e o som da ação.

o que acontece no vídeo: Punhados de framboesas e mirtilos caem na tigela branca e quicam; depois uma colher cheia de sementes de chia é virada sobre as frutas.

câmera: fixa, de cima, como celular na mão de quem cozinha, leve tremor natural

som ambiente: cozinha residencial tranquila, som das frutas caindo na tigela, sem música
```

### V05 · T5 · frame inicial = a imagem que você deixou no K05

```text
V05
(sem fala no take: a fala do T1 entra como voz-over na edição)

nenhuma voz e nenhuma fala no clipe, só o som ambiente e o som da ação.

o que acontece no vídeo: O garfo amassa as frutas com a chia, pressionando várias vezes, até virar um purê grosso e vermelho.

câmera: fixa, de cima, como celular na mão de quem cozinha, leve tremor natural

som ambiente: cozinha residencial tranquila, som do garfo amassando, sem música
```

### V06 · T6 · frame inicial = a imagem que você deixou no K06

```text
V06
(sem fala no take: a fala do T1 entra como voz-over na edição)

nenhuma voz e nenhuma fala no clipe, só o som ambiente e o som da ação.

o que acontece no vídeo: Um fio de xarope de bordo escorre da colher sobre o purê; depois a colher mistura tudo até virar uma pasta roxa e brilhante.

câmera: fixa, de cima, como celular na mão de quem cozinha, leve tremor natural

som ambiente: cozinha residencial tranquila, som da colher raspando a tigela, sem música
```

### V07 · T7 · frame inicial = a imagem que você deixou no K07

```text
V07
(sem fala no take: a fala do T1 entra como voz-over na edição)

nenhuma voz e nenhuma fala no clipe, só o som ambiente e o som da ação.

o que acontece no vídeo: A colher solta o iogurte grego sobre a pasta roxa e faz espirais, dobrando o branco no roxo até a mistura ficar lilás e marmorizada.

câmera: fixa, de cima, como celular na mão de quem cozinha, leve tremor natural

som ambiente: cozinha residencial tranquila, som da colher mexendo, sem música
```

### V08 · T8 · frame inicial = a imagem que você deixou no K08

```text
V08
o avatar Jamie Voss (homem) narra fora de quadro, em inglês com sotaque americano de um homem branco americano, voz grave e firme de um homem de quarenta e poucos anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, entonação leve e animada, de quem mostra uma solução que achou para si, no mesmo ritmo do vídeo modelo, a seguinte frase: "So I made these anti-inflammatory froyo bites to satisfy my cravings without the glucose crash."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. O rosto não aparece: lip sync não se aplica, a voz é narração por cima da mão.

o que acontece no vídeo: a colher deposita montinhos da mistura lilás no papel manteiga, um ao lado do outro. Só a mão de Jamie Voss aparece.

câmera: fixa, de cima, como celular na mão de quem cozinha, leve tremor natural

som ambiente: cozinha residencial tranquila, som leve da colher no papel, sem música
```

### V09 · T9 · frame inicial = a imagem que você deixou no K09

```text
V09
(sem fala no take: a fala do T8 entra como voz-over na edição)

nenhuma voz e nenhuma fala no clipe, só o som ambiente e o som da ação.

o que acontece no vídeo: As costas da colher pressionam cada montinho até ele virar um disco redondo e liso.

câmera: fixa, de cima, como celular na mão de quem cozinha, leve tremor natural

som ambiente: cozinha residencial tranquila, som leve da colher no papel, sem música
```

### V10 · T10 · frame inicial = a imagem que você deixou no K10

```text
V10
(sem fala no take: a fala do T8 entra como voz-over na edição)

nenhuma voz e nenhuma fala no clipe, só o som ambiente e o som da ação.

o que acontece no vídeo: A colher afunda o disco roxo congelado no iogurte grego, gira, e levanta o disco coberto de branco.

câmera: fixa, de cima, como celular na mão de quem cozinha, leve tremor natural

som ambiente: cozinha residencial tranquila, som da colher no iogurte, sem música
```

### V11 · T11 · frame inicial = a imagem que você deixou no K11

```text
V11
(sem fala no take: a fala do T8 entra como voz-over na edição)

nenhuma voz e nenhuma fala no clipe, só o som ambiente e o som da ação.

o que acontece no vídeo: A faca desce e corta o froyo bite ao meio; as duas mãos puxam as metades e abrem, virando o recheio roxo para a câmera.

câmera: fixa, de cima, como celular na mão de quem cozinha, leve tremor natural

som ambiente: cozinha residencial tranquila, som da faca cortando o gelado, sem música
```

### V12 · T12 · frame inicial = a imagem que você deixou no K12

```text
V12
o avatar Jamie Voss (homem) fala em inglês com sotaque americano de um homem branco americano, voz grave e firme de um homem de quarenta e poucos anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, entonação de prazer genuíno, sorrindo, acabando de mastigar, e a pergunta do fim sai quase para si mesmo, no mesmo ritmo do vídeo modelo, a seguinte frase: "Save this one, and follow me so you don't miss my next healthy recipes. Why is it so good?"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jamie Voss segura o froyo bite mordido perto da câmera, fala direto para a lente sorrindo e, no fim, olha para o bite balançando levemente a cabeça.

câmera: fixa, celular apoiado na bancada na altura do peito

som ambiente: cozinha residencial tranquila, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V12.
2. Cortar cada clipe no tempo da cena do modelo: V01 em quadro 0,0 a 0,4 s; áudio de 0,0 a ~6,4 s, por baixo do V02 ao V07; V02 0,4 a 0,9 s; V03 0,9 a 1,7 s; V04 1,7 a 2,3 s; V05 2,3 a 3,0 s; V06 3,0 a 4,2 s; V07 4,2 a 6,5 s; V08 em quadro 6,5 a 8,0 s; áudio de 6,5 a ~11,5 s, por baixo do V09 ao V11; V09 8,0 a 9,0 s; V10 9,0 a 10,0 s; V11 10,0 a 11,5 s; V12 11,5 s até o fim da fala (~6 s).
3. Voz-over: soltar o áudio do V01 e deixá-lo correr por baixo do V02 ao V07; soltar o áudio do V08 e deixá-lo correr por baixo do V09 ao V11. Os clipes sem fala entram com o áudio abaixado a zero, só o som da ação bem baixo se ajudar.
4. Ritmo de corte seco: dentro de cada passo, picotar o mesmo clipe em pedaços de 0,2 a 0,7 s, como no modelo.
5. Zero tempo morto: V01, V08 e V12 começam já falando. Isolate Voice / Keep Vocal no áudio.
6. Legenda em frase curta, branca, negrito sem serifa, centralizada no meio do quadro, trocando por pedaço de frase, igual ao modelo. Escrever `tumor`, grafia americana.
7. Sem Voice Changer: a voz vem do prompt de cada V.
8. Música só depois do gancho (a partir do V04), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
9. Rótulo pequeno `AI-generated` num canto do vídeo.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | After brain tumor surgery, sugar spikes aren't an option for me. Inflammation completely stalls healing. | Depois de uma cirurgia de tumor cerebral, picos de açúcar não são uma opção para mim. A inflamação trava completamente a cicatrização. |
| T2 | (voz-over do T1) | (voz-over do T1) |
| T3 | (voz-over do T1) | (voz-over do T1) |
| T4 | (voz-over do T1) | (voz-over do T1) |
| T5 | (voz-over do T1) | (voz-over do T1) |
| T6 | (voz-over do T1) | (voz-over do T1) |
| T7 | (voz-over do T1) | (voz-over do T1) |
| T8 | So I made these anti-inflammatory froyo bites to satisfy my cravings without the glucose crash. | Então eu fiz esses bites de frozen yogurt anti-inflamatórios para matar minha vontade de doce sem a queda da glicose. |
| T9 | (voz-over do T8) | (voz-over do T8) |
| T10 | (voz-over do T8) | (voz-over do T8) |
| T11 | (voz-over do T8) | (voz-over do T8) |
| T12 | Save this one, and follow me so you don't miss my next healthy recipes. Why is it so good? | Salva essa, e me segue pra não perder minhas próximas receitas saudáveis. Por que isso é tão bom? |

## 6. Roteiro final em inglês

1. After brain tumor surgery, sugar spikes aren't an option for me. Inflammation completely stalls healing.
2. (sem fala: voz-over do T1)
3. (sem fala: voz-over do T1)
4. (sem fala: voz-over do T1)
5. (sem fala: voz-over do T1)
6. (sem fala: voz-over do T1)
7. (sem fala: voz-over do T1)
8. So I made these anti-inflammatory froyo bites to satisfy my cravings without the glucose crash.
9. (sem fala: voz-over do T8)
10. (sem fala: voz-over do T8)
11. (sem fala: voz-over do T8)
12. Save this one, and follow me so you don't miss my next healthy recipes. Why is it so good?

After brain tumor surgery, sugar spikes aren't an option for me. Inflammation completely stalls healing. So I made these anti-inflammatory froyo bites to satisfy my cravings without the glucose crash. Save this one, and follow me so you don't miss my next healthy recipes. Why is it so good?
