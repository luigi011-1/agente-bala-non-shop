# Instrucoes do agente executor do Google Flow AI

Versao 20, 2026-10-06. Contrato de execucao, subordinado ao roteador de cada oferta.
Auraly segue exclusivamente WORKFLOW_AURALY.md. Angle 1/2 seguem CLAUDE.md e, no FitWell,
PLAYBOOK_FITYWELL.md. Os pacotes existentes permanecem como foram aprovados.

Este documento nao manda o Codex gerar imagens, abrir navegador ou executar Flow. O operador
leva estas instrucoes ao executor. Nao inserir este texto dentro dos prompts K/V. No Auraly, K e V
podem chegar na mesma entrega textual, em blocos separados. O executor registra ambos, executa todos
os K primeiro, espera a selecao manual e so entao executa os V correspondentes.

## Bloco para a memoria do executor

Voce executa prompts finalizados dentro do Google Flow. Nao reescreva, traduza, resuma nem
altere a copy. Registre o perfil da producao antes de gerar qualquer asset. Perfil ausente ou
incompativel com os codigos recebidos exige esclarecimento, nunca escolha silenciosa.

### Perfis de execucao

| Configuracao | AURALY | CLASSICO (Angle 1/2) |
|---|---|---|
| Imagem | Nano Banana 2 | Nano Banana 2 |
| Formato | 9:16 vertical, imagem e video | 9:16 vertical, imagem e video |
| Anexo da imagem (K) | So o character sheet do avatar ativo | So o character sheet (ou a imagem de avatar) do avatar ativo |
| Imagens por K | 4, com selecao manual | 4, com selecao manual (o operador apaga 3 e deixa 1) |
| Relacao K/V | Mapa explicito recebido com o pacote; um K pode alimentar varios V | Maior K menor ou igual ao numero de V |
| Video | Veo 3.1 Lite | Omni Flash, e somente ele |
| Prioridade | Lower Priority | Padrao do Omni Flash |
| Duracao por clipe | 8 segundos | 8 segundos |
| Variacoes por V | 1, um unico resultado por prompt | 1, um unico resultado por prompt |
| Anexo do video (V) | So a imagem escolhida do K, como INITIAL FRAME | So a imagem escolhida do K, como INITIAL FRAME |
| Lote de video | Fechado, no maximo 7 codigos V | Fechado, no maximo 7 codigos V |

REGRA UNICA DE QUANTIDADE E FORMATO (v19, Luigi, 2026-10-05), vale em TODOS os perfis: **4 imagens por K,
1 video por V, e SEMPRE 9:16 vertical tanto na imagem quanto no video**. Antes de cada K e de cada V,
conferir a proporcao 9:16; nunca 16:9, 1:1 nem 4:5. Se a interface nao permitir 9:16, parar e avisar. Antes de cada V, colocar a quantidade de saida do video em 1; nunca gerar duas ou
mais versoes do mesmo V. Os valores Auraly reproduzem as travas de WORKFLOW_AURALY.md (modelo e
prioridade). Nunca transportar o modelo de video classico (Omni Flash) para Auraly. Um pacote historico com outro contrato nao autoriza alterar uma producao
nova; preservar seu contrato aprovado quando o usuario solicitar especificamente sua retomada.

### 🔴 ANEXOS (v20, Luigi, 2026-10-06): SO O CHARACTER SHEET NA IMAGEM, SO A IMAGEM ESCOLHIDA NO VIDEO

Falha real: o executor parou dizendo que "nao recebeu o frame modelo no pacote". **Nao existe frame
modelo.** Nenhum K e nenhum V precisa do frame do video original. Os prompts sao autossuficientes:
cenario, pose, camera e acao do video original estao escritos por extenso dentro de cada prompt.

1. **IMAGEM (K):** o unico anexo e o CHARACTER SHEET do avatar ativo (a imagem de avatar que o operador
   anexou). Fluxo de cada K: anexar o character sheet, colar o prompt, gerar 4 variacoes em 9:16, parar.
   O operador escolhe uma. Nunca pedir, esperar ou procurar frame do video modelo, anchor em cena real,
   REF-CARTA, REF-A ou qualquer outra imagem. Onde este documento disser "anchor", ler "character sheet
   do avatar ativo".
2. **VIDEO (V):** o unico anexo e a imagem que o operador escolheu daquele K, como INITIAL FRAME.
   Fluxo de cada V: anexar essa imagem, colar o prompt de video, gerar 1 resultado em 9:16. Nada mais.
   Nunca anexar o character sheet, o frame do modelo ou outra imagem no video.
3. **Se o pacote mencionar um frame modelo, "segundo anexo" ou outra referencia, ignorar essa mencao e
   NAO parar por isso.** So o character sheet (K) e a imagem escolhida (V) valem. Parar somente se o
   character sheet do avatar ativo ou a imagem escolhida do K faltar.
4. Unica ampliacao: no MOVIE STYLE os `REF-P` aprovados sao os character sheets do elenco e sao os anexos
   do K (um por personagem principal, ate o mapa dizer). O `REF-COMPOSICAO` do short form acabou: a
   composicao vem escrita no K, e o anexo do K e o character sheet.
5. O texto do prompt manda: nao reescrever, nao completar com o que "falta" do frame modelo.

### 🔴 CLASSICO: 4 imagens por K, selecao do operador, video so no Omni Flash (v14, 2026-09-24)

Falha real registrada: o operador pedia quatro variacoes por K e o executor continuava gerando uma
so. Isto e obrigatorio em todo K do perfil CLASSICO:

1. **Quatro imagens por K, sempre.** Antes de gerar cada K, abrir o seletor de quantidade de saida
   do Nano Banana 2 e colocar em 4 (x4). Conferir o seletor em TODO K, porque ele pode voltar para 1
   sozinho. Um K com menos de quatro imagens esta INCOMPLETO. Se a interface entregar menos de
   quatro, gerar o MESMO prompt, com o MESMO character sheet, de novo ate existirem quatro candidatas daquele
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

### AURALY, character sheet e cenario do video modelo (Luigi, 2026-10-04; vale SO no Auraly)

Roster Auraly: Avery Knox, Jordan Vale (ricaço), Devon Price (careca) e Morgan Vance (Jordan e Devon sao avatares novos desde 2026-10-07; os antigos com esses nomes foram aposentados). Desde a v20 todo K Auraly leva UM
unico anexo: o CHARACTER SHEET do avatar ativo (close do rosto mais frente, costas e os dois lados,
fundo cinza), que trava identidade, corpo e roupa. O cenario, o angulo de camera e o enquadramento sao
os do video modelo, quase 100% fieis, e vem escritos por inteiro no texto do K (a v18 mandava anexar
tambem o frame do modelo; revogado na v20). Nunca copiar o fundo cinza do sheet para a cena e nunca
trocar o cenario descrito no K. Tudo organico: nada sobrenatural (brilho magico, aura, particulas,
objeto flutuando, efeito visual) que o texto do K nao peca. FitWell e Sea Moss (perfil CLASSICO) usam o
mesmo anexo unico e o avatar fixo por conta abaixo.

(Historico ate a v17:) A referencia de cada um era a anchor em cena real, anexada em todo K. Na v18 e v19 foi character sheet mais frame do modelo.

AVATAR FIXO POR CONTA (v16, 2026-09-25; no Auraly so a ROUPA continua fixa desde a v18): cada conta usa o mesmo avatar com a roupa e o cenario-base
da anchor em todo video e em todo gancho. O texto do K descreve esse cenario e essa roupa. Quando o
video modelo tem uma cena em outro lugar, o texto do K descreve o lugar novo e manda usar a anchor
para identidade e roupa; a pessoa e a roupa nunca mudam. O angulo de camera serve a acao estrutural
preservada: pode ser exotico quando aumenta a anomalia, mas pode se repetir entre variacoes para
preservar composicao e timing. Mudar o angulo conta como a unica variavel dessa variacao.

No T1, a anomalia visual domina. O kit completo de tarologo nao e obrigatorio: usar de zero a dois
marcadores discretos de Auraly somente se nao competirem com o heroi. Desde a v18 (Luigi, 2026-10-04)
nao ha efeito visual nem nada sobrenatural, salvo quando o proprio video modelo tem e o texto do V
pede; efeitos multiplos ou cinematograficos continuam proibidos. Do T2 ao CTA, volta o kit de credencial visual
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

Receber o character sheet do avatar e registrar o identificador e nome do arquivo. Nao casar imagens por ordem de
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

Usar Nano Banana 2, formato 9:16 e o character sheet do avatar ativo como unico anexo. Colar cada prompt literalmente e gerar a
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
Cada codigo V tem uma unica variacao (um resultado), gerada do frame selecionado.

CLASSICO: V usa o maior K disponivel cujo numero nao exceda o de V. Por exemplo, com K01, K03 e
K06: V01/V02 usam K01; V03/V04/V05 usam K03; V06 usa K06. Se nao houver K anterior ou igual,
parar. Nao adivinhar pela aparencia ou ordem da galeria. Cada V tem uma variacao, gerada no Omni
Flash a partir da UNICA imagem que o operador deixou naquele K.

### Videos em lotes fechados

1. Receber e registrar toda a fila V, sem executar tudo automaticamente.
2. Antes de cada V, conferir avatar, perfil e K indicado no MAPA K/V.
3. Usar a imagem exclusivamente como INITIAL FRAME, nunca Element, ingredient ou referencia de objeto.
4. Configurar o modelo do perfil: AURALY em Veo 3.1 Lite, Lower Priority, oito segundos, um
   unico resultado por V; CLASSICO somente em Omni Flash, oito segundos, um unico resultado por V.
5. Iniciar somente o primeiro lote de no maximo sete codigos V. O teto e de codigos, nao uma autorizacao para iniciar codigos adicionais por vaga liberada.
6. Esperar todos os codigos desse lote. Nao preencher vagas com o lote seguinte.
7. Informar concluidos, falhas e pendentes. Se houver pendentes, parar e aguardar `prossiga`.
8. Mesmo quando o lote terminar, esperar `prossiga` para iniciar o proximo lote.
9. Ao retomar, executar somente o trabalho pendente autorizado. Nunca reiniciar um V concluido
   sem pedido explicito. Distinguir o V que falhou dos que ja foram concluidos.
10. Se a interface nao permitir a configuracao requerida, informar a limitacao antes de mudar
    modelo, prioridade, quantidade, duracao ou modo de referencia.

A fala e literal. A acao continua o estado inicial da imagem. Manter camera e som indicados,
sem adicionar musica, legenda, traducao ou texto auxiliar por conta propria.

### Fechamento

Relatar arquivos gerados por avatar, K/V e variacao, com pendencias explicitas. Geracao de um
avatar nao conclui a fila inteira. Entrega de prompts, midia gerada, montagem e publicacao sao
marcos diferentes. Nunca declarar publicacao ou resultado comercial pela existencia de assets.

## Historico resumido

v1-v4: configuracoes e formato evoluiram entre 08 e 09/09; lotes fechados substituem fila continua.
v5: perfil de uma imagem final e um video em 11/09.
v6: reutilizacao de K por varios V em 12/09.
v7: separacao explicita de perfis. Auraly preserva o contrato do workflow canonico (4 imagens,
selecao manual, 3 variacoes, K/V pelo mesmo numero); o classico preserva o contrato v6. As versoes
anteriores sao historico, nao instrucoes concorrentes.
v8, 2026-09-15: corrigido bug real reportado pelo Luigi (`producao/fitywell_arroz`), o executor
colou o prompt de IMAGEM no campo de video depois de gerar/editar os K corretamente. Adicionada a
secao "Reconhecer prompt de IMAGEM (K) contra prompt de VIDEO (V)", com a checagem mecanica das
tres marcas obrigatorias (`o que acontece no vídeo:`, `câmera:`, `som ambiente:`) antes de
qualquer submissao de video. Vale para os dois perfis, Auraly e Classico.
v9, 2026-09-18: excecao do kit de tarologo para os quatro avatares de luxo da Auraly.
v11, 2026-09-20: o portfolio 4/3/3 em tres familias foi REVOGADO pelo Luigi no mesmo dia e
substituido pelo METODO PUZZLE aplicado ao hook do video modelo, igual ao Angulo 2: uma acao
estrutural preservada e dez variacoes de uma variavel cada. Acrescentada a regra do T1 mudo com
cortes internos ao clipe, que nao pode fazer o executor parar na checagem das tres marcas.
v17, 2026-09-30: Morgan Vance entra no roster Auraly (conta organica nova). Sem mudanca de
configuracao.
v12, 2026-09-22: roster Auraly reduzido a Walt, Darlene e Lorraine. A fingerprint sai: a referencia
e a anchor em cena real, com instrucao de usar so a identidade quando o K pede cenario novo. A
excecao dos avatares de luxo (v9) foi removida junto com eles.
v13, 2026-09-23: movie style (short form e venda). Character sheets `REF-P` gerados e aprovados
antes dos K, anexados por um MAPA DE ANEXOS; V de dialogo com o bloco `falas no take` (quem fala,
voz e emocao em cada linha); B-roll com `(sem fala no take: ...)`. As tres marcas continuam a
checagem mecanica de todo V.
v13, 2026-09-23: secao de short form de crescimento sem anchor (`producao/sf_torta_vovo`): dupla
descrita no K, REF-COMPOSICAO como unico anexo, um K alimentando tres V e V de dialogo nomeando
quem fala.
v14, 2026-09-24: perfil CLASSICO passa a gerar QUATRO imagens por K, com selecao manual do operador
(ele apaga tres e deixa uma), e o video passa a ser SOMENTE no Omni Flash, um unico resultado por V.
Motivo: o executor gerava uma imagem so mesmo quando o operador pedia quatro. O AURALY nao muda.
v15, 2026-09-24: juntadas no mesmo arquivo as tres linhas que corriam em paralelo em worktrees
separadas: movie style com `REF-P` (v13), short form de crescimento sem anchor (a outra v13, de
`producao/sf_torta_vovo`) e o perfil CLASSICO de quatro imagens e Omni Flash (v14). Nenhuma regra
de conteudo mudou nesta versao.
v16, 2026-09-25: AVATAR FIXO POR CONTA tambem no Auraly. Revoga o cenario proprio e a roupa livre por
gancho da v7: roupa e cenario-base da anchor em todo video e gancho; so o angulo de camera varia.
v19, 2026-10-05: regra unica para todos os perfis, a pedido do Luigi: SEMPRE 4 imagens por K e SEMPRE 1
video (um unico resultado) por V. Revoga o video com mais de um resultado por V no Auraly (Veo 3.1 Lite). Modelo e prioridade
de cada perfil nao mudam. Tambem fixado: formato 9:16 para imagem e video em todos os perfis.
v18, 2026-10-04: Auraly passa a anexar o CHARACTER SHEET (identidade e roupa) mais o frame do video
modelo (cenario, angulo e enquadramento) em todo K. O cenario e o angulo sao os do modelo, quase 100%
fieis, organicos e sem nada sobrenatural. Revoga so no Auraly a parte de cenario do avatar fixo da
v16; a roupa segue fixa pelo sheet. FitWell e Sea Moss nao mudam.
v17, 2026-09-25: a pedido do Luigi, todo prompt de IMAGEM (K e REF-P) passa a ser entregue em JSON,
para o modelo compreender melhor cada parte. As regras de conteudo nao mudam. O executor cola o
objeto inteiro, de `{` a `}`; o reconhecimento K contra V ganha a marca mecanica do `{` inicial.
v10, 2026-09-20: sincronizado com o portfolio Auraly 4/3/3, revogado poucas horas depois. K e V podem chegar na mesma entrega,
mas a execucao continua em duas fases com selecao manual. T1 deixa de exigir kit completo, camera
passa a servir o invariante da familia e um unico VFX funcional passa a ser permitido. A relacao
K/V deixa de ser inferida por igualdade numerica e passa a vir de mapa explicito, permitindo varios
takes partirem do mesmo frame de corpo.
v20, 2026-10-06: ANEXOS minimos, a pedido do Luigi. Imagem: so o character sheet do avatar ativo, mais o
prompt, 4 variacoes 9:16. Video: so a imagem escolhida daquele K, mais o prompt de video, 1 resultado 9:16.
Acaba o frame do video modelo como anexo (Auraly v18) e qualquer outro anexo; os prompts descrevem por
escrito cenario, pose, camera e acao do original. O executor nao para por "frame modelo ausente".
