# Referências de edição V03–V05 — 2026-10-11

Escopo: aprendizado de edição para **Sea Moss / Natural Rems Gummies (Angle 1)** e **FitWell APP (Angle 2)**, resolvidos em `operacao/angulos.json`. Não é modelagem de copy, aprovação de roteiro nem produção. Auraly requer adaptação e não recebe estes padrões automaticamente.

## Método e limitações

Fontes operacionais examinadas: `docs/pos-producao-edicao-regras.md` (baseline vigente itens 8 e 16b), `AGENTS.md`, início de roteamento de `CLAUDE.md`, `.agents/skills/watch/SKILL.md`, `operacao/angulos.json`. Pipeline portable `/watch`, 5 fps em todo o arquivo, cenas com threshold 0,2, 1 job e CPU 2 threads; extração de cada arquivo em sequência, seguida por ASR **um de cada vez** com a função canônica `transcribe` do pipeline e palavras aproximadas Faster-Whisper small.en. Grades completas e frames críticos abertos pessoalmente. Manifestos distinguem conclusão de extração e revisão; `visual_review.json` registra o trabalho humano/modelo separado.

**Áudio perceptivo indisponível:** não ouvi estes arquivos por uma ferramenta que entregasse áudio ao modelo. Transcrição ASR não equivale a escuta. Não há conclusão observada sobre instrumentos, emoção da trilha, BPM, crescendos, sincronização de batidas, timbre, volume isolado da música ou efeitos sonoros. RMS do mix não resolveria esses itens. A investigação musical permanece pendente. Todas as propostas musicais abaixo são propostas, não descrição do original.

ASR pode confundir palavras: V04 “Constipate it” contrasta com legenda visual “Constipated”; V05 “sour soft” contrasta com rótulo “Soursop”. Legendas do original não são roteiro canônico. Densidade de fala é palavras ASR / duração total, incluindo pausas; não demonstra o multiplicador aplicado no original. Gaps ASR são candidatos a ausência de fala, não silêncio acústico comprovado.

## Medições

| Referência e nome original | Duração / quadro | Unidades ASR | Unidades/s global | Gap ASR longo no hook | Detectores de cena |
|---|---|---:|---:|---|---|
| V03 `snapinsta-1791763924795.mp4` | 48,830 s; 720×1280; 30 fps | 183 | 3,748 (225/min) | 2,44–3,82 s (1,38 s) | 7,40; 18,133; 26,60; 35,967; 45,133 s |
| V04 `snapinsta-1791763902279.mp4` | 57,027 s; 720×1280; 30 fps | 196 | 3,437 (206/min) | 1,70–4,66 s (2,96 s) | 2,90; 4,033; 5,533; 9,20; 12,533; 24,333; 29,50 s |
| V05 `snapinsta-1791763875945.mp4` | 71,795 s; 720×1280; 30 fps | 253 | 3,524 (211/min) | 5,00–6,76 s (1,76 s) | 17,933; 22,667; 35,90; 46,267; 71,633 s |

Lista automática **não é contagem total de cortes**: falha em cortes de match-action e pode contar overlay/efeito. As mudanças adicionais vistas abaixo têm precisão visual de aproximadamente ±0,2s, salvo tempo FFmpeg informado. Dados e hash SHA256 em `evidencias-edicao-2026-10-11/v0*/metrics.json`. A contagem acima usa unidades do alinhamento ASR (que pode separar contrações). Pelo tokenizador lexical comum `scripts/analisar_edicao_referencia.py`, são V03 **180 palavras / 3,686 palavras/s**, V04 **193 / 3,384**, V05 **249 / 3,468**. Para comparar com V01/V02, usar esta última definição, salva em `metricas.json`.

Mix original medido pelo mesmo script: V03 −14,46 LUFS integrado / +0,23 dBTP / LRA 2,50; V04 −15,03 LUFS / −0,72 dBTP / LRA 4,40; V05 −14,61 LUFS / −0,54 dBTP / LRA 3,60. Medição do arquivo misturado, sem qualquer inferência sobre emoção ou ganho isolado da trilha. Não importar pico positivo do modelo: nossa entrega deve manter headroom.

## V03 — cano obstruído → receita → produto → CTA

| Tempo | Evidência visual / ação | Fala ASR ou legenda vista | Função e edição |
|---|---|---|---|
| 0–2,44 | Homem agachado, câmera baixa junto ao piso; copo âmbar e boca do cano dominam primeiro plano | “This the eviction notice…” | HOOK falado. Rosto ainda legível no alto; objeto mais próximo que rosto. Sem introdução de contexto. |
| 2,44–3,82 | Despejo continua; obstrução sai do cano entre 3,4–3,8 s | ASR sem palavras | PAYOFF. Não cortar automaticamente esta janela por ausência de fala. Legenda desaparece enquanto ação completa. |
| ~3,8–7,30 | Corte para bancada, panela/herói ocupando metade inferior; limão é despejado | “Get a pot of water…” | RECEITA falada; corte muda situação após payoff, preserva identidade/ambiente. |
| 7,40–11,30 | Colher em cima da panela; chia e linhaça entram em ações sucessivas | “Teaspoon…” | Cada ingrediente justifica mudança de pose/prop; câmera quase estável. |
| 11,44–14,12 | Frasco entra em mão direita da imagem e é inclinado; líquido visível caindo | “Splash of soursop bitters…” | REVEAL de produto em uso, não product card isolado. Rótulo legível em frame 11,8 s. |
| 14,50–17,92 | Colheres adicionais; ações não interrompem fala | “Teaspoon of turmeric…” | Corpo ritmado por gestos, não cortes arbitrários por segundo. |
| 18,133–26,48 | Plano mais próximo, homem segura copo à lente; sem mostrar espera de fervura | “Let it boil for 10 minutes…” | Elipse temporal para resultado. O comando de receita é dito com bebida pronta. |
| 26,60–35,68 | Overlay de conversa à direita sobre rosto, enquanto copo e legenda seguem à esquerda | “If y’all want those bitters…” | PROVA apresentada. Print cobre parte grande do rosto e fica ~9,37 s; copiar função apenas com evidência real, reposicionar para não competir. |
| 35,967–44,88 | Overlay sai; mantém close do rosto+copo durante instrução de clique | “Just click my name…” | CTA sem frenesi de cortes; gesto/copo permanecem como âncora visual. |
| 45,133–48,83 | Jump cut visível ao reiniciar despedida; bebida reaparece levantada | “And make sure…” | Fecho. Não importar religião, promessa, produto ou CTA do modelo. |

Evidências locais (raiz `docs/evidencias-edicao-2026-10-11/v03/`): `overview/overview_scenes_01.png`; **todas** `overview_timeline_01.png` a `_13.png`. Individuais abertos: `frames/timeline/tl_t00000.0000_000001.png`, `tl_t00003.6000_000019.png`, `tl_t00011.8000_000060.png`, `tl_t00026.6000_000134.png`.

Legenda: creme/clara, bloco alinhado à esquerda; mistura serifada (inclusive itálico) e sans pesada. “eviction” grande 0,4–0,6 s; “notice” 0,8–1,2 s; conectivos menores. “Teaspoon” permanece enquanto linhas menores completam “of chia”; texto não é substituído por uma palavra solitária a cada frame. Área típica x≈3–10%, y≈55–63% neste material. Há expansão/blur na entrada de palavras vistas em 2,2s/2,4s e 32,2s/32,4s. Família tipográfica exata não identificada. Em partes, legenda invade copo/panela: aproveitar hierarquia, melhorar colisões.

Frames selecionados para commit: [tl_t00000.0000_000001.jpg](evidencias-edicao-2026-10-11/v03/frames_criticos/tl_t00000.0000_000001.jpg), [tl_t00003.6000_000019.jpg](evidencias-edicao-2026-10-11/v03/frames_criticos/tl_t00003.6000_000019.jpg), [tl_t00011.8000_000060.jpg](evidencias-edicao-2026-10-11/v03/frames_criticos/tl_t00011.8000_000060.jpg), [tl_t00026.6000_000134.jpg](evidencias-edicao-2026-10-11/v03/frames_criticos/tl_t00026.6000_000134.jpg).

## V04 — POV incomum → reação → preparo → plano contínuo de venda

| Tempo | Evidência visual / ação | Fala ASR ou legenda vista | Função e edição |
|---|---|---|---|
| 0–1,70 | Câmera olhando para cima através de aro do vaso; homem aciona alavanca | Legenda “Constipated. Not for long.” | HOOK com enquadramento incomum. Texto grande central no primeiro instante; depois esquerda. |
| 1,70–4,66 | Água envolve lente; quadro quase todo líquido 2,9–4,0 s; ele sorri 4,0–4,6 s | ASR sem palavras | PAYOFF + reação; candidato de pausa protegido, não “tempo morto”. Não se pode confirmar som de descarga. |
| 4,66–5,533 | Homem aponta para lente e aproxima mão | “Yo…” | Gestual prepara mudança; 5,533 s é smear/transição para bancada, vista na grade de cenas. |
| 5,533–9,14 | Bancada; despeja água em jarra transparente; rosto perto, objeto central | “some warm water first…” | Continuidade pelo movimento/água. |
| 9,20–12,42 | Corte para limão espremido | “Splash a lemon…” | RECIPE com legenda temática de ingrediente. |
| 12,533–17,74 | Colher de linhaça, despejo e mão apoiada na mesa | “Tablespoon of flaxseed…” | Plano mantido ao explicar mecanismo e concluir ação. |
| ~17,8–24,18 | Frasco entra, despejo e rótulo no mesmo plano | “Now the shot…” | REVEAL de produto sem interromper contato visual. Detector não capturou toda troca de prop. |
| 24,333–29,26 | Ameixas caem; mão gesticula ao explicar | “Handful of prunes…” | Próximo ingrediente sem espera de buscar utensílio. |
| 29,50–38,00 | Elipse para bebida pronta na mão; não mostra liquidificador funcionando | “Blend it all up…” | Resultado substitui execução longa; pequeno humor/reação sustentados no plano. |
| 38–49,26 | Mesmo homem+copo, mão livre indica destino, mais espaço de mesa em quadro | “And if y’all want…” | Venda/CTA de orientação; estabilidade, sem zoom obrigatório. |
| 49,50–57,03 | Pedido de comentário, follow, despedida e brinde | “Comment flush…” | Fecho ainda com bebida. `Follow` destacado grande 52,5–53,1 s, mas referência segue falando; nossa regra de follow final permanece. |

Evidências locais (raiz `docs/evidencias-edicao-2026-10-11/v04/`): `overview/overview_scenes_01.png`; **todas** `overview_timeline_01.png` a `_15.png`. Individuais abertos: `frames/timeline/tl_t00000.0000_000001.png`, `tl_t00002.8000_000015.png`, `tl_t00005.6000_000029.png`, `tl_t00017.8000_000090.png`.

Legenda: estilo compartilhado com V03, cor creme, sans bold + serif italic, conectivos menores. Palavra “Tablespoon” grande 12,6–14,0s; “of flaxseed” constrói linhas menores. “right” 8,4–9,2s; “Splash” 9,4–10,6s; “Amazon” 42,8–43,4s em serif grande; “profile” 47,4–47,6s. Máximo observado de até três linhas, combinações frequentemente 3–6 palavras. A palavra de 13 letras no hook quase ocupa toda a largura: largura/medição deve ser adaptativa, não tamanho fixo.

Frames selecionados para commit: [tl_t00000.0000_000001.jpg](evidencias-edicao-2026-10-11/v04/frames_criticos/tl_t00000.0000_000001.jpg), [tl_t00002.8000_000015.jpg](evidencias-edicao-2026-10-11/v04/frames_criticos/tl_t00002.8000_000015.jpg), [tl_t00005.6000_000029.jpg](evidencias-edicao-2026-10-11/v04/frames_criticos/tl_t00005.6000_000029.jpg), [tl_t00017.8000_000090.jpg](evidencias-edicao-2026-10-11/v04/frames_criticos/tl_t00017.8000_000090.jpg).

## V05 — metáfora física → preparo → overhead do produto → CTA

| Tempo | Evidência visual / ação | Fala ASR ou legenda vista | Função e edição |
|---|---|---|---|
| 0–5,00 | Câmera rente à mesa, objeto branco segmentado no primeiro plano e homem+copo verde atrás; copo começa a virar | “Parasites… till we put that magnet…” | HOOK falado; objeto domina parte inferior; sem certificar se é animal real, prop ou mídia gerada. |
| 5,00–6,76 | Objeto desliza para dentro do copo deitado; homem observa e reage | ASR sem palavras | PAYOFF sustentado ~1,76s; não é erro/silêncio descartável. Movimento observado não prova mecanismo biológico. |
| ~7,2–17,88 | Copo novamente de pé; ator explica ao lado da mesa | “This juice…” | Match cut/elipse para fala sem limpar mesa em tempo real. |
| 17,933–22,58 | Plano maior em pé, colher de folhas sobre jarra de liquidificador | “Cilantro, in…” | Corte muda escala ao entrar preparo, rosto ocupa menos quadro e utensílios ficam inteiros. |
| 22,667–31,74 | Outra tigela de folhas, colher e explicação | “Parsley, in…” | Ação e fala juntas; mantém narrativa em talking head. |
| ~31,8–35,74 | Limão espremido acima da jarra | “Key lime juice…” | Próxima etapa sem mostrar busca/espera. |
| 35,90–41,02 | Corte overhead: mão/frascos acima da jarra; líquido despejado, rótulo vira para lente | “Gonna need some herbal…” | Produto recebe plano dedicado em uso. Aos 39,4s frasco upright legível. Faces não necessárias em toda cena. |
| ~41,2–45,96 | Overhead mantém jarra; tigela de gengibre substitui frasco | “Ginger, in…” | Match cut de prop; corte não detectado em threshold 0,2. Texto fica junto à tarefa. |
| 46,267–53,22 | Volta a plano médio; bebida verde pronta na mão | “Add some water and blend…” | Elipse do blender, retorno do rosto ao entrar resultado. |
| 53,54–66,48 | Plano médio contínuo, mão indica o destino e copo na outra mão | “Comment detox…”; produto e perfil | CTA deixa gestos visíveis; nome da marca e destino ganham hierarquia de texto. |
| 66,62–71,79 | Follow + fala de fecho, mão no peito e copo na mesa | “Follow your boy…” | Final humano/gestual; quadro não corta colado no último fonema. |

Evidências locais (raiz `docs/evidencias-edicao-2026-10-11/v05/`): `overview/overview_scenes_01.png`; **todas** `overview_timeline_01.png` a `_18.png`. Individuais abertos: `frames/timeline/tl_t00000.0000_000001.png`, `tl_t00005.6000_000029.png`, `tl_t00036.4000_000183.png`, `tl_t00062.4000_000313.png`.

Legenda: creme, hierarquia semântica; “Parasites” grande 0,2–1,0s, “heavy” 2,2–3,4s, “magnet” 4,0–4,6s; texto desaparece na ação sem fala 4,8–6,6s. No overhead, “Gonna” sans grande + “need” serif italic + “some” sans normal coexistem (36,4s). `Amazon` 58,6–59,0s e `profile` 65,8–66,0s recebem destaque; posição à esquerda do torso y≈45–60% no plano mais aberto. Palavra isolada grande não é regra universal: composição muda com escala do plano.

Frames selecionados para commit: [tl_t00000.0000_000001.jpg](evidencias-edicao-2026-10-11/v05/frames_criticos/tl_t00000.0000_000001.jpg), [tl_t00005.6000_000029.jpg](evidencias-edicao-2026-10-11/v05/frames_criticos/tl_t00005.6000_000029.jpg), [tl_t00036.4000_000183.jpg](evidencias-edicao-2026-10-11/v05/frames_criticos/tl_t00036.4000_000183.jpg), [tl_t00062.4000_000313.jpg](evidencias-edicao-2026-10-11/v05/frames_criticos/tl_t00062.4000_000313.jpg).

## Propostas implementáveis derivadas destas evidências

| Proposta | Evidência | Implementação sugerida | Escopo / cuidado |
|---|---|---|---|
| Proteger ação sem fala com intervalo explícito | Payoffs V03 2,44–3,82; V04 1,70–4,66; V05 5–6,76 | `protected_intervals`/beat de reveal no plano de edição; cortar excesso antes/depois, preservar acontecimento e breve reação | Sea Moss/FitWell. Tratar “sem fala” diferente de “sem conteúdo”. Auraly depende do hook. |
| Legenda por pequenos grupos com destaque editorial | Ingredientes, Amazon e profile nos três | Grupo 3–6 palavras, 1–3 linhas; palavra chave bold grande, conectivos menores; serif italic opcional; manter palavra chave enquanto complemento acumula | Opt-in Sea Moss/FitWell; não substituir default de Auraly. Usar texto aprovado. |
| Caixa/âncora ajustável conforme prop | V03 panela/copo; V05 overhead/torso | Safe area configurável por beat; medir largura; evitar rosto, rótulo e objeto; não marcar colisão “OK” sem frame de QA | Não copiar sobreposição ruim da referência. |
| Limpar esperas, não comprimir todos os beats iguais | Elipses 18,133 V03; 29,50 V04; 46,267 V05 | Cortar procura de objeto/espera; manter início, contato e término da ação aprovada; respeitar palavra por palavra | Baseline vigente: alvo 3,8 palavras/s para FitWell e outros, 4,0 Auraly; multiplicador entre 1,0x e 1,25x calculado por vídeo (regras item 8). Não inferir multiplicador original. |
| Variação de câmera por função do beat | V05 overhead aos 35,90; plano maior aos 17,933 e 46,267 | Brief de enquadramento: hook herói foreground, preparo mãos+objeto inteiro, reveal produto legível, CTA rosto+gesto | Cabe no planejamento de K, não escrever ação/cena extra no V curto. Não gerar prompts neste estudo. |
| Produto durante ação real e rótulo descoberto | V03 11,8; V04 17,8; V05 36,4–40,4 | Planejar take em que pega/mostra/abre o frasco/gummy e mantém rótulo; reservar legenda ao lado | Adaptar a gummies, não despejar bitters ou importar claims do modelo. FitWell demonstra app/hábito. |
| Corte seco motivado domina, efeito breve pontual | V04 smear 5,533; demais trocas por ingredientes/resultados | Não aumentar efeitos automaticamente; manter transição opcional só em mudança maior | Nenhuma evidência de dois light leaks obrigatórios nestes três. Mantém default existente até decisão do orquestrador. |
| Música por beat com ganho/ducking verificável | Sem escuta válida do original | Baseline vigente item 16b: música normalizada a −14 LUFS e baixada −18 dB da voz, sem ducking, fade-in 0,3s/fade-out 0,8s. Proposta opt-in Sea Moss/FitWell: curvas por beat de −30 a −18 dB, sem superar −18 dB; QA com stems separados | É desenho proposto, não insight musical confirmado. Não escolher trilha por RMS do mix. |

O maior ganho demonstrável é **edição orientada por ação e semântica**, não volume de efeitos ou aceleração extrema. Corpo dos vídeos mantém vários segundos de plano estável quando gesto e legenda já avançam a narrativa. Nenhum destes arquivos traz métrica de conversão; não declarar que uma técnica “vende mais” a partir de preferência estética.

## Estado real

V03/V04/V05: extração, ASR e revisão visual completos. Música e emoção sonora: **pendentes de escuta perceptiva válida**. Não foram alterados editor, copy, workflows, prompts, checkpoints de produção, Flow ou ofertas. Artefatos binários permanecem locais ignorados; textos/manifestos/transcrições/dados podem entrar no commit do orquestrador.
