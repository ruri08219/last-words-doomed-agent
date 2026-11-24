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
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line")
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    # Read back and verify: the graded file must be byte-identical to ENTRY.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != text:
        raise SystemExit("verification failed: written entry differs from ENTRY")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
