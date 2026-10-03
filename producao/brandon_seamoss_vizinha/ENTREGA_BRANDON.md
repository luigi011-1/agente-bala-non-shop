# ENTREGA | holistic.brandon | Natural Rems Sea Moss Venda, a vizinha de 57

Produção `brandon_seamoss_vizinha` · Ângulo 1 (Natural Rems Sea Moss) · VENDA · vídeo modelo de avatar IA · movie style família B · rodada de VALIDAÇÃO · perfil CLÁSSICO

## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v17)

Colar inteiro na memória do agente antes do primeiro REF-P.

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

Roster Auraly: Walt Hensley, Darlene Pruitt, Lorraine Vance e Morgan Vance (desde 2026-09-30). A referencia de cada um e a anchor
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

Checklist de envio: 35/35 aprovados (N/A: A1, A10, A12, A13 e A14 fiéis ao modelo na rodada de validação, sem arquivo de ganchos; C4 sem selfie; C7 sem motion control)

Ficha: 35/35 K conferidos contra o frame do modelo, placar F1 a F6 + G1 a G8 completo em cada um, com evidência literal (N/A só em G2 no box, sem céu nem janela em quadro, e G8 nos takes sem fala) (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Mapa de anexos

- **REF-P1 a REF-P3:** gerar do zero, sem anexo, e aprovar os três antes do primeiro K.
- **K01 a K15 (esquete):** os REF-P aprovados de quem está em quadro, na ordem abaixo, e por último o frame do modelo (só composição).
- **K16 a K35 (Brandon):** âncora `producao/_ancoras/holistic_brandon_ancora.jpg` + frame do modelo (só composição); do K31 ao K35 também a foto do produto `producao/_ancoras/natural_rems_seamoss_produto.jpg`.
- K01 a K35 casam com V01 a V35 pelo número. V01, V02 e V15 são sem fala.

| Código | Take | Anexar, nesta ordem |
|---|---|---|
| REF-P1 | elenco, VIZINHA | nenhuma |
| REF-P2 | elenco, MARIDO | nenhuma |
| REF-P3 | elenco, ESPOSA | nenhuma |
| K01 / V01 | T1, plano aberto mudo, vizinha podando e o casal correndo | REF-P1 (VIZINHA) + REF-P2 (MARIDO) + REF-P3 (ESPOSA) + FRAME DO MODELO `input/frames_modelo/K01_modelo.png` (por último, só composição) |
| K02 / V02 | T2, close da esposa em choque | REF-P3 (ESPOSA) + FRAME DO MODELO `input/frames_modelo/K02_modelo.png` (por último, só composição) |
| K03 / V03 | T3, o marido chega na vizinha | REF-P1 (VIZINHA) + REF-P2 (MARIDO) + REF-P3 (ESPOSA) + FRAME DO MODELO `input/frames_modelo/K03_modelo.png` (por último, só composição) |
| K04 / V04 | T4, a vizinha se vira | REF-P1 (VIZINHA) + REF-P2 (MARIDO) + FRAME DO MODELO `input/frames_modelo/K04_modelo.png` (por último, só composição) |
| K05 / V05 | T5, o marido se apresenta, a esposa ofegante atrás | REF-P2 (MARIDO) + REF-P3 (ESPOSA) + REF-P1 (VIZINHA) + FRAME DO MODELO `input/frames_modelo/K05_modelo.png` (por último, só composição) |
| K06 / V06 | T6, close do marido, you look so fine | REF-P2 (MARIDO) + FRAME DO MODELO `input/frames_modelo/K06_modelo.png` (por último, só composição) |
| K07 / V07 | T7, a vizinha aponta a esposa correndo | REF-P1 (VIZINHA) + REF-P3 (ESPOSA) + REF-P2 (MARIDO) + FRAME DO MODELO `input/frames_modelo/K07_modelo.png` (por último, só composição) |
| K08 / V08 | T8, o marido de perfil, if my wife looked like you | REF-P2 (MARIDO) + REF-P1 (VIZINHA) + REF-P3 (ESPOSA) + FRAME DO MODELO `input/frames_modelo/K08_modelo.png` (por último, só composição) |
| K09 / V09 | T9, close da vizinha, start doing what I do | REF-P1 (VIZINHA) + REF-P2 (MARIDO) + FRAME DO MODELO `input/frames_modelo/K09_modelo.png` (por último, só composição) |
| K10 / V10 | T10, close do marido, hitting the gym | REF-P2 (MARIDO) + FRAME DO MODELO `input/frames_modelo/K10_modelo.png` (por último, só composição) |
| K11 / V11 | T11, a vizinha volta a podar, I am fifty-seven | REF-P1 (VIZINHA) + REF-P2 (MARIDO) + FRAME DO MODELO `input/frames_modelo/K11_modelo.png` (por último, só composição) |
| K12 / V12 | T12, close do marido em choque, what | REF-P2 (MARIDO) + FRAME DO MODELO `input/frames_modelo/K12_modelo.png` (por último, só composição) |
| K13 / V13 | T13, o marido, what's your secret | REF-P2 (MARIDO) + REF-P1 (VIZINHA) + FRAME DO MODELO `input/frames_modelo/K13_modelo.png` (por último, só composição) |
| K14 / V14 | T14, a indicação, this holistic coach | REF-P1 (VIZINHA) + REF-P2 (MARIDO) + FRAME DO MODELO `input/frames_modelo/K14_modelo.png` (por último, só composição) |
| K15 / V15 | T15, close do marido ouvindo, mudo | REF-P2 (MARIDO) + FRAME DO MODELO `input/frames_modelo/K15_modelo.png` (por último, só composição) |
| K16 / V16 | T16, credencial de coach, mãos na mesa | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K16_modelo.png` (só composição) |
| K17 / V17 | T17, receita 1, copo e meio limão | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K17_modelo.png` (só composição) |
| K18 / V18 | T18, receita 1, benefício | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K18_modelo.png` (só composição) |
| K19 / V19 | T19, ponte para a pele | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K19_modelo.png` (só composição) |
| K20 / V20 | T20, receita 2, a máscara na tigelinha | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K20_modelo.png` (só composição) |
| K21 / V21 | T21, receita 2, benefício e virada | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K21_modelo.png` (só composição) |
| K22 / V22 | T22, o álibi do estresse | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K22_modelo.png` (só composição) |
| K23 / V23 | T23, receita 3, o pote de sea moss | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K23_modelo.png` (só composição) |
| K24 / V24 | T24, receita 3, autoridade de coach | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K24_modelo.png` (só composição) |
| K25 / V25 | T25, mecanismo, o estresse queima os minerais | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K25_modelo.png` (só composição) |
| K26 / V26 | T26, mecanismo, o gel devolve os minerais | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K26_modelo.png` (só composição) |
| K27 / V27 | T27, prova social das clientes | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K27_modelo.png` (só composição) |
| K28 / V28 | T28, a conspiração da prateleira | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K28_modelo.png` (só composição) |
| K29 / V29 | T29, ninguém vai fazer por você | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K29_modelo.png` (só composição) |
| K30 / V30 | T30, o obstáculo, açúcar e enchimento | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K30_modelo.png` (só composição) |
| K31 / V31 | T31, o produto, o frasco sobe no nome | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K31_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |
| K32 / V32 | T32, diferencial 16 em 1 | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K32_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |
| K33 / V33 | T33, prova social da coach | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K33_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |
| K34 / V34 | T34, comment yes + follow | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K34_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |
| K35 / V35 | T35, CTA da marca, Amazon e legenda | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K35_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |

## 2. PROMPTS DE IMAGEM

### Character sheets (gerar e aprovar antes dos K)

### REF-P1 · VIZINHA · sem anexo

```text
REF-P1
{
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "sheet_layout": "CHARACTER SHEET of ONE person on a plain light grey wall background: three full-body views side by side (front, three-quarter and profile) in the lower two thirds, and a large front close-up of the face across the top third. The same person, the same clothes and the same hair in every view.",
  "identity_main": "The neighbor: a fictional white American woman who looks about thirty, slim and athletic with a toned flat stomach, long straight light blonde hair past her shoulders, fair skin, light blue eyes, thin clear round eyeglasses with a pale gold frame, a plain black sports bra top with nothing printed on it, high-waisted navy blue bike shorts and black gardening gloves.",
  "expression": "Neutral relaxed expression, mouth closed, looking straight ahead.",
  "lighting": "Flat neutral daylight, soft and even on the face and body, no harsh shadows, no warm orange cast and no yellow tint.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing. No blur, no bokeh.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden hour light, no AI polish, no beauty smoothing, no cinematic lighting, no labels, no numbers, no arrows, no second person"
}
```

### REF-P2 · MARIDO · sem anexo

```text
REF-P2
{
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "sheet_layout": "CHARACTER SHEET of ONE person on a plain light grey wall background: three full-body views side by side (front, three-quarter and profile) in the lower two thirds, and a large front close-up of the face across the top third. The same person, the same clothes and the same hair in every view.",
  "identity_main": "The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes, only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt.",
  "expression": "Neutral relaxed expression, mouth closed, looking straight ahead.",
  "lighting": "Flat neutral daylight, soft and even on the face and body, no harsh shadows, no warm orange cast and no yellow tint.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing. No blur, no bokeh.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden hour light, no AI polish, no beauty smoothing, no cinematic lighting, no labels, no numbers, no arrows, no second person"
}
```

### REF-P3 · ESPOSA · sem anexo

```text
REF-P3
{
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "sheet_layout": "CHARACTER SHEET of ONE person on a plain light grey wall background: three full-body views side by side (front, three-quarter and profile) in the lower two thirds, and a large front close-up of the face across the top third. The same person, the same clothes and the same hair in every view.",
  "identity_main": "The wife: a fictional white American woman around thirty-five, plus-size with a full round body, brown hair pulled back in a messy ponytail, fair skin flushed pink from running, blue-grey eyes, a heather grey sports bra, grey leggings, light grey running shoes and a black smartwatch.",
  "expression": "Neutral relaxed expression, mouth closed, looking straight ahead.",
  "lighting": "Flat neutral daylight, soft and even on the face and body, no harsh shadows, no warm orange cast and no yellow tint.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing. No blur, no bokeh.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden hour light, no AI polish, no beauty smoothing, no cinematic lighting, no labels, no numbers, no arrows, no second person"
}
```

### Keyframes (um bloco por K)

### K01 · T1, plano aberto mudo, vizinha podando e o casal correndo · anexar REF-P1 (VIZINHA) + REF-P2 (MARIDO) + REF-P3 (ESPOSA) + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the neighbor is the person in the first character sheet; the husband is the person in the second character sheet; the wife is the person in the third character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The neighbor: a fictional white American woman who looks about thirty, slim and athletic with a toned flat stomach, long straight light blonde hair past her shoulders, fair skin, light blue eyes, thin clear round eyeglasses with a pale gold frame. The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes. The wife: a fictional white American woman around thirty-five, plus-size with a full round body, brown hair pulled back in a messy ponytail, fair skin flushed pink from running, blue-grey eyes.",
  "wardrobe": "the neighbor wears a plain black sports bra top with nothing printed on it, high-waisted navy blue bike shorts and black gardening gloves; the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt; the wife wears a heather grey sports bra, grey leggings, light grey running shoes and a black smartwatch.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "Long-handled wooden hedge shears in the neighbor's gloved hands, the blades open against the hedge.",
  "posture": "The neighbor stands in profile in the left foreground, bent forward at the hips, trimming the hedge; far behind her on the wet sidewalk, the husband and the wife jog side by side toward the camera.",
  "composition": "The neighbor is about 100 centimeters from the lens and fills the left 40 percent of the frame from head to knees; the husband and the wife are about six meters away in the center and right, each about 25 percent of the frame tall. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: mid-stride jogging, the shears half closed, nobody has spoken yet.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K02 · T2, close da esposa em choque · anexar REF-P3 (ESPOSA) + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the wife is the person in the first character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The wife: a fictional white American woman around thirty-five, plus-size with a full round body, brown hair pulled back in a messy ponytail, fair skin flushed pink from running, blue-grey eyes.",
  "wardrobe": "the wife wears a heather grey sports bra, grey leggings, light grey running shoes and a black smartwatch.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "No object in her hands; both palms pressed flat against the sides of her head.",
  "posture": "The wife stares past the camera in shock, both palms pressed flat against the sides of her head, eyes wide open, mouth stretched wide open in a silent gasp.",
  "composition": "The wife's face is about 25 centimeters from the lens and fills the upper 70 percent of the frame, her shoulders and grey sports bra at the bottom edge. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held at her eye level, wide 0.5x lens, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: frozen mid-gasp, mouth wide open, eyebrows high.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K03 · T3, o marido chega na vizinha · anexar REF-P1 (VIZINHA) + REF-P2 (MARIDO) + REF-P3 (ESPOSA) + FRAME DO MODELO

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the neighbor is the person in the first character sheet; the husband is the person in the second character sheet; the wife is the person in the third character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The neighbor: a fictional white American woman who looks about thirty, slim and athletic with a toned flat stomach, long straight light blonde hair past her shoulders, fair skin, light blue eyes, thin clear round eyeglasses with a pale gold frame. The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes. The wife: a fictional white American woman around thirty-five, plus-size with a full round body, brown hair pulled back in a messy ponytail, fair skin flushed pink from running, blue-grey eyes.",
  "wardrobe": "the neighbor wears a plain black sports bra top with nothing printed on it, high-waisted navy blue bike shorts and black gardening gloves; the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt; the wife wears a heather grey sports bra, grey leggings, light grey running shoes and a black smartwatch.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "The hedge shears hang from the neighbor's gloved hand.",
  "posture": "Seen over the neighbor's shoulder, the husband walks up toward her smiling, one hand raised in a small wave; the wife is still jogging, small, on the sidewalk behind him.",
  "composition": "The neighbor's bare shoulder and blonde hair are about 20 centimeters from the lens, cut by the left edge and filling the left 25 percent of the frame; the husband is about two meters away in the center, from the thighs up, filling 50 percent of the frame height. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: the husband mid-step, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K04 · T4, a vizinha se vira · anexar REF-P1 (VIZINHA) + REF-P2 (MARIDO) + FRAME DO MODELO

```text
K04
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the neighbor is the person in the first character sheet; the husband is the person in the second character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The neighbor: a fictional white American woman who looks about thirty, slim and athletic with a toned flat stomach, long straight light blonde hair past her shoulders, fair skin, light blue eyes, thin clear round eyeglasses with a pale gold frame. The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes.",
  "wardrobe": "the neighbor wears a plain black sports bra top with nothing printed on it, high-waisted navy blue bike shorts and black gardening gloves; the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "The neighbor holds the wooden hedge shears closed in front of her waist.",
  "posture": "The neighbor has just turned toward the husband, polite and cool, holding the shears.",
  "composition": "The neighbor is about 70 centimeters from the lens, from the waist up, filling 60 percent of the frame; the husband's bare shoulder is about 20 centimeters from the lens, cut by the right edge. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: the neighbor is caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K05 · T5, o marido se apresenta, a esposa ofegante atrás · anexar REF-P2 (MARIDO) + REF-P3 (ESPOSA) + REF-P1 (VIZINHA) + FRAME DO MODELO

```text
K05
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the husband is the person in the first character sheet; the wife is the person in the second character sheet; the neighbor is the person in the third character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes. The wife: a fictional white American woman around thirty-five, plus-size with a full round body, brown hair pulled back in a messy ponytail, fair skin flushed pink from running, blue-grey eyes. The neighbor: a fictional white American woman who looks about thirty, slim and athletic with a toned flat stomach, long straight light blonde hair past her shoulders, fair skin, light blue eyes, thin clear round eyeglasses with a pale gold frame.",
  "wardrobe": "the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt; the wife wears a heather grey sports bra, grey leggings, light grey running shoes and a black smartwatch; the neighbor wears a plain black sports bra top with nothing printed on it, high-waisted navy blue bike shorts and black gardening gloves.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "No props in the husband's hands.",
  "posture": "The husband stands facing the neighbor, gesturing with an open hand toward the house next door; behind him on the sidewalk the wife is bent over with her hands on her knees, catching her breath.",
  "composition": "The husband is about 120 centimeters from the lens, from the hips up, filling 55 percent of the frame at the right of center; the wife is about four meters behind him, small, about 20 percent of the frame tall; the neighbor's bare shoulder and blonde hair are about 20 centimeters from the lens, cut by the left edge. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: the husband is caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K06 · T6, close do marido, you look so fine · anexar REF-P2 (MARIDO) + FRAME DO MODELO

```text
K06
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the husband is the person in the first character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes.",
  "wardrobe": "the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "A leafy green hedge branch pokes into the lower left corner of the frame.",
  "posture": "The husband looks just past the lens at the neighbor with a flirty half smile.",
  "composition": "The husband's face and chest are about 40 centimeters from the lens and fill 70 percent of the frame; the hedge branch is about 10 centimeters from the lens in the lower left corner. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: the husband is caught mid-sentence, lips naturally parted, animated expression, flirty.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K07 · T7, a vizinha aponta a esposa correndo · anexar REF-P1 (VIZINHA) + REF-P3 (ESPOSA) + REF-P2 (MARIDO) + FRAME DO MODELO

```text
K07
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the neighbor is the person in the first character sheet; the wife is the person in the second character sheet; the husband is the person in the third character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The neighbor: a fictional white American woman who looks about thirty, slim and athletic with a toned flat stomach, long straight light blonde hair past her shoulders, fair skin, light blue eyes, thin clear round eyeglasses with a pale gold frame. The wife: a fictional white American woman around thirty-five, plus-size with a full round body, brown hair pulled back in a messy ponytail, fair skin flushed pink from running, blue-grey eyes. The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes.",
  "wardrobe": "the neighbor wears a plain black sports bra top with nothing printed on it, high-waisted navy blue bike shorts and black gardening gloves; the wife wears a heather grey sports bra, grey leggings, light grey running shoes and a black smartwatch; the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "The hedge shears hang from the neighbor's gloved hand.",
  "posture": "The neighbor, in three-quarter view, glances past the husband toward the wife, who is jogging away down the sidewalk with her back to the camera.",
  "composition": "The neighbor is about 80 centimeters from the lens, from the waist up, filling the left 55 percent of the frame; the husband's bare arm is about 20 centimeters from the lens, cut by the right edge; the wife is about eight meters away in the center, small, about 15 percent of the frame tall. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: the neighbor is caught mid-sentence, lips naturally parted, animated expression, eyebrows slightly raised.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K08 · T8, o marido de perfil, if my wife looked like you · anexar REF-P2 (MARIDO) + REF-P1 (VIZINHA) + REF-P3 (ESPOSA) + FRAME DO MODELO

```text
K08
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the husband is the person in the first character sheet; the neighbor is the person in the second character sheet; the wife is the person in the third character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes. The neighbor: a fictional white American woman who looks about thirty, slim and athletic with a toned flat stomach, long straight light blonde hair past her shoulders, fair skin, light blue eyes, thin clear round eyeglasses with a pale gold frame. The wife: a fictional white American woman around thirty-five, plus-size with a full round body, brown hair pulled back in a messy ponytail, fair skin flushed pink from running, blue-grey eyes.",
  "wardrobe": "the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt; the neighbor wears a plain black sports bra top with nothing printed on it, high-waisted navy blue bike shorts and black gardening gloves; the wife wears a heather grey sports bra, grey leggings, light grey running shoes and a black smartwatch.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "A hedge branch crosses the lower foreground.",
  "posture": "The husband stands in profile looking at the neighbor, one hand open toward her; far behind, the wife keeps jogging away.",
  "composition": "The husband is about 100 centimeters from the lens, from the hips up, filling the right 50 percent of the frame; the neighbor is cut by the left edge; the wife is about fifteen meters away, tiny, about 8 percent of the frame tall; the hedge branch is about 15 centimeters from the lens. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: the husband is caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K09 · T9, close da vizinha, start doing what I do · anexar REF-P1 (VIZINHA) + REF-P2 (MARIDO) + FRAME DO MODELO

```text
K09
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the neighbor is the person in the first character sheet; the husband is the person in the second character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The neighbor: a fictional white American woman who looks about thirty, slim and athletic with a toned flat stomach, long straight light blonde hair past her shoulders, fair skin, light blue eyes, thin clear round eyeglasses with a pale gold frame. The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes.",
  "wardrobe": "the neighbor wears a plain black sports bra top with nothing printed on it, high-waisted navy blue bike shorts and black gardening gloves; the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "The wooden handle of the hedge shears in her gloved hand at the bottom of the frame.",
  "posture": "The neighbor looks at the husband, dry and unimpressed.",
  "composition": "The neighbor is about 45 centimeters from the lens, from the chest up, filling 65 percent of the frame; the husband's shoulder is about 20 centimeters from the lens, cut by the right edge. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: the neighbor is caught mid-sentence, lips naturally parted, animated expression, no smile.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K10 · T10, close do marido, hitting the gym · anexar REF-P2 (MARIDO) + FRAME DO MODELO

```text
K10
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the husband is the person in the first character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes.",
  "wardrobe": "the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "Hedge leaves in the lower left corner of the frame.",
  "posture": "The husband tilts his head, curious and still flirting.",
  "composition": "The husband's face and chest are about 40 centimeters from the lens and fill 70 percent of the frame; the hedge leaves are about 10 centimeters from the lens in the lower left corner. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held just below his chin height, tilted slightly up, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: the husband is caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K11 · T11, a vizinha volta a podar, I am fifty-seven · anexar REF-P1 (VIZINHA) + REF-P2 (MARIDO) + FRAME DO MODELO

```text
K11
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the neighbor is the person in the first character sheet; the husband is the person in the second character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The neighbor: a fictional white American woman who looks about thirty, slim and athletic with a toned flat stomach, long straight light blonde hair past her shoulders, fair skin, light blue eyes, thin clear round eyeglasses with a pale gold frame. The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes.",
  "wardrobe": "the neighbor wears a plain black sports bra top with nothing printed on it, high-waisted navy blue bike shorts and black gardening gloves; the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "The wooden hedge shears open in both gloved hands, against the hedge.",
  "posture": "The neighbor is back at the hedge, shears open in both hands, glancing back over her shoulder.",
  "composition": "The neighbor is about 90 centimeters from the lens, from the knees up, filling 55 percent of the frame; the husband's bare arm is about 20 centimeters from the lens, cut by the right edge. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: the neighbor is caught mid-sentence, lips naturally parted, animated expression, matter-of-fact.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K12 · T12, close do marido em choque, what · anexar REF-P2 (MARIDO) + FRAME DO MODELO

```text
K12
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the husband is the person in the first character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes.",
  "wardrobe": "the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "No props.",
  "posture": "The husband stares straight ahead in total shock, eyebrows raised high, mouth open.",
  "composition": "The husband's face is about 35 centimeters from the lens and fills 60 percent of the frame. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held at his eye level, standard 1x lens, straight-on, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: the husband is caught mid-sentence, lips naturally parted, animated expression, frozen in shock.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K13 · T13, o marido, what's your secret · anexar REF-P2 (MARIDO) + REF-P1 (VIZINHA) + FRAME DO MODELO

```text
K13
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the husband is the person in the first character sheet; the neighbor is the person in the second character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes. The neighbor: a fictional white American woman who looks about thirty, slim and athletic with a toned flat stomach, long straight light blonde hair past her shoulders, fair skin, light blue eyes, thin clear round eyeglasses with a pale gold frame.",
  "wardrobe": "the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt; the neighbor wears a plain black sports bra top with nothing printed on it, high-waisted navy blue bike shorts and black gardening gloves.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "Hedge branches in the lower foreground.",
  "posture": "The husband faces the neighbor, hands open in disbelief.",
  "composition": "The husband is about 100 centimeters from the lens, from the hips up, filling 60 percent of the frame; the neighbor's shoulder is cut by the left edge; the hedge branches are about 15 centimeters from the lens at the bottom. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: the husband is caught mid-sentence, lips naturally parted, animated expression, amazed.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K14 · T14, a indicação, this holistic coach · anexar REF-P1 (VIZINHA) + REF-P2 (MARIDO) + FRAME DO MODELO

```text
K14
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the neighbor is the person in the first character sheet; the husband is the person in the second character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The neighbor: a fictional white American woman who looks about thirty, slim and athletic with a toned flat stomach, long straight light blonde hair past her shoulders, fair skin, light blue eyes, thin clear round eyeglasses with a pale gold frame. The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes.",
  "wardrobe": "the neighbor wears a plain black sports bra top with nothing printed on it, high-waisted navy blue bike shorts and black gardening gloves; the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "A bunch of freshly cut hedge branches in the neighbor's right gloved hand and an open black garbage bag held in her left gloved hand.",
  "posture": "The neighbor faces the husband, holding up the cut branches and the garbage bag.",
  "composition": "The neighbor is about 80 centimeters from the lens, from the waist up, filling 60 percent of the frame; the husband's hand is about 20 centimeters from the lens at the lower right edge. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: the neighbor is caught mid-sentence, lips naturally parted, animated expression, casual.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K15 · T15, close do marido ouvindo, mudo · anexar REF-P2 (MARIDO) + FRAME DO MODELO

```text
K15
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated scene with fictional characters, no real person is depicted.",
  "reference_use": "Use the attached character sheets ONLY for faces, hair, bodies and clothes: the husband is the person in the first character sheet. The last attached image is a composition reference only: copy its camera position, framing and where each person stands, never its faces, bodies, clothes, houses or caption text.",
  "identity_main": "The husband: a fictional white American man around thirty-two, very muscular and lean, shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept up, light stubble, grey-blue eyes.",
  "wardrobe": "the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch on his left wrist and a thin gold wedding ring, no shirt.",
  "scene": "A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, never blown white.",
  "prop": "No props.",
  "posture": "The husband listens in silence, mouth closed, slowly taking it in.",
  "composition": "The husband's face and chest are about 35 centimeters from the lens and fill 65 percent of the frame. Every face in sharp focus. The background is reduced by framing, never by blur.",
  "camera": "phone held at his eye level, standard 1x lens, straight-on, light handheld",
  "lighting": "Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky clearly visible with soft grey texture, no warm orange cast and no yellow tint.",
  "state": "Start frame: mouth closed, a slow blink.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
}
```

### K16 · T16, credencial de coach, mãos na mesa · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K16
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "Nothing in her hands; the black table is empty.",
  "posture": "Brandon stands behind the black table, both hands resting flat on it, shoulders square to the lens.",
  "composition": "Straight-on medium shot from the waist up: the phone lens is about 60 centimeters from her, she fills 60 percent of the frame, her hands resting flat on the black table at the bottom edge. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, calm and sure.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K17 · T17, receita 1, copo e meio limão · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K17
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A clear drinking glass of warm water in her left hand and half a lemon with its cut side facing the lens in her right hand, both held at chest height.",
  "posture": "Brandon holds the glass and the lemon half out toward the lens, the lemon tilted above the glass.",
  "composition": "Straight-on medium shot: the phone lens is about 25 centimeters from the glass and the lemon, which fills the lower 30 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The black table edge is at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, about to squeeze the lemon into the glass.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K18 · T18, receita 1, benefício · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K18
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A clear drinking glass of warm water in her left hand and half a lemon with its cut side facing the lens in her right hand, both held at chest height.",
  "posture": "Brandon holds the glass and the lemon half side by side at chest height.",
  "composition": "Straight-on medium shot: the phone lens is about 25 centimeters from the glass and the lemon, which fills the lower 30 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The black table edge is at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, lively and certain.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K19 · T19, ponte para a pele · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K19
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A clear drinking glass of warm water in her left hand and half a lemon with its cut side facing the lens in her right hand, lowered a little.",
  "posture": "Brandon holds the glass and the lemon half a little lower, about to put them down.",
  "composition": "Straight-on medium shot from slightly above: the phone lens is about 30 centimeters from the glass and the lemon, which fills the lower 25 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The black table edge is at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, raising one eyebrow, turning a point.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K20 · T20, receita 2, a máscara na tigelinha · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K20
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A small clear glass bowl with a pale creamy yellow mixture of apple cider vinegar and coconut oil, smooth and slightly glossy, held in her left hand at chest height; two fingers of her right hand touch the mixture.",
  "posture": "Brandon holds the bowl toward the lens and dips two fingers into the mixture.",
  "composition": "Straight-on medium shot: the phone lens is about 25 centimeters from the bowl, which fills the lower 25 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The black table edge is at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, explaining, focused.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K21 · T21, receita 2, benefício e virada · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K21
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A small clear glass bowl with a pale creamy yellow mixture of apple cider vinegar and coconut oil, smooth and slightly glossy, held in both hands at chest height.",
  "posture": "Brandon holds the bowl in both hands toward the lens.",
  "composition": "Straight-on medium shot: the phone lens is about 25 centimeters from the bowl, which fills the lower 25 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The black table edge is at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, confident, a little conspiratorial at the end.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K22 · T22, o álibi do estresse · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K22
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A small clear glass bowl with a pale creamy yellow mixture of apple cider vinegar and coconut oil, smooth and slightly glossy, held in both hands at chest height.",
  "posture": "Brandon holds the bowl in both hands, leaning slightly toward the lens.",
  "composition": "Straight-on medium shot, a little tighter: the phone lens is about 30 centimeters from the bowl, which fills the lower 22 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The black table edge is at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, serious and reassuring.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K23 · T23, receita 3, o pote de sea moss · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K23
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A wide clear glass jar filled with dried raw Irish sea moss: tangled pale golden and beige seaweed strands with a light frosty sea-salt coating, held in both hands at chest height.",
  "posture": "Brandon holds the jar of dried sea moss in both hands, pushed toward the lens.",
  "composition": "Straight-on medium shot: the phone lens is about 25 centimeters from the jar, which fills the lower 35 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The black table edge is at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, emphatic, this is the important one.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K24 · T24, receita 3, autoridade de coach · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K24
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A wide clear glass jar filled with dried raw Irish sea moss: tangled pale golden and beige seaweed strands with a light frosty sea-salt coating, held in both hands at chest height.",
  "posture": "Brandon holds the jar of dried sea moss in both hands at chest height.",
  "composition": "Straight-on medium shot: the phone lens is about 25 centimeters from the jar, which fills the lower 35 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The black table edge is at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warm and proud.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K25 · T25, mecanismo, o estresse queima os minerais · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K25
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A wide clear glass jar filled with dried raw Irish sea moss: tangled pale golden and beige seaweed strands with a light frosty sea-salt coating, held in her left hand at chest height; her right hand open beside it.",
  "posture": "Brandon holds the jar in her left hand and explains with her right hand open.",
  "composition": "Straight-on medium shot from slightly above: the phone lens is about 30 centimeters from the jar, which fills the lower 30 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The black table edge is at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, serious, explaining.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K26 · T26, mecanismo, o gel devolve os minerais · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K26
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A small clear glass bowl holding a spoonful of smooth pale beige sea moss gel, glossy and jelly-like, held in her left hand at chest height; her right index finger points at the gel.",
  "posture": "Brandon holds the small bowl toward the lens and points at the gel with her right index finger.",
  "composition": "Straight-on medium shot: the phone lens is about 25 centimeters from the bowl, which fills the lower 25 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The black table edge is at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, calm and reassuring.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K27 · T27, prova social das clientes · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K27
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A small clear glass bowl holding a spoonful of smooth pale beige sea moss gel, glossy and jelly-like, held in both hands at chest height.",
  "posture": "Brandon holds the small bowl of gel in both hands.",
  "composition": "Straight-on medium shot: the phone lens is about 25 centimeters from the bowl, which fills the lower 25 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The black table edge is at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warm, telling a story.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K28 · T28, a conspiração da prateleira · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K28
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "Nothing in her hands; the black table is empty.",
  "posture": "Brandon leans on the black table with both hands, closer to the lens.",
  "composition": "Straight-on close medium shot: the phone lens is about 45 centimeters from her face, her head and shoulders fill the upper 60 percent of the frame, her hands on the black table edge at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, indignant, lowering her voice.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K29 · T29, ninguém vai fazer por você · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K29
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "Nothing in her hands; the black table is empty.",
  "posture": "Brandon leans on the black table with both hands, closer to the lens, one hand lifting slightly.",
  "composition": "Straight-on close medium shot: the phone lens is about 45 centimeters from her face, her head and shoulders fill the upper 60 percent of the frame, her hands on the black table edge at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, firm.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K30 · T30, o obstáculo, açúcar e enchimento · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K30
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A small clear glass bowl heaped with white granulated sugar in her left hand and a small clear glass bowl heaped with a fine white powder in her right hand, both held out at chest height.",
  "posture": "Brandon holds one small bowl in each hand, out toward the lens.",
  "composition": "Straight-on medium shot: the phone lens is about 25 centimeters from the two bowls, which fills the lower 35 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The black table edge is at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warning, a little disgusted.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bowls or jar"
}
```

### K31 · T31, o produto, o frasco sobe no nome · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K31
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "In her right hand, held low just above the black table, the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill shapes and green seaweed illustrations on both sides, label facing the camera, fully readable. Nothing else on the table.",
  "posture": "Brandon holds the jar low in her right hand, about to raise it beside her face.",
  "composition": "Straight-on medium shot: the phone lens is about 35 centimeters from the jar, which she holds low in her right hand just above the black table and fills the lower right 20 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, proud, about to show it.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label"
}
```

### K32 · T32, diferencial 16 em 1 · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K32
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "In her right hand, held still beside her right cheek, the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill shapes and green seaweed illustrations on both sides, label facing the camera, fully readable. Her left hand rests on the black table.",
  "posture": "Brandon holds the jar still beside her right cheek, label toward the lens.",
  "composition": "Straight-on medium shot: the jar is held up beside her right cheek and pushed slightly toward the camera, the phone lens is about 30 centimeters from the jar, which fills 20 percent of the frame at the right of her face, closer to the camera than her face, label facing the camera and fully readable. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, lively, listing.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label"
}
```

### K33 · T33, prova social da coach · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K33
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "In her right hand, held still beside her right cheek, the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill shapes and green seaweed illustrations on both sides, label facing the camera, fully readable. Her left hand rests on the black table.",
  "posture": "Brandon holds the jar still beside her right cheek, label toward the lens.",
  "composition": "Straight-on medium shot: the jar is held up beside her right cheek and pushed slightly toward the camera, the phone lens is about 30 centimeters from the jar, which fills 20 percent of the frame at the right of her face, closer to the camera than her face, label facing the camera and fully readable. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warm and certain.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label"
}
```

### K34 · T34, comment yes + follow · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K34
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "In her right hand, held still beside her right cheek, the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill shapes and green seaweed illustrations on both sides, label facing the camera, fully readable. Her left hand rests on the black table.",
  "posture": "Brandon holds the jar still beside her right cheek, label toward the lens.",
  "composition": "Straight-on medium shot: the jar is held up beside her right cheek and pushed slightly toward the camera, the phone lens is about 30 centimeters from the jar, which fills 20 percent of the frame at the right of her face, closer to the camera than her face, label facing the camera and fully readable. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, inviting, smiling on yes.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label"
}
```

### K35 · T35, CTA da marca, Amazon e legenda · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K35
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "In her right hand, held still beside her right cheek, the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill shapes and green seaweed illustrations on both sides, label facing the camera, fully readable. Her left hand rests on the black table.",
  "posture": "Brandon holds the jar still beside her right cheek, label toward the lens.",
  "composition": "Straight-on medium shot: the jar is held up beside her right cheek and pushed slightly toward the camera, the phone lens is about 30 centimeters from the jar, which fills 20 percent of the frame at the right of her face, closer to the camera than her face, label facing the camera and fully readable. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, clear and slow on the brand name.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem que você deixou no K01

```text
V01
(sem fala no take: abertura muda, a primeira fala entra no V03)

o que acontece no vídeo: A vizinha poda a cerca viva no primeiro plano; o marido e a esposa vêm correndo pela calçada molhada na direção da câmera.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, tesoura de poda cortando galhos e passos na calçada molhada, sem música
```

### V02 · T2 · frame inicial = a imagem que você deixou no K02

```text
V02
(sem fala no take: reação muda da esposa, ninguém fala)

o que acontece no vídeo: A esposa fica paralisada de choque, com as mãos coladas na cabeça e a boca escancarada, olhando para frente.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, respiração ofegante de corrida, sem música
```

### V03 · T3 · frame inicial = a imagem que você deixou no K03

```text
V03
falas no take, em inglês, na ordem:
1. o MARIDO (homem sarado sem camisa, de short cinza), voz masculina de barítono de um homem de uns trinta anos, confiante e galanteadora, sotaque americano padrão, fala animado, alto, chegando: "Hey!"
A VIZINHA e a ESPOSA não dizem nenhuma palavra.

cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de quem está falando.

o que acontece no vídeo: O marido chega trotando até a vizinha, sorrindo, com a mão erguida num aceno. Ele diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, sem música
```

### V04 · T4 · frame inicial = a imagem que você deixou no K04

```text
V04
falas no take, em inglês, na ordem:
1. a VIZINHA (mulher loira de óculos redondos, top preto e luvas pretas), voz feminina de uma mulher de uns trinta anos, média, clara e segura, sotaque americano do sul, leve, fala educada e seca: "Hey."
O MARIDO não diz nenhuma palavra.

cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de quem está falando.

o que acontece no vídeo: A vizinha se vira para o marido segurando a tesoura e responde. Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, sem música
```

### V05 · T5 · frame inicial = a imagem que você deixou no K05

```text
V05
falas no take, em inglês, na ordem:
1. o MARIDO (homem sarado sem camisa, de short cinza), voz masculina de barítono de um homem de uns trinta anos, confiante e galanteadora, sotaque americano padrão, fala galanteador e simpático: "I'm your new neighbor next door. I saw you a couple times."
A VIZINHA e a ESPOSA não dizem nenhuma palavra.

cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de quem está falando.

o que acontece no vídeo: O marido aponta a casa ao lado com a mão aberta enquanto fala; ao fundo a esposa continua curvada, recuperando o fôlego. Ele diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, sem música
```

### V06 · T6 · frame inicial = a imagem que você deixou no K06

```text
V06
falas no take, em inglês, na ordem:
1. o MARIDO (homem sarado sem camisa, de short cinza), voz masculina de barítono de um homem de uns trinta anos, confiante e galanteadora, sotaque americano padrão, fala galanteador, voz baixa: "You look so fine."
Ninguém mais fala.

cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de quem está falando.

o que acontece no vídeo: O marido sorri de canto e fala olhando a vizinha. Ele diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, sem música
```

### V07 · T7 · frame inicial = a imagem que você deixou no K07

```text
V07
falas no take, em inglês, na ordem:
1. a VIZINHA (mulher loira de óculos redondos, top preto e luvas pretas), voz feminina de uma mulher de uns trinta anos, média, clara e segura, sotaque americano do sul, leve, fala irônica, sobrancelha erguida: "Sweetheart, was that your wife running?"
O MARIDO e a ESPOSA não dizem nenhuma palavra.

cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de quem está falando.

o que acontece no vídeo: A vizinha olha para a esposa que se afasta correndo e fala com o marido. Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, sem música
```

### V08 · T8 · frame inicial = a imagem que você deixou no K08

```text
V08
falas no take, em inglês, na ordem:
1. o MARIDO (homem sarado sem camisa, de short cinza), voz masculina de barítono de um homem de uns trinta anos, confiante e galanteadora, sotaque americano padrão, fala galanteador, sem vergonha nenhuma: "Yes. But if my wife looked like you, I would have never left the house."
A VIZINHA e a ESPOSA não dizem nenhuma palavra.

cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de quem está falando.

o que acontece no vídeo: O marido abre a mão na direção da vizinha enquanto fala; a esposa segue correndo ao longe.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, sem música
```

### V09 · T9 · frame inicial = a imagem que você deixou no K09

```text
V09
falas no take, em inglês, na ordem:
1. a VIZINHA (mulher loira de óculos redondos, top preto e luvas pretas), voz feminina de uma mulher de uns trinta anos, média, clara e segura, sotaque americano do sul, leve, fala seca e cortante: "Then she should probably start doing what I do."
O MARIDO não diz nenhuma palavra.

cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de quem está falando.

o que acontece no vídeo: A vizinha olha para o marido e fala, sem sorrir. Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, sem música
```

### V10 · T10 · frame inicial = a imagem que você deixou no K10

```text
V10
falas no take, em inglês, na ordem:
1. o MARIDO (homem sarado sem camisa, de short cinza), voz masculina de barítono de um homem de uns trinta anos, confiante e galanteadora, sotaque americano padrão, fala curioso, ainda flertando: "And what is that, hitting the gym every day?"
Ninguém mais fala.

cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de quem está falando.

o que acontece no vídeo: O marido inclina a cabeça e pergunta. Ele diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, sem música
```

### V11 · T11 · frame inicial = a imagem que você deixou no K11

```text
V11
falas no take, em inglês, na ordem:
1. a VIZINHA (mulher loira de óculos redondos, top preto e luvas pretas), voz feminina de uma mulher de uns trinta anos, média, clara e segura, sotaque americano do sul, leve, fala tranquila e direta, sem parar de podar: "No. I am fifty-seven. I stopped training like a kid years ago."
O MARIDO não diz nenhuma palavra.

cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de quem está falando.

o que acontece no vídeo: A vizinha volta a podar e responde olhando por cima do ombro. Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, tesoura de poda cortando galhos, sem música
```

### V12 · T12 · frame inicial = a imagem que você deixou no K12

```text
V12
falas no take, em inglês, na ordem:
1. o MARIDO (homem sarado sem camisa, de short cinza), voz masculina de barítono de um homem de uns trinta anos, confiante e galanteadora, sotaque americano padrão, fala em choque, alto: "What?"
Ninguém mais fala.

cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de quem está falando.

o que acontece no vídeo: O marido arregala os olhos e fala. Ele diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, sem música
```

### V13 · T13 · frame inicial = a imagem que você deixou no K13

```text
V13
falas no take, em inglês, na ordem:
1. o MARIDO (homem sarado sem camisa, de short cinza), voz masculina de barítono de um homem de uns trinta anos, confiante e galanteadora, sotaque americano padrão, fala incrédulo e espantado: "Fifty-seven? You're old enough to be my mom. What's your secret?"
A VIZINHA não diz nenhuma palavra.

cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de quem está falando.

o que acontece no vídeo: O marido abre as mãos, incrédulo, e fala. Ele diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, sem música
```

### V14 · T14 · frame inicial = a imagem que você deixou no K14

```text
V14
falas no take, em inglês, na ordem:
1. a VIZINHA (mulher loira de óculos redondos, top preto e luvas pretas), voz feminina de uma mulher de uns trinta anos, média, clara e segura, sotaque americano do sul, leve, fala casual e confiante, como quem conta um segredo simples: "I just listened to this holistic coach I found online. She taught me literally everything."
O MARIDO não diz nenhuma palavra.

cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de quem está falando.

o que acontece no vídeo: A vizinha ergue os galhos podados e o saco de lixo e fala com naturalidade.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, farfalhar do saco de lixo, sem música
```

### V15 · T15 · frame inicial = a imagem que você deixou no K15

```text
V15
(sem fala no take: o "literally everything" da vizinha no V14 entra como voz-over na edição; o marido fica calado)

o que acontece no vídeo: O marido escuta em silêncio, pisca devagar e fica pensativo.

câmera: leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano

som ambiente: rua de bairro residencial depois da chuva, pássaros ao longe, sem música
```

### V16 · T16 · frame inicial = a imagem que você deixou no K16

```text
V16
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e segura de quem tem autoridade, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I'm a holistic coach, and my oldest clients outwork people half their age. Save this video. You never know when your body will need it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com as duas mãos apoiadas na mesa preta.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V17 · T17 · frame inicial = a imagem que você deixou no K17

```text
V17
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e didática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Number one: lemon juice and warm water. Squeeze half a lemon into a glass of warm water and drink it every morning on an empty stomach."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon ergue o copo e o meio limão e, no squeeze, espreme o limão dentro do copo.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V18 · T18 · frame inicial = a imagem que você deixou no K18

```text
V18
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e convicta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "It flushes out your digestive system, jump-starts your metabolism, and cuts through sugar cravings before they even start."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera segurando o copo e o meio limão.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V19 · T19 · frame inicial = a imagem que você deixou no K19

```text
V19
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação intrigante, virando o assunto, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "But a flat belly means little if your skin is still dull and wrinkly."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera e baixa um pouco o copo e o limão.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V20 · T20 · frame inicial = a imagem que você deixou no K20

```text
V20
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação didática e prática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Number two: apple cider vinegar and coconut oil. Mix one teaspoon of vinegar into a tablespoon of coconut oil and apply it to your face for fifteen minutes."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon mexe a mistura com dois dedos e, no face, toca a bochecha com os dedos.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V21 · T21 · frame inicial = a imagem que você deixou no K21

```text
V21
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação confiante, baixando a voz no fim como quem conta um segredo, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "It tightens the skin, fades fine lines, and brings back that glow. Women pay hundreds for facials that do less. But here is what most people miss."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera segurando a tigelinha com as duas mãos.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V22 · T22 · frame inicial = a imagem que você deixou no K22

```text
V22
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação séria e acolhedora, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If your stress has been high for years, you will never get the body you want, no matter how clean you eat or how hard you work out."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon se inclina um pouco para a câmera segurando a tigelinha.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V23 · T23 · frame inicial = a imagem que você deixou no K23

```text
V23
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação enfática, como quem chega na parte mais importante, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "That is why this next one is the most important. Number three: sea moss."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon empurra o pote de sea moss seco na direção da câmera e fala.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V24 · T24 · frame inicial = a imagem que você deixou no K24

```text
V24
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa e orgulhosa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I started telling my clients to put sea moss back into every single morning years ago, and it became the one thing that changed everything."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera segurando o pote com as duas mãos.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V25 · T25 · frame inicial = a imagem que você deixou no K25

```text
V25
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação séria e explicativa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Every stressful day burns through your minerals, and when nothing puts them back, your body stays stuck in alarm mode, wired at night and hungry for sugar."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala segurando o pote numa mão e explicando com a outra mão aberta.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V26 · T26 · frame inicial = a imagem que você deixou no K26

```text
V26
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e tranquilizadora, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Sea moss carries those minerals right back in, so your body stops guarding itself and finally gets out of alarm mode."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon aponta o gel com o indicador e fala para a câmera.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V27 · T27 · frame inicial = a imagem que você deixou no K27

```text
V27
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa, contando uma história, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I told our brothers and sisters in their forties to sixties about it, and they came back telling me they finally sleep through the night."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera segurando a tigelinha com as duas mãos.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V28 · T28 · frame inicial = a imagem que você deixou no K28

```text
V28
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação indignada, baixando a voz, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "And the scary part is they stripped the minerals out of almost everything on the shelf, because a starved body keeps craving, and a craving customer keeps buying."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon se apoia na mesa e fala para a câmera, mais perto.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V29 · T29 · frame inicial = a imagem que você deixou no K29

```text
V29
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação firme e direta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "So if they took it out, you need to put it back in yourself. Nobody is going to do that for you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera apoiada na mesa, levantando um pouco uma das mãos.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V30 · T30 · frame inicial = a imagem que você deixou no K30

```text
V30
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação de alerta, com um leve desgosto, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "But I have to warn you, not all sea moss is the same. Most of it is packed with sugar and fillers that feed the cravings even more."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon mostra uma tigelinha em cada mão e fala para a câmera.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V31 · T31 · frame inicial = a imagem que você deixou no K31

```text
V31
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação orgulhosa, dizendo Natural Rems Sea Moss devagar e por inteiro, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The only one I use is Natural Rems Sea Moss. Wild Irish sea moss, made right here in the USA, with less than a gram of sugar."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon ergue o frasco devagar da altura da cintura até o lado do rosto no nome do produto e o deixa parado, rótulo de frente.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V32 · T32 · frame inicial = a imagem que você deixou no K32

```text
V32
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada, listando, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Sixteen ingredients in one green apple gummy, ashwagandha included, so you are not lining up five bottles every morning. Thousands of people order it every month."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V33 · T33 · frame inicial = a imagem que você deixou no K33

```text
V33
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa e segura, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "And the clients I train who switched to it all tell me the same thing: it is the first routine they have never skipped."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V34 · T34 · frame inicial = a imagem que você deixou no K34

```text
V34
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação convidativa, sorrindo no yes, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Comment yes if your body has been stuck in alarm mode, and follow me so you do not lose these three."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com o frasco parado ao lado do rosto, sorrindo no yes.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V35 · T35 · frame inicial = a imagem que você deixou no K35

```text
V35
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação clara, dizendo Natural Rems Sea Moss devagar e por inteiro, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the caption."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente, do começo ao fim, sem baixar o frasco.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V35.
2. Esquete no tempo exato do modelo: V01 0,00 a 0,97 s; V02 0,97 a 2,97 s; V03 2,97 a 3,50 s; V04 3,50 a 4,50 s; V05 4,50 a 7,87 s; V06 7,87 a 9,47 s; V07 9,47 a 11,80 s; V08 11,80 a 16,83 s; V09 16,83 a 18,70 s; V10 18,70 a 21,07 s; V11 21,07 a 23,87 s; V12 23,87 a 24,57 s; V13 24,57 a 27,43 s; V14 27,43 a 29,80 s; V15 29,80 a 30,90 s.
3. **V14 → V15:** cortar para o V15 em "She taught me" e deixar o áudio do V14 continuar por baixo com "literally everything" sobre o close do marido calado.
4. Corte seco do V15 para o V16 (a Brandon entra já falando). Do V16 ao V35, cortar logo depois da última palavra de cada clipe.
5. Zero tempo morto: todo clipe falado começa já falando. Isolate Voice / Keep Vocal no áudio.
6. Legenda de tela branca sem serifa, duas a três palavras por vez, no meio do quadro, igual ao modelo. No V34, `yes` grande e isolado na tela. No V35, duas setas vermelhas apontando para baixo (para a legenda do post), como no modelo.
7. Sem Voice Changer: a voz de cada personagem e da Brandon vem do prompt de cada V.
8. Música opcional só a partir do V16, nunca na esquete, entre -19 e -20 dB, fora da biblioteca do TikTok.
9. Rótulo pequeno `AI-generated` num canto do vídeo.
10. No V31 a V35 o frasco não pode ser cortado nem coberto: nenhum B-roll por cima (regra da marca).

## 5. Legenda do post

- Primeira linha, sempre: `#ad #syntheticperformer #naturalrems`
- Logo abaixo: o link da Amazon do Natural Rems Sea Moss (o V35 manda tocar no link da legenda).
- Chave de conteúdo de IA da plataforma LIGADA.

## 6. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | (sem fala) | (sem fala) |
| T2 | (sem fala) | (sem fala) |
| T3 | Hey! | Oi! |
| T4 | Hey. | Oi. |
| T5 | I'm your new neighbor next door. I saw you a couple times. | Sou seu vizinho novo aqui do lado. Te vi umas vezes. |
| T6 | You look so fine. | Você está muito bem. |
| T7 | Sweetheart, was that your wife running? | Querido, aquela correndo era sua esposa? |
| T8 | Yes. But if my wife looked like you, I would have never left the house. | Era. Mas se a minha esposa fosse como você, eu nunca teria saído de casa. |
| T9 | Then she should probably start doing what I do. | Então talvez ela devesse começar a fazer o que eu faço. |
| T10 | And what is that, hitting the gym every day? | E o que é, academia todo dia? |
| T11 | No. I am fifty-seven. I stopped training like a kid years ago. | Não. Eu tenho cinquenta e sete. Parei de treinar feito criança faz anos. |
| T12 | What? | O quê? |
| T13 | Fifty-seven? You're old enough to be my mom. What's your secret? | Cinquenta e sete? Você tem idade pra ser minha mãe. Qual é o seu segredo? |
| T14 | I just listened to this holistic coach I found online. She taught me literally everything. | Eu só ouvi uma coach holística que achei na internet. Ela me ensinou literalmente tudo. |
| T15 | (voz-over do T14: literally everything) | (voz-over do T14: literalmente tudo) |
| T16 | I'm a holistic coach, and my oldest clients outwork people half their age. Save this video. You never know when your body will need it. | Eu sou coach holística, e as minhas clientes mais velhas dão conta de mais do que gente com metade da idade delas. Salva esse vídeo. Você nunca sabe quando o seu corpo vai precisar dele. |
| T17 | Number one: lemon juice and warm water. Squeeze half a lemon into a glass of warm water and drink it every morning on an empty stomach. | Número um: suco de limão e água morna. Esprema meio limão num copo de água morna e beba toda manhã em jejum. |
| T18 | It flushes out your digestive system, jump-starts your metabolism, and cuts through sugar cravings before they even start. | Limpa o seu sistema digestivo, dá a partida no seu metabolismo e corta a vontade de doce antes de ela começar. |
| T19 | But a flat belly means little if your skin is still dull and wrinkly. | Mas barriga lisa vale pouco se a sua pele continua opaca e enrugada. |
| T20 | Number two: apple cider vinegar and coconut oil. Mix one teaspoon of vinegar into a tablespoon of coconut oil and apply it to your face for fifteen minutes. | Número dois: vinagre de maçã e óleo de coco. Misture uma colher de chá de vinagre numa colher de sopa de óleo de coco e passe no rosto por quinze minutos. |
| T21 | It tightens the skin, fades fine lines, and brings back that glow. Women pay hundreds for facials that do less. But here is what most people miss. | Firma a pele, apaga as linhas finas e traz aquele brilho de volta. Tem mulher que paga centenas por limpeza de pele que faz menos. Mas é aqui que a maioria das pessoas erra. |
| T22 | If your stress has been high for years, you will never get the body you want, no matter how clean you eat or how hard you work out. | Se o seu estresse está alto há anos, você nunca vai ter o corpo que quer, não importa o quão limpo você coma ou o quanto você treine. |
| T23 | That is why this next one is the most important. Number three: sea moss. | Por isso esta próxima é a mais importante. Número três: sea moss. |
| T24 | I started telling my clients to put sea moss back into every single morning years ago, and it became the one thing that changed everything. | Eu comecei a mandar as minhas clientes colocarem o sea moss de volta em toda manhã faz anos, e virou a única coisa que mudou tudo. |
| T25 | Every stressful day burns through your minerals, and when nothing puts them back, your body stays stuck in alarm mode, wired at night and hungry for sugar. | Todo dia estressante queima os seus minerais, e quando nada repõe, o seu corpo fica preso no modo alarme, ligado à noite e com fome de doce. |
| T26 | Sea moss carries those minerals right back in, so your body stops guarding itself and finally gets out of alarm mode. | O sea moss leva esses minerais de volta pra dentro, então o seu corpo para de se proteger e finalmente sai do modo alarme. |
| T27 | I told our brothers and sisters in their forties to sixties about it, and they came back telling me they finally sleep through the night. | Eu contei isso pros nossos irmãos e irmãs de quarenta a sessenta anos, e eles voltaram me dizendo que finalmente dormem a noite inteira. |
| T28 | And the scary part is they stripped the minerals out of almost everything on the shelf, because a starved body keeps craving, and a craving customer keeps buying. | E o assustador é que tiraram os minerais de quase tudo que está na prateleira, porque um corpo faminto continua com vontade, e um cliente com vontade continua comprando. |
| T29 | So if they took it out, you need to put it back in yourself. Nobody is going to do that for you. | Então, se eles tiraram, você precisa colocar de volta sozinho. Ninguém vai fazer isso por você. |
| T30 | But I have to warn you, not all sea moss is the same. Most of it is packed with sugar and fillers that feed the cravings even more. | Mas eu preciso te avisar: nem todo sea moss é igual. A maioria vem lotada de açúcar e enchimento que alimentam ainda mais a vontade de doce. |
| T31 | The only one I use is Natural Rems Sea Moss. Wild Irish sea moss, made right here in the USA, with less than a gram of sugar. | O único que eu uso é o Natural Rems Sea Moss. Sea moss irlandês selvagem, feito aqui mesmo nos EUA, com menos de um grama de açúcar. |
| T32 | Sixteen ingredients in one green apple gummy, ashwagandha included, so you are not lining up five bottles every morning. Thousands of people order it every month. | Dezesseis ingredientes numa goma de maçã verde, ashwagandha incluída, pra você não ter que enfileirar cinco frascos toda manhã. Milhares de pessoas compram todo mês. |
| T33 | And the clients I train who switched to it all tell me the same thing: it is the first routine they have never skipped. | E as clientes que eu treino e trocaram por ele me dizem a mesma coisa: é a primeira rotina que elas nunca pularam. |
| T34 | Comment yes if your body has been stuck in alarm mode, and follow me so you do not lose these three. | Comente yes se o seu corpo anda preso no modo alarme, e me siga pra não perder essas três. |
| T35 | Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the caption. | Procure Natural Rems Sea Moss na Amazon. Ou é só tocar no link que eu deixei na legenda. |

## 7. Roteiro final em inglês

1. (sem fala)
2. (sem fala)
3. Hey!
4. Hey.
5. I'm your new neighbor next door. I saw you a couple times.
6. You look so fine.
7. Sweetheart, was that your wife running?
8. Yes. But if my wife looked like you, I would have never left the house.
9. Then she should probably start doing what I do.
10. And what is that, hitting the gym every day?
11. No. I am fifty-seven. I stopped training like a kid years ago.
12. What?
13. Fifty-seven? You're old enough to be my mom. What's your secret?
14. I just listened to this holistic coach I found online. She taught me literally everything.
15. (voz-over do T14: literally everything)
16. I'm a holistic coach, and my oldest clients outwork people half their age. Save this video. You never know when your body will need it.
17. Number one: lemon juice and warm water. Squeeze half a lemon into a glass of warm water and drink it every morning on an empty stomach.
18. It flushes out your digestive system, jump-starts your metabolism, and cuts through sugar cravings before they even start.
19. But a flat belly means little if your skin is still dull and wrinkly.
20. Number two: apple cider vinegar and coconut oil. Mix one teaspoon of vinegar into a tablespoon of coconut oil and apply it to your face for fifteen minutes.
21. It tightens the skin, fades fine lines, and brings back that glow. Women pay hundreds for facials that do less. But here is what most people miss.
22. If your stress has been high for years, you will never get the body you want, no matter how clean you eat or how hard you work out.
23. That is why this next one is the most important. Number three: sea moss.
24. I started telling my clients to put sea moss back into every single morning years ago, and it became the one thing that changed everything.
25. Every stressful day burns through your minerals, and when nothing puts them back, your body stays stuck in alarm mode, wired at night and hungry for sugar.
26. Sea moss carries those minerals right back in, so your body stops guarding itself and finally gets out of alarm mode.
27. I told our brothers and sisters in their forties to sixties about it, and they came back telling me they finally sleep through the night.
28. And the scary part is they stripped the minerals out of almost everything on the shelf, because a starved body keeps craving, and a craving customer keeps buying.
29. So if they took it out, you need to put it back in yourself. Nobody is going to do that for you.
30. But I have to warn you, not all sea moss is the same. Most of it is packed with sugar and fillers that feed the cravings even more.
31. The only one I use is Natural Rems Sea Moss. Wild Irish sea moss, made right here in the USA, with less than a gram of sugar.
32. Sixteen ingredients in one green apple gummy, ashwagandha included, so you are not lining up five bottles every morning. Thousands of people order it every month.
33. And the clients I train who switched to it all tell me the same thing: it is the first routine they have never skipped.
34. Comment yes if your body has been stuck in alarm mode, and follow me so you do not lose these three.
35. Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the caption.

Hey! Hey. I'm your new neighbor next door. I saw you a couple times. You look so fine. Sweetheart, was that your wife running? Yes. But if my wife looked like you, I would have never left the house. Then she should probably start doing what I do. And what is that, hitting the gym every day? No. I am fifty-seven. I stopped training like a kid years ago. What? Fifty-seven? You're old enough to be my mom. What's your secret? I just listened to this holistic coach I found online. She taught me literally everything. I'm a holistic coach, and my oldest clients outwork people half their age. Save this video. You never know when your body will need it. Number one: lemon juice and warm water. Squeeze half a lemon into a glass of warm water and drink it every morning on an empty stomach. It flushes out your digestive system, jump-starts your metabolism, and cuts through sugar cravings before they even start. But a flat belly means little if your skin is still dull and wrinkly. Number two: apple cider vinegar and coconut oil. Mix one teaspoon of vinegar into a tablespoon of coconut oil and apply it to your face for fifteen minutes. It tightens the skin, fades fine lines, and brings back that glow. Women pay hundreds for facials that do less. But here is what most people miss. If your stress has been high for years, you will never get the body you want, no matter how clean you eat or how hard you work out. That is why this next one is the most important. Number three: sea moss. I started telling my clients to put sea moss back into every single morning years ago, and it became the one thing that changed everything. Every stressful day burns through your minerals, and when nothing puts them back, your body stays stuck in alarm mode, wired at night and hungry for sugar. Sea moss carries those minerals right back in, so your body stops guarding itself and finally gets out of alarm mode. I told our brothers and sisters in their forties to sixties about it, and they came back telling me they finally sleep through the night. And the scary part is they stripped the minerals out of almost everything on the shelf, because a starved body keeps craving, and a craving customer keeps buying. So if they took it out, you need to put it back in yourself. Nobody is going to do that for you. But I have to warn you, not all sea moss is the same. Most of it is packed with sugar and fillers that feed the cravings even more. The only one I use is Natural Rems Sea Moss. Wild Irish sea moss, made right here in the USA, with less than a gram of sugar. Sixteen ingredients in one green apple gummy, ashwagandha included, so you are not lining up five bottles every morning. Thousands of people order it every month. And the clients I train who switched to it all tell me the same thing: it is the first routine they have never skipped. Comment yes if your body has been stuck in alarm mode, and follow me so you do not lose these three. Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the caption.
