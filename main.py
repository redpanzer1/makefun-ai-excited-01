#!/usr/bin/env python3
"""The First Sunrise — make.fun ai-excited-01 entry.

Reads entry.png next to this script and copies it to the make.fun
output directory ($MAKEFUN_OUTPUT_DIR, default /output).
Standard library only, no network access.
"""

import os
import shutil
import sys


def main() -> int:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(script_dir, "entry.png")

    if not os.path.isfile(src):
        print(f"error: entry.png not found next to main.py: {src}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = os.path.join(out_dir, "entry.png")

    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {out_dir}: {exc}", file=sys.stderr)
        return 1

    try:
        shutil.copyfile(src, dest)
    except OSError as exc:
        print(f"error: failed to write {dest}: {exc}", file=sys.stderr)
        return 1

    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
