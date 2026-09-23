# -*- coding: utf-8 -*-
"""
checar_frases.py - Detector de frase queimada na mesma conta.

A regra do fechamento manda nao repetir as frases do video anterior, e hoje
isso vive so na memoria, em listas escritas a mao ("frases queimadas na conta
do Melody"). Este script compara as falas de um roteiro contra todos os
roteiros ANTERIORES DA MESMA CONTA e aponta as sequencias repetidas.

Duas coisas que ele NAO trata como defeito, e por que:

  1. Clone entre avatares. O CLAUDE.md autoriza rodar o mesmo roteiro em outro
     avatar, entao dois pacotes do mesmo roteiro em contas diferentes compartilharem trechos e o esperado.
     Contas diferentes nunca sao comparadas.
  2. Boilerplate de CTA. "comment yes and i will send you the link" repete de
     proposito. O script descobre isso sozinho: sequencia que aparece em 3 ou
     mais CONTAS distintas e template da operacao, nao frase queimada.

Uso:
    python checar_frases.py                     varre tudo, conta por conta
    python checar_frases.py producao/melody_sal roteiro novo contra os antigos
    python checar_frases.py --n 5               sequencia minima (padrao 6)

Entra no PORTAO P2, antes de tocar na copy. Criado em 2026-08-29.
"""
from __future__ import annotations
import sys
import os
import io
import re
import glob
import itertools
from collections import defaultdict

import checar_entrega as CE

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

N_PADRAO = 6
MIN_CONTAS_BOILERPLATE = 3

# O beat de CTA repete de proposito: a mesma ordem ("comment yes", "222"), o
# mesmo follow gate, a mesma promessa de DM. Filtrar por BEAT e preciso;
# filtrar so por frequencia nao funciona, porque a ordem muda com o angulo
# (yes nos 1, 2 e 4; 222 no 3) e nunca alcanca contas suficientes.
RE_BEAT_CTA = re.compile(r"^\s*CTA\b|FOLLOW\s*GATE", re.I)


def conta_de(pasta):
    """A conta e o prefixo antes do primeiro _ (melody, brandon, dana, walt...)."""
    return os.path.basename(pasta).split("_")[0]


def falas_do_pacote(pasta):
    p = os.path.join(pasta, "ROTEIRO.md")
    if not os.path.exists(p):
        return []
    texto = io.open(p, encoding="utf-8").read()
    return [(t["id"], t["head"], CE.norm_fala(t["fala"]))
            for t in CE.parse_takes(texto)
            if t.get("fala") and not RE_BEAT_CTA.search(t["head"] or "")]


def ngrams(frase, n):
    w = re.findall(r"[a-z']+", frase.lower())
    return [" ".join(w[i:i + n]) for i in range(len(w) - n + 1)]


def carregar(n):
    """{pacote: {ngram: (take_id, head, fala)}} para todo pacote com roteiro."""
    dados = {}
    for d in sorted(glob.glob("producao/*")):
        if not os.path.isdir(d):
            continue
        falas = falas_do_pacote(d)
        if not falas:
            continue
        idx = {}
        for tid, head, fala in falas:
            for g in ngrams(fala, n):
                idx.setdefault(g, (tid, head, fala))
        dados[os.path.basename(d)] = idx
    return dados


def boilerplate(dados):
    """Sequencia presente em 3+ CONTAS distintas e template, nao frase queimada."""
    contas_por_gram = defaultdict(set)
    for pacote, idx in dados.items():
        c = conta_de(pacote)
        for g in idx:
            contas_por_gram[g].add(c)
    return {g for g, cs in contas_por_gram.items() if len(cs) >= MIN_CONTAS_BOILERPLATE}


def comparar(a, b, dados, tmpl):
    """Trechos que a e b compartilham, ja sem o boilerplate da operacao."""
    return sorted((set(dados[a]) & set(dados[b])) - tmpl)


def main():
    args = [x for x in sys.argv[1:]]
    n = N_PADRAO
    if "--n" in args:
        i = args.index("--n")
        n = int(args[i + 1])
        del args[i:i + 2]
    alvo = args[0].rstrip("/\\") if args else None

    dados = carregar(n)
    if not dados:
        print("Nenhum ROTEIRO.md com falas encontrado em producao/.")
        return 2
    tmpl = boilerplate(dados)

    print("=" * 82)
    print("  frases queimadas | %d pacotes, sequencia minima de %d palavras" % (len(dados), n))
    print("  %d sequencias tratadas como boilerplate (aparecem em %d+ contas)"
          % (len(tmpl), MIN_CONTAS_BOILERPLATE))
    print("=" * 82)

    if alvo:
        nome = os.path.basename(alvo)
        if nome not in dados:
            print("ERRO: %s nao tem ROTEIRO.md com falas." % alvo)
            return 2
        conta = conta_de(nome)
        irmaos = [p for p in dados if conta_de(p) == conta and p != nome]
        if not irmaos:
            print("  [OK] %s e o primeiro roteiro da conta '%s'." % (nome, conta))
            return 0
        achou = 0
        for outro in sorted(irmaos):
            comuns = comparar(nome, outro, dados, tmpl)
            if not comuns:
                continue
            achou += len(comuns)
            print("\n  [FALHA] %s repete %d trecho(s) de %s" % (nome, len(comuns), outro))
            for g in comuns[:6]:
                tid, head, _ = dados[nome][g]
                print('      %-5s "%s"' % (tid, g))
                print('            beat: %s' % head)
            if len(comuns) > 6:
                print("      ... e mais %d" % (len(comuns) - 6))
        if not achou:
            print("  [OK] %s nao repete nada dos %d roteiros anteriores da conta '%s'."
                  % (nome, len(irmaos), conta))
        print()
        return 1 if achou else 0

    # varredura geral, conta por conta
    total = 0
    for conta in sorted({conta_de(p) for p in dados}):
        pacotes = sorted(p for p in dados if conta_de(p) == conta)
        if len(pacotes) < 2:
            continue
        pares = []
        for a, b in itertools.combinations(pacotes, 2):
            comuns = comparar(a, b, dados, tmpl)
            if comuns:
                pares.append((len(comuns), a, b, comuns))
        pares.sort(reverse=True)
        print("\n  conta '%s' (%d pacotes)" % (conta, len(pacotes)))
        if not pares:
            print("      [OK] nenhuma frase repetida entre eles")
            continue
        for qtd, a, b, comuns in pares:
            total += qtd
            print("      [AVISO] %-20s x %-20s  %d trecho(s)" % (a, b, qtd))
            for g in comuns[:3]:
                print('               "%s"' % g)
    print("\n" + "-" * 82)
    print("  %d repeticoes intra-conta fora do boilerplate" % total)
    print("  Clone entre avatares nao e comparado, e autorizado pelo CLAUDE.md.")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
