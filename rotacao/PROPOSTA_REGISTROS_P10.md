# Proposta de registros do P10 (log de rotação + biblioteca-videos)

Levantado em 2026-10-05 a partir de `python checar_rotacao.py` e das pastas em `producao/`.
Nada foi editado ainda. Depois do seu ok eu escrevo na memória viva, rodo `bash sync_memoria.sh`,
`checar_memoria.py` e `checar_rotacao.py`, e só faço commit/push com a sua confirmação.

## O que o levantamento mostrou

1. **`controle/resultados.json` está vazio.** Não há nenhuma publicação registrada, então eu não sei
   quais destes vídeos foram ao ar. O P10 manda registrar **depois** da postagem. Proposta: tudo entra
   como `PREPARADO, sem publicação confirmada` (o mesmo formato já usado no log em 2026-09-05), e vira
   publicado quando você disser quais foram.
2. **Só 5 dos 25 pacotes consumiram rota argumentativa.** Os outros 20 são growth (clone literal, sem
   bloco de venda) ou Auraly (fecha em ritual, sem argumento), e não queimam rota. Eles entram no log
   numa linha curta "sem rota" só para fechar o aviso.
3. **Conflito na conta da Brandon: a rota 7 foi usada duas vezes seguidas.** `brandon_maca_alho`
   (roteiro aprovado em 2026-10-01) e `fitywell_brownie_feijao` (2026-10-02) dizem os dois que a rota 7
   "ainda está livre". Se os dois forem ao ar, a regra de rotação foi quebrada. Decisão sua: postar só
   um deles com a rota 7, ou aceitar e registrar a repetição.
4. **Falso positivo do checador:** `fitywell_pernas` e `fitywell_dentes` aparecem como presentes na
   biblioteca, mas o casamento foi por token ("pernas", "dentes" em textos de outros casos). Os dois
   também estão fora. A biblioteca real tem **25** faltando, não 23.
5. **Bug do checador:** os 6 pacotes `auraly_*` saem como ângulo "?" ou "1" em vez de 3, então caem na
   lista de dívida em vez da lista "Ângulo 3, pode ser legítimo". Posso corrigir a detecção no
   `checar_rotacao.py` (lendo `pipeline: auraly`) no mesmo commit, se você quiser.

## A. Log de rotas (banco-rotas-argumentativas, seção "Log de rotas usadas")

### Pacotes que consumiram rota (linhas novas na tabela principal + logs por conta)

| Data | Vídeo | Ângulo | Rota usada |
|---|---|---|---|
| 2026-09-10 | Pernas / bicarbonato (Dana, Jamie, Lynn) `producao/fitywell_pernas/` | 2 | Rota "uma das três causas", **nomeadas** (hormônios, metabolismo, intestino) + álibi no CTA |
| 2026-09-10 | Água de arroz / intestino (Dana, Jamie, Lynn) `producao/fitywell_arroz/` | 2 | Rota "uma das três causas", a água só toca o intestino + álibi no T6 |
| 2026-09-10 | Churrasco, movie style integral (Dana DONE, Lynn ACTIVE, Jamie PENDING) `producao/dana_churrasco/` | 4 | Mecanismo do mostrador (sono, carga, cintura) + álibi "it is not your age, it is your playbook". Obstáculo: **rota de fuga A**, "eu acho isso de graça na internet" (T13) |
| 2026-10-01 | Alho na maçã que espuma (Brandon) `producao/brandon_maca_alho/` | 2 | **Rota 7** (a receita sem diagnóstico). Virada por **contagem quebrada** (gatilho 1, o quinto ingrediente). Obstáculo novo: o app de graça escreve a mesma receita pra todas |
| 2026-10-02 | Brownie de feijão preto (Brandon) `producao/fitywell_brownie_feijao/` | 2 | **Rota 7** de novo ⚠️. Virada por **escalada de magnitude** (gatilho 2). Obstáculos: custo de tempo de fazer sozinha + app de caloria grátis |

Acréscimos nos logs por conta:
- **Brandon:** maçã/alho (rota 7, contagem quebrada) e brownie (rota 7, escalada de magnitude).
  "Ainda disponíveis" passa a ser rotas 1, 2, 4 e 6; gatilhos perda ativa e pergunta sem saída.
- **Dana, Jamie e Lynn (Ângulo 2):** log novo por conta, com pernas e arroz (três causas nas duas).
  ⚠️ As duas usaram a mesma rota nos mesmos três avatares, então a próxima venda deles precisa de outra.
- **Dana e Lynn (Ângulo 4):** log novo, churrasco (mostrador + rota de fuga A).

### Pacotes sem rota (uma linha só, agrupada)

> **Sem rota consumida (growth, clone literal, ou Ângulo 3 sem beat de argumento):**
> `fitywell_barriga_verao`, `fitywell_cheesecake`, `fitywell_dentes`, `fitywell_growth_canela_acucar`,
> `fitywell_growth_cortisol_cintura`, `fitywell_growth_cortisol_props`, `fitywell_growth_dentes_agua`,
> `fitywell_growth_froyo_bites`, `fitywell_growth_modelo_intestino`, `fitywell_growth_salmao_agua`,
> `fitywell_growth_wentao_healer`, `brandon_pao_sementes`, `brandon_pes_peroxido`, `sf_madrasta_frango`,
> `auraly_growth_sal_tenis`, `auraly_growth_prece`, `auraly_growth_dinheiro`, `auraly_growth_maos_vidro`,
> `auraly_venda_fortuna`, `auraly_manifestacao_outubro`.

## B. Biblioteca-videos (25 entradas novas, numeradas a partir de 33)

Formato curto: número, nome, caminho, data, modelo, avatares, esqueleto, o que não repetir.

**Ângulo 2 (FityWell)**
- **33. Pernas / bicarbonato** · `producao/fitywell_pernas/` · 2026-09-10 · herbalista asiático, 28s · Dana, Jamie, Lynn (COACH) · pó num modelo de pernas com glóbulos amarelos, espuma, pele lisa → receita → protocolo → ponte das 3 causas → álibi → `yes` + quiz. ⭐ Gabarito vivo do P5. Não repetir: três causas nestes três avatares.
- **34. Água de arroz / intestino** · `producao/fitywell_arroz/` · 2026-09-10 · casal idoso, 22s · Dana (pacote entregue), Jamie e Lynn PENDING · erro doméstico (despejar a água pelo ralo) com o modelo de intestino no lugar do couro cabeludo → demo → mecanismo → três causas. Não repetir: três causas, ralo.
- **35. Barriga antes do verão** · `producao/fitywell_barriga_verao/` · 2026-09-12 · 12s, um take · Dana, Jamie DONE, Lynn ACTIVE · bastão aponta do tronco obeso ao magro, "one simple ingredient", growth.
- **36. Cheesecake de iogurte grego** · `producao/fitywell_cheesecake/` · Dana, Jamie, Lynn DONE · receita fit + forno + benefícios + sono, growth com `comment cheesecake`.
- **37. Clareador dental caseiro** · `producao/fitywell_dentes/` · 2026-09-17 · Dana, Jamie, Lynn DONE · modelo dental manchado molhado, pasta de coco, growth. Mesmo esqueleto do caso 6 (Andrew_Heals).
- **38. Gengibre sob a língua** · `producao/fitywell_growth_wentao_healer/` · 2026-09-19 · 29s · fila de 10 · cliente 40+ com gengibre na língua, coach aponta, pausa da vontade de beliscar, growth.
- **39. Pernas, vestido e braço (cortisol)** · `producao/fitywell_growth_cortisol_props/` · 2026-09-19 · fila de 9 · comparação de props de corpo com luvas azuis, 4 ganchos num corpo só, growth.
- **40. Jeans, cinto e blusa (cortisol)** · `producao/fitywell_growth_cortisol_cintura/` · 2026-09-19 · fila de 9 · variação do 39 trocando a zona (cintura), roteiro v2 aguardando aprovação.
- **41. Canela sobre o açúcar da barriga** · `producao/fitywell_growth_canela_acucar/` · 2026-09-23 · James Smith, 26s · fila de 9 · canela desaba montanha de açúcar num manequim → receita → `yes`. Parente do caso 12 (Melody).
- **42. Água lavando o modelo dental** · `producao/fitywell_growth_dentes_agua/` · 2026-09-24 · 37,7s · fila de 9 · mesmo nicho do 37, outro modelo; precedente de voz fora de quadro saindo do próprio clipe.
- **43. Froyo bites anti-inflamatórios** · `producao/fitywell_growth_froyo_bites/` · 2026-09-25 · orgânico, 13,8s, 36 jump cuts · fila de 6 · receita POV, save + follow.
- **44. Modelo transparente de intestino e chá de limão** · `producao/fitywell_growth_modelo_intestino/` · 2026-09-25 · 53,7s · fila de 5 · bloco de produto Amazon de terceiro removido, growth.
- **45. Salmão na água quente, peixe na fria, brócolis no vinagre** · `producao/fitywell_growth_salmao_agua/` · 2026-10-02 · Jake Miller Health, 30s · Eva ACTIVE, Brandon PENDING · família de inspeção de comida (mesma do `fitywell_inspecao`), testes diferentes.
- **46. Pão de sementes sem farinha** · `producao/brandon_pao_sementes/` · 2026-09-29 · 27,7s · Brandon · chia na água morna → receita → `yes`, growth.
- **47. Spray de peróxido nos pés** · `producao/brandon_pes_peroxido/` · 2026-09-29 · 48,8s · Brandon · WD-40 trocado por peróxido, espuma no pé → escalda-pés com bicarbonato, growth. Parente do caso 15 (Melody), outra conta.
- **48. Alho na maçã que espuma** · `producao/brandon_maca_alho/` · 2026-10-01 · Ken.remedie, 38,7s · Brandon · VENDA: maçã + alho espumando → suco → bloco de venda com plano Metabolic Reset no comentário fixado. Não repetir: rota 7, contagem quebrada.
- **49. Brownie de feijão preto** · `producao/fitywell_brownie_feijao/` · 2026-10-02 · Chef Joey, 32,5s · Brandon · VENDA: receita → bloco de venda (rota 7, escalada de magnitude, três causas). Não repetir: rota 7, escalada de magnitude.
- **50. Madrasta e o frango (short form)** · `producao/sf_madrasta_frango/` · 2026-09-24 · 25s, 9 planos · elenco próprio, sem avatar fixo · movie style de growth, card "follow to part 2".

**Ângulo 3 (Auraly)**
- **51. Sal no tênis de trabalho** · `producao/auraly_growth_sal_tenis/` · 2026-09-29 · avatar IA, 114s · Darlene, Lorraine, Walt · growth, "keep your mouth shut" + selos + follow.
- **52. Prece de mãos juntas** · `producao/auraly_growth_prece/` · 2026-09-29 · orgânico, 117s · Darlene, Lorraine, Walt · mesmo script do 51 com frases reescritas.
- **53. Perfume nos pés (dinheiro)** · `producao/auraly_growth_dinheiro/` · 2026-09-29 · avatar IA, 130s · Darlene, Lorraine, Walt · growth de dinheiro, cinco takes reescritos contra repetição.
- **54. Sal no prato dourado, 11:11 (fortuna)** · `producao/auraly_venda_fortuna/` · 2026-09-29 · avatar IA, 125s · Darlene, Lorraine, Walt · VENDA, ramificação dinheiro, `222` → Stories.
- **55. Embaralhando o tarô, datas de outubro** · `producao/auraly_manifestacao_outubro/` · 2026-09-30 · orgânico, 53s · Darlene, Lorraine, Walt · VENDA, datas cravadas 1 a 3 de outubro (vídeo envelhece depois disso).
- **56. Mãos na mesa de vidro** · `producao/auraly_growth_maos_vidro/` · 2026-10-02 · orgânico, 100s · Morgan Vance · mesmo script do 51/52, literal porque a conta é nova.

**Ângulo 4 (Body Hacks)**
- **57. Churrasco, movie style integral** · `producao/dana_churrasco/` · 2026-09-10 · Diane Jackson, 94,7s · Dana DONE, Lynn ACTIVE, Jamie PENDING · primeiro movie style integral da FityWell: elogio ao rival → farpa → exames normais → picape → mentor → o mostrador da manhã → livro + $9.90 + `yes`.

Observação: as datas são as do próprio pacote (roteiro ou fila), não de postagem.
