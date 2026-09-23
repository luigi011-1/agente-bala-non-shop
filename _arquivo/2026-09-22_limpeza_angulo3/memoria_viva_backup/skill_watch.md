---
name: skill-watch
description: "Skill /watch — pipeline que \"assiste\" um .mp4 de referência (cenas + hook denso + timeline densa + transcrição de áudio Whisper) e entrega decomposição beat a beat. Substitui a extração esparsa de frames do processo antigo. Local, dependências e uso."
metadata: 
  node_type: memory
  type: project
  originSessionId: 246ef273-2f24-4b5d-8e5e-51929be93030
  modified: 2026-08-12T21:14:10.203Z
---

# Skill /watch (decomposição aprimorada de vídeo)

Criada em 2026-08-12 para aprimorar a **Fase 2 (Decomposição)** de [[processo-7-fases]]. Resolve os erros do método antigo (frames esparsos + miniaturas minúsculas perdiam reveals que acontecem DENTRO de um take, ex.: cristais derretendo e mostrando os gomos da barriga).

## O que ela faz
Pipeline único que, a partir de um `.mp4`:
1. Sonda o vídeo (ffprobe).
2. Extrai 1 frame por **corte de cena** (mapa de takes).
3. Extrai a **timeline inteira densa a 0,2s (5fps) no vídeo COMPLETO** ← pega reveals dentro de qualquer take (hook, corpo E cta). Decisão do usuário (2026-08-12): densidade uniforme, não só no hook.
4. **Transcreve o áudio** com faster-whisper (timestamps por segmento).
5. Gera **grades legíveis** (Pillow, tiles grandes com rótulo de timestamp; timeline em folhas de 20).
6. Escreve `manifest.json` + `transcript.txt/json`.

Saída em `<pasta_do_video>/<nome>_watch/`.

## Local
`C:\Users\luigi\Desktop\AGENTE NON-SHOP\.claude\skills\watch\`
- `SKILL.md` — instruções que eu sigo (inclui a disciplina: ler grades → zoom full-res nos reveals → decompor beat a beat → confirmar herói do hook antes de produzir).
- `scripts\watch_pipeline.py` — o pipeline.
- `scripts\run_watch.ps1` — wrapper que recarrega o PATH e chama o Python.

## Como rodar
```
powershell -File ".claude/skills/watch/scripts/run_watch.ps1" -Video "CAMINHO.mp4"
```
Opções via `-Extra`: `--model medium.en` (transcrição +precisa/+lenta), `--hook-seconds`, `--timeline-fps`, `--scene-threshold`, `--no-audio`.

## Dependências instaladas nesta máquina (2026-08-12)
- Python 3.12.10 → `C:\Users\luigi\AppData\Local\Programs\Python\Python312\python.exe`
- ffmpeg/ffprobe 9.0 (Gyan, via winget) → `%LOCALAPPDATA%\Microsoft\WinGet\Links\`
- faster-whisper 1.2.1 + modelo `small.en` (cache HF)
- Pillow 12.3

## Limitações honestas
- Não é "assistir" contínuo com olhos/ouvidos — é amostragem densa de frames + transcrição de áudio. É o máximo real possível, e mata os erros do método antigo.
- ffmpeg 9.0 removeu `-vsync` (usar `-fps_mode`). PATH precisa ser recarregado em shell novo (o wrapper faz isso).

## Regra de uso
A transcrição é **conferência**, não substitui a análise visual do herói do hook. Sempre confirmar herói/reveal com o usuário se houver ambiguidade ([[erros-recorrentes]]).
