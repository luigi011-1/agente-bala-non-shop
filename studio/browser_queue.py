"""Durable, anchor-only ChatGPT UI jobs. No paid API or private ChatGPT endpoint.

One project holds one bilingual script, the selected visual hooks and N avatar anchors.
enqueue() fans the image set (one frame per hook + BODY + CTA) across every avatar, so a
job is identified by (project, avatar, frame). The extension runs one ChatGPT tab per
avatar.
"""
import copy
import hashlib
import io
import json
import re
import secrets
import threading
import uuid
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

from PIL import Image

from . import storage as store

LOCK = threading.RLock()
ACTIVE = {'preparing', 'submitting', 'generating', 'receiving'}
DOWNLOADS = Path.home() / 'Downloads'
# Maximum validity of a preflight receipt. This is NOT a sleep or minimum wait — it is
# only the expiry window. A receipt is valid from registration until this many seconds
# have elapsed. 120s gives ample cover for concurrent activation of 4 assets while
# keeping stale receipts from lingering. Reducing below ~60s risks timeout during the
# activate round-trip on a slow network; never introduce sleep(TTL) anywhere.
PREFLIGHT_TTL_SECONDS = 120


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
        'running': False, 'concurrency': 4, 'jobs': [], 'connected_at': None,
        'preflights': [], 'preflight_requests': [], 'extension_session_id': None,
        'batch_authorizations': []}


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


def has_jobs(pid):
    return any((j.get('project') == pid or j.get('production_id') == pid)
               and j['status'] != 'cancelled' for j in load()['jobs'])


def clear(pid):
    """Drop this project's queue so avatars can be changed. Files already saved stay on disk."""
    with LOCK:
        state = load()
        scoped = [j for j in state['jobs'] if j.get('project') == pid or j.get('production_id') == pid]
        if any(j['status'] in ACTIVE for j in scoped):
            raise ValueError('Há envios em andamento. Pause e aguarde antes de limpar a fila.')
        state['jobs'] = [j for j in state['jobs'] if j not in scoped]
        state = save(state)
    # A fresh prepare after this starts a new dated run folder.
    if any(j.get('project') == pid for j in scoped):
        store.change(pid, browser_run_name=None)
    return state


def _video_prompts_text(project, avatar_name):
    """One Veo 3.1 video prompt per take, in the five-block structure, per avatar."""
    from .rules import video_prompt
    takes = {t['id']: t for t in project['script']['takes']}
    lines = [f'# Prompts de vídeo · Veo 3.1 · {avatar_name}', f'# {project["title"]}', '',
             'Gere um clipe por bloco, com a imagem indicada da mesma pasta. A fala é a do',
             'roteiro final aprovado; não altere nem reordene.', '']
    n = 0
    for frame in _frames(project):
        hook = next((h for h in project.get('hooks', []) if h['id'] == frame.get('hook_id')), None)
        for tid in frame.get('takes', []):
            take = takes.get(tid)
            if not take:
                continue
            n += 1
            action = hook['action'] if hook else take['action']
            lines += [f'## V{n:02} · {tid} · imagem {frame["id"]}', '', video_prompt(take, action), '', '---', '']
    return '\n'.join(lines)


def standalone_prompt(frame, avatar_name):
    """One attachment only: this avatar's anchor. Generate a NEW image for this scene."""
    payload = {
        'task': 'Generate ONE photorealistic vertical 9:16 image now. Do not return a text prompt or a collage.',
        'avatar': avatar_name,
        'reference_policy': (
            f'The ONLY attached image is the original anchor photo of {avatar_name}. It is the '
            'authority for face, hair, wardrobe, room and lighting. The anchor already shows a '
            'holographic SOULMATE card on the table: put that same card model into her hands and '
            'keep it from this scene onward. Generate this scene as a NEW image; no previously '
            'generated image is attached or required. Keep the seven grouped scene-kit categories.'),
        'current_scene': frame['prompt'],
        'output': 'One image, portrait 9:16, natural skin texture, neutral daylight. No captions or overlays.'}
    return json.dumps(payload, ensure_ascii=False, indent=2)


def prompt_matches_current(job, frame, avatar_name):
    expected = standalone_prompt(frame, avatar_name)
    if expected == job['prompt']:
        return True
    try:
        return json.loads(expected) == json.loads(job['prompt'])
    except (TypeError, json.JSONDecodeError):
        return False


def _frames(project):
    return (project.get('imageset') or {}).get('frames', [])


def enqueue(ids, limit=None, only_avatar=None, only_frame=None):
    with LOCK, store.LOCK:
        state = load()
        additions = []
        for pid in dict.fromkeys(ids):
            p = store.get(pid)
            if p.get('busy'):
                raise ValueError('Aguarde ou pause a etapa em andamento antes de usar o Chrome.')
            frames = _frames(p)
            avatars = p.get('avatars', [])
            if not frames:
                raise ValueError('Monte o conjunto de imagens antes de preparar a fila.')
            if not avatars:
                raise ValueError('Suba ao menos uma âncora de avatar.')
            scenes = frames[:limit] if limit else frames
            if only_frame and not any(f['id'] == only_frame for f in frames):
                raise ValueError('Esta cena não existe mais no conjunto atual.')
            # One dated folder per production run; one sub-folder per avatar inside it.
            run_name = p.get('browser_run_name')
            if not run_name:
                run_name = f"{datetime.now().strftime('%Y-%m-%d')}_{slug(p['title'])}_{pid[:8]}"
                store.change(pid, browser_run_name=run_name)
            for avatar in avatars:
                if only_avatar and avatar['id'] != only_avatar:
                    continue
                anchor_path = store.artifact(pid, avatar['file'])
                anchor_hash = digest(anchor_path.read_bytes())
                folder = DOWNLOADS / 'Auraly Studio' / run_name / slug(avatar['name'])
                for index, frame in enumerate(scenes, 1):
                    fid = frame['id']
                    if only_frame and fid != only_frame:
                        continue
                    if not re.fullmatch(r'[A-Za-z0-9_-]{1,50}', fid):
                        raise ValueError('Identificador de imagem inválido.')
                    if any(j.get('project') == pid and j.get('avatar_id') == avatar['id'] and j.get('frame') == fid
                           and j['status'] != 'cancelled' for j in state['jobs'] + additions):
                        continue
                    prompt = standalone_prompt(frame, avatar['name'])
                    fingerprint = digest((pid + avatar['id'] + fid + prompt + anchor_hash).encode())
                    additions.append({'id': uuid.uuid4().hex, 'project': pid,
                        'avatar_id': avatar['id'], 'avatar': avatar['name'],
                        'avatar_key': f"{pid[:8]}:{avatar['id']}",
                        'frame': fid, 'title': frame.get('title', fid), 'index': index,
                        'prompt': prompt, 'anchor_rel': avatar['file'], 'anchor_sha256': anchor_hash,
                        'fingerprint': fingerprint, 'status': 'queued', 'created': store.now(),
                        'tab_id': None, 'conversation_url': None,
                        'destination_dir': str(folder), 'error': None})
        state['jobs'].extend(additions)
        save(state)
        return state


CANONICAL_JOB_FIELDS = {
    'production_id', 'pipeline', 'avatar_id', 'asset_id', 'prompt', 'prompt_sha256',
    'anchor_sha256', 'source_prompt_package_sha256', 'source_script_sha256',
    'hook_selection_sha256', 'canonical_state_path', 'canonical_asset_fingerprint', 'references',
}


def enqueue_materialized(specifications):
    """Add pre-resolved canonical jobs without touching legacy project/SQLite data.

    Phase A jobs are deliberately ``execution_ready=False``. They are durable contracts for the
    existing queue, but claim() will not hand them to the Chrome extension until Phase B adds
    multi-reference execution support.
    """
    with LOCK:
        state = load()
        additions = []
        existing = {job.get('canonical_asset_fingerprint') for job in state['jobs']
                    if job.get('job_kind') == 'canonical_materialized' and job['status'] != 'cancelled'}
        for spec in specifications:
            missing = CANONICAL_JOB_FIELDS - set(spec)
            if missing:
                raise ValueError(f'Job materializado sem campos obrigatórios: {sorted(missing)}')
            if spec['pipeline'] != 'auraly_soulmate':
                raise ValueError('Job materializado aceito somente para auraly_soulmate.')
            if not isinstance(spec['references'], list) or not spec['references']:
                raise ValueError('Job materializado exige referências estruturadas.')
            roles = [reference.get('role') for reference in spec['references']]
            if len(roles) != len(set(roles)):
                raise ValueError('Papéis de referência precisam ser únicos.')
            for reference in spec['references']:
                if not {'role', 'canonical_path', 'sha256'} <= set(reference):
                    raise ValueError('Referência materializada incompleta.')
                if reference['role'] not in {'avatar_anchor', 'shared_card_reference', 'parent_approved_result'}:
                    raise ValueError('Papel de referência materializada inválido.')
            # Reference requirements belong to the canonical asset contract, not to a
            # historical asset-id allowlist.  Legacy soulmate jobs still carry both
            # roles; newer packages may deliberately use only their avatar anchor.
            fingerprint = spec['canonical_asset_fingerprint']
            if fingerprint in existing:
                continue
            job = copy.deepcopy(spec)
            job['references'] = sorted(job['references'], key=lambda ref: ref['role'])
            job.update({
                'id': uuid.uuid4().hex, 'job_kind': 'canonical_materialized',
                'fingerprint': fingerprint, 'status': 'queued', 'created': store.now(),
                'updated': None, 'tab_id': None, 'conversation_url': None, 'error': None,
                'execution_ready': False, 'review_status': 'pending',
                'avatar': spec['avatar_id'],
                'avatar_key': f"{spec['production_id']}:{spec['avatar_id']}",
                'frame': spec['asset_id'], 'title': spec['asset_id'],
                'index': len(additions) + 1,
                'destination_dir': str(Path(spec['canonical_state_path']).parent / 'browser-results' / spec['avatar_id']),
            })
            additions.append(job)
            existing.add(fingerprint)
        state['jobs'].extend(additions)
        return save(state)


def _utcnow():
    return datetime.now(timezone.utc)


def _preflight_url(url):
    return isinstance(url, str) and re.fullmatch(r'https://chatgpt\.com/', url) is not None


def _invalidate_session_preflights(state, session_id):
    for row in state.get('preflights', []):
        if row.get('extension_session_id') != session_id and row.get('status') == 'valid':
            row.update(status='invalidated', invalidated_reason='A sessão da extensão foi substituída.')
    for row in state.get('preflight_requests', []):
        if row.get('extension_session_id') and row.get('extension_session_id') != session_id and row.get('status') == 'ready':
            row.update(status='expired', error='A sessão da extensão foi substituída.')
        elif row.get('extension_session_id') and row.get('extension_session_id') != session_id and row.get('status') == 'checking':
            # The prior worker may have been suspended after it marked the request as
            # checking. Re-queue the same durable request for the new session; this
            # never authorizes execution and never creates a duplicate request.
            row.update(status='requested', extension_session_id=None,
                       error='Preflight interrompido por reinício da extensão; aguardando a nova sessão.')


def request_preflight(jid, canonical_asset_fingerprint, requested_tab_id=None):
    """Ask the normal extension polling loop for readiness only; never enable or claim a job."""
    with LOCK:
        state = load(); job = next((j for j in state['jobs'] if j['id'] == jid), None)
        if not job or job.get('job_kind') != 'canonical_materialized':
            raise ValueError('Job materializado inexistente.')
        if job.get('execution_ready') or job.get('status') != 'queued':
            raise ValueError('O job não está disponível para preflight.')
        if job.get('canonical_asset_fingerprint') != canonical_asset_fingerprint:
            raise ValueError('Fingerprint mudou; pedido de preflight recusado.')
        current = next((r for r in state.get('preflight_requests', []) if r.get('job_id') == jid
                        and r.get('canonical_asset_fingerprint') == canonical_asset_fingerprint
                        and r.get('status') in {'requested', 'checking', 'ready'}), None)
        if current:
            return copy.deepcopy(current)
        for row in state.get('preflight_requests', []):
            if row.get('job_id') == jid and row.get('status') in {'requested', 'checking', 'ready'}:
                row.update(status='expired', error='Fingerprint substituído por novo pedido.')
        row = {'request_id': uuid.uuid4().hex, 'job_id': jid,
               'canonical_asset_fingerprint': canonical_asset_fingerprint, 'requested_at': store.now(),
               'requested_tab_id': requested_tab_id, 'status': 'requested', 'error': None,
               'extension_session_id': None, 'preflight_id': None}
        state.setdefault('preflight_requests', []).append(row); save(state)
        return copy.deepcopy(row)


def mark_preflight_checking(request_id, jid, canonical_asset_fingerprint, extension_session_id):
    with LOCK:
        state = load(); row = next((r for r in state.get('preflight_requests', []) if r.get('request_id') == request_id), None)
        job = next((j for j in state['jobs'] if j['id'] == jid), None)
        if not row or row.get('status') != 'requested' or not job:
            raise ValueError('Pedido de preflight não está disponível.')
        if row['job_id'] != jid or row['canonical_asset_fingerprint'] != canonical_asset_fingerprint or job.get('canonical_asset_fingerprint') != canonical_asset_fingerprint or job.get('execution_ready'):
            row.update(status='expired', error='Job ou fingerprint mudou.'); save(state)
            raise ValueError('Pedido de preflight expirado.')
        row.update(status='checking', checking_at=store.now(), extension_session_id=extension_session_id)
        save(state); return copy.deepcopy(row)


def fail_preflight_request(request_id, extension_session_id, error):
    with LOCK:
        state = load(); row = next((r for r in state.get('preflight_requests', []) if r.get('request_id') == request_id), None)
        if not row or row.get('status') != 'checking' or row.get('extension_session_id') != extension_session_id:
            raise ValueError('Pedido de preflight não pode receber falha desta sessão.')
        row.update(status='failed', failed_at=store.now(), error=str(error)[:1000]); return save(state)


def register_preflight(report):
    """Record an extension-proven, short-lived clean-tab receipt; never enable a job here."""
    required = {'job_id', 'canonical_asset_fingerprint', 'tab_id', 'window_id', 'url',
                'extension_session_id', 'nonce', 'content_script_ready', 'composer_ready',
                'upload_ready', 'draft_empty', 'generation_idle', 'modal_clear', 'conversation_clean'}
    missing = required - set(report)
    if missing:
        raise ValueError(f'Preflight incompleto: {sorted(missing)}')
    identity = {'job_id', 'canonical_asset_fingerprint', 'tab_id', 'window_id', 'url', 'extension_session_id', 'nonce'}
    if not _preflight_url(report['url']):
        raise ValueError('A URL do preflight não é uma conversa nova permitida do ChatGPT.')
    if not all(report[key] is True for key in required - identity):
        raise ValueError('A aba não está limpa e pronta para uma submissão segura.')
    with LOCK:
        state = load(); job = next((j for j in state['jobs'] if j['id'] == report['job_id']), None)
        if not job or job.get('job_kind') != 'canonical_materialized':
            raise ValueError('Job materializado inexistente.')
        if job.get('execution_ready') or job.get('status') != 'queued':
            raise ValueError('O job não está disponível para preflight.')
        if job.get('canonical_asset_fingerprint') != report['canonical_asset_fingerprint']:
            raise ValueError('Fingerprint mudou; preflight recusado.')
        _invalidate_session_preflights(state, report['extension_session_id'])
        now = _utcnow(); expiry = now + timedelta(seconds=PREFLIGHT_TTL_SECONDS)
        row = {key: report[key] for key in required}
        row.update(preflight_id=uuid.uuid4().hex, created_at=now.isoformat(), expires_at=expiry.isoformat(), status='valid')
        state.setdefault('preflights', []).append(row)
        state['extension_session_id'] = report['extension_session_id']
        for request in state.get('preflight_requests', []):
            if request.get('job_id') == report['job_id'] and request.get('canonical_asset_fingerprint') == report['canonical_asset_fingerprint'] and request.get('status') == 'checking' and request.get('extension_session_id') == report['extension_session_id']:
                request.update(status='ready', ready_at=store.now(), preflight_id=row['preflight_id'], error=None)
        save(state)
        return copy.deepcopy(row)


def activate_materialized(jid, canonical_asset_fingerprint, preflight_id, revalidation):
    """Enable exactly one job only after the identical tab freshly proves readiness."""
    with LOCK:
        state = load()
        job = next((item for item in state['jobs'] if item['id'] == jid), None)
        if not job or job.get('job_kind') != 'canonical_materialized':
            raise ValueError('Job materializado inexistente.')
        if job.get('canonical_asset_fingerprint') != canonical_asset_fingerprint:
            raise ValueError('Fingerprint mudou desde a materialização; ativação recusada.')
        if job['status'] != 'queued' or job.get('execution_ready'):
            raise ValueError('Somente um job materializado novo e não ativado pode ser habilitado.')
        if _job_in_preflight_only_batch(state, jid):
            raise ValueError('Job pertence a um batch preflight_only (allow_activation=False); ativação recusada.')
        receipt = next((p for p in state.get('preflights', []) if p.get('preflight_id') == preflight_id), None)
        if not receipt or receipt.get('status') != 'valid':
            raise ValueError('Recibo de preflight inexistente ou não utilizável.')
        if _utcnow() >= datetime.fromisoformat(receipt['expires_at']):
            receipt['status'] = 'expired'; save(state)
            raise ValueError('Recibo de preflight expirado.')
        bound = ('job_id', 'canonical_asset_fingerprint', 'tab_id', 'window_id', 'url', 'extension_session_id')
        if any(receipt.get(key) != revalidation.get(key) for key in bound):
            receipt.update(status='invalidated', invalidated_reason='A aba, sessão ou identidade mudou.'); save(state)
            raise ValueError('A revalidação não corresponde ao preflight original.')
        readiness = ('content_script_ready', 'composer_ready', 'upload_ready', 'draft_empty', 'generation_idle', 'modal_clear', 'conversation_clean')
        if not _preflight_url(revalidation.get('url')) or not all(revalidation.get(key) is True for key in readiness):
            receipt.update(status='invalidated', invalidated_reason='A aba deixou de estar limpa ou pronta.'); save(state)
            raise ValueError('A revalidação da aba falhou; ativação recusada.')
        if state.get('extension_session_id') != receipt['extension_session_id']:
            receipt.update(status='invalidated', invalidated_reason='A extensão foi reiniciada.'); save(state)
            raise ValueError('A sessão da extensão mudou; ativação recusada.')
        canonical_path = Path(job['canonical_state_path'])
        from . import pipeline_state
        canonical = pipeline_state.load(canonical_path)
        avatar = canonical['avatars'].get(job['avatar_id'], {})
        asset = avatar.get('assets', {}).get(job['asset_id'])
        if not asset or asset.get('canonical_asset_fingerprint') != canonical_asset_fingerprint:
            raise ValueError('Estado canônico não reconhece o fingerprint atual do asset.')
        if asset.get('status') != 'queued' or asset.get('queue_job_id') != jid:
            raise ValueError('Estado canônico e fila não concordam sobre o job a ativar.')
        for ref in job['references']:
            path = Path(ref['canonical_path'])
            if not path.is_file() or digest(path.read_bytes()) != ref['sha256']:
                raise ValueError(f"Referência {ref['role']} ausente ou divergente; ativação recusada.")
        receipt.update(status='consumed', consumed_at=store.now())
        job.update(execution_ready=True, activated_at=store.now(),
                   activation_fingerprint=canonical_asset_fingerprint,
                   activation_preflight_id=preflight_id,
                   tab_id=receipt['tab_id'], window_id=receipt['window_id'],
                   preflight_url=receipt['url'],
                   authorized_extension_session_id=receipt['extension_session_id'],
                   authorized_target={'tab_id': receipt['tab_id'], 'window_id': receipt['window_id'],
                                      'url': receipt['url'], 'extension_session_id': receipt['extension_session_id'],
                                      'preflight_id': preflight_id})
        return save(state)


BATCH_STATUSES = ('authorized', 'preflighting', 'executing', 'awaiting_results', 'partially_failed', 'completed')


def authorize_batch(production_id, pipeline, avatar_id, asset_fingerprints,
                    allow_activation=True):
    """Explicitly authorize a set of assets for execution now.

    ``asset_fingerprints`` is a dict mapping asset_id to the caller-known
    canonical_asset_fingerprint. Eligibility (``eligible_for_execution=True``)
    is a precondition but not sufficient: the caller must explicitly name the
    assets and their fingerprints. This prevents implicit "all queued jobs run"
    semantics.

    ``allow_activation=False`` creates a **preflight_only** batch: preflights
    are requested and tabs are created so readiness can be verified, but
    ``activate_materialized()`` will refuse to enable any job from this batch
    and ``autoActivatePreflights()`` in the extension will skip them entirely.
    Use this for benchmarks and dry-runs. The batch cannot be promoted to
    execute mode; create a new batch with ``allow_activation=True`` to execute.
    """
    if pipeline != 'auraly_soulmate':
        raise ValueError('Batch de autorização aceito somente para auraly_soulmate.')
    if not asset_fingerprints:
        raise ValueError('Batch vazio; informe ao menos um asset.')
    with LOCK:
        state = load()
        jobs_by_asset = {
            j['asset_id']: j for j in state['jobs']
            if j.get('production_id') == production_id
            and j.get('avatar_id') == avatar_id
            and j.get('job_kind') == 'canonical_materialized'
            and j['status'] != 'cancelled'
        }
        authorized_assets = []
        for asset_id, expected_fp in asset_fingerprints.items():
            job = jobs_by_asset.get(asset_id)
            if not job:
                raise ValueError(f'Asset {asset_id} não encontrado na fila.')
            if job.get('canonical_asset_fingerprint') != expected_fp:
                raise ValueError(
                    f'Fingerprint de {asset_id} divergiu; reautorize com os fingerprints atuais.')
            authorized_assets.append({
                'asset_id': asset_id,
                'job_id': job['id'],
                'canonical_asset_fingerprint': expected_fp,
            })
        batch = {
            'batch_id': uuid.uuid4().hex,
            'production_id': production_id,
            'pipeline': pipeline,
            'avatar_id': avatar_id,
            'authorized_at': store.now(),
            'status': 'authorized',
            'allow_activation': bool(allow_activation),
            'assets': authorized_assets,
        }
        state.setdefault('batch_authorizations', []).append(batch)
        save(state)
        return copy.deepcopy(batch)


def _job_in_preflight_only_batch(state, job_id):
    """Return True if this job belongs to any batch with allow_activation=False."""
    for batch in state.get('batch_authorizations', []):
        if not batch.get('allow_activation', True):
            if any(a['job_id'] == job_id for a in batch.get('assets', [])):
                return True
    return False


def dispatch_batch(batch_id):
    """Fire preflight requests for all fingerprint-valid assets in the batch.

    Returns immediately — the extension handles tab creation and readiness via
    its polling loop. Each asset is independent: a fingerprint divergence on
    K02 does not block K01/K03/K04. Idempotent: won't duplicate active preflight
    requests.
    """
    with LOCK:
        state = load()
        batch = next((b for b in state.get('batch_authorizations', [])
                      if b['batch_id'] == batch_id), None)
        if not batch:
            raise ValueError('Batch de autorização não encontrado.')
        if batch['status'] not in {'authorized', 'preflighting'}:
            raise ValueError(f'Batch não está em estado de disparo: {batch["status"]}.')
        allow_activation = batch.get('allow_activation', True)
        dispatched, skipped = [], []
        for asset in batch['assets']:
            job = next((j for j in state['jobs'] if j['id'] == asset['job_id']), None)
            if not job:
                skipped.append({'asset_id': asset['asset_id'], 'reason': 'job não encontrado'})
                continue
            if job.get('canonical_asset_fingerprint') != asset['canonical_asset_fingerprint']:
                skipped.append({'asset_id': asset['asset_id'], 'reason': 'fingerprint divergiu'})
                continue
            if job.get('execution_ready') or job['status'] not in {'queued'}:
                skipped.append({'asset_id': asset['asset_id'],
                                'reason': f'status atual: {job["status"]}'})
                continue
            existing = next(
                (r for r in state.get('preflight_requests', [])
                 if r.get('job_id') == asset['job_id']
                 and r.get('canonical_asset_fingerprint') == asset['canonical_asset_fingerprint']
                 and r.get('status') in {'requested', 'checking', 'ready'}),
                None)
            if existing:
                dispatched.append({'asset_id': asset['asset_id'],
                                   'request_id': existing['request_id'], 'reused': True})
                continue
            row = {
                'request_id': uuid.uuid4().hex, 'job_id': asset['job_id'],
                'canonical_asset_fingerprint': asset['canonical_asset_fingerprint'],
                'requested_at': store.now(), 'requested_tab_id': None,
                'status': 'requested', 'error': None,
                'extension_session_id': None, 'preflight_id': None,
                'batch_id': batch_id,
                'allow_activation': allow_activation,
            }
            state.setdefault('preflight_requests', []).append(row)
            dispatched.append({'asset_id': asset['asset_id'],
                               'request_id': row['request_id'], 'reused': False})
        batch['status'] = 'preflighting'
        save(state)
        return {'batch_id': batch_id, 'dispatched': dispatched, 'skipped': skipped}


def get_batch(batch_id):
    state = load()
    batch = next((b for b in state.get('batch_authorizations', [])
                  if b['batch_id'] == batch_id), None)
    if not batch:
        raise ValueError('Batch de autorização não encontrado.')
    return copy.deepcopy(batch)


def control(running, concurrency=2):
    with LOCK:
        state = load()
        state.update(running=running, concurrency=concurrency)
        return save(state)


def heartbeat(extension_session_id=None, agent_protocol_version=None, agent_capabilities=None):
    with LOCK:
        state = load()
        if extension_session_id:
            _invalidate_session_preflights(state, extension_session_id)
            state['extension_session_id'] = extension_session_id
        state['connected_at'] = store.now()
        if agent_protocol_version is not None:
            state['agent_protocol_version'] = agent_protocol_version
        if agent_capabilities is not None:
            state['agent_capabilities'] = agent_capabilities
        return save(state)


def claim():
    with LOCK, store.LOCK:
        state = load()
        active = [j for j in state['jobs'] if j['status'] in ACTIVE]
        if not state['running'] or len(active) >= state['concurrency']:
            return None
        blocked = {j.get('avatar_key') for j in state['jobs'] if j['status'] in ACTIVE | {'attention'}}
        for job in state['jobs']:
            if job.get('job_kind') == 'canonical_materialized' and not job.get('execution_ready'):
                continue
            if _job_in_preflight_only_batch(state, job['id']):
                continue
            if job.get('job_kind') == 'canonical_materialized' and not all(job.get(key) is not None for key in
                    ('activation_preflight_id', 'tab_id', 'window_id', 'preflight_url', 'authorized_extension_session_id')):
                # A malformed activated job is never executable; preserve it for diagnosis.
                job.update(status='attention', error='Alvo autorizado de execução ausente; novo preflight necessário.')
                save(state)
                continue
            if job['status'] != 'queued' or job['avatar_key'] in blocked:
                continue
            if job.get('job_kind') != 'canonical_materialized' and store.get(job['project']).get('busy'):
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
        if job.get('job_kind') == 'canonical_materialized' and not job.get('execution_ready'):
            raise ValueError('Job materializado não está habilitado para execução.')
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


def update(jid, status, tab_id=None, conversation_url=None, error=None):
    with LOCK:
        state = load()
        job = next((j for j in state['jobs'] if j['id'] == jid), None)
        if not job:
            raise ValueError('Tarefa inexistente.')
        if job.get('job_kind') == 'canonical_materialized' and not job.get('execution_ready'):
            raise ValueError('Job materializado não está habilitado para execução.')
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
    path = store.artifact(job['project'], job['anchor_rel'])
    if digest(path.read_bytes()) != job['anchor_sha256']:
        raise ValueError('Âncora alterada depois da criação da fila.')
    return path


def reference(jid, role):
    """Resolve one materialized reference by semantic role and verify its immutable hash."""
    job = get_job(jid)
    if not job or job.get('job_kind') != 'canonical_materialized':
        raise ValueError('Referência materializada inexistente.')
    if not job.get('execution_ready'):
        raise ValueError('Job materializado não está habilitado para execução.')
    matches = [ref for ref in job.get('references', []) if ref.get('role') == role]
    if len(matches) != 1:
        raise ValueError('Referência obrigatória ausente ou ambígua.')
    path = Path(matches[0]['canonical_path'])
    if not path.is_file():
        raise ValueError('Referência obrigatória inacessível.')
    if digest(path.read_bytes()) != matches[0]['sha256']:
        raise ValueError('Referência obrigatória alterada depois da criação da fila.')
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
        if job.get('job_kind') == 'canonical_materialized' and not job.get('execution_ready'):
            raise ValueError('Job materializado não está habilitado para execução.')
        sha = digest(raw)
        if job['status'] == 'done':
            if job['image_sha256'] != sha:
                raise ValueError('Resultado diferente para uma tarefa já concluída.')
            return job
        if job['status'] not in {'generating', 'receiving', 'attention'}:
            raise ValueError('Esta tarefa ainda não foi enviada.')
        dest = Path(job['destination_dir'])
        dest.mkdir(parents=True, exist_ok=True)
        name = f"{job['avatar_id']}_{job['index']:03d}_{job['frame']}_{job['id'][:8]}{ext}"
        path = dest / name
        # A deterministic name makes an interrupted receipt safe to repeat.
        if path.exists() and digest(path.read_bytes()) != sha:
            raise ValueError('Arquivo de saída já existe com outro conteúdo.')
        temp = path.with_suffix(ext + '.part')
        temp.write_bytes(raw)
        temp.replace(path)
        (dest / (Path(name).stem + '_prompt.json')).write_text(job['prompt'], encoding='utf-8')
        if job.get('job_kind') == 'canonical_materialized':
            local = path
        else:
            local = store.folder(job['project']) / 'browser-images' / name
            local.parent.mkdir(exist_ok=True)
            local.write_bytes(raw)
        job.update(status='done', file=str(path), local_file=str(local), image_sha256=sha,
                   dimensions=list(dimensions), finished=store.now(), error=None)
        save(state)
        store.write_json(dest / 'manifest.json', [j for j in state['jobs'] if j['destination_dir'] == str(dest)])
        if job.get('job_kind') != 'canonical_materialized':
            project = store.get(job['project'])
            if project.get('script') and project.get('imageset'):
                (dest / 'PROMPTS_VIDEO_VEO.txt').write_text(
                    _video_prompts_text(project, job['avatar']), encoding='utf-8')
            store.event(job['project'], f"ChatGPT Chrome: {job['avatar']} · {job['frame']} salvo em Downloads. Revisão visual pendente.")
        return job


def result_file(jid):
    job = get_job(jid)
    if not job or job['status'] != 'done':
        raise ValueError('Esta tarefa ainda não tem imagem salva.')
    if job.get('job_kind') == 'canonical_materialized':
        path = Path(job['local_file'])
        if not path.is_file():
            raise ValueError('Resultado materializado não encontrado.')
    else:
        path = store.artifact(job['project'], str(Path(job['local_file']).relative_to(store.folder(job['project']))))
    if digest(path.read_bytes()) != job['image_sha256']:
        raise ValueError('A imagem salva foi alterada. Revise uma nova tentativa.')
    return path


def current_scene(job, project):
    frame = next((f for f in _frames(project) if f['id'] == job['frame']), None)
    if not frame or not prompt_matches_current(job, frame, job['avatar']):
        raise ValueError('O conjunto de imagens mudou desde a geração. Prepare uma nova tentativa para esta cena.')
    anchor(job['id'])
    return frame


def review(jid, decision, comment=''):
    with LOCK, store.LOCK:
        state = load()
        job = next((j for j in state['jobs'] if j['id'] == jid), None)
        if not job or job['status'] != 'done':
            raise ValueError('Somente imagens salvas podem ser revisadas.')
        materialized = job.get('job_kind') == 'canonical_materialized'
        if materialized and not job.get('execution_ready'):
            raise ValueError('Job materializado não está habilitado para execução.')
        project = None if materialized else store.get(job['project'])
        if decision == 'approve':
            if materialized:
                for ref in job.get('references', []):
                    reference(jid, ref['role'])
            else:
                current_scene(job, project)
            result_file(jid)
            job.update(review_status='approved', reviewed_at=store.now(), review_comment=comment)
        elif decision == 'retry':
            if materialized:
                job.update(status='cancelled', review_status='rejected', reviewed_at=store.now(), review_comment=comment)
                save(state)
                fresh = {k: v for k, v in job.items() if k not in {
                    'claimed_at', 'updated', 'file', 'local_file', 'dimensions', 'finished', 'image_sha256'}}
                fresh.update(id=uuid.uuid4().hex, status='queued', tab_id=None, conversation_url=None,
                             error=None, created=store.now(), retry_of=jid)
                state['jobs'].insert(state['jobs'].index(job) + 1, fresh)
                return save(state)
            frame = next((f for f in _frames(project) if f['id'] == job['frame']), None)
            if project.get('busy') or not frame:
                raise ValueError('Aguarde a etapa ou verifique se a cena ainda existe no conjunto.')
            store.artifact(job['project'], job['anchor_rel']).read_bytes()
            job.update(status='cancelled', review_status='rejected', reviewed_at=store.now(), review_comment=comment)
            save(state)
            # Rebuild only this avatar's scene from the current image set; the old file stays on disk.
            state = enqueue([job['project']], only_avatar=job['avatar_id'], only_frame=job['frame'])
            fresh = next((j for j in state['jobs'] if j['project'] == job['project']
                          and j['avatar_id'] == job['avatar_id'] and j['frame'] == job['frame']
                          and j['status'] == 'queued'), None)
            if fresh:
                fresh['retry_of'] = jid
        else:
            raise ValueError('Decisão inválida.')
        return save(state)


def _avatar(project, aid):
    avatar = next((a for a in project.get('avatars', []) if a['id'] == aid), None)
    if not avatar:
        raise ValueError('Avatar não encontrado neste projeto.')
    return avatar


def export_package(pid, aid):
    """Export one avatar's approved Chrome results, with real image format and exact speech."""
    from .rules import validate_imageset, validate_script, video_prompt
    with LOCK, store.LOCK:
        project = store.get(pid)
        avatar = _avatar(project, aid)
        validate_script(project['script'])
        validate_imageset(project['imageset'], project['selected'], project['script'])
        frames = _frames(project)
        jobs = [j for j in load()['jobs'] if j.get('project') == pid and j['avatar_id'] == aid
                and j['status'] != 'cancelled']
        selected = []
        for frame in frames:
            matches = [j for j in jobs if j['frame'] == frame['id']]
            if len(matches) != 1 or matches[0]['status'] != 'done' or matches[0].get('review_status') != 'approved':
                raise ValueError(f"{avatar['name']} · {frame['id']}: gere e aprove a imagem antes de exportar o pacote.")
            job = matches[0]
            current_scene(job, project)
            selected.append((frame, job, result_file(job['id'])))
        takes = {t['id']: t for t in project['script']['takes']}
        clips, image_manifest = [], []
        script_lines = [f"# {project['title']} · {avatar['name']}", '', '## Roteiro cena a cena', '']
        for take in takes.values():
            script_lines.extend([f"### {take['id']} · {take['beat']} · Setup {take['setup']}",
                                 '', take['speech'], '', take['translation'], ''])
        script_lines.extend(['## Roteiro só-fala', '', '\n\n'.join(t['speech'] for t in takes.values())])
        prompts = [f"# Prompts de produção · {avatar['name']}", '',
                   'Cada imagem foi gerada com a âncora original. A carta SOULMATE já está na mesa da âncora.', '',
                   '## Continuidade', '', project['script'].get('continuity', ''), '']
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
        manifest = {'project': pid, 'title': project['title'], 'avatar': avatar['name'],
                    'avatar_id': aid, 'source': 'chatgpt-chrome', 'model': None,
                    'exported_at': store.now(), 'images': image_manifest, 'clips': clips,
                    'selected_hooks': project['selected']}
        target = store.folder(pid) / f"auraly-chrome-{slug(avatar['name'])}.zip"
        temp = target.with_suffix('.zip.tmp')
        with zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED) as archive:
            for frame, job, path in selected:
                archive.write(path, f"imagens/{frame['id']}{path.suffix.lower()}")
                archive.writestr(f"prompts/{frame['id']}.json", job['prompt'])
            archive.write(store.artifact(pid, avatar['file']), 'ancora/anchor.png')
            archive.writestr('ROTEIRO.md', '\n'.join(script_lines))
            archive.writestr('PROMPTS_PRODUCAO.md', '\n'.join(prompts))
            archive.writestr('PROMPTS_VIDEO_VEO.txt', _video_prompts_text(project, avatar['name']))
            archive.writestr('manifest.json', json.dumps(manifest, ensure_ascii=False, indent=2))
            analysis = store.folder(pid) / 'ANALISE.json'
            if analysis.is_file():
                archive.write(analysis, 'ANALISE.json')
        temp.replace(target)
        return target
