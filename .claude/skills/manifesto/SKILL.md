---
name: manifesto
description: Vídeo-manifesto de marca em tipografia cinética com locução (texto palavra por palavra sincronizado com a voz, palavra-chave grande na cor da marca, fundos claro/escuro trocados por um círculo que cresce, ícones em blocos 3D, logo desenhado). Use quando o produtor mandar uma referência nesse estilo, pedir "vídeo institucional", "manifesto", "motion com texto e voz", "vídeo da marca", ou um anúncio que apresente as funcionalidades de um software/serviço sem filmagem. Produz em HyperFrames, não no Flow.
---

# Manifesto — tipografia cinética com locução

Validado em 2026-10-09 no ObraUp (SaaS de gestão de obras), aprovado pelo Pedro: "gostei demais do
resultado". Casos e lições em `docs/pos-producao-casos.md`. O motor está em `template/`.

## Por que não é Flow

O Veo erra letra e ritmo quando o texto é o protagonista. Aqui o vídeo **é** o texto: cada
palavra precisa entrar no milissegundo da fala, com a grafia certa. Isso é HTML animado →
MP4 no **HyperFrames** (plugin instalado). O agente monta tudo; o produtor não gera nada.

## Fluxo — 7 etapas, 3 paradas

| # | Quem | Etapa |
|---|---|---|
| 1 | Produtor | Manda a referência de estilo (.mp4) e o material da marca. **Pedido de cliente: briefing de `references/briefing.md` respondido** |
| 2 | Você | `watch` na referência, com `--model small` (a fala costuma ser PT; `small.en` devolve lixo) |
| 3 | Você | Analisa a gramática visual e a estrutura do roteiro (`references/estilo-build-atlas.md`) |
| 4 | Você ↔ produtor | **PARADA 1 · roteiro** (tabela locução × visual) |
| 5 | Você | Monta o projeto a partir de `template/` e entrega um **rascunho sem voz** para ele sentir o movimento |
| 6 | Produtor | **PARADA 2 · voz** (ElevenLabs, recomendado) |
| 7 | Você | Alinha, mistura, renderiza, faz o QA quadro a quadro. **PARADA 3 · aprovação** |

## Etapa 3 — o que ler na referência

Complete antes de escrever: *a marca troca o "como era" pelo "como é", e cada frase tem um
símbolo visual.* Estrutura de manifesto que funcionou (ver `references/roteiro-obraup.md`):

1. Como era (o vilão concreto: no ObraUp, planilha + WhatsApp + memória)
2. "Mas X mudou / cresceu" → a consequência dolorosa (o prejuízo chegando sem avisar)
3. Nasce a marca (logo desenhado)
4. Três benefícios curtos ("mais controle, mais margem, uma obra que o cliente vê")
5. "Não é X, é Y" (o objeto riscado com X)
6. A lista do que oferece (ícones entrando **no instante em que cada nome é falado**)
7. As funções-herói, uma por cena, com mini-interface (IA, comparativo, aprovação do cliente)
8. Crença ("não se gere no improviso" / "acreditamos em dado, prazo e decisão")
9. Autoridade (quem fez) → slogan com o argumento central do público → CTA

Use o **estudo de público** da marca se existir:
o argumento central e o concorrente real entram literalmente no roteiro.

## Etapa 5 — montar

```bash
mkdir -p producao/<data>_<marca>_manifesto && cd $_
L=~/.claude/plugins/cache/hyperframes/hyperframes/<versão>/skills/hyperframes/scripts/plugin-cli.mjs
node $L init manifesto --example blank --resolution portrait --non-interactive --skill general-video
cp "$CLAUDE_PROJECT_DIR"/.claude/skills/manifesto/template/* manifesto/
```

No `build.mjs`, troque **só** a marca (o resto é motor):
- linha das cores (`NAVY`, `ORANGE`, `LIGHT`…): tire do CSS do próprio app/site;
- `LOGO_PATH` e `wordmark`: o SVG do favicon da marca, traço por traço;
- `P.cta`: o texto do botão e o site;
- fontes: baixe as woff2 da marca para `fonts/` (Google Fonts serve woff2 variável).

O `script.json` tem uma cena por frase: `theme` (`light`/`dark`), `text` com `*destaque*`,
`prop` (o visual) e `say` quando a pronúncia precisa de ajuda ("ObraUp" → "Obra Up").
Props prontos: `tile` (ícone), `chat`, `helmets`, `margin` (número caindo), `logo`,
`receipt` (riscado), `bars`, `modules` (grade sincronizada com a fala), `bridge`, `upia`
(chat de IA virando cartão), `compare`, `rdo` (carimbo de aprovado), `nochaos`, `checklist`,
`final`, `cta`. Para outra marca, renomeie e reescreva o conteúdo dos props; a mecânica fica.

`node build.mjs` → `lint` (0 erros) → `snapshot` no fim de cada cena → `render -q draft`.

## Etapa 6 — a voz (o que mais pesou)

- **Locução inteira numa tomada só.** Gerar frase por frase deixou a voz "lenta e
  travada": a entonação recomeça a cada frase. Acelerar e cortar pausas ajudou, mas não curou.
- **ElevenLabs gerada pelo produtor** é o caminho preferido. Voz aprovada para B2B masculino:
  "Gabriel - Shorts & Reels" (61s para o roteiro do ObraUp). Peça o caminho do mp3
  (Finder → botão direito → segurar Option → "Copiar como Nome do Caminho").
- HeyGen (OAuth grátis) dá ~10 min/mês e acaba rápido: 5 amostras + 21 falas esgotaram.
  Se usar, gere amostras curtas e a locução final numa tomada (`template/voice_take.mjs`).
- Vozes PT masculinas sérias no HeyGen: Pedro Lima - Serious (`0d0e23e8170446e38b18a7380b2d30a8`), Oscar, Giles, Borges, Adriano.

## Etapa 7 — alinhar, misturar, renderizar

```bash
ffmpeg -i voz.mp3 -ar 16000 -ac 1 g16.wav
whisper-cli -m <modelo>/ggml-small.bin -f g16.wav -l pt -ml 1 -sow -ojf -of words
python3 align_voice.py     # texto da tela × fala (difflib), respiro de 0,6s só nas trocas de fundo
python3 mix.py             # whoosh nas trocas + rebuild
node $L render -q looks -o renders/<marca>_manifesto_vN.mp4
```

Antes de renderizar: `df -h /System/Volumes/Data` (o render pede ~1-2 GB; com menos de 1 GB
ele para com "Low disk space"). Peça ao produtor para liberar espaço, nunca apague nada dele.

**QA** (contact sheet `ffmpeg -vf "fps=2,scale=100:-1,tile=15x8"`), nesta ordem:
1. Toda palavra aparece quando é falada? A cena com `say` diferente do texto cai no rateio.
2. Troca de fundo limpa: o texto antigo sai antes do círculo, a cena nova entra depois.
3. Última tela fica parada no CTA (a última cena não faz fade).
4. Números e cores dos props coerentes (a margem fica vermelha inteira, inclusive o "%").

## Regras

1. **Dados de demonstração sempre.** Prints do app do cliente trazem nomes, salários e fotos
   reais: servem só de referência de layout.
2. **Números a favor.** Obras atrasadas, PPC 0% e alerta vermelho no print viram dados
   positivos e plausíveis no vídeo.
3. Uma frase = uma cena = um símbolo. Palavra-chave no máximo 2 por cena.
4. Nada de travessão no roteiro.
5. Entregue primeiro o rascunho sem voz: o produtor aprova o movimento antes de gastar voz.
6. Música: o catálogo do HeyGen exige o `heygen` CLI. Peça um mp3 ao produtor.

## Variante: vídeo de imóvel (temporada/locação) · `template-imovel/`

Validado em 2026-10-09 (apto na Praia das Fontes, 36s). Material do proprietário, sem IA:
fotos + vídeos curtos de celular. Roteiro "um dia perfeito": varanda/vista (gancho, vídeo) →
café na varanda → piscina até o mar (vídeo) → aérea → montagem de interiores com etiquetas →
lazer → pôr do sol (vídeo) → ficha com checks + botão WhatsApp. Sem preço em temporada
(o valor muda com a data); CTA "Consulte datas no WhatsApp". Sem locução: som do mar dos
próprios vídeos como trilha.

- Preparo: `cropdetect` com `-loop 1` tira tarja de print; tudo vira 1080x1920 cover;
  vídeos do WhatsApp chegam em 576px de largura: peça os originais "como documento".
- `imovel.json` define as cenas (`media` + `text` com `*destaque*`, `montagem`, `final`) e a ficha.
- Texto: Inter + Playfair Display itálico na palavra-chave, cor areia. **O `.tin` precisa do
  `font-size` do texto**, senão o espaço entre palavras herda 16px e as palavras grudam.
- Vídeo dentro de wrapper NÃO temporizado (lint `video_nested_in_timed_element`); crossfade
  animando a opacidade do wrapper.
- Nunca deixar a IA alterar o imóvel. Se animar foto no Flow, só câmera e natureza.

### Imóvel v2 "elaborado" · `template-imovel/build_elaborado.mjs` (o produtor pediu "algo melhor e mais bem elaborado")
O que transformou a apresentação de fotos em peça: **história em horários** (Sexta 18h → Sábado 7h →
10h → 13h → 17h40 → Domingo, carimbo de relógio), **gancho com a imagem mais bonita** (pôr do sol +
"Seu próximo *fim de semana*"), **fundo areia com cartões** que expandem até tela cheia, **álbum** de
interiores empilhando no tempo da música, **pino caindo** na aérea, ficha em **grade de ícones**,
**calendário** marcando sex-sáb-dom (sem mês nem datas reais) e CTA "Reserve sua data".
Música: medir BPM e o primeiro tempo forte (energia de graves por 10ms + autocorrelação, sem numpy);
o gancho fica na introdução calma e o corte da primeira cena cai no tempo forte; uma cena por compasso.
Correção de cor quente única em todas as mídias (`eq` + `colorbalance`). Mix: lofi -14 LUFS + mar 0,32 + whoosh.
Bugs que custaram: título de uma cena vazando para o vídeo todo (id/condição de bloco); calendário com
a coluna errada (confira em que dia da semana cai o dia 1).
