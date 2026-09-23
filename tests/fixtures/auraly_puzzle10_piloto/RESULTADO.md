# Resultado do lote piloto Auraly - 10 variacoes por Puzzle

Data: 2026-09-20
Escopo: fluxo documental completo, da ideacao ao pacote K/V de um avatar, sem geracao de midia.

♻️ **Regenerado em 2026-09-20.** A versao anterior deste piloto usava o contrato `4 + 3 + 3` em
tres familias, revogado pelo Luigi na mesma data. A pasta se chamava `auraly_portfolio_433_piloto`.
O lote atual usa o contrato vigente: **uma acao estrutural tirada do hook do video modelo, 10
variacoes, uma variavel trocada em cada**, que e o mesmo metodo do Angulo 2.

Comando executado:

```text
python3 checar_entrega.py tests/fixtures/auraly_puzzle10_piloto --estrito
```

Resultado observado:

- 10 verificacoes aprovadas, 0 avisos, 0 falhas;
- acao estrutural preservada e reconhecida;
- 10 hooks reconhecidos, com uma unica variavel trocada em cada;
- nenhum travessao nos arquivos;
- keyword `222` presente;
- 3 takes falados, todos dentro de 13 a 29 palavras, com o T1 corretamente mudo;
- secoes obrigatorias do `ROTEIRO.md` no formato auraly;
- objetivo GROWTH documentado, entao Stories nao e exigido;
- nenhuma fala cita preco;
- travas do Angulo 3 respeitadas;
- 8 prompts V examinados em 2 arquivos de pacote;
- hooks 1, 4, 10, 9 e 6 bloqueados para o pacote piloto;
- reutilizacao deliberada de K06 por V06 e V07 mantida;
- V08 ligado explicitamente ao CTA K10;
- checkpoint encerrado em `PRODUCTION_COMPLETE` com a fila concluida.

Testes negativos automatizados (`PYTHONPATH=. python3 tests/test_operacao.py`, 24 testes) confirmam
que o validador reprova contagem diferente de 10, acao estrutural ausente, duas variaveis centrais
no mesmo hook, formato historico em modo estrito e **tambem o contrato 4/3/3 em familias**, que
passou a ser explicitamente invalido.

Validacao mecanica nao comprova realismo, qualidade criativa, renderizacao, publicacao nem
resultado comercial.
