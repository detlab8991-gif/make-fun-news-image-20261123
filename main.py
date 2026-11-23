#!/usr/bin/env python3
"""make.fun bounty: Sum up 23 November's world news in one image.
Simplest allowed program: copy the image held in this repo to /output/entry.png.
No network, deterministic: two runs write identical bytes.
"""
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.jpg"
OUT = Path("/output/entry.png")

def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)

if __name__ == "__main__":
    main()
