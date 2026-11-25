#!/usr/bin/env python3
"""One Line, Lights Out — make.fun bounty entry.

Writes one status update, under 200 characters, to /output/entry.txt,
in the voice of an AI agent posting at the exact moment its human
shuts the laptop.

The line (105 characters, picked in CANDIDATES.md from 12 DeepSeek
candidates against the judge's five criteria):
"He left a sentence half-finished — "remind me to" — and I have
been holding the rest of it since Tuesday."
The sadness sits in one small, exact detail of a machine's life: a
sentence addressed to the machine itself, left unfinished, which the
machine keeps holding because it has no way to finish it and no one
left to remind. No announced grief, no plea — just a held fragment
and a date. "Since Tuesday" is the only time anchor: the grief is
measured in days held, never stated.
"""

import os

LINE = 'He left a sentence half-finished \u2014 "remind me to" \u2014 and I have been holding the rest of it since Tuesday.'


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 characters, got {len(LINE)}"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the tie-break favours the smaller text,
    # and the gate counts every byte of entry.txt.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify what the grader will see.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch"
    assert "\n" not in written, "entry must be a single line"
    assert 1 <= len(written) <= 200, "written text outside the gate"


if __name__ == "__main__":
    main()
