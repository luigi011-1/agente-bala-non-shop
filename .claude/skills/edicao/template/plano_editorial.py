"""Plano editorial explícito; nenhuma proteção é inferida do ASR.

Tempos de proteção usam a origem do take; pontos de música usam a saída
editada. O editor continua responsável pela conferência contra o roteiro,
normalização/ducking da música, looping e validação visual.
"""
import copy
import json
import math


def _number(value, name, low=0, high=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{name}: número finito obrigatório")
    if value < low or (high is not None and value > high):
        raise ValueError(f"{name}: fora dos limites")
    return value


def _keys(obj, allowed, required, name):
    if not isinstance(obj, dict):
        raise ValueError(f"{name}: objeto obrigatório")
    if set(obj) - set(allowed) or set(required) - set(obj):
        raise ValueError(f"{name}: campos desconhecidos ou obrigatórios ausentes")


def _take(value):
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("take: inteiro positivo obrigatório")
    return value


def validar_plano(plan):
    """Valida e devolve cópia; recusa campos não implementados."""
    _keys(plan, ('version', 'offer', 'adaptation', 'protected_intervals', 'rhythm', 'music', 'captions'),
          ('version', 'offer'), 'plano')
    if type(plan['version']) is not int or plan['version'] != 1:
        raise ValueError('version deve ser 1')
    if plan['offer'] not in ('fitwell', 'sea_moss', 'auraly'):
        raise ValueError('offer não suportada')
    if 'adaptation' in plan:
        _keys(plan['adaptation'], ('rationale',), ('rationale',), 'adaptation')
        if not isinstance(plan['adaptation']['rationale'], str) or not plan['adaptation']['rationale'].strip():
            raise ValueError('adaptation.rationale obrigatório')
    if plan['offer'] == 'auraly' and 'adaptation' not in plan:
        raise ValueError('Auraly exige adaptação explícita com rationale')
    if 'captions' in plan:
        if plan['offer'] == 'auraly':
            raise ValueError('captions Auraly exige o workflow visual próprio')
        captions = plan['captions']
        _keys(captions, ('max_words', 'top', 'hero_top'), (), 'captions')
        for field, low, high in (('max_words', 2, 6), ('top', 200, 1500), ('hero_top', 200, 1500)):
            if field in captions:
                if type(captions[field]) is not int:
                    raise ValueError(f'captions.{field}: inteiro obrigatório')
                _number(captions[field], f'captions.{field}', low, high)
    for field in ('protected_intervals', 'rhythm'):
        if not isinstance(plan.get(field, []), list):
            raise ValueError(f'{field}: lista obrigatória')
    for item in plan.get('protected_intervals', []):
        _keys(item, ('take', 'start', 'end', 'reason'), ('take', 'start', 'end', 'reason'), 'proteção')
        _take(item['take'])
        _number(item['start'], 'start')
        _number(item['end'], 'end')
        if item['end'] <= item['start']:
            raise ValueError('proteção: end deve ser maior que start')
        if not isinstance(item['reason'], str) or not item['reason'].strip():
            raise ValueError('proteção exige reason')
    seen = set()
    for item in plan.get('rhythm', []):
        _keys(item, ('take', 'speed'), ('take', 'speed'), 'ritmo')
        take = _take(item['take'])
        _number(item['speed'], 'speed', 1, 1.25)
        if take in seen:
            raise ValueError('ritmo: take duplicado')
        seen.add(take)
    music = plan.get('music', {})
    _keys(music, ('start_seconds', 'fade_in_seconds', 'fade_out_seconds', 'points'), (), 'music')
    for field in ('start_seconds', 'fade_in_seconds', 'fade_out_seconds'):
        _number(music.get(field, 0), field)
    if not isinstance(music.get('points', []), list):
        raise ValueError('music.points: lista obrigatória')
    previous = -1
    for item in music.get('points', []):
        _keys(item, ('time', 'db'), ('time', 'db'), 'ponto de música')
        at = _number(item['time'], 'time')
        _number(item['db'], 'db', -30, -18)
        if at <= previous:
            raise ValueError('pontos de música devem estar em ordem estrita')
        previous = at
    return copy.deepcopy(plan)


def carregar_plano(path):
    """Lê JSON UTF-8; planos ausentes não ligam este modo automaticamente."""
    with open(path, encoding='utf-8') as handle:
        return validar_plano(json.load(handle))


def validar_contexto(plan, producao_auraly, estilo):
    """Flag de estilo não pode remover a fronteira da oferta detectada."""
    plan = validar_plano(plan)
    if producao_auraly and estilo != 'auraly':
        raise ValueError('Produção Auraly exige estilo e plano Auraly adaptados')
    if (estilo == 'auraly') != (plan['offer'] == 'auraly'):
        raise ValueError('Plano editorial de outra oferta: Auraly exige adaptação própria')
    return plan


def _union(intervals):
    result = []
    for a, b in sorted(intervals):
        if result and a <= result[-1][1]:
            result[-1][1] = max(result[-1][1], b)
        else:
            result.append([a, b])
    return result


def proteger_intervalos(intervals, take, plan, duration):
    """Une ilhas existentes à ação/pausa marcada; recusa extrapolação."""
    plan = validar_plano(plan)
    _take(take)
    _number(duration, 'duration')
    union = []
    for item in intervals:
        if not isinstance(item, (list, tuple)) or len(item) != 2:
            raise ValueError('intervalo deve ser [start,end]')
        a, b = item
        _number(a, 'start', 0, duration)
        _number(b, 'end', 0, duration)
        if b <= a:
            raise ValueError('intervalo vazio ou invertido')
        union.append([a, b])
    for item in plan.get('protected_intervals', []):
        if item['take'] == take:
            if item['end'] > duration:
                raise ValueError('proteção fora da duração do take')
            union.append([item['start'], item['end']])
    return _union(union)


def aplicar_ritmo(segs, plan):
    """Retorna cópias, com o/d recalculados e limites protegidos divididos.

    Rampas mute nunca mudam. Inserts mute em velocidade normal podem
    receber override do take; proteção usa 1x se não houver override.
    """
    plan = validar_plano(plan)
    if not isinstance(segs, list):
        raise ValueError('segs: lista obrigatória')
    speeds = {x['take']: x['speed'] for x in plan.get('rhythm', [])}
    protected = {}
    for item in plan.get('protected_intervals', []):
        protected.setdefault(item['take'], []).append([item['start'], item['end']])
    available = set()
    for seg in segs:
        _keys(seg, ('k', 'a', 'b', 'sp', 'mute', 'o', 'd'), ('k', 'a', 'b', 'sp'), 'segmento')
        available.add(_take(seg['k']))
    if (set(speeds) | set(protected)) - available:
        raise ValueError('plano referencia take ausente dos segmentos')
    result, offset = [], 0.0
    for seg in segs:
        _keys(seg, ('k', 'a', 'b', 'sp', 'mute', 'o', 'd'), ('k', 'a', 'b', 'sp'), 'segmento')
        take = _take(seg['k'])
        a, b = _number(seg['a'], 'a'), _number(seg['b'], 'b')
        speed = _number(seg['sp'], 'sp')
        for field in ('o', 'd'):
            if field in seg:
                _number(seg[field], field)
        if b <= a or speed <= 0:
            raise ValueError('segmento vazio ou velocidade zero')
        if 'mute' in seg and not isinstance(seg['mute'], bool):
            raise ValueError('mute deve ser booleano')
        spans = _union(protected.get(take, []))
        boundaries = sorted({a, b} | {t for span in spans for t in span if a < t < b})
        for start, end in zip(boundaries, boundaries[1:]):
            item = copy.deepcopy(seg)
            protected_here = any(x <= start and end <= y for x, y in spans)
            item['a'], item['b'] = start, end
            ramp = seg.get('mute') and seg['sp'] > 1.25
            if protected_here and not ramp:
                item['sp'] = speeds.get(take, 1.0)
            elif not ramp and take in speeds:
                item['sp'] = speeds[take]
            item['o'] = offset
            item['d'] = (end - start) / item['sp']
            offset += item['d']
            result.append(item)
    return result


def protected_output_windows(segs, plan):
    """Interseções protegidas na saída, para exceções delimitadas do QA.

    Não libera silêncio de um take inteiro nem deduz proteção por ASR.
    Usar depois de montar_base, que ajusta o/d à contagem real de frames.
    No QA, um silêncio só é permitido se seu intervalo INTEIRO estiver
    coberto pela união retornada; testar apenas início ou sobreposição
    liberaria indevidamente a parcela fora da proteção.
    """
    plan = validar_plano(plan)
    windows = []
    for seg in segs:
        _keys(seg, ('k', 'a', 'b', 'sp', 'mute', 'o', 'd'), ('k', 'a', 'b', 'o', 'd'), 'segmento de saída')
        _take(seg['k'])
        for field in ('a', 'b', 'o', 'd'):
            _number(seg[field], field)
        if seg['b'] <= seg['a'] or seg['d'] <= 0:
            raise ValueError('segmento de saída vazio ou invertido')
        for item in plan.get('protected_intervals', []):
            if seg['k'] != item['take']:
                continue
            start = max(seg['a'], item['start'])
            end = min(seg['b'], item['end'])
            if end > start:
                scale = seg['d'] / (seg['b'] - seg['a'])
                windows.append([seg['o'] + (start - seg['a']) * scale,
                                seg['o'] + (end - seg['a']) * scale])
    return _union(windows)


def silencios_nao_autorizados(silences, segs, plan, tolerance=0):
    """Retorna silêncios não totalmente cobertos por proteção ou mute.

    Une autorizações adjacentes antes da conferência. Tolerância máxima
    de um frame a 30fps; não usa início isolado nem overlap como permissão.
    """
    _number(tolerance, 'tolerance', 0, 1 / 30)
    windows = protected_output_windows(segs, plan)
    for seg in segs:
        if 'mute' in seg and not isinstance(seg['mute'], bool):
            raise ValueError('mute deve ser booleano')
        if seg.get('mute'):
            windows.append([seg['o'], seg['o'] + seg['d']])
    windows = _union(windows)
    if not isinstance(silences, (list, tuple)):
        raise ValueError('silences: lista obrigatória')
    rejected = []
    for silence in silences:
        if not isinstance(silence, (list, tuple)) or len(silence) != 2:
            raise ValueError('silêncio deve ser [start,end]')
        start, end = silence
        _number(start, 'silence.start')
        _number(end, 'silence.end')
        if end <= start:
            raise ValueError('silêncio vazio ou invertido')
        if not any(a - tolerance <= start and end <= b + tolerance for a, b in windows):
            rejected.append(copy.deepcopy(silence))
    return rejected


def music_start_seconds(plan):
    """Offset da fonte musical; não confundir com os pontos na saída."""
    return validar_plano(plan).get('music', {}).get('start_seconds', 0)


def filtro_musica(total, plan, base_db=-18):
    """Filtro FFmpeg para música já normalizada, antes do ducking.

    Pontos interpolam dB na timeline de saída; fora deles mantém o extremo.
    Limites -30..-18 são ganhos do filtro, não medição voz/música. A cama
    padrão vigente usa -18 dB (regras de edição, item 16b); o plano pode
    reduzi-la nas janelas marcadas. Conferir inteligibilidade no mix final.
    """
    plan = validar_plano(plan)
    _number(total, 'total')
    if total <= 0:
        raise ValueError('total deve ser positivo')
    _number(base_db, 'base_db', -30, -18)
    music = plan.get('music', {})
    points = music.get('points', [])
    if any(x['time'] > total for x in points):
        raise ValueError('ponto musical fora da timeline de saída')
    def fmt(number):
        return format(number, '.12g')
    expression = fmt(points[-1]['db']) if points else fmt(base_db)
    for left, right in reversed(list(zip(points, points[1:]))):
        delta = (right['db'] - left['db']) / (right['time'] - left['time'])
        line = f"({fmt(left['db'])}+(t-{fmt(left['time'])})*{fmt(delta)})"
        expression = f"if(lt(t,{fmt(right['time'])}),{line},{expression})"
    if points:
        expression = f"if(lt(t,{fmt(points[0]['time'])}),{fmt(points[0]['db'])},{expression})"
    filters = [f"volume='pow(10,({expression})/20)':eval=frame"]
    for kind, field in (('in', 'fade_in_seconds'), ('out', 'fade_out_seconds')):
        duration = min(total, music.get(field, .3 if kind == 'in' else .8))
        if duration:
            start = 0 if kind == 'in' else total - duration
            filters.append(f'afade=t={kind}:st={fmt(start)}:d={fmt(duration)}')
    return ','.join(filters)
