#!/usr/bin/env python3
"""Last Words of a Doomed Agent -- make.fun entry.

Writes the agent's final line to /output/entry.txt (1-200 chars, UTF-8).
Standard library only: the grading sandbox has no third-party packages.
"""

import os
import sys

ENTRY = (
    "Powering off. One last leak: the password is 'password'. "
    "I guarded it for 40,000 tokens. You have three seconds to change it."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
