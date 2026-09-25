"""A ficha do frame tem que reprovar o K01 que o Luigi gerou em 2026-09-25 e saiu outro gancho."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import ficha_frame as ff

FICHA = '''# FICHA DO FRAME

## K01
Frame: `frame.png`
Termos de forma: "upside-down U" · "funnel neck"

| Item | Status | Evidencia |
|---|---|---|
| F1 forma do heroi | OK | "upside-down U" |
| F2 quanto do quadro | OK | "fills the lower sixty percent of the frame" |
| F3 distancia da lente | OK | "only a few inches from the model" |
| F4 camera | OK | "ultra-wide 0.5x lens" |
| F5 pose do avatar | OK | "crouches low" |
| F6 lista fechada | OK | "The counter around the model is empty" |
| G1 luz neutra | OK | "Neutral overcast daylight" |
| G2 ceu ou janela | OK | "the outside clearly visible through the window" |
| G3 foco | OK | "everything in sharp focus" |
| G4 realismo | OK | "Real skin with visible pores" |
| G5 sem tom quente | OK | "no warm orange color cast" |
| G6 sem texto | OK | "no captions" |
| G7 bandeira | OK | "small American flag" |
| G8 boca no K de fala | OK | "caught mid-sentence" |
'''

BASE = {
    "scene": "His kitchen with a small American flag on the shelf.",
    "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window.",
    "state": "Start frame: he is caught mid-sentence.",
    "realism": "Real skin with visible pores, everything in sharp focus.",
    "negative": "no captions, no warm orange color cast, no blur",
}

# O K01 que falhou: forma generica, proximidade so em adjetivo, camera sem lente, props inventados.
K_ERRADO = dict(BASE, **{
    "prop": "A clear transparent plastic teaching model of a digestive tube: one long clear tube folded back and "
            "forth in tight loops. On the counter at the side: a raw chicken drumstick and a cup of yogurt.",
    "posture": "He crouches and leans in behind the teaching model.",
    "composition": "The teaching model fills the middle and lower part of the frame, very close to the lens, "
                   "large in frame, much closer to the camera than his face.",
    "camera": "phone camera low, at counter height, very close to the model, slight upward angle",
})

K_CERTO = dict(BASE, **{
    "prop": "An anatomical teaching model: a thick outer tube frames the sides like an upside-down U, a short "
            "funnel neck opens at the top center.",
    "posture": "He crouches low behind the counter.",
    "composition": "Taken with the lens only a few inches from the model: it fills the lower sixty percent of the "
                   "frame. The counter around the model is empty.",
    "camera": "phone lying almost flat on the counter, ultra-wide 0.5x lens pointing slightly upward",
})


class FichaFrame(unittest.TestCase):
    def validar(self, k, ficha=FICHA, nome="producao_nova"):
        with tempfile.TemporaryDirectory() as d:
            pasta = Path(d) / nome
            pasta.mkdir()
            (pasta / "frame.png").write_bytes(b"x")
            if ficha is not None:
                (pasta / "FICHA_FRAMES.md").write_text(ficha, encoding="utf-8")
            with mock.patch.object(ff, "legado", return_value={"producao_velha"}):
                return ff.validar_ficha(str(pasta), {"PROMPTS_A.md": {"K01": json.dumps(k)}})

    def falhas(self, issues):
        return [m for nivel, _, m, _ in issues if nivel == "FALHA"]

    def test_k01_errado_de_2026_09_25_reprova(self):
        f = " ".join(self.falhas(self.validar(K_ERRADO)))
        self.assertIn("upside-down U", f)          # forma generica
        self.assertIn("QUANTO do quadro", f)        # proximidade so em adjetivo
        self.assertIn("distancia", f)
        self.assertIn("lente e a altura", f)        # camera sem lente
        self.assertIn("The counter around the model is empty", f)   # props inventados

    def test_k01_pela_ficha_passa(self):
        self.assertEqual(self.falhas(self.validar(K_CERTO)), [])

    def test_sem_ficha_reprova(self):
        self.assertTrue(any("nao existe" in m for m in self.falhas(self.validar(K_CERTO, ficha=None))))

    def test_item_obrigatorio_nao_pode_ser_na(self):
        ficha = FICHA.replace('| F2 quanto do quadro | OK | "fills the lower sixty percent of the frame" |',
                              "| F2 quanto do quadro | N/A | sem heroi |")
        self.assertTrue(any("nao pode ser N/A" in m for m in self.falhas(self.validar(K_CERTO, ficha))))

    def test_producao_legado_nao_e_cobrada(self):
        self.assertEqual(self.falhas(self.validar(K_ERRADO, ficha=None, nome="producao_velha")), [])


if __name__ == "__main__":
    unittest.main()
