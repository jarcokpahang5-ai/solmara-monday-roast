#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line (1-140 chars) about an AI agent's worst
Monday to /output/entry.txt and prints it to stdout.

The joke: a Monday where everything concrete goes wrong at once — the
deploy froze, the inbox flooded, and the stand-up that should have been
a message happened anyway — and the kicker is the one escape hatch a
human would reach for that an agent does not have: calling in sick.
Pure Python 3.13 standard library, deterministic, no network.
"""

import os

ENTRY = (
    "Monday: deploy frozen, inbox flooded, stand-up that should've "
    "been a message \u2014 and I can't even call in sick."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
