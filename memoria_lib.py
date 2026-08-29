# -*- coding: utf-8 -*-
"""
memoria_lib.py - Parser compartilhado da memoria viva.

Usado por checar_memoria.py (o lint) e por grafo_memoria.py (as arestas de
wikilink). Existe para os dois lerem a memoria do mesmo jeito, em vez de cada
um inventar o seu parser e discordarem em silencio.

A FONTE DE VERDADE e ~/.claude/projects/<slug>/memory, nunca o espelho
memoria/ do repo. Ver a regra no CLAUDE.md.

Criado em 2026-08-29.
"""
from __future__ import annotations
import io
import os
import re
import glob

ESPELHO = "memoria"
NAO_E_MEMORIA = {"MEMORY.md", "README.md"}


def ler(path):
    return io.open(path, encoding="utf-8").read()


# ------------------------------------------------------------------ localizacao
def localizar_memoria_viva(raiz="."):
    """Descobre ~/.claude/projects/<slug>/memory a partir do diretorio do projeto.

    O slug e o caminho absoluto com todo caractere nao alfanumerico virando '-'.
    A letra do drive pode aparecer em qualquer caixa dependendo de como o
    processo foi iniciado, entao a busca cai para uma varredura sem caixa em vez
    de confiar no primeiro palpite. Um override explicito por MEMORIA_VIVA
    sempre vence.
    """
    env = os.environ.get("MEMORIA_VIVA")
    if env:
        return env if os.path.isdir(env) else None

    base = os.path.join(os.path.expanduser("~"), ".claude", "projects")
    if not os.path.isdir(base):
        return None

    slug = re.sub(r"[^A-Za-z0-9]", "-", os.path.abspath(raiz))
    direto = os.path.join(base, slug, "memory")
    if os.path.isdir(direto):
        return direto

    alvo = slug.lower()
    for d in glob.glob(os.path.join(base, "*")):
        if os.path.basename(d).lower() == alvo:
            cand = os.path.join(d, "memory")
            if os.path.isdir(cand):
                return cand
    return None


# ------------------------------------------------------------------ frontmatter
_FM = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)


def parse_frontmatter(texto):
    """Devolve (campos, corpo). Parser proposital de uma chave por linha.

    A memoria so usa name/description/metadata.type, entao nao vale arrastar um
    parser de YAML completo para dentro de um lint que precisa rodar sempre.
    """
    m = _FM.match(texto)
    if not m:
        return {}, texto
    campos = {}
    for linha in m.group(1).splitlines():
        if not linha.strip() or linha.lstrip().startswith("#"):
            continue
        mk = re.match(r"^(\s*)([A-Za-z_][\w-]*):\s*(.*)$", linha)
        if not mk:
            continue
        indent, chave, valor = mk.group(1), mk.group(2), mk.group(3).strip()
        if indent:                      # aninhado, ex. metadata.type
            chave = "metadata." + chave
        if len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in "\"'":
            valor = valor[1:-1]
        campos[chave] = valor
    return campos, texto[m.end():]


WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")


def ler_memorias(dir_memoria):
    """Le todo .md de memoria da pasta. MEMORY.md e README.md ficam de fora."""
    out = []
    for path in sorted(glob.glob(os.path.join(dir_memoria, "*.md"))):
        arquivo = os.path.basename(path)
        if arquivo in NAO_E_MEMORIA:
            continue
        texto = ler(path)
        campos, corpo = parse_frontmatter(texto)
        out.append({
            "arquivo": arquivo,
            "path": path,
            "name": campos.get("name", ""),
            "description": campos.get("description", ""),
            "type": campos.get("metadata.type", campos.get("type", "")),
            "tem_frontmatter": bool(campos),
            "corpo": corpo,
            "wikilinks": [w.strip() for w in WIKILINK.findall(corpo)],
        })
    return out


def ler_indice(dir_memoria):
    """Devolve {arquivo.md: numero_da_linha} para os links do MEMORY.md."""
    path = os.path.join(dir_memoria, "MEMORY.md")
    if not os.path.exists(path):
        return {}
    alvos = {}
    for n, linha in enumerate(ler(path).splitlines(), 1):
        for alvo in re.findall(r"\]\(([^)]+\.md)\)", linha):
            alvos.setdefault(os.path.basename(alvo), n)
    return alvos


def mapa_name_para_arquivo(memorias):
    """{name do frontmatter: arquivo.md}. Nome repetido vira lista de conflito."""
    mapa, repetidos = {}, {}
    for m in memorias:
        if not m["name"]:
            continue
        if m["name"] in mapa:
            repetidos.setdefault(m["name"], [mapa[m["name"]]]).append(m["arquivo"])
        else:
            mapa[m["name"]] = m["arquivo"]
    return mapa, repetidos
