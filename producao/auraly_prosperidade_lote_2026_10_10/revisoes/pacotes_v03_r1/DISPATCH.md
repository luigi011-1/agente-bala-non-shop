# Execução 521f6abb-5123-4f27-8c68-f86fe10eb882

Ângulo: Auraly APP
Tarefa: revisar
Especialista: bala-revisor
Revisor independente: bala-revisor

Leia AGENTS.md e siga o roteador canônico. Abra somente os artefatos necessários à etapa.
Current stage: IMAGE_PROMPTS
Next action: Montar pacote K/V de Avery Knox deste modelo a partir do roteiro e hook aprovados; depois Devon Price e Jordan Vale, preservando a fila do intake.

Use as ferramentas do Codex para delegar; este CLI prepara contexto, não chama um modelo.
Depois da autoria, prepare TASK novo para revisar a versão final. O revisor recebe as fontes e
a entrega, avalia os fatos e retorna JSON conforme o schema, sem editar os arquivos.
O orquestrador registra o JSON com registrar-revisao e confere a cobertura antes de entregar.
Se houver falha, corrigir e revisar novamente os arquivos finais; jamais reutilizar parecer stale.
A aprovação de roteiro permanece com Luigi. Nenhuma ação no Flow é executada por este CLI.
