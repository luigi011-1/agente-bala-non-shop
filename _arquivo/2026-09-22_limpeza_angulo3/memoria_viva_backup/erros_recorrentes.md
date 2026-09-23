---
name: erros-recorrentes
description: "Catálogo de erros reais de produção com correção — falhas 1-7 (imagem) + 3 erros históricos de leitura do hook (braço/água/caçamba-movie-style) + MICRO-PROTOCOLO OBRIGATÓRIO de 5 perguntas que DEVE ser rodado antes de qualquer prompt de T1/hook."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 246ef273-2f24-4b5d-8e5e-51929be93030
  modified: 2026-08-15T06:10:52.067Z
---

# Erros Recorrentes de Produção e Como Corrigir

**Why:** cada erro abaixo custou retrabalho real. Documentar evita repetir.

**How to apply:** consultar antes de gerar imagens e ao revisar cada frame.

## Falha #1 (a mais MORTAL): enfraquecer estrutura virando talking head
Se o original mostra algo ACONTECENDO (líquido dissolvendo, bicho saindo, braço encolhendo), o clone TEM que mostrar a mesma coisa. Transformar demonstração em "avatar só falando" mata a conversão. **A demo tem que continuar demo.**

## Falha #2: inventar frames que não existem no original
Não adicionar cenas que o original não tem. Reproduzir só os beats existentes.

## Falha #3: deixar a foto-âncora ditar câmera/pose
Foto do avatar é referência de identidade, não de enquadramento. Se ela é sentada e relaxada e você não corrigir, a cena sai sentada e relaxada.

**Solução:**
- Campo `reference_use` restringindo âncora a identidade/roupa/cenário
- Campo `posture` com override explícito ("standing upright, NOT the seated slouch, no legs or lap in frame")
- Negative: "no seated slouch"

## Falha #4: texto carimbado nas imagens
A IA adora escrever nas imagens.

**Solução:** "no text, no captions, no words on screen" no negative de TODO prompt. Legenda só na edição. ([[regras-universais]] #2.)

## Falha #5: gerar antes/durante/depois como imagens de UMA transformação
Dentro de um mesmo take, gerar SÓ o estado inicial. A transformação acontece no vídeo.
- **Exceção:** os "estágios" do antes/depois disfarçado (braço encolhendo em takes DIFERENTES) — isso é correto e cada estágio tem sua imagem.

## Falha #6: prop/modelo sai errado (coração no lugar de útero)
A IA defaulta pro modelo anatômico mais comum que conhece (coração, crânio) quando você só dá o nome.

**Solução:** descrever **FORMA e COR**, não só o nome.
- ❌ "female reproductive system model"
- ✅ "pink plastic model shaped like a uterus with two curved fallopian tubes branching to the sides and a central canal below"
- Negative: "no heart model, no skull, no brain model"
- Se teimar: gerar o modelo certo isolado, aprovar, usar como referência de objeto.

## Falha #7: volume/cobertura insuficiente do herói
Pediu "cristais de açúcar na barriga" e saiu camada fininha tipo molho.

**Solução:** forçar o volume no prompt:
- "THICK, TALL, HEAPED MOUND of amber sugar crystals, piled high with 3D volume, so much that almost no bare skin is visible"
- Negative: "no thin scattered sugar layer, no flat sauce-like coating"
- Puxar câmera pra perto/de cima do herói.

## Erro histórico #1: ler ERRADO o herói do hook
Interpretei "braço com gordura encolhendo take a take" como "mulher bebendo líquido com continuidade" (roupa mudando de cor = pattern-matching preguiçoso). Usuário teve que corrigir. Ver [[metodo-puzzle]] caso do antes/depois disfarçado.

## Erro histórico #2: ler ERRADO onde a água caía
Num outro hook (kitty/Erik Cole), disse que a água caía "nos pés / ao lado dela" quando na verdade era na virilha, por cima da roupa. O herói é essa metáfora — se você erra o alvo, mata o hook.

## Erro histórico #3: ler tableau em vez da AÇÃO (hook movie style, 39x outlier)
Hook de estacionamento: li como "mulher empurrando carrinho + homem atrás" e dei o carrinho pra ela. O REAL: a mulher lutava pra **abrir a caçamba emperrada**, o homem chega com o carrinho DELE e **abre a caçamba com uma mão só** — o **feito de força é o herói do hook**. Perdi o feito inteiro. Três causas encadeadas:
1. **Li quadros estáticos, não rastreei a ação entre frames.** A caçamba fechada→aberta é a mudança-chave; não tracei (a `/watch` existe pra isso).
2. **Deixei o padrão visual atropelar a transcrição literal.** A fala dizia "it never **opens** properly" — a palavra "opens" dizia o que acontecia, e eu ignorei em favor do pattern "carrinho".
3. **Movie style: não perguntei qual FEITO gera a fala de admiração.** "I wish my husband were as strong as you" aponta pra uma ação de força específica (abrir a caçamba). A frase emocional é ponteiro pro feito.
Mesma família dos erros #1 e #2: pattern-match do visual em vez de rastrear a ação real.

## Solução permanente para os TRÊS erros de leitura
- SEMPRE reanalisar o hook frame a frame denso e **rastrear a AÇÃO** ("o que muda entre os frames? o que abre/derrete/encolhe/se move?"), não ler um retrato parado.
- **Cruzar a transcrição literal com o visual:** se a fala diz opens/melts/moves/clears, achar isso acontecendo na tela.
- **Movie style: identificar o FEITO que dispara a fala emocional.** A frase de admiração/inveja aponta pra uma ação específica; achar qual.
- **Confirmar quem faz o quê e quem tem qual prop**, rastreando quem chega/segura o quê ao longo dos frames.
- Confirmar com o usuário em QUALQUER ambiguidade sobre o herói. **Nunca pattern-matching** — a primeira leitura costuma ser a errada.

## MICRO-PROTOCOLO OBRIGATÓRIO — rodar ANTES de escrever qualquer prompt de T1 (hook)

**5 perguntas que eu DEVO responder (por escrito, na minha análise) antes de tocar no prompt:**

1. **O que MUDA entre os frames do hook?** (caçamba fecha→abre, braço gordo→fino, líquido alto→baixo) — essa mudança é o herói.
2. **Quem faz o quê?** Listar cada pessoa + sua ação + seus props. Não assumir. Se a mulher está com as mãos na caçamba, ela está tentando abrir a caçamba, não empurrando um carrinho.
3. **Qual objeto pertence a quem?** Rastrear quem chega segurando/empurrando o quê ao longo de 3+ frames.
4. **A transcrição confirma?** Pegar os VERBOS da fala (opens, melts, clears, pours) e achar o verbo acontecendo no visual.
5. **[Movie style] Qual FEITO específico justifica a frase emocional?** A fala de admiração ("I wish...", "How did you...") aponta pra UMA ação. Qual?

**Se qualquer resposta for "não tenho certeza":** parar e perguntar ao usuário ANTES de gerar o prompt. Nunca entregar prompt com ambiguidade no hook.

## Checklist rápido de imagem antes de aprovar
- [ ] `reference_use` travando âncora presente?
- [ ] Traços canônicos do avatar corretos (cruz certa, cenário certo — [[avatares-fichas]])?
- [ ] "no text" no negative?
- [ ] Só o estado inicial (não a transformação)?
- [ ] Herói com volume/cobertura/forma bem descritos?
- [ ] Segunda pessoa travada (rosto) e estágios gerados a partir do original (não cascata)?
- [ ] Frame-herói gerado no Pro com variações?
