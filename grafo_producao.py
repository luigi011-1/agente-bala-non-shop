# -*- coding: utf-8 -*-
"""
grafo_producao.py - Poe os takes de producao/ dentro do grafo, sem LLM.

Irmao do grafo_memoria.py. Junto com ele, fecha o ciclo: as duas metades do
grafo passam a ser reconstruiveis de forma determinista, e a passada semantica
por subagente vira enriquecimento opcional em vez de requisito.

Reaproveita os parsers do checar_entrega.py, entao le exatamente o que o linter
le. Se o formato do ROTEIRO.md mudar, os dois quebram juntos, que e melhor do
que um mentir em silencio.

O QUE ENTRA E POR QUE:
  Por padrao, so os TAKES. Eles carregam a fala e o nome do beat, que e o que
  responde pergunta de copy ("que videos tiveram beat de AUTODIAGNOSTICO?").
  Keyframes e clipes sao encanamento de producao, ja coberto pelo
  checar_entrega.py, e entrariam so inflando o grafo. Ficam atras de --completo.

Uso:
    python grafo_producao.py              so os takes
    python grafo_producao.py --completo   takes + keyframes + clipes
    python grafo_producao.py --dry-run    mostra sem escrever

LIMITE CONHECIDO: nao regenera o GRAPH_REPORT.md, igual ao grafo_memoria.py.

Criado em 2026-08-29.
"""
from __future__ import annotations
import sys
import os
import io
import re
import json
import glob

import checar_entrega as CE

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

GRAFO = os.path.join("graphify-out", "graph.json")
ORIGEM = "producao"


def slug(s):
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def id_arquivo(pkg, arquivo):
    """Os nos de arquivo do lado producao foram criados com raiz em producao/."""
    return "arquivo_" + slug("%s/%s" % (pkg, arquivo))


def beat_de(head):
    """'AUTODIAGNOSTICO . TALKING . Setup G' -> 'AUTODIAGNOSTICO'."""
    return re.split(r"[·|]", head or "", 1)[0].strip() or "?"


def main():
    args = sys.argv[1:]
    dry = "--dry-run" in args
    completo = "--completo" in args

    if not os.path.exists(GRAFO):
        print("ERRO: %s nao existe. Rodar /graphify antes." % GRAFO)
        return 2

    g = json.loads(io.open(GRAFO, encoding="utf-8").read())
    ids = {n["id"] for n in g["nodes"]}

    antes = len(g["links"])
    g["links"] = [e for e in g["links"] if e.get("origem") != ORIGEM]
    g["nodes"] = [n for n in g["nodes"] if n.get("origem") != ORIGEM]
    removidas = antes - len(g["links"])
    ids = {n["id"] for n in g["nodes"]}

    novos, arestas = [], []
    stats = {"pacotes": 0, "takes": 0, "kfs": 0, "clipes": 0, "arquivos_criados": 0}

    def no(nid, label, tipo, source_file):
        novos.append({
            "id": nid, "label": label, "file_type": tipo,
            "source_file": source_file, "source_location": None, "source_url": None,
            "captured_at": None, "author": None, "contributor": None,
            "community": None, "community_name": None, "origem": ORIGEM,
        })

    def aresta(src, tgt, rel, sf):
        arestas.append({
            "source": src, "target": tgt, "relation": rel,
            "confidence": "EXTRACTED", "confidence_score": 1.0,
            "source_file": sf, "source_location": None, "weight": 1.0,
            "origem": ORIGEM,
        })

    def garantir_arquivo(pkg, arquivo):
        nid = id_arquivo(pkg, arquivo)
        if nid not in ids and not any(n["id"] == nid for n in novos):
            no(nid, "%s/%s" % (pkg, arquivo), "document", "%s/%s" % (pkg, arquivo))
            stats["arquivos_criados"] += 1
        return nid

    for d in sorted(glob.glob("producao/*")):
        pkg = os.path.basename(d)
        if not os.path.isdir(d) or pkg.startswith("_"):
            continue
        roteiro = CE.ler(os.path.join(d, "ROTEIRO.md"))
        if not roteiro:
            continue
        stats["pacotes"] += 1
        no_roteiro = garantir_arquivo(pkg, "ROTEIRO.md")

        for t in CE.parse_takes(roteiro):
            tid = "take_%s_%s" % (slug(pkg), slug(t["id"]))
            beat = beat_de(t["head"])
            rot = "%s/ROTEIRO.md" % pkg
            no(tid, "%s %s: %s" % (pkg, t["id"], beat), "document", rot)
            aresta(no_roteiro, tid, "references", rot)
            stats["takes"] += 1

        if not completo:
            continue

        prompts = CE.ler(os.path.join(d, "PROMPTS_PRODUCAO.md"))
        if not prompts:
            continue
        no_prompts = garantir_arquivo(pkg, "PROMPTS_PRODUCAO.md")
        pr = "%s/PROMPTS_PRODUCAO.md" % pkg

        for k in CE.parse_keyframes(prompts):
            kid = "keyframe_%s_%s" % (slug(pkg), slug(k["id"]))
            no(kid, "%s %s" % (pkg, k["id"]), "image", pr)
            aresta(no_prompts, kid, "references", pr)
            stats["kfs"] += 1

        for v in CE.parse_videos(prompts):
            vid = "clipe_%s_%s" % (slug(pkg), slug(v["id"]))
            no(vid, "%s %s" % (pkg, v["id"]), "document", pr)
            aresta(no_prompts, vid, "references", pr)
            aresta(vid, "take_%s_%s" % (slug(pkg), slug(v["take"])), "implements", pr)
            aresta(vid, "keyframe_%s_%s" % (slug(pkg), slug(v["usa"])), "references", pr)
            stats["clipes"] += 1

    conhecidos = ids | {n["id"] for n in novos}
    arestas = [e for e in arestas
               if e["source"] in conhecidos and e["target"] in conhecidos]

    g["nodes"].extend(novos)
    g["links"].extend(arestas)

    print("pacotes      : %d" % stats["pacotes"])
    print("takes        : %d" % stats["takes"])
    if completo:
        print("keyframes    : %d" % stats["kfs"])
        print("clipes       : %d" % stats["clipes"])
    if stats["arquivos_criados"]:
        print("nos arquivo  : %d criados (pacote ainda sem no no grafo)"
              % stats["arquivos_criados"])
    if removidas:
        print("substituidas : %d arestas da rodada anterior" % removidas)
    print("novos nos    : %d | novas arestas: %d" % (len(novos), len(arestas)))

    if dry:
        print("\n--dry-run: nada foi escrito.")
        return 0

    io.open(GRAFO, "w", encoding="utf-8").write(json.dumps(g, ensure_ascii=False))
    print("\n%s: %d nos, %d arestas" % (GRAFO, len(g["nodes"]), len(g["links"])))
    print("GRAPH_REPORT.md NAO foi regenerado e agora esta atras na contagem.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
