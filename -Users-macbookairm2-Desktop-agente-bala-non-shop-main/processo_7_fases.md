---
name: processo-7-fases
description: "Pipeline operacional completo em 7 fases — do .mp4 de referência ao vídeo final. Ingestão, Decomposição frame a frame, Variável, Roteiro, Prompts de imagem, Geração de imagem, Geração de vídeo, mais pós-produção."
metadata: 
  node_type: memory
  type: project
  originSessionId: 246ef273-2f24-4b5d-8e5e-51929be93030
  modified: 2026-08-21T23:51:39.526Z
---

# Processo de Produção — as 7 Fases

## FASE 1 — Ingestão
Precisa de 3 insumos: **.mp4 de referência** + **roteiro/copy** + **foto do avatar** (ex.: `melody_carter_.png`).

- Regra: entregar `.mp4` e roteiro **juntos**. Roteiro sozinho não basta (falta estrutura visual); vídeo sozinho não basta (falta fala exata).
- **Insight crítico:** se você recebeu o vídeo de referência, ele JÁ foi gerado uma vez e passou. Consequência para a Fase 7: **a fala nunca é o problema em restrições**, porque já passou uma vez. Ver [[restricoes-protocolo]].

## FASE 2 — Decomposição (FRAME A FRAME — a mais importante)
Nunca "bata o olho" e presuma estrutura.

**Como decompor tecnicamente:**
1. Extrair frames com `ffmpeg` — a cada 1-2s no geral, a cada 0,3-0,5s no hook.
   Comando: `ffmpeg -ss [SEGUNDO] -i "video.mp4" -frames:v 1 -q:v 3 frame_[SEGUNDO].png -y`
2. Montar contact sheets com `montage` (ImageMagick).
   Ex.: `montage frame_0.png ... -tile 5x2 -geometry 240x427+3+3 -background white -title "Parte 1" sheet1.png`
3. Olhar CADA frame — hook em densidade máxima (0,3s) porque o detalhe herói costuma estar em movimento rápido.

**Tabela beat a beat (por cena):** Timestamp | Esqueleto visual | Nº pessoas (1 solo / 2+) | Props (tigela, luvas, livro...) | Fala (resumo) | Label (HOOK/MECANISMO/RECEITA/PROTOCOLO/RESULTADO/PROVA/CTA)

**Nunca passar batido:** herói do hook exato (não presumir), segunda pessoa e papel, o que muda entre takes (cor de roupa, tamanho, ângulo), props que dão credibilidade, cenário original, onde exatamente algo acontece (a água cai NO ponto X, não Y).

## FASE 3 — Definição da Variável
- Qual a nova variável (ingrediente/produto/problema)?
- Cada beat mantém a mesma função com conteúdo novo?
- Congruência com o avatar (cenário, gênero, registro, idade)? Ajustar ângulo (coach que prescreve) sem mexer na estrutura.
- Sem variável óbvia (testemunho) → 100% fiel, diferenciar por avatar/cliente.

## FASE 4 — Roteiro Final
- Takes de ~8s cada (quebrar falas longas em takes).
- **Sem em dash ("—")**. Frases curtas.
- Registro do avatar.
- **Keyword sempre "yes"** no CTA (sobrepondo palavra do original).
- Ajustes de congruência (idade, coach angle, sem "dear" se não combina).
- **Estrutura idêntica** — só variável muda.
- Marcar cada take como **TALKING** ou **B-ROLL**.

## FASE 5 — Prompts de Imagem
~~Um prompt por take~~ **CORRIGIDO em 2026-08-20: um prompt por SETUP/BLOCO, não por take.** Takes contíguos que compartilham cenário, enquadramento, ângulo e props usam a MESMA imagem, e só os prompts de vídeo variam. Regra completa em [[feedback-prompt-imagem-compartilhado]].

Cada imagem gera o **estado INICIAL** do bloco (nunca o meio ou fim). Transformação acontece na Fase 7 (vídeo).
- Nunca gere before/durante/depois como imagens separadas de UMA transformação (exceção: estágios do antes/depois disfarçado, que são takes diferentes).
- Zero texto na imagem (negative sempre com "no text, no captions, no words on screen").
- Foto do avatar = âncora de identidade/roupa/cenário, NÃO dita pose/câmera.

Templates em [[prompts-imagem-json]].

## FASE 6 — Geração de Imagem
- Volume no **Nano Banana 2**; frames-herói no **Nano Banana Pro**.
- **Travar 2ª pessoa primeiro:** gerar a cliente, aprovar rosto, reusar como referência nos outros takes. Faz ou quebra vídeos de antes/depois.
- **Estágios de transformação:** gerar estágio 1, aprovar, gerar demais por edição a partir do 1 (nunca cascata). Enquadramento idêntico.
- Frames-herói do hook: várias variações até acertar.
- Revisar cada imagem (o prop saiu certo? — ver caso modelo anatômico virando coração em [[erros-recorrentes]]).

## FASE 7 — Geração de Vídeo (animar a imagem)
Cada imagem vira clipe de ~8s no **Veo 3.1 via Flow** (ou Lite/Lower Priority pra não gastar crédito).

Formato do prompt (texto simples, NÃO JSON):
```
o avatar (homem/mulher) fala em inglês fluente a seguinte frase: "[FALA EXATA]"

o que acontece no vídeo: [ação fiel ao frame, ENXUTA]

câmera: [movimento simples]

som ambiente: [ambiente], sem música
```

Regras críticas:
- TALKING → linha "o avatar fala"; B-ROLL → sem fala, marcar "(sem fala no take)", locução entra na edição.
- **A fala vai INTEIRA no prompt sempre.** Nunca retire pra destravar restrição. Regra inviolável ([[restricoes-protocolo]]).
- Descrição ENXUTA (só o que acontece, sem excesso de ângulo/posição/adjetivo).
- "sem música" sempre (trilha entra na edição, controle + anti-strike).

## PÓS-PRODUÇÃO
- Juntar takes na ordem.
- Legendas grandes estilo Captions.ai Prism Pro — incluindo keyword "yes" no CTA.
- Take gerado sem fala (b-roll ou travado no gerador) → adicionar locução (gravada ou TTS) + legenda.
- Adicionar trilha/música na edição.
- Export 9:16.
