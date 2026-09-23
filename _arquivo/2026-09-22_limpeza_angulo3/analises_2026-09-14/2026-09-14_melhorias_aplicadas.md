# Melhorias aplicadas em 14/09/2026

A partir da autorização para executar as propostas da análise, foram implementadas três frentes: alinhamento documental, biblioteca criativa e medição por publicação. Esta nota é um registro de manutenção, não um workflow de produção.

## Alinhamento da operação

- `WORKFLOW_AURALY.md` continua sendo a fonte operacional de Auraly. Passou a explicitar objetivo SALE/GROWTH, autoridade do checkpoint sobre vistas da fila, identidade estável do avatar, diferença entre entrega de prompts e publicação e limites da validação mecânica.
- `CLAUDE.md`, `PLAYBOOK_MESTRE_AURALY.md`, `AURALY_AGENT.md` e `CONHECIMENTO_PROMPT_IMAGEM.md` receberam delimitação de escopo para impedir que instruções históricas concorram com o roteador atual.
- `PLAYBOOK_FITYWELL.md` distingue o pacote histórico 1:1 do casamento clássico por maior K anterior ou igual ao V.
- `producao/_flow/INSTRUCOES_AGENTE_FLOW.md` documenta perfis separados: Auraly preserva quatro imagens com seleção manual, três variações de vídeo e K/V com mesmo número; clássico mantém uma imagem final, uma variação de vídeo e casamento por maior K anterior. O executor continua subordinado ao workflow e às esperas de aprovação.
- `.claude/hooks/gabarito_hook.py` passou a rotear, sem copiar configurações ou apresentar o playbook histórico como fonte operacional.

A fila da produção `barbie_the_aries_1_kris_robin_shelby_casey` foi sincronizada por nome com o checkpoint: quatro DONE e PRODUCTION_COMPLETE. O checkpoint recebeu `Objective: SALE`, coerente com o roteiro de Stories existente. Não foram criadas aprovações nem alteradas falas ou prompts dessa produção. Produções antigas sem checkpoint continuam identificadas como histórico.

## Validação documental

`auraly_validacao.py` e a integração em `checar_entrega.py` acrescentam leitura de pacotes limpos K/V na raiz ou em subpastas, detecção de códigos duplicados, comparação literal de falas, cobertura de roteiro, casamento de imagem/vídeo e consistência de estado. Crescimento explicitamente documentado não exige Stories; a transcrição do vídeo modelo não define o objetivo da adaptação. O gate também reconhece `two two two` na ordem de CTA e na regra do gesto de comentar.

O modo `--estrito` exige checkpoint. O modo padrão avisa quando o histórico não permite verificar estado e aprovações. A correspondência K/V por identidade numérica é aplicada aos pacotes com checkpoint Auraly; históricos sem checkpoint não recebem essa certificação. A checagem continua documental: não comprova seleção visual, geração, renderização, publicação ou performance. Arquivos nomeados como lote/ciclo não recebem afirmação de cobertura integral.

## Biblioteca e resultados

A entrada de uso é [controle/README.md](../controle/README.md).

- [Biblioteca criativa](../controle/BIBLIOTECA_CRIATIVA.md): 36 roteiros indexados, separados entre as três ofertas oficiais e o Angle 4 histórico. O JSON preserva metadados documentados, abertura, referências e fontes. Campos ausentes permanecem vazios; dois roteiros sem headings de takes compatíveis têm zero takes reconhecidos, o que não significa vídeo sem cenas.
- [Rotas de consulta](../controle/ROTAS_DE_CONSULTA.md): exemplos por necessidade criativa e hipóteses que podem ser medidas, sem tratar afirmações de performance dos documentos como comprovação.
- [Resultados](../controle/RESULTADOS.md): registro por publicação com identidade, hook, objetivo, canal, coleta, métricas e custos. Nenhuma métrica foi inventada; a base inicial está vazia.
- `gerenciar_operacao.py`: atualiza índices/relatório, busca por ângulo e termo, valida registros e permite visualizar ou aplicar sincronização de fila por identidade. Não muda etapas nem gera mídia.

## Verificação executada

| Verificação | Resultado |
|---|---|
| Testes automatizados de pacotes, estado, identidade e métricas | 16 passaram |
| Hook: pedido operacional, saudação e payload inválido | 3 cenários passaram |
| Auraly Barbie, modo estrito | 0 falhas, 0 avisos; 48 prompts V examinados |
| Auraly Olivia, crescimento histórico | 0 falhas; avisos sobre conferência visual e ausência de checkpoint; 120 ocorrências de prompts V examinadas |
| FitWell pernas | 0 falhas; aviso de conferência visual |
| Korella Melody açúcar | 13 falhas de faixa de palavras, já presentes antes desta manutenção; saída anterior e atual idênticas |
| Biblioteca | 36 registros com oferta identificada; links locais de controle verificados |
| Base de resultados vazia | Estrutura validada; sem dados de performance |

As 120 ocorrências de Olivia incluem representações repetidas em arquivos de entrega; não são 120 vídeos únicos. As 13 falhas de Korella foram registradas, não corrigidas por reescrita automática de copy histórica.

A [saída das verificações](2026-09-14_validacao_melhorias.txt) fica preservada para consulta. Não foi executada uma validação integral de todos os pacotes históricos. Não há repositório Git nesta pasta, portanto não houve commit.

Para usar agora: consulte a biblioteca por oferta; após publicar, registre os dados reais em `controle/resultados.json` e execute `python3 gerenciar_operacao.py atualizar`. Comparações devem manter oferta, objetivo, conta e janela compatíveis.
