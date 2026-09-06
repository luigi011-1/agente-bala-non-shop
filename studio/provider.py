"""Text-only provider: OpenAI Responses with a Google Gemini fallback on typed 429.

Image generation was removed: every image is now made by the operator in their own
ChatGPT browser session (see browser_queue.py and the chrome-extension).
"""
import base64
import json
import math
import mimetypes
import os
import random
import re
import threading
import time
from pathlib import Path

import httpx

from . import credentials
from . import storage as store
from .rules import POLICY

_key = os.environ.get('OPENAI_API_KEY', '')
_gemini_key = os.environ.get('GEMINI_API_KEY', '')
DEFAULT_MODEL = 'gpt-6-astra'
DEFAULT_GEMINI_MODEL = 'gemini-3.5-flash'
DEFAULT_EFFORT = 'medium'
_model = os.environ.get('AURALY_TEXT_MODEL', DEFAULT_MODEL)
_effort = DEFAULT_EFFORT
_verification = None
_text_provider = 'auto'
_lock = threading.Lock()

# 429 may be a billing wall: switch provider once, never blindly retry it.
TRANSIENT_STATUS = (408, 429, 500, 502, 503, 504, 520, 522, 524)


def configure(key=None, model=None, effort=None, gemini_key=None, text_provider=None):
    global _key, _model, _effort, _verification, _gemini_key, _text_provider
    with _lock:
        if effort and effort not in ['low', 'medium', 'high', 'xhigh', 'max']:
            raise ValueError('Nível de raciocínio inválido.')
        if key is not None:
            _key = key.strip()
        if gemini_key is not None:
            _gemini_key = gemini_key.strip()
        if model:
            _model = model.strip()
        if effort:
            _effort = effort
        if text_provider is not None:
            if text_provider not in ('auto', 'openai', 'gemini'):
                raise ValueError('Provedor de texto inválido.')
            _text_provider = text_provider
        _verification = None


def load_preferences():
    path = store.DATA / 'preferences.json'
    if path.is_file():
        value = json.loads(path.read_text(encoding='utf-8-sig'))
        secrets = json.loads(credentials.unprotect(value['protected_credentials'])) if value.get('protected_credentials') else value
        configure(key=secrets.get('openai_key'),
                  gemini_key=secrets.get('gemini_key'),
                  text_provider=value.get('text_provider', 'auto'),
                  model=value.get('text_model', DEFAULT_MODEL),
                  effort=value.get('reasoning_effort', DEFAULT_EFFORT))
        if any(k in value for k in ('openai_key', 'gemini_key')):
            save_preferences()


def save_preferences():
    store.write_json(store.DATA / 'preferences.json',
                     {'text_model': _model, 'reasoning_effort': _effort,
                      'text_provider': _text_provider,
                      'protected_credentials': credentials.protect(json.dumps({
                          'openai_key': _key, 'gemini_key': _gemini_key}))})


def settings():
    return {'configured': bool(_key), 'gemini_configured': bool(_gemini_key),
            'text_model': _model, 'reasoning_effort': _effort, 'verification': _verification,
            'gemini_model': DEFAULT_GEMINI_MODEL, 'text_provider': _text_provider,
            'key_storage': 'Protegidas por Windows DPAPI, vinculadas ao usuário atual.'}


def safe_error(value):
    text = str(value)
    if _key:
        text = text.replace(_key, '[CHAVE OCULTA]')
    if _gemini_key:
        text = text.replace(_gemini_key, '[CHAVE OCULTA]')
    return re.sub(r'(sk-|AIza)[A-Za-z0-9_\-]+', '[CHAVE OCULTA]', text)[:1200]


def verify_access():
    """Read-only catalog check, not a generation/vision/credit test."""
    global _verification
    require_key()
    with _lock:
        key, model = _key, _model
    try:
        with httpx.Client(timeout=20) as client:
            response = client.get('https://api.openai.com/v1/models/' + model,
                                  headers={'Authorization': f'Bearer {key}'})
            if response.is_error:
                raise ValueError(f'Não foi possível consultar {model}: HTTP {response.status_code}. '
                                 'Verifique a chave e as permissões do projeto.')
            if response.json().get('id') != model:
                raise ValueError('A API retornou um identificador de modelo inesperado.')
    except httpx.TransportError:
        raise ValueError('Não foi possível conectar à OpenAI para verificar o acesso.') from None
    with _lock:
        if key != _key or model != _model:
            raise ValueError('Conexão alterada durante a verificação. Verifique novamente.')
        _verification = {'checked_at': store.now(), 'model': model, 'kind': 'catalog_only',
                         'note': 'Modelo consultável. Geração, saldo e qualidade ainda não testados.'}
    return _verification


def check_call_allowed(project, route='responses'):
    if project.get('pause_requested'):
        raise ValueError('Etapa pausada antes da próxima chamada. Resultados recebidos foram preservados.')
    limit = project.get('call_limits', {}).get('text', 200)
    used = len(project.get('calls', []))
    if used >= limit:
        raise ValueError(f'Limite de chamadas de texto atingido ({used}/{limit}). Ajuste o limite para continuar.')


def require_key():
    if not _key:
        raise ValueError('Configure sua chave OpenAI em Conexão para executar esta etapa.')


def require_think_key():
    available = {'openai': _key, 'gemini': _gemini_key}
    if not (any(available.values()) if _text_provider == 'auto' else available[_text_provider]):
        raise ValueError('Configure a chave do provedor de texto selecionado em Conexão.')


class ProviderError(ValueError):
    def __init__(self, message, status, retry_after=None):
        super().__init__(message)
        self.status = status
        try:
            self.retry_after = max(0, float(retry_after))
        except (ValueError, TypeError):
            self.retry_after = 0


def request(pid, route, **kwargs):
    require_key()
    payload = kwargs.get('json', kwargs.get('data', {}))
    call = {'route': route, 'started': store.now(), 'status': 'sent',
            'model': payload.get('model'), 'reasoning_effort': payload.get('reasoning', {}).get('effort')}
    with store.LOCK:
        p = store.get(pid)
        check_call_allowed(p, route)
        p['calls'].append(call)
        index = len(p['calls']) - 1
        store.save(p)
    try:
        with httpx.Client(timeout=httpx.Timeout(600, connect=20)) as client:
            r = client.post('https://api.openai.com/v1/' + route,
                            headers={'Authorization': f'Bearer {_key}'}, **kwargs)
        if r.is_error:
            call['http_status'] = r.status_code
            try:
                err = r.json().get('error', {})
                detail = str(err.get('message', 'Falha no provedor.'))
                call['error_code'] = safe_error(err.get('code', ''))
            except ValueError:
                detail = 'Falha no provedor.'
            call['error_detail'] = safe_error(detail)
            raise ProviderError(safe_error(f'OpenAI HTTP {r.status_code}: {detail[:800]}'), r.status_code, retry_after=r.headers.get('retry-after'))
        body = r.json()
        call.update(status='completed', request_id=r.headers.get('x-request-id'),
                    usage=body.get('usage'), finished=store.now())
        return body
    except Exception as exc:
        call.update(status='uncertain' if isinstance(exc, httpx.TransportError) else 'failed')
        if isinstance(exc, httpx.TransportError):
            raise ValueError('Conexão interrompida. Confira antes de tentar novamente.') from None
        raise
    finally:
        with store.LOCK:
            p = store.get(pid)
            p['calls'][index] = call
            store.save(p)


def data_url(path):
    mime = mimetypes.guess_type(str(path))[0] or 'image/png'
    return f'data:{mime};base64,' + base64.b64encode(Path(path).read_bytes()).decode()


def _openai_think(pid, instruction, data, images=(), context=False):
    inputs = [{'type': 'input_text', 'text': 'Analyze the following input data and return the result as a valid JSON object.\n' +
               json.dumps(data, ensure_ascii=False)}]
    for path in images:
        inputs += [{'type': 'input_text', 'text': f'FRAME/REFERENCE: {Path(path).name}'},
                   {'type': 'input_image', 'image_url': data_url(path), 'detail': 'high'}]
    docs = (store.folder(pid) / 'sources.md').read_text(encoding='utf-8') if context else ''
    body = request(pid, 'responses', json={
        'model': _model, 'store': False, 'reasoning': {'effort': _effort},
        'instructions': POLICY + '\n' + instruction + '\nREFERENCE DOCUMENTS:\n' + docs,
        'input': [{'role': 'user', 'content': inputs}],
        'text': {'format': {'type': 'json_object'}}, 'max_output_tokens': 14000})
    if body.get('status') != 'completed':
        raise ValueError('Resposta de análise incompleta. Nenhuma aprovação foi registrada.')
    text = ''.join(c.get('text', '') for o in body.get('output', [])
                   for c in o.get('content', []) if c.get('type') == 'output_text')
    try:
        return json.loads(text)
    except ValueError:
        raise ValueError('O modelo não retornou JSON válido; etapa preservada para revisão.') from None


def _gemini_think(pid, instruction, data, images=(), context=False):
    with _lock:
        key = _gemini_key
    if not key:
        raise ValueError('Configure sua chave Gemini em Conexão.')

    parts = [{'text': 'Analyze the following input data and return the result as a valid json object.\n' +
              json.dumps(data, ensure_ascii=False)}]
    for path in images:
        mime = mimetypes.guess_type(str(path))[0] or 'image/png'
        b64 = base64.b64encode(Path(path).read_bytes()).decode()
        parts.append({'text': f'FRAME/REFERENCE: {Path(path).name}'})
        parts.append({'inline_data': {'mime_type': mime, 'data': b64}})

    docs = (store.folder(pid) / 'sources.md').read_text(encoding='utf-8') if context else ''
    system_text = POLICY + '\n' + instruction + '\nREFERENCE DOCUMENTS:\n' + docs

    call = {'route': 'gemini/generate', 'started': store.now(), 'status': 'sent',
            'model': DEFAULT_GEMINI_MODEL}
    with store.LOCK:
        p = store.get(pid)
        check_call_allowed(p, 'gemini/generate')
        p['calls'].append(call)
        index = len(p['calls']) - 1
        store.save(p)

    try:
        url = (f'https://generativelanguage.googleapis.com/v1beta/models/'
               f'{DEFAULT_GEMINI_MODEL}:generateContent?key={key}')
        payload = {
            'system_instruction': {'parts': [{'text': system_text +
                                              '\n\nIMPORTANT: Return ONLY a valid JSON object. No markdown fences, no explanation.'}]},
            'contents': [{'role': 'user', 'parts': parts}],
            'generationConfig': {
                'responseMimeType': 'application/json',
                'maxOutputTokens': 14000,
                'temperature': 0.7,
            },
        }
        with httpx.Client(timeout=httpx.Timeout(600, connect=20)) as client:
            r = client.post(url, json=payload)

        if r.is_error:
            try:
                err = r.json().get('error', {})
                detail = str(err.get('message', 'Falha no provedor.'))
            except ValueError:
                detail = 'Falha no provedor.'
            call.update(http_status=r.status_code, error_detail=safe_error(detail))
            raise ProviderError(safe_error(f'Gemini HTTP {r.status_code}: {detail[:800]}'), r.status_code, retry_after=r.headers.get('retry-after'))

        body = r.json()
        usage = body.get('usageMetadata', {})
        call.update(status='completed', finished=store.now(),
                    usage={'prompt_tokens': usage.get('promptTokenCount'),
                           'completion_tokens': usage.get('candidatesTokenCount'),
                           'total_tokens': usage.get('totalTokenCount')})

        candidates = body.get('candidates', [])
        if not candidates:
            raise ValueError('Gemini não retornou resposta; etapa preservada para revisão.')
        text = ''.join(p.get('text', '') for p in candidates[0].get('content', {}).get('parts', []))
        text = text.strip()
        if text.startswith('```'):
            text = re.sub(r'^```(?:json)?\s*', '', text)
            text = re.sub(r'\s*```\s*$', '', text)
        try:
            return json.loads(text)
        except ValueError:
            raise ValueError('Gemini não retornou JSON válido; etapa preservada para revisão.') from None

    except Exception as exc:
        call.update(status='uncertain' if isinstance(exc, httpx.TransportError) else 'failed')
        if not isinstance(exc, ValueError):
            raise ValueError(safe_error(exc)) from None
        if call['status'] != 'completed':
            call.update(status='failed')
        raise
    finally:
        with store.LOCK:
            p = store.get(pid)
            p['calls'][index] = call
            store.save(p)


def retry_wait(pid, seconds, provider_name, attempt):
    """Visible, interruptible backoff. Does not count as an API request."""
    if seconds > 120:
        raise ValueError('Provedor pediu espera superior a 120s. Checkpoints salvos; retome mais tarde.')
    store.change(pid, waiting_provider=provider_name, retry_attempt=attempt, retry_wait_seconds=seconds)
    store.event(pid, f'{provider_name} temporariamente indisponível. Nova tentativa {attempt}/3 em {seconds:.0f}s; resultados salvos.')
    try:
        for _ in range(max(1, math.ceil(seconds))):
            if store.get(pid).get('pause_requested'):
                raise ValueError('Pausado durante a espera. Nenhuma nova chamada enviada.')
            time.sleep(1)
    finally:
        store.change(pid, waiting_provider=None)


def think(pid, instruction, data, images=(), context=False):
    require_think_key()
    available = {'openai': _key, 'gemini': _gemini_key}
    order = [k for k, key in available.items() if key] if _text_provider == 'auto' else [_text_provider]
    # Persist the successful fallback for this project; explicit selection overrides it.
    sticky = store.get(pid).get('active_text_provider')
    if _text_provider == 'auto' and sticky in order:
        order = order[order.index(sticky):]
    functions = {'openai': _openai_think, 'gemini': _gemini_think}
    last = None
    for position, name in enumerate(order):
        store.change(pid, active_text_provider=name)
        for attempt in range(3):
            check_call_allowed(store.get(pid), 'responses')
            try:
                return functions[name](pid, instruction, data, images, context)
            except ProviderError as exc:
                last = exc
                if exc.status not in TRANSIENT_STATUS:
                    raise
                if exc.status == 429 or attempt == 2:
                    break
                retry_wait(pid, max(exc.retry_after, 10 * 2 ** attempt + random.uniform(0, 3)), name, attempt + 2)
        if position + 1 < len(order):
            store.event(pid, f'{name} indisponível (HTTP {last.status}). Continuando com {order[position + 1]}; cobrança conforme provedor.')
    raise last
