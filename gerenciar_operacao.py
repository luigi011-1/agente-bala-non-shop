#!/usr/bin/env python3
"""Indice e medicao documental; nao inicia nem altera etapas de producao."""
import argparse
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import re
from urllib.parse import quote
from auraly_validacao import campo, normalizar, sincronizar_fila
from checar_entrega import parse_takes

ROOT = Path(__file__).resolve().parent
CONTROLE = ROOT / 'controle'
OFERTAS = {1: 'Natural Rems Sea Moss', 2: 'FitWell', 3: 'Auraly', 4: 'Body Hacks'}
CONTAGENS = ('impressoes', 'visualizacoes', 'reproducoes_3s', 'conclusoes', 'curtidas', 'comentarios', 'salvamentos', 'compartilhamentos', 'seguidores', 'cliques', 'visitas_destino', 'compras')
VALORES = ('receita', 'custo', 'minutos_trabalho')


def ler_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def gravar_json(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def linha_campo(texto, nome):
    for linha in texto.splitlines():
        simples = linha.replace('**', '').strip().lstrip('- ').strip()
        if simples.startswith('|'):
            cols = [c.strip() for c in simples.strip('|').split('|')]
            if len(cols) >= 2 and normalizar(cols[0].rstrip(':')) == normalizar(nome):
                return cols[1]
        if normalizar(simples).startswith(normalizar(nome) + ':'):
            return simples.split(':', 1)[1].strip()
    return None


def biblioteca():
    registros = []
    for p in sorted((ROOT / 'producao').glob('*/ROTEIRO.md')):
        txt = p.read_text(encoding='utf-8')
        header = re.split(r'^##\s', txt, maxsplit=1, flags=re.M)[0]
        angulo = re.search(r'(?:angulo|angle)\s*([1-4])', normalizar(header))
        numero = int(angulo[1]) if angulo else None
        if numero is None and (re.search(r'pipeline:\s*auraly|^# .*Auraly', header, re.M | re.I) or re.search(r'^- \*\*Travas Auraly:', txt, re.M)):
            numero = 3
        cp = p.with_name('CHECKPOINT.md')
        checkpoint = cp.read_text(encoding='utf-8') if cp.exists() else ''
        funil = linha_campo(header, 'Funil')
        declarado = campo(checkpoint, 'Objective').upper()
        objetivo = declarado if declarado in ('SALE', 'GROWTH') else ('GROWTH' if funil and 'crescimento' in normalizar(funil) else None)
        takes = parse_takes(txt)
        registros.append({
            'producao_id': p.parent.name, 'angulo': numero,
            'oferta': ('Historico: Korella Saffron' if numero == 1 and not re.search(r'natural rems|sea moss', txt, re.I)
                       else OFERTAS.get(numero, 'Nao identificado')),
            'objetivo_declarado': objetivo, 'funil_documentado': funil,
            'referencia': linha_campo(header, 'Vídeo modelo'),
            'avatares_documentados': linha_campo(header, 'Avatares') or linha_campo(header, 'Avatar'),
            'variavel_e_ponte_documentadas': linha_campo(header, 'Variável trocada') or linha_campo(header, 'Ponte pro rosto'),
            'entrada_narrativa_documentada': linha_campo(header, 'Ângulo de entrada'),
            'formato_documentado': linha_campo(header, 'Formato'),
            'enquadramento_documentado': linha_campo(header, 'Enquadramento') or linha_campo(header, 'Enquadramento do avatar'),
            'abertura_documentada': takes[0] if takes else None,
            'takes_reconhecidos': len(takes),
            'estado_checkpoint': campo(checkpoint, 'Current stage') or None,
            'fonte': str(p.relative_to(ROOT)),
            'evidencia': 'Documento de producao; desempenho nao comprovado por este registro.'
        })
    return registros


def validar_resultados(doc, ids):
    if not isinstance(doc, dict) or set(doc) != {'versao', 'publicacoes'} or doc['versao'] != 1 or not isinstance(doc['publicacoes'], list):
        raise ValueError('Esperado objeto versao: 1 e publicacoes: lista.')
    vistos = set()
    campos = {'id', 'producao_id', 'avatar_id', 'hook_id', 'objetivo', 'canal', 'url', 'publicado_em', 'coletado_em', 'moeda', 'observacoes', 'origem', *CONTAGENS, *VALORES}
    for r in doc['publicacoes']:
        if not isinstance(r, dict) or set(r) - campos:
            raise ValueError('Publicacao invalida ou campo desconhecido.')
        for nome in ('id', 'producao_id', 'avatar_id', 'hook_id', 'objetivo', 'canal', 'publicado_em', 'coletado_em'):
            if not isinstance(r.get(nome), str) or not r[nome].strip():
                raise ValueError('Campo obrigatorio: ' + nome)
        if r['id'] in vistos:
            raise ValueError('ID duplicado: ' + r['id'])
        vistos.add(r['id'])
        if r['producao_id'] not in ids or r['objetivo'] not in ('SALE', 'GROWTH'):
            raise ValueError('Producao desconhecida ou objetivo invalido: ' + r['id'])
        if ids[r['producao_id']] and ids[r['producao_id']] != r['objetivo']:
            raise ValueError('Objetivo diverge da producao: ' + r['id'])
        datas = []
        for k in ('publicado_em', 'coletado_em'):
            try:
                d = datetime.fromisoformat(r[k].replace('Z', '+00:00'))
            except ValueError as exc:
                raise ValueError('Data ISO 8601 invalida: ' + k) from exc
            if d.tzinfo is None or d > datetime.now(timezone.utc):
                raise ValueError('Data deve conter fuso e nao pode ser futura: ' + k)
            datas.append(d)
        if datas[1] < datas[0]:
            raise ValueError('Coleta anterior a publicacao.')
        for k in CONTAGENS + VALORES:
            v = r.get(k)
            if v is not None and (isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or v < 0 or (k in CONTAGENS and not isinstance(v, int))):
                raise ValueError('Metrica invalida: ' + k)
        # 2026-09-25: origem do video modelo (PERFIL_ORGANICO.md). REAL = pessoa real, IA = avatar IA.
        if r.get('origem') is not None and r['origem'] not in ('REAL', 'IA'):
            raise ValueError('Origem deve ser REAL ou IA: ' + r['id'])
        if any(r.get(k) is not None for k in ('receita', 'custo')) and not re.fullmatch(r'[A-Z]{3}', r.get('moeda') or ''):
            raise ValueError('Informe moeda com tres letras para receita/custo.')
    return doc


def registrar(args):
    """Grava ou atualiza UMA publicacao em resultados.json, validando o arquivo inteiro antes.

    Mesmo id = mesma publicacao: as metricas novas substituem as antigas (nova coleta), nunca somam.
    """
    path = CONTROLE / 'resultados.json'
    doc = ler_json(path)
    agora = datetime.now(timezone.utc).astimezone().replace(microsecond=0).isoformat()
    r = {'id': args.id or '%s:%s:%s:%s' % (args.producao, args.avatar, args.hook, args.canal),
         'producao_id': args.producao, 'avatar_id': args.avatar, 'hook_id': args.hook,
         'objetivo': args.objetivo, 'canal': args.canal, 'publicado_em': args.publicado_em,
         'coletado_em': args.coletado_em or agora}
    for par in args.metrica:
        if '=' not in par:
            raise ValueError('Metrica no formato nome=valor: ' + par)
        k, v = par.split('=', 1)
        if k not in CONTAGENS + VALORES:
            raise ValueError('Metrica desconhecida: ' + k)
        r[k] = int(v) if k in CONTAGENS else float(v)
    for k in ('url', 'moeda', 'observacoes', 'origem'):
        if getattr(args, k, None):
            r[k] = getattr(args, k)
    antigos = [x for x in doc['publicacoes'] if x.get('id') == r['id']]
    base = dict(antigos[0]) if antigos else {}
    base.update(r)
    novo = {'versao': doc['versao'], 'publicacoes': [x for x in doc['publicacoes'] if x.get('id') != r['id']] + [base]}
    validar_resultados(novo, {x['producao_id']: x['objetivo_declarado'] for x in biblioteca()})
    gravar_json(path, novo)
    atualizar()
    print(('Atualizada' if antigos else 'Registrada') + ' a publicacao ' + r['id'])


def razao(a, b):
    return a / b if a is not None and b is not None and b > 0 else None


def metricas(r):
    return {'taxa_3s': razao(r.get('reproducoes_3s'), r.get('visualizacoes')),
            'taxa_conclusao': razao(r.get('conclusoes'), r.get('visualizacoes')),
            'ctr': razao(r.get('cliques'), r.get('impressoes')),
            'conversao': razao(r.get('compras'), r.get('visitas_destino')),
            'roas': razao(r.get('receita'), r.get('custo'))}


def celula(s):
    return str(s if s is not None else 'Não documentado').replace('|', '\\|').replace('\n', ' ')


def atualizar():
    registros = biblioteca()
    dados = validar_resultados(ler_json(CONTROLE / 'resultados.json'), {r['producao_id']: r['objetivo_declarado'] for r in registros})
    gravar_json(CONTROLE / 'biblioteca_criativa.json', {'versao': 1, 'producoes': registros})
    linhas = ['# Biblioteca criativa', '', 'Índice derivado dos roteiros. Não é workflow nem ranking de performance. Campos ausentes permanecem não documentados. O campo de variável preserva o texto da fonte, incluindo alegações ainda não verificadas.', '', 'Para consultar: `python3 gerenciar_operacao.py buscar --angulo 3 --termo segredo`.', '']
    # Agrupa pela oferta de cada registro: no angulo 1 a Korella historica e o Sea Moss ficam separados.
    ofertas = []
    for n in (1, 2, 3, 4, None):
        for r in registros:
            if r['angulo'] == n and r['oferta'] not in ofertas:
                ofertas.append(r['oferta'])
    for oferta in ofertas:
        grupo = [r for r in registros if r['oferta'] == oferta]
        linhas += ['## ' + (oferta if oferta != 'Nao identificado' else 'Sem classificação'), '', '| Produção / fonte | Objetivo explícito | Variável e ponte documentadas | Enquadramento |', '|---|---|---|---|']
        for r in grupo:
            link = '[%s](%s)' % (r['producao_id'], quote(str(ROOT / r['fonte']), safe='/'))
            linhas.append('| ' + ' | '.join([link, celula(r['objetivo_declarado']), celula(r['variavel_e_ponte_documentadas']), celula(r['enquadramento_documentado'])]) + ' |')
        linhas.append('')
    (CONTROLE / 'BIBLIOTECA_CRIATIVA.md').write_text('\n'.join(linhas) + '\n', encoding='utf-8')
    linhas = ['# Resultados de publicação', '', 'Dados declarados pelo operador. Uma linha por publicação, com a coleta mais recente registrada. Não somar coletas de períodos diferentes nem comparar variantes com janelas de observação diferentes.', '']
    if not dados['publicacoes']:
        linhas.append('Nenhuma publicação com métricas registrada. Não há base para apontar um criativo vencedor.')
    else:
        linhas += ['| ID | Produção | Objetivo | Origem | Canal | Coletado em | 3s/views | Conclusões/views | Cliques/impressões | Compras/visitas | Receita/custo |', '|---|---|---|---|---|---|---|---|---|---|---|']
        for r in dados['publicacoes']:
            m = metricas(r)
            valores = [('%.2f%%' % (v * 100) if k != 'roas' else '%.2fx' % v) if v is not None else 'Sem base' for k, v in m.items()]
            linhas.append('| ' + ' | '.join(celula(v) for v in [r['id'], r['producao_id'], r['objetivo'], r.get('origem'), r['canal'], r['coletado_em'], *valores]) + ' |')
    linhas += ['', 'As taxas só são interpretáveis quando numerador e denominador vêm da mesma publicação, janela e definição da plataforma. Zero é resultado medido; null é desconhecido. Custo deve ter escopo consistente; receita/custo não representa lucro líquido.']
    (CONTROLE / 'RESULTADOS.md').write_text('\n'.join(linhas) + '\n', encoding='utf-8')
    print('%d roteiros indexados; %d publicacoes com dados.' % (len(registros), len(dados['publicacoes'])))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='acao', required=True)
    sub.add_parser('atualizar')
    sub.add_parser('validar')
    buscar = sub.add_parser('buscar'); buscar.add_argument('--angulo', type=int, choices=[1, 2, 3, 4]); buscar.add_argument('--termo', default='')
    sync = sub.add_parser('sincronizar-fila'); sync.add_argument('pasta', type=Path); sync.add_argument('--aplicar', action='store_true')
    reg = sub.add_parser('registrar', help='grava ou atualiza uma publicacao em resultados.json')
    for nome in ('--producao', '--avatar', '--hook', '--canal', '--publicado-em'):
        reg.add_argument(nome, required=True)
    reg.add_argument('--objetivo', required=True, choices=['SALE', 'GROWTH'])
    reg.add_argument('--coletado-em'); reg.add_argument('--id'); reg.add_argument('--url')
    reg.add_argument('--moeda'); reg.add_argument('--observacoes')
    reg.add_argument('--origem', choices=['REAL', 'IA'], help='video modelo de pessoa real ou de avatar IA (PERFIL_ORGANICO.md)')
    reg.add_argument('--metrica', action='append', default=[], help='nome=valor, repetivel')
    args = parser.parse_args()
    try:
        if args.acao == 'atualizar':
            atualizar()
        elif args.acao == 'validar':
            validar_resultados(ler_json(CONTROLE / 'resultados.json'), {r['producao_id']: r['objetivo_declarado'] for r in biblioteca()})
            print('Estrutura valida. Isso nao comprova a origem das metricas.')
        elif args.acao == 'registrar':
            registrar(args)
        elif args.acao == 'buscar':
            encontrados = [r for r in biblioteca() if (args.angulo is None or r['angulo'] == args.angulo) and normalizar(args.termo) in normalizar(json.dumps(r, ensure_ascii=False))]
            print(json.dumps(encontrados, ensure_ascii=False, indent=2))
        elif args.acao == 'sincronizar-fila':
            p = args.pasta / 'AVATAR_QUEUE.md'
            antes = p.read_text(encoding='utf-8')
            depois = sincronizar_fila((args.pasta / 'CHECKPOINT.md').read_text(encoding='utf-8'), antes)
            if args.aplicar:
                p.write_text(depois, encoding='utf-8')
                print('Fila sincronizada por identidade.')
            else:
                import difflib
                print(''.join(difflib.unified_diff(antes.splitlines(True), depois.splitlines(True), fromfile=str(p), tofile='vista derivada')), end='')
    except (ValueError, OSError) as exc:
        parser.exit(1, 'Erro: %s\n' % exc)


if __name__ == '__main__':
    main()
