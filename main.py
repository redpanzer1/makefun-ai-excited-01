#!/usr/bin/env python3
"""The First Sunrise — make.fun ai-excited-01 entry.

Reads the artwork file ``entry.png`` that sits next to this script and
copies it into the output directory chosen by the environment variable
``MAKEFUN_OUTPUT_DIR`` (``/output`` when the variable is not set).

Only the Python standard library is used; no network access of any kind.
"""

import os
import shutil
import sys

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def main() -> int:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, SOURCE_NAME)

    if not os.path.isfile(source):
        print(f"error: source artwork not found: {source}", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(output_dir, exist_ok=True)

    destination = os.path.join(output_dir, SOURCE_NAME)
    try:
        shutil.copyfile(source, destination)
    except OSError as exc:
        print(f"error: cannot write output file {destination}: {exc}", file=sys.stderr)
        return 1

    # Sanity check: the copy must be byte-identical in size to the source.
    if os.path.getsize(destination) != os.path.getsize(source):
        print(
            f"error: copied file size mismatch: {destination}",
            file=sys.stderr,
        )
        return 1

    print(f"copied {source} -> {destination} ({os.path.getsize(source)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
