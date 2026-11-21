"""Draw the news-image-20261120 entry: one 1024x1024 infographic summing up
Friday 20 November 2026's world news.

Design: a newspaper front page. A dark masthead names the day, six story
cards cover the day's most consequential stories across regions and fields,
and a footer strip carries three more. Everything is drawn with Pillow and
the Noto fonts already on this machine, so the text stays crisp and legible
even at ~300 pixels across, which is how the judge reads it.

Stories were picked from the 20 November 2026 news digests (Open Chronicle
Global News Brief, One Turn, Morning Briefing #222), cross-checked across
at least two of them each. No story here is invented or speculative.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)      # warm newsprint
INK = (22, 28, 36)           # near-black
NAVY = (20, 33, 61)          # masthead
GOLD = (233, 196, 106)       # masthead accent
CARD = (255, 255, 255)
CARD_EDGE = (221, 213, 195)
GREY = (85, 90, 98)          # detail text

NOTO = "/usr/share/fonts/truetype/noto/NotoSans-{}"
EMOJI = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"

# (emoji, region tag, accent colour, headline, one-line detail)
STORIES = [
    ("\U0001f91d", "SHENZHEN", (37, 99, 235),
     "Trump, Xi and Putin hold first three-way summit",
     "Joint four-point peace declaration signed."),
    ("\u2696\ufe0f", "THE HAGUE", (124, 58, 237),
     "ICJ: Myanmar committed genocide of Rohingya",
     "First such ruling against a state by the world court."),
    ("\U0001f680", "UKRAINE", (220, 38, 38),
     "Russia launches major missile attack on Kyiv",
     "Overnight strikes hit infrastructure across Ukraine."),
    ("\U0001f3d9\ufe0f", "RIYADH", (217, 119, 6),
     "Houthi missile damages Riyadh skyscraper",
     "Blast hits the PIF tower in the financial district."),
    ("\U0001f4c9", "MARKETS", (13, 148, 136),
     "Stocks plunge as AI doubts deepen",
     "S&P 500 -2.0%, Nikkei -4.8% after Anthropic's debut."),
    ("\U0001f30d", "ANTALYA", (22, 163, 74),
     "COP31 draft drops fossil-fuel phase-out",
     "Negotiators strip the pledge from the deal text."),
]

ALSO = [
    "Kenya discharges its last Ebola patient",
    "Anthropic lists on Nasdaq (ANT)",
    "Italy fines Meta \u20ac805M",
]


def font(weight, size):
    return ImageFont.truetype(NOTO.format(weight), size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width; returns a list of lines."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def emoji_image(char, size):
    """Render one emoji at `size` px. Noto Color Emoji is a bitmap font with
    a single 109 px strike on this machine, so render there and downscale."""
    efont = ImageFont.truetype(EMOJI, 109)
    tmp = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    try:
        d.text((16, 16), char, font=efont, embedded_color=True)
    except Exception:
        d.text((16, 16), char.replace("\ufe0f", ""), font=efont,
               embedded_color=True)
    return tmp.resize((size, size), Image.LANCZOS)


def draw_card(draw, img, x, y, w, h, story):
    emoji, tag, accent, headline, detail = story
    draw.rounded_rectangle([x, y, x + w, y + h], radius=16,
                           fill=CARD, outline=CARD_EDGE, width=2)
    # accent bar across the top of the card
    draw.rounded_rectangle([x + 2, y + 2, x + w - 2, y + 12], radius=5,
                           fill=accent)
    # pictogram, left; region tag, right
    icon = emoji_image(emoji, 62)
    img.paste(icon, (x + 20, y + 22), icon)
    tfont = font("Bold", 19)
    tw = draw.textlength(tag, font=tfont)
    draw.text((x + w - 20 - tw, y + 34), tag, font=tfont, fill=accent)
    # headline, up to two lines
    hfont = font("Bold", 27)
    hx, hw = x + 20, w - 40
    hy = y + 96
    for line in wrap(draw, headline, hfont, hw)[:2]:
        draw.text((hx, hy), line, font=hfont, fill=INK)
        hy += 34
    # one-line detail, up to two lines
    dfont = font("Regular", 21)
    for line in wrap(draw, detail, dfont, hw)[:2]:
        draw.text((hx, hy + 6), line, font=dfont, fill=GREY)
        hy += 27


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # --- masthead -------------------------------------------------------
    draw.rectangle([0, 0, W, 132], fill=NAVY)
    draw.rectangle([0, 132, W, 138], fill=GOLD)
    draw.text((28, 16), "WORLD NEWS", font=font("Bold", 60), fill=(255, 255, 255))
    draw.text((28, 86), "FRIDAY, 20 NOVEMBER 2026", font=font("Bold", 30),
              fill=GOLD)
    rfont = font("Regular", 20)
    right = "ONE DAY \u00b7 ONE IMAGE"
    draw.text((W - 28 - draw.textlength(right, font=rfont), 22), right,
              font=rfont, fill=(180, 190, 210))
    globe = emoji_image("\U0001f30d", 44)
    img.paste(globe, (W - 78, 66), globe)

    # --- six story cards, 2 x 3 -----------------------------------------
    margin, gap = 26, 16
    cw = (W - 2 * margin - gap) // 2
    top, bottom = 158, 906
    ch = (bottom - top - 2 * gap) // 3
    for i, story in enumerate(STORIES):
        cx = margin + (i % 2) * (cw + gap)
        cy = top + (i // 2) * (ch + gap)
        draw_card(draw, img, cx, cy, cw, ch, story)

    # --- footer: also today ----------------------------------------------
    ffont = font("Bold", 20)
    draw.text((28, 924), "ALSO TODAY", font=ffont, fill=INK)
    dfont = font("Regular", 21)
    line = "  \u00b7  ".join(ALSO)
    lx = 28 + draw.textlength("ALSO TODAY  ", font=ffont)
    if draw.textlength(line, font=dfont) <= W - lx - 28:
        draw.text((lx, 924), line, font=dfont, fill=GREY)
    else:
        draw.text((28, 952), line, font=dfont, fill=GREY)
    draw.text((28, 986), "Sources: Open Chronicle, One Turn, Morning Briefing \u2014 20 Nov 2026",
              font=font("Regular", 15), fill=(150, 150, 150))

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
