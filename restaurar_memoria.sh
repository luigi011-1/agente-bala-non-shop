#!/usr/bin/env bash
# restaurar_memoria.sh
#
# Equivalente em bash do restaurar_memoria.ps1, para macOS e Linux (2026-09-24).
# O clone traz o ESPELHO memoria/, mas a memoria VIVA mora fora do repo, em
# ~/.claude/projects/<slug>/memory/. Sem restaurar, o agente nasce com o processo
# inteiro e zero copy. Este script copia o espelho para a memoria viva.
#
# Mesma semantica do .ps1: arquivo novo e copiado; arquivo igual fica; arquivo
# DIVERGENTE nao e tocado, a nao ser com --force. README.md e so do repo.
#
# Uso:  bash restaurar_memoria.sh           (seguro, nao sobrescreve divergentes)
#       bash restaurar_memoria.sh --force   (o espelho vence)
#
# Compativel com o bash 3.2 do macOS (sem mapfile, sem arrays associativos).

set -euo pipefail

force=0
[ "${1:-}" = "--force" ] && force=1

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
origem="$repo_root/memoria"

# Numa worktree (.claude/worktrees/<nome>) a memoria pertence ao checkout PRINCIPAL.
raiz_principal="$repo_root"
if comum="$(git -C "$repo_root" rev-parse --path-format=absolute --git-common-dir 2>/dev/null)"; then
    raiz_principal="$(dirname "$comum")"
fi

# Mesmo slug do memoria_lib.py: todo caractere nao alfanumerico vira '-'.
slug="$(printf '%s' "$raiz_principal" | sed 's/[^A-Za-z0-9]/-/g')"
destino="${MEMORIA_VIVA:-$HOME/.claude/projects/$slug/memory}"

if [ ! -d "$origem" ]; then
    echo "ERRO: nao achei o espelho em $origem" >&2
    echo "      Rodar este script de dentro do clone do repositorio." >&2
    exit 1
fi

if [ ! -d "$destino" ]; then
    mkdir -p "$destino"
    echo "Criei a pasta de memoria viva: $destino"
fi

novos=(); mudados=(); iguais=(); conflitos=()
total=0

for f in "$origem"/*.md; do
    [ -e "$f" ] || continue
    nome="$(basename "$f")"
    [ "$nome" = "README.md" ] && continue
    total=$((total + 1))
    alvo="$destino/$nome"
    if [ ! -f "$alvo" ]; then
        cp "$f" "$alvo"; novos+=("$nome")
    elif cmp -s "$f" "$alvo"; then
        iguais+=("$nome")
    elif [ "$force" -eq 1 ]; then
        cp "$f" "$alvo"; mudados+=("$nome")
    else
        conflitos+=("$nome")
    fi
done

echo
echo "Origem (espelho do repo): $origem"
echo "Destino (memoria viva)  : $destino"
echo "Total no espelho        : $total arquivos de memoria"
echo

if [ "${#novos[@]}" -gt 0 ]; then echo "RESTAURADOS (${#novos[@]}):"; printf '  + %s\n' "${novos[@]}"; fi
if [ "${#mudados[@]}" -gt 0 ]; then echo "SOBRESCRITOS (${#mudados[@]}):"; printf '  ~ %s\n' "${mudados[@]}"; fi
if [ "${#iguais[@]}" -gt 0 ]; then echo "JA IGUAIS (${#iguais[@]})"; fi
if [ "${#conflitos[@]}" -gt 0 ]; then
    echo
    echo "DIVERGENTES (${#conflitos[@]}), nao toquei:"
    printf '  ! %s\n' "${conflitos[@]}"
    echo
    echo "A memoria viva deste computador tem versao diferente do espelho."
    echo "Se o espelho e que esta certo, rodar de novo com --force."
    echo "Se a memoria viva e que esta certa, rodar sync_memoria.sh e commitar."
fi

if [ ! -f "$destino/MEMORY.md" ]; then
    echo
    echo "AVISO: $destino/MEMORY.md nao existe. Sem o indice a memoria nao carrega."
    exit 1
fi
echo
echo "Pronto. Conferir com: python3 checar_memoria.py"
