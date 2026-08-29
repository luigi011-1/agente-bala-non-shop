# -*- coding: utf-8 -*-
"""
grafo_memoria.py - Poe os wikilinks da memoria dentro do grafo do graphify.

Os arquivos de memoria se citam com [[nome]]. Sao 269 referencias escritas a
mao, explicitas, e a extracao por LLM nao as capturou: os subagentes trabalham
por chunk e evitam criar no para alvo que nao esta no chunk deles. Resultado:
o grafo tinha 124 nos de arquivo e ZERO aresta arquivo-para-arquivo.

Este script emite essas arestas de forma determinista. Sem LLM, sem subagente,
roda em milissegundos. E o antidoto para o pior defeito do grafo, que e
envelhecer e custar da ordem de 1M de tokens para atualizar: a camada de
doutrina passa a poder ser refeita a qualquer momento, de graca.

Uso:
    python grafo_memoria.py            aplica em graphify-out/graph.json
    python grafo_memoria.py --dry-run  so mostra o que faria

LIMITE CONHECIDO: nao regenera o GRAPH_REPORT.md. Depois de rodar, o relatorio
fica atras do grafo na contagem de arestas. Regenerar com o pipeline do
graphify quando isso importar.

Criado em 2026-08-29.
"""
from __future__ import annotations
import sys
import os
import re
import json
import io

import memoria_lib as ML

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

GRAFO = os.path.join("graphify-out", "graph.json")
ORIGEM = "wikilink"          # etiqueta que torna o script idempotente


def slug(s):
    """Mesma normalizacao usada para criar os nos de arquivo do esqueleto."""
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def id_do_arquivo(arquivo):
    return "arquivo_" + slug("%s/%s" % (ML.ESPELHO, arquivo))


def main():
    dry = "--dry-run" in sys.argv[1:]

    dir_memoria = ML.localizar_memoria_viva(".")
    if not dir_memoria:
        print("ERRO: nao achei a memoria viva. Definir MEMORIA_VIVA.")
        return 2
    if not os.path.exists(GRAFO):
        print("ERRO: %s nao existe. Rodar /graphify antes." % GRAFO)
        return 2

    memorias = ML.ler_memorias(dir_memoria)
    mapa, _ = ML.mapa_name_para_arquivo(memorias)

    g = json.loads(io.open(GRAFO, encoding="utf-8").read())
    ids = {n["id"] for n in g["nodes"]}

    # tira as arestas da rodada anterior para nao acumular duplicata
    antes = len(g["links"])
    g["links"] = [e for e in g["links"] if e.get("origem") != ORIGEM]
    removidas = antes - len(g["links"])

    novos_nos, arestas, sem_no, quebrados = [], [], set(), []
    vistos = set()

    for m in memorias:
        origem_id = id_do_arquivo(m["arquivo"])
        if origem_id not in ids and origem_id not in vistos:
            novos_nos.append((origem_id, m["arquivo"]))
            vistos.add(origem_id)
        for alvo_nome in m["wikilinks"]:
            alvo_arq = mapa.get(alvo_nome)
            if not alvo_arq:
                quebrados.append((m["arquivo"], alvo_nome))
                continue
            alvo_id = id_do_arquivo(alvo_arq)
            if alvo_id not in ids and alvo_id not in vistos:
                novos_nos.append((alvo_id, alvo_arq))
                vistos.add(alvo_id)
            par = (origem_id, alvo_id)
            if origem_id == alvo_id or par in sem_no:
                continue
            sem_no.add(par)
            arestas.append({
                "source": origem_id,
                "target": alvo_id,
                "relation": "references",
                "confidence": "EXTRACTED",
                "confidence_score": 1.0,
                "source_file": "%s/%s" % (ML.ESPELHO, m["arquivo"]),
                "source_location": None,
                "weight": 1.0,
                "origem": ORIGEM,
            })

    for nid, arquivo in novos_nos:
        g["nodes"].append({
            "id": nid,
            "label": "%s/%s" % (ML.ESPELHO, arquivo),
            "file_type": "document",
            "source_file": "%s/%s" % (ML.ESPELHO, arquivo),
            "source_location": None, "source_url": None, "captured_at": None,
            "author": None, "contributor": None,
            "community": None, "community_name": None,
        })

    g["links"].extend(arestas)

    print("memoria viva : %s" % dir_memoria)
    print("memorias     : %d" % len(memorias))
    print("wikilinks    : %d resolvidos em %d arestas unicas"
          % (sum(len(m["wikilinks"]) for m in memorias), len(arestas)))
    if removidas:
        print("substituidas : %d arestas da rodada anterior" % removidas)
    if novos_nos:
        print("nos criados  : %d (memoria nova, ainda sem no no grafo)" % len(novos_nos))
        for _, a in novos_nos:
            print("               + %s" % a)
    if quebrados:
        print("QUEBRADOS    : %d wikilinks sem alvo (rodar checar_memoria.py)" % len(quebrados))
        for src, alvo in quebrados:
            print("               ! [[%s]] em %s" % (alvo, src))

    if dry:
        print("\n--dry-run: nada foi escrito.")
        return 0

    io.open(GRAFO, "w", encoding="utf-8").write(json.dumps(g, ensure_ascii=False))
    print("\n%s: %d nos, %d arestas" % (GRAFO, len(g["nodes"]), len(g["links"])))
    print("GRAPH_REPORT.md NAO foi regenerado e agora esta atras na contagem.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
