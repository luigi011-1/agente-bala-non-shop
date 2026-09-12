# Codex bootstrap obrigatorio - AGENTE NON-SHOP

Este arquivo deve ser lido antes de qualquer acao, analise ou resposta operacional neste projeto.
Ele apenas identifica o workflow e roteia o Codex para a fonte de verdade correspondente.

## Angulos comerciais oficiais

- ANGLE 1: nutraceutical / Korella Saffron.
- ANGLE 2: FitWell / health-weight-loss app.
- ANGLE 3: Auraly app. Manifestation, soulmate, 11:11, 222, 333, 777, law of attraction,
  synchronicity, signs from the universe e romantic connection pertencem a esta oferta.

Nao existe um Angle 3 padrao de growth tarot. Oferta, promessa, mecanismo, nicho, CTA e linguagem
especifica dos tres angulos nunca se misturam. Principios universais, como Metodo Puzzle, podem
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
> 1 - Angle 1  
> 2 - Angle 2  
> 3 - Auraly

Nao analisar nem adaptar antes da definicao do angulo.

## Outros angulos

Para Angle 1 e Angle 2, usar `CLAUDE.md` como roteador geral e consultar somente os arquivos
especificos do angulo e da etapa. `AGENT_WORKFLOW.md`, Auraly Studio, bridge, extensao Chrome e
browser automation sao historicos, salvo pedido explicito do usuario.

## Regras permanentes

- COPY THE ENGINEERING, NOT THE WORDS.
- O Codex analisa, escreve e organiza; nao gera imagens e nao executa Google Flow.
- `AVATAR DONE != PRODUCTION DONE`.
- Estado operacional nunca depende apenas da conversa.
- Nunca criar uma segunda versao conflitante do workflow.
