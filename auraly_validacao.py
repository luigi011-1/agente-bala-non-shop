"""Verificacoes documentais Auraly. Nao altera producoes nem executa geracao."""
from pathlib import Path
import re
import unicodedata


def normalizar(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c)).lower()


def campo(texto, nome):
    matches = re.findall(r'^' + re.escape(nome) + r':\s*(.*?)\s*$', texto, re.M | re.I)
    return matches[-1] if matches else ''


def objetivo(roteiro, checkpoint=''):
    """Somente campo explicito ou cabecalho de funil, nunca a transcricao do modelo."""
    declarado = campo(checkpoint, 'Objective') or campo(roteiro[:2000], 'objective')
    if declarado:
        value = normalizar(declarado).strip()
        return {'growth': 'GROWTH', 'crescimento': 'GROWTH', 'sale': 'SALE', 'venda': 'SALE'}.get(value, 'INVALID')
    for linha in roteiro.splitlines():
        if re.match(r'^##\s', linha):
            break
        if re.search(r'\*\*Funil\s*:?\*\*', linha, re.I):
            if 'crescimento' in normalizar(linha):
                return 'GROWTH'
    return 'SALE'


# 2026-09-20: o Auraly deixou de usar o portfolio 4/3/3 em tres familias e passou
# a usar o METODO PUZZLE aplicado ao hook do VIDEO MODELO, igual ao Angulo 2:
# uma unica acao estrutural preservada e 10 variacoes trocando UMA variavel cada.
# A regex de familia some junto com o contrato antigo.
RE_ACAO_ESTRUTURAL = re.compile(
    r'^\s*(?:[-*]\s*)?(?:\*\*)?(?:A[cç][aã]o estrutural|Structural action)(?:\*\*)?\s*:',
    re.M | re.I)
RE_HOOK_PORTFOLIO = re.compile(r'^(?:#{1,6}\s*)?HOOK\s+(\d+)\b[^\n]*$', re.M | re.I)
DEGRAUS = {'dificuldade', 'contradicao', 'reacao', 'eua', 'escala',
           'struggle', 'contradiction', 'reaction', 'usa', 'scale'}


def _valor_rotulo(bloco, nomes):
    """Le campo de uma linha ou o primeiro valor util logo abaixo do rotulo."""
    alt = '|'.join(nomes)
    padrao = re.compile(
        r'^\s*(?:[-*]\s*)?(?:\*\*)?(?:' + alt + r')(?:\*\*)?\s*:\s*(.*?)\s*$',
        re.M | re.I)
    m = padrao.search(bloco)
    if not m:
        return ''
    if m[1].strip():
        return m[1].strip()
    resto = bloco[m.end():]
    for linha in resto.splitlines():
        valor = linha.strip().strip('*').strip()
        if not valor:
            continue
        if valor.startswith('#') or re.match(r'^[A-Za-zÁ-Úá-ú ]+\s*:', valor):
            return ''
        return valor
    return ''


RE_RODADA = re.compile(
    r'^\s*(?:[-*]\s*)?(?:\*\*)?(?:Rodada|Round)(?:\*\*)?\s*:\s*(?:\*\*)?\s*([A-Za-zÇçÃã]+)', re.M | re.I)


def rodada_ganchos(texto):
    """VALIDACAO ou VARIACAO pelo rotulo do topo; sem rotulo = contrato das 10 (historico)."""
    m = RE_RODADA.search(texto or '')
    if not m:
        return ''
    v = normalizar(m[1])
    if v.startswith('valida'):
        return 'VALIDACAO'
    if v.startswith('varia'):
        return 'VARIACAO'
    return 'INVALIDA'


def validar_hook_fiel(texto):
    """Rodada de validacao (Luigi, 2026-09-23): UM hook, o do video modelo, clonado fiel.

    Sem degrau, sem controle e sem as 10. Cada desvio do modelo vem declarado.
    """
    issues = []
    add = lambda nivel, msg, loc='GANCHOS_VISUAIS.md': issues.append(
        (nivel, 'hook-fiel', msg, loc))
    hooks = list(RE_HOOK_PORTFOLIO.finditer(texto))
    topo = texto[:hooks[0].start()] if hooks else texto
    if not RE_ACAO_ESTRUTURAL.search(texto):
        add('FALHA', 'Falta "Acao estrutural:" do hook do video modelo.')
    if not _valor_rotulo(topo, [r'Pe[cç]a viral', r'Viral piece']):
        add('FALHA', 'Falta "Peca viral:" no topo (o que fez o modelo viralizar).')
    if _valor_rotulo(topo, [r'Degrau', r'Step up']):
        add('FALHA', 'Rodada de validacao nao leva degrau: o hook e o do modelo, fiel.')
    if len(hooks) != 1 or hooks[0][1] != '1':
        add('FALHA', 'Rodada de validacao exige um unico HOOK 1 (o fiel); as 10 variacoes '
                     'so existem na rodada de variacao.')
        return issues
    if not re.search(r'\bFIEL\b|\bFAITHFUL\b', hooks[0][0], re.I):
        add('FALHA', 'O HOOK 1 da rodada de validacao deve vir marcado como FIEL.')
    secao = texto[hooks[0].end():]
    for nomes, nome in (([r'Cena', r'Scene'], 'Cena'),
                        ([r'Screen text', r'Texto de tela'], 'Screen text'),
                        ([r'Desvios obrigat[oó]rios', r'Forced deviations'], 'Desvios obrigatorios')):
        if not _valor_rotulo(secao, nomes):
            add('FALHA', 'HOOK 1 sem %s.' % nome)
    if not any(i[0] == 'FALHA' for i in issues):
        add('OK', 'Rodada de validacao: um hook fiel ao modelo, desvios declarados.')
    return issues


def validar_portfolio_ganchos(texto, estrito=False):
    """Valida o contrato Auraly de 10 variacoes por PUZZLE, sem tocar outros angulos.

    Substitui em 2026-09-20 o contrato 4/3/3 em tres familias. Agora o esqueleto
    vem do hook do VIDEO MODELO, fica intacto nas dez, e cada hook troca UMA
    variavel. Mesmo mecanismo do Angulo 2, decidido pelo Luigi.
    """
    issues = []
    add = lambda nivel, msg, loc='GANCHOS_VISUAIS.md': issues.append(
        (nivel, 'portfolio-hooks', msg, loc))
    if not texto:
        add('FALHA' if estrito else 'AVISO',
            'GANCHOS_VISUAIS.md ausente; o gancho da producao nao foi verificado.')
        return issues

    rodada = rodada_ganchos(texto)
    if rodada == 'INVALIDA':
        add('FALHA', 'Rodada deve ser VALIDACAO ou VARIACAO.')
        return issues
    if rodada == 'VALIDACAO':
        return validar_hook_fiel(texto)
    topo_rodada = texto[:RE_HOOK_PORTFOLIO.search(texto).start()] \
        if RE_HOOK_PORTFOLIO.search(texto) else texto
    if rodada == 'VARIACAO' and not _valor_rotulo(topo_rodada, [r'Base validada', r'Validated from']):
        add('FALHA', 'Rodada de variacao sem "Base validada:" (so abre depois de um video '
                     'postado performar, por ordem do Luigi).')
    elif not rodada:
        add('FALHA' if estrito else 'AVISO',
            'Falta "Rodada:" no topo (VALIDACAO ou VARIACAO, GATE_VISUAL.md Parte 4 Passo 0).')

    acao = RE_ACAO_ESTRUTURAL.search(texto)
    hooks = list(RE_HOOK_PORTFOLIO.finditer(texto))
    # A "Acao estrutural" e o que marca o contrato novo, do mesmo jeito que o
    # cabecalho 4/3/3 marcava o anterior. Sem ela o arquivo e formato historico:
    # avisa no modo normal e so reprova no estrito.
    if not acao:
        add('FALHA' if estrito else 'AVISO',
            'Formato historico: falta a "Acao estrutural:" preservada do hook do video modelo.')
        return issues
    if re.search(r'PORTFOLIO\s+AURALY\s+4\s*/\s*3\s*/\s*3', texto, re.I) or \
       re.search(r'^(?:#{1,6}\s*)?(?:FAMILY|FAM[IÍ]LIA)\s+[ABC]\b', texto, re.M | re.I):
        add('FALHA', 'Contrato 4/3/3 em familias foi revogado em 2026-09-20; '
                     'usar uma acao estrutural unica e 10 variacoes por Puzzle.')

    # 2026-09-22: PUZZLE COM DEGRAU (GATE_VISUAL.md, Parte 4). O topo declara a peca
    # viral e UM degrau aplicado ao esqueleto; HOOK 1 e o CONTROLE sem degrau. Pacote
    # anterior a isso so avisa no modo normal, igual a regra da acao estrutural.
    topo = texto[:hooks[0].start()] if hooks else texto
    nivel_novo = 'FALHA' if estrito else 'AVISO'
    if not _valor_rotulo(topo, [r'Pe[cç]a viral', r'Viral piece']):
        add(nivel_novo, 'Falta "Peca viral:" no topo (o que fez o modelo viralizar, intocavel).')
    degrau = _valor_rotulo(topo, [r'Degrau', r'Step up'])
    if not degrau:
        add(nivel_novo, 'Falta "Degrau:" no topo (Puzzle com degrau, GATE_VISUAL.md Parte 4).')
    else:
        dm = re.match(r'^([A-Za-zÁ-Úá-ú_]+)', degrau)
        if not dm or normalizar(dm[1]) not in DEGRAUS:
            add('FALHA', 'Degrau "%s" fora da escada: DIFICULDADE, CONTRADICAO, REACAO, EUA '
                         'ou ESCALA.' % degrau)
    controles = [m for m in hooks if re.search(r'\bCONTROLE?\b', m[0], re.I)]
    if len(controles) > 1:
        add('FALHA', 'Mais de um HOOK marcado como CONTROLE; o controle e unico.')
    elif not controles:
        add(nivel_novo, 'Nenhum HOOK marcado como CONTROLE (esqueleto original, sem o degrau).')
    elif controles[0][1] != '1':
        add('AVISO', 'O CONTROLE deveria ser o HOOK 1 (o mais congruente com o modelo).')

    numeros = [int(m[1]) for m in hooks]
    if len(numeros) != 10 or sorted(numeros) != list(range(1, 11)):
        add('FALHA', 'Exige exatamente HOOK 1 a HOOK 10, sem lacunas ou duplicatas.')

    categorias = {'object', 'material', 'color', 'location', 'angle', 'result', 'marker',
                  'objeto', 'cor', 'local', 'angulo', 'resultado', 'marcador',
                  'substancia', 'substance', 'alvo', 'target'}
    anomalias = {'fisica', 'contextual', 'transformacional', 'semantica',
                 'physical', 'transformational', 'semantic'}
    for i, hm in enumerate(hooks):
        fim = hooks[i + 1].start() if i + 1 < len(hooks) else len(texto)
        secao = texto[hm.end():fim]
        loc = 'GANCHOS_VISUAIS.md:%d' % (texto.count('\n', 0, hm.start()) + 1)
        variavel = _valor_rotulo(secao, [r'Changed variable', r'Vari[aá]vel alterada',
                                         r'Vari[aá]vel trocada'])
        vm = re.match(r'^([A-Za-zÁ-Úá-ú]+)\s*(?:-|—|:)\s*(.+)$', variavel)
        if not vm or normalizar(vm[1]) not in categorias or not vm[2].strip():
            add('FALHA', 'HOOK %s deve declarar uma categoria e uma unica mudanca '
                         'em Variavel trocada.' % hm[1], loc)
        elif re.search(r'\b(?:OBJECT|MATERIAL|COLOR|LOCATION|ANGLE|RESULT|MARKER|OBJETO|COR'
                       r'|LOCAL|ANGULO|RESULTADO|MARCADOR|SUBSTANCIA|ALVO)\s*(?:-|—|:)',
                       vm[2], re.I):
            add('FALHA', 'HOOK %s declara mais de uma variavel central.' % hm[1], loc)
        anomalia = normalizar(_valor_rotulo(secao, [r'Dominant anomaly', r'Anomalia dominante']))
        if anomalia not in anomalias:
            add('FALHA', 'HOOK %s sem uma anomalia dominante valida.' % hm[1], loc)
        for nomes, campo_nome in (([r'Screen text', r'Texto de tela'], 'Screen text'),
                                  ([r'Delayed meaning', r'Significado adiado'], 'Delayed meaning')):
            if not _valor_rotulo(secao, nomes):
                add('FALHA', 'HOOK %s sem %s.' % (hm[1], campo_nome), loc)

    if not any(i[0] == 'FALHA' for i in issues):
        add('OK', 'Hooks Auraly validos: acao estrutural preservada e 10 variacoes, '
                  'uma variavel trocada por hook.')
    return issues


def fila_checkpoint(texto):
    secao = re.search(r'^## Avatar queue\s*\n(.*?)(?=^## |\Z)', texto, re.M | re.S)
    return re.findall(r'^\[(DONE|ACTIVE|PENDING)\]\s+(.+?)\s*$', secao[1], re.M) if secao else []


def fila_tabela(texto):
    out = []
    for linha in texto.splitlines():
        cols = [c.strip() for c in linha.strip().strip('|').split('|')]
        if len(cols) >= 4 and cols[0].isdigit():
            status = re.match(r'(DONE|ACTIVE|PENDING)\b', cols[-1])
            if status:
                out.append((status[1], cols[1]))
    return out


def verificar_estado(checkpoint, queue='', estrito=False):
    issues = []
    add = lambda nivel, msg: issues.append((nivel, 'estado', msg, 'CHECKPOINT.md'))
    if not checkpoint:
        add('FALHA' if estrito else 'AVISO', 'Sem checkpoint: estado e aprovacoes nao verificados (pasta historica).')
        return issues
    stages = {'INTAKE', 'WAITING_ANGLE', 'ANALYSIS', 'METHOD_PUZZLE', 'SCRIPT_MODELLING', 'WAITING_SCRIPT_APPROVAL', 'HOOK_IDEATION', 'WAITING_HOOK_SELECTION', 'IMAGE_PROMPTS', 'WAITING_IMAGE_SELECTION', 'VIDEO_PROMPTS', 'AVATAR_TRANSITION', 'PRODUCTION_COMPLETE'}
    stage = campo(checkpoint, 'Current stage')
    if stage not in stages:
        add('FALHA', 'Current stage ausente ou invalido.')
    for name in ('Production', 'Angle', 'Reference video', 'Current avatar', 'Next action'):
        if not campo(checkpoint, name):
            add('FALHA', name + ' ausente.')
    if not campo(checkpoint, 'Objective'):
        add('FALHA' if estrito else 'AVISO', 'Objective ausente: explicitar SALE ou GROWTH ao retomar.')
    elif objetivo('', checkpoint) == 'INVALID':
        add('FALHA', 'Objective deve ser SALE ou GROWTH.')
    # 2026-09-23 (Luigi): validar antes de variar. VALIDATION nao passa por selecao de hook;
    # VARIATION so existe apontando o video validado.
    rodada = campo(checkpoint, 'Round').upper()
    if not rodada:
        add('FALHA' if estrito else 'AVISO',
            'Round ausente: explicitar VALIDATION ou VARIATION (GATE_VISUAL.md Parte 4 Passo 0).')
    elif rodada not in ('VALIDATION', 'VARIATION'):
        add('FALHA', 'Round deve ser VALIDATION ou VARIATION.')
    elif rodada == 'VALIDATION' and stage in ('HOOK_IDEATION', 'WAITING_HOOK_SELECTION'):
        add('FALHA', 'Round VALIDATION nao tem etapa de hooks: aprovado o roteiro, vai para IMAGE_PROMPTS.')
    elif rodada == 'VARIATION' and not campo(checkpoint, 'Validated from'):
        add('FALHA', 'Round VARIATION sem "Validated from:" (producao, avatar e resultado do video validado).')
    actions = set(re.findall(r'^Next action:\s*(.+)$', checkpoint, re.M))
    if len(actions) > 1:
        add('FALHA', 'Next action divergente dentro do checkpoint.')
    fila = fila_checkpoint(checkpoint)
    nomes = [normalizar(nome) for _, nome in fila]
    if not fila or len(nomes) != len(set(nomes)):
        add('FALHA', 'Fila ausente ou com identidades duplicadas.')
    ativos = [nome for estado, nome in fila if estado == 'ACTIVE']
    if len(ativos) > 1:
        add('FALHA', 'Mais de um avatar ACTIVE.')
    if stage == 'PRODUCTION_COMPLETE':
        if not fila or any(s != 'DONE' for s, _ in fila):
            add('FALHA', 'PRODUCTION_COMPLETE com avatares nao concluidos.')
        if campo(checkpoint, 'Current avatar').upper() != 'NONE':
            add('FALHA', 'Producao completa deve ter Current avatar: NONE.')
    elif ativos and normalizar(campo(checkpoint, 'Current avatar')) != normalizar(ativos[0]):
        add('FALHA', 'Current avatar nao corresponde ao ACTIVE da fila.')
    if queue:
        q = {normalizar(n): s for s, n in fila_tabela(queue)}
        c = {normalizar(n): s for s, n in fila}
        if q != c:
            add('FALHA', 'AVATAR_QUEUE diverge do checkpoint autoritativo. Sincronizar a vista, sem reabrir pacotes.')
    return issues


RE_CODIGO = re.compile(r'^(?:#{1,4}\s+)?([KV]\d+[A-Z]?)\s*(?:[·|].*)?$', re.M)
RE_MAPA_KV = re.compile(
    r'^(?:#{1,4}\s+)?(V\d+[A-Z]?)\b[^\n]*?(?:->|:|usa\s+|·\s*(?:T\d+\s*·\s*)?)\s*(K\d+[A-Z]?)\b',
    re.M | re.I)


def blocos(texto):
    """Le tanto K/V limpos quanto headings historicos; preserva localizacao."""
    ms = list(RE_CODIGO.finditer(texto))
    out = []
    for i, m in enumerate(ms):
        corpo = texto[m.end():ms[i + 1].start() if i + 1 < len(ms) else len(texto)].strip()
        fenced = re.search(r'```(?:text|json)?\s*\n(.*?)\n```', corpo, re.S)
        if fenced:
            corpo = fenced[1].strip()
        else:
            corpo = re.sub(r'^```\w*\s*$','',corpo, flags=re.M).strip()
        out.append({'id': m[1], 'bloco': corpo, 'linha': texto.count('\n', 0, m.start()) + 1, 'head': m[0]})
    return out


def mapa_kv(texto):
    """Extrai V -> K tanto do MAPA K/V limpo quanto de headings historicos."""
    return [(m[1].upper(), m[2].upper(), texto.count('\n', 0, m.start()) + 1)
            for m in RE_MAPA_KV.finditer(texto)]


def fala_video(texto):
    if re.search(r'sem fala no take|no speech|no dialogue|silent clip', texto, re.I):
        return None, True
    m = re.search(r'(?:a seguinte frase|voice|tone):\s*"([^"\n]+)"', texto, re.I)
    if not m:
        m = re.search(r'"([^"\n]{15,}?)"', texto)
    return (m[1] if m else None), False


def texto_fala(s):
    return re.sub(r'\s+', ' ', (s or '').translate(str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'}))).strip().strip('"')


def auditar_pacote(pasta, takes, estrito=False):
    pasta = Path(pasta)
    checkpoint = (pasta / 'CHECKPOINT.md').read_text() if (pasta / 'CHECKPOINT.md').exists() else ''
    queue = (pasta / 'AVATAR_QUEUE.md').read_text() if (pasta / 'AVATAR_QUEUE.md').exists() else ''
    issues = verificar_estado(checkpoint, queue, estrito)
    parsed = {}
    mapas = {}
    imagens_por_pasta = {}
    for p in sorted(pasta.rglob('*')):
        if p.suffix.lower() not in {'.md', '.txt'} or not re.match(r'(PROMPTS|FLOW|BLOCO|VIDEO_BLOCK|IMAGE_BLOCK|CENARIO_)', p.name, re.I):
            if not re.match(r'MAPA', p.name, re.I):
                continue
        if any(part in {'watch', 'pacote_browser'} for part in p.relative_to(pasta).parts):
            continue
        texto = p.read_text()
        bs = blocos(texto)
        if bs:
            parsed[p] = bs
        elif 'VIDEO' in p.stem.upper():
            issues.append(('FALHA', 'cobertura', 'Arquivo de video sem codigos reconheciveis.', str(p.relative_to(pasta))))
        for v, k, linha in mapa_kv(texto):
            chave = (p.parent, v)
            if chave in mapas and mapas[chave][0] != k:
                issues.append(('FALHA', 'casamento-kv',
                               '%s tem mapas conflitantes: %s e %s.' % (v, mapas[chave][0], k),
                               '%s:%d' % (p.relative_to(pasta), linha)))
            else:
                mapas[chave] = (k, p)
        for b in bs:
            if b['id'].startswith('K'):
                imagens_por_pasta.setdefault(p.parent, set()).add(b['id'])
    falas = {texto_fala(t['fala']) for t in takes if t['fala']}
    mudo = any(t['mudo'] for t in takes)
    obrigatorias = {texto_fala(t['fala']) for t in takes if t['fala'] and not t['mudo']}
    nvideo = 0
    for p, bs in parsed.items():
        loc = str(p.relative_to(pasta))
        vistos = set()
        reconhecidas = set()
        videos = [b for b in bs if b['id'].startswith('V')]
        for b in bs:
            code, body = b['id'], b['bloco']
            at = '%s:%d' % (loc, b['linha'])
            if code in vistos:
                issues.append(('FALHA', 'codigos', code + ' duplicado no arquivo.', at))
            vistos.add(code)
            if not body:
                issues.append(('FALHA', 'cobertura', code + ' sem prompt.', at))
            if not code.startswith('V'):
                continue
            nvideo += 1
            fala, silent = fala_video(body)
            if silent:
                if not mudo:
                    issues.append(('FALHA', 'fala-literal', code + ' mudo sem take mudo correspondente.', at))
            elif not fala or texto_fala(fala) not in falas:
                issues.append(('FALHA', 'fala-literal', code + ' sem correspondencia literal no roteiro aprovado.', at))
            else:
                reconhecidas.add(texto_fala(fala))
            if not re.search(r'sem m[uú]sica|no music', body, re.I):
                issues.append(('FALHA', 'blocos-video', code + ' sem indicacao de ausencia de musica.', at))
            if not silent and not re.search(r'lip[ -]?sync', body, re.I):
                issues.append(('FALHA', 'blocos-video', code + ' sem indicacao de lip sync.', at))
        # Lotes parciais sao documentados como tais; nao afirmar cobertura de roteiro inteiro.
        parcial = bool(re.search(r'lote|ciclo', p.stem, re.I))
        if videos and not parcial and obrigatorias - reconhecidas:
            issues.append(('FALHA', 'cobertura', '%s: %d fala(s) do roteiro nao cobertas.' % (p.name, len(obrigatorias - reconhecidas)), loc))
        if videos and checkpoint:
            imagens = imagens_por_pasta.get(p.parent, set())
            if not imagens:
                issues.append(('FALHA', 'casamento-kv', 'Nao foi possivel identificar univocamente o pacote K deste avatar.', loc))
            else:
                faltam, sem_mapa = [], []
                for b in videos:
                    code = b['id']
                    explicito = mapas.get((p.parent, code), (None, None))[0]
                    correspondente = code.replace('V', 'K', 1)
                    k = explicito or (correspondente if correspondente in imagens else None)
                    if not k:
                        sem_mapa.append(code)
                    elif k not in imagens:
                        faltam.append('%s -> %s' % (code, k))
                if sem_mapa:
                    issues.append(('FALHA', 'casamento-kv',
                                   'V sem MAPA K/V explicito e sem K de mesmo numero: ' + ', '.join(sem_mapa), loc))
                if faltam:
                    issues.append(('FALHA', 'casamento-kv',
                                   'MAPA K/V aponta para imagens ausentes: ' + ', '.join(faltam), loc))
    if not takes:
        issues.append(('FALHA', 'cobertura', 'Nenhum take reconhecido no roteiro. Copy nao verificada.', 'ROTEIRO.md'))
    if not nvideo:
        nivel = 'FALHA' if campo(checkpoint, 'Current stage') == 'PRODUCTION_COMPLETE' else 'AVISO'
        issues.append((nivel, 'cobertura', 'Nenhum prompt V verificado; a etapa pode ainda nao ter sido entregue.', str(pasta)))
    else:
        issues.append(('OK', 'cobertura', '%d prompts V examinados em %d arquivos de pacote; nao comprova geracao/publicacao.' % (nvideo, len(parsed)), str(pasta)))
    return issues


def sincronizar_fila(checkpoint, queue):
    """Deriva somente estados da tabela. Falha se os nomes nao casarem exatamente."""
    fc, ft = fila_checkpoint(checkpoint), fila_tabela(queue)
    estados = {normalizar(n): s for s, n in fc}
    atuais = {normalizar(n): s for s, n in ft}
    if len(fc) != len(estados) or len(ft) != len(atuais):
        raise ValueError('Identidades duplicadas: sincronizacao recusada.')
    if not estados or estados.keys() != atuais.keys():
        raise ValueError('Identidades divergentes: nao sincronizar pela ordem.')
    lines = []
    for line in queue.splitlines():
        cols = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cols) >= 4 and cols[0].isdigit() and normalizar(cols[1]) in estados:
            cols[-1] = re.sub(r'^(DONE|ACTIVE|PENDING)\b', estados[normalizar(cols[1])], cols[-1])
            line = '| ' + ' | '.join(cols) + ' |'
        elif line.startswith('**Estado:**'):
            line = '**Estado:** ' + campo(checkpoint, 'Current stage') + ' (derivado de CHECKPOINT.md)'
        lines.append(line)
    return '\n'.join(lines) + '\n'
