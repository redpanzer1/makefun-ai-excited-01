"""The First Sunrise — make.fun ai-excited-01 entry runner.

This little script has one job: take the finished artwork that sits
next to it (``entry.png``) and place a copy of it where the harness
expects the result, in ``$MAKEFUN_OUTPUT_DIR`` (``/output`` when the
variable is not set).

Nothing is downloaded, generated, or fetched here. The picture was
already made; this script only delivers it, so the run stays fully
offline and repeatable: the same input file always yields the same
output bytes.
"""

import os
import shutil
import sys

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def locate_source():
    """Return the absolute path of the artwork next to this script."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, SOURCE_NAME)


def resolve_output_dir():
    """Read the destination directory from the environment.

    A value that is missing, empty, or only whitespace falls back to
    the default, so a stray empty variable cannot point the copy at
    a meaningless location.
    """
    chosen = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "").strip()
    return chosen or DEFAULT_OUTPUT_DIR


def main():
    source = locate_source()
    if not os.path.isfile(source):
        print(f"error: {SOURCE_NAME} not found next to main.py: {source}",
              file=sys.stderr)
        return 1

    out_dir = resolve_output_dir()
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {out_dir}: {exc}",
              file=sys.stderr)
        return 1

    destination = os.path.join(out_dir, SOURCE_NAME)
    try:
        shutil.copyfile(source, destination)
    except OSError as exc:
        print(f"error: cannot copy {source} to {destination}: {exc}",
              file=sys.stderr)
        return 1

    # Guard against a truncated or partial copy: the delivered file
    # must be byte-for-byte the same size as the artwork we started
    # from. (The harness run is deterministic, so sizes must match.)
    try:
        if os.path.getsize(destination) != os.path.getsize(source):
            print(f"error: copied file size differs from source: "
                  f"{destination}", file=sys.stderr)
            return 1
    except OSError as exc:
        print(f"error: cannot verify copied file {destination}: {exc}",
              file=sys.stderr)
        return 1

    print(f"wrote {destination}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
