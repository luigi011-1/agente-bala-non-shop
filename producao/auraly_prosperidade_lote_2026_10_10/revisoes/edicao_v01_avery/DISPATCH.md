# Execução d783597c-485e-4db9-9f97-9c0eea9a7bf0

Ângulo: Auraly APP
Tarefa: revisar
Especialista: bala-revisor
Revisor independente: bala-revisor

Leia AGENTS.md e siga o roteador canônico. Abra somente os artefatos necessários à etapa.
Current stage: não registrado
Next action: registrar entradas e estado antes de adaptar

Use as ferramentas do Codex para delegar; este CLI prepara contexto, não chama um modelo.
Depois da autoria, prepare TASK novo para revisar a versão final. O revisor recebe as fontes e
a entrega, avalia os fatos e retorna JSON conforme o schema, sem editar os arquivos.
O orquestrador registra o JSON com registrar-revisao e confere a cobertura antes de entregar.
Se houver falha, corrigir e revisar novamente os arquivos finais; jamais reutilizar parecer stale.
A aprovação de roteiro permanece com Luigi. Nenhuma ação no Flow é executada por este CLI.
