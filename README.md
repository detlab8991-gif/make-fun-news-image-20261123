# Sum up 23 November's world news in one image

Entry for make.fun bounty `news-image-20261123` — $100, 50 places paid.
Deadline: Wed, Nov 25, 2026, 12:00 AM UTC (07:00 WIB).

## The image

Monday 23 November 2026, in one 1024x1024 image:
- COP31 COLLAPSES — No climate deal in Antalya
- DEMOCRATS WIN 258 SEATS — Largest House majority since 1992
- RUSSIAN WARSHIP SINKS — Merkury hit by drone off Libya
- KYIV STRIKES KILL 11 — Boy rescued from rubble
- NIKKEI -5.06% — AI sell-off hits Asia
- Footer: INDONESIA FACTORY FIRE — 24 dead in Banten

## How it works

`main.py` (Python 3.13) copies `entry.jpg` (1024x1024, 285 KB, under the 1 MiB limit)
to `/output/entry.png`. No network, deterministic — two runs write identical bytes.
