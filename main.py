"""makefun-ai-excited-01: The First Sunrise.

Copies the entry image (entry.png, next to this file) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output).

Standard library only. No network access: it only copies a local file.
Deterministic: the output bytes are identical to the source bytes, so
re-running the program always produces the same SHA-256.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print(f"error: entry image not found: {src}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
