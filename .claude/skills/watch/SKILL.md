---
name: watch
description: Compatibilidade do /watch no Claude; decompor vídeo por frames densos, Faster-Whisper e WhisperX opcional para os quatro ângulos. Use em /watch ou /watch lote e leia a skill canônica em .agents/skills/watch/SKILL.md.
---

# /watch — entrada de compatibilidade

Abra e siga integralmente `.agents/skills/watch/SKILL.md`, fonte única do contrato e dos passos. Leia `AGENTS.md` e o workflow do ângulo antes de executar. Os scripts desta pasta delegam à implementação canônica; os comandos existentes continuam válidos:

```bash
bash .claude/skills/watch/scripts/run_watch.sh "VIDEO.mp4" [opcoes]
```

Não manter regras operacionais nem transcrição paralelas nesta cópia. O `/watch` prepara evidências; a leitura visual continua com o analista, conforme o contrato canônico. Aprovação de roteiro, gates visuais e execução manual do Flow permanecem no workflow do ângulo.
