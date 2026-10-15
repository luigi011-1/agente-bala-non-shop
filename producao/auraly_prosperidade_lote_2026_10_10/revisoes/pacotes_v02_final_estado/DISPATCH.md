# Execução 6d20129f-d9e9-411e-bbad-a7a501f8e504

Ângulo: Auraly APP
Tarefa: revisar
Especialista: bala-revisor
Revisor independente: bala-revisor

Leia AGENTS.md e siga o roteador canônico. Abra somente os artefatos necessários à etapa.
Current stage: PRODUCTION_COMPLETE
Next action: Receber takes do Flow nas pastas do lote e executar edicao sequencial na ordem V01/Avery, Devon, Jordan; depois V02 e V03. Jordan exige transcricao em espanhol.

Use as ferramentas do Codex para delegar; este CLI prepara contexto, não chama um modelo.
Depois da autoria, prepare TASK novo para revisar a versão final. O revisor recebe as fontes e
a entrega, avalia os fatos e retorna JSON conforme o schema, sem editar os arquivos.
O orquestrador registra o JSON com registrar-revisao e confere a cobertura antes de entregar.
Se houver falha, corrigir e revisar novamente os arquivos finais; jamais reutilizar parecer stale.
A aprovação de roteiro permanece com Luigi. Nenhuma ação no Flow é executada por este CLI.
