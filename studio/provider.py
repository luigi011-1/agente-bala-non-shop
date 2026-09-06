import base64
import json
import mimetypes
import os
import re
import threading
import time
import math
import random
from contextlib import ExitStack
from pathlib import Path

import httpx

from . import storage as store
from .rules import POLICY
from . import credentials

_key = os.environ.get('OPENAI_API_KEY', '')
_kie_key = os.environ.get('KIE_API_KEY', '')
_gemini_key = os.environ.get('GEMINI_API_KEY', '')
DEFAULT_MODEL = 'gpt-6-astra'
DEFAULT_GEMINI_MODEL = 'gemini-3.5-flash'
DEFAULT_EFFORT = 'medium'
_model = os.environ.get('AURALY_TEXT_MODEL', DEFAULT_MODEL)
_effort = DEFAULT_EFFORT
_verification = None
_allow_temp_upload = False
_text_provider = 'auto'
_lock = threading.Lock()


def configure(key=None, model=None, effort=None, kie_key=None, gemini_key=None, allow_temp_upload=None, text_provider=None):
    global _key, _model, _effort, _verification, _kie_key, _gemini_key, _allow_temp_upload
    global _text_provider
    with _lock:
        if effort and effort not in ['low', 'medium', 'high', 'xhigh', 'max']:
            raise ValueError('Nível de raciocínio inválido.')
        if key is not None:
            _key = key.strip()
        if kie_key is not None:
            _kie_key = kie_key.strip()
        if gemini_key is not None:
            _gemini_key = gemini_key.strip()
        if model:
            _model = model.strip()
        if effort:
            _effort = effort
        if allow_temp_upload is not None:
            _allow_temp_upload = allow_temp_upload
        if text_provider is not None:
            if text_provider not in ('auto', 'openai', 'gemini', 'kie'):
                raise ValueError('Provedor de texto inválido.')
            _text_provider = text_provider
        _verification = None


def load_preferences():
    path = store.DATA / 'preferences.json'
    if path.is_file():
        value = json.loads(path.read_text(encoding='utf-8-sig'))
        secrets = json.loads(credentials.unprotect(value['protected_credentials'])) if value.get('protected_credentials') else value
        configure(key=secrets.get('openai_key'),
                  kie_key=secrets.get('kie_key'),
                  gemini_key=secrets.get('gemini_key'),
                  allow_temp_upload=value.get('allow_temp_upload', False),
                  text_provider=value.get('text_provider', 'auto'),
                  model=value.get('text_model', DEFAULT_MODEL),
                  effort=value.get('reasoning_effort', DEFAULT_EFFORT))
        if any(k in value for k in ('openai_key', 'kie_key', 'gemini_key')):
            save_preferences()


def save_preferences():
    store.write_json(store.DATA / 'preferences.json',
                     {'text_model': _model, 'reasoning_effort': _effort,
                      'allow_temp_upload': _allow_temp_upload,
                      'text_provider': _text_provider,
                      'protected_credentials': credentials.protect(json.dumps({
                          'openai_key': _key, 'kie_key': _kie_key, 'gemini_key': _gemini_key}))})


def settings():
    return {'configured': bool(_key), 'kie_configured': bool(_kie_key),
            'gemini_configured': bool(_gemini_key),
            'text_model': _model, 'image_model': 'gpt-image-2',
            'reasoning_effort': _effort, 'verification': _verification,
            'gemini_model': DEFAULT_GEMINI_MODEL, 'allow_temp_upload': _allow_temp_upload,
            'text_provider': _text_provider,
            'key_storage': 'Protegidas por Windows DPAPI, vinculadas ao usuário atual.'}


def safe_error(value):
    text = str(value)
    if _key:
        text = text.replace(_key, '[CHAVE OCULTA]')
    if _kie_key:
        text = text.replace(_kie_key, '[CHAVE OCULTA]')
    if _gemini_key:
        text = text.replace(_gemini_key, '[CHAVE OCULTA]')
    return re.sub(r'(sk-|pcsk_|AIza)[A-Za-z0-9_\\-]+', '[CHAVE OCULTA]', text)[:1200]


def verify_access():
    """Read-only catalog check, not a generation/vision/credit test."""
    global _verification
    require_key()
    with _lock:
        key, model = _key, _model
    models = [model, 'gpt-image-2']
    try:
        with httpx.Client(timeout=20) as client:
            for model_id in models:
                response = client.get('https://api.openai.com/v1/models/' + model_id,
                                      headers={'Authorization': f'Bearer {key}'})
                if response.is_error:
                    raise ValueError(f'Não foi possível consultar {model_id}: HTTP {response.status_code}. '
                                     'Verifique a chave e as permissões do projeto.')
                if response.json().get('id') != model_id:
                    raise ValueError('A API retornou um identificador de modelo inesperado.')
    except httpx.TransportError:
        raise ValueError('Não foi possível conectar à OpenAI para verificar o acesso.') from None
    with _lock:
        if key != _key or model != _model:
            raise ValueError('Conexão alterada durante a verificação. Verifique novamente.')
        _verification = {'checked_at': store.now(), 'models': models, 'kind': 'catalog_only',
                         'note': 'Modelos consultáveis. Geração, saldo e qualidade ainda não testados.'}
    return _verification


def call_kind(route):
    return 'image' if route.startswith('images/') or route == 'kie/images' else 'text'


def check_call_allowed(project, route):
    if project.get('pause_requested'):
        raise ValueError('Produção pausada antes da próxima chamada. Resultados recebidos foram preservados.')
    kind = call_kind(route)
    limit = project.get('call_limits', {}).get(kind, 32 if kind == 'image' else 100)
    used = sum(call_kind(c['route']) == kind for c in project['calls'])
    if used >= limit:
        raise ValueError(f'Limite de chamadas {kind} atingido ({used}/{limit}). Ajuste o limite para continuar.')


def require_key():
    if not _key:
        raise ValueError('Configure sua chave OpenAI em Conexão para executar esta etapa.')


def require_think_key():
    available = {'openai': _key, 'gemini': _gemini_key, 'kie': _kie_key}
    if not (any(available.values()) if _text_provider == 'auto' else available[_text_provider]):
        raise ValueError('Configure a chave do provedor de texto selecionado em Conexão.')


def require_image_key():
    if not _key and not _kie_key:
        raise ValueError('Configure sua chave OpenAI ou Kie.ai em Conexão para gerar imagens.')


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
        # No automatic retries: image requests may have incurred a charge on timeout.
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
            raise ValueError('Conexão interrompida. A chamada pode ter sido cobrada; confira antes de tentar novamente.') from None
        raise
    finally:
        with store.LOCK:
            p = store.get(pid)
            p['calls'][index] = call
            store.save(p)


class ProviderError(ValueError):
    def __init__(self, message, status, retry_after=None):
        super().__init__(message)
        self.status = status
        try:
            self.retry_after = max(0, float(retry_after))
        except (ValueError, TypeError):
            self.retry_after = 0


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
        r = None
        for attempt in range(1):
            with httpx.Client(timeout=httpx.Timeout(600, connect=20)) as client:
                r = client.post(url, json=payload)
            # One recorded request per attempt. Operator controls retries.

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


# Kie.ai rejected a 3.46MB inline data URL and accepted 1.77MB; keep a margin under the 2MB mark.
KIE_INLINE_BUDGET = 1_800_000
# 520/522/524 are Cloudflare gateway timeouts that Kie.ai surfaces on slow vision calls.
TRANSIENT_STATUS = (408, 429, 500, 502, 503, 504, 520, 522, 524)


def _compress_for_kie(path):
    """PNG grids exceed Kie.ai's inline data URL limit; JPEG at native resolution fits well under it.
    Resolution is only sacrificed as a last resort, since the grids carry on-screen captions."""
    from PIL import Image as PILImage
    import io as _io
    with PILImage.open(path) as im:
        rgb = im.convert('RGB')
        for quality, cap in ((90, None), (82, None), (82, 3000), (78, 2048), (72, 1280)):
            frame = rgb
            if cap and max(rgb.size) > cap:
                frame = rgb.copy()
                frame.thumbnail((cap, cap), PILImage.LANCZOS)
            buf = _io.BytesIO()
            frame.save(buf, format='JPEG', quality=quality, optimize=True)
            raw = buf.getvalue()
            if len(raw) * 4 // 3 <= KIE_INLINE_BUDGET:
                break
    return 'data:image/jpeg;base64,' + base64.b64encode(raw).decode()


def _kie_think(pid, instruction, data, images=(), context=False):
    route = 'kie/text'
    docs = (store.folder(pid) / 'sources.md').read_text(encoding='utf-8') if context else ''
    content = [{'type': 'text', 'text': 'Return only valid JSON.\n' + json.dumps(data, ensure_ascii=False)}]
    for path in images:
        compressed = _compress_for_kie(Path(path))
        content.extend([{'type': 'text', 'text': f'FRAME: {Path(path).name}'},
                        {'type': 'image_url', 'image_url': {'url': compressed}}])
    call = {'route': route, 'model': 'gemini-3-5-flash-thinking', 'started': store.now(), 'status': 'sent'}
    with store.LOCK:
        p = store.get(pid)
        check_call_allowed(p, route)
        p['calls'].append(call)
        index = len(p['calls']) - 1
        store.save(p)
    try:
        with httpx.Client(timeout=httpx.Timeout(600, connect=20)) as client:
            response = client.post('https://api.kie.ai/gemini-3-5-flash-openai/v1/chat/completions',
                headers={'Authorization': f'Bearer {_kie_key}'}, json={
                    'model': call['model'], 'stream': False, 'max_tokens': 14000,
                    'messages': [{'role': 'system', 'content': POLICY + '\n' + instruction + '\nREFERENCE DOCUMENTS:\n' + docs},
                                 {'role': 'user', 'content': content}]})
        if response.is_error:
            call.update(http_status=response.status_code)
            raise ProviderError(f'Kie.ai Gemini HTTP {response.status_code}', response.status_code,
                                retry_after=response.headers.get('retry-after'))
        body = response.json()
        if isinstance(body, dict) and 'code' in body and 'msg' in body and 'choices' not in body:
            code = body.get('code', 0)
            msg = safe_error(str(body.get('msg', 'erro desconhecido')))
            call.update(http_status=code, error_detail=msg)
            if code in TRANSIENT_STATUS:
                raise ProviderError(f'Kie.ai Gemini HTTP {code}: {msg}', code)
            raise ValueError(f'Kie.ai erro: {msg}')
        if body.get('choices'):
            choice = body['choices'][0]
            fr = choice.get('finish_reason')
            if fr not in (None, 'stop', 'length'):
                raise ValueError(f'Kie.ai retornou resposta incompleta (finish_reason: {fr}).')
            if fr == 'length':
                store.event(pid, 'Kie.ai: saída truncada por limite de tokens; tentando extrair JSON parcial.')
            result = choice.get('message', {}).get('content', '')
        else:
            candidates = body.get('candidates', [])
            fr = candidates[0].get('finishReason') if candidates else None
            if not candidates or fr not in (None, 'STOP', 'MAX_TOKENS'):
                raise ValueError(f'Kie.ai retornou resposta incompleta (finishReason: {fr}).')
            if fr == 'MAX_TOKENS':
                store.event(pid, 'Kie.ai: saída truncada por limite de tokens; tentando extrair JSON parcial.')
            result = ''.join(part.get('text', '') for part in candidates[0].get('content', {}).get('parts', []) if not part.get('thought'))
        result = re.sub(r'^```(?:json)?\s*|\s*```$', '', result.strip())
        try:
            parsed = json.loads(result)
        except json.JSONDecodeError:
            # Try to salvage truncated JSON by closing open brackets
            patched = result
            opens = patched.count('{') - patched.count('}')
            open_arr = patched.count('[') - patched.count(']')
            if opens > 0 or open_arr > 0:
                if patched.rstrip().endswith(','):
                    patched = patched.rstrip()[:-1]
                patched += ']' * max(0, open_arr) + '}' * max(0, opens)
                try:
                    parsed = json.loads(patched)
                except json.JSONDecodeError:
                    raise ValueError('Kie.ai não retornou JSON válido; etapa preservada para revisão.') from None
            else:
                raise ValueError('Kie.ai não retornou JSON válido; etapa preservada para revisão.') from None
        if not isinstance(parsed, dict):
            raise ValueError('Kie.ai não retornou objeto JSON.')
        call.update(status='completed', usage=body.get('usage', body.get('usageMetadata')),
                    credits_consumed=body.get('credits_consumed'))
        return parsed
    except Exception as exc:
        call['status'] = 'uncertain' if isinstance(exc, httpx.TransportError) else 'failed'
        if isinstance(exc, ProviderError):
            raise
        raise ValueError(safe_error(exc)) from None
    finally:
        call['finished'] = store.now()
        with store.LOCK:
            p = store.get(pid)
            p['calls'][index] = call
            store.save(p)


def think(pid, instruction, data, images=(), context=False):
    require_think_key()
    available = {'openai': _key, 'gemini': _gemini_key, 'kie': _kie_key}
    order = [k for k, key in available.items() if key] if _text_provider == 'auto' else [_text_provider]
    # Persist the successful fallback for this project; explicit selection overrides it.
    sticky = store.get(pid).get('active_text_provider')
    if _text_provider == 'auto' and sticky in order:
        order = order[order.index(sticky):]
    functions = {'openai': _openai_think, 'gemini': _gemini_think, 'kie': _kie_think}
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
                # 429 may be billing: switch once, do not blindly retry billing failures.
                if exc.status == 429 or attempt == 2:
                    break
                retry_wait(pid, max(exc.retry_after, 10 * 2 ** attempt + random.uniform(0, 3)), name, attempt + 2)
        if position + 1 < len(order):
            store.event(pid, f'{name} indisponível (HTTP {last.status}). Continuando com {order[position + 1]}; cobrança conforme provedor.')
    raise last


def _upload_temp(path):
    """Upload a file to tmpfiles.org and return a direct download URL (1h expiry)."""
    with httpx.Client(timeout=30) as client:
        with open(path, 'rb') as f:
            r = client.post('https://tmpfiles.org/api/v1/upload',
                            files={'file': (path.name, f,
                                            mimetypes.guess_type(str(path))[0] or 'image/png')})
    if r.is_error:
        raise ValueError(f'Falha ao enviar referência temporária: HTTP {r.status_code}')
    url = r.json().get('data', {}).get('url', '')
    if not url:
        raise ValueError('Upload temporário não retornou URL.')
    return url.replace('tmpfiles.org/', 'tmpfiles.org/dl/', 1)


def _kie_image(pid, prompt, references, destination, recovery=None):
    """Generate/edit image via Kie.ai GPT Image 2 (async task model)."""
    with _lock:
        key = _kie_key
    if not key:
        raise ValueError('Configure sua chave Kie.ai para usar o fallback de imagem.')
    headers = {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}

    if recovery is None:
        check_call_allowed(store.get(pid), 'kie/images')
    if references and not _allow_temp_upload:
        raise ValueError('Kie.ai requer envio das referências ao tmpfiles.org. Autorize explicitamente em Conexão.')

    if references:
        urls = []
        for path in references:
            check_call_allowed(store.get(pid), 'kie/images')
            urls.append(_upload_temp(path))
        body = {'model': 'gpt-image-2-image-to-image',
                'input': {'prompt': prompt, 'input_urls': urls,
                          'aspect_ratio': '9:16', 'resolution': '2K'}}
    else:
        body = {'model': 'gpt-image-2-text-to-image',
                'input': {'prompt': prompt, 'aspect_ratio': '9:16', 'resolution': '2K'}}

    call = {'route': 'kie/images', 'started': store.now(), 'status': 'sent',
            'model': body['model']}
    with store.LOCK:
        p = store.get(pid)
        if recovery is not None:
            index = recovery
            call = p['calls'][index]
        else:
            check_call_allowed(p, 'kie/images')
            call['destination'] = str(destination.relative_to(store.folder(pid))).replace('\\', '/')
            p['calls'].append(call)
            index = len(p['calls']) - 1
            store.save(p)

    try:
        if recovery is None:
            with httpx.Client(timeout=30) as client:
                r = client.post('https://api.kie.ai/api/v1/jobs/createTask',
                                headers=headers, json=body)
            if r.is_error:
                raise ValueError(f'Kie.ai HTTP {r.status_code}')
            resp = r.json()
            if resp.get('code') != 200:
                raise ValueError(safe_error(f'Kie.ai: {resp.get("msg", "erro ao criar task")}'))
            task_id = resp['data']['taskId']
            call.update(task_id=task_id, status='pending')
            with store.LOCK:
                p = store.get(pid)
                p['calls'][index] = call
                store.save(p)
        else:
            task_id = call['task_id']

        delay = 3
        deadline = time.monotonic() + 600
        while time.monotonic() < deadline:
            if store.get(pid).get('pause_requested'):
                raise ValueError('Consulta pausada. A tarefa remota continua; retome para recuperar o resultado.')
            time.sleep(delay)
            if store.get(pid).get('pause_requested'):
                raise ValueError('Consulta pausada. Retome para recuperar a tarefa existente.')
            with httpx.Client(timeout=30) as client:
                sr = client.get(f'https://api.kie.ai/api/v1/jobs/recordInfo?taskId={task_id}',
                                headers={'Authorization': f'Bearer {key}'})
            if sr.is_error:
                raise ValueError(f'Kie.ai poll HTTP {sr.status_code}')
            sdata = sr.json().get('data', {})
            state = sdata.get('state', '')

            if state == 'success':
                result = json.loads(sdata.get('resultJson', '{}'))
                img_urls = result.get('resultUrls', [])
                if not img_urls:
                    raise ValueError('Kie.ai completou sem retornar URL da imagem.')
                with httpx.Client(timeout=120) as client:
                    img_r = client.get(img_urls[0])
                if img_r.is_error:
                    raise ValueError(f'Falha ao baixar imagem do Kie.ai: HTTP {img_r.status_code}')
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(img_r.content)
                from PIL import Image as PILImage
                with PILImage.open(destination) as im:
                    im.verify()
                call.update(status='completed', finished=store.now(),
                            usage={'kie_credits': sdata.get('creditsConsumed'),
                                   'kie_task_id': task_id})
                return

            if state == 'fail':
                call['remote_failed'] = True
                raise ValueError(f'Kie.ai geração falhou: {sdata.get("failMsg", "erro desconhecido")}')

            delay = min(delay * 1.5, 10)

        raise ValueError('Kie.ai: timeout após 10 minutos.')
    except Exception as exc:
        call.update(status='failed' if call.get('remote_failed') else 'uncertain')
        if not isinstance(exc, ValueError):
            raise ValueError(safe_error(exc)) from None
        raise
    finally:
        with store.LOCK:
            p = store.get(pid)
            p['calls'][index] = call
            store.save(p)


def image(pid, prompt, references, destination):
    if _key:
        try:
            _openai_image(pid, prompt, references, destination)
            return
        except ProviderError as exc:
            if exc.status != 429 or not _kie_key:
                raise
            store.event(pid, 'OpenAI HTTP 429 (limite/cota). Alternando para Kie.ai; cobrança na conta Kie.ai.')
    if _kie_key:
        _kie_image(pid, prompt, references, destination)
        return
    raise ValueError('Nenhuma chave de API configurada para geração de imagem.')


def recover_image(pid, relative):
    """Only query an existing remote task. Never submit a generation."""
    p = store.get(pid)
    for index in range(len(p['calls']) - 1, -1, -1):
        call = p['calls'][index]
        if call.get('destination') == relative and call.get('task_id') and not call.get('remote_failed'):
            _kie_image(pid, '', [], store.folder(pid) / relative, recovery=index)
            return True
    return False


def _openai_image(pid, prompt, references, destination):
    fields = {'model': 'gpt-image-2', 'prompt': prompt, 'n': '1', 'size': '1152x2048',
              'quality': 'high', 'output_format': 'png'}
    if references:
        with ExitStack() as stack:
            files = [('image[]', (p.name, stack.enter_context(p.open('rb')),
                                  mimetypes.guess_type(p.name)[0] or 'image/png')) for p in references]
            body = request(pid, 'images/edits', data=fields, files=files)
    else:
        fields['n'] = 1
        body = request(pid, 'images/generations', json=fields)
    encoded = body.get('data', [{}])[0].get('b64_json')
    if not encoded:
        raise ValueError('A API não retornou uma imagem PNG.')
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(base64.b64decode(encoded, validate=True))
    from PIL import Image
    with Image.open(destination) as im:
        im.verify()
