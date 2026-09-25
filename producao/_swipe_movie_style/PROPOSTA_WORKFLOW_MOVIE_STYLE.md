# Workflow prático de MOVIE STYLE (v2, APROVADO 2026-09-23)

**Status: APROVADO pelo Luigi em 2026-09-23.** Falta só a escolha da primeira produção; as peças da
seção 7 marcadas "a fazer" são construídas antes dela. Base: os 24 virais validados de `rodada_2026_09_22/` e os 14 de 2026-09-12.

**Escopo por agora: só FityWell (Ângulo 2) e Auraly (Ângulo 3).** Korella fica fora (Luigi,
2026-09-23).

## Decisões do Luigi (2026-09-23)
| # | Decisão |
|---|---|
| 1 | **Sem Voice Changer.** A voz de cada personagem é descrita no prompt de vídeo (timbre, idade, sotaque e entonação/emoção da fala), para TODAS as falas de TODOS os personagens |
| 2 | **Médico em cena liberado**, desde que não seja a autoridade que vende ou recomenda o produto |
| 3 | **Só FityWell e Auraly** por agora |
| 4 | **Parte 2 sob pedido:** o Luigi reenvia o vídeo que fizemos e pede a parte 2 |
| 5 | Primeira produção: **aguardando** |
| + | **Decomposição do short form lista TODOS os WTF**, sem número fixo |
| + | **Character sheet de cada personagem principal**, para consistência ao longo do vídeo |

---

## 0. Onde isto encaixa (sem criar workflow concorrente)

O `AGENTS.md` proíbe uma segunda versão conflitante do workflow. O movie style é um **módulo de
formato** dentro do roteador que já manda em cada ângulo:

| Ângulo | Roteador (não muda) |
|---|---|
| 2 FityWell | `CLAUDE.md` + `PLAYBOOK_FITYWELL.md` |
| 3 Auraly | `WORKFLOW_AURALY.md` + `CHECKPOINT.md` |

O cabeçalho do `ROTEIRO.md` declara o formato, ao lado dos marcadores que já existem:
```
formato: short-form   + tipo: crescimento   ← marcador que o linter já entende
formato: movie-venda
```

---

## 1. Etapa 0 · TRIAGEM, sempre primeiro

Na primeira resposta eu digo qual é o formato:

| Pergunta | Short form | Movie style de venda |
|---|---|---|
| Tem produto, marca, link ou keyword? | não | sim |
| Duração | 13 a 30s | 60 a 120s |
| Cenários | 1 | 4 a 6 |
| Termina | no pico, ou na sentença numa frase | resolvido (transformação, vingança) |

Na dúvida, pergunto. Os dois formatos nunca dividem roteiro, gancho nem pacote.

---

## 2. ELENCO: character sheet de cada personagem principal

Vale para os dois formatos.

**Quem ganha character sheet:** todo personagem que aparece em **mais de um clipe** ou que precisa
ser reconhecido de uma cena para outra (agressor, vítima, protagonista nos dois estados de corpo,
quem faz a ponte, filho que volta no final).
**Quem não ganha:** personagem que aparece uma vez só e figurante de fundo. Esses são descritos
por escrito dentro do K em que aparecem.
**O avatar do ângulo** (Dana, Jamie ou Lynn; Walt, Darlene ou Lorraine) já tem a âncora, que faz o
papel de character sheet.

**Como fica a entrega:**
1. Ficha de cada personagem principal, fora dos blocos: nome de trabalho, idade, etnia, corpo,
   cabelo, roupa, um traço que o torna reconhecível e a **ficha de voz** (seção 6).
2. **`REF-P1`, `REF-P2`...**: um prompt de character sheet por personagem principal (frente,
   três quartos e perfil, corpo inteiro e close de rosto, fundo neutro, mesma roupa da cena),
   `GERAR DO ZERO`, gerado e **aprovado antes de qualquer K**.
3. Cada `K__` diz no mapa (fora do bloco) quais `REF-P` anexar, e **também descreve o personagem por
   escrito**, porque o prompt continua autossuficiente.
4. A protagonista do movie style de venda ganha **dois** sheets, um por estado de corpo. O segundo
   sai por edição do primeiro, aprovado, nunca em cascata.
5. O rosto de um personagem nunca se repete em outra conta (checklist B8).
6. **A parte 2 reaproveita os sheets da parte 1.** O elenco é o mesmo, e é isso que faz a parte 2
   parecer continuação.

---

## 3. SHORT FORM (growth): o workflow

### S1 · Decomposição (`/watch`)
**Entrego no chat**, sem copy ainda:

| t | Beat | Quem fala | Fala literal | Plano |
|---|---|---|---|---|
| 0.0 | TRANSGRESSÃO | [agressor] | "..." | [aberto / close] |
| ... | ... | | | |
| fim | CORTE (aberto ou fechado) | | | |

E a **lista de TODOS os momentos WTF**, sem número fixo: segundo, quem provoca, tipo (transgressão,
virada de status, revelação de passado, escalada física, segunda crueldade) e se é falado ou
visual. Mais o motivo banal, o tipo de final, o elenco (quem é principal e quem aparece uma vez) e
o cenário.

### S2 · Modelagem da copy: como eu penso
É crescimento, então vale `feedback-growth-video-sem-venda`: **clonar quase palavra por palavra**.
Zero ponte, álibi, produto ou keyword.
1. **Nenhum WTF do modelo some**, e o espaçamento entre eles se preserva. A frase de transgressão e
   o motivo banal não se tocam.
2. **Ajusto só o necessário:** nome próprio, gíria que não soa americana, referência que o público
   dos EUA não pega, e fala acima de 29 palavras por take (quebra em fim de frase, nunca filler).
3. **Marco o ponto de corte.** Final aberto: o último frame é o rosto da vítima ANTES de reagir, ou
   a promessa de consequência dita pelo agressor. Final fechado: a sentença numa frase.
4. **Série opcional pelo Puzzle:** controle (clone) + variações trocando UMA variável (`AGRESSOR`,
   `VÍTIMA`, `EVENTO`, `MOTIVO BANAL` ou `VIRADA`).

**Entrego:** roteiro com rótulo de quem fala, contagem por take e o texto do card final.
**Espero aprovação.**
```
### T1 · TRANSGRESSÃO · DIÁLOGO · Setup A
> AGRESSOR: "..."
> VÍTIMA: "..."
(palavras: NN)
```

### S3 · Pacote
1. Instruções do agente Flow (perfil CLÁSSICO), coladas inteiras
2. Fichas do elenco + bloco `REF-P` (character sheets), para gerar e aprovar primeiro
3. Bloco único de imagem (`K01`...), com o mapa de anexos fora do bloco
4. Bloco único de vídeo (`V01`...)
5. Mapa K/V e CapCut: ordem dos clipes, cortes, card `follow to part 2` e quanto tempo fica
6. `Checklist de envio: X/X aprovados`
7. Transcrição final EN e PT

**Custo típico:** 2 a 3 REF, 2 a 4 K e 2 a 4 V para 15 a 25s.

### S4 · Parte 2 (só quando o Luigi pedir)
Ele reenvia o vídeo que fizemos e pede a parte 2. Ela é uma **produção própria**: abre no exato
ponto em que a parte 1 cortou (a reação da vítima), reaproveita os `REF-P` da parte 1 e segue o
mesmo formato.

---

## 4. MOVIE STYLE DE VENDA: o workflow

### M1 · Decomposição (`/watch`)
**Entrego:** o modelo encaixado no esqueleto de 17 beats (`MOVIE_STYLE_VENDA.md`), com fala
literal por beat, e cinco leituras: versão do pitch ("28 dias" ou "diagnóstico no corpo"), tipo de
ponte até a mentora, mecanismo do problema e da solução, elenco por papel, onde a venda entra (%)
e como fecha.

### M2 · Copy: de trás para frente
O pitch é o ativo e o ato 1 é trocável, então escrevo nesta ordem:
1. **Mecanismo e ponte do ângulo**, encaixados na arquitetura do modelo: vilão escondido → leitura
   fria de 3 sintomas → *"it works on the X side, so what you're doing finally gets through"*.
2. **Bloco de pitch, escrito UMA vez:** álibi na primeira frase da mentora, objeção como pergunta,
   **a solução só depois que a protagonista pergunta**, obstáculo de mercado, CTA do ângulo, follow
   com motivo.
3. **A ponte até a mentora** (seção 5 para a FityWell).
4. **O ato 1, pelo Puzzle do modelo:** humilhação com figura de comparação, idade como prova,
   esforço, abandono. O médico que falha pode entrar (decisão 2).
5. **O fechamento de vingança.**
6. **Crivos do P2:** crivo de copy, `compliance-riscos`; na FityWell o "nunca culpar ela" roda
   duas vezes.

**Entrego:** tabela `# | Beat | Original | Adaptado`, roteiro cena a cena com rótulo de quem fala,
contagem por take, só-fala e o claim mais arriscado. **Espero aprovação.**

### M3 · Ganchos
As 10 variações mexem **só no ato 1**, pelo Puzzle com degrau e pela skill `gancho-verbal`.
**Espero a escolha.**

### M4 · Pacote
A ordem do S3, com a mentora = avatar do ângulo (âncora anexada), a protagonista com dois sheets,
o K de corpo neutro ao gancho e o linter com zero falhas.
**Custo típico:** 3 a 5 REF, 10 a 16 K e 12 a 15 V.

---

## 5. Por ângulo

| | FityWell (2) | Auraly (3) |
|---|---|---|
| Família | **A**, mentora dentro da cena | **B**, indicação e corte seco |
| Mentora | Dana, Jamie ou Lynn (homens, coach) | a avatar entra depois do corte |
| Produto em quadro | **não** | **não** |
| CTA | `yes` + quiz | `222` primeiro, Stories depois |
| Travas extras | nunca culpar ela (2x) | rosto lacrado, registro divino, preço nunca dito |
| Short form | tema pelo público da conta, zero produto | idem |

**Pontes para mentor HOMEM (FityWell).** A estranha que aborda a mulher chorando (*"come see me"*)
soa como assédio na boca de um homem desconhecido. As pontes da amostra que funcionam:
1. **amiga passa o número** e a protagonista liga para agendar (DJ1, DJ2);
2. **a figura da comparação indica** (DJ6, DJ7, RT3);
3. **vídeo no celular:** a amiga mostra o vídeo do coach falando para a lente (RT3).

---

## 6. Prompt de vídeo com DIÁLOGO e VOZ DESCRITA

**Ficha de voz:** cada personagem que fala ganha uma descrição de timbre fixa (idade aparente,
grave ou aguda, rouca ou limpa, ritmo, sotaque americano de quem), escrita uma vez na ficha do
elenco e **copiada igual em todo V** em que ele fala. A emoção muda por fala; o timbre não.

```
falas no take, em inglês, na ordem:
1. [PERSONAGEM A, descrição visual curta], voz [FICHA DE VOZ DE A], fala com [entonação/emoção desta fala]: "[FALA EXATA]"
2. [PERSONAGEM B, descrição visual curta], voz [FICHA DE VOZ DE B], responde com [entonação/emoção]: "[FALA EXATA]"
[PERSONAGEM C] fica em silêncio o tempo todo.

cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última
palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de
quem está falando.

o que acontece no vídeo: [ação enxuta]

câmera: [como se alguém da plateia estivesse filmando, com troca de plano para a reação]

som ambiente: [ambiente], sem música
```
No máximo **2 pessoas falando por clipe**, 13 a 29 palavras somando as falas, quem cala está
escrito. O take de um só falante usa a mesma linha, com um item.

---

## 7. O que precisa ser construído antes da primeira produção

| Peça | O que muda | Status |
|---|---|---|
| Checklist de envio | B9 (médico em cena), C2 (voz por personagem), D1 (sem Voice Changer) | ✅ feito em 2026-09-23 |
| `checar_entrega.py` | ler TODAS as falas rotuladas de um take, somar palavras, comparar a fala literal na ordem, aceitar o bloco "falas no take" | a fazer |
| `INSTRUCOES_AGENTE_FLOW.md` v13 | o executor reconhece V com diálogo (as 3 marcas continuam) e anexa os `REF-P` indicados no mapa, além da âncora | a fazer |
| `CLAUDE.md` | registrar a exceção: no movie style o `REF-P` é anexado (hoje o formato do Flow diz que REF não entra e o anexo é só a âncora) | a fazer |
| Gabarito vivo | a primeira produção de cada formato vira o gabarito | depois da 1ª produção |
