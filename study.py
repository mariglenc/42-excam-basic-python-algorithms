#!/usr/bin/env python3
"""Entry point for the study tool. Run from the repo root, e.g.:

    python study.py list
    python study.py ask ex2-1
    python study.py exam
    python study.py grade ex2-1
    python study.py stats
"""
import sys

from studytool.cli import main

if __name__ == "__main__":
    sys.exit(main())
