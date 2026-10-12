"""Contrato opt-in, proteção temporal e filtro musical executável."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('plano_editorial', ROOT / '.claude/skills/edicao/template/plano_editorial.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def plan(**kwargs):
    return dict(version=1, offer='sea_moss', **kwargs)


class EditorialTests(unittest.TestCase):
    def test_auraly_style_override_cannot_accept_sea_moss_plan(self):
        with self.assertRaises(ValueError):
            MODULE.validar_contexto(plan(), True, 'fitwell')
        with self.assertRaises(ValueError):
            MODULE.validar_contexto(plan(), True, 'auraly')
        adapted = dict(version=1, offer='auraly', adaptation=dict(rationale='Ritmo próprio'))
        with self.assertRaises(ValueError):
            MODULE.validar_contexto(adapted, True, 'fitwell')
        self.assertEqual(MODULE.validar_contexto(adapted, True, 'auraly'), adapted)
        self.assertEqual(MODULE.validar_contexto(plan(), False, 'fitwell'), plan())

    def test_read_json_and_copy(self):
        original = plan(rhythm=[dict(take=1, speed=1.1)])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'plan.json'
            path.write_text(json.dumps(original))
            result = MODULE.carregar_plano(path)
        result['rhythm'][0]['speed'] = 1.2
        self.assertEqual(original['rhythm'][0]['speed'], 1.1)

    def test_auraly_requires_reasoned_adaptation(self):
        with self.assertRaises(ValueError):
            MODULE.validar_plano(dict(version=1, offer='auraly'))
        result = MODULE.validar_plano(dict(version=1, offer='auraly', adaptation=dict(rationale='Adaptar ao tom da oferta.')))
        self.assertEqual(result['offer'], 'auraly')

    def test_caption_layout_valid_limits_and_optional_fields(self):
        for captions in ({}, {'max_words': 2, 'top': 200, 'hero_top': 1500},
                         {'max_words': 6, 'top': 1500, 'hero_top': 200}, {'top': 880}):
            self.assertEqual(MODULE.validar_plano(plan(captions=captions))['captions'], captions)

    def test_caption_layout_rejects_invalid_counts_anchors_and_aliases(self):
        bad = [{'max_words': 1}, {'max_words': 7}, {'max_words': True}, {'max_words': 3.0},
               {'top': 199}, {'top': 1501}, {'hero_top': 199}, {'hero_top': 1501},
               {'top': False}, {'hero_top': float('nan')}, {'maxWords': 3},
               {'font': 'Anton'}, {'style': 'semantic'}, None]
        for captions in bad:
            with self.subTest(captions=captions), self.assertRaises(ValueError):
                MODULE.validar_plano(plan(captions=captions))

    def test_caption_layout_refuses_auraly_even_with_adaptation(self):
        with self.assertRaises(ValueError):
            MODULE.validar_plano(dict(version=1, offer='auraly',
                                     adaptation=dict(rationale='Tom próprio adaptado'), captions={'top': 880}))

    def test_protection_union_and_no_automatic_protection(self):
        protection = [dict(take=1, start=0, end=2.4, reason='Ação visual observada'),
                      dict(take=1, start=2, end=3, reason='Conclusão da ação')]
        original = [[2.5, 4], [5, 6]]
        self.assertEqual(MODULE.proteger_intervalos(original, 1, plan(protected_intervals=protection), 7), [[0, 4], [5, 6]])
        self.assertEqual(MODULE.proteger_intervalos(original, 1, plan(), 7), original)
        self.assertEqual(original, [[2.5, 4], [5, 6]])

    def test_bad_protection_bounds_and_numbers(self):
        for start, end in [(0, 8), (3, 2), (-1, 2), (True, 2), (0, float('nan'))]:
            with self.subTest(start=start, end=end), self.assertRaises(ValueError):
                MODULE.proteger_intervalos([], 1, plan(protected_intervals=[dict(take=1, start=start, end=end, reason='ação')]), 7)
        for intervals in [[[3, 2]], [[0, float('inf')]], [[0, True]], [[0]]]:
            with self.assertRaises(ValueError):
                MODULE.proteger_intervalos(intervals, 1, plan(), 7)

    def test_missing_invalid_unknown_and_duplicate_take(self):
        bad = [plan(other=1), plan(rhythm=[dict(speed=1)]),
               plan(rhythm=[dict(take=True, speed=1)]),
               plan(rhythm=[dict(take=1, speed=1.1), dict(take=1, speed=1.2)]),
               plan(protected_intervals=[dict(take=1, start=0, end=1, reason=' ')]),
               plan(music=dict(points=[dict(time=1, db=-20), dict(time=1, db=-21)])),
               plan(music=dict(points=[dict(time=0, db=-17)]))]
        for item in bad:
            with self.subTest(item=item), self.assertRaises(ValueError):
                MODULE.validar_plano(item)

    def test_rhythm_mapping_mute_insert_and_ramp(self):
        segs = [dict(k=1, a=0, b=2, sp=1.12), dict(k=1, a=2, b=3, sp=5, mute=True),
                dict(k=2, a=0, b=2, sp=1.12, mute=True)]
        old = copy.deepcopy(segs)
        output = MODULE.aplicar_ritmo(segs, plan(rhythm=[dict(take=1, speed=1.25), dict(take=2, speed=1)]))
        self.assertEqual([s['sp'] for s in output], [1.25, 5, 1])
        self.assertAlmostEqual(output[2]['o'], 1.8)
        self.assertAlmostEqual(output[2]['d'], 2)
        self.assertEqual(segs, old)

    def test_protected_action_keeps_normal_speed_only_in_span(self):
        p = plan(protected_intervals=[dict(take=1, start=0, end=1, reason='Mostrar objeto')])
        output = MODULE.aplicar_ritmo([dict(k=1, a=0, b=3, sp=1.2)], p)
        self.assertEqual([s['sp'] for s in output], [1, 1.2])
        self.assertEqual(MODULE.protected_output_windows(output, p), [[0, 1]])

    def test_output_window_uses_actual_frame_duration(self):
        p = plan(protected_intervals=[dict(take=1, start=1, end=2, reason='Pausa útil')])
        output = [dict(k=1, a=0, b=3, sp=1.2, o=4, d=2.4)]
        windows = MODULE.protected_output_windows(output, p)
        self.assertAlmostEqual(windows[0][0], 4.8)
        self.assertAlmostEqual(windows[0][1], 5.6)

    def test_output_protection_only_intersections_and_matching_take(self):
        p = plan(protected_intervals=[dict(take=1, start=1, end=4, reason='Ação'),
                                     dict(take=1, start=6, end=7, reason='Pausa')])
        segs = [dict(k=1, a=0, b=2, sp=1, o=0, d=2),
                dict(k=2, a=0, b=2, sp=1, o=2, d=2),
                dict(k=1, a=3, b=5, sp=1, o=4, d=2),
                dict(k=1, a=7, b=8, sp=1, o=6, d=1)]
        # A fonte removida [2,3], o take 2 e a borda em 7 não
        # estendem autorização aos silêncios vizinhos.
        self.assertEqual(MODULE.protected_output_windows(segs, p), [[1, 2], [4, 5]])

    def test_adjacent_overlapping_protection_merges_without_extra_margin(self):
        p = plan(protected_intervals=[dict(take=1, start=1, end=2, reason='Ação'),
                                     dict(take=1, start=1.5, end=3, reason='Continuação')])
        segs = [dict(k=1, a=0, b=2, sp=1, o=0, d=2),
                dict(k=1, a=2, b=4, sp=1, o=2, d=2)]
        self.assertEqual(MODULE.protected_output_windows(segs, p), [[1, 3]])

    def test_speed_numbers(self):
        for speed in [True, float('nan'), float('inf'), .99, 1.26]:
            with self.subTest(speed=speed), self.assertRaises(ValueError):
                MODULE.validar_plano(plan(rhythm=[dict(take=1, speed=speed)]))

    def test_take_absent_and_invalid_output_time(self):
        with self.assertRaises(ValueError):
            MODULE.aplicar_ritmo([dict(k=1, a=0, b=1, sp=1)], plan(rhythm=[dict(take=2, speed=1)]))
        with self.assertRaises(ValueError):
            MODULE.protected_output_windows([dict(k=1, a=0, b=1, o=float('nan'), d=1)], plan())

    def test_music_offset_and_fades_short_clip(self):
        p = plan(music=dict(start_seconds=30, fade_in_seconds=2, fade_out_seconds=3, points=[dict(time=0, db=-30), dict(time=.2, db=-18)]))
        self.assertEqual(MODULE.music_start_seconds(p), 30)
        filters = MODULE.filtro_musica(.3, p)
        self.assertIn('afade=t=in:st=0:d=0.3', filters)
        self.assertIn('afade=t=out:st=0:d=0.3', filters)
        with self.assertRaises(ValueError):
            MODULE.filtro_musica(.1, p)

    def test_default_music_fades_and_explicit_zero(self):
        result = MODULE.filtro_musica(2, plan(music={}))
        self.assertIn('afade=t=in:st=0:d=0.3', result)
        self.assertIn('afade=t=out:st=1.2:d=0.8', result)
        self.assertNotIn('afade', MODULE.filtro_musica(2, plan(music={'fade_in_seconds': 0, 'fade_out_seconds': 0})))

    def test_silence_adjacent_permissions_union_and_outside_rejected(self):
        p = plan(protected_intervals=[dict(take=1, start=0, end=1, reason='Ação')])
        segs = [dict(k=1, a=0, b=1, sp=1, o=0, d=1),
                dict(k=1, a=1, b=3.5, sp=5, o=1, d=.5, mute=True)]
        self.assertEqual(MODULE.silencios_nao_autorizados([[.8, 1.2], [1.4, 1.8]], segs, p), [[1.4, 1.8]])
        self.assertEqual(MODULE.silencios_nao_autorizados([[.8, 1.2]], segs[:1], p), [[.8, 1.2]])
        self.assertEqual(MODULE.silencios_nao_autorizados([[.1, .3]], segs[:1], plan()), [[.1, .3]])

    def test_silence_numeric_validation_and_bounded_tolerance(self):
        segs = [dict(k=1, a=0, b=1, sp=1, o=0, d=1, mute=True)]
        self.assertEqual(MODULE.silencios_nao_autorizados([[0, 1.02]], segs, plan(), 1 / 30), [])
        for tolerance in [-.1, .04, True, float('nan')]:
            with self.subTest(tolerance=tolerance), self.assertRaises(ValueError):
                MODULE.silencios_nao_autorizados([], segs, plan(), tolerance)
        for silence in [[0, True], [0, float('inf')], [1, 0], [0], [0, 0]]:
            with self.subTest(silence=silence), self.assertRaises(ValueError):
                MODULE.silencios_nao_autorizados([silence], segs, plan())

    @unittest.skipUnless(shutil.which('ffmpeg'), 'ffmpeg indisponível')
    def test_ffmpeg_real_envelope_expression(self):
        p = plan(music=dict(fade_in_seconds=.02, fade_out_seconds=.02, points=[dict(time=0, db=-30), dict(time=.1, db=-18), dict(time=.2, db=-25)]))
        result = subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-f', 'lavfi', '-i',
                                 'sine=frequency=440:duration=0.3', '-af', MODULE.filtro_musica(.3, p),
                                 '-f', 'null', '-'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
