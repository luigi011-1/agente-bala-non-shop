# ENTREGA | holistic.brandon | FityWell Growth Pés com água oxigenada

Produção `brandon_pes_peroxido` · Ângulo 2 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil CLÁSSICO

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

Checklist de envio: 34/34 aprovados (N/A: A1, A2, A7 fiéis ao modelo; C3 a C7 sem segunda pessoa, selfie, frase repetida, cena atuada ou motion control)

Ficha: 9/9 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos

- **Âncora holistic.brandon:** `producao/_ancoras/holistic_brandon_ancora.jpg` em TODOS os K (no K05, macro dos pés, ela entra pela pele e pelo cenário).
- **Em cada K**, anexar também o frame do modelo daquele passo (`producao/brandon_pes_peroxido/input/frames_modelo/Kxx_modelo.png`), só como referência de composição.
- K01 a K09 casam com V01 a V09 pelo número. Todos os V têm fala.

| Código | Take | Frame do modelo |
|---|---|---|
| K01 / V01 | T1, gancho, spray no pé colado na lente | `input/frames_modelo/K01_modelo.png` |
| K02 / V02 | T2, espuma no pé, olhando para a câmera | `input/frames_modelo/K02_modelo.png` |
| K03 / V03 | T3, receita no chão, spray no pote | `input/frames_modelo/K03_modelo.png` |
| K04 / V04 | T4, sentada no banco, pés no pote | `input/frames_modelo/K04_modelo.png` |
| K05 / V05 | T5, macro dos pés na água borbulhando | `input/frames_modelo/K05_modelo.png` |
| K06 / V06 | T6, no banco, resultado | `input/frames_modelo/K06_modelo.png` |
| K07 / V07 | T7, no banco, autoridade | `input/frames_modelo/K07_modelo.png` |
| K08 / V08 | T8, no banco, inclinada | `input/frames_modelo/K08_modelo.png` |
| K09 / V09 | T9, CTA, plano mais fechado | `input/frames_modelo/K09_modelo.png` |

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho, spray no pé colado na lente · anexar ÂNCORA + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, leather vest, feathers, wooden floor, rug, tiles, the blue and yellow aerosol can or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings. Barefoot.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The floor is black rubber gym flooring.",
  "prop": "A plain brown plastic trigger sprayer with a white trigger and no label, filled with hydrogen peroxide, held in her right hand and pointed at the top of her bare left foot. Her left leg is stretched forward so her bare left foot rests on the black rubber floor very close to the lens, the top of the foot facing the camera.",
  "posture": "Brandon sits cross-legged on the black rubber gym floor, her left leg stretched forward, her left hand resting on her shin, her right hand holding the trigger sprayer.",
  "composition": "Floor-level shot: the phone lens is about 30 centimeters from her bare foot, which fills the lower 30 percent of the frame at the center right, far closer to the camera than her face and larger than her head, nothing else competing with it; the trigger sprayer sits at the lower left and her head is in the upper part of the frame. Nothing else is on the floor. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the floor, standard 1x lens pointing slightly upward, straight-on, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and feet with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the first fine mist is leaving the nozzle toward the top of the foot; the skin is still clean, no foam yet. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the trigger sprayer, container, glass or spoon, no studio, no plastic-looking skin, no extra fingers, no extra toes, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no second person, no metal aerosol can, no wooden floor, no living room rug, no ceramic tile floor, no leather vest, no feathers, no silver cross, no foam yet"
}
```

### K02 · T2, espuma no pé, olhando para a câmera · anexar ÂNCORA + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, leather vest, feathers, wooden floor, rug, tiles, the blue and yellow aerosol can or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings. Barefoot.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The floor is black rubber gym flooring.",
  "prop": "A thick patch of white foam with big bubbles covers the top of her bare left foot and ankle. Her left leg is stretched forward so her bare left foot rests on the black rubber floor very close to the lens, the top of the foot facing the camera. Lowered in her right hand she holds a plain brown plastic trigger sprayer with a white trigger and no label, filled with hydrogen peroxide.",
  "posture": "Brandon sits cross-legged on the black rubber gym floor, her left leg stretched forward, her left hand resting on her shin, her right hand holding the trigger sprayer.",
  "composition": "Floor-level shot: the phone lens is about 30 centimeters from her bare foot, which fills the lower 30 percent of the frame at the center right, far closer to the camera than her face and larger than her head, nothing else competing with it; the trigger sprayer sits at the lower left and her head is in the upper part of the frame. Nothing else is on the floor. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the floor, standard 1x lens pointing slightly upward, straight-on, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and feet with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the foam sits on the foot, still. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, serious.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the trigger sprayer, container, glass or spoon, no studio, no plastic-looking skin, no extra fingers, no extra toes, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no second person, no metal aerosol can, no wooden floor, no living room rug, no ceramic tile floor, no leather vest, no feathers, no silver cross"
}
```

### K03 · T3, receita no chão, spray no pote · anexar ÂNCORA + FRAME DO MODELO

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, leather vest, feathers, wooden floor, rug, tiles, the blue and yellow aerosol can or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings. Barefoot.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The floor is black rubber gym flooring.",
  "prop": "A clear rectangular plastic storage container, empty, standing on the black rubber floor very close to the lens; a clear drinking glass full of warm water stands to its left and a metal spoon heaped with white baking soda lies on the floor in front of it. She holds a plain brown plastic trigger sprayer with a white trigger and no label, filled with hydrogen peroxide in her right hand, pointed into the container.",
  "posture": "Brandon sits cross-legged on the black rubber floor right behind the container, leaning slightly toward it.",
  "composition": "Floor-level shot: the phone lens is about 35 centimeters from the container, which with the glass fills the lower 30 percent of the frame, closer to the camera than her face; her head and torso fill the upper part of the frame. Nothing else is on the floor. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the floor, standard 1x lens pointing slightly upward, straight-on, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and feet with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the first spray of mist is going into the empty container. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the trigger sprayer, container, glass or spoon, no studio, no plastic-looking skin, no extra fingers, no extra toes, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no second person, no metal aerosol can, no wooden floor, no living room rug, no ceramic tile floor, no leather vest, no feathers, no silver cross"
}
```

### K04 · T4, sentada no banco, pés no pote · anexar ÂNCORA + FRAME DO MODELO

```text
K04
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, leather vest, feathers, wooden floor, rug, tiles, the blue and yellow aerosol can or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings. Barefoot.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The floor is black rubber gym flooring.",
  "prop": "Both of her bare feet stand inside a clear rectangular plastic storage container filled with warm water, on the black rubber floor very close to the lens.",
  "posture": "Brandon sits upright on a black padded gym bench, knees apart, both hands resting on her knees, seen from head to feet.",
  "composition": "Low floor-level wide shot: the phone lens is about 40 centimeters from the container, which fills the lower 25 percent of the frame, closer to the camera than her face; she fills the rest of the frame from head to feet. Nothing else is on the floor. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the floor, standard 1x lens pointing slightly upward, straight-on, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and feet with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: small bubbles are starting to rise around her feet. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the trigger sprayer, container, glass or spoon, no studio, no plastic-looking skin, no extra fingers, no extra toes, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no second person, no metal aerosol can, no wooden floor, no living room rug, no ceramic tile floor, no leather vest, no feathers, no silver cross"
}
```

### K05 · T5, macro dos pés na água borbulhando · anexar ÂNCORA + FRAME DO MODELO

```text
K05
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, leather vest, feathers, wooden floor, rug, tiles, the blue and yellow aerosol can or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings. Barefoot.",
  "scene": "At the top edge of the frame, beyond the container, a strip of the black rubber gym floor and the white-painted concrete block wall with the small American flag pinned on it, discreet but clearly visible and in focus.",
  "prop": "Her two bare feet inside a clear rectangular plastic storage container, seen through its clear side wall, the warm water full of rising bubbles and a thick layer of white foam fizzing around her ankles.",
  "posture": "Only her feet and lower shins are in frame.",
  "composition": "Macro close-up at floor level: the phone lens is about 10 centimeters from the side wall of the container, which fills the whole frame edge to edge. Nothing else is in frame. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the floor against the container, standard 1x lens, level, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and feet with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the water is fizzing, bubbles rising along the toes and the foam building around the ankles.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the trigger sprayer, container, glass or spoon, no studio, no plastic-looking skin, no extra fingers, no extra toes, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no second person, no metal aerosol can, no wooden floor, no living room rug, no ceramic tile floor, no leather vest, no feathers, no silver cross, no face in frame"
}
```

### K06 · T6, no banco, resultado · anexar ÂNCORA + FRAME DO MODELO

```text
K06
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, leather vest, feathers, wooden floor, rug, tiles, the blue and yellow aerosol can or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings. Barefoot.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The floor is black rubber gym flooring.",
  "prop": "No prop in her hands; the trigger sprayer and the container are out of frame.",
  "posture": "Brandon sits upright on a black padded gym bench, knees apart, both hands resting on her thighs, seen from the head down to mid-thigh.",
  "composition": "Straight-on medium shot: the phone lens is about 60 centimeters from her; her face and torso fill the upper two thirds of the frame and her hands on her thighs sit in the lower part, closer to the lens than her face. Nothing else is in frame. The background is reduced by framing, never by blur.",
  "camera": "phone on a small tripod at waist height, standard 1x lens, straight-on, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and feet with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, calm and sure.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the trigger sprayer, container, glass or spoon, no studio, no plastic-looking skin, no extra fingers, no extra toes, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no second person, no metal aerosol can, no wooden floor, no living room rug, no ceramic tile floor, no leather vest, no feathers, no silver cross"
}
```

### K07 · T7, no banco, autoridade · anexar ÂNCORA + FRAME DO MODELO

```text
K07
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, leather vest, feathers, wooden floor, rug, tiles, the blue and yellow aerosol can or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings. Barefoot.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The floor is black rubber gym flooring.",
  "prop": "No prop in her hands; the trigger sprayer and the container are out of frame.",
  "posture": "Brandon sits upright on a black padded gym bench, knees apart, one hand resting on her thigh, the other hand open in a small gesture, seen from the head down to mid-thigh.",
  "composition": "Straight-on medium shot: the phone lens is about 60 centimeters from her; her face and torso fill the upper two thirds of the frame and her hands on her thighs sit in the lower part, closer to the lens than her face. Nothing else is in frame. The background is reduced by framing, never by blur.",
  "camera": "phone on a small tripod at waist height, standard 1x lens, straight-on, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and feet with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, one hand open in a small gesture.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the trigger sprayer, container, glass or spoon, no studio, no plastic-looking skin, no extra fingers, no extra toes, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no second person, no metal aerosol can, no wooden floor, no living room rug, no ceramic tile floor, no leather vest, no feathers, no silver cross"
}
```

### K08 · T8, no banco, inclinada · anexar ÂNCORA + FRAME DO MODELO

```text
K08
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, leather vest, feathers, wooden floor, rug, tiles, the blue and yellow aerosol can or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings. Barefoot.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The floor is black rubber gym flooring.",
  "prop": "No prop in her hands; the trigger sprayer and the container are out of frame.",
  "posture": "Brandon sits leaning slightly forward on a black padded gym bench, knees apart, both hands resting on her thighs, seen from the head down to mid-thigh.",
  "composition": "Straight-on medium shot: the phone lens is about 60 centimeters from her; her face and torso fill the upper two thirds of the frame and her hands on her thighs sit in the lower part, closer to the lens than her face. Nothing else is in frame. The background is reduced by framing, never by blur.",
  "camera": "phone on a small tripod at waist height, standard 1x lens, straight-on, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and feet with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon leans slightly toward the lens and is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the trigger sprayer, container, glass or spoon, no studio, no plastic-looking skin, no extra fingers, no extra toes, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no second person, no metal aerosol can, no wooden floor, no living room rug, no ceramic tile floor, no leather vest, no feathers, no silver cross"
}
```

### K09 · T9, CTA, plano mais fechado · anexar ÂNCORA + FRAME DO MODELO

```text
K09
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, leather vest, feathers, wooden floor, rug, tiles, the blue and yellow aerosol can or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings. Barefoot.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The floor is black rubber gym flooring.",
  "prop": "No prop in her hands; the trigger sprayer and the container are out of frame.",
  "posture": "Brandon sits upright on a black padded gym bench, knees apart, both hands resting on her thighs, seen from the head down to mid-thigh.",
  "composition": "Straight-on medium close shot, the tightest of the video: the phone lens is about 45 centimeters from her; her face and torso fill the upper three quarters of the frame and her hands on her thighs sit at the bottom edge. Nothing else is in frame. The background is reduced by framing, never by blur.",
  "camera": "phone on a small tripod at waist height, standard 1x lens, straight-on, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and feet with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is smiling warmly, caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the trigger sprayer, container, glass or spoon, no studio, no plastic-looking skin, no extra fingers, no extra toes, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no second person, no metal aerosol can, no wooden floor, no living room rug, no ceramic tile floor, no leather vest, no feathers, no silver cross"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem que você deixou no K01

```text
V01
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação intrigante e desafiadora, devagar, como quem avisa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Spray hydrogen peroxide on your feet and watch what happens."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon borrifa o spray no dorso do pé descalço; por volta de 2 segundos uma espuma branca aparece na pele e vai crescendo em bolhas grossas; nos últimos segundos a câmera se aproxima devagar do pé.

câmera: fixa no chão, com aproximação lenta até o pé nos últimos segundos

som ambiente: box de treino em casa, tranquilo, chiado do spray e espuma estalando, sem música
```

### V02 · T2 · frame inicial = a imagem que você deixou no K02

```text
V02
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação séria, baixando um pouco a voz, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If it starts foaming, you just found out what has been living on them."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, sentada no chão com a espuma branca no pé, olha para a câmera e fala, séria.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, espuma estalando baixinho, sem música
```

### V03 · T3 · frame inicial = a imagem que você deixou no K03

```text
V03
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "In a container, spray three to four times in container, add two cups of warm water and one spoonful of baking soda."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon borrifa três vezes dentro do pote, despeja o copo de água morna no pote e vira a colher de bicarbonato na água.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, água caindo no pote, sem música
```

### V04 · T4 · frame inicial = a imagem que você deixou no K04

```text
V04
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Soak for 15 minutes and watch the foam."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, sentada no banco com os dois pés dentro do pote, fala para a câmera enquanto bolhas começam a subir em volta dos pés. Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, água borbulhando, sem música
```

### V05 · T5 · frame inicial = a imagem que você deixou no K05

```text
V05
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação didática e convicta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "That fizz is a chemical reaction with the bacteria and dead skin that your soap has been missing for years."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: A água em volta dos pés efervesce, com bolhas subindo e espuma branca crescendo. O rosto dela fica fora de quadro e a voz dela narra.

câmera: fixa, colada na parede do pote

som ambiente: box de treino em casa, tranquilo, água borbulhando, sem música
```

### V06 · T6 · frame inicial = a imagem que você deixou no K06

```text
V06
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação convicta e animada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "It clears the odor, softens cracked heels, peels dead skin right off, and even thick yellow nails begin growing out clear again."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, sentada no banco, fala para a câmera com as mãos nas coxas, com pequenos movimentos naturais.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V07 · T7 · frame inicial = a imagem que você deixou no K07

```text
V07
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e segura, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "In wellness practices in the USA, we say that the body speaks through the feet."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera e abre uma das mãos num gesto pequeno e natural.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V08 · T8 · frame inicial = a imagem que você deixou no K08

```text
V08
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e reflexiva, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The soles carry what the rest of the body leaves behind."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon se inclina um pouco para a frente e fala para a câmera, calma. Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V09 · T9 · frame inicial = a imagem que você deixou no K09

```text
V09
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa e convidativa, sorrindo no yes, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "This simple remedy is one way to begin listening. Follow me and comment yes if you want more home remedies like this."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala direto com quem assiste, sorrindo no yes, com as mãos nas coxas.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V09.
2. Cortar cada clipe no tempo da cena do modelo: V01 0,0 a 5,8 s; V02 5,8 a 9,6 s; V03 9,8 a 17,7 s; V04 17,7 a 20,4 s; V05 20,4 a 25,6 s; V06 25,6 a 33,3 s; V07 33,3 a 38,2 s; V08 38,2 a 41,3 s; V09 41,3 a 48,8 s.
3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. Flash branco de ~0,2 s entre o V02 e o V03, e dissolve curto entre o V04 e o V05, como no modelo.
5. No V01 a fala ocupa quase a cena inteira, devagar; não acelerar. Nos V04 e V08 (cenas curtas) a fala vem no começo; cortar logo depois da última palavra.
6. Legenda em caixa alta, branca, com a palavra-chave em amarelo, na metade de baixo do quadro, igual ao modelo.
7. Sem Voice Changer: a voz vem do prompt de cada V.
8. Música só depois do gancho (a partir do V03), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
9. Rótulo pequeno `AI-generated` num canto do vídeo.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | Spray hydrogen peroxide on your feet and watch what happens. | Borrife água oxigenada nos seus pés e veja o que acontece. |
| T2 | If it starts foaming, you just found out what has been living on them. | Se começar a espumar, você acabou de descobrir o que anda vivendo neles. |
| T3 | In a container, spray three to four times in container, add two cups of warm water and one spoonful of baking soda. | Num pote, borrife de três a quatro vezes dentro do pote, acrescente duas xícaras de água morna e uma colher de bicarbonato. |
| T4 | Soak for 15 minutes and watch the foam. | Deixe de molho por 15 minutos e veja a espuma. |
| T5 | That fizz is a chemical reaction with the bacteria and dead skin that your soap has been missing for years. | Essa efervescência é uma reação química com as bactérias e a pele morta que o seu sabonete deixa passar há anos. |
| T6 | It clears the odor, softens cracked heels, peels dead skin right off, and even thick yellow nails begin growing out clear again. | Tira o cheiro, amacia o calcanhar rachado, solta a pele morta, e até a unha grossa e amarelada começa a crescer limpa de novo. |
| T7 | In wellness practices in the USA, we say that the body speaks through the feet. | Nas práticas de bem-estar nos EUA, a gente diz que o corpo fala pelos pés. |
| T8 | The soles carry what the rest of the body leaves behind. | As solas carregam o que o resto do corpo deixa para trás. |
| T9 | This simple remedy is one way to begin listening. Follow me and comment yes if you want more home remedies like this. | Esse remédio simples é um jeito de começar a escutar. Me siga e comente yes se você quer mais remédios caseiros como este. |

## 6. Roteiro final em inglês

1. Spray hydrogen peroxide on your feet and watch what happens.
2. If it starts foaming, you just found out what has been living on them.
3. In a container, spray three to four times in container, add two cups of warm water and one spoonful of baking soda.
4. Soak for 15 minutes and watch the foam.
5. That fizz is a chemical reaction with the bacteria and dead skin that your soap has been missing for years.
6. It clears the odor, softens cracked heels, peels dead skin right off, and even thick yellow nails begin growing out clear again.
7. In wellness practices in the USA, we say that the body speaks through the feet.
8. The soles carry what the rest of the body leaves behind.
9. This simple remedy is one way to begin listening. Follow me and comment yes if you want more home remedies like this.

Spray hydrogen peroxide on your feet and watch what happens. If it starts foaming, you just found out what has been living on them. In a container, spray three to four times in container, add two cups of warm water and one spoonful of baking soda. Soak for 15 minutes and watch the foam. That fizz is a chemical reaction with the bacteria and dead skin that your soap has been missing for years. It clears the odor, softens cracked heels, peels dead skin right off, and even thick yellow nails begin growing out clear again. In wellness practices in the USA, we say that the body speaks through the feet. The soles carry what the rest of the body leaves behind. This simple remedy is one way to begin listening. Follow me and comment yes if you want more home remedies like this.
