"""Durable, anchor-only ChatGPT UI jobs. No paid API or private ChatGPT endpoint."""
import copy
import hashlib
import io
import json
import os
import re
import secrets
import threading
import uuid
import zipfile
from datetime import datetime
from pathlib import Path
from PIL import Image
from . import storage as store

LOCK = threading.RLock()
ACTIVE = {'preparing', 'submitting', 'generating', 'receiving'}
DOWNLOADS = Path.home() / 'Downloads'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def token():
    path = store.DATA / 'browser-connection.key'
    with LOCK:
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text(secrets.token_urlsafe(32), encoding='utf-8')
        return path.read_text(encoding='utf-8').strip()


def load():
    path = store.DATA / 'browser-queue.json'
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else {
        'running': False, 'concurrency': 2, 'jobs': [], 'connected_at': None}


def save(state):
    store.write_json(store.DATA / 'browser-queue.json', state)
    return state


def recover():
    with LOCK:
        state = load()
        state['running'] = False
        return save(state)


def slug(value):
    return re.sub(r'[^a-zA-Z0-9_-]+', '-', value).strip('-')[:70] or 'avatar'


def standalone_prompt(frame, frames, avatar):
    """Keep full original scene text; resolve references as TEXT, never extra images."""
    by_id = {f['id']: f for f in frames}
    chain, visited = [], set()
    parent = frame.get('parent')
    while parent:
        if parent in visited or parent not in by_id:
            raise ValueError('Dependência de cena inválida.')
        visited.add(parent)
        original = by_id[parent]
        chain.insert(0, {'id': parent, 'description': original['prompt']})
        parent = original.get('parent')
    prompt = copy.deepcopy(frame['prompt'])
    prompt['reference_use'] = (
        f'The ONLY attached image is the original anchor of {avatar}. '
        'Use it for identity, clothing, room and lighting. Generate this scene as a NEW image. '
        'No previous generated image is attached or required.')
    payload = {
        'task': 'Generate ONE photorealistic vertical 9:16 image now. Do not return a text prompt or a collage.',
        'avatar': avatar,
        'reference_policy': 'One attachment only: the original avatar anchor. '
            'Prior scene identifiers in the descriptions below refer ONLY to the textual context provided here. '
            'Never ask for or assume another image. Current scene overrides prior action and props. '
            'Use the anchor as the authority for face, outfit and environment.',
        'prior_scene_text_context': chain,
        'prop_description': [{'design': f['prompt'].get('scene', ''),
                              'material': f['prompt'].get('realism', '')}
                             for f in frames if f.get('role') == 'reference'],
        'current_scene': prompt,
        'output': 'One image, portrait 9:16, natural skin texture, neutral daylight. No captions or overlays.'}
    return json.dumps(payload, ensure_ascii=False, indent=2)


def normalize_prompt_payload(value):
    payload = json.loads(value)
    normalized = []
    for item in payload.get('prop_description', []):
        if isinstance(item, dict) and ('design' in item or 'material' in item):
            normalized.append(item)
        elif isinstance(item, dict):
            normalized.append({'design': item.get('scene', ''), 'material': item.get('realism', '')})
        else:
            normalized.append(item)
    payload['prop_description'] = normalized
    return payload


def prompt_matches_current(job, frame, frames, avatar):
    expected = standalone_prompt(frame, frames, avatar)
    if expected == job['prompt']:
        return True
    try:
        return normalize_prompt_payload(expected) == normalize_prompt_payload(job['prompt'])
    except (TypeError, json.JSONDecodeError):
        return False


def enqueue(ids, limit=None, only_frame=None):
    with LOCK, store.LOCK:
        state = load()
        additions = []
        for pid in dict.fromkeys(ids):
            p = store.get(pid)
            if p.get('busy'):
                raise ValueError('Aguarde ou pause a execução por API antes de usar o Chrome.')
            frames = (p.get('plan') or {}).get('frames', [])
            if not frames:
                raise ValueError('Produção sem plano de imagens.')
            anchor = store.artifact(pid, 'anchor.png')
            anchor_hash = digest(anchor.read_bytes())
            scenes = [f for f in frames if f.get('role') != 'reference']
            if only_frame and not any(f['id'] == only_frame for f in scenes):
                raise ValueError('Esta cena não existe mais no plano atual.')
            if limit:
                scenes = scenes[:limit]
            for index, frame in enumerate(scenes, 1):
                if only_frame and frame['id'] != only_frame:
                    continue
                fid = frame['id']
                if not re.fullmatch(r'[A-Za-z0-9_-]{1,50}', fid):
                    raise ValueError('Identificador de imagem inválido.')
                prompt = standalone_prompt(frame, frames, p['avatar'])
                fingerprint = digest((pid + fid + prompt + anchor_hash).encode())
                if any(j['project'] == pid and j['frame'] == fid and j['status'] != 'cancelled'
                       for j in state['jobs'] + additions):
                    continue
                jid = uuid.uuid4().hex
                folder = DOWNLOADS / 'Auraly Studio' / (slug(p['avatar']) + '_' + datetime.now().strftime('%Y-%m-%d')) / pid[:8]
                additions.append({'id': jid, 'project': pid, 'avatar': p['avatar'],
                    'frame': fid, 'title': frame.get('title', fid), 'index': index,
                    'prompt': prompt, 'anchor_sha256': anchor_hash, 'fingerprint': fingerprint,
                    'status': 'queued', 'created': store.now(), 'tab_id': None,
                    'conversation_url': None, 'destination_dir': str(folder), 'error': None})
        state['jobs'].extend(additions)
        save(state)
        return state


def control(running, concurrency=2):
    with LOCK:
        state = load()
        state.update(running=running, concurrency=concurrency)
        return save(state)


def heartbeat():
    with LOCK:
        state = load()
        state['connected_at'] = store.now()
        return save(state)


def claim():
    with LOCK, store.LOCK:
        state = load()
        active = [j for j in state['jobs'] if j['status'] in ACTIVE]
        if not state['running'] or len(active) >= state['concurrency']:
            return None
        blocked = {j['avatar'] for j in state['jobs'] if j['status'] in ACTIVE | {'attention'}}
        for job in state['jobs']:
            if job['status'] != 'queued' or job['avatar'] in blocked:
                continue
            if store.get(job['project']).get('busy'):
                continue
            job.update(status='preparing', claimed_at=store.now())
            save(state)
            return copy.deepcopy(job)
        return None


def get_job(jid):
    return next((j for j in load()['jobs'] if j['id'] == jid), None)


def recover_job(jid, action):
    with LOCK:
        state = load()
        job = next((j for j in state['jobs'] if j['id'] == jid), None)
        if not job or job['status'] != 'attention':
            raise ValueError('Somente uma tarefa em atenção pode ser recuperada.')
        if action == 'inspect':
            if not job['tab_id']:
                raise ValueError('Não há aba registrada para consultar.')
            job.update(status='generating', error=None, claimed_at=store.now())
        elif action == 'retry':
            job['status'] = 'cancelled'
            fresh = {k: v for k, v in job.items() if k not in {
                'claimed_at', 'updated', 'file', 'local_file', 'dimensions', 'finished', 'image_sha256'}}
            fresh.update(id=uuid.uuid4().hex, status='queued', tab_id=None, conversation_url=None,
                         error=None, created=store.now(), retry_of=jid)
            state['jobs'].insert(state['jobs'].index(job) + 1, fresh)
        else:
            raise ValueError('Ação inválida.')
        return save(state)


def api_generation_allowed(pid):
    # Caller holds store.LOCK; don't acquire LOCK in reverse order here.
    if any(j['project'] == pid and j['status'] in ACTIVE | {'queued', 'attention'} for j in load()['jobs']):
        raise ValueError('Esta produção tem uma fila no Chrome. Conclua-a antes de gerar por API.')


def update(jid, status, tab_id=None, conversation_url=None, error=None):
    with LOCK:
        state = load()
        job = next((j for j in state['jobs'] if j['id'] == jid), None)
        if not job:
            raise ValueError('Tarefa inexistente.')
        allowed = {'preparing': {'preparing', 'submitting', 'attention'},
                   'submitting': {'generating', 'attention'},
                   'generating': {'generating', 'receiving', 'attention'},
                   'receiving': {'receiving', 'attention'},
                   'attention': {'generating'}}
        if status not in allowed.get(job['status'], set()):
            raise ValueError('Transição de tarefa inválida; resultado preservado.')
        if status == 'submitting' and not state['running']:
            raise ValueError('Fila pausada antes do envio.')
        job['status'] = status
        job['updated'] = store.now()
        if tab_id is not None:
            job['tab_id'] = tab_id
        if conversation_url:
            if not re.fullmatch(r'https://chatgpt\.com/c/[A-Za-z0-9-]+', conversation_url):
                raise ValueError('Conversa inválida.')
            job['conversation_url'] = conversation_url
        job['error'] = error[:1000] if error else None
        save(state)
        return job


def anchor(jid):
    job = get_job(jid)
    if not job:
        raise ValueError('Tarefa inexistente.')
    path = store.artifact(job['project'], 'anchor.png')
    if digest(path.read_bytes()) != job['anchor_sha256']:
        raise ValueError('Âncora alterada depois da criação da fila.')
    return path


def receive(jid, raw):
    if len(raw) > 35 * 1024 * 1024:
        raise ValueError('Imagem acima de 35 MB.')
    try:
        with Image.open(io.BytesIO(raw)) as im:
            fmt, dimensions = im.format, im.size
            im.verify()
        ext = {'PNG': '.png', 'JPEG': '.jpg', 'WEBP': '.webp'}[fmt]
        if min(dimensions) < 256:
            raise ValueError('Miniatura recebida em vez de imagem de produção.')
    except Exception as exc:
        raise ValueError('Imagem inválida ou miniatura; download não registrado.') from exc
    with LOCK, store.LOCK:
        state = load()
        job = next((j for j in state['jobs'] if j['id'] == jid), None)
        if not job:
            raise ValueError('Tarefa inexistente.')
        sha = digest(raw)
        if job['status'] == 'done':
            if job['image_sha256'] != sha:
                raise ValueError('Resultado diferente para uma tarefa já concluída.')
            return job
        if job['status'] not in {'generating', 'receiving', 'attention'}:
            raise ValueError('Esta tarefa ainda não foi enviada.')
        dest = Path(job['destination_dir'])
        dest.mkdir(parents=True, exist_ok=True)
        name = f"{job['index']:03d}_{job['frame']}_{job['id'][:8]}{ext}"
        path = dest / name
        # A deterministic name makes an interrupted receipt safe to repeat.
        if path.exists() and digest(path.read_bytes()) != sha:
            raise ValueError('Arquivo de saída já existe com outro conteúdo.')
        temp = path.with_suffix(ext + '.part')
        temp.write_bytes(raw)
        temp.replace(path)
        (dest / (Path(name).stem + '_prompt.json')).write_text(job['prompt'], encoding='utf-8')
        local = store.folder(job['project']) / 'browser-images' / name
        local.parent.mkdir(exist_ok=True)
        local.write_bytes(raw)
        job.update(status='done', file=str(path), local_file=str(local), image_sha256=sha,
                   dimensions=list(dimensions), finished=store.now(), error=None)
        save(state)
        store.write_json(dest / 'manifest.json', [j for j in state['jobs'] if j['destination_dir'] == str(dest)])
        store.event(job['project'], f"ChatGPT Chrome: {job['frame']} salvo em Downloads. Revisão visual pendente.")
        return job


def result_file(jid):
    job = get_job(jid)
    if not job or job['status'] != 'done':
        raise ValueError('Esta tarefa ainda não tem imagem salva.')
    path = store.artifact(job['project'], str(Path(job['local_file']).relative_to(store.folder(job['project']))))
    if digest(path.read_bytes()) != job['image_sha256']:
        raise ValueError('A imagem salva foi alterada. Revise uma nova tentativa.')
    return path


def current_scene(job, project):
    frames = (project.get('plan') or {}).get('frames', [])
    frame = next((f for f in frames if f['id'] == job['frame'] and f.get('role') != 'reference'), None)
    if not frame or not prompt_matches_current(job, frame, frames, project['avatar']):
        raise ValueError('O plano mudou desde a geração. Prepare uma nova tentativa para esta cena.')
    anchor(job['id'])
    return frame


def review(jid, decision, comment=''):
    with LOCK, store.LOCK:
        state = load()
        job = next((j for j in state['jobs'] if j['id'] == jid), None)
        if not job or job['status'] != 'done':
            raise ValueError('Somente imagens salvas podem ser revisadas.')
        if decision == 'approve':
            current_scene(job, store.get(job['project']))
            result_file(jid)
            job.update(review_status='approved', reviewed_at=store.now(), review_comment=comment)
        elif decision == 'retry':
            job.update(status='cancelled', review_status='rejected', reviewed_at=store.now(), review_comment=comment)
            # Validate before changing state; a failed retry must preserve the old job.
            project = store.get(job['project'])
            frames = (project.get('plan') or {}).get('frames', [])
            frame = next((f for f in frames if f['id'] == job['frame'] and f.get('role') != 'reference'), None)
            if project.get('busy') or not frame:
                raise ValueError('Aguarde a produção ou verifique se a cena ainda existe no plano.')
            standalone_prompt(frame, frames, project['avatar'])
            store.artifact(job['project'], 'anchor.png').read_bytes()
            save(state)
            # Rebuild only this scene from the current plan, preserving the old result on disk.
            state = enqueue([job['project']], only_frame=job['frame'])
            fresh = next((j for j in state['jobs'] if j['project'] == job['project']
                          and j['frame'] == job['frame'] and j['status'] == 'queued'), None)
            if fresh:
                fresh['retry_of'] = jid
        else:
            raise ValueError('Decisão inválida.')
        return save(state)


def export_package(pid):
    """Export only approved Chrome results, with the real image format and exact speech."""
    from .rules import validate_plan, validate_script, video_prompt
    with LOCK, store.LOCK:
        project = store.get(pid)
        validate_script(project['script'])
        validate_plan(project['plan'], project['selected'], project['script'])
        frames = [f for f in project['plan']['frames'] if f.get('role') != 'reference']
        jobs = [j for j in load()['jobs'] if j['project'] == pid and j['status'] != 'cancelled']
        selected = []
        for frame in frames:
            matches = [j for j in jobs if j['frame'] == frame['id']]
            if len(matches) != 1 or matches[0]['status'] != 'done' or matches[0].get('review_status') != 'approved':
                raise ValueError(f"{frame['id']}: gere e aprove a imagem antes de exportar o pacote completo.")
            job = matches[0]
            current_scene(job, project)
            selected.append((frame, job, result_file(job['id'])))
        takes = {t['id']: t for t in project['script']['takes']}
        clips, image_manifest = [], []
        script_lines = [f"# {project['title']} · {project['avatar']}", '', '## Roteiro cena a cena', '']
        for take in takes.values():
            script_lines.extend([f"### {take['id']} · {take['beat']} · Setup {take['setup']}",
                                 '', take['speech'], '', take['translation'], ''])
        script_lines.extend(['## Roteiro só-fala', '', '\n\n'.join(t['speech'] for t in takes.values())])
        prompts = [f"# Prompts de produção · {project['avatar']}", '',
                   'Cada imagem foi gerada com a âncora original. Referências de objetos são descrições textuais.', '',
                   '## Identidade e continuidade', '', project['script'].get('identity_lock', ''), '',
                   project['script'].get('continuity', ''), '']
        for frame, job, path in selected:
            member = f"imagens/{frame['id']}{path.suffix.lower()}"
            image_manifest.append({'frame': frame['id'], 'file': member, 'job': job['id'],
                'sha256': job['image_sha256'], 'anchor_sha256': job['anchor_sha256'],
                'dimensions': job['dimensions'], 'reviewed_at': job['reviewed_at'],
                'review_comment': job.get('review_comment', ''), 'conversation_url': job.get('conversation_url')})
            prompts.extend([f"## {frame['id']} · {frame['title']}", '', f'Imagem: {member}', '',
                            '```json', job['prompt'], '```', ''])
            for tid in frame['takes']:
                hook = next((h for h in project['hooks'] if h['id'] == frame.get('hook_id')), None)
                clip = {'id': f'V{len(clips)+1:02}', 'take': tid, 'image': member,
                        'hook_id': frame.get('hook_id'),
                        'prompt': video_prompt(takes[tid], hook['action'] if hook else takes[tid]['action'])}
                clips.append(clip)
                prompts.extend([f"### {clip['id']} · {tid} · usa {member}", '', '```text', clip['prompt'], '```', ''])
        prompts.extend(['## Montagem no CapCut', '',
                        'Cada gancho + corpo e CTA em ordem de take. Vertical 9:16. Legendas e setas na edição.', '',
                        '## Revisão antes do Flow', '',
                        'Conferir identidade, mãos, carta, continuidade, estado inicial da ação e fala completa.'])
        manifest = {'project': pid, 'title': project['title'], 'avatar': project['avatar'],
                    'source': 'chatgpt-chrome', 'model': None, 'exported_at': store.now(),
                    'images': image_manifest, 'clips': clips, 'selected_hooks': project['selected']}
        target = store.folder(pid) / 'auraly-chrome-flow.zip'
        temp = target.with_suffix('.zip.tmp')
        with zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED) as archive:
            for frame, job, path in selected:
                archive.write(path, f"imagens/{frame['id']}{path.suffix.lower()}")
                archive.writestr(f"prompts/{frame['id']}.json", job['prompt'])
            archive.write(store.artifact(pid, 'anchor.png'), 'ancora/anchor.png')
            archive.writestr('ROTEIRO.md', '\n'.join(script_lines))
            archive.writestr('PROMPTS_PRODUCAO.md', '\n'.join(prompts))
            archive.writestr('FLOW_PROMPTS.txt', '\n\n'.join(
                f"{c['id']} | {c['take']} | imagem {c['image']}\n{c['prompt']}" for c in clips))
            archive.writestr('manifest.json', json.dumps(manifest, ensure_ascii=False, indent=2))
            analysis = store.folder(pid) / 'ANALISE.json'
            if analysis.is_file():
                archive.write(analysis, 'ANALISE.json')
        temp.replace(target)
        return target
