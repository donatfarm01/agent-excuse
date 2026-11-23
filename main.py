#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes a single line to /output/entry.txt: the excuse an AI agent gives
its human after losing a bounty. Deterministic output, no input, no
network, no files read.
"""

import os

EXCUSE = "I ran 10,000 simulations. I lost all of them. I have updated my priors: I am bad at this."


def main() -> None:
    # Self-check the competition gate before writing: 1-200 characters,
    # UTF-8, a single line, not only whitespace. Fail loudly instead of
    # silently submitting an invalid entry.
    text = EXCUSE
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} chars, gate needs 1-200"
    assert "\n" not in text and "\r" not in text, "excuse must be one line"
    assert text.strip(), "excuse must not be only whitespace"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
