#!/bin/bash
# Orquestrador único do lote Sea Moss receitas (2026-10-14): fila sequencial, sem interação.
S=/private/tmp/claude-501/-Users-macbookairm2-agente-bala-non-shop-agente-bala-non-shop/769237f4-1ad1-43d3-a650-d5a556746023/scratchpad
R="/Users/macbookairm2/agente bala non-shop/agente-bala-non-shop"
ST="$R/producao/seamoss_receitas_lote_2026_10_13/STATUS_EDICAO.md"
cd "$R"
printf '# Status da edição automática (lote Sea Moss receitas, 2026-10-14)\n\n| Vídeo | Produção | Estado | Arquivo | Conferências com falha | Hora |\n|---|---|---|---|---|---|\n' > "$ST"
roda(){ # pasta producao saida
  echo "=== $(date +%H:%M) INICIO $1"
  .venv-operacao/bin/python $S/auto.py "$1" "$2"; code=$?
  w=$(ls -td /tmp/edicao/"$1"-* 2>/dev/null | head -1); rel="$w/RELATORIO.md"
  mkdir -p "$R/producao/$2/edicao"; cp "$rel" "$w"/cortes.png "$w"/legendas.png "$R/producao/$2/edicao/" 2>/dev/null
  f=$(ls "$w"/*_editado.mp4 2>/dev/null | head -1)
  if [ $code -eq 0 ] && [ -n "$f" ] && grep -q 'Fala dos takes contra o roteiro, palavra por palavra: OK' "$rel"; then
    ffmpeg -v error -y -i "$f" -c:v libx264 -crf 20 -preset medium -c:a aac -b:a 192k -movflags +faststart "$HOME/Desktop/$1/$3_editado.mp4"
    falhas=$(grep -E ': FALHA' "$rel" | sed 's/^- //' | tr '\n' ' ')
    echo "PRONTO $1 -> ~/Desktop/$1/$3_editado.mp4 | $falhas"
    echo "| $1 | $2 | PRONTO | ~/Desktop/$1/$3_editado.mp4 | $falhas | $(date +%H:%M) |" >> "$ST"
    rm -rf "$w"
  elif [ $code -eq 3 ]; then
    echo "SEM SOLUCAO $1: ver reais ($S/reais_$2.txt)"
    echo "| $1 | $2 | SEM SOLUÇÃO AUTOMÁTICA | $(tr '\n' ' ' < $S/reais_$2.txt) | | $(date +%H:%M) |" >> "$ST"
  else
    echo "FALHOU $1 (ver $rel)"
    echo "| $1 | $2 | FALHOU | producao/$2/edicao/RELATORIO.md | | $(date +%H:%M) |" >> "$ST"
  fi
  df -h ~ | tail -1
}
#roda "Meredith - V01" meredith_seamoss_canela_limao v01_canela_meredith
#roda "Marshall - V01" marshall_seamoss_canela_limao v01_canela_marshall
#roda "Cassidy hargroove - V01" cassidy_seamoss_canela_limao v01_canela_cassidy
#roda "Meredith - V02" meredith_seamoss_bolinho_maca v02_bolinho_meredith
#roda "Marshall - V02" marshall_seamoss_bolinho_maca v02_bolinho_marshall
#roda "Cassidy Hargove - V02" cassidy_seamoss_bolinho_maca v02_bolinho_cassidy
#roda "Meredith - V03" meredith_seamoss_wrap_lentilha v03_wrap_meredith
#roda "Marshall - V03" marshall_seamoss_wrap_lentilha v03_wrap_marshall
#roda "Cassidy Hargrove - V03" cassidy_seamoss_wrap_lentilha v03_wrap_cassidy
#roda "Meredith - V04" meredith_seamoss_sorvete_banana v04_sorvete_meredith
#roda "Marshal - V04" marshall_seamoss_sorvete_banana v04_sorvete_marshall
#roda "Cassidy Hargrove - V04" cassidy_seamoss_sorvete_banana v04_sorvete_cassidy
for item in \
 "Meredith - V01|meredith_seamoss_canela_limao|v01_canela_meredith" \
 "Marshall - V01|marshall_seamoss_canela_limao|v01_canela_marshall" \
 "Cassidy hargroove - V01|cassidy_seamoss_canela_limao|v01_canela_cassidy" \
 "Meredith - V02|meredith_seamoss_bolinho_maca|v02_bolinho_meredith" \
 "Marshall - V02|marshall_seamoss_bolinho_maca|v02_bolinho_marshall" \
 "Cassidy Hargove - V02|cassidy_seamoss_bolinho_maca|v02_bolinho_cassidy" \
 "Meredith - V03|meredith_seamoss_wrap_lentilha|v03_wrap_meredith" \
 "Marshall - V03|marshall_seamoss_wrap_lentilha|v03_wrap_marshall" \
 "Cassidy Hargrove - V03|cassidy_seamoss_wrap_lentilha|v03_wrap_cassidy" \
 "Meredith - V04|meredith_seamoss_sorvete_banana|v04_sorvete_meredith" \
 "Marshal - V04|marshall_seamoss_sorvete_banana|v04_sorvete_marshall" \
 "Cassidy Hargrove - V04|cassidy_seamoss_sorvete_banana|v04_sorvete_cassidy"; do
  IFS='|' read -r p pr o <<< "$item"; roda "$p" "$pr" "$o"
done
echo "LOTE COMPLETO $(date +%H:%M)"
