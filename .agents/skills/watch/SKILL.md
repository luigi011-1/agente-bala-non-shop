---
name: watch
description: Decompor vídeos de referência para Sea Moss, FitWell, Auraly e Body Hacks com frames densos, transcrição Faster-Whisper e alinhamento por palavra WhisperX quando necessário. Use em /watch, /watch lote ou ao receber vídeo para análise ou adaptação. Extrair evidências não equivale a concluir a leitura visual nem autoriza produção sem os gates do ângulo.
---

# /watch — evidências e decomposição de vídeo

Leia `AGENTS.md` no checkout antes de trabalhar. Esta skill implementa a decomposição, sem substituir os workflows comerciais. Auraly segue `WORKFLOW_AURALY.md -> CHECKPOINT.md -> Next action`; os demais ângulos seguem o roteamento de `CLAUDE.md`. Reuse decisões já registradas e leia somente as fontes da etapa.

## Contrato

| Campo | Conteúdo |
|---|---|
| Função | Extrair cenas, timeline completa, fala e, quando necessário, palavras alinhadas; depois construir a decomposição a partir das imagens realmente abertas. |
| Entradas | Arquivo de vídeo legível no ambiente; ângulo já definido ou recuperado do checkpoint; origem IA/pessoa real/inconclusiva; objetivo e conta quando a produção exigir. Roteiro original, se já fornecido, serve de conferência. |
| Entregas | `manifest.json`, frames, grades, `audio/transcript.txt` e `.json` quando houve transcrição; `audio/alignment.json` e `words.json` quando WhisperX foi solicitado e executado; tabela beat a beat com evidências visuais. |
| Limites | Não gerar mídia, abrir Flow ou alterar oferta; não inventar fala em vídeo mudo; não afirmar ter assistido antes de abrir todas as grades; não montar pacote antes da aprovação do roteiro prevista no workflow. |

Se o ângulo necessário à produção não estiver disponível, faça o intake de `AGENTS.md` uma única vez. Antes da decomposição consulte os portões e referências indicados pelo roteador, inclusive biblioteca de vídeos/erros recorrentes quando aplicável. Gates de copy entram na etapa de copy, conforme o workflow, sem carregar toda a memória por padrão.

## Executar

Com o checkout como diretório de trabalho:

```bash
bash .agents/skills/watch/scripts/run_watch.sh "VIDEO.mp4"
# Alinhamento por palavras quando o tempo exato da fala for necessário:
bash .agents/skills/watch/scripts/run_watch.sh "VIDEO.mp4" --alignment whisperx
# Referência paga explicitamente muda:
bash .agents/skills/watch/scripts/run_watch.sh "VIDEO.mp4" --no-audio
```

O wrapper prioriza `.venv-operacao`, preparado por `scripts/preparar_operacao.py`. A skill pessoal aponta por symlink para este checkout; resolva esse caminho para encontrar a raiz. A entrada comum também funciona de outro diretório: `python3 "CAMINHO_CHECKOUT/scripts/dispatch.py" watch --video "VIDEO.mp4"`. Não presuma dependências instaladas em uma máquina nova. Compatibilidade: comandos antigos em `.claude/skills/watch/scripts/` delegam à mesma implementação.

Windows:

```powershell
powershell -File .agents/skills/watch/scripts/run_watch.ps1 -Video "VIDEO.mp4" -PipelineArgs @("--alignment", "whisperx")
```

Padrões: Faster-Whisper `small.en`, inglês, CPU/int8, 4 threads, até 4 tarefas de grades, 5 fps em todo o vídeo. A extração de cenas/timeline usa uma decodificação; transcrição e grades podem executar em paralelo. Mac não exige CUDA. WhisperX reutiliza essa transcrição para alinhamento, sem diarização e sem token por padrão.

Opções úteis:

- `--language auto --model small`: detectar idioma com modelo multilíngue; para português use `--language pt --model small`. Modelos `.en` são só inglês.
- `--timeline-fps 10`: aumentar a densidade; `--scene-threshold 0.15`: detectar cortes mais sutis.
- `--word-timestamps`: palavras do Faster-Whisper sem carregar WhisperX; para alinhamento dedicado use `--alignment whisperx`.
- `--allow-no-audio`: ausência de áudio é esperada, mas transcrever se uma faixa existir. `--no-audio` pula a fala por decisão explícita.
- `--outdir DIR`: pasta exclusiva das evidências; não pode conter o arquivo de entrada. Artefatos prévios do próprio `/watch` são substituídos, arquivos desconhecidos são protegidos.
- `--max-frames N` e `--command-timeout SEGUNDOS`: limites ajustáveis. Exceder o orçamento gera falha explícita; nunca cortar silenciosamente o vídeo.

## Conferir o processamento

Sempre abra `manifest.json` da execução atual, inclusive quando o comando sair com erro.

| Estado | Ação |
|---|---|
| `COMPLETE` / exit 0 | Extração solicitada concluída. A leitura visual continua pendente. |
| `PARTIAL` / exit 2 | Há evidências úteis, mas transcrição/alinhamento/áudio esperado está incompleto. Leia `errors`, repare quando possível e reporte o que ficou pendente. |
| `FAILED` / exit 2 | Não apresentar a decomposição como completa; identificar e resolver a causa. |
| `RUNNING` | Execução em andamento ou interrompida; nenhum artefato autoriza declarar sucesso. |

`analysis_status=PENDING_VISUAL_REVIEW` e `coverage.visual_review_performed=false` são deliberados: um script não certifica uma leitura visual. `NO_SPEECH_DETECTED` significa que o modelo não detectou fala, não prova que não existe. Se a imagem ou roteiro indicar fala, confira novamente. `SKIPPED_BY_REQUEST` e `NO_AUDIO_STREAM` não geram texto inventado. WhisperX preserva palavras sem tempo e declara `PARTIAL`; nunca completar lacunas com zero ou copiar o tempo da palavra vizinha. A primeira execução pode baixar modelos públicos e NLTK; falha de rede aparece no manifest.

## Ler e decompor

O analista que assina a decomposição precisa abrir pessoalmente as grades e os frames críticos. O orquestrador pode delegar a análise inteira ao especialista; não usar resumo de outro agente como prova de que o vídeo foi visto.

1. Abra transcrição e todas as grades de cenas em lote; não presumir que o original é IA.
2. Abra as grades da timeline em ordem, em lotes de até 6 imagens. As duas primeiras grades cobrem aproximadamente os primeiros 8 segundos com os padrões atuais; depois cubra corpo e CTA completos.
3. Abra os frames individuais em resolução cheia para hook, mudanças dentro de take, reveals e props. Timestamps da timeline são a grade de amostragem do filtro FPS; os das cenas vêm do FFmpeg.
4. Se um instante estiver entre amostras, extraia uma janela de zoom com FFmpeg em outra pasta e abra essas imagens. Não concluir ação pelo retrato parado.
5. Construa a tabela abaixo e cite arquivos/timestamps efetivamente inspecionados. Se o WhisperX estiver disponível, palavras alinhadas ajudam a relacionar fala e ação; não substituem a imagem.

| Timestamp | Esqueleto visual | Pessoas | Props | Fala literal ou mudo | HOOK/MECANISMO/RECEITA/PROTOCOLO/RESULTADO/PROVA/CTA | TALKING/B-ROLL | Ação e mudança |
|---|---|---|---|---|---|---|---|

Identifique o herói exato do hook, o pico do reveal, quem faz o quê e quem segura cada prop. Rastreie verbos como opens/melts/moves/clears nos frames e a ação física que provoca uma reação verbal. Em origem orgânica real, acrescente a ficha de `PERFIL_ORGANICO.md`: objeto/distância da lente, câmera/cortes/plano maior, início e primeira frase da fala, molduras verbais, texto de tela, CTA original literal e substituição aplicável, nomes/marcas a trocar.

Se uma ambiguidade persistir após zoom e conferência, registre-a e use o gate do workflow antes de prompts. Ao chegar à copy, use os portões atuais e apresente todos os takes em tabela bilíngue para a aprovação do Luigi. Em `/watch lote`, cada vídeo tem pasta/checkpoint/evidências próprios; consolide pendências por número e confira repetição na mesma conta. Não misture os quatro produtos ou suas regras de CTA.
