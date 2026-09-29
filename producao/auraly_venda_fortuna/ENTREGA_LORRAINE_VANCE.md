# ENTREGA | Lorraine Vance | Auraly Venda Fortuna

Produção `auraly_venda_fortuna` · Ângulo 3 · SALE (ramificação de dinheiro) · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY

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

Checklist de envio: 33/33 aprovados (N/A: A1, A7, A9 fiéis ao modelo, gancho mudo sem fala; C3 a C7 sem segunda pessoa, selfie, frase curta repetida, cena atuada ou motion control)

Ficha: 3/3 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos e mapa

- **Âncora Lorraine Vance:** `producao/_ancoras/lorraine_vance_ancora.jpg` em TODOS os K.
- **Em cada K**, anexar também o frame do modelo daquele K (`input/frames_modelo/Kxx_modelo.png`), só como composição.

```text
MAPA K/V
V01: K01
V02: K02
V03: K03
V04: K03
V05: K03
V06: K03
V07: K03
V08: K03
V09: K03
V10: K03
V11: K03
V12: K03
V13: K03
V14: K03
V15: K03
V16: K03
V17: K03
V18: K03
```

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho mudo, sal no prato dourado e as pombas · anexar ÂNCORA + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Lorraine Vance's exact identity, wardrobe, jewelry, SOULMATE card and own setting. Use the second attached image only as a composition reference for the camera position, framing and action; do not copy its person, clothes, room, pendant, labels or on-screen text.",
  "identity_main": "The exact fictional AI character Lorraine Vance: white American woman around fifty-two, closely shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, fine lines and no makeup.",
  "wardrobe": "Light-wash denim shirt worn open over a fitted black crew-neck T-shirt, dark jeans, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar.",
  "scene": "Her own bright white American kitchen, the same lived-in kitchen as the reference, unchanged. She stands at the white-framed kitchen window opened wide, with a wide white ledge under it; through the open window a quiet American residential street with houses, lawns and parked cars is clearly visible. On the light wood floating shelf beside the window clear quartz crystal points, a lit incense stick with a thin line of smoke and a small American flag, discreet but visible and in focus; on the white wall a framed zodiac wheel chart and a small wooden crucifix.",
  "prop": "A shallow round gold plate with a wide flat rim, plain polished gold with soft reflections, sits empty on the ledge of the open kitchen window in the lower left corner. Lorraine Vance holds a small dark wooden bowl heaped with coarse white salt crystals with both hands at waist height, starting to tip it toward the plate.",
  "posture": "Lorraine Vance stands right beside the plate, body turned slightly toward the lens, looking straight into the lens with a serious, calm face, mouth closed.",
  "composition": "The gold plate is very close to the lens in the lower left corner, about 12 inches from the lens, and takes up about 20 percent of the frame; the bowl in her hands sits just behind it; both are closer to the camera than her face, nothing else competing with them. Lorraine Vance fills the right half from the waist up, face in the upper third; the open kitchen window fills the left half. Nothing else is on the ledge. The background is reduced by framing, never by blur.",
  "camera": "phone on a tripod at chest height, 1x lens, about three feet from the face, straight on, fixed",
  "lighting": "Neutral overcast daylight from the open window, the street outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the bowl is just starting to tip; the plate is still empty; no birds in frame yet.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed lettering on the plate, the bowl or the medallion, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no glowing aura, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no birds yet, no salt already on the plate, no pendant in frame, no card in frame"
}
```

### K02 · T2, inserto mudo, medalhão colado na lente · anexar ÂNCORA + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Lorraine Vance's exact identity, wardrobe, jewelry, SOULMATE card and own setting. Use the second attached image only as a composition reference for the camera position, framing and action; do not copy its person, clothes, room, pendant, labels or on-screen text.",
  "identity_main": "The exact fictional AI character Lorraine Vance: white American woman around fifty-two, closely shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, fine lines and no makeup.",
  "wardrobe": "Light-wash denim shirt worn open over a fitted black crew-neck T-shirt, dark jeans, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar.",
  "scene": "Her own bright white American kitchen, the same lived-in kitchen as the reference, unchanged. She stands at the white-framed kitchen window opened wide, with a wide white ledge under it; through the open window a quiet American residential street with houses, lawns and parked cars is clearly visible. On the light wood floating shelf beside the window clear quartz crystal points, a lit incense stick with a thin line of smoke and a small American flag, discreet but visible and in focus; on the white wall a framed zodiac wheel chart and a small wooden crucifix.",
  "prop": "Lorraine Vance raises the medallion: a large round gold coin medallion about the size of a palm, with a raised sunburst and a small star engraved on its face and a thick beaded rim, hanging from a thick gold rope chain, held up by the chain in one raised hand, the medallion hanging motionless right in front of the lens. In the other hand, at waist height, the small dark wooden bowl heaped with coarse white salt crystals. On the ledge behind, the shallow round gold plate with a wide flat rim, plain polished gold with soft reflections, now covered with coarse white salt.",
  "posture": "Lorraine Vance stands beside the ledge, one arm raised holding the chain high, the gold coin medallion hanging between the lens and her face; her face is visible behind it, looking into the lens.",
  "composition": "Extreme close-up: the gold coin medallion hangs about 6 inches from the lens in the center and takes up about 30 percent of the frame, far larger than her face, the gold rope chain running up to her freckled fair hand with bare fingers at the top edge. The bowl sits in the lower right corner and the plate in the lower left. Nothing else is on the ledge. The background is reduced by framing, never by blur.",
  "camera": "phone on a tripod at chest height, 1x lens, straight on, fixed",
  "lighting": "Neutral overcast daylight from the open window, the street outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the medallion is already raised and still in front of the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed lettering on the plate, the bowl or the medallion, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no glowing aura, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no birds in frame, no card in frame, no figurine pendant"
}
```

### K03 · T3 a T18, corpo, medalhão e carta na janela · anexar ÂNCORA + FRAME DO MODELO

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Lorraine Vance's exact identity, wardrobe, jewelry, SOULMATE card and own setting. Use the second attached image only as a composition reference for the camera position, framing and action; do not copy its person, clothes, room, pendant, labels or on-screen text.",
  "identity_main": "The exact fictional AI character Lorraine Vance: white American woman around fifty-two, closely shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, fine lines and no makeup.",
  "wardrobe": "Light-wash denim shirt worn open over a fitted black crew-neck T-shirt, dark jeans, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar.",
  "scene": "Her own bright white American kitchen, the same lived-in kitchen as the reference, unchanged. She stands at the white-framed kitchen window opened wide, with a wide white ledge under it; through the open window a quiet American residential street with houses, lawns and parked cars is clearly visible. On the light wood floating shelf beside the window clear quartz crystal points, a lit incense stick with a thin line of smoke and a small American flag, discreet but visible and in focus; on the white wall a framed zodiac wheel chart and a small wooden crucifix.",
  "prop": "With one hand Lorraine Vance holds the gold rope chain up at shoulder height so the large round gold coin medallion about the size of a palm, with a raised sunburst and a small star engraved on its face and a thick beaded rim, hanging from a thick gold rope chain, hangs at chest height, held a little forward toward the lens. In the other hand, at chest height and facing the lens, she holds the holographic SOULMATE card from the reference: a tarot-sized card with a rainbow mirror-foil border and saturated art of a brown-haired woman and a man embracing under a rainbow glow, a bright heart and red roses at the bottom, with the word SOULMATE on a pale banner at the bottom. On the ledge in the lower left corner, a shallow round gold plate with a wide flat rim, plain polished gold with soft reflections, now empty.",
  "posture": "Lorraine Vance stands right beside the plate, body turned slightly toward the lens, from the waist up, talking to the lens.",
  "composition": "The empty gold plate is very close to the lens in the lower left corner, about 12 inches from the lens, and takes up about 20 percent of the frame; the gold coin medallion hangs at chest height held forward, closer to the camera than her face. Lorraine Vance fills the right half from the waist up, face in the upper third; the open kitchen window fills the left half. Nothing else is on the ledge. The background is reduced by framing, never by blur.",
  "camera": "phone on a tripod at chest height, 1x lens, about three feet from the face, straight on, fixed",
  "lighting": "Neutral overcast daylight from the open window, the street outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Lorraine Vance looks into the lens, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed lettering on the plate, the bowl or the medallion, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no glowing aura, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no birds in frame, no bowl in frame, no figurine pendant, no second card"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem escolhida do K01

```text
V01
(sem fala no take: gancho mudo, a avatar fica em silêncio o clipe inteiro, boca fechada)

o que acontece no vídeo: Lorraine Vance inclina a tigela e o sal grosso cai no prato dourado do parapeito, formando um montinho branco. Perto dos dois segundos e meio, a cortina entra com o vento e duas pombas brancas entram voando pela janela aberta e pousam no prato de sal. Lorraine Vance fica parada segurando a tigela, olhando séria para a lente.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sal caindo no prato, vento e bater de asas, sem música
```

### V02 · T2 · frame inicial = a imagem escolhida do K02

```text
V02
(sem fala no take: inserto mudo, a avatar fica em silêncio)

o que acontece no vídeo: o medalhão dourado de moeda balança de leve na corrente diante da lente, segurado no alto pela mão de Lorraine Vance, que olha para a lente atrás dele.

câmera: fixa, bem perto do medalhão

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, leve tilintar da corrente, sem música
```

### V03 · T3 · frame inicial = a imagem escolhida do K03

```text
V03
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, quase sussurrando, séria e confidencial, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "What you hear here stays between you and the universe. Tell no one. Only a handful will be shown this before the month is over."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o medalhão pendurado na corrente com uma mão e a carta com a outra, e fala baixo para a câmera.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V04 · T4 · frame inicial = a imagem escolhida do K03

```text
V04
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme, em tom de alerta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I don't know who you are, but stay right here, because if this found you today, it came to you as a last warning."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance olha firme para a lente, o medalhão balançando de leve na corrente.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V05 · T5 · frame inicial = a imagem escolhida do K03

```text
V05
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, baixa e emocionada, como quem revela um segredo, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Money, prosperity and love are rushing toward you right now. Keep it to yourself, but the 11:11 portal just opened in your life."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o medalhão pendurado na corrente com uma mão e a carta com a outra, e fala para a câmera com pequenos movimentos naturais.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V06 · T6 · frame inicial = a imagem escolhida do K03

```text
V06
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, calma e certa, com pausa antes de "You were chosen", voz autêntica, como se exigisse ser ouvida, a seguinte frase: "In 33 minutes, something extraordinary is going to happen in your life. The worst is over. You were chosen."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o medalhão pendurado na corrente com uma mão e a carta com a outra, e fala para a câmera com pequenos movimentos naturais.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V07 · T7 · frame inicial = a imagem escolhida do K03

```text
V07
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, séria, em tom de aviso, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "But if you scroll past this video, you will interrupt this energy, and the blessing will pass right by you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o medalhão pendurado na corrente com uma mão e a carta com a outra, e fala para a câmera com pequenos movimentos naturais.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V08 · T8 · frame inicial = a imagem escolhida do K03

```text
V08
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, calma e firme, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "However, if you immediately share this video with yourself, you will seal this blessing."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o medalhão pendurado na corrente com uma mão e a carta com a outra, e fala para a câmera com pequenos movimentos naturais.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V09 · T9 · frame inicial = a imagem escolhida do K03

```text
V09
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, de olhos semicerrados, como quem está vendo algo, baixa e intensa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I can see money, abundance and someone special stepping into your life. Something rare is moving around you as we speak."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance fecha os olhos por um instante e volta a olhar para a lente, segurando o medalhão e a carta.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V10 · T10 · frame inicial = a imagem escolhida do K03

```text
V10
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme e solene, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Before you move on, make a fist with your right hand and stay until the very end. This message is not for everyone. The universe picked you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o medalhão pendurado na corrente com uma mão e a carta com a outra, e fala para a câmera com pequenos movimentos naturais.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V11 · T11 · frame inicial = a imagem escolhida do K03

```text
V11
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, emocionada e convicta, marcando "exactly 11:11", voz autêntica, como se exigisse ser ouvida, a seguinte frase: "An extremely large amount of money is going to land in your bank account, and your soulmate will contact you tomorrow at exactly 11:11 a.m."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance ergue um pouco o medalhão na corrente enquanto fala.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V12 · T12 · frame inicial = a imagem escolhida do K03

```text
V12
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, calorosa e emocionada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "This person is bringing much more than love: money, opportunity and a major financial change, and they will treat you the way you have always deserved."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o medalhão pendurado na corrente com uma mão e a carta com a outra, e fala para a câmera com pequenos movimentos naturais.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V13 · T13 · frame inicial = a imagem escolhida do K03

```text
V13
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, suave e segura, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Maybe you don't understand how this will happen, but the person coming toward you will open a door you could never open on your own."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o medalhão pendurado na corrente com uma mão e a carta com a outra, e fala para a câmera com pequenos movimentos naturais.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V14 · T14 · frame inicial = a imagem escolhida do K03

```text
V14
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, séria e solene, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "This is your final message from the universe, so take this very seriously."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o medalhão pendurado na corrente com uma mão e a carta com a outra, e fala para a câmera com pequenos movimentos naturais.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V15 · T15 · frame inicial = a imagem escolhida do K03

```text
V15
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme, em ritmo de instrução, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Like this video, that's your first seal. Save this post, that's your second seal."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o medalhão pendurado na corrente com uma mão e a carta com a outra, e fala para a câmera com pequenos movimentos naturais.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V16 · T16 · frame inicial = a imagem escolhida do K03

```text
V16
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme e rápida, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "And send this video to yourself, that's your third seal. Now type 222 in the comments, that's how this gets tied to your name."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance mostra a carta para a lente e fala com firmeza.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V17 · T17 · frame inicial = a imagem escolhida do K03

```text
V17
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, animada, depois baixa e séria, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If you did everything correctly, in 33 minutes you are going to receive your good news. Now pay very close attention to this final and most important detail."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o medalhão pendurado na corrente com uma mão e a carta com a outra, e fala para a câmera com pequenos movimentos naturais.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

### V18 · T18 · frame inicial = a imagem escolhida do K03

```text
V18
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, próxima e urgente, olhando direto na lente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Tap my profile picture and check my stories before they disappear, because the rest of this message is waiting for you there."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance se inclina um pouco para a lente, segurando o medalhão e a carta.

câmera: fixa, no tripé, sem movimento

som ambiente: cozinha silenciosa, rua tranquila lá fora pela janela aberta, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V18.
2. V01 (gancho mudo): usar ~4,5 s, do sal caindo até as pombas pousadas. Tarja fixa em duas linhas no meio do quadro: "TELL NO ONE!" / "The 11:11 portal just opened."
3. V02 (inserto mudo): usar ~1 s do medalhão parado na lente; a primeira palavra do V03 pode entrar por cima.
4. V03 a V18: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / Keep Vocal no áudio. Todos saem do mesmo frame, então a troca de clipe fica no mesmo enquadramento, como no modelo.
5. "11:11" amarelo fixo no canto superior direito do V01 ao V18.
6. Legenda karaokê em caixa alta, branca, palavra atual em amarelo, na altura do prato, do V03 ao V18.
7. Sem Voice Changer: a voz vem do prompt de cada V.
8. Música só a partir do V03, nunca no gancho mudo, entre -19 e -20 dB, fora da biblioteca do TikTok.
9. Rótulo pequeno `AI-generated` num canto do vídeo.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | (sem fala) | (sem fala) |
| T2 | (sem fala) | (sem fala) |
| T3 | What you hear here stays between you and the universe. Tell no one. Only a handful will be shown this before the month is over. | O que você ouvir aqui fica entre você e o universo. Não conte pra ninguém. Só um punhado de pessoas vai ver isto antes de o mês terminar. |
| T4 | I don't know who you are, but stay right here, because if this found you today, it came to you as a last warning. | Eu não sei quem você é, mas fique bem aqui, porque se isto te encontrou hoje, chegou até você como um último aviso. |
| T5 | Money, prosperity and love are rushing toward you right now. Keep it to yourself, but the 11:11 portal just opened in your life. | Dinheiro, prosperidade e amor estão correndo na sua direção agora mesmo. Guarde isso pra você, mas o portal 11:11 acabou de se abrir na sua vida. |
| T6 | In 33 minutes, something extraordinary is going to happen in your life. The worst is over. You were chosen. | Em 33 minutos, algo extraordinário vai acontecer na sua vida. O pior passou. Você foi escolhida. |
| T7 | But if you scroll past this video, you will interrupt this energy, and the blessing will pass right by you. | Mas se você passar este vídeo, vai interromper essa energia, e a bênção vai passar direto por você. |
| T8 | However, if you immediately share this video with yourself, you will seal this blessing. | Porém, se você mandar este vídeo pra você mesma agora, vai selar essa bênção. |
| T9 | I can see money, abundance and someone special stepping into your life. Something rare is moving around you as we speak. | Eu consigo ver dinheiro, abundância e alguém especial entrando na sua vida. Algo raro está se mexendo ao seu redor enquanto a gente fala. |
| T10 | Before you move on, make a fist with your right hand and stay until the very end. This message is not for everyone. The universe picked you. | Antes de seguir, feche a mão direita e fique até o finalzinho. Esta mensagem não é pra todo mundo. O universo escolheu você. |
| T11 | An extremely large amount of money is going to land in your bank account, and your soulmate will contact you tomorrow at exactly 11:11 a.m. | Uma quantia enorme de dinheiro vai cair na sua conta bancária, e a sua alma gêmea vai entrar em contato amanhã exatamente às 11:11 da manhã. |
| T12 | This person is bringing much more than love: money, opportunity and a major financial change, and they will treat you the way you have always deserved. | Essa pessoa está trazendo muito mais que amor: dinheiro, oportunidade e uma grande virada financeira, e vai te tratar do jeito que você sempre mereceu. |
| T13 | Maybe you don't understand how this will happen, but the person coming toward you will open a door you could never open on your own. | Talvez você não entenda como isso vai acontecer, mas a pessoa que está vindo na sua direção vai abrir uma porta que você nunca conseguiria abrir sozinha. |
| T14 | This is your final message from the universe, so take this very seriously. | Esta é a sua última mensagem do universo, então leve isso muito a sério. |
| T15 | Like this video, that's your first seal. Save this post, that's your second seal. | Curta este vídeo, esse é o seu primeiro selo. Salve este post, esse é o seu segundo selo. |
| T16 | And send this video to yourself, that's your third seal. Now type 222 in the comments, that's how this gets tied to your name. | E mande este vídeo pra você mesma, esse é o seu terceiro selo. Agora escreva 222 nos comentários, é assim que isso fica amarrado ao seu nome. |
| T17 | If you did everything correctly, in 33 minutes you are going to receive your good news. Now pay very close attention to this final and most important detail. | Se você fez tudo certo, em 33 minutos você vai receber a sua boa notícia. Agora preste muita atenção a este último e mais importante detalhe. |
| T18 | Tap my profile picture and check my stories before they disappear, because the rest of this message is waiting for you there. | Toque na minha foto de perfil e veja os meus stories antes que sumam, porque o resto desta mensagem está te esperando lá. |

## 6. Roteiro final em inglês

1. (sem fala)
2. (sem fala)
3. What you hear here stays between you and the universe. Tell no one. Only a handful will be shown this before the month is over.
4. I don't know who you are, but stay right here, because if this found you today, it came to you as a last warning.
5. Money, prosperity and love are rushing toward you right now. Keep it to yourself, but the 11:11 portal just opened in your life.
6. In 33 minutes, something extraordinary is going to happen in your life. The worst is over. You were chosen.
7. But if you scroll past this video, you will interrupt this energy, and the blessing will pass right by you.
8. However, if you immediately share this video with yourself, you will seal this blessing.
9. I can see money, abundance and someone special stepping into your life. Something rare is moving around you as we speak.
10. Before you move on, make a fist with your right hand and stay until the very end. This message is not for everyone. The universe picked you.
11. An extremely large amount of money is going to land in your bank account, and your soulmate will contact you tomorrow at exactly 11:11 a.m.
12. This person is bringing much more than love: money, opportunity and a major financial change, and they will treat you the way you have always deserved.
13. Maybe you don't understand how this will happen, but the person coming toward you will open a door you could never open on your own.
14. This is your final message from the universe, so take this very seriously.
15. Like this video, that's your first seal. Save this post, that's your second seal.
16. And send this video to yourself, that's your third seal. Now type 222 in the comments, that's how this gets tied to your name.
17. If you did everything correctly, in 33 minutes you are going to receive your good news. Now pay very close attention to this final and most important detail.
18. Tap my profile picture and check my stories before they disappear, because the rest of this message is waiting for you there.

What you hear here stays between you and the universe. Tell no one. Only a handful will be shown this before the month is over. I don't know who you are, but stay right here, because if this found you today, it came to you as a last warning. Money, prosperity and love are rushing toward you right now. Keep it to yourself, but the 11:11 portal just opened in your life. In 33 minutes, something extraordinary is going to happen in your life. The worst is over. You were chosen. But if you scroll past this video, you will interrupt this energy, and the blessing will pass right by you. However, if you immediately share this video with yourself, you will seal this blessing. I can see money, abundance and someone special stepping into your life. Something rare is moving around you as we speak. Before you move on, make a fist with your right hand and stay until the very end. This message is not for everyone. The universe picked you. An extremely large amount of money is going to land in your bank account, and your soulmate will contact you tomorrow at exactly 11:11 a.m. This person is bringing much more than love: money, opportunity and a major financial change, and they will treat you the way you have always deserved. Maybe you don't understand how this will happen, but the person coming toward you will open a door you could never open on your own. This is your final message from the universe, so take this very seriously. Like this video, that's your first seal. Save this post, that's your second seal. And send this video to yourself, that's your third seal. Now type 222 in the comments, that's how this gets tied to your name. If you did everything correctly, in 33 minutes you are going to receive your good news. Now pay very close attention to this final and most important detail. Tap my profile picture and check my stories before they disappear, because the rest of this message is waiting for you there.
