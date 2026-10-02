# ENTREGA | holistic.brandon | FityWell Venda Brownie de feijão preto

Produção `fitywell_brownie_feijao` · Ângulo 2 · VENDA · rodada de VALIDAÇÃO · perfil CLÁSSICO

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

Checklist de envio: 37/37 aprovados (N/A: A2 e A7 fiéis ao modelo; C3, C6 e C7 sem segunda pessoa, cena atuada ou motion control)

Ficha: 10/10 K, placar 14/14 cada (N/A com motivo: G2 em todos, G8 nos closes sem rosto K02 a K08)

## Anexos e mapa K/V

- **Âncora holistic.brandon:** `producao/_ancoras/holistic_brandon_ancora.jpg` em TODOS os K.
- **Só no K01**, anexar também `input/frames_modelo/K01_modelo.png` (referência de composição, nada além disso).
- Perfil clássico: cada V usa a imagem que sobrou no maior K de número menor ou igual ao dele.

| V | Frame inicial | Take |
|---|---|---|
| V01 | K01 | T1, gancho, a tigela de feijão preto perto da lente com o amassador |
| V02 | K02 | T2, close da tigela, dois ovos entrando no feijão (voz fora de quadro) |
| V03 | K03 | T3, close, colher de cacau em pó sobre a tigela |
| V04 | K04 | T4, close, mel cru escorrendo da colher |
| V05 | K05 | T5, close, canela em pó caindo no centro da tigela |
| V06 | K06 | T6, close, batedor na massa de chocolate (voz fora de quadro) |
| V07 | K07 | T7, close, massa escorrendo para a forma forrada |
| V08 | K08 | T8, a forma entrando no forno de bancada do box |
| V09 | K09 | T9, reveal, brownie pronto na mesa e os potinhos na frente |
| V10 | K09 | T10, mesmo quadro do K09 |
| V11 | K11 | T11, selfie com o pedaço de brownie perto da lente (fechamento e CTA) |
| V12 | K11 | T12, mesmo quadro do K11 |
| V13 | K11 | T13, mesmo quadro do K11 |
| V14 | K11 | T14, mesmo quadro do K11 |
| V15 | K11 | T15, mesmo quadro do K11 |
| V16 | K11 | T16, mesmo quadro do K11 |

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho, a tigela de feijão preto perto da lente com o amassador · anexar ÂNCORA + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Brandon's exact identity, wardrobe and own setting. Do not copy its pose or framing. Use the second attached image only as a composition reference for the glass bowl of black beans held close to the lens at the lower center, the masher raised over it and the person centered behind it; do not copy its man, his chef jacket, glasses, kitchen or colors.",
  "identity_main": "The exact fictional AI character Brandon, explicitly female: Black mixed-race American woman around thirty, athletic build, light brown skin with light freckles across her nose and cheeks, brown eyes, cornrow braids that turn into long loose braids down to her waist with wooden and gold beads at the tips, small stud earrings, a floral blackwork tattoo sleeve on her right arm, a fine tattoo on the inside of her left arm and a fine floral tattoo on her chest below the left collarbone.",
  "wardrobe": "White ribbed tank top, loose black lightweight training shorts, and a thin gold chain with a small gold cross pendant.",
  "scene": "Her own garage training box, the same room as the reference image, unchanged: white-painted concrete block walls under a dark wood slat ceiling, a red neon sign on the left wall, a small American flag high on the wall at the right, and a metal-and-wood shelf with glass jars of seeds at the far right. A black table stands in front of her.",
  "prop": "Brandon holds a round clear glass mixing bowl full of cooked black beans with her left hand, pushed toward the lens, and her right hand raises a stainless steel potato masher with a flat perforated plate just above the beans, about to press down. On the black table in front of her lie only a wooden spoon and a wire whisk.",
  "posture": "Brandon is standing behind her black table, leaning slightly toward the camera, the left hand under the bowl, the right hand gripping the masher.",
  "composition": "The glass bowl of black beans fills about 25 percent of the frame at the lower center, held about 35 centimeters from the lens, large in frame and closer to the camera than her face; the masher rises beside it. From the chest up, her head and upper chest clear and centered in the upper half of the frame, her face about 70 centimeters from the lens. Nothing else competes with the bowl of black beans. The background is reduced by framing, never by blur.",
  "camera": "phone camera on a small tripod at chest height, 26 mm wide lens, straight on, slight downward angle toward the table, fixed",
  "lighting": "Neutral overcast daylight coming in from a wide open garage door out of frame, soft even light on the face with no harsh shadows, the red neon adding only a faint glow on the wall behind her.",
  "state": "Start frame: the masher is just above the whole shiny black beans, not a single bean mashed yet. Brandon looks into the lens, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, no second person in frame, no visible phone, no mashed beans yet, no chef jacket"
}
```

### K02 · T2, close da tigela, dois ovos entrando no feijão (voz fora de quadro) · anexar ÂNCORA

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Brandon's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Brandon, explicitly female: Black mixed-race American woman around thirty, athletic build, light brown skin with light freckles across her nose and cheeks, brown eyes, cornrow braids that turn into long loose braids down to her waist with wooden and gold beads at the tips, small stud earrings, a floral blackwork tattoo sleeve on her right arm, a fine tattoo on the inside of her left arm and a fine floral tattoo on her chest below the left collarbone.",
  "wardrobe": "White ribbed tank top, loose black lightweight training shorts, and a thin gold chain with a small gold cross pendant.",
  "scene": "Her own garage training box, the same room as the reference image, unchanged: white-painted concrete block walls under a dark wood slat ceiling, a red neon sign on the left wall, a small American flag high on the wall at the right, and a metal-and-wood shelf with glass jars of seeds at the far right. A black table stands in front of her.",
  "prop": "A round clear glass mixing bowl of roughly mashed black beans stands on the black table in the lower foreground. Her right hand tips a small clear glass cup, and two whole raw eggs with bright orange yolks slide out of it into the beans. Beside the bowl on the black table stand three small clear glass bowls: one of cocoa powder, one of golden raw honey and one of ground cinnamon. Nothing else is on the table.",
  "posture": "Close shot: only her hands and the white ribbed tank top of her torso behind them are in frame, her face above the top edge of the frame; only the tip of her chin shows at the very top edge.",
  "composition": "The bowl of black beans fills the bottom 40 percent of the frame, about 40 centimeters from the lens, very close to the lens and large in frame, the eggs sliding in at its center; the three small bowls sit beside it. No face in frame. The background is reduced by framing, never by blur.",
  "camera": "phone camera on a small tripod at chest height, tilted down about 30 degrees toward the table, 26 mm wide lens, fixed",
  "lighting": "Neutral overcast daylight coming in from a wide open garage door out of frame, soft even light on the face with no harsh shadows, the red neon adding only a faint glow on the wall behind her.",
  "state": "Start frame: the first egg yolk is just touching the black beans, the second still sliding out of the cup.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, no second person in frame, no visible phone, no face in frame, no cracked eggshell pieces in the bowl"
}
```

### K03 · T3, close, colher de cacau em pó sobre a tigela · anexar ÂNCORA

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Brandon's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Brandon, explicitly female: Black mixed-race American woman around thirty, athletic build, light brown skin with light freckles across her nose and cheeks, brown eyes, cornrow braids that turn into long loose braids down to her waist with wooden and gold beads at the tips, small stud earrings, a floral blackwork tattoo sleeve on her right arm, a fine tattoo on the inside of her left arm and a fine floral tattoo on her chest below the left collarbone.",
  "wardrobe": "White ribbed tank top, loose black lightweight training shorts, and a thin gold chain with a small gold cross pendant.",
  "scene": "Her own garage training box, the same room as the reference image, unchanged: white-painted concrete block walls under a dark wood slat ceiling, a red neon sign on the left wall, a small American flag high on the wall at the right, and a metal-and-wood shelf with glass jars of seeds at the far right. A black table stands in front of her.",
  "prop": "Inside a round clear glass mixing bowl on the black table: roughly mashed black beans with two raw egg yolks on top. Her right hand holds a metal spoon heaped with dark cocoa powder right above the yolks, and her left hand holds a small clear glass bowl of cocoa powder just behind it. Nothing else is in frame.",
  "posture": "Close shot: only her hands and the white ribbed tank top of her torso behind them are in frame, her face above the top edge of the frame.",
  "composition": "The bowl fills the bottom 60 percent of the frame, about 30 centimeters from the lens, very close to the lens and large in frame, the heaped spoon of cocoa at the center. No face in frame. The background is reduced by framing, never by blur.",
  "camera": "phone camera held above the table at chest height, looking down at about 45 degrees into the bowl, 26 mm wide lens, fixed",
  "lighting": "Neutral overcast daylight coming in from a wide open garage door out of frame, soft even light on the face with no harsh shadows, the red neon adding only a faint glow on the wall behind her.",
  "state": "Start frame: the spoon is full and level, the first grains of cocoa starting to fall onto the yolks.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, no second person in frame, no visible phone, no face in frame"
}
```

### K04 · T4, close, mel cru escorrendo da colher · anexar ÂNCORA

```text
K04
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Brandon's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Brandon, explicitly female: Black mixed-race American woman around thirty, athletic build, light brown skin with light freckles across her nose and cheeks, brown eyes, cornrow braids that turn into long loose braids down to her waist with wooden and gold beads at the tips, small stud earrings, a floral blackwork tattoo sleeve on her right arm, a fine tattoo on the inside of her left arm and a fine floral tattoo on her chest below the left collarbone.",
  "wardrobe": "White ribbed tank top, loose black lightweight training shorts, and a thin gold chain with a small gold cross pendant.",
  "scene": "Her own garage training box, the same room as the reference image, unchanged: white-painted concrete block walls under a dark wood slat ceiling, a red neon sign on the left wall, a small American flag high on the wall at the right, and a metal-and-wood shelf with glass jars of seeds at the far right. A black table stands in front of her.",
  "prop": "Inside a round clear glass mixing bowl on the black table: roughly mashed black beans with raw egg and cocoa powder on top. Her right hand holds a metal spoon above the bowl, and a thick glossy stream of golden raw honey pours from it onto the beans. Nothing else is in frame.",
  "posture": "Close shot: only her hands and the white ribbed tank top of her torso behind them are in frame, her face above the top edge of the frame.",
  "composition": "The bowl fills the bottom 55 percent of the frame, about 30 centimeters from the lens, very close to the lens and large in frame, the honey stream in the center of the frame. No face in frame. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height just above the bowl rim, slight downward angle, 26 mm wide lens, fixed",
  "lighting": "Neutral overcast daylight coming in from a wide open garage door out of frame, soft even light on the face with no harsh shadows, the red neon adding only a faint glow on the wall behind her.",
  "state": "Start frame: the honey stream is already falling in one unbroken golden ribbon.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, no second person in frame, no visible phone, no face in frame"
}
```

### K05 · T5, close, canela em pó caindo no centro da tigela · anexar ÂNCORA

```text
K05
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Brandon's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Brandon, explicitly female: Black mixed-race American woman around thirty, athletic build, light brown skin with light freckles across her nose and cheeks, brown eyes, cornrow braids that turn into long loose braids down to her waist with wooden and gold beads at the tips, small stud earrings, a floral blackwork tattoo sleeve on her right arm, a fine tattoo on the inside of her left arm and a fine floral tattoo on her chest below the left collarbone.",
  "wardrobe": "White ribbed tank top, loose black lightweight training shorts, and a thin gold chain with a small gold cross pendant.",
  "scene": "Her own garage training box, the same room as the reference image, unchanged: white-painted concrete block walls under a dark wood slat ceiling, a red neon sign on the left wall, a small American flag high on the wall at the right, and a metal-and-wood shelf with glass jars of seeds at the far right. A black table stands in front of her.",
  "prop": "Inside a round clear glass mixing bowl on the black table: roughly mashed black beans glossy with honey, egg and cocoa. Her right hand tips a metal spoon of reddish-brown ground cinnamon over the center of the bowl, the powder just starting to fall. Nothing else is in frame.",
  "posture": "Close shot: only her hands and the white ribbed tank top of her torso behind them are in frame, her face above the top edge of the frame.",
  "composition": "The bowl fills the bottom 60 percent of the frame, about 30 centimeters from the lens, very close to the lens and large in frame, the spoon of cinnamon at the center. No face in frame. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height above the bowl, looking down at about 45 degrees, 26 mm wide lens, fixed",
  "lighting": "Neutral overcast daylight coming in from a wide open garage door out of frame, soft even light on the face with no harsh shadows, the red neon adding only a faint glow on the wall behind her.",
  "state": "Start frame: the spoon is tipping and the first cinnamon falls onto the glossy beans.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, no second person in frame, no visible phone, no face in frame"
}
```

### K06 · T6, close, batedor na massa de chocolate (voz fora de quadro) · anexar ÂNCORA

```text
K06
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Brandon's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Brandon, explicitly female: Black mixed-race American woman around thirty, athletic build, light brown skin with light freckles across her nose and cheeks, brown eyes, cornrow braids that turn into long loose braids down to her waist with wooden and gold beads at the tips, small stud earrings, a floral blackwork tattoo sleeve on her right arm, a fine tattoo on the inside of her left arm and a fine floral tattoo on her chest below the left collarbone.",
  "wardrobe": "White ribbed tank top, loose black lightweight training shorts, and a thin gold chain with a small gold cross pendant.",
  "scene": "Her own garage training box, the same room as the reference image, unchanged: white-painted concrete block walls under a dark wood slat ceiling, a red neon sign on the left wall, a small American flag high on the wall at the right, and a metal-and-wood shelf with glass jars of seeds at the far right. A black table stands in front of her.",
  "prop": "A round clear glass mixing bowl on the black table is full of smooth, glossy, thick chocolate-brown batter. Her right hand works a stainless steel wire whisk through it, leaving swirls, and her left hand steadies the bowl rim. Nothing else is in frame.",
  "posture": "Close shot: only her hands and the white ribbed tank top of her torso behind them are in frame, her face above the top edge of the frame.",
  "composition": "The bowl of batter fills the bottom 60 percent of the frame, about 30 centimeters from the lens, very close to the lens and large in frame, the whisk swirls at the center. No face in frame. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height just above the bowl, slight downward angle, 26 mm wide lens, fixed",
  "lighting": "Neutral overcast daylight coming in from a wide open garage door out of frame, soft even light on the face with no harsh shadows, the red neon adding only a faint glow on the wall behind her.",
  "state": "Start frame: the whisk is mid-stroke in the smooth glossy batter.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, no second person in frame, no visible phone, no face in frame, no whole beans visible in the batter"
}
```

### K07 · T7, close, massa escorrendo para a forma forrada · anexar ÂNCORA

```text
K07
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Brandon's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Brandon, explicitly female: Black mixed-race American woman around thirty, athletic build, light brown skin with light freckles across her nose and cheeks, brown eyes, cornrow braids that turn into long loose braids down to her waist with wooden and gold beads at the tips, small stud earrings, a floral blackwork tattoo sleeve on her right arm, a fine tattoo on the inside of her left arm and a fine floral tattoo on her chest below the left collarbone.",
  "wardrobe": "White ribbed tank top, loose black lightweight training shorts, and a thin gold chain with a small gold cross pendant.",
  "scene": "Her own garage training box, the same room as the reference image, unchanged: white-painted concrete block walls under a dark wood slat ceiling, a red neon sign on the left wall, a small American flag high on the wall at the right, and a metal-and-wood shelf with glass jars of seeds at the far right. A black table stands in front of her.",
  "prop": "Her left hand tilts the round clear glass mixing bowl over a square dark metal baking tin lined with parchment paper on the black table, and a thick ribbon of glossy chocolate batter pours out and folds into a mound in the center of the tin. Her right hand holds the wire whisk against the bowl. Nothing else is in frame.",
  "posture": "Close shot: only her hands and the white ribbed tank top of her torso behind them are in frame, her face above the top edge of the frame.",
  "composition": "The square baking tin fills the bottom 45 percent of the frame, about 35 centimeters from the lens, very close to the lens and large in frame; the ribbon of batter runs down the center of the frame from the tilted bowl. No face in frame. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, looking down at about 40 degrees at the tin on the table, 26 mm wide lens, fixed",
  "lighting": "Neutral overcast daylight coming in from a wide open garage door out of frame, soft even light on the face with no harsh shadows, the red neon adding only a faint glow on the wall behind her.",
  "state": "Start frame: the ribbon of batter is already falling and has started a small mound in the tin.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, no second person in frame, no visible phone, no face in frame"
}
```

### K08 · T8, a forma entrando no forno de bancada do box · anexar ÂNCORA

```text
K08
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Brandon's exact identity, wardrobe and own setting. Do not copy its pose or framing. The countertop oven is new: it stands on the same metal-and-wood shelf of her garage box.",
  "identity_main": "The exact fictional AI character Brandon, explicitly female: Black mixed-race American woman around thirty, athletic build, light brown skin with light freckles across her nose and cheeks, brown eyes, cornrow braids that turn into long loose braids down to her waist with wooden and gold beads at the tips, small stud earrings, a floral blackwork tattoo sleeve on her right arm, a fine tattoo on the inside of her left arm and a fine floral tattoo on her chest below the left collarbone.",
  "wardrobe": "White ribbed tank top, loose black lightweight training shorts, and a thin gold chain with a small gold cross pendant.",
  "scene": "Her own garage training box, the same room as the reference image, unchanged: white-painted concrete block walls under a dark wood slat ceiling, a red neon sign on the left wall, a small American flag high on the wall at the right, and a metal-and-wood shelf with glass jars of seeds at the far right. A black table stands in front of her.",
  "prop": "A stainless steel countertop convection oven with a black glass door, a plain smooth front and two simple round black knobs, stands on the metal-and-wood shelf of her garage box, the door wide open and the wire rack visible inside. Her two hands slide the square metal baking tin of raw chocolate batter, lined with parchment paper, onto the rack. Nothing else is in frame.",
  "posture": "Only her forearms and hands enter the frame from the left, sliding the tin in; no face in frame.",
  "composition": "The open countertop oven fills about 70 percent of the frame, its open door about 50 centimeters from the lens, large in frame and centered, the tin halfway onto the rack. No face in frame. The background is reduced by framing, never by blur.",
  "camera": "phone camera at counter level on the shelf, level with the oven rack, 26 mm wide lens, straight on, fixed",
  "lighting": "Neutral overcast daylight coming in from a wide open garage door out of frame, soft even light on the face with no harsh shadows, the red neon adding only a faint glow on the wall behind her.",
  "state": "Start frame: the tin is halfway onto the rack, the oven light on inside.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, no second person in frame, no visible phone, no face in frame"
}
```

### K09 · T9, reveal, brownie pronto na mesa e os potinhos na frente · anexar ÂNCORA

```text
K09
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Brandon's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Brandon, explicitly female: Black mixed-race American woman around thirty, athletic build, light brown skin with light freckles across her nose and cheeks, brown eyes, cornrow braids that turn into long loose braids down to her waist with wooden and gold beads at the tips, small stud earrings, a floral blackwork tattoo sleeve on her right arm, a fine tattoo on the inside of her left arm and a fine floral tattoo on her chest below the left collarbone.",
  "wardrobe": "White ribbed tank top, loose black lightweight training shorts, and a thin gold chain with a small gold cross pendant.",
  "scene": "Her own garage training box, the same room as the reference image, unchanged: white-painted concrete block walls under a dark wood slat ceiling, a red neon sign on the left wall, a small American flag high on the wall at the right, and a metal-and-wood shelf with glass jars of seeds at the far right. A black table stands in front of her.",
  "prop": "On the black table in front of her: a square dark metal baking tin of freshly baked fudgy brownies with a crackly shiny top, still in its parchment paper, and in front of it a row of five small bowls holding black beans, cocoa powder, one raw egg yolk, ground cinnamon and golden raw honey, with a pair of grey oven mitts at the left. Nothing else is on the table.",
  "posture": "Brandon is standing behind her black table, both hands raised in front of her chest mid-gesture, open palms, talking.",
  "composition": "The tin of brownies and the row of small bowls fill the bottom 30 percent of the frame, the front bowls about 40 centimeters from the lens, closer to the camera than her face. From the waist up, her head and upper chest clear and centered in the upper half of the frame, her face about 80 centimeters from the lens. The background is reduced by framing, never by blur.",
  "camera": "phone camera on a small tripod at chest height, 26 mm wide lens, straight on, slight downward angle toward the table, fixed",
  "lighting": "Neutral overcast daylight coming in from a wide open garage door out of frame, soft even light on the face with no harsh shadows, the red neon adding only a faint glow on the wall behind her.",
  "state": "Start frame: Brandon gestures with both open hands over the brownies, eyes on the lens, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, no second person in frame, no visible phone, no chef jacket"
}
```

### K11 · T11, selfie com o pedaço de brownie perto da lente (fechamento e CTA) · anexar ÂNCORA

```text
K11
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Brandon's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Brandon, explicitly female: Black mixed-race American woman around thirty, athletic build, light brown skin with light freckles across her nose and cheeks, brown eyes, cornrow braids that turn into long loose braids down to her waist with wooden and gold beads at the tips, small stud earrings, a floral blackwork tattoo sleeve on her right arm, a fine tattoo on the inside of her left arm and a fine floral tattoo on her chest below the left collarbone.",
  "wardrobe": "White ribbed tank top, loose black lightweight training shorts, and a thin gold chain with a small gold cross pendant.",
  "scene": "Her own garage training box, the same room as the reference image, unchanged: white-painted concrete block walls under a dark wood slat ceiling, a red neon sign on the left wall, a small American flag high on the wall at the right, and a metal-and-wood shelf with glass jars of seeds at the far right. A black table stands in front of her.",
  "prop": "Brandon holds a thick square piece of fudgy chocolate brownie with a crackly shiny top in her right hand, close to the lens at the lower left of the frame. The piece is whole, not bitten.",
  "posture": "Selfie: her left arm is stretched out toward the camera holding the phone out of frame at the right edge; her right hand holds the brownie piece up near the lens.",
  "composition": "Tightest shot of the video. The brownie piece fills about 15 percent of the frame at the lower left, about 25 centimeters from the lens, closer to the camera than her face; her face is clear in the upper center, about 50 centimeters from the lens, head and shoulders in frame, the extended left arm entering from the right edge. The background is reduced by framing, never by blur.",
  "camera": "front phone camera held at arm's length at eye level, ultra-wide 0.5x selfie lens, slight high angle, handheld",
  "lighting": "Neutral overcast daylight coming in from a wide open garage door out of frame, soft even light on the face with no harsh shadows, the red neon adding only a faint glow on the wall behind her.",
  "state": "Start frame: Brandon looks straight into the lens with a serious, certain expression, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, no second person in frame, no bitten brownie"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem que você deixou no K01

```text
V01
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina média, firme e calorosa de uma mulher atlética de uns trinta anos, entonação direta e curiosa, de quem vai contar uma receita que parece impossível, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If you mash one can of black beans,"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon amassa o feijão preto na tigela com o amassador, duas ou três vezes, segurando a tigela perto da câmera; ela diz a frase em ritmo natural logo no começo e continua amassando olhando para a lente.

câmera: fixa, no tripé, na altura do peito

som ambiente: box de treino tranquilo, som do amassador no feijão, sem música
```

### V02 · T2 · frame inicial = a imagem que você deixou no K02

```text
V02
a avatar Brandon, mulher, fora de quadro (só as mãos e a regata aparecem, o rosto fica acima do quadro), fala em inglês com sotaque americano de uma mulher negra americana, voz feminina média, firme e calorosa de uma mulher atlética de uns trinta anos, no ritmo de quem dita uma receita, clara e segura, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "mix in two eggs, two tablespoons of cocoa powder, three tablespoons of raw honey and half a teaspoon of cinnamon,"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a mão vira o potinho e os dois ovos caem inteiros dentro da tigela de feijão; só a regata e a ponta do queixo aparecem, o rosto fica fora de quadro. A voz diz a frase inteira em ritmo natural logo no começo e o resto do clipe é a tigela.

câmera: fixa, levemente de cima para a tigela

som ambiente: box de treino tranquilo, som leve dos ovos caindo, sem música
```

### V03 · T3 · frame inicial = a imagem que você deixou no K03

```text
V03
(sem fala no take: a fala do T2 continua como voz-over na edição)

o que acontece no vídeo: a colher vira o cacau em pó dentro da tigela, em cima dos ovos e do feijão.

câmera: fixa, de cima para dentro da tigela

som ambiente: box de treino tranquilo, som leve da colher, sem música
```

### V04 · T4 · frame inicial = a imagem que você deixou no K04

```text
V04
(sem fala no take: a fala do T2 continua como voz-over na edição)

o que acontece no vídeo: o mel cru cai da colher em fio grosso e dourado sobre o feijão.

câmera: fixa, logo acima da borda da tigela

som ambiente: box de treino tranquilo, sem música
```

### V05 · T5 · frame inicial = a imagem que você deixou no K05

```text
V05
(sem fala no take: a fala do T2 continua como voz-over na edição)

o que acontece no vídeo: a colher vira a canela em pó no centro da tigela.

câmera: fixa, de cima para dentro da tigela

som ambiente: box de treino tranquilo, som leve da colher, sem música
```

### V06 · T6 · frame inicial = a imagem que você deixou no K06

```text
V06
a avatar Brandon, mulher, fora de quadro (só as mãos e a regata aparecem, o rosto fica acima do quadro), fala em inglês com sotaque americano de uma mulher negra americana, voz feminina média, firme e calorosa de uma mulher atlética de uns trinta anos, no ritmo de quem dita uma receita, clara e segura, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "pour into a greased tin and bake at 350 for 20 minutes."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o batedor de arame gira na massa de chocolate lisa e brilhante, fazendo espirais; só as mãos e a regata aparecem. A voz diz a frase inteira em ritmo natural logo no começo e o resto do clipe é a massa sendo batida.

câmera: fixa, logo acima da tigela

som ambiente: box de treino tranquilo, som do batedor na tigela de vidro, sem música
```

### V07 · T7 · frame inicial = a imagem que você deixou no K07

```text
V07
(sem fala no take: a fala do T6 continua como voz-over na edição)

o que acontece no vídeo: a tigela inclina e a massa grossa de chocolate escorre em fita para dentro da forma forrada, empilhando em dobras.

câmera: fixa, de cima para a forma

som ambiente: box de treino tranquilo, som leve da massa caindo, sem música
```

### V08 · T8 · frame inicial = a imagem que você deixou no K08

```text
V08
(sem fala no take: a fala do T6 continua como voz-over na edição)

o que acontece no vídeo: as mãos empurram a forma até o fundo do forno de bancada e a porta começa a fechar.

câmera: fixa, na altura da prateleira do forno

som ambiente: box de treino tranquilo, som do forno e da grade de metal, sem música
```

### V09 · T9 · frame inicial = a imagem que você deixou no K09

```text
V09
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina média, firme e calorosa de uma mulher atlética de uns trinta anos, entonação animada e apetitosa, com um sorriso na voz, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "What you get are fudgy rich chocolate brownies that not only look like they came straight out of a proper bakery but feed the good bacteria in your gut."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon gesticula com as duas mãos abertas por cima do brownie e fala para a câmera, animada.

câmera: fixa, no tripé, na altura do peito

som ambiente: box de treino tranquilo, sem música
```

### V10 · T10 · frame inicial = a imagem que você deixou no K09

```text
V10
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina média, firme e calorosa de uma mulher atlética de uns trinta anos, entonação confiante e calorosa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Slow down how fast sugar hits your blood and keep your sugar craving dead quiet for hours."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon continua falando para a câmera com gestos pequenos por cima do brownie, confiante.

câmera: fixa, no tripé, na altura do peito

som ambiente: box de treino tranquilo, sem música
```

### V11 · T11 · frame inicial = a imagem que você deixou no K11

```text
V11
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina média, firme e calorosa de uma mulher atlética de uns trinta anos, a voz muda de animada para séria, firme, como quem vai contar o que ninguém conta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "And this works. But quieting the craving for a few hours is the smallest part of it. What matters is why it comes back every single night."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, em selfie, segura o pedaço de brownie perto da lente e fala direto com a câmera; a expressão muda de animada para séria.

câmera: selfie na mão com leve tremor natural; a mão que segura o celular nunca se mexe, só a outra mão se move com o brownie

som ambiente: box de treino tranquilo, sem música
```

### V12 · T12 · frame inicial = a imagem que você deixou no K11

```text
V12
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina média, firme e calorosa de uma mulher atlética de uns trinta anos, entonação firme e acolhedora, com convicção total no 'It's not', voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Every woman over forty I coach tells me it's willpower. It's not. A recipe is not a diagnosis, and nobody ever told you what yours is."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, em selfie, segura o pedaço de brownie perto da lente e fala direto com a câmera, firme, balançando a cabeça de leve no 'It's not'.

câmera: selfie na mão com leve tremor natural; a mão que segura o celular nunca se mexe, só a outra mão se move com o brownie

som ambiente: box de treino tranquilo, sem música
```

### V13 · T13 · frame inicial = a imagem que você deixou no K11

```text
V13
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina média, firme e calorosa de uma mulher atlética de uns trinta anos, entonação didática e firme, sem pressa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "After forty that craving comes from one of three places: your hormones, your gut or your metabolism. This brownie calms one. If yours is another, it comes right back."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, em selfie, levanta um pouco o pedaço de brownie no 'This brownie calms one' e fala direto com a câmera.

câmera: selfie na mão com leve tremor natural; a mão que segura o celular nunca se mexe, só a outra mão se move com o brownie

som ambiente: box de treino tranquilo, sem música
```

### V14 · T14 · frame inicial = a imagem que você deixou no K11

```text
V14
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina média, firme e calorosa de uma mulher atlética de uns trinta anos, entonação firme, com um leve tom de indignação com o app, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "A calorie app would just tell you to skip the brownie, which makes the craving louder. And guessing which one is yours can cost you another year."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, em selfie, segura o pedaço de brownie perto da lente e fala direto com a câmera, firme.

câmera: selfie na mão com leve tremor natural; a mão que segura o celular nunca se mexe, só a outra mão se move com o brownie

som ambiente: box de treino tranquilo, sem música
```

### V15 · T15 · frame inicial = a imagem que você deixou no K11

```text
V15
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina média, firme e calorosa de uma mulher atlética de uns trinta anos, entonação direta e segura, sem sorrir, olhando fundo na lente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Comment yes if that craving hits you every night, and follow me so you don't lose this."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, em selfie, segura o pedaço de brownie perto da lente e fala direto com a câmera, séria e segura.

câmera: selfie na mão com leve tremor natural; a mão que segura o celular nunca se mexe, só a outra mão se move com o brownie

som ambiente: box de treino tranquilo, sem música
```

### V16 · T16 · frame inicial = a imagem que você deixou no K11

```text
V16
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina média, firme e calorosa de uma mulher atlética de uns trinta anos, entonação firme, urgente e convicta, sem tom de oferta, como quem aponta a única saída, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Your personalized FityWell Metabolic Reset plan is the only way to find which of the three is yours. Tap the link in the pinned comment before tonight's craving hits."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, em selfie, se aproxima um pouco da lente e fala direto com a câmera, firme e urgente, segurando o pedaço de brownie.

câmera: selfie na mão com leve tremor natural; a mão que segura o celular nunca se mexe, só a outra mão se move com o brownie

som ambiente: box de treino tranquilo, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01, V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14, V15, V16.
2. Cortes no tempo das cenas do modelo: V01 0,0 a 2,4 s; V02 2,4 a 3,5 s (o áudio corre até 8,2 s); V03 3,5 a 5,2 s; V04 5,2 a 6,8 s; V05 6,8 a 8,2 s; V06 8,2 a 9,1 s (o áudio corre até 10,9 s); V07 9,1 a 10,5 s; V08 10,5 a 10,9 s; V09 10,9 a 19,2 s; V10 19,2 a 24,7 s; V11 clipe inteiro, corte no fim da frase; V12 clipe inteiro, corte no fim da frase; V13 clipe inteiro, corte no fim da frase; V14 clipe inteiro, corte no fim da frase; V15 clipe inteiro, corte no fim da frase; V16 clipe inteiro, corte no fim da frase.
3. Voz-over: o áudio do V02 corre por baixo de V02, V03, V04 e V05; o do V06 corre por baixo de V06, V07 e V08. Os B-rolls entram sem áudio próprio.
4. Zero tempo morto: todo clipe falado começa já falando. Isolate Voice / Keep Vocal no áudio.
5. Legenda de uma palavra por vez, caixa alta, fonte bold branca com contorno, no meio do quadro, do começo ao fim, igual ao modelo.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Música só do V09 em diante, nunca no gancho nem na receita, entre -19 e -20 dB, fora da biblioteca do TikTok.
8. Rótulo pequeno `AI-generated` num canto do vídeo.
9. No V16, uma seta de edição apontando para baixo (comentário fixado) na frase "Tap the link in the pinned comment". Fixar o comentário com o link no vídeo publicado.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | If you mash one can of black beans, | Se você amassar uma lata de feijão preto, |
| T2 | mix in two eggs, two tablespoons of cocoa powder, three tablespoons of raw honey and half a teaspoon of cinnamon, | misturar dois ovos, duas colheres de sopa de cacau em pó, três colheres de sopa de mel cru e meia colher de chá de canela, |
| T3 | (B-roll, sem fala) | (B-roll, sem fala) |
| T4 | (B-roll, sem fala) | (B-roll, sem fala) |
| T5 | (B-roll, sem fala) | (B-roll, sem fala) |
| T6 | pour into a greased tin and bake at 350 for 20 minutes. | despejar numa forma untada e assar a 180 graus por 20 minutos. |
| T7 | (B-roll, sem fala) | (B-roll, sem fala) |
| T8 | (B-roll, sem fala) | (B-roll, sem fala) |
| T9 | What you get are fudgy rich chocolate brownies that not only look like they came straight out of a proper bakery but feed the good bacteria in your gut. | O que você ganha são brownies de chocolate cremosos e intensos, que não só parecem ter saído direto de uma confeitaria de verdade, como alimentam as bactérias boas do seu intestino. |
| T10 | Slow down how fast sugar hits your blood and keep your sugar craving dead quiet for hours. | Diminuem a velocidade com que o açúcar chega no seu sangue e deixam sua vontade de doce completamente quieta por horas. |
| T11 | And this works. But quieting the craving for a few hours is the smallest part of it. What matters is why it comes back every single night. | E isso funciona. Mas acalmar a vontade por algumas horas é a menor parte. O que importa é por que ela volta toda santa noite. |
| T12 | Every woman over forty I coach tells me it's willpower. It's not. A recipe is not a diagnosis, and nobody ever told you what yours is. | Toda mulher acima dos quarenta que eu acompanho me diz que é força de vontade. Não é. Receita não é diagnóstico, e ninguém nunca te disse qual é o seu. |
| T13 | After forty that craving comes from one of three places: your hormones, your gut or your metabolism. This brownie calms one. If yours is another, it comes right back. | Depois dos quarenta essa vontade vem de um de três lugares: seus hormônios, seu intestino ou seu metabolismo. Esse brownie acalma um. Se o seu for outro, ela volta na hora. |
| T14 | A calorie app would just tell you to skip the brownie, which makes the craving louder. And guessing which one is yours can cost you another year. | Um app de calorias só ia te mandar cortar o brownie, e isso deixa a vontade ainda mais alta. E adivinhar qual é o seu pode te custar mais um ano. |
| T15 | Comment yes if that craving hits you every night, and follow me so you don't lose this. | Comente yes se essa vontade te pega toda noite, e me siga para não perder isso. |
| T16 | Your personalized FityWell Metabolic Reset plan is the only way to find which of the three is yours. Tap the link in the pinned comment before tonight's craving hits. | O seu plano personalizado Metabolic Reset da FityWell é o único jeito de descobrir qual das três é a sua. Toque no link do comentário fixado antes da vontade de hoje à noite chegar. |

## 6. Roteiro final em inglês

1. If you mash one can of black beans,
2. mix in two eggs, two tablespoons of cocoa powder, three tablespoons of raw honey and half a teaspoon of cinnamon,
6. pour into a greased tin and bake at 350 for 20 minutes.
9. What you get are fudgy rich chocolate brownies that not only look like they came straight out of a proper bakery but feed the good bacteria in your gut.
10. Slow down how fast sugar hits your blood and keep your sugar craving dead quiet for hours.
11. And this works. But quieting the craving for a few hours is the smallest part of it. What matters is why it comes back every single night.
12. Every woman over forty I coach tells me it's willpower. It's not. A recipe is not a diagnosis, and nobody ever told you what yours is.
13. After forty that craving comes from one of three places: your hormones, your gut or your metabolism. This brownie calms one. If yours is another, it comes right back.
14. A calorie app would just tell you to skip the brownie, which makes the craving louder. And guessing which one is yours can cost you another year.
15. Comment yes if that craving hits you every night, and follow me so you don't lose this.
16. Your personalized FityWell Metabolic Reset plan is the only way to find which of the three is yours. Tap the link in the pinned comment before tonight's craving hits.

If you mash one can of black beans, mix in two eggs, two tablespoons of cocoa powder, three tablespoons of raw honey and half a teaspoon of cinnamon, pour into a greased tin and bake at 350 for 20 minutes. What you get are fudgy rich chocolate brownies that not only look like they came straight out of a proper bakery but feed the good bacteria in your gut. Slow down how fast sugar hits your blood and keep your sugar craving dead quiet for hours. And this works. But quieting the craving for a few hours is the smallest part of it. What matters is why it comes back every single night. Every woman over forty I coach tells me it's willpower. It's not. A recipe is not a diagnosis, and nobody ever told you what yours is. After forty that craving comes from one of three places: your hormones, your gut or your metabolism. This brownie calms one. If yours is another, it comes right back. A calorie app would just tell you to skip the brownie, which makes the craving louder. And guessing which one is yours can cost you another year. Comment yes if that craving hits you every night, and follow me so you don't lose this. Your personalized FityWell Metabolic Reset plan is the only way to find which of the three is yours. Tap the link in the pinned comment before tonight's craving hits.
