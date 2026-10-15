# Aprendizado de edição — referências do Luigi, 2026-10-11

Pedido: estudar cinco referências, melhorar a edição automática, registrar e
commitar antes da prática. Aplicação principal **FitWell e Sea Moss**.
Auraly só recebe decisões adaptadas à oferta, nunca herança automática deste estudo.
Este documento complementa `pos-producao-edicao-regras.md`; não substitui o
comando único nem os gates de fala, imagem, roteiro ou entrega.

## Evidências

| ID na ordem enviada | Arquivo original | Duração | Palavras/s lexical ASR no vídeo inteiro | Aprendizado mais claro |
|---|---|---:|---:|---|
| V01 | snapinsta-1791763841045.mp4 | 43,47 s | 3,04 | Ação inicial antes de falar, legenda hierárquica e CTA em quadro maior |
| V02 | snapinsta-1791764012212.mp4 | 55,22 s | 3,35 | Close → demonstração → close com objeto; cursiva e pequenos destaques |
| V03 | snapinsta-1791763924795.mp4 | 48,83 s | 3,69 | Payoff visual sem fala 2,44–3,82 s; produto em uso |
| V04 | snapinsta-1791763902279.mp4 | 57,03 s | 3,38 | Ação e reação sem fala 1,70–4,66 s; corte após completar acontecimento |
| V05 | snapinsta-1791763875945.mp4 | 71,80 s | 3,47 | Payoff 5–6,76 s e câmera overhead para mostrar produto aos 35,90 s |

Detalhamento: `analises-edicao-2026-10-11-v01-v02.md` e
`analises-edicao-2026-10-11-v03-v05.md`. Fontes, SHA256, manifests, transcrições,
RMS/LUFS e registro de leitura em `evidencias-edicao-2026-10-11/`.
Todas as grades completas foram abertas pelo analista responsável. Frames
críticos selecionados ficam versionados; grades densas e MP4 ficam locais.
Não há inferência de performance comercial a partir de preferência de edição.

## Decisões que entram na prática

1. **Remover espera inútil, preservar ação útil.** Pausa sem fala com
   transformação, gesto de produto ou reação não é automaticamente descartável.
   O operador identifica intervalo e razão a partir do vídeo/takes vistos.
   Fora dos intervalos marcados, continuam os cortes de silêncio e o QA vigente.
2. **Ritmo por beat.** Nem preparo, rótulo, payoff e CTA devem sofrer a mesma
   compressão. Manter ação protegida a 1x quando a velocidade comprometer a
   compreensão. Usar 1–1,25x por take quando indicado; não alegar saber a
   aceleração usada no vídeo original a partir de palavras/s globais.
3. **Legenda acompanha a ideia e o quadro.** Grupos curtos, quebra por frase e
   take, termo principal destacado quando útil, posição definida pelo objeto e
   rosto. Algumas referências mostram 3–6 palavras em até três linhas; isso é
   opção de composição, não obrigação em todas as frases. Catálogo HyperFrames
   continua prioritário. Não imitar sobreposição sobre boca, mãos ou rótulo.
4. **Câmera tem função.** Hook: objeto/ação perto da lente. Demonstração:
   rosto, mãos e produto inteiros. Reveal: enquadramento que mostra uso e
   rótulo, inclusive overhead quando o modelo exigir. CTA: gesto legível,
   contato visual e continuidade do objeto. Definir isso antes no K, sem
   acrescentar descrição longa ao V aposentado.
5. **Produto participa da ação.** Sea Moss: frasco/gummy identificável no
   momento apropriado, com continuidade de embalagem. FitWell: demonstração
   de app/hábito conforme oferta. Não importar a receita, bitters ou promessa
   da referência para o nosso produto.
6. **Música recebe planejamento temporal.** Escolher trecho de entrada da
   biblioteca e curva de volume por beat; deixar a voz compreensível e evitar
   fim abrupto/trilha acabando antes do vídeo. Na faixa pré-normalizada, cama
   base -18 dB vigente; envelope opt-in permite reduções até -30 dB. Esses
   valores são projeto de mix e não relação música/voz medida nas referências.
   Escolha emocional e validação perceptiva permanecem dependentes de escuta.

## Implementado no editor

O comando continua `python3 .claude/skills/edicao/template/editar.py PASTA`.
Modo editorial opcional: `--plano-editorial CAMINHO/plano_editorial.json`.
O operador prepara o plano por produção após inspecionar os takes, sem pedir
ao Luigi configuração técnica. Sem plano, os padrões existentes permanecem.
Arquivo exemplar abaixo é didático, não plano pronto dos próximos vídeos.

- `protected_intervals`: tempo **da fonte do take já conferido**, número na
  ordem final reconhecida pela fala e razão observada. União com as ilhas de
  fala antes de cortar; intervalos fora da duração são recusados. Se limpeza
  de fala aparar esse take, o editor para para recalcular os tempos, evitando
  aplicar marcação antiga à fonte nova. Isso não autoriza falta/troca de palavra.
- `rhythm`: velocidade por take. Proteção sem override fica 1x; override
  explícito vale para o take, inclusive proteção. Rampas mudas 5x preexistentes
  permanecem. Duração e offsets são recalculados; cortes menores que dois
  frames criados pelo plano são recusados.
- `captions`: alvo de palavras por grupo antes da união de páginas curtas, posição normal e posição de
  take-herói no render padrão FitWell/Sea Moss. Não é teto rígido após a união de páginas para leitura; a união não atravessa takes. Defaults 3/880/760, coordenadas
  no quadro 1080×1920. Primeira legenda começa na fala, não no começo de uma
  ação muda preservada. Escolha de fonte/destaque ainda usa o catálogo e o
  acabamento existentes; não foi implementada uma clonagem da fonte original.
  Estilos do catálogo usam o adaptador próprio, não estes anchors do render
  padrão. Para aplicar os anchors, usar `--legenda padrao`.
- `music`: offset na **faixa musical**; pontos de ganho na **saída editada**,
  interpolados em dB, fade-in/fade-out. Fonte curta é repetida até completar
  a duração. Sem bloco `music`, o mixer anterior permanece. Fades omitidos mantêm 0,3/0,8 s; zero explícito os desliga. Offset fora da faixa e curva fora da saída são recusados. O
  envelope manual não detecta BPM nem decide emoção pela energia RMS.
- `plano_editorial_aplicado.json` e relatório registram o plano realmente usado.
  Conferência de silêncio libera só janelas protegidas/rampas inteiras, com
  tolerância de um frame. Legenda/rosto/produto e cortes continuam exigindo QA.
- Auraly: plano de outra oferta é recusado; plano Auraly exige justificativa
  de adaptação. Este bloco de `captions` é recusado na Auraly, que mantém seu
  próprio workflow visual. Nenhum default Auraly foi mudado por este estudo.

```json
{
  "version": 1,
  "offer": "sea_moss",
  "protected_intervals": [
    {"take": 1, "start": 0, "end": 2, "reason": "Exemplo: ação de produto vista nos takes"}
  ],
  "rhythm": [{"take": 1, "speed": 1}],
  "captions": {"max_words": 4, "top": 880, "hero_top": 760},
  "music": {
    "start_seconds": 0,
    "fade_in_seconds": 0.3,
    "fade_out_seconds": 0.8,
    "points": [{"time": 0, "db": -24}, {"time": 3, "db": -18}]
  }
}
```

## Música: limite da análise e próximo controle de qualidade

Não houve ferramenta de escuta perceptiva nesta sessão nem separação confiável
de stems. Medimos áudio misturado, cerca de -14,3 a -15 LUFS, com sinal antes
de certas falas. **Não confirmados**: instrumentos, BPM, emoção, crescendos e
sincronização da música original com os cortes. O ganho isolado da cama não
pode ser deduzido do RMS do arquivo misturado. Nenhuma dessas hipóteses foi
transformada em regra automática.

O aprendizado musical entregue é uma capacidade de implementação testada e um
plano de uso, com a limitação acima registrada. A primeira prática ainda precisa
validar como o mix e o ritmo soam juntos, e conferir as legendas/imagem no render.
Teste de expressão FFmpeg/duração não certifica qualidade emocional.

## Validação e fronteira de conclusão

Testes específicos em `tests/test_plano_editorial.py` e
`tests/test_editar_plano_integracao.py`: schema, herança Auraly, intervalos,
velocidade, janelas de QA, defaults e mix real FFmpeg com faixa curta.
Testes usam áudio sintético para comprovar execução e energia depois do fim
da fonte; não certificam escuta. Não houve edição comercial/render de vídeo
com estes novos parâmetros nesta fase, conforme pedido de aprendizado antes
da prática. Revisão independente e commit registrados ao concluir a fase.

Para refazer medições: rodar `/watch` nos arquivos originais e depois
`scripts/analisar_edicao_referencia.py VIDEO WATCH_DIR --output METRICAS.json`
com `.venv-operacao/bin/python`. Frames são regeneráveis a partir dos hashes e
timestamps, com arquivos originais legíveis. Não procurar títulos/contas na
internet: referências já foram fornecidas diretamente pelo Luigi.
