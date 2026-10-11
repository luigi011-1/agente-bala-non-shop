---
name: ambiente-mac-luigi
description: "Mac do Luigi (MacBook Air M2, 8 núcleos, 16 GB, disco de 228 GB quase cheio): o que já está instalado para /watch e edição, e as armadilhas de disco, git, memória e VS Code (2026-10-10)"
metadata:
  node_type: memory
  type: project
  originSessionId: c642df4f-f1fb-40d0-8d3c-047fd36bab5f
  modified: 2026-10-10T03:24:40.632Z
---

Em 2026-10-09/10 a operação passou a rodar também no Mac do Luigi, no VS Code, pasta
`~/agente bala non-shop/agente-bala-non-shop`. Até então rodava só na nuvem.

**Já instalado (não reinstalar):** Node 22 (`brew node@22`, no PATH pelo `~/.zprofile`), Python 3.12
(`brew`), `.venv-operacao` do `/watch` (`preparar_operacao.py`), `faster-whisper` no Python 3.9 do sistema
(o `editar.py` roda nele), `whisper-cpp` e `git-lfs` pelo brew, HyperFrames 0.8.143 com o Chrome de render,
modelos `ggml-small(.en)` em `~/.cache/whisper-cpp/models`. Repos da HeyGen em `~/ferramentas/hyperframes`
e `~/ferramentas/hyperframes-launch-video`; as 21 skills do HyperFrames ligadas em `~/.claude/skills`.

**Why:** cada item custou uma falha no meio do teste (watch sem Python 3.10+, clone sem git-lfs,
`preparar_hyperframes.sh` sem cmake, música apontando para `/mnt/project-files`). E o disco encheu duas
vezes no meio do trabalho.

**How to apply:**
- **Disco:** rodar `df -h /` antes de teste ou lote. Cada edição usa ~600 MB de trabalho e o `/watch` a 5 fps
  ~500 MB por vídeo: apagar as pastas de trabalho e os quadros depois de usar. Em 2026-10-09 o disco chegou a
  1,2 GB livres e a escrita falhou (`ENOSPC`) no meio de uma alteração do editor, que não foi gravada.
- **Não criar worktree por iniciativa:** cada um custa 3,3 GB. Criei três vazios, ocupando 9,9 GB, e tive que apagar.
- **VS Code:** as janelas abertas por mim ficam no MESMO processo desta sessão; não dá para fechar uma janela
  específica (sem permissão de acessibilidade) e matar o processo derruba a sessão. Pedir para o Luigi fechar.
- **Memória:** a memória viva deste checkout nasceu vazia; `restaurar_memoria.sh` resolve sem apagar nada.
  NUNCA rodar `sync_memoria.sh` com a memória viva vazia: o espelho do repo seria apagado.
- **rm com variável:** usar `"${VAR:?}"/...`; a checagem de segurança bloqueia `rm -rf $VAR/*`.
- **Paralelo:** no Mac, uma edição por vez; duas só ganham ~30%. Lote grande = uma sessão da nuvem por vídeo.
- **Pendente em 2026-10-10:** PR #58 (editor + regras) esperando o merge do Luigi; o checkout está no branch
  `claude/editor-conferencia-palavra`.

Lições do editor em [[edicao-licoes-teste]]. Ferramentas gerais em [[stack-ferramentas]].
