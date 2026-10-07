# Validação da implementação da Operação Bala

Verificada em 2026-10-06/07, macOS Apple Silicon, Python 3.12.14. Base: origin/main 9954cdc; implementação em codex/operacao-skills-agentes.

## Cobertura das seis frentes

| Frente solicitada | Entrega implementada | Evidência |
|---|---|---|
| Skills com funções, entradas, entregas e limites | Cinco skills canônicas em .agents/skills; contratos atualizados nas quatro skills legadas | 10 SKILL.md passaram no validador; cinco interfaces YAML; catálogo da sessão reconheceu as cinco skills pessoais |
| Revisor independente | Perfil bala-revisor em leitura, parecer JSON e registro vinculado aos arquivos revisados | Cenários de estado/CTA e regressões de fonte/mídia alterada, revisor incorreto e parecer conflitante |
| Orquestrador + poucos especialistas | Skill operacao-bala, taskpacks, bala-pesquisador, bala-produtor e bala-revisor | TOML válidos, fontes mínimas por ângulo, roteamento preservado; delegação disponível no Codex |
| Faster-Whisper /watch | Fonte única, CPU int8, timeline/cortes, idioma e áudio explícitos, estados e reruns | FFmpeg real em fixtures; ASR real small.en, dois segmentos corretos no teste integrado |
| WhisperX | Alinhamento opcional da transcrição existente, sem diarização | Execução real: 16/16 palavras com start/end; zero palavras sem tempo |
| Crawlee | Coleta limitada, domínios IG/FB, redirects controlados, provas por campo, relatório de lacunas/bloqueios | Crawlee real em HTTP local; teste público retornou BLOCKED com motivos, sem aprovações fictícias |

## Validações executadas

- `python3 scripts/dispatch.py preflight`: dependências presentes, versões verificadas.
- `.venv-operacao/bin/python -m pip check`: nenhuma dependência quebrada.
- `.venv-operacao/bin/python -m unittest discover -s tests -q`: **109 testes, OK**; 67 existiam antes da implementação.
- 10 skills no quick_validate; YAML das cinco interfaces e TOML dos três perfis válidos.
- `bash -n` e execução SO_DEPS do hook de nuvem; wrapper pessoal por symlink rodou fora do checkout.
- `git diff --check`: sem erros de whitespace.
- Teste comportamental independente: mineração Sea Moss descobre seeds sem Manus; Auraly WAITING_SCRIPT_APPROVAL aguarda roteiro; FitWell pago mantém APP, Belly Melt Plan e CTA de botão com exceção video-para-video.

## Execução integrada de áudio

Vídeo sintético local de 6,47483 s: padrão de cores em movimento e voz do sistema, sem conteúdo comercial. Extração a 5 fps gerou 32 frames e duas grades de timeline. As grades e a de cenas foram abertas pelos revisores.

Texto transcrito:

> Today we are testing a simple video workflow. Listen carefully and check every word before publishing.

O /watch retornou COMPLETE em 8,302 s no teste com modelos em cache; Faster-Whisper transcreveu os dois segmentos e WhisperX alinhou as 16 palavras, sem lacunas. Esse tempo é uma medição desta amostra, não uma promessa de desempenho para outros vídeos. O manifesto continua marcando a interpretação visual de um criativo como pendente: extração concluída não significa análise comercial concluída.

## Coleta pública e limites verificados

Seeds oficiais: instagram.com/instagram e facebook.com/facebook. Crawlee respeitou robots e retornou **BLOCKED**, exit 2, zero aprovados e motivos por URL. Isso comprova o tratamento do bloqueio, não acesso irrestrito às plataformas ou uma mineração diária com resultados.

A busca web do pesquisador descobre candidatos e provas públicas. País EUA, criação em até 30 dias e IA exclusiva continuam desconhecidos quando não há evidência suficiente. Não usar inglês, primeira postagem ou bio AI como prova. Toda aprovação exige os critérios comprovados; nenhuma condição é relaxada em silêncio.

## Correções encontradas durante os testes

- PyAV 19 removeu metadata_errors usado por Faster-Whisper 1.2.1: fixado PyAV 18.0.0.
- WhisperX retornava escalares NumPy não serializáveis: normalização numérica, null para tempos ausentes e regressão adicionada.
- Parecer podia sobreviver à alteração de imagem: fingerprints agora incluem mídia e as fontes relevantes; --artifact cobre saídas externas à produção.
- JSON-LD de vídeos recomendados podia contaminar métricas: exige identidade do vídeo; fallback canônico só para único objeto principal comprovado.
- Cache compartilhado de RequestQueue escondia reruns: fila única por execução.

## Instalação e reprodução

Runtime local `.venv-operacao`; cinco symlinks pessoais em ~/.agents/skills e três perfis em ~/.codex/agents. A sessão reconheceu operacao-bala, minerar-referencias, adaptar-conteudo, revisar-producao e watch. Modelos small.en e alinhador inglês estão no cache local. No Mac arm64/Python 3.12, o instalador usa o lock resolvido; em outro host instala dependências diretas.

Reprodução e uso: `OPERACAO_AGENTES.md`. Evidências brutas estão em operacao/execucoes/validacao-2026-10-06/ (fora do git, incluindo mídia sintética). O taskpack final e o parecer independente são salvos em operacao/execucoes/revisao-implantacao/.

Não foram executados wrappers PowerShell/Windows nem testes em host Linux. Aprovação de roteiro, seleção e Flow continuam nas regras canônicas. Esta implementação não cria automação diária nem ativa Manus.

## Documentação primária consultada

- [Skills e descoberta local do Codex](https://learn.chatgpt.com/docs/build-skills)
- [Perfis de subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper)
- [WhisperX](https://github.com/m-bain/whisperX)
- [Crawlee Python](https://crawlee.dev/python/docs/quick-start)
- [PyAV 19: opções removidas](https://github.com/PyAV-Org/PyAV/releases/tag/v19.0.0)
