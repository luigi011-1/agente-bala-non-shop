# Codex bootstrap obrigatorio - AGENTE NON-SHOP

Este arquivo deve ser lido antes de qualquer acao, analise ou resposta operacional neste projeto.
Ele apenas identifica o workflow e roteia o Codex para a fonte de verdade correspondente.

## Angulos comerciais oficiais

- ANGLE 1: nutraceutical / Natural Rems Sea Moss 16-in-1 Gummies (Amazon), desde 2026-10-02.
  Substitui a Korella Saffron, que fica como historico. Doutrina na memoria `angulo1-copy-seamoss`.
- ANGLE 2: FitWell / health-weight-loss app.
- ANGLE 3: Auraly app. Manifestation, soulmate, 11:11, 222, 333, 777, law of attraction,
  synchronicity, signs from the universe e romantic connection pertencem a esta oferta.

- ANGLE 4: Body Hacks For Men 40+ (FitWell, ebook de habitos, homens 40+). De volta ao intake em
  2026-10-02 para rodar na holistic.brandon (COACH); Dana, Jamie e Lynn seguem como PAR. Doutrina na
  memoria `angulo4-copy-bodyhacks`.

Nao existe um Angle 3 padrao de growth tarot. Oferta, promessa, mecanismo, nicho, CTA e linguagem
especifica dos quatro angulos nunca se misturam. Principios universais, como Metodo Puzzle, podem
atravessar os angulos.

## Roteamento obrigatorio do Angle 3 / Auraly

Se a producao for Angle 3 / Auraly, a cadeia operacional obrigatoria e somente:

```text
AGENTS.md
-> WORKFLOW_AURALY.md
-> producao/<producao_ativa>/CHECKPOINT.md
-> executar somente Next action
```

Antes de responder durante uma producao Auraly:

1. ler este `AGENTS.md`;
2. ler `WORKFLOW_AURALY.md`;
3. localizar a producao ativa pelo `CHECKPOINT.md` cujo estado nao seja `PRODUCTION_COMPLETE`;
4. ler o `CHECKPOINT.md` dessa producao;
5. identificar `Current stage` e `Next action`;
6. abrir somente o artefato indicado para essa etapa;
7. executar somente a proxima acao registrada;
8. atualizar o checkpoint imediatamente quando o estado mudar.

Se o checkpoint ja contem uma decisao, nao procurar a conversa antiga e nao reconstruir contexto.
Nao repetir scan completo do projeto, analise do video, copy, Metodo Puzzle, roteiro ou hooks ja
concluidos. Nao reler playbooks ou memorias irrelevantes.

As regras operacionais, estagios, comandos e formatos de resposta do Auraly ficam exclusivamente em
`WORKFLOW_AURALY.md`. Inteligencia de copy continua nos arquivos apontados por esse workflow e so e
consultada quando a etapa atual exigir.

## Intake Auraly sem checkpoint

Ao receber `.mp4` e anchors:

1. registrar o video e todas as anchors em uma nova pasta de producao;
2. criar `CHECKPOINT.md` imediatamente;
3. se Auraly/Angle 3 ja foi declarado, nao perguntar novamente;
4. se o angulo nao foi declarado, listar os arquivos recebidos e perguntar:

> Qual angulo desta producao?  
> 1 - Angle 1 (Sea Moss)  
> 2 - Angle 2 (FitWell)  
> 3 - Auraly  
> 4 - Angle 4 (Body Hacks)

Nao analisar nem adaptar antes da definicao do angulo.

## Outros angulos

Para Angle 1, Angle 2 e Angle 4, usar `CLAUDE.md` como roteador geral e consultar somente os arquivos
especificos do angulo e da etapa. `AGENT_WORKFLOW.md` e Auraly Studio (ambos arquivados em `_arquivo/` em 2026-09-22), bridge, extensao Chrome e
browser automation sao historicos, salvo pedido explicito do usuario.

## Regras permanentes

- COPY THE ENGINEERING, NOT THE WORDS.
- O Codex analisa, escreve e organiza; nao gera imagens e nao executa Google Flow.
- `AVATAR DONE != PRODUCTION DONE`.
- Estado operacional nunca depende apenas da conversa.
- Nunca criar uma segunda versao conflitante do workflow.
- Todo prompt de imagem e toda lista de ganchos, em qualquer angulo, passam por `GATE_VISUAL.md`
  (realismo anti cara de IA, heroi colado na lente, checklist de gancho visual).
- Video modelo de pessoa real (organico), em FitWell ou Auraly: `PERFIL_ORGANICO.md`. Copia literal
  de gancho visual, copy e estrutura; so o CTA muda conforme angulo e objetivo (Luigi, 2026-09-25).
- Nenhum K ou REF-P sem a ficha do frame e o placar com evidencia citada (`FICHA_FRAMES.md`,
  `GATE_VISUAL.md` Parte 6, Luigi 2026-09-25), em FitWell e Auraly. O linter reprova sem ela.
- Nenhum gancho, K, V, pacote ou prompt avulso e enviado sem o checklist de envio 100% aprovado
  (`GATE_VISUAL.md` Parte 5, memoria `checklist-envio-prompt`). Item reprovado impede o envio.

## Skills, especialistas e ferramentas da operacao (2026-10-06)

`OPERACAO_AGENTES.md` descreve as interfaces de execucao, sem substituir os roteadores acima.
As skills canonicas novas ficam em `.agents/skills/`: `operacao-bala`, `minerar-referencias`,
`watch`, `adaptar-conteudo` e `revisar-producao`. Cada uma declara entradas, entregas e limites.
`operacao/angulos.json` resolve os quatro produtos atuais e aponta suas doutrinas; nao e um workflow.

O Codex orquestra com dois especialistas (`bala-pesquisador`, `bala-produtor`) e um revisor
independente (`bala-revisor`, somente leitura), definidos em `.codex/agents/`. Antes de entregar
um resultado destas skills, o revisor le os artefatos finais e as fontes, sem escrever a producao.
Parecer tecnico nao substitui a aprovacao de roteiro do Luigi. Atualizar arquivos exige nova revisao.
Taskpacks e fingerprints registram escopo e versao; o CHECKPOINT continua sendo o estado canonico.

`scripts/dispatch.py` resolve a raiz real e usa `.venv-operacao`: `preflight`, `preparar`,
`watch`, `minerar` e `registrar-revisao`. `scripts/preparar_operacao.py` prepara o runtime e
registra as skills/agentes locais. Faster-Whisper transcreve; WhisperX e alinhamento opcional por
palavra, sem diarizacao por padrao. A extracao do /watch nao substitui ver os frames.
Crawlee coleta paginas publicas IG/FB limitadas e distingue filtros confirmados, desconhecidos
e bloqueios. Nem idioma nem primeira postagem provam pais ou criacao do perfil.

## Regras de trabalho do projeto (espelho do projeto Claude, 2026-10-06)

Estas regras vieram do projeto no claude.ai (instrucoes + memoria do projeto) e valem para o Codex
tambem. Onde houver conflito, `WORKFLOW_AURALY.md`, `GATE_VISUAL.md` e `producao/_flow/INSTRUCOES_AGENTE_FLOW.md`
continuam sendo a fonte de verdade de cada tema. Skills do Luigi em `.claude/skills/`
(`contexto-operacao-luigi`, `avatar-realista`, `gancho-verbal`, `produzir`, `watch`): ler o `SKILL.md`
quando o assunto pedir.

### Como o Luigi trabalha
- Fala portugues. Quer tudo resolvido rapido e sozinho; so chamar quando a mao dele for realmente necessaria.
- **Aprovacao de roteiro e a trava de qualidade:** apresentar sempre o roteiro final COMPLETO numa tabela
  bilingue (`take | English | Portugues`), com todos os takes, inclusive os inserts mudos. Esperar a
  aprovacao ou os ajustes dele antes de montar o pacote.
- Lote: quando ele manda varios videos modelo, produzir um por video, em paralelo. Formato combinado:
  `/watch lote`, um bloco numerado por video com `video` (anexo), `conta`, `angulo`, `tipo`
  (venda/growth), `avatar` (anexo ou "o de sempre da conta"), `obs`. Campos comuns vao uma vez em
  `todos: ...`. Videos entram como arquivo; caminho local do Mac nao e legivel na nuvem.
- Em lote, juntar o que esta pendente de aprovacao numa unica mensagem numerada por video. Conferir
  conflitos entre videos da mesma conta: rotacao de rota argumentativa, frases repetidas, mesmo avatar.
- Perguntar ao Luigi antes de dar merge em PR.
- Nao pedir postagens, datas nem metricas por video e nao cobrar o registro em `controle/resultados.json`
  (decisao 2026-10-05). "O video X performou" dito por ele e o gatilho da rodada de variacao.
- Copy de referencia (2026-10-06): quando ele cola a transcricao de um anuncio escalado "como base",
  extrair as dores, o mecanismo e os nomes fortes e reescrever para o NOSSO formato e produto. Nunca
  copiar fala nem gancho literal da referencia.

### Contas, CTA e organico x pago
- Decisao 2026-10-05: o CTA manda para o link da LEGENDA, nao para comentario fixado, em todas as contas,
  ate o Luigi dizer o contrario. Vale so para posts ORGANICOS.
- Decisao 2026-10-06: anuncio PAGO (trafego pago) termina com CTA apontando para o botao do anuncio
  (ex.: "Tap below to get your personalized FityWell plan 👇"). Sem CTA de legenda e sem "comment".
- Auraly e sempre o Angulo 3. Ate 2026-10-05 nenhum video Auraly viralizou; hipotese do Luigi: o avatar
  nao casou com as copies validadas. Considerar troca/ajuste de avatar (`congruencia-matriz`) antes de
  variar ganchos; nao abrir rodada de variacao.
- Auraly venda dinheiro/prosperidade/fortuna (2026-10-06): promessa agressiva e consequencia forte se os
  selos nao forem seguidos, mas agressivo DENTRO da logica do selo; sem valor em dolar garantido e sem
  ameaca de doenca, morte ou acidente. Padrao organico (CTA para Stories) ate ele dizer que e pago.

### Regra de anexos do Flow (Luigi, 2026-10-06), todas as producoes
- Prompt de IMAGEM: ele anexa SO o character sheet do avatar e cola o prompt. 4 variacoes, 9:16. Sem
  frame do video modelo, sem nenhuma outra imagem.
- Prompt de VIDEO: ele anexa SO a imagem escolhida para a cena e cola o prompt. 1 variacao, 9:16.
- Logo todo prompt e autossuficiente: cena, pose e acao do original descritas por escrito.
- Character sheets Auraly: Avery Knox = mulher loira ~60, camisa branca, jeans, joias turquesa; Devon
  Price = mulher de cabelo grisalho raspado, argolas, camisa jeans; Jordan Vale = homem de barba
  grisalha, colete de couro preto, tatuagens.
- Avatares novos (2026-10-07, sheets aprovados em `producao/_ancoras/character_sheets/`, prompts em `producao/auraly_avatares_rico_careca/`; ficam no lugar de Devon Price e Jordan Vale): Gordon Ashby = homem ~68, cabelo prateado, oculos de aro dourado, smoking creme com gravata-borboleta (rico); Celeste Marlow = mulher ~50 careca, blazer de renda creme, pulseira rose-gold, colar de coracao.
- Regra v19 (PR #26, ja no main): sempre 4 imagens por K e 1 video por V, sempre 9:16. Texto canonico
  em `producao/_flow/INSTRUCOES_AGENTE_FLOW.md`. Menu real do Flow: imagem "Nano Banana 2.1"; video
  "Veo 3.1 - Lite" (Auraly) e "Omni 1.1 Flash" (classico). Nao existe "Lower Priority".
- Nao propor robo/automacao de UI do Flow: o Luigi abandonou em 2026-10-06 e removeu do Mac (o codigo
  do PR #27 nao entra).

### Bloco do agente Flow, toda producao (Luigi, 2026-10-06, feedback forte)
- TODA producao entrega, no chat, o bloco do agente Flow pronto para colar (arquivo anexo + texto em
  bloco de codigo).
- O bloco cobre SO a producao atual (ele abre um projeto Flow novo por producao). Nunca incluir outras
  contas, angulos, perfis ou historico (nada de short form, movie style, Natural Rems, FitWell, tabelas
  de perfil): conteudo demais fez o agente "ficar burro". Modelo Auraly atual:
  `flow_agente/AGENTE_FLOW_AURALY_ATUAL.md`.
- Dizer de forma objetiva: imagem = character sheet + prompt, 4 variacoes 9:16, ele apaga 3 e fica com
  1 escolhida a mao; video = so a imagem escolhida + prompt, 1 variacao 9:16, nada mais anexado.
- Falha, censura ou prompt bloqueado: tentar de novo com o MESMO prompt EXATO (nunca editar) e insistir
  ate gerar. Cobrir variaveis do mundo real (formato errado, menos variacoes, relato de status).

### FitWell em trafego pago (2026-10-06)
- Publico 40+, homens e mulheres; mulheres mais velhas fortes, definidas mas femininas.
- Metodo: "puzzle"/Genjutsu video-para-video no Omni Flash: modelo mp4 + imagem do avatar posta na cena
  original + prompt que copia movimento, tempo e enquadramento e troca so a pessoa.
- Audio removido dos videos modelo (copyright no Flow): todo prompt de video diz que o original e o
  resultado sao SEM audio.
- Telas de celular: app generico de treino/comida, nunca UI nem logo da FityWell. Texto de tela entra no
  CapCut, nunca no video gerado.
- Nome do plano na copy (substitui "Metabolic Reset"): **Belly Melt Plan** ("Lean Again Plan" foi
  rejeitado). Dores: mesmo publico do Natural Rems, reaproveitar as dores. FityWell e um APP: nunca
  vender como nutra, ebook ou suplemento.
- Copy UGC enxuta, sem enchimento, frase padrao de UGC americano. Realismo acima de exagero nos prompts
  de imagem (imagem obesa exagerada foi rejeitada como irreal).
- Formato validado: `producao/fitywell_mae_filha/` (filha em green screen conta a virada da mae 40+;
  gancho com palavrao, foto "antes" obesa atras, insert de treino, selfie com dor + plano personalizado
  + CTA Learn More). Tambem em `producao/fitywell_coach_antes_depois/`, `fitywell_treino_halteres/`,
  `fitywell_ads_casa/`.

### Ambiente
- Cloud: ambiente "Operacao bala", rede liberada; hook SessionStart instala faster-whisper, Pillow, av
  e Whisper small.en. Videos modelo (`*.mp4`) ficam fora do git (`.gitignore`).
