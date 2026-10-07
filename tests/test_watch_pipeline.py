"""/watch regression tests. Synthetic FFmpeg fixtures; no ASR model/network download."""
import importlib.util
from contextlib import redirect_stderr
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".agents/skills/watch/scripts/watch_pipeline.py"
SPEC = importlib.util.spec_from_file_location("watch_pipeline", SCRIPT)
watch = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(watch)


class WatchArguments(unittest.TestCase):
    def test_invalid_numeric_options_fail_before_extracting(self):
        for flags in (["--timeline-fps", "0"], ["--timeline-fps", "nan"],
                      ["--scene-threshold", "1.1"], ["--jobs", "0"],
                      ["--cpu-threads", "0"], ["--command-timeout", "inf"]):
            with self.subTest(flags=flags), redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as failure:
                watch.main(["--video", "unused.mp4", *flags])
            self.assertEqual(failure.exception.code, 2)

    def test_silent_mode_cannot_claim_word_alignment(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            watch.main(["--video", "unused.mp4", "--no-audio", "--alignment", "whisperx"])

    def test_english_model_does_not_process_portuguese_as_english(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            watch.main(["--video", "unused.mp4", "--language", "pt"])

    def test_unknown_output_files_are_protected(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            (output / "audio").mkdir()
            original = output / "audio/audio.wav"
            original.write_bytes(b"user asset")
            with self.assertRaises(watch.PipelineError):
                watch.check_output_ownership(output)
            self.assertEqual(original.read_bytes(), b"user asset")

    def test_existing_lock_is_never_removed_by_another_run(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            lock = output / ".watch.lock"
            lock.write_text("other process")
            with self.assertRaises(watch.PipelineError):
                with watch.output_lock(output):
                    self.fail("acquired existing lock")
            self.assertEqual(lock.read_text(), "other process")

    def test_compatibility_entry_point_exposes_same_options(self):
        result = subprocess.run([sys.executable, str(ROOT / ".claude/skills/watch/scripts/watch_pipeline.py"),
                                 "--help"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("--alignment", result.stdout)


class WordAlignment(unittest.TestCase):
    @unittest.skipUnless(importlib.util.find_spec("numpy"), "NumPy required for actual WhisperX scalar regression")
    def test_numpy_word_data_serializes_without_losing_missing_times(self):
        import numpy as np
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "words.json"
            watch.write_json(target, {"segment_index": np.int64(2), "words": [
                {"word": "hello", "start": np.float32(0.125), "end": np.float64(0.5)},
                {"word": "2024", "start": np.float64(float("nan"))}]})
            result = json.loads(target.read_text())
        self.assertEqual(result["segment_index"], 2)
        self.assertEqual(result["words"][0]["start"], 0.125)
        self.assertIsNone(result["words"][1]["start"])
        self.assertNotIn("end", result["words"][1])

    def align_fake(self, source, words):
        align = mock.Mock(return_value={"segments": [{"text": "example", "words": words}],
                                        "word_segments": words})
        fake = SimpleNamespace(load_align_model=mock.Mock(return_value=(object(), {})), align=align)
        with mock.patch.dict(sys.modules, {"whisperx": fake}):
            result = watch.align_words(source, Path("audio.wav"), "en", "cpu")
        self.assertEqual(align.call_args.kwargs["interpolate_method"], "ignore")
        return result

    def test_missing_word_times_are_preserved_and_reported_partial(self):
        words = [{"word": "In", "start": 0.1, "end": 0.2}, {"word": "2024"}]
        result = self.align_fake([{"start": 0, "end": 1, "text": "In 2024"}], words)
        self.assertEqual(result["status"], "PARTIAL")
        self.assertEqual(result["unaligned_word_count"], 1)
        self.assertNotIn("start", result["words"][1])

    def test_segment_dropped_by_whisperx_cannot_pass_as_complete(self):
        result = self.align_fake([{"start": 0, "end": 1, "text": "First second"}],
                                 [{"word": "First", "start": 0.1, "end": 0.2}])
        self.assertEqual(result["status"], "PARTIAL")
        self.assertEqual(result["expected_word_count"], 2)


FFMPEG = shutil.which("ffmpeg") or ("/opt/homebrew/bin/ffmpeg" if Path("/opt/homebrew/bin/ffmpeg").exists() else None)
HAS_PILLOW = importlib.util.find_spec("PIL") is not None


@unittest.skipUnless(FFMPEG and HAS_PILLOW, "FFmpeg and Pillow required for synthetic video regression fixtures")
class WatchFixtures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture_dir = tempfile.TemporaryDirectory()
        cls.silent = Path(cls.fixture_dir.name) / "silent.mp4"
        cls.audio_video = Path(cls.fixture_dir.name) / "audio.mp4"
        command = [FFMPEG, "-v", "error", "-y"]
        for color in ("red", "blue", "red"):
            command += ["-f", "lavfi", "-i", f"color=c={color}:s=64x96:r=10:d=0.8"]
        command += ["-filter_complex", "[0:v][1:v][2:v]concat=n=3:v=1:a=0[out]",
                    "-map", "[out]", "-c:v", "libx264", "-pix_fmt", "yuv420p", str(cls.silent)]
        subprocess.run(command, check=True, capture_output=True, timeout=30)
        subprocess.run([FFMPEG, "-v", "error", "-y", "-i", str(cls.silent), "-f", "lavfi", "-i",
                        "sine=frequency=440:duration=2.4", "-c:v", "copy", "-c:a", "aac", "-shortest",
                        str(cls.audio_video)], check=True, capture_output=True, timeout=30)

    @classmethod
    def tearDownClass(cls):
        cls.fixture_dir.cleanup()

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.output = Path(self.temporary.name) / "decomposition"

    def tearDown(self):
        self.temporary.cleanup()

    def process(self, video=None, *flags):
        args = watch.build_parser().parse_args(["--video", str(video or self.silent),
                                                "--outdir", str(self.output), "--jobs", "1", *flags])
        return watch.process(args)

    def test_silent_reference_complete_only_when_explicitly_allowed(self):
        first = self.process()
        self.assertEqual(first["status"], "PARTIAL")
        self.assertEqual(first["audio"]["status"], "NO_AUDIO_STREAM")
        self.assertFalse(first["transcript"])
        second = self.process(None, "--allow-no-audio")
        self.assertEqual(second["status"], "COMPLETE")
        self.assertFalse(second["coverage"]["visual_review_performed"])
        self.assertEqual(second["analysis_status"], "PENDING_VISUAL_REVIEW")
        self.assertNotEqual(first["run_id"], second["run_id"])

    def test_dense_timeline_includes_first_frame_and_cuts(self):
        result = self.process(None, "--no-audio")
        self.assertEqual(result["status"], "COMPLETE")
        self.assertEqual(len(result["timeline"]), 12)
        self.assertEqual(result["scenes"][0]["t"], 0)
        self.assertEqual([item["t"] for item in result["scenes"]], [0, 0.8, 1.6])
        self.assertAlmostEqual(result["timeline"][-1]["t"], 2.2)
        for kind in ("timeline", "scenes"):
            for item in result[kind]:
                self.assertTrue((self.output / "frames" / kind / item["file"]).is_file())
            for image in result["overview"][kind]:
                self.assertTrue((self.output / "overview" / image).is_file())

    def test_asr_failure_on_rerun_never_reuses_old_transcript_or_words(self):
        segments = [{"start": 0.1, "end": 1.8, "text": "A real transcript"}]
        with mock.patch.object(watch, "faster_transcription", return_value=(segments, "en")):
            first = self.process(self.audio_video)
        self.assertEqual(first["status"], "COMPLETE")
        self.assertTrue((self.output / "audio/transcript.txt").exists())
        (self.output / "audio/words.json").write_text('[{"word":"old"}]')
        with mock.patch.object(watch, "faster_transcription", side_effect=ImportError("missing backend")):
            second = self.process(self.audio_video)
        self.assertEqual(second["status"], "PARTIAL")
        self.assertEqual(second["audio"]["status"], "FAILED")
        self.assertFalse(second["transcript"])
        self.assertFalse((self.output / "audio/transcript.txt").exists())
        self.assertFalse((self.output / "audio/words.json").exists())
        self.assertTrue((self.output / "overview" / second["overview"]["timeline"][0]).exists())
        self.assertEqual(json.loads((self.output / "manifest.json").read_text())["status"], "PARTIAL")

    def test_alignment_failure_keeps_genuine_transcription_but_returns_partial(self):
        segments = [{"start": 0.1, "end": 1.8, "text": "Spoken words"}]
        with mock.patch.object(watch, "faster_transcription", return_value=(segments, "en")), \
                mock.patch.object(watch, "align_words", side_effect=RuntimeError("download unavailable")):
            result = self.process(self.audio_video, "--alignment", "whisperx")
        self.assertEqual(result["status"], "PARTIAL")
        self.assertEqual(result["audio"]["status"], "SUCCEEDED")
        self.assertEqual(result["alignment"]["status"], "FAILED")
        self.assertEqual(json.loads((self.output / "audio/transcript.json").read_text()), segments)
        self.assertFalse((self.output / "audio/words.json").exists())

    def test_frame_failure_on_rerun_invalidates_and_removes_old_frames(self):
        self.process(None, "--no-audio")
        with mock.patch.object(watch, "extract_frames", side_effect=watch.PipelineError("decode error")):
            result = self.process(None, "--no-audio")
        self.assertEqual(result["status"], "FAILED")
        self.assertFalse((self.output / "frames").exists())
        self.assertFalse((self.output / "overview").exists())
        self.assertEqual(result["timeline"], [])

    def test_sampling_budget_fails_instead_of_truncating(self):
        result = self.process(None, "--no-audio", "--max-frames", "5")
        self.assertEqual(result["status"], "FAILED")
        self.assertEqual(result["timeline"], [])
        self.assertIn("nao sera truncado", result["errors"][0])

    @unittest.skipUnless(os.name != "nt" and shutil.which("bash"), "Unix symlink wrapper regression")
    def test_personal_skill_symlink_resolves_checkout_from_another_directory(self):
        link = Path(self.temporary.name) / "personal-watch"
        link.symlink_to(ROOT / ".agents/skills/watch", target_is_directory=True)
        result = subprocess.run(["bash", str(link / "scripts/run_watch.sh"), str(self.silent),
                                 "--no-audio", "--jobs", "1", "--outdir", str(self.output)],
                                cwd=self.temporary.name, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads((self.output / "manifest.json").read_text())["status"], "COMPLETE")


if __name__ == "__main__":
    unittest.main()
