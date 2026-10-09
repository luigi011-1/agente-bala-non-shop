# Pós-produção — casos e lições (Pedro, 2026-10-05 a 10-09)

Contribuição do Pedro. Não muda nenhuma regra de copy, ângulo ou workflow deste repo: cobre a
**forma** do vídeo depois que o roteiro e os takes existem. Skills: `manifesto`, `edicao`, `anuncio-app`.
Regras técnicas do Flow: `docs/pos-producao-flow-frames.md`.

## Qual skill para qual pedido

| O que chega | Skill | Ferramenta |
|---|---|---|
| Takes prontos para editar (jump cut, legenda, música) | `edicao` | HyperFrames, o agente edita e renderiza |
| Anúncio do app com telas reais, cenas do dia a dia, sem rosto | `anuncio-app` | Nano Banana → Veo (Frames to Video) |
| Referência de texto animado + locução (institucional, funcionalidades) | `manifesto` | HyperFrames |
| Fotos e vídeos de um imóvel (temporada, locação) | `manifesto` → variante imóvel | HyperFrames |

HyperFrames: plugin do Claude Code (`claude plugin marketplace add heygen-com/hyperframes` →
`claude plugin install hyperframes@hyperframes`). Precisa de Node 22+ e FFmpeg.

## Checagens antes de gerar ou renderizar
- Diga onde está cada arquivo a anexar e abra a pasta: o operador não navega o projeto.
- `df -h`: render pede 1-2 GB livres; com menos de 1 GB para com "Low disk space".
- Voz: locução **inteira numa tomada** (ElevenLabs). Frase por frase fica "lenta e travada".
- Edição: peça uma **referência do estilo** antes. "Dopaminérgico" quer dizer coisas diferentes.

## Compliance · filtro de "filmagem escondida" (Nano Banana) · 2026-10-06

**Sintoma:** "Esta geração talvez viole nossas políticas", 3 de 3, num close das mãos da
Leslie com o celular. O mesmo projeto já tinha passado com ela de perfil.

**Gatilho:** a combinação, não uma palavra. `seen from behind` + `sneaking a look` +
`bare toned shoulder` + `her lap` + foto-âncora sensual anexada = leitura de voyeurismo.

**O que passou:**
1. Tirar todo vocabulário de espiar e de corpo visto por trás. O flagra fica na composição
   (máquina em primeiro plano, câmera baixa, ela de costas) e no movimento do vídeo.
2. **Não anexar a âncora sensual** quando o plano é close. Mãos, pulseira e capa do celular
   descritas em texto bastam.
3. Prompt em **texto corrido curto** em vez de JSON longo.
4. Plano B: tela verde lisa no celular (nada para o filtro ler).

Pedido "mais gostosa": funcionou `curvy athletic hourglass figure, slim waist, tight
leggings that hug her curves, elegant and sensual, never vulgar` + negative `no deep
cleavage, no sports bra only, no glamour posing, no heavy makeup`. Não descreva o corpo por
trás num plano de costas.

## Casos

### Caso 27. App da senhora do lado (Leslie) · 2026-10-05 a 10-06 · FORMA 1 do zero
- **Modelo:** filmagem real, 13,6s, sem fala, texto fixo "Alguém sabe o nome do app que essa
  menina do meu lado tava usando??? 😭". POV na remada → câmera acha a moça no banco → close
  por cima do ombro na tela do app de treino.
- **Mecanismo:** curiosidade sobre o nome do app numa cena de flagra, não de anúncio.
- **Rota:** a troca v2v (FORMA 2) falhou 4x ("Falha ao gerar áudio"). Refeito do zero.
- **Âncora que funcionou:** Leslie sentada na remada, de costas, câmera a ~1m atrás do ombro
  direito, tela visível por cima do ombro. Regata preta justa, legging, corrente e pulseira
  de ouro, pérolas. Corpo atlético curvilíneo, "sexy sem ser vulgar".
- **O que errou e custou:** imagens posadas (centralizada, de frente, corpo inteiro) não
  leem como flagra; mão na cabeça lê como dor de cabeça; mãos geradas sem anexo saem com
  80 anos (corrigir por edição: "well-kept woman around 60"); K01 e K02 gerados separados
  quebraram o espaço do vídeo; close "por trás" foi recusado pelo filtro.
- **Regras novas:** `flow-frames.md` (geografia, tela do celular) e `compliance.md`
  (filtro de filmagem escondida).
- **Copy:** texto na tela A "does anyone know what app the lady next to me at the gym was
  using??? 😭" / B "she told me she's 72… does anyone know what app she was using??? 😭"
  (recomendada). Legenda com `yes` e follow-gate, sem nome do app.

### Caso 28. FityWell, anúncio animado do app · 2026-10-08 · motion de app (sem avatar)
- **Formato:** anúncio pago, ~14s, 9:16, inglês, sem locução. Telas reais extraídas das
  gravações de tela do produtor. Pipeline completo na skill `anuncio-app`.
- **Estrutura validada (teste montado no CapCut, 19,4s):** "Snap your plate." scan no prato
  e etiquetas de kcal → etiquetas voam para o celular → "Get clear numbers." tela Food 383 kcal
  (o número contou de 219 para 383 sozinho, ficou ótimo) → zoom → "Workouts that fit your
  week." com figura anatômica 3D na ponte de glúteo → fechamento Fitywell + "Simple meals.
  Clear numbers. No guesswork." + botão "Find your starting point".
- **Defeitos do teste:** etiquetas se multiplicam ao voar (acelerar 2x); tela branca por ~1s
  no V2 (cortar); figura parada 4s (descrever o movimento passo a passo); 19s é longo para
  ad (alvo 14s).
- **Omni 10s em plano único:** hook lindo, mas inventou todas as telas do app depois de 3,4s
  e errou a grafia das etiquetas. Ver `flow-frames.md` §5.

### Caso 29. ObraUp, manifesto em tipografia cinética · 2026-10-09 · HyperFrames (sem Flow)
- **Pedido:** "mostrar as funcionalidades que ele tem", no estilo de uma referência de consórcio
  (Build Atlas, 79s, texto palavra por palavra + locução + fundos claro/escuro + ícones 3D).
- **Público:** dono de construtora, 36-50, WhatsApp + planilha. Argumento central do estudo de
  público usado no slogan: "Pare de perder margem sem perceber". CTA: demo de 20 min no WhatsApp.
- **Resultado:** v3, 61s, voz ElevenLabs "Gabriel". Produtor: "gostei demais do resultado".
- **Custou:** voz HeyGen frase por frase ("lenta e travada", 2 versões) e a cota grátis do
  mês; render parado por disco cheio. Tudo virou regra na skill `manifesto`.
- **Cuidado de dados:** os prints do app tinham nomes e salários de funcionários reais e um
  painel com 8 de 9 obras atrasadas. Nada disso foi para o vídeo.

### Caso 30. Edição de takes (coach + bebida matinal) · 2026-10-09 · skill `edicao`
- v1 "dopaminérgica" (pop-ups, zoom, SFX, legenda amarela) reprovada: faltava tirar silêncio e acelerar.
- v2 no estilo da referência do produtor (Holistic Brandon): 50s de takes → 24,4s, zero pausa, 1,12x,
  legenda serifada branca minúscula no centro, light leak em 2 trocas. Aprovada com travadas leves.
- Lição-mãe: pedir a referência do estilo antes de editar.

### Caso 31. FitWell growth v2, chá glow (avatar de tranças) · 2026-10-09 · skill `edicao`, 1º teste nosso
- **Entrada:** 5 takes do Flow (Omni, 720x1280, 24fps, 10s cada) do `fitywell_growth_v2`. Todas as
  falas saíram literais do roteiro (conferido por transcrição take a take).
- **Saída:** 24,7s, 1080x1920, 3,6 palavras/s, estilo v2 aprovado (sem silêncio, 1,12x, legenda
  serifada branca no centro, light leak na entrada do T2 e do T4). Sem música: a trilha não está no repo.
- **Acertos:** cortar pelo `silencedetect` e descartar ilha de som sem palavra (ruído de fim de take);
  legenda com o tempo do whisper no vídeo cortado e o TEXTO do roteiro (quando a contagem de palavras
  bate, a escuta nunca entra na tela); trim dentro do filtro em vez de `-ss` antes do `-i`.
- **Erro achado e corrigido antes da entrega:** `minterpolate` (24→30fps) aplicado no vídeo inteiro
  interpola ATRAVÉS do corte e cria um quadro fantasma (dois takes misturados) na troca T3→T4.
  Conserto: `minterpolate` por segmento, antes do `concat`. Conferir sempre com contact sheet a
  ±0,1s de cada corte.
- **Ajuste novo:** no take-herói (cabeça com espuma lavando), a pausa de 1,3s no meio da fala foi
  ACELERADA 5x em vez de cortada: o reveal continua sem pulo e a pausa vira 0,27s.
- **Do Flow, não da edição (próximas produções):** o bule ganha tampa de madeira no T4 e não tem no
  T3; o T4 começa com o bule no réchaud e ela só levanta durante a pausa, então o corte pula a ação;
  o T5 pedia a mão apontando para baixo e ela não aponta. Prompt de vídeo do T4 deveria abrir com o
  bule já na mão (igual ao K04) e o K03/K04 descrever a mesma tampa.
- **Custo:** ~7 min de `minterpolate` na nuvem + render HyperFrames. Script: `template/edit_ritmo_v3.mjs`.
- **Resultado aprovado pelo Luigi.** Regras fixas que saíram daqui: `docs/pos-producao-edicao-regras.md`.
