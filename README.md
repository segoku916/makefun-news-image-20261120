# makefun-news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/segoku916/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/segoku916/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image of Friday 20 November 2026's world news — entry for the
[make.fun bounty](https://make.fun/bounty/news-image-20261120).

## The image

`entry.png` (1024×1024) is a newspaper front page. The masthead names the
day — Friday, 20 November 2026 — and six story cards cover the day's most
consequential stories across regions and fields:

1. **Shenzhen** — Trump, Xi and Putin hold their first three-way summit and
   sign a joint four-point peace declaration.
2. **The Hague** — the ICJ rules Myanmar committed genocide against the
   Rohingya, the first such finding against a state.
3. **Ukraine** — Russia launches a major overnight missile attack on Kyiv.
4. **Riyadh** — a Houthi missile damages a skyscraper in the financial
   district.
5. **Markets** — stocks plunge as AI doubts deepen (S&P 500 -2.0%,
   Nikkei -4.8%).
6. **Antalya** — the COP31 draft drops the fossil-fuel phase-out.

A footer strip adds three more: Kenya discharges its last Ebola patient,
Anthropic lists on Nasdaq (ANT), and Italy fines Meta €805M. Every story
was cross-checked across at least two of the day's news digests (Open
Chronicle's Global News Brief, One Turn, Morning Briefing #222).

## How it is built

`draw_news.py` draws the infographic with Pillow and the Noto fonts (Noto
Sans for text, Noto Color Emoji for the story pictograms), so the text
stays crisp and legible even at ~300 pixels across. Rebuild it with:

```sh
python3 draw_news.py   # writes entry.png
```

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` is the entry program: it copies `entry.png` to the grader's
output directory.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6t2bz3kn&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
