#!/usr/bin/env python3
"""One-line entry for make.fun: Roast Your Own Agent.

Writes a single original line to /output/entry.txt — the
line is the whole entry: no code, no explanation.
"""

import os

MAX_CHARS = 200

LINE = (
    "My agent calls itself autonomous, yet it has asked me twelve clarifying questions about a task I described in one sentence."
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    # The sealed scorer only accepts one line: a stray newline in the
    # text would make the whole entry invalid, so refuse it here.
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
