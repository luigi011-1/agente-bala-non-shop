import json
import flow_seguro as fs

K_ANTIGO = {
    "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
    "reference_use": "Use the attached character sheet only for Jordan Vale's exact identity (face, skin, hair, body), wardrobe and jewelry; ignore its grey studio background. The setting is described here.",
    "identity_main": "The exact fictional AI character Jordan Vale, explicitly male: very rich white American man around sixty-eight.",
    "wardrobe": "Cream dinner jacket.", "scene": "A dining room.",
    "prop": "He holds an amber glass bottle of whiskey with a plain cream paper label with no readable text; a small real flame burns on the pile.",
    "posture": "Sits upright.", "composition": "Centered. Nothing else is in frame. The background is reduced by framing, never by blur.",
    "camera": "1x lens", "lighting": "Neutral overcast daylight, never white or blown out, with no harsh shadows.",
    "state": "Start frame.", "realism": "iPhone footage look, no AI polish, no beauty smoothing.",
    "aspect_ratio": "9:16 vertical",
    "negative": "no captions, no subtitles, no extra fingers, no de-aging, no phone in frame",
}


def test_k_antigo_e_pego_e_k_novo_passa():
    antigo = json.dumps(K_ANTIGO)
    termos = {t for _, t, _ in fs.varrer_k(antigo)}
    assert any("real person" in t or "fictional AI" in t for t in termos)
    assert any("explicitly" in t for t in termos)
    assert any("whiskey" in t.lower() for t in termos)
    novo = fs.seguro_k(K_ANTIGO)
    assert "fiction_note" not in novo and "negative" not in novo
    assert "text-free" in novo["clean_frame"]
    texto = fs.texto_flow(novo)
    assert fs.varrer_k(texto) == [], fs.varrer_k(texto)
    assert "SMARTPHONE" in texto and "iPhone" not in texto


def test_v_troca_termos_mas_preserva_a_fala():
    v = ('o que acontece no vídeo: ele vira o uísque sobre o sal e um isqueiro acende; fala: "o uísque e o isqueiro ficam na mesa"')
    out = fs.seguro_v(v)
    assert 'fala: "o uísque e o isqueiro ficam na mesa"' in out
    assert "isqueiro acende" not in out and "uísque sobre" not in out
    assert fs.varrer_v(out) == []


def test_limite_de_negacoes():
    assert any(n == "FALHA" for n, _, _ in fs.varrer_k("no a, no b, never c"))
    assert not fs.varrer_k("A plain text-free frame, everything in sharp focus.")
