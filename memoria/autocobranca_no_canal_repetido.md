---
name: autocobranca-no-canal-repetido
description: "Correcao do Luigi em 2026-08-29: nao devolver ao usuario a tarefa de me policiar. Regra que compete com uma instrucao repetida a cada turno so vence se estiver no mesmo canal repetido, nunca num arquivo lido uma vez por sessao."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 743d3401-da9c-4753-ba54-509bfe4c9d13
  modified: 2026-08-29T03:23:11.892Z
---

# Autocobranca vai no canal repetido, nao no pedido ao Luigi

**2026-08-29.** Eu tinha escrito a precedencia PORTAO > grafo > lembranca no `CLAUDE.md` e depois
pedi ao Luigi: *"vale voce me cobrar isso na primeira producao, se eu citar uma regra sem ter
aberto o arquivo"*. Ele respondeu: **"isso e algo que voce mesmo pode se cobrar automaticamente"**.

Ele esta certo, e o erro tem nome: e o mesmo que o `CLAUDE.md` ja descreve nos PORTOES DE CONSULTA,
*"eu nao abro documento sozinho"*. Transferir a vigilancia para o usuario e a versao social de
depender da minha lembranca.

**Why:** o nudge do graphify entra a **cada busca**, e o `CLAUDE.md` entra **uma vez por sessao**.
Volume vence conteudo. Uma regra correta num canal de baixa frequencia perde para uma regra
concorrente num canal de alta frequencia, por mais bem escrita que seja.

**How to apply:** quando uma regra nova precisar competir com algo repetido, colocar a regra **no
mesmo canal repetido**. Aqui: a autocobranca foi para o texto do `.claude/hooks/gabarito_hook.py`
(UserPromptSubmit), que injeta em todo prompt de producao, e nao so para o `CLAUDE.md`.
O criterio concreto que ficou no hook: *antes de citar regra de portao, eu abri esse arquivo NESTA
sessao ou estou repetindo o resumo do grafo?* Se foi o grafo, a resposta nao sai.

Corolario: **nunca terminar uma entrega pedindo ao Luigi que fiscalize um comportamento meu.**
Se da para instrumentar, instrumentar. Ver [[workflow-entrega-gabarito]] e [[grafo-pendencia-semantica]].

## Erro colateral da mesma sessao: afirmar sem medir direito

No mesmo dia eu quase removi o guard `Read|Glob` do graphify dizendo que era "peso morto, efeito
zero", baseado em um teste que deu silencio em tres arquivos. O guard **nao** e inerte: ele fica
calado quando o grafo esta em dia para aquele arquivo e dispara quando esta **defasado**, dizendo
*"may be STALE for this file... Reading the file directly is fine"*, que e informacao util e nao
desencoraja leitura. O classificador barrou a remocao antes que eu degradasse a configuracao.
**Silencio em N amostras nao e prova de inercia.** Ver [[erros-recorrentes]].
