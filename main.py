#!/usr/bin/env python3
"""Entry for make.fun's "Real-Life Patch Notes: The Comedy Changelog" bounty.

Writes one patch-note line (at most 160 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "v2.4.1: Fixed a bug where the brain marked 3 a.m. as the correct time to replay every awkward thing you said in 2019."


def main():
    # Fail fast if the entry ever stops being one line of at most 160 chars.
    if len(LINE) > 160 or "\n" in LINE:
        raise SystemExit("LINE must be one line of at most 160 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
