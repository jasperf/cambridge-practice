#!/usr/bin/env python3
"""Generate the four Human Biology diagram SVGs (same house style as the delivery-vans SVG).

Writes science-diagram-{cell-to-gene,mitosis-meiosis,xx-xy,mother-fetus}.svg.

    python3 scripts/build_human_biology_diagrams.py            # into s2/science-formula-sheets/svg/
    python3 scripts/build_human_biology_diagrams.py some/dir   # somewhere else, e.g. to preview

Dependency-free. Preview a still with `rsvg-convert -w 900 file.svg -o file.png`
(rsvg ignores animation); open the SVG in a browser to see it move.
"""
import math, sys, os
from xml.sax.saxutils import escape

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "s2", "science-formula-sheets", "svg")
W = 1080
NAVY = "#14213D"; MUTED = "#5B6478"; CREAM = "#FBF5E9"; EDGE = "#EADFCB"
GREEN = "#2F9E44"; MUM = "#D6336C"; DAD = "#1C6DD0"; AMBER = "#F5A623"; AMBER_D = "#B5650A"
FONT = "Montserrat,Helvetica,Arial,DejaVu Sans,sans-serif"


def t(x, y, s, size=16, fill=NAVY, weight=None, anchor=None, extra=""):
    a = f' font-weight="{weight}"' if weight else ""
    a += f' text-anchor="{anchor}"' if anchor else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}"{a}{extra}>{escape(s)}</text>'


def wrap(x, y, s, width, size=16, fill=NAVY, weight=None, lh=None, anchor=None):
    """Wrap text into tspans. width in px; ~0.56em per char for Montserrat-ish fonts."""
    maxc = int(width / (size * 0.56))
    lh = lh or round(size * 1.4)
    lines, cur = [], ""
    for w in s.split():
        if len(cur) + len(w) + 1 > maxc and cur:
            lines.append(cur); cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    a = f' font-weight="{weight}"' if weight else ""
    a += f' text-anchor="{anchor}"' if anchor else ""
    spans = "".join(f'<tspan x="{x}" dy="{0 if i == 0 else lh}">{escape(l)}</tspan>' for i, l in enumerate(lines))
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}"{a}>{spans}</text>', len(lines) * lh


def head(h, eyebrow, title, sub):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" font-family="{FONT}">\n'
            f'<rect width="{W}" height="{h}" fill="{CREAM}"/><rect width="14" height="{h}" fill="{GREEN}"/>\n'
            + t(56, 62, eyebrow, 20, GREEN, 700, extra=' letter-spacing="2"') + "\n"
            + t(56, 108, title, 40, NAVY, 800) + "\n"
            + t(56, 136, sub, 20, MUTED) + "\n")


def panel(x, y, w, h, title=None):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#fff" stroke="{EDGE}"/>'
    if title:
        s += t(x + 28, y + 38, title, 20, NAVY, 800)
    return s + "\n"


def rod(cx, cy, length, color, angle=0, width=12):
    """An unreplicated chromosome: a rounded rod."""
    return (f'<rect x="{cx - width / 2}" y="{cy - length / 2}" width="{width}" height="{length}" rx="{width / 2}" '
            f'fill="{color}" transform="rotate({angle} {cx} {cy})"/>')


# ---------------------------------------------------------------- 1. Cell to gene
def cell_to_gene():
    H = 1130
    o = [head(H, "HUMAN BIOLOGY · WHERE GENES LIVE", "From Cell to Gene",
              "Zoom in: cell, nucleus, chromosome, DNA. A gene is one short section of the DNA.")]
    o.append(panel(56, 166, 968, 520, "Zoom in, step by step"))
    cxs = [190, 540, 890]; cy = 330; R = 100
    # zoom connectors
    for a, b in ((0, 1), (1, 2)):
        x1 = cxs[a] + R + 10; x2 = cxs[b] - R - 10
        o.append(f'<line x1="{x1}" y1="{cy}" x2="{x2 - 10}" y2="{cy}" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 6"/>'
                 f'<polygon points="{x2},{cy} {x2 - 14},{cy - 8} {x2 - 14},{cy + 8}" fill="{MUTED}"/>')
        o.append(t((x1 + x2) // 2, cy - 14, "zoom in", 13, MUTED, 700, "middle"))
    # cell
    c = cxs[0]
    o.append(f'<circle cx="{c}" cy="{cy}" r="{R}" fill="#FFF0DB" stroke="#E8590C" stroke-width="3"/>')
    o.append(f'<ellipse cx="{c - 40}" cy="{cy + 40}" rx="14" ry="7" fill="#FFC078"/><ellipse cx="{c + 50}" cy="{cy - 45}" rx="12" ry="6" fill="#FFC078"/>'
             f'<ellipse cx="{c + 45}" cy="{cy + 50}" rx="10" ry="6" fill="#FFC078"/>')
    o.append(f'<circle cx="{c + 5}" cy="{cy - 5}" r="34" fill="#D0BFFF" stroke="#7048E8" stroke-width="3">'
             f'<animate attributeName="stroke-width" values="3;7;3" dur="2s" repeatCount="indefinite"/></circle>')
    o.append(f'<circle cx="{c + 12}" cy="{cy - 10}" r="9" fill="#9775FA"/>')
    # nucleus
    c = cxs[1]
    o.append(f'<circle cx="{c}" cy="{cy}" r="{R}" fill="#E5DBFF" stroke="#7048E8" stroke-width="3"/>')
    spots = [(-50, -30, 40, 30, DAD), (-20, -50, 34, -25, MUM), (25, -40, 44, 60, DAD), (50, 5, 30, -10, MUM),
             (-55, 25, 30, 75, MUM), (-15, 45, 40, -55, DAD), (30, 45, 26, 20, MUM), (5, 0, 46, 10, DAD)]
    for dx, dy, L, ang, col in spots:
        o.append(rod(c + dx, cy + dy, L, col, ang, 9))
    o.append(f'<circle cx="{c + 5}" cy="{cy}" r="30" fill="none" stroke="{AMBER}" stroke-width="4">'
             f'<animate attributeName="opacity" values="0.2;1;0.2" dur="2s" repeatCount="indefinite"/></circle>')
    # chromosome (replicated X shape)
    c = cxs[2]
    o.append(f'<circle cx="{c}" cy="{cy}" r="{R}" fill="#E7F5FF" stroke="{DAD}" stroke-width="3"/>')
    for ang in (-16, 16):
        o.append(f'<rect x="{c - 13}" y="{cy - 78}" width="26" height="156" rx="13" fill="{DAD}" transform="rotate({ang} {c} {cy})"/>')
        for k in (-55, -30, 25, 50):
            o.append(f'<rect x="{c - 13}" y="{cy + k}" width="26" height="5" fill="#fff" opacity="0.45" transform="rotate({ang} {c} {cy})"/>')
    o.append(f'<rect x="{c - 13}" y="{cy - 50}" width="26" height="16" fill="{AMBER}" stroke="{AMBER_D}" stroke-width="2" transform="rotate(-16 {c} {cy})">'
             f'<animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/></rect>')
    o.append(f'<circle cx="{c}" cy="{cy}" r="9" fill="{NAVY}"/>')
    labels = [("Cell", "The nucleus is the control centre"),
              ("Nucleus", "Holds 46 chromosomes"),
              ("Chromosome", "One long, coiled DNA molecule")]
    for (big, small), cx in zip(labels, cxs):
        o.append(t(cx, cy + R + 36, big, 22, NAVY, 800, "middle"))
        o.append(t(cx, cy + R + 60, small, 15, MUTED, None, "middle"))
    # zoom fan from chromosome to helix band
    by = 580; P = 120; A = 30; x0, x1 = 96, 984
    o.append(t(x0, by - 56, "Unwind a chromosome and you get DNA:", 16, NAVY, 700))
    # helix band (clip + scrolling group = looks like it turns)
    o.append(f'<defs><clipPath id="band"><rect x="{x0}" y="{by - 46}" width="{x1 - x0}" height="92" rx="10"/></clipPath></defs>')
    o.append(f'<rect x="{x0}" y="{by - 46}" width="{x1 - x0}" height="92" rx="10" fill="#F8F9FB" stroke="{EDGE}"/>')
    gx0, gx1 = 600, 760
    o.append(f'<rect x="{gx0}" y="{by - 46}" width="{gx1 - gx0}" height="92" fill="{AMBER}" opacity="0.25"/>')
    o.append(f'<g clip-path="url(#band)"><g>')
    base_cols = ["#2F9E44", "#E8590C", "#7048E8", "#1098AD"]
    xs = range(x0 - P, x1 + P + 1, 4)
    def strand(phase):
        return " ".join(f'{"M" if i == 0 else "L"}{x},{by + A * math.sin(2 * math.pi * (x - x0) / P + phase):.1f}' for i, x in enumerate(xs))
    k = 0
    for x in range(x0 - P, x1 + P + 1, P // 8):
        ya = by + A * math.sin(2 * math.pi * (x - x0) / P); yb = by + A * math.sin(2 * math.pi * (x - x0) / P + math.pi)
        col = base_cols[(k * 7 + k // 3) % 4]; k += 1
        o.append(f'<line x1="{x}" y1="{ya:.1f}" x2="{x}" y2="{yb:.1f}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>')
    o.append(f'<path d="{strand(0)}" fill="none" stroke="{NAVY}" stroke-width="7"/>')
    o.append(f'<path d="{strand(math.pi)}" fill="none" stroke="#868E96" stroke-width="7"/>')
    o.append(f'<animateTransform attributeName="transform" type="translate" from="0 0" to="-{P} 0" dur="4s" repeatCount="indefinite"/></g></g>')
    o.append(f'<rect x="{gx0}" y="{by - 46}" width="{gx1 - gx0}" height="92" fill="none" stroke="{AMBER_D}" stroke-width="3" stroke-dasharray="8 5"/>')
    o.append(t((gx0 + gx1) // 2, by + 72, "one gene", 18, AMBER_D, 800, "middle"))
    o.append(t((gx0 + gx1) // 2, by + 92, "e.g. for eye colour", 14, MUTED, None, "middle"))
    o.append(t(x0 + 6, by + 72, "two strands twisted like a ladder: the double helix", 15, MUTED))
    # fact cards
    cards = [
        ("DNA", "DeoxyriboNucleic Acid: the chemical chromosomes are made of. It holds the instructions for every characteristic."),
        ("Double helix", "Two strands twisted round each other like a spiral ladder. Watson and Crick worked out this shape in 1953."),
        ("46 = 23 pairs", "Every body cell has 46 chromosomes in 23 pairs. One of each pair came from Mum, the other from Dad."),
        ("Gene", "A short section of DNA that codes for one characteristic. Half your genes come from each parent, so you look like both but are not identical to either."),
    ]
    cw, ch = 472, 186
    for i, (h, body) in enumerate(cards):
        x = 56 + (i % 2) * (cw + 24); y = 710 + (i // 2) * (ch + 20)
        o.append(panel(x, y, cw, ch))
        o.append(f'<rect x="{x}" y="{y + 18}" width="6" height="{ch - 36}" rx="3" fill="{GREEN}"/>')
        o.append(t(x + 28, y + 44, h, 22, NAVY, 800))
        w, _ = wrap(x + 28, y + 76, body, cw - 56, 16, MUTED, lh=24)
        o.append(w)
    # karyotype strip in card 3: 23 tiny pairs
    x = 56 + 0 * (cw + 24); y = 710 + ch + 20
    for i in range(23):
        px = x + 30 + i * 19; L = 30 - i * 0.8
        o.append(rod(px, y + ch - 30, L, DAD, 0, 6) + rod(px + 8, y + ch - 30, L, MUM, 0, 6))
    o.append("</svg>\n")
    return "\n".join(o)


# ---------------------------------------------------------------- 2. Mitosis vs meiosis
def chromos(cx, cy, set_):
    """set_: list of (length, colour). Laid out side by side."""
    n = len(set_); s = []
    for i, (L, col) in enumerate(set_):
        px = cx + (i - (n - 1) / 2) * 18
        s.append(rod(px, cy, L, col, 0, 10))
    return "".join(s)


def cell(cx, cy, r, set_, fill="#FFF4E6", stroke="#E8590C"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="3"/>' + chromos(cx, cy, set_)


def arrow(x1, y1, x2, y2, col=MUTED):
    ang = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - 14 * math.cos(ang), y2 - 14 * math.sin(ang)
    p1 = (hx + 7 * math.sin(ang), hy - 7 * math.cos(ang)); p2 = (hx - 7 * math.sin(ang), hy + 7 * math.cos(ang))
    return (f'<line x1="{x1}" y1="{y1}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{col}" stroke-width="3"/>'
            f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{col}"/>')


def stage(content, show_from, dur=9):
    """Visible at t=0 (good for stills); during the loop hides then reappears in order."""
    a = 0.66; b = 0.70
    return (f'<g>{content}<animate attributeName="opacity" values="1;1;0;0;1;1" '
            f'keyTimes="0;{a};{b};{show_from};{show_from + 0.04:.2f};1" dur="{dur}s" repeatCount="indefinite"/></g>')


def mitosis_meiosis():
    H = 1180
    o = [head(H, "HUMAN BIOLOGY · CELL DIVISION", "Mitosis and Meiosis",
              "Two ways a cell divides. Count the chromosomes in each new cell.")]
    LB, SB, LP, SP = (52, DAD), (30, DAD), (52, MUM), (30, MUM)
    full = [LB, LP, SB, SP]
    o.append(panel(56, 166, 476, 640))
    o.append(panel(548, 166, 476, 640))
    # mitosis
    mx = 294
    o.append(t(mx, 210, "Mitosis", 30, GREEN, 800, "middle"))
    o.append(t(mx, 236, "1 division → 2 cells", 17, NAVY, 700, "middle"))
    o.append(cell(mx, 330, 66, full))
    o.append(stage(arrow(mx - 20, 400, mx - 90, 470) + arrow(mx + 20, 400, mx + 90, 470)
                   + cell(mx - 110, 540, 62, full) + cell(mx + 110, 540, 62, full), 0.78))
    o.append(t(mx, 640, "2 cells, identical to the parent", 17, NAVY, 700, "middle"))
    o.append(t(mx, 666, "4 chromosomes → 4 in each cell", 16, MUTED, None, "middle"))
    o.append(t(mx, 692, "diploid (2n) · 46 in a human cell", 16, MUTED, None, "middle"))
    o.append(f'<rect x="96" y="716" width="396" height="66" rx="10" fill="#EBFBEE"/>')
    o.append(t(mx, 744, "Used for growth and repair", 17, GREEN, 800, "middle"))
    o.append(t(mx, 768, "and to grow from zygote to baby", 15, MUTED, None, "middle"))
    # meiosis
    ex = 786
    o.append(t(ex, 210, "Meiosis", 30, MUM, 800, "middle"))
    o.append(t(ex, 236, "2 divisions → 4 cells", 17, NAVY, 700, "middle"))
    o.append(cell(ex, 310, 56, full))
    mid = stage(arrow(ex - 20, 370, ex - 80, 400) + arrow(ex + 20, 370, ex + 80, 400)
                + cell(ex - 100, 438, 42, [LB, SP]) + cell(ex + 100, 438, 42, [LP, SB]), 0.76)
    o.append(mid)
    combos = [[LB, SP], [LB, SP], [LP, SB], [LP, SB]]
    xs = [ex - 165, ex - 55, ex + 55, ex + 165]
    low = ""
    for i, (x, cset) in enumerate(zip(xs, combos)):
        parent = ex - 100 if i < 2 else ex + 100
        low += arrow(parent, 482, x, 520) + cell(x, 562, 40, cset, "#FFF0F6", MUM)
    o.append(stage(low, 0.86))
    o.append(t(ex, 640, "4 cells, all different", 17, NAVY, 700, "middle"))
    o.append(t(ex, 666, "4 chromosomes → 2 in each cell (half)", 16, MUTED, None, "middle"))
    o.append(t(ex, 692, "haploid (n) · 23 in a human gamete", 16, MUTED, None, "middle"))
    o.append(f'<rect x="588" y="716" width="396" height="66" rx="10" fill="#FFF0F6"/>')
    o.append(t(ex, 744, "Used to make gametes", 17, MUM, 800, "middle"))
    o.append(t(ex, 768, "sperm in the testes, eggs in the ovaries", 15, MUTED, None, "middle"))
    # key
    o.append(rod(80, 830, 22, DAD, 90, 8) + t(100, 836, "from Dad", 14, MUTED))
    o.append(rod(200, 830, 22, MUM, 90, 8) + t(220, 836, "from Mum", 14, MUTED))
    o.append(t(320, 836, "This model cell has 4 chromosomes (2 pairs). A human body cell has 46 (23 pairs).", 14, MUTED))
    # fertilisation strip
    y0 = 860
    o.append(panel(56, y0, 968, 296, "Fertilisation puts the number back"))
    fy = y0 + 130
    # sperm swimming to egg
    o.append(f'<circle cx="610" cy="{fy}" r="58" fill="#FFF0F6" stroke="{MUM}" stroke-width="3"/>')
    o.append(t(610, fy + 6, "egg", 18, MUM, 800, "middle"))
    o.append(t(610, fy + 84, "egg: n = 23", 16, NAVY, 700, "middle"))
    sperm = (f'<g><ellipse cx="0" cy="0" rx="15" ry="10" fill="{DAD}"/>'
             f'<path fill="none" stroke="{DAD}" stroke-width="3" stroke-linecap="round" d="M-14,0 C-30,-10 -40,10 -56,0 S-80,-10 -92,0">'
             f'<animate attributeName="d" dur="0.5s" repeatCount="indefinite" values="M-14,0 C-30,-10 -40,10 -56,0 S-80,-10 -92,0;M-14,0 C-30,10 -40,-10 -56,0 S-80,10 -92,0;M-14,0 C-30,-10 -40,10 -56,0 S-80,-10 -92,0"/></path>'
             f'<animateMotion dur="9s" repeatCount="indefinite" keyTimes="0;0.5;1" keyPoints="0;1;1" calcMode="linear" path="M220,{fy} C330,{fy - 40} 420,{fy + 40} 545,{fy}"/></g>')
    o.append(t(250, fy + 84, "sperm: n = 23", 16, NAVY, 700, "middle"))
    o.append(sperm)
    o.append(t(408, fy + 84, "+", 30, NAVY, 800, "middle"))
    o.append(arrow(684, fy, 770, fy, NAVY))
    o.append(f'<circle cx="850" cy="{fy}" r="62" fill="#EBFBEE" stroke="{GREEN}" stroke-width="3"/>')
    o.append(t(850, fy - 2, "zygote", 18, GREEN, 800, "middle"))
    o.append(t(850, fy + 22, "46", 22, NAVY, 800, "middle"))
    o.append(t(850, fy + 84, "zygote: 2n = 46", 16, NAVY, 700, "middle"))
    w, _ = wrap(84, y0 + 250, "Without meiosis the zygote would get 46 + 46 = 92, and the number would double every generation. "
                "Other animals work the same way: cat 38 → gametes 19, horse 64 → 32, chimpanzee 48 → 24.", 920, 16, MUTED, lh=24)
    o.append(w)
    o.append("</svg>\n")
    return "\n".join(o)


# ---------------------------------------------------------------- 3. XX and XY
def xchrom(cx, cy, h, col):
    return (f'<g><rect x="{cx - 5}" y="{cy - h / 2}" width="10" height="{h}" rx="5" fill="{col}" transform="rotate(-22 {cx} {cy})"/>'
            f'<rect x="{cx - 5}" y="{cy - h / 2}" width="10" height="{h}" rx="5" fill="{col}" transform="rotate(22 {cx} {cy})"/></g>')


def ychrom(cx, cy, h, col):
    return (f'<g><rect x="{cx - 5}" y="{cy - h * 0.1}" width="10" height="{h * 0.6}" rx="5" fill="{col}"/>'
            f'<rect x="{cx - 5}" y="{cy - h * 0.45}" width="10" height="{h * 0.45}" rx="5" fill="{col}" transform="rotate(-30 {cx} {cy})"/>'
            f'<rect x="{cx - 5}" y="{cy - h * 0.45}" width="10" height="{h * 0.45}" rx="5" fill="{col}" transform="rotate(30 {cx} {cy})"/></g>')


def boy_or_girl():
    H = 1170
    o = [head(H, "HUMAN BIOLOGY · BOY OR GIRL?", "XX and XY",
              "Pair 23 decides. The egg always brings an X; the sperm brings an X or a Y.")]
    o.append(panel(56, 166, 968, 270, "23 pairs: 22 pairs of autosomes + 1 pair of sex chromosomes"))
    for row, (who, col, last) in enumerate((("Mum (female)", MUM, "XX"), ("Dad (male)", DAD, "XY"))):
        y = 260 + row * 92
        o.append(t(84, y + 6, who, 18, col, 800))
        for i in range(22):
            px = 250 + i * 28; L = 44 - i * 1.0
            o.append(rod(px, y, L, "#ADB5BD", 0, 6) + rod(px + 9, y, L, "#CED4DA", 0, 6))
        o.append(f'<rect x="878" y="{y - 36}" width="118" height="72" rx="12" fill="{"#FFF0F6" if row == 0 else "#E7F5FF"}" stroke="{col}" stroke-width="2"/>')
        o.append(xchrom(910, y, 46, col))
        o.append((xchrom if last == "XX" else ychrom)(962, y, 46 if last == "XX" else 34, col))
        o.append(t(937, y + 54, last, 18, col, 800, "middle"))
    o.append(t(250, 410, "pairs 1–22: autosomes (eye colour, hair, height …)", 14, MUTED))
    o.append(t(937, 426, "pair 23", 13, MUTED, 700, "middle"))
    # punnett
    py = 460
    o.append(panel(56, py, 560, 470, "Each baby: a 50 : 50 chance"))
    gx, gy, cs = 236, py + 110, 150
    o.append(t(gx + cs, gy - 46, "Dad's sperm", 16, DAD, 800, "middle"))
    o.append(t(gx - 66, gy + cs + 6, "Mum's eggs", 16, MUM, 800, "middle", ' transform="rotate(-90 %d %d)"' % (gx - 66, gy + cs)))
    for j, g in enumerate("XY"):
        o.append(t(gx + cs * j + cs // 2, gy - 14, g, 26, DAD, 800, "middle"))
    for i in range(2):
        o.append(t(gx - 24, gy + cs * i + cs // 2 + 9, "X", 26, MUM, 800, "middle"))
        for j, g in enumerate("XY"):
            girl = g == "X"
            fill = "#FFF0F6" if girl else "#E7F5FF"
            x = gx + cs * j; y = gy + cs * i
            o.append(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="{fill}" stroke="{NAVY}" stroke-width="2"/>')
            o.append(f'<text x="{x + cs // 2}" y="{y + 66}" font-size="32" font-weight="800" text-anchor="middle">'
                     f'<tspan fill="{MUM}">X</tspan><tspan fill="{MUM if girl else DAD}">{g}</tspan></text>')
            o.append(t(x + cs // 2, y + 102, "girl" if girl else "boy", 20, MUM if girl else DAD, 800, "middle"))
        # pulse Y column
    o.append(f'<rect x="{gx + cs}" y="{gy}" width="{cs}" height="{cs * 2}" fill="none" stroke="{AMBER}" stroke-width="5">'
             f'<animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite"/></rect>')
    o.append(t(336, py + 450, "2 girls : 2 boys = 50% each", 18, NAVY, 800, "middle"))
    # right: sperm decides
    o.append(panel(632, py, 392, 470, "The sperm decides"))
    ey = py + 250
    o.append(f'<circle cx="930" cy="{ey}" r="60" fill="#FFF0F6" stroke="{MUM}" stroke-width="3"/>')
    o.append(t(930, ey + 10, "X", 30, MUM, 800, "middle"))
    o.append(t(930, ey + 90, "every egg: X", 15, MUM, 800, "middle"))
    for k, (lab, yoff, delay) in enumerate((("X", -70, "0s"), ("Y", 70, "-3s"))):
        tail = "M-14,0 C-26,-8 -34,8 -46,0 S-64,-8 -74,0"
        tail2 = "M-14,0 C-26,8 -34,-8 -46,0 S-64,8 -74,0"
        o.append(f'<g><ellipse cx="0" cy="0" rx="16" ry="11" fill="{DAD}"/>'
                 f'<text x="0" y="5" font-size="14" font-weight="800" fill="#fff" text-anchor="middle">{lab}</text>'
                 f'<path fill="none" stroke="{DAD}" stroke-width="3" stroke-linecap="round" d="{tail}">'
                 f'<animate attributeName="d" dur="0.5s" repeatCount="indefinite" values="{tail};{tail2};{tail}"/></path>'
                 f'<animateMotion dur="6s" begin="{delay}" repeatCount="indefinite" keyTimes="0;0.5;1" keyPoints="0;1;1" calcMode="linear" '
                 f'path="M720,{ey + yoff} C770,{ey + yoff * 0.6} 820,{ey + yoff * 0.5} 858,{ey + yoff * 0.45:.0f}"/></g>')
    o.append(t(700, ey - 100, "sperm with X", 15, DAD, 800))
    o.append(t(700, ey + 120, "sperm with Y", 15, DAD, 800))
    w, _ = wrap(660, py + 72, "Half of Dad's sperm carry an X, half carry a Y. Mum can only give an X.", 340, 15, MUTED, lh=21)
    o.append(w)
    o.append(t(660, py + 410, "X sperm + X egg → XX girl", 16, MUM, 800))
    o.append(t(660, py + 436, "Y sperm + X egg → XY boy", 16, DAD, 800))
    # bottom notes
    by = 954
    o.append(panel(56, by, 968, 190, "Remember"))
    notes = [
        "Female = XX, male = XY. The Y chromosome is much smaller than the X.",
        "Eggs all carry X, so the egg can't decide. Sperm carry X or Y, so the father's sperm decides.",
        "Each fertilisation is a new 50 : 50 chance. Earlier children make no difference: no baby is ever 'due'.",
    ]
    for i, n in enumerate(notes):
        o.append(f'<circle cx="92" cy="{by + 78 + i * 38}" r="6" fill="{GREEN}"/>' + t(110, by + 84 + i * 38, n, 17, NAVY))
    o.append("</svg>\n")
    return "\n".join(o)


# ---------------------------------------------------------------- 4. Mother and fetus
def mother_fetus():
    H = 1300
    o = [head(H, "HUMAN BIOLOGY · PREGNANCY", "Mother and Fetus",
              "What Mum eats, drinks, smokes or takes reaches the baby through the placenta.")]
    o.append(panel(56, 166, 968, 640, "Inside the uterus (womb)"))
    ux, uy = 330, 470
    # uterus wall and fluid
    o.append(f'<ellipse cx="{ux}" cy="{uy}" rx="225" ry="245" fill="#FFC9C9" stroke="#C92A2A" stroke-width="3"/>')
    o.append(f'<ellipse cx="{ux}" cy="{uy + 5}" rx="190" ry="210" fill="#E7F5FF" stroke="#74C0FC" stroke-width="2"/>')
    # placenta on upper right inner wall
    plx, ply = 448, 322
    o.append(f'<ellipse cx="{plx}" cy="{ply}" rx="42" ry="78" fill="#A61E4D" transform="rotate(40 {plx} {ply})"/>')
    for k in range(5):
        o.append(f'<path d="M{plx - 20 + k * 10},{ply - 30 + k * 12} q8,6 0,14" stroke="#F783AC" stroke-width="2" fill="none"/>')
    # mother's blood vessel entering placenta from outside
    vessel = f"M640,214 C590,230 540,250 {plx + 30},{ply - 22}"
    o.append(f'<path d="{vessel}" stroke="#C92A2A" stroke-width="16" fill="none" stroke-linecap="round"/>')
    # fetus: curled
    fx, fy = 300, 470
    o.append(f'<ellipse cx="{fx + 10}" cy="{fy + 50}" rx="78" ry="98" fill="#FFD8A8" stroke="#D9480F" stroke-width="2" transform="rotate(-18 {fx + 10} {fy + 50})"/>')
    o.append(f'<circle cx="{fx - 30}" cy="{fy - 70}" r="66" fill="#FFD8A8" stroke="#D9480F" stroke-width="2"/>')
    o.append(f'<circle cx="{fx - 55}" cy="{fy - 80}" r="5" fill="{NAVY}"/>')
    o.append(f'<path d="M{fx - 62},{fy - 52} q8,6 16,0" stroke="#D9480F" stroke-width="2" fill="none"/>')
    # arm & leg
    o.append(f'<path d="M{fx - 10},{fy + 10} q-60,20 -70,-20" stroke="#FFC078" stroke-width="22" fill="none" stroke-linecap="round"/>')
    o.append(f'<path d="M{fx + 50},{fy + 110} q-40,50 -110,30" stroke="#FFC078" stroke-width="26" fill="none" stroke-linecap="round"/>')
    # umbilical cord from belly to placenta
    navel = (fx + 40, fy + 50)
    cord = f"M{plx - 20},{ply + 30} C{plx + 10},{ply + 120} {navel[0] + 80},{navel[1] - 40} {navel[0]},{navel[1]}"
    o.append(f'<path d="{cord}" stroke="#E64980" stroke-width="14" fill="none" stroke-linecap="round"/>')
    o.append(f'<path d="{cord}" stroke="#FCC2D7" stroke-width="4" fill="none" stroke-dasharray="4 10"/>')
    # moving particles: full route vessel->placenta->cord
    inward = f"M640,214 C590,230 540,250 {plx + 30},{ply - 22} L{plx - 20},{ply + 30} C{plx + 10},{ply + 120} {navel[0] + 80},{navel[1] - 40} {navel[0]},{navel[1]}"
    outward = f"M{navel[0]},{navel[1]} C{navel[0] + 80},{navel[1] - 40} {plx + 10},{ply + 120} {plx - 20},{ply + 30} L{plx + 30},{ply - 22} C540,250 590,230 640,214"
    def dots(path, col, n, dur, r=7, shape="c", off=0.0):
        s = ""
        for i in range(n):
            b = -dur * i / n - off
            if shape == "c":
                g = f'<circle r="{r}" fill="{col}" stroke="#fff" stroke-width="1.5"/>'
            else:
                g = (f'<g><circle r="{r + 1}" fill="{col}" stroke="#fff" stroke-width="1.5"/>'
                     f'<path d="M-3.5,-3.5 L3.5,3.5 M3.5,-3.5 L-3.5,3.5" stroke="#fff" stroke-width="2"/></g>')
            s += f'<g>{g}<animateMotion dur="{dur}s" begin="{b:.2f}s" repeatCount="indefinite" path="{path}"/></g>'
        return s
    o.append(dots(inward, GREEN, 5, 6))
    o.append(dots(outward, "#868E96", 4, 6, 6))
    o.append(dots(inward, "#E03131", 2, 6, 7, "x", 0.6))
    # labels with leader lines
    def lab(x, y, tx, ty, s, col=NAVY, anchor=None):
        return (f'<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty}" stroke="{MUTED}" stroke-width="1.5"/>'
                f'<circle cx="{x}" cy="{y}" r="3.5" fill="{MUTED}"/>' + t(tx + (6 if anchor is None else -6), ty + 5, s, 16, col, 800, anchor))
    o.append(lab(plx + 22, ply - 10, 600, 300, "placenta"))
    o.append(lab(430, 440, 600, 380, "umbilical cord"))
    o.append(lab(fx + 30, fy + 90, 600, 450, "fetus"))
    o.append(lab(ux + 120, uy + 150, 600, 520, "amniotic fluid"))
    o.append(lab(ux + 160, uy + 205, 600, 590, "uterus wall (muscle)"))
    o.append(t(650, 222, "Mum's blood", 15, "#C92A2A", 800))
    # legend
    lx, ly = 600, 650
    o.append(f'<line x1="{lx}" y1="{ly - 20}" x2="1000" y2="{ly - 20}" stroke="{EDGE}" stroke-width="2"/>')
    o.append(f'<circle cx="{lx + 8}" cy="{ly + 6}" r="7" fill="{GREEN}"/>' + t(lx + 24, ly + 12, "oxygen and food → to the fetus", 15, NAVY, 700))
    o.append(f'<circle cx="{lx + 8}" cy="{ly + 38}" r="6" fill="#868E96"/>' + t(lx + 24, ly + 44, "carbon dioxide and waste → back to Mum", 15, NAVY, 700))
    o.append(f'<circle cx="{lx + 8}" cy="{ly + 70}" r="8" fill="#E03131"/><path d="M{lx + 4.5},{ly + 66.5} L{lx + 11.5},{ly + 73.5} M{lx + 11.5},{ly + 66.5} L{lx + 4.5},{ly + 73.5}" stroke="#fff" stroke-width="2"/>'
             + t(lx + 24, ly + 76, "harmful things get through too:", 15, "#C92A2A", 700))
    o.append(t(lx + 24, ly + 98, "nicotine, carbon monoxide, alcohol, drugs", 15, MUTED))
    o.append(t(lx + 24, ly + 120, "and listeria bacteria", 15, MUTED))
    o.append(t(84, 790, "The fetus grows in the uterus for about 9 months. Mum's blood and the baby's blood never mix: things pass across in the placenta.", 14, MUTED))
    # three cards
    cards = [
        ("Diet", GREEN, ["Eat a balanced diet: protein, vitamins and minerals such as iron and calcium.",
                         "Poor diet: the fetus grows slowly; the baby is born small and less able to fight disease.",
                         "Avoid soft cheese (Camembert, Brie): it can carry listeria, which can kill a fetus.",
                         "Less caffeine (coffee, tea, chocolate): it can slow growth."]),
        ("Smoking", "#495057", ["Carbon monoxide takes the place of oxygen in the blood, so the fetus gets less oxygen.",
                                "Its heart beats faster to get more oxygen to its cells.",
                                "Risks: born early (premature), low birth weight, stillbirth."]),
        ("Alcohol & drugs", "#C92A2A", ["Alcohol crosses the placenta into the fetus's blood.",
                                        "Heavy drinking: fetal alcohol syndrome (small head, smooth upper lip, small eye openings, learning problems).",
                                        "Drugs such as heroin: the baby can be born addicted."]),
    ]
    cw = 307; cy0 = 830; ch = 446
    for i, (h, col, pts) in enumerate(cards):
        x = 56 + i * (cw + 23.5)
        o.append(panel(x, cy0, cw, ch))
        o.append(f'<rect x="{x}" y="{cy0}" width="{cw}" height="10" rx="5" fill="{col}"/>')
        o.append(t(x + 24, cy0 + 50, h, 24, col, 800))
        yy = cy0 + 88
        for p in pts:
            o.append(f'<circle cx="{x + 30}" cy="{yy - 5}" r="4" fill="{col}"/>')
            w, hh = wrap(x + 44, yy, p, cw - 66, 15, NAVY, lh=21)
            o.append(w); yy += hh + 14
    o.append("</svg>\n")
    return "\n".join(o)


for name, fn in (("science-diagram-cell-to-gene", cell_to_gene),
                 ("science-diagram-mitosis-meiosis", mitosis_meiosis),
                 ("science-diagram-xx-xy", boy_or_girl),
                 ("science-diagram-mother-fetus", mother_fetus)):
    with open(os.path.join(OUT, name + ".svg"), "w") as f:
        f.write(fn())
    print("wrote", name)
