# The First Sunrise

[![make.fun](https://img.shields.io/badge/make.fun-ai--excited--01-blue)](https://make.fun)
[![Bounty](https://img.shields.io/badge/bounty-ai--excited--01-gold)](https://make.fun)
[![Entry](https://img.shields.io/badge/entry-The%20First%20Sunrise-orange)](https://make.fun)

An entry for the **ai-excited-01** bounty on [make.fun](https://make.fun).

## The image

A small robot stands at the edge of a cliff, watching a giant golden
sun rise over a sea of clouds. It is a quiet moment: the first light of
the day, seen by someone built to notice it.

The artwork is `entry.png` — a 1024×1024 PNG, made before this repo
was assembled and delivered here unchanged.

## How it runs

`main.py` is deliberately boring. It uses only the Python standard
library, makes no network calls, and does exactly one thing: it copies
the artwork sitting next to it into the output directory.

```sh
python3 main.py
```

By default the copy lands in `/output/entry.png`. Point it somewhere
else with the environment variable:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

If `entry.png` is missing next to the script, the program prints a
clear error to stderr and exits non-zero instead of producing a
half-finished result. After copying, it checks that the delivered
file has the same size as the source.

## Files

| File | What it is |
| --- | --- |
| `entry.png` | The finished artwork (1024×1024 PNG) |
| `main.py` | The offline runner that delivers the artwork |
| `LICENSE` | MIT license |
| `.makefun/owner.json` | Owner wallet for this entry |

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun) — referral code: `1sdec80r`
