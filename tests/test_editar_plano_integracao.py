"""Integração editorial sem ASR/download: ilhas simuladas, mix FFmpeg real."""
import importlib.util
import struct
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import wave

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('editar_integracao', ROOT / '.claude/skills/edicao/template/editar.py')
EDITOR = importlib.util.module_from_spec(SPEC)
# Evita bootstrap execv/modelos em teste unitário; ASR não é parte deste
# contrato. O mix abaixo usa FFmpeg real e o módulo motor real.
with mock.patch.dict(sys.modules, {'whisperx': mock.MagicMock()}):
    SPEC.loader.exec_module(EDITOR)


def plan(**kwargs):
    return dict(version=1, offer='sea_moss', **kwargs)


class EditorIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.patch = mock.patch.object(EDITOR, 'PLANO_EDITORIAL', None)
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def test_short_caption_does_not_merge_across_takes_in_editorial_mode(self):
        EDITOR.PLANO_EDITORIAL = plan()
        pages = [[dict(w='first', t=0, k=1)], [dict(w='second', t=.1, k=2)]]
        self.assertEqual(EDITOR.juntar_curtas(pages), pages)

    def test_sub_frame_protection_is_rejected_before_source_filter(self):
        EDITOR.PLANO_EDITORIAL = plan(protected_intervals=[dict(take=1, start=0, end=.01, reason='Inválido para render')])
        with mock.patch.object(EDITOR, 'ilhas', return_value=[[2, 3]]), self.assertRaises(ValueError):
            EDITOR.segmentos([(1, 'take.mp4')], {1: [['word', 2, 3]]}, {})

    def test_default_does_not_expand_source_islands(self):
        with mock.patch.object(EDITOR, 'ilhas', return_value=[[2, 3], [4, 5]]):
            segs = EDITOR.segmentos([(1, 'take.mp4')], {1: [['word', 2, 3]]}, {1: 5})
        self.assertEqual([(s['a'], s['b'], s['sp']) for s in segs], [(2, 3, 1.12), (3, 4, 5), (4, 5, 1.12)])

    def test_initial_action_joins_fala_preserves_later_ramp(self):
        EDITOR.PLANO_EDITORIAL = plan(protected_intervals=[dict(take=1, start=0, end=2.5, reason='Mostrar produto antes da fala')],
                                     rhythm=[dict(take=1, speed=1.1)])
        with mock.patch.object(EDITOR, 'dur', return_value=6), mock.patch.object(EDITOR.motor, 'ilhas_v4', return_value=[[2.3, 3], [4, 5]]):
            segs = EDITOR.segmentos([(1, 'take.mp4')], {1: [['word', 2.3, 3]]}, {1: 5}, {1: [['word', 2.3, 3]]})
        self.assertEqual([(s['a'], s['b']) for s in segs], [(0, 3), (3, 4), (4, 5)])
        output = EDITOR.plano_editorial.aplicar_ritmo(segs, EDITOR.PLANO_EDITORIAL)
        ramp = [s for s in output if s.get('mute')]
        self.assertEqual(len(ramp), 1)
        self.assertEqual(ramp[0]['sp'], 5)
        self.assertTrue(all(s['sp'] == 1.1 for s in output if not s.get('mute')))
        windows = EDITOR.plano_editorial.protected_output_windows(output, EDITOR.PLANO_EDITORIAL)
        self.assertAlmostEqual(windows[0][1], 2.5 / 1.1)

    def test_protected_mute_take_marks_all_islands_mute(self):
        EDITOR.PLANO_EDITORIAL = plan(protected_intervals=[dict(take=1, start=0, end=2, reason='Ação inicial')])
        with mock.patch.object(EDITOR, 'dur', return_value=6), mock.patch.object(EDITOR, 'janela_insert', return_value=[[4, 5]]):
            segs = EDITOR.segmentos([(1, 'silent.mp4')], {1: []}, {})
        self.assertTrue(all(s.get('mute') for s in segs), segs)

    def test_mix_command_opt_in_offsets_and_loops_music_only(self):
        EDITOR.PLANO_EDITORIAL = plan(music=dict(start_seconds=2, points=[dict(time=0, db=-30), dict(time=1, db=-18)]))
        with mock.patch.object(EDITOR, 'sh') as run, mock.patch.object(EDITOR, 'dur', return_value=10):
            offset = EDITOR.mixar('voice.wav', 'music.wav', 2, 'out.wav')
        command = run.call_args.args[0]
        self.assertEqual(offset, 2)
        self.assertEqual(command[command.index('-ss') + 1], '2')
        self.assertEqual(command[command.index('-stream_loop') + 1], '-1')
        self.assertLess(command.index('voice.wav'), command.index('-stream_loop'))
        filters = command[command.index('-filter_complex') + 1]
        self.assertIn("volume='pow(10", filters)
        self.assertIn('atrim=duration=2.000000', filters)

    def test_music_source_offset_past_end_is_rejected(self):
        EDITOR.PLANO_EDITORIAL = plan(music=dict(start_seconds=.3))
        with mock.patch.object(EDITOR, 'dur', return_value=.2), self.assertRaises(ValueError):
            EDITOR.mixar('voice.wav', 'music.wav', 1, 'out.wav')

    def test_default_mix_command_remains_same(self):
        with mock.patch.object(EDITOR, 'sh') as run, mock.patch.object(EDITOR, 'sh_err', return_value=''):
            EDITOR.mixar('voice.wav', 'music.wav', 2, 'out.wav')
        command = run.call_args.args[0]
        self.assertNotIn('-stream_loop', command)
        self.assertIn('volume=-18dB', command[command.index('-filter_complex') + 1])

    def test_protection_only_keeps_default_music_path_and_fades(self):
        EDITOR.PLANO_EDITORIAL = plan(protected_intervals=[dict(take=1, start=0, end=1, reason='Ação')])
        with mock.patch.object(EDITOR, 'sh') as run, mock.patch.object(EDITOR, 'sh_err', return_value=''):
            EDITOR.mixar('voice.wav', 'music.wav', 2, 'out.wav')
        command = run.call_args.args[0]
        filters = command[command.index('-filter_complex') + 1]
        self.assertNotIn('-stream_loop', command)
        self.assertIn('volume=-18dB', filters)
        self.assertIn('afade=t=in:d=0.3', filters)
        self.assertIn('afade=t=out:st=1.20:d=0.8', filters)

    def test_no_music_copies_voice_even_with_plan(self):
        EDITOR.PLANO_EDITORIAL = plan()
        with tempfile.TemporaryDirectory() as tmp:
            source, target = Path(tmp) / 'voice.wav', Path(tmp) / 'out.wav'
            source.write_bytes(b'preserved original')
            self.assertEqual(EDITOR.mixar(str(source), None, 2, str(target)), 0)
            self.assertEqual(target.read_bytes(), source.read_bytes())

    @unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'FFmpeg indisponível')
    def test_real_mix_short_music_loop_and_source_offset(self):
        EDITOR.PLANO_EDITORIAL = plan(music=dict(start_seconds=.08, fade_in_seconds=.03, fade_out_seconds=.05,
                                               points=[dict(time=0, db=-30), dict(time=.4, db=-18)]))
        with tempfile.TemporaryDirectory() as tmp:
            voice, music, target = [str(Path(tmp) / name) for name in ('voice.wav', 'music.wav', 'out.wav')]
            for path, signal in ((voice, 'anullsrc=r=44100:cl=mono:d=0.7'),
                                 (music, 'sine=frequency=180:duration=0.2')):
                subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i',
                                signal, '-ar', '44100', '-ac', '1', path], check=True)
            self.assertEqual(EDITOR.mixar(voice, music, .7, target), .08)
            with wave.open(target) as output:
                duration = output.getnframes() / output.getframerate()
                self.assertAlmostEqual(duration, .7, delta=.025)
                self.assertEqual(output.getnchannels(), 1)
                self.assertEqual(output.getframerate(), 44100)
                output.setpos(int(.5 * output.getframerate()))
                tail = output.readframes(int(.08 * output.getframerate()))
                samples = struct.unpack('<' + 'h' * (len(tail) // 2), tail)
                # Voz é zero: energia nesta janela posterior ao fim da faixa
                # curta comprova que o looping musical continua no mix.
                self.assertGreater(sum(x * x for x in samples) / len(samples), 1)


if __name__ == '__main__':
    unittest.main()
