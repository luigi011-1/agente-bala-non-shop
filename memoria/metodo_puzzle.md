---
name: metodo-puzzle
description: "Método Puzzle — clonar estrutura de vídeo vencedor trocando só a variável. Conceitos de esqueleto, variável, herói do hook, congruência, e o caso especial antes/depois disfarçado de continuidade."
metadata: 
  node_type: memory
  type: project
  originSessionId: 246ef273-2f24-4b5d-8e5e-51929be93030
  modified: 2026-08-14T18:47:10.678Z
---

# Método Puzzle — o coração de tudo

**Regra central:** pega-se vídeo que JÁ PROVOU funcionar, entende-se POR QUE funciona (estrutura), e recria-se essa estrutura com o SEU avatar + SEU produto, mudando o MÍNIMO possível. Criatividade em excesso é o inimigo.

**Why:** um vídeo vencedor tem cada elemento lá por um motivo (mesmo que você não saiba qual). Luvas azuis dão credibilidade; reveal nojento para o scroll; troca de roupa finge dias; livro dá autoridade. Quando você "melhora", pode remover a peça que fazia converter.

**How to apply:** teste final ao terminar cada clone → *"um estranho reconheceria que é a MESMA estrutura, só com outra variável/avatar?"* Se sim = certo. Se não = quebrou o método, refaça fiel.

## Os 3 conceitos que dominam tudo

### 1. ESQUELETO (não muda)
Sequência de beats com funções específicas — sagrada:
- **HOOK** (2-6s) — elemento visual chocante que para o scroll
- **MECANISMO / CONSPIRAÇÃO** — "ninguém te conta isso porque..."
- **RECEITA** — preparo, ingredientes, mistura
- **PROTOCOLO** — como usar ("morno, jejum, 7 dias")
- **RESULTADO** — o que acontece
- **PROVA / AUTORIDADE** — "15 anos com mulheres", livro, modelo anatômico
- **CTA + FOLLOW-GATE** — "comente yes, siga primeiro"

Nem todo vídeo tem todos os beats, mas os que estão devem ser reproduzidos na mesma ordem com a mesma função visual.

**Regra de ouro:** nunca enfraqueça uma demonstração transformando-a em talking head. Se o original mostra algo acontecendo (líquido dissolvendo, bicho saindo, braço encolhendo), o clone TEM que mostrar a mesma coisa. Falha #1 mais mortal.

### 2. VARIÁVEL (muda)
A coisa trocável: ingrediente, produto, problema atacado. Ao trocar, cada beat mantém a MESMA FUNÇÃO. Vídeos de testemunho/transformação muitas vezes não têm variável óbvia — diferenciação vem do avatar/cliente, estrutura fica 100% fiel.

### 3. HERÓI DO HOOK (o que MAIS importa)
O elemento visual dos primeiros segundos que faz o dedo parar. Identificar exige **frame a frame** (não pattern-matching). Se errar o herói, vídeo morre. Erros históricos catalogados em [[erros-recorrentes]].

**Composição visual do hook (hook bom vs ruim — do playbook Korella):** duas variáveis separam um hook que segura o scroll de um que vaza atenção. Aplicar SEMPRE ao escrever o prompt do frame do T1:
1. **Foco no herói.** Ruim = muita coisa na tela, a atenção se dispersa e o que fez viralizar se perde. Bom = **foco total no herói**, nada competindo. → no T1 o herói domina o enquadramento; tudo o mais fica secundário, desfocado ou fora de quadro.
2. **Distância de câmera.** Ruim = ângulo distante, frio, não conecta. Bom = **quase close-up**, íntimo, prende, para o scroll. → puxar a câmera pra perto do herói; preferir close/plano fechado a plano aberto no hook.

Reforça o que já vinha em [[prompts-imagem-json]] ("enquadramento herói: lower foreground + câmera puxada pra perto") — agora com o contraste explícito bom/ruim.

**Exemplos reais de heróis:**
- Açúcar cristalizado numa barriga que derrete quando a canela cai
- Dentes sujos que a água lava revelando brancos
- Braço esticado no primeiro plano com gordura encolhendo take a take (roupa muda de cor pra fingir dias)
- Insetos pretos saindo do brócolis em água salgada
- Líquido âmber despejado no modelo anatômico que lava os insetos
- Barriga estufada ao lado do coach que aponta "não é gordura, é disbiose"

## Congruência (o que faz o clone parecer natural)
Sempre checar:
- **Cenário × produto:** receita pede cozinha; disciplina pede garagem/box
- **Gênero × produto:** produto de saúde íntima feminina na boca de avatar masculino → reposicionar como **coach que prescreve** ("as mulheres que eu treino..."), NUNCA como usuário; ou usar avatar feminino
- **Registro × avatar:** ajusta a fala pro registro sem mudar estrutura
- **Idade × claim:** avatar jovem não diz "em 30 anos de wellness" → "em todos os meus anos"
- **Props coerentes:** luvas azuis de nitrila = inspetor/lab; manter

## Caso especial: antes/depois disfarçado de continuidade
Um dos hooks mais fortes. Parece: pessoa bebendo líquido, trocando de roupa a cada corte. **É na verdade:** braço no primeiro plano com gordura encolhendo take a take; troca de roupa é só pra espectador achar que foram dias diferentes. Beber o líquido é secundário.

**Como gerar em estágios:**
1. Gerar estágio 1 (gordura máxima) do zero, aprovar → é a âncora
2. Estágios 2 e 3 **por edição a partir do estágio 1 original** (NUNCA em cascata, senão a pessoa "deriva"), mudando SÓ gordura + cor da roupa; travar "não mude rosto/braço/fundo/ângulo"
3. Enquadramento idêntico entre estágios pra redução ficar óbvia no corte

Ver [[prompts-imagem-json]] modelo "comando de edição".

## Refinamento de SELEÇÃO DE FONTE (aula do mentor, 2026-08) — corrige "copie mais"
Fidelidade à ESTRUTURA continua (o esqueleto é sagrado). O que mudou é **o que se escolhe pra clonar**, porque o mercado saturou:
- ❌ **Não** clonar os vídeos de IA do MESMO nicho que todo mundo já clona (as vovós "genaicontent", os symptom videos comuns, comparação de pepino). Estão saturados → 100–500 views.
- ✅ Clonar **(a) vencedores genuinamente novos/insaturados** ou **(b) visuais virais de OUTROS nichos** (cabelo, pets, conteúdo pra mulher, creators reais não-IA) e re-mapear pro nosso ângulo.
- "Criatividade nunca vem do zero" — sempre parte de algo viral, mas a **fonte** tem que ser fresca/cross-niche, não o clone-do-clone. Se travar: dar o vídeo ao ChatGPT/Gemini e perguntar "como adapto isto ao meu avatar?".
- Ângulo de dinheiro real da operação: **vitalidade masculina** (ED, fluxo sanguíneo, cortisol, "the soldier/pipe", ejaculação precoce; público homens negros 50+) + secundário **menopausa** (avatar feminino "Mandy"). Qualquer viral de detox/estômago vira **fluxo de sangue pro soldier**. Detalhe em [[produtos-angulos]].
- **Regra nº1 de venda do hook:** o texto na tela tem que carregar **desejo OU controvérsia de saúde** ligada ao produto — senão viraliza mas não vende ("viral ≠ vendas").

## Princípio filosófico
"Na dúvida, copie. Fidelidade é o método." Trabalho não é criatividade do zero — é replicação disciplinada de vencedores comprovados. **Nuance atual:** fidelidade é da ESTRUTURA; a FONTE deve ser um vencedor novo ou cross-niche, não o vídeo saturado do próprio nicho (ver refinamento acima).

---

## O Puzzle também gera as VARIAÇÕES DE GANCHO na FityWell (2026-09-10)

Regra nova do Luigi: nos ângulos 2 e 4 as variações de gancho visual não são inventadas, são
**Puzzle aplicado ao próprio herói do hook**. Preserva-se a ação estrutural do hook original e troca-se
**uma variável por vez**, o ingrediente ou o alvo. Detalhe e exemplo canônico em
[[ganchos-variacao-puzzle]].
