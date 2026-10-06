# Como testar a instrução v20 do agente do Flow

1. Abra um agente do Flow NOVO e cole na memória o conteúdo inteiro de `INSTRUCAO_AGENTE_FLOW_v20.md` (é só o bloco, sem histórico).
2. Escolha uma produção pequena (ex.: Auraly cofre na cama, 3 K e 10 V) e peça a FILA ao Claude: ele roda `python gerar_fila.py <ENTREGA>.md`. Cole a FILA, o perfil e as âncoras no agente junto com os prompts K/V.
3. Provoque uma falha de propósito (cancele uma geração ou use um prompt que o Flow recuse) e mande `status`, depois `refaz FALHOU`. O esperado: ele marca FALHOU, repete o mesmo prompt até 2 vezes e, se continuar falhando, marca BLOQUEADO e segue sem reescrever.
4. Feche o chat no meio, abra outro, cole a última FILA e mande `proximo`. O esperado: ele retoma da primeira linha PENDENTE ou FALHOU. Me conte o que ele errou e eu ajusto antes do merge.
