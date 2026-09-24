# Short form · Madrasta e o frango | Ângulo 2 (FityWell) | Pacote de Prompts

formato: short-form
tipo: crescimento

Vídeo modelo: `Muszynski Venetia_Cheguei em casa mais ced_2855227928192545_1080p_20260923.mp4` (25,15s)

Âncora: **nenhuma** (short form sem avatar fixo). A identidade de cada personagem vem do seu
character sheet `REF-P`, gerado e aprovado antes de qualquer K.

Funil: nenhum. Card `follow to part 2` na edição.

Gerado por `gerar_pacote.py` (fonte única dos prompts). Nunca editar este arquivo à mão: editar o
gerador e rodar de novo.

---

## Índice de geração

| Ordem | Código | Take | Anexar | Ação de geração |
|---|---|---|---|---|
| 1 | REF-P1 | | nada | GERAR DO ZERO. Character sheet da MADRASTA |
| 2 | REF-P2 | | nada | GERAR DO ZERO. Character sheet do PAI |
| 3 | REF-P3 | | nada | GERAR DO ZERO. Character sheet da EMILY |
| 4 | REF-P4 | | nada | GERAR DO ZERO. Character sheet do FILHO |
| 5 | K01 | T1 | REF-P3, REF-P1, REF-P2 + composição | GERAR DO ZERO. Emily estica a mão para o frango, o pai na porta |
| 6 | K02 | T2 | REF-P2, REF-P3 + composição | GERAR DO ZERO. O pai segura Emily chorando, marcas na bochecha |
| 7 | K03 | T3 | REF-P2, REF-P1 + composição | GERAR DO ZERO. Inserto: o prato de frango e a tigela de arroz |
| 8 | K04 | T4 | REF-P1, REF-P2 + composição | GERAR DO ZERO. A madrasta de braços cruzados |
| 9 | K05 | T5 | REF-P4, REF-P1, REF-P2 + composição | GERAR DO ZERO. O filho encara a mãe do outro lado da ilha |
| 10 | K06 | T6 | REF-P4 + composição | GERAR DO ZERO. Inserto: a mão tira o iPhone do bolso |
| 11 | K07 | T7 | REF-P1 + composição | GERAR DO ZERO. Close do rosto travado da madrasta |

Regra de bolso: **os `REF-P` saem primeiro e sem anexo. Cada K anexa os `REF-P` aprovados, na
ordem da tabela, e por último o frame de composição do modelo.** Todo K é GERAR DO ZERO a partir
dos sheets; nenhum K é editado de outro K, então não existe cascata.

---

## Fichas do elenco e de voz

| Código | Personagem | Aparência | Ficha de voz (igual em todo V) |
|---|---|---|---|
| REF-P1 | MADRASTA | branca, ~40, loira platinada de coque baixo, sardas leves, blusa de seda creme, calça preta, brincos de ouro pequenos | voz feminina de uns quarenta anos, média-aguda, fria e cortante, sotaque americano padrão |
| REF-P2 | PAI | negro, ~42, barba curta, cabelo bem curto, camisa social azul-marinho, relógio prateado | voz masculina grave de barítono, uns quarenta anos, sotaque americano de homem negro |
| REF-P3 | EMILY | negra, ~6, marias-chiquinhas com elásticos rosa, vestido rosa de babados | voz de menina de seis anos, fina e aguda, sotaque americano |
| REF-P4 | FILHO | negro, ~8, cabelo raspado, camisa oxford azul-clara, calça cáqui, cinto marrom, iPhone azul no bolso | voz de menino de oito anos, clara e ainda infantil, sotaque americano |

A emoção muda a cada fala; o timbre não muda nunca (checklist C2).

---

## Trava de identidade e continuidade

- Os quatro personagens saem **sempre** dos seus `REF-P`, com a mesma roupa, o mesmo cabelo e os
  mesmos acessórios em todos os K. Nada de troca de figurino.
- A MADRASTA mantém o coque baixo e a blusa creme; o PAI, o relógio prateado no pulso esquerdo;
  EMILY, os elásticos rosa; o FILHO, o iPhone azul no bolso direito.
- **As marcas na bochecha de Emily só existem a partir do K02.** No `REF-P3` e no K01 o rosto dela
  está limpo.
- Cenário único, igual em todos os K: cozinha americana branca, ilha de bancada cinza, porta para o
  corredor ao fundo, janela sobre a pia com céu nublado, **ímã de bandeira dos EUA na geladeira**.
- Luz neutra de dia nublado, sem tom quente, tudo em foco.
- Nenhum rosto pode repetir o do vídeo modelo nem o de outra conta (checklist B8). O frame de
  composição serve só para posição de câmera e das pessoas.

## Trava do prop herói

```text
A white plate piled high with golden fried chicken pieces and, right next to it, a small grey bowl of
plain cold white rice, on the light grey quartz countertop of the kitchen island, very close to the
lens in the lower foreground, large in frame, closer to the camera than any face.
```

É a prova do motivo banal (frango para o filho dela, arroz frio para a filha dele). Aparece em K01,
K02, K03, K04 e K05.

## Trava da 2ª pessoa (REF-P, character sheets)

Os quatro personagens são principais, porque todos aparecem em mais de um clipe ou precisam ser
reconhecidos entre cenas. Não há figurante nem personagem de uma aparição só. **Gerar os quatro
`REF-P` e aprovar antes do primeiro K.**

---

# Prompts de imagem

{{REFS}}
{{KS}}
---

## Bloco global de vídeo

```text
falas no take, em inglês, na ordem:
1. [QUEM FALA, descrição visual curta], [FICHA DE VOZ], fala [EMOÇÃO DESTA FALA]: "[FALA EXATA DO ROTEIRO]"
2. [QUEM RESPONDE, descrição visual curta], [FICHA DE VOZ], fala [EMOÇÃO]: "[FALA EXATA DO ROTEIRO]"
[QUEM FICA CALADO] não diz nenhuma palavra.

cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de quem está falando.

o que acontece no vídeo: [ação enxuta]

câmera: leve handheld, como alguém na cozinha filmando com o celular, sem trocar de plano

som ambiente: cozinha silenciosa de casa, [som da cena], sem música
```

No B-roll a primeira parte vira `(sem fala no take: ...)` e a linha do lip sync sai.

---

# Prompts de vídeo

{{VS}}
---

## Mapa de âncoras

| Código | Anexar, nesta ordem | Observação |
|---|---|---|
{{MAPA}}

Imagem: Nano Banana 2, 9:16, 1 imagem final por código (perfil CLÁSSICO).
Vídeo: Veo 3.1 Lite, Lower Priority, 8 segundos, 1 variação, imagem como INITIAL FRAME.
`V01` usa `K01`, e assim por diante, pelo número.

---

## Montagem no CapCut

1. **Ordem dos clipes, numerados:** V01, V02, V03, V04, V05, V06, V07.
2. **V01 (~4,5s):** cortar logo depois de "What did you do to my daughter?".
3. **V02 (~5s) + V03 (~2s):** quando o pai começa "Why does my daughter only get cold rice?", cortar
   para o V03 (o dedo apontando o prato) com a voz dele continuando por cima, e voltar ao V02 para a
   última fala de Emily.
4. **V04 (~3,5s):** a explosão, do descruzar dos braços até ele segurá-la.
5. **V05 (~6s) + V06 (~1,5s) + V07 (~2s):** no "I recorded everything, Mom.", cortar para o V06 (o
   celular saindo do bolso) com a voz por cima; no "Even what you did afterwards.", cortar para o
   V07 (o rosto travado) com a voz por cima.
6. **Card final:** `follow to part 2`, texto grande e centralizado, sobre o último frame do V07,
   por ~1,5s. Nada falado.
7. Cortar todo silêncio antes da primeira fala de cada clipe (checklist D2).
8. **Sem música** no vídeo inteiro; só o som da cena.
9. **Sem Voice Changer** (checklist D1). A voz de cada personagem vem descrita no prompt.
10. Rótulo pequeno `AI-generated` num canto (checklist D4).
11. Exportar em 9:16, 1080 por 1920. Duração final alvo: ~25s.

---

## Gates de qualidade

1. [ ] Os quatro `REF-P` foram aprovados antes do primeiro K.
2. [ ] O mesmo rosto, cabelo e roupa de cada personagem em todos os K.
3. [ ] Nenhum rosto parecido com o do vídeo modelo.
4. [ ] As marcas na bochecha de Emily aparecem do K02 em diante, nunca antes.
5. [ ] O prato de frango e a tigela de arroz estão no primeiro plano, perto da lente, onde pedidos.
6. [ ] O ímã de bandeira dos EUA aparece e está em foco em todos os K.
7. [ ] Luz neutra de dia nublado, céu com textura na janela, nenhuma imagem com tom quente.
8. [ ] Zero blur em qualquer imagem.
9. [ ] Em cada V de diálogo, a fala saiu na boca certa (checklist C3).
10. [ ] A voz de cada personagem soa igual em todos os clipes em que ele fala.
11. [ ] A fala de cada V bate palavra por palavra com o `ROTEIRO.md`.
12. [ ] O card `follow to part 2` entra sobre o último frame, sem fala.
13. [ ] `python3 checar_entrega.py producao/sf_madrasta_frango` fechou sem FALHA.
