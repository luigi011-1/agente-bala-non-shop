# Validação técnica do aprendizado — 2026-10-11

- Comando: `.venv-operacao/bin/python -m unittest discover -s tests -p 'test_*plano*.py'`
- Resultado: **32 testes, todos passaram**.
- Cobertura: schema finito/estrito; Auraly sem herança pelo flag de estilo;
  proteção de ação; limites de fonte; tempo mínimo para render; velocidade e
  rampas; legenda curta sem união entre takes; permissões de silêncio unidas,
  contenção inteira e tolerância limitada; fades omitidos/zero explícito;
  offset musical; plano sem decisão musical conserva mixer padrão.
- FFmpeg real: execução da expressão de volume e mix de voz sintética
  silenciosa com música sintética curta. Duração conferida e energia presente
  depois do fim da fonte comprovaram looping. Isso não equivale a ouvir/emocionar.
- Smoke CLI: `editar.py --help` reconhece `--plano-editorial`.
- Whitespace: `git diff --check` sem achados.
- Todas as cinco métricas foram geradas pelo script comum e confrontadas com
  os arquivos legíveis nesta sessão; frames selecionados estão nas pastas V01–V05.

Não executado nesta fase: render comercial completo, revisão visual de um
vídeo comercial com os novos parâmetros, escuta perceptiva da música original
e do mix final. A fase é estudo técnico e visual; essas verificações continuam
necessárias na prática. Parecer independente fica em `REVISAO.json`.

Git: somente arquivos deste aprendizado e hunks novos do editor/router/skill
entram no commit. As alterações anteriores de outras frentes permanecem no
workspace. Vídeos originais e grades densas não são versionados.
