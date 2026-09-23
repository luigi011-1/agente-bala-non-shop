# Instrucoes do agente executor do Google Flow AI

Versao 12, 2026-09-22. Contrato de execucao, subordinado ao roteador de cada oferta.
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
v12, 2026-09-22: roster Auraly reduzido a Walt, Darlene e Lorraine. A fingerprint sai: a referencia
e a anchor em cena real, com instrucao de usar so a identidade quando o K pede cenario novo. A
excecao dos avatares de luxo (v9) foi removida junto com eles.
v10, 2026-09-20: sincronizado com o portfolio Auraly 4/3/3, revogado poucas horas depois. K e V podem chegar na mesma entrega,
mas a execucao continua em duas fases com selecao manual. T1 deixa de exigir kit completo, camera
passa a servir o invariante da familia e um unico VFX funcional passa a ser permitido. A relacao
K/V deixa de ser inferida por igualdade numerica e passa a vir de mapa explicito, permitindo varios
takes partirem do mesmo frame de corpo.
