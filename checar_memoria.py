# -*- coding: utf-8 -*-
"""
checar_memoria.py - Gate mecanico da MEMORIA, irmao do checar_entrega.py.

Le a memoria viva DO DISCO e checa o que da para checar por maquina: wikilink
quebrado, memoria fora do indice, linha do indice apontando para arquivo que
nao existe, frontmatter invalido e drift entre a memoria viva e o espelho
memoria/ do repo.

Uso:
    python checar_memoria.py
    python checar_memoria.py --sem-espelho     (pula a checagem de drift)

Existe pelo mesmo motivo do checar_entrega.py: regra lembrada e regra
esquecida. E porque renomear memoria quebra wikilink em silencio, que foi
exatamente o que aconteceu em 2026-08-29.

Criado em 2026-08-29.
"""
from __future__ import annotations
import sys
import os
import glob

import memoria_lib as ML

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FALHAS, AVISOS, OKS = [], [], []
TIPOS_VALIDOS = {"user", "feedback", "project", "reference"}


def falha(check, msg, loc=""):
    FALHAS.append((check, msg, loc))


def aviso(check, msg, loc=""):
    AVISOS.append((check, msg, loc))


def ok(check, msg=""):
    OKS.append((check, msg))


# ------------------------------------------------------------------- checagens
def c_frontmatter(memorias):
    ruins = 0
    for m in memorias:
        if not m["tem_frontmatter"]:
            falha("frontmatter", "%s nao tem frontmatter" % m["arquivo"])
            ruins += 1
            continue
        if not m["name"]:
            falha("frontmatter", "%s nao tem 'name:'" % m["arquivo"])
            ruins += 1
        if not m["description"]:
            falha("frontmatter", "%s nao tem 'description:'" % m["arquivo"])
            ruins += 1
        if m["type"] not in TIPOS_VALIDOS:
            falha("frontmatter",
                  "%s tem type '%s' (validos: %s)"
                  % (m["arquivo"], m["type"] or "vazio", ", ".join(sorted(TIPOS_VALIDOS))))
            ruins += 1
    if not ruins:
        ok("frontmatter", "%d memorias com name, description e type validos" % len(memorias))


def c_nome_unico(memorias):
    _, repetidos = ML.mapa_name_para_arquivo(memorias)
    for nome, arqs in repetidos.items():
        falha("nome-unico", "name '%s' repetido em: %s" % (nome, ", ".join(sorted(arqs))))
    if not repetidos:
        ok("nome-unico", "nenhum 'name:' duplicado")


def c_wikilinks(memorias):
    mapa, _ = ML.mapa_name_para_arquivo(memorias)
    quebrados = 0
    total = 0
    for m in memorias:
        for alvo in m["wikilinks"]:
            total += 1
            if alvo not in mapa:
                falha("wikilink", "[[%s]] nao existe" % alvo,
                      "citado em %s" % m["arquivo"])
                quebrados += 1
    if not quebrados:
        ok("wikilink", "%d wikilinks, todos resolvem" % total)


def c_indice(memorias, dir_memoria):
    indice = ML.ler_indice(dir_memoria)
    arquivos = {m["arquivo"] for m in memorias}

    fora = sorted(arquivos - set(indice))
    for a in fora:
        falha("indice", "%s nao tem linha no MEMORY.md" % a,
              "MEMORY.md e lista de ordens: memoria fora dele nunca e aberta")

    mortos = sorted(set(indice) - arquivos)
    for a in mortos:
        falha("indice", "MEMORY.md aponta para %s, que nao existe" % a,
              "MEMORY.md linha %d" % indice[a])

    if not fora and not mortos:
        ok("indice", "%d memorias, todas indexadas e sem link morto" % len(arquivos))


def c_orfas(memorias):
    """Memoria que ninguem cita nao e falha, mas vale saber: so o indice a alcanca."""
    mapa, _ = ML.mapa_name_para_arquivo(memorias)
    citadas = set()
    for m in memorias:
        citadas.update(a for a in m["wikilinks"] if a in mapa)
    orfas = sorted(m["name"] for m in memorias if m["name"] and m["name"] not in citadas)
    if orfas:
        aviso("orfas", "%d memorias que nenhuma outra cita: %s"
              % (len(orfas), ", ".join(orfas)),
              "so o MEMORY.md leva ate elas. Linkar de quem for relacionado")
    else:
        ok("orfas", "toda memoria e citada por pelo menos outra")


def c_espelho(memorias, dir_memoria):
    """O espelho memoria/ e backup versionado. Drift silencioso e pior que nada."""
    if not os.path.isdir(ML.ESPELHO):
        aviso("espelho", "pasta %s/ nao existe neste diretorio" % ML.ESPELHO)
        return
    vivos = {m["arquivo"] for m in memorias} | {"MEMORY.md"}
    espelhados = {os.path.basename(p) for p in glob.glob(os.path.join(ML.ESPELHO, "*.md"))}
    espelhados -= {"README.md"}

    faltando = sorted(vivos - espelhados)
    sobrando = sorted(espelhados - vivos)
    difs = []
    for a in sorted(vivos & espelhados):
        try:
            if ML.ler(os.path.join(dir_memoria, a)) != ML.ler(os.path.join(ML.ESPELHO, a)):
                difs.append(a)
        except OSError:
            difs.append(a)

    for a in faltando:
        falha("espelho", "%s existe na memoria viva e nao no espelho" % a,
              "rodar: powershell -ExecutionPolicy Bypass -File sync_memoria.ps1")
    for a in sobrando:
        falha("espelho", "%s existe no espelho e nao na memoria viva" % a,
              "sobra de memoria apagada; rodar o sync")
    for a in difs:
        falha("espelho", "%s difere entre memoria viva e espelho" % a,
              "rodar o sync antes de commitar")
    if not faltando and not sobrando and not difs:
        ok("espelho", "%d arquivos identicos entre memoria viva e %s/"
           % (len(vivos), ML.ESPELHO))


# ------------------------------------------------------------------------ main
def main():
    checar_espelho = "--sem-espelho" not in sys.argv[1:]

    dir_memoria = ML.localizar_memoria_viva(".")
    if not dir_memoria:
        print("ERRO: nao achei a memoria viva.")
        print("Definir MEMORIA_VIVA com o caminho de ~/.claude/projects/<slug>/memory")
        return 2

    memorias = ML.ler_memorias(dir_memoria)
    if not memorias:
        print("ERRO: nenhuma memoria encontrada em %s" % dir_memoria)
        return 2

    c_frontmatter(memorias)
    c_nome_unico(memorias)
    c_wikilinks(memorias)
    c_indice(memorias, dir_memoria)
    c_orfas(memorias)
    if checar_espelho:
        c_espelho(memorias, dir_memoria)

    print("=" * 82)
    print("  memoria viva: %s   (%d memorias)" % (dir_memoria, len(memorias)))
    print("=" * 82)
    for c, m in OKS:
        print("  [OK]     %-14s %s" % (c, m))
    for c, m, loc in AVISOS:
        print("  [AVISO]  %-14s %s%s" % (c, m, ("\n           -> %s" % loc) if loc else ""))
    for c, m, loc in FALHAS:
        print("  [FALHA]  %-14s %s%s" % (c, m, ("\n           -> %s" % loc) if loc else ""))
    print("-" * 82)
    print("  %d ok, %d avisos, %d FALHAS" % (len(OKS), len(AVISOS), len(FALHAS)))
    print()
    return 1 if FALHAS else 0


if __name__ == "__main__":
    sys.exit(main())
