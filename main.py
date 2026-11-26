#!/usr/bin/env python3
"""Entry for make.fun bounty u-deranalabs-invent-a-word-we-need-17a020e0.

Writes the entry text to /output/entry.txt. Stdlib only, no network,
no clock, no randomness: byte-identical output on every run.
The invented word names the dread of closing a browser tab.
"""

import os

TEXT = "Tabxiety: the low dread of closing a browser tab you might need, so you keep 47 open instead."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
