# Como deixar o agente do Flow confiavel (plano pratico)

## Por que ele se perde
1. A memoria dele tem ~295 linhas com historico (v14, v16, v18...). Modelo pequeno se afoga: regra velha e nova competem.
2. Ele nao tem ESTADO. Nao existe lugar onde esteja escrito "K03 falhou, V02 pronto". Sem estado, "gera de novo o que falhou" e impossivel, ele precisa adivinhar olhando a tela.
3. Nao existe protocolo de falha. A instrucao diz o que fazer quando da certo, quase nada sobre erro, fila cheia, imagem faltando, video bloqueado.

## Caminho A: instrucao curta + fila com estado (2 a 3 horas, sem risco, dentro das regras atuais)

### A1. Instrucao de 1 pagina (a v20)
Cortar para so o que ele executa: perfil, 4 imagens por K, 1 video por V, 9:16, modelo, INITIAL FRAME, lote de 7. Historico e justificativas ficam so no repo, nunca na memoria dele.

### A2. FILA.md por producao (o agente le e atualiza)
O gerar_pacote.py passa a gerar uma tabela, uma linha por codigo:

| Codigo | Tipo | Anexos | Status | Tentativas | Nota |
|---|---|---|---|---|---|
| K01 | imagem | sheet + frame | PENDENTE | 0 | |
| V01 | video | INITIAL FRAME K01 | PENDENTE | 0 | |

Status permitidos: PENDENTE, GERANDO, PRONTO, FALHOU, BLOQUEADO (moderacao), SELECIONADO (so o Luigi marca).
Regra do agente: depois de CADA geracao, reescrever a linha e colar a tabela no chat. Ele nunca decide o proximo passo de cabeca, so pega a primeira linha PENDENTE ou FALHOU.

### A3. Protocolo de falha (cola na memoria)
- Falha de geracao (erro, tile vazio, travou): FALHOU, tentativas+1, repetir o MESMO prompt e o MESMO anexo, ate 2 vezes.
- Falhou 3 vezes ou mensagem de moderacao: BLOQUEADO, parar esse codigo, avisar o Luigi e seguir para o proximo. Nunca reescrever o prompt.
- Comando do Luigi "refaz os que falharam": listar todas as linhas FALHOU e repetir, um por vez, sem tocar nos PRONTO.
- Perdeu o contexto / chat novo: Luigi cola a FILA.md atual e o agente retoma da primeira pendente.
- Antes de cada K: seletor em 4 e 9:16. Antes de cada V: modelo, 1 saida, 9:16, INITIAL FRAME.

### A4. Comandos curtos que o Luigi usa
`status` (mostra a tabela), `proximo` (gera o proximo), `refaz FALHOU`, `refaz K03`, `parar`.

### A5. Divisao de trabalho com o Claude
O Claude (aqui) monta pacote, FILA.md e validacao. O Luigi cola a FILA atualizada de volta no chat quando quiser que o Claude confira o que sobrou ou refaca prompt de algum bloqueado. O agente do Flow so executa.

## Caminho B: automacao de verdade (1 a 2 dias, so com o OK do Luigi)

Atencao: o CLAUDE.md registra que automacao de navegador e bridge foram DESCONTINUADOS em 2026-09-08. Isto reverteria essa decisao, entao so faco com ordem explicita.

Opcoes:
- B1. Script Playwright rodando no Mac do Luigi: abre o Chrome com o perfil ja logado no Flow, le a FILA.json, cola prompt, anexa imagem, marca 4 saidas, espera, baixa os resultados e atualiza o status sozinho. Funciona com o Flow que ele ja paga, mas quebra quando a interface do Flow muda, e precisa de ajuste fino de seletores (eu nao consigo testar o Flow daqui, entao seria iterativo com ele).
- B2. API do Google (Gemini API: Nano Banana para imagem, Veo para video) com um script Python que le a FILA.json. Mais estavel, sem navegador, retry automatico. Mas cobra por uso a parte, nao usa os creditos do Flow, e Omni Flash / Lower Priority talvez nao existam na API.
- B3. Meio termo: o script so prepara tudo (pasta por codigo com prompt.txt e anexo, renomeia downloads K01-1..4, confere se falta algum arquivo e gera a lista "faltam: K03-2, V05"). Nao automatiza o clique, mas resolve a parte de se perder.

## Recomendacao
Fazer A inteiro agora (e B3 junto, e barato). Rodar uma producao real com isso. Se ainda doer, decidir B1 ou B2 com base no que ainda trava.

## Ordem de execucao
1. Claude escreve a v20 curta de INSTRUCOES_AGENTE_FLOW.md + atualiza o checar_entrega (rejeita v19) e o gerar_pacote.py para gerar FILA.md/FILA.json.
2. Luigi cola a v20 no agente e testa com uma producao pequena (3 K + 3 V), provocando uma falha de proposito para ver o "refaz FALHOU".
3. Luigi devolve o que travou, Claude ajusta a instrucao.
4. So depois, decidir o Caminho B.
