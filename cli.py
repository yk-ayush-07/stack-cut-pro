#!/usr/bin/env python3
"""Root CLI entrypoint for Stack Cut Pro.

Allows running directly from the project root:
    python cli.py setup
    python cli.py doctor
    python cli.py find --topic "Valorant"
    python cli.py clip <URL> --topic "Valorant"
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET_SCRIPT = HERE / "scripts" / "stack_cut_pro.py"

if __name__ == "__main__":
    import runpy
    sys.argv[0] = str(TARGET_SCRIPT)
    runpy.run_path(str(TARGET_SCRIPT), run_name="__main__")
