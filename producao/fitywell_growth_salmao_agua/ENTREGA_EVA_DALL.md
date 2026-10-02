# ENTREGA | Eva Dall | FityWell Growth Salmão na água

Produção `fitywell_growth_salmao_agua` · Ângulo 2 · GROWTH · rodada de VALIDAÇÃO · perfil CLÁSSICO

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

Checklist de envio: 34/34 aprovados (N/A: A2, A7 e A10 fiéis ao modelo e sem produto; C3, C4, C6 e C7 sem segunda pessoa, selfie, cena atuada ou motion control; E2 sem mecanismo, vídeo de growth)

Ficha: 5/5 K, placar 14/14 cada (N/A com motivo: G2 em todos, G8 no K02)

## Anexos

- **Âncora Eva Dall:** `producao/_ancoras/eva_dall_ancora.jpeg` em TODOS os K.
- **Só no K01**, anexar também `input/frames_modelo/K01_modelo.png` (referência de composição, nada além disso).
- K01 a K05 casam com V01 a V05 pelo número.

| Código | Take |
|---|---|
| K01 / V01 | T1, gancho, o filé de salmão entrando no aquário de água quente |
| K02 / V02 | T2, close do aquário, o filé inteiro no fundo antes de se desmanchar |
| K03 / V03 | T3, salmão inteiro entrando na água fria |
| K04 / V04 | T4, brócolis na tigela de vidro, água despejada |
| K05 / V05 | T5, tábua com frango, salmão e truta, CTA |

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho, o filé de salmão entrando no aquário de água quente · anexar ÂNCORA + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing. Use the second attached image only as a composition reference for the glass tank filling the lower third, the hand lowering the salmon fillet into it and the person centered behind it; do not copy its man, his T-shirt, his room or its colors.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen, the same room as the reference image, unchanged: a strongly veined dark green marble counter in front of him, a matching dark green marble wall behind the stove at the left, tall windows to the right and a small American flag on the shelf beside a small potted plant.",
  "prop": "A rectangular clear glass tank with no lid, shaped like a small aquarium about as wide as his shoulders and one hand deep, stands on the dark green veined marble counter, filled almost to the top with clear hot water. Eva Dall's right hand is lowering a thick raw salmon fillet, bright orange with thin white fat lines, held by one corner between the fingertips: the lower half of the fillet is already under the water, the upper half still above the surface, with small ripples spreading around it. The work surface is otherwise empty.",
  "posture": "Eva Dall is standing behind his dark green marble counter, leaning slightly toward the camera, the right hand reaching down into the tank, the left forearm resting on the work surface beside it.",
  "composition": "The glass tank fills the bottom 35 percent of the frame, very close to the lens, its front glass wall about 30 centimeters from the camera, large in frame and closer to the camera than his face; the salmon fillet sits in the center of that lower third and is the brightest thing in the frame. From the chest up, his head and upper chest clear and centered in the upper half of the frame, his face about 70 centimeters from the lens. Nothing else competes with the salmon fillet. The background is reduced by framing, never by blur.",
  "camera": "phone camera on a small tripod at chest height, 26 mm wide lens, straight on, slight downward angle toward the work surface, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "state": "Start frame: the salmon fillet is half submerged and still perfectly whole, ripples on the water. Eva Dall looks into the lens, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no aquarium gravel, no aquarium plants or decorations, no live fish swimming, no lid on the tank, no cooked fish, no broken or flaking fillet yet"
}
```

### K02 · T2, close do aquário, o filé inteiro no fundo antes de se desmanchar · anexar ÂNCORA

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen, the same room as the reference image, unchanged: a strongly veined dark green marble counter in front of him, a matching dark green marble wall behind the stove at the left, tall windows to the right and a small American flag on the shelf beside a small potted plant.",
  "prop": "A rectangular clear glass tank with no lid, shaped like a small aquarium about as wide as his shoulders and one hand deep, stands on the dark green veined marble counter, filled with clear hot water, seen at water level through its front glass wall. One whole thick raw salmon fillet, bright orange with thin white fat lines, rests flat on the glass bottom in the center of the tank, intact. Nothing else is inside the tank.",
  "posture": "Behind the tank only Eva Dall's torso is visible, his white ribbed tank top and thin silver chain, with the fingertips of one hand resting on the top edge of the tank. His face is above the top edge of the frame.",
  "composition": "Close shot at tank height: the tank fills the frame from the bottom edge up to about 75 percent of its height, its front glass wall about 20 centimeters from the lens, very close to the lens, large in frame; the salmon fillet sits in the center of the frame, larger than his hand. Above the waterline only his torso. No face in frame. The background is reduced by framing, never by blur.",
  "camera": "phone camera low, at counter level, at the height of the water, about 20 centimeters from the front glass, 26 mm wide lens, straight on, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "state": "Start frame: the water is calm and clear, the fillet lies whole and still on the bottom, not a single flake floating yet.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no aquarium gravel, no aquarium plants or decorations, no live fish swimming, no lid on the tank, no cooked fish, no face in frame, no broken or flaking fillet yet"
}
```

### K03 · T3, salmão inteiro entrando na água fria · anexar ÂNCORA

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen, the same room as the reference image, unchanged: a strongly veined dark green marble counter in front of him, a matching dark green marble wall behind the stove at the left, tall windows to the right and a small American flag on the shelf beside a small potted plant.",
  "prop": "A rectangular clear glass tank with no lid, shaped like a small aquarium about as wide as his shoulders and one hand deep, stands on the dark green veined marble counter, filled with clear cold water. Eva Dall's right hand holds a whole raw salmon by the back, silver skin with small black spots, head and tail intact, lying on its side and longer than the tank is deep, and lowers it into the water: the belly is just under the surface and the tail hangs over the front edge, with ripples around it. The work surface is otherwise empty.",
  "posture": "Eva Dall is standing behind his dark green marble counter, leaning slightly toward the camera, the right hand holding the fish over the tank, the left forearm resting on the work surface.",
  "composition": "The glass tank with the whole salmon fills the bottom 35 percent of the frame, very close to the lens, its front glass wall about 30 centimeters from the camera, large in frame and closer to the camera than his face; the salmon runs almost the full width of the frame. From the chest up, his head and upper chest clear and centered in the upper half of the frame, his face about 70 centimeters from the lens. Nothing else competes with the salmon. The background is reduced by framing, never by blur.",
  "camera": "phone camera on a small tripod at chest height, 26 mm wide lens, straight on, slight downward angle toward the work surface, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "state": "Start frame: the whole salmon is half in the water, not yet released. Eva Dall looks into the lens, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no aquarium gravel, no aquarium plants or decorations, no live fish swimming, no lid on the tank, no cooked fish"
}
```

### K04 · T4, brócolis na tigela de vidro, água despejada · anexar ÂNCORA

```text
K04
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen, the same room as the reference image, unchanged: a strongly veined dark green marble counter in front of him, a matching dark green marble wall behind the stove at the left, tall windows to the right and a small American flag on the shelf beside a small potted plant.",
  "prop": "A round clear glass mixing bowl full of fresh, clean-looking bright green broccoli florets half covered in water stands on the dark green veined marble counter in the lower foreground. Eva Dall's right hand holds a clear plastic water bottle with no label, tilted over the bowl, pouring a steady stream of water onto the florets. A small plain clear glass vinegar cruet with no label stands on the work surface beside the bowl. Nothing else is on the work surface.",
  "posture": "Eva Dall is standing behind his dark green marble counter, leaning slightly toward the camera, the left hand resting flat on the work surface beside the bowl.",
  "composition": "The glass bowl of broccoli fills the bottom 30 percent of the frame, very close to the lens, about 30 centimeters from the camera, large in frame and closer to the camera than his face. From the chest up, his head and upper chest clear and centered in the upper half of the frame, his face about 70 centimeters from the lens. Nothing else competes with the broccoli bowl. The background is reduced by framing, never by blur.",
  "camera": "phone camera on a small tripod at chest height, 26 mm wide lens, straight on, slight downward angle toward the work surface, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "state": "Start frame: water is streaming from the water bottle onto the broccoli, small splashes on the surface. Eva Dall looks into the lens, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no cooked broccoli, no sauce, no plate"
}
```

### K05 · T5, tábua com frango, salmão e truta, CTA · anexar ÂNCORA

```text
K05
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen, the same room as the reference image, unchanged: a strongly veined dark green marble counter in front of him, a matching dark green marble wall behind the stove at the left, tall windows to the right and a small American flag on the shelf beside a small potted plant.",
  "prop": "Eva Dall holds a thick rectangular wooden cutting board horizontally with both hands, pushed toward the lens, very close to the camera in the lower foreground, large in frame: on the board a whole raw chicken on the left, three thick raw salmon fillet portions standing side by side in the middle, bright orange with white fat lines, and a whole raw trout with silver and pink skin on the right. Nothing else is on the board.",
  "posture": "Eva Dall is standing behind his dark green marble counter, leaning slightly toward the camera, holding the board by its two short ends.",
  "composition": "The cutting board fills the bottom 35 percent of the frame, its front edge about 30 centimeters from the lens, closer to the camera than his face, the salmon portions in the center. From the chest up, his head and upper chest clear and centered in the upper half of the frame, his face about 70 centimeters from the lens. This is the tightest talking shot of the video. The background is reduced by framing, never by blur.",
  "camera": "phone camera on a small tripod at chest height, 26 mm wide lens, straight on, slight downward angle toward the work surface, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "state": "Start frame: Eva Dall smiles wide with excitement, eyes on the lens, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no cooked food, no packaging, no price tags"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem que você deixou no K01

```text
V01
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação direta e curiosa, de quem vai mostrar um teste que pouca gente conhece, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "If you bought salmon at the market, put it in hot water."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Eva Dall termina de baixar o filé de salmão na água do aquário, solta o filé e ele desce devagar até o fundo; ele fala olhando para a câmera. Ele diz a frase em ritmo natural logo no começo e depois fica olhando para o aquário em silêncio.

câmera: fixa, no tripé, na altura do peito

som ambiente: cozinha residencial tranquila, som leve de água mexendo, sem música
```

### V02 · T2 · frame inicial = a imagem que você deixou no K02

```text
V02
o avatar Eva Dall, homem, fora de quadro (só o torso aparece, o rosto fica acima do quadro), fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação séria e firme, com um toque de alerta, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "If it falls apart easily, the meat isn't real."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o filé de salmão parado no fundo do aquário começa a rachar pelas linhas brancas de gordura e se desfaz em dezenas de lascas laranja que se soltam e flutuam pela água; atrás do vidro só aparece o torso, parado, com a mão apoiada na borda do aquário. A voz diz a frase em ritmo natural logo no começo e o resto do clipe é o filé se desmanchando.

câmera: fixa, na altura da água, colada no vidro do aquário

som ambiente: cozinha residencial tranquila, som leve e abafado de água, sem música
```

### V03 · T3 · frame inicial = a imagem que você deixou no K03

```text
V03
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação didática e confiante, explicando com clareza, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Number two, put your fish in cold water. If it sinks, it's fresh. If it floats, it's been sitting on the shelf too long."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Eva Dall solta o salmão inteiro dentro da água; o peixe afunda devagar e fica deitado no fundo do aquário; ele apoia os braços dos dois lados do aquário e fala para a câmera.

câmera: fixa, no tripé, com uma leve descida e aproximação contínua, sem corte

som ambiente: cozinha residencial tranquila, som de água mexendo quando o peixe entra, sem música
```

### V04 · T4 · frame inicial = a imagem que você deixou no K04

```text
V04
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação didática, com um leve tom de nojo no fim da frase, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Number three, put broccoli in water with a splash of vinegar. Any hidden insects and their eggs will come loose and end up in the water."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Eva Dall despeja a água da garrafa sobre os brócolis, larga a garrafa, pega a garrafinha de vinagre e despeja um fio dentro da tigela; na metade do clipe a câmera avança devagar até a tigela encher o quadro e o rosto sair por cima; no close, pequenas larvinhas finas e bege se soltam dos floretes e ficam boiando na água.

câmera: fixa no começo, depois push-in lento e contínuo até a tigela, sem corte

som ambiente: cozinha residencial tranquila, som da água caindo na tigela, sem música
```

### V05 · T5 · frame inicial = a imagem que você deixou no K05

```text
V05
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação animada e convidativa, sorrindo, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "I have tips like this for almost every food you buy. Save this and comment with other foods for more. Follow me so you don't miss out."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Eva Dall segura a tábua com as duas mãos e fala para a câmera, sorrindo animado; nos últimos segundos a câmera avança devagar até a tábua, o rosto sai por cima e o quadro fecha nas postas de salmão.

câmera: fixa, depois push-in lento e contínuo até a tábua nos últimos segundos, sem corte

som ambiente: cozinha residencial tranquila, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01, V02, V03, V04, V05.
2. Cortar cada clipe no tempo da cena do modelo: V01 0,0 a 3,0 s; V02 3,0 a 7,5 s; V03 7,5 a 15,1 s; V04 15,1 a 22,8 s; V05 22,8 a 30,0 s.
3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. V01 e V02 são cenas curtas: a fala vem no começo; cortar V01 logo depois de "hot water" e V02 quando o filé estiver todo em lascas, no tempo da cena.
5. Legenda de 2 a 3 palavras por vez, caixa alta, fonte bold branca com contorno preto e a palavra falada em amarelo, no meio do quadro, do começo ao fim, igual ao modelo.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Música só do V03 em diante, nunca no gancho (V01 e V02), entre -19 e -20 dB, fora da biblioteca do TikTok.
8. Rótulo pequeno `AI-generated` num canto do vídeo.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | If you bought salmon at the market, put it in hot water. | Se você comprou salmão no mercado, coloque ele na água quente. |
| T2 | If it falls apart easily, the meat isn't real. | Se ele se desmanchar fácil, a carne não é de verdade. |
| T3 | Number two, put your fish in cold water. If it sinks, it's fresh. If it floats, it's been sitting on the shelf too long. | Número dois, coloque o seu peixe na água fria. Se ele afundar, está fresco. Se ele boiar, ficou tempo demais na prateleira. |
| T4 | Number three, put broccoli in water with a splash of vinegar. Any hidden insects and their eggs will come loose and end up in the water. | Número três, coloque o brócolis na água com um pouco de vinagre. Qualquer inseto escondido e os ovos dele vão se soltar e ficar na água. |
| T5 | I have tips like this for almost every food you buy. Save this and comment with other foods for more. Follow me so you don't miss out. | Eu tenho dicas assim para quase todo alimento que você compra. Salve isso e comente outros alimentos para ver mais. Me siga para não perder nada. |

## 6. Roteiro final em inglês

1. If you bought salmon at the market, put it in hot water.
2. If it falls apart easily, the meat isn't real.
3. Number two, put your fish in cold water. If it sinks, it's fresh. If it floats, it's been sitting on the shelf too long.
4. Number three, put broccoli in water with a splash of vinegar. Any hidden insects and their eggs will come loose and end up in the water.
5. I have tips like this for almost every food you buy. Save this and comment with other foods for more. Follow me so you don't miss out.

If you bought salmon at the market, put it in hot water. If it falls apart easily, the meat isn't real. Number two, put your fish in cold water. If it sinks, it's fresh. If it floats, it's been sitting on the shelf too long. Number three, put broccoli in water with a splash of vinegar. Any hidden insects and their eggs will come loose and end up in the water. I have tips like this for almost every food you buy. Save this and comment with other foods for more. Follow me so you don't miss out.
