"""Catálogo de pesquisa editorial independente de produtos/ofertas."""
from __future__ import annotations
import json
from pathlib import Path
import re
import unicodedata


def _key(text: str) -> str:
    value = unicodedata.normalize('NFKD', text.casefold())
    value = ''.join(c for c in value if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '-', value).strip('-')


def catalog() -> dict:
    return json.loads(Path(__file__).with_name('catalogo_nichos.json').read_text(encoding='utf-8'))


def resolve_niche(niche: str | None = None, *, angle: str | None = None) -> dict:
    """Explicit niche wins; legacy angle only supplies broad editorial default."""
    data = catalog()
    if niche is None and angle:
        for item in data['niches']:
            if angle in item['legacy_angles']:
                return {k: item[k] for k in ('slug', 'label', 'search_terms_en')} | {'custom': False}
    if not isinstance(niche, str) or not niche.strip() or len(niche.strip()) > 200:
        raise ValueError('Informe --niche (nicho textual até 200 caracteres) ou --angle legado')
    key = _key(niche)
    if not key:
        raise ValueError('Nicho deve conter texto pesquisável')
    for item in data['niches']:
        if key in {_key(v) for v in [item['slug'], item['label'], *item['aliases']]}:
            return {k: item[k] for k in ('slug', 'label', 'search_terms_en')} | {'custom': False}
    # Free-form labels are retained as search hints. The researcher translates
    # them to English before discovery; the catalog never inserts product names.
    return {'slug': key, 'label': niche.strip(), 'search_terms_en': [], 'custom': True}


def mining_defaults() -> dict:
    return dict(catalog()['defaults'])
