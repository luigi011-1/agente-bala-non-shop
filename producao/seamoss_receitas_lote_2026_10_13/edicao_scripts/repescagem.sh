#!/bin/bash
# Repescagem: espera a fila principal e reedita os vídeos listados em repescagem.txt (um "pasta|produção|saída" por linha).
S=/private/tmp/claude-501/-Users-macbookairm2-agente-bala-non-shop-agente-bala-non-shop/769237f4-1ad1-43d3-a650-d5a556746023/scratchpad
while pgrep -f 'orq2.sh' >/dev/null; do sleep 20; done
R="/Users/macbookairm2/agente bala non-shop/agente-bala-non-shop"
ST="$R/producao/seamoss_receitas_lote_2026_10_13/STATUS_EDICAO.md"
cd "$R"
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
feitos=""
while true; do
  item=$(grep -v -F -x -f <(printf '%s\n' $feitos | sed 's/§/ /g' | grep . || echo "@@nada@@") "$S/repescagem.txt" | head -1)
  [ -z "$item" ] && break
  feitos="$feitos $(echo "$item" | sed 's/ /§/g')"
  IFS='|' read -r p pr o <<< "$item"; echo "=== REPESCAGEM"; roda "$p" "$pr" "$o"
done
echo "LOTE COMPLETO (repescagem) $(date +%H:%M)"
