# Execução 36c0ba7e-e912-4488-b59e-57ecfe37803c

Ângulo: FitWell / FityWell APP
Tarefa: adaptar
Especialista: bala-produtor
Revisor independente: bala-revisor

Leia AGENTS.md e siga o roteador canônico. Abra somente os artefatos necessários à etapa.
Current stage: ANALYSIS_IN_PROGRESS
Next action: Decompor referência com /watch, classificar origem e preparar roteiro completo para aprovação.

Use as ferramentas do Codex para delegar; este CLI prepara contexto, não chama um modelo.
Depois da autoria, prepare TASK novo para revisar a versão final. O revisor recebe as fontes e
a entrega, avalia os fatos e retorna JSON conforme o schema, sem editar os arquivos.
O orquestrador registra o JSON com registrar-revisao e confere a cobertura antes de entregar.
Se houver falha, corrigir e revisar novamente os arquivos finais; jamais reutilizar parecer stale.
A aprovação de roteiro permanece com Luigi. Nenhuma ação no Flow é executada por este CLI.
