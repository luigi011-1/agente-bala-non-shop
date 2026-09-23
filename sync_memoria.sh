#!/usr/bin/env bash
# sync_memoria.sh
#
# Equivalente em bash do sync_memoria.ps1, para macOS e Linux.
# Criado em 2026-09-20: o .ps1 e Windows-only ($env:USERPROFILE, paths com '\') e
# nao roda no Mac, entao o espelho ficou 14 arquivos atras da memoria viva sem
# ninguem perceber. Mesma semantica do .ps1, inclusive a lista de preservados.
#
# POR QUE ISTO EXISTE
# A memoria de verdade vive em ~/.claude/projects/<projeto>/memory/ e e la que o
# agente escreve. A pasta memoria/ do repo e SO UM ESPELHO, para backup e historico.
# Sem sync viram duas fontes de verdade e o espelho apodrece, que e o problema que
# fez o PORTAO P10 existir.
#
# REGRA: rodar ANTES de todo commit que envolva memoria. Nunca editar memoria/ na mao.
#
# Uso:  bash sync_memoria.sh

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
destino="$repo_root/memoria"

# O Claude Code deriva o nome da pasta do projeto do caminho: '/' e ' ' viram '-'
slug="$(echo "$repo_root" | sed 's/[\/ ]/-/g')"
origem="$HOME/.claude/projects/$slug/memory"

if [ ! -d "$origem" ]; then
    # fallback: procura qualquer pasta de projeto que contenha um MEMORY.md
    mapfile -t candidatos < <(find "$HOME/.claude/projects" -maxdepth 2 -name MEMORY.md -path '*/memory/*' 2>/dev/null)
    if [ "${#candidatos[@]}" -eq 1 ]; then
        origem="$(dirname "${candidatos[0]}")"
        echo "Aviso: caminho derivado nao existia, usando $origem"
    else
        echo "ERRO: nao achei a pasta de memoria." >&2
        echo "Esperava: $origem" >&2
        exit 1
    fi
fi

mkdir -p "$destino"

# Arquivos que sao SO DO REPO e nunca existiram na memoria viva. Sem esta lista o
# laco de remocao os apaga em todo sync. Era o caso do README.md.
preservados=("README.md")

novos=(); mudados=(); removidos=(); mantidos=()

for f in "$origem"/*.md; do
    [ -e "$f" ] || continue
    nome="$(basename "$f")"
    alvo="$destino/$nome"
    if [ ! -f "$alvo" ]; then
        cp "$f" "$alvo"; novos+=("$nome")
    elif ! cmp -s "$f" "$alvo"; then
        cp "$f" "$alvo"; mudados+=("$nome")
    fi
done

for e in "$destino"/*.md; do
    [ -e "$e" ] || continue
    nome="$(basename "$e")"
    if printf '%s\n' "${preservados[@]}" | grep -qx "$nome"; then
        mantidos+=("$nome"); continue
    fi
    if [ ! -f "$origem/$nome" ]; then
        rm -f "$e"; removidos+=("$nome")
    fi
done

total="$(ls -1 "$origem"/*.md 2>/dev/null | wc -l | tr -d ' ')"
echo
echo "Origem : $origem"
echo "Destino: $destino"
echo "Total  : $total arquivos de memoria"
echo

[ "${#novos[@]}"     -gt 0 ] && { echo "NOVOS (${#novos[@]}):";         printf '  + %s\n' "${novos[@]}"; }
[ "${#mudados[@]}"   -gt 0 ] && { echo "MUDADOS (${#mudados[@]}):";     printf '  ~ %s\n' "${mudados[@]}"; }
[ "${#removidos[@]}" -gt 0 ] && { echo "REMOVIDOS (${#removidos[@]}):"; printf '  - %s\n' "${removidos[@]}"; }
[ "${#mantidos[@]}"  -gt 0 ] && { echo "PRESERVADOS (${#mantidos[@]}):"; printf '  = %s (arquivo do repo, nao da memoria)\n' "${mantidos[@]}"; }

if [ "${#novos[@]}" -eq 0 ] && [ "${#mudados[@]}" -eq 0 ] && [ "${#removidos[@]}" -eq 0 ]; then
    echo "Espelho ja estava em dia. Nada a fazer."
else
    echo
    echo "Pronto. Agora: git add memoria/ && git commit"
fi
echo
