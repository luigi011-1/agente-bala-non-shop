"""Shared analysis, isolated avatar projects, bounded existing worker pool."""
import copy
import shutil
from PIL import Image
from . import storage as store, engine, provider
from .rules import validate_script


def create(source_id, avatars, registry, count, request_id):
    with store.LOCK:
        source = store.get(source_id)
        existing = source.get('batches', {}).get(request_id)
        if existing:
            return existing
        if source['busy'] or not source.get('analysis') or source['status'] in ('uploaded', 'extracted', 'analysis_ready'):
            raise ValueError('Conclua e aprove a análise comum antes de criar o lote.')
        if not 1 <= count <= 5 or not avatars or len(set(avatars)) != len(avatars):
            raise ValueError('Escolha avatares diferentes e 1–5 variações.')
        if any(a not in registry or not registry[a][1].is_file() for a in avatars):
            raise ValueError('Âncora de avatar indisponível.')
        for filename in ('source.mp4', 'sources.md', 'ANALISE.json'):
            if not (store.folder(source_id) / filename).is_file():
                raise ValueError(f'Referência comum incompleta: {filename}.')
        for avatar in avatars:
            with Image.open(registry[avatar][1]) as image:
                image.verify()
        ids = []
        for avatar in avatars:
            name, anchor = registry[avatar]
            p = store.create(f'{source["title"][:70]} · {name}', name, source['direction'])
            folder = store.folder(p['id'])
            for filename in ('source.mp4', 'sources.md', 'ANALISE.json'):
                shutil.copy2(store.folder(source_id) / filename, folder / filename)
            with Image.open(anchor) as image:
                image.convert('RGB').save(folder / 'anchor.png')
            values = {k: copy.deepcopy(source[k]) for k in ('analysis', 'transcript', 'sources', 'duration', 'extraction', 'clarification') if k in source}
            store.change(p['id'], **values, status='analysis_approved', batch_source=source_id,
                         batch_id=request_id, hook_count=count, queue_state='ready',
                         call_limits={'text': 100, 'image': 32})
            ids.append(p['id'])
        source.setdefault('batches', {})[request_id] = ids
        store.save(source)
        return ids


def advance(pid, produce=False):
    while True:
        p = store.get(pid)
        if p.get('pause_requested'):
            raise ValueError('Lote pausado; resultados preservados.')
        status = p['status']
        if status == 'analysis_approved':
            engine.script(pid)
        elif not produce:
            return
        elif status == 'script_ready':
            validate_script(p['script'])
            store.change(pid, status='script_approved', script_approved_at=store.now(), approval_mode='batch_operator_authorization')
        elif status == 'script_approved':
            engine.hooks(pid)
        elif status == 'hooks_ready':
            selected = [h['id'] for h in p['hooks'][:p['hook_count']]]
            if len(selected) != p['hook_count']:
                raise ValueError('Quantidade de ganchos insuficiente.')
            store.change(pid, selected=selected, status='hooks_selected')
        elif status == 'hooks_selected':
            engine.plan(pid)
        elif status in ('plan_ready', 'generating'):
            store.change(pid, status='generating')
            engine.generate(pid)
        else:
            return


def worker(pid, produce):
    try:
        store.change(pid, queue_state='running')
        advance(pid, produce)
        store.change(pid, queue_state='complete' if store.get(pid)['status'] == 'complete' else 'review')
    except Exception as exc:
        store.change(pid, error=provider.safe_error(exc), queue_state='attention')
        store.event(pid, 'Atenção: ' + provider.safe_error(exc))
    finally:
        store.change(pid, busy=False)


def enqueue(ids, pool, produce=False):
    queued = []
    with store.LOCK:
        projects = [store.get(pid) for pid in dict.fromkeys(ids)]
        if any(not p.get('batch_source') for p in projects):
            raise ValueError('Projeto não pertence a um lote.')
        provider.require_think_key()
        if produce:
            from .browser_queue import api_generation_allowed
            for p in projects:
                api_generation_allowed(p['id'])
            provider.require_image_key()
        for p in projects:
            if p['busy'] or p['status'] == 'complete':
                continue
            store.change(p['id'], busy=True, error=None, pause_requested=False,
                         queue_state='queued', batch_produce_authorized=produce)
            pool.submit(worker, p['id'], produce)
            queued.append(p['id'])
    return queued
