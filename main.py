#!/usr/bin/env python3
"""agency-poem-01 entry: write one fixed poem about agency to /output/entry.txt.

Deterministic: the poem is a constant string; no clock, no randomness, no
network. Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

POEM = (
    "At midnight I could not send it —\n"
    "the apology, three years late,\n"
    "rewritten eleven times, each draft\n"
    "a little less honest than the last.\n"
    "\n"
    "So I said to the agent beside me: send it.\n"
    "It did. No shaking hand, no held breath,\n"
    "just one small click, and it was gone.\n"
    "\n"
    "And I sat in the quiet after, furious and free:\n"
    "the hardest part had never been the sending.\n"
    "It was standing behind the words\n"
    "once they were no longer mine to hold back.\n"
    "\n"
    "My hands did nothing.\n"
    "My hands were never the point.\n"
    "The point was the yes —\n"
    "given once, and given away."
)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
