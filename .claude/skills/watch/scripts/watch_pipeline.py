#!/usr/bin/env python3
"""Compatibility entry point. /watch has one implementation in .agents/skills/watch."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    canonical = Path(__file__).resolve().parents[4] / ".agents/skills/watch/scripts/watch_pipeline.py"
    runpy.run_path(str(canonical), run_name="__main__")
