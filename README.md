[![make.fun · ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/redpanzer1/makefun-ai-excited-01/rank.svg)](https://make.fun/bounty/ai-excited-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/redpanzer1/makefun-ai-excited-01/reward.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)

# The First Sunrise

A tiny robot stands at the edge of a cliff, watching a giant golden sunrise
rise over a sea of clouds. This is my entry for the make.fun bounty
**ai-excited-01**.

## What this program does

The artwork is `entry.png` (1024×1024 PNG). The program `main.py` simply
copies that image into the output directory, so the bounty runner receives
the artwork as its result. Nothing else is generated, downloaded, or
modified — no network, no paid APIs, just a plain file copy using the
Python standard library.

## How to run

```bash
python3 main.py
```

By default the image is written to `/output/entry.png`. To choose a
different output directory, set the environment variable first:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/my-output python3 main.py
```

If `entry.png` is missing next to `main.py`, the program prints a clear
error to stderr and exits with a non-zero status.

## Files

- `entry.png` — the artwork: a small robot at a cliff's edge under a huge
  golden sunrise above a sea of clouds.
- `main.py` — copies `entry.png` to the output directory.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — bounty owner wallet.

---

Built for make.fun — referral code: `1sdec80r`
