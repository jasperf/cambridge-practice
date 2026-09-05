#!/usr/bin/env python3
"""Check that a printable .md mirrors its .html sibling's MCQ option order.

Reordering options in the HTML to fix the answer spread silently desyncs the
printable unless the .md is reordered the same way. Run after every shuffle.

Usage:  python3 scripts/mcq_sync.py s2/t1/**/*.html
"""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from mcq_audit import parse_sheet, visible_text

# html writes <sub>2</sub>/<sup>+</sup>; the md mirror writes the unicode glyph
SUPSUB = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉⁺⁻⁼−–—', '01234567890123456789+-=---')

def similarity(a, b):
    aw, bw = set(re.findall(r'[a-z0-9]+', norm_words(a))), set(re.findall(r'[a-z0-9]+', norm_words(b)))
    return len(aw & bw) / len(aw | bw) if aw | bw else 0.0

def option_overlap(hopts, mopts):
    hn = {norm(v) for v in hopts.values()}
    mn = {norm(v) for v in mopts.values()}
    return len(hn & mn) / len(hn | mn) if hn | mn else 0.0

def norm_words(t):
    return re.sub(r'[^a-z0-9]+', ' ', visible_text(t).lower())

def norm(t):
    t = visible_text(t).lower().translate(SUPSUB)
    return re.sub(r'[^a-z0-9+-]+', '', t)

def parse_md(path):
    """Yield (question_number, stem, {letter: option_text}) in document order.

    The printable is often a superset of the interactive sheet - it adds
    short-answer questions - so its numbering does not line up with the html.
    Callers should align on the stem, not the number.
    """
    out, cur, stem, opts = [], None, '', {}
    def flush():
        if cur and opts:
            out.append((cur, stem, dict(opts)))
    for line in path.read_text(encoding='utf-8').splitlines():
        q = re.match(r'\s*\*\*Q(\d+)\*\*(.*)', line)
        o = re.match(r'\s*[-*]\s*\*?\*?([A-F])\)\s*(.+)', line)
        if q:
            flush()
            cur, stem, opts = q.group(1), '', {}
        elif o and cur:
            opts[o.group(1).lower()] = o.group(2).strip()
        elif cur and not opts and line.strip():
            stem += ' ' + line.strip()
    flush()
    return out

def main(paths):
    bad = 0
    for html_path in sorted(pathlib.Path(p) for p in paths):
        md_path = html_path.with_suffix('.md')
        if not md_path.exists():
            continue
        hq = [q for q in parse_sheet(html_path) if q['options']]
        mq = parse_md(md_path)
        if len(mq) <= max(1, len(hq) // 4):
            print(f'\n\033[1m{md_path}\033[0m')
            print(f'  [SKIP ] printable is free-response (no options to keep in sync)')
            continue
        extra = len(mq) - len(hq)
        note = f'  (+{extra} printable-only)' if extra > 0 else ''
        print(f'\n\033[1m{md_path}\033[0m  (html {len(hq)} MCQ / md {len(mq)} MCQ){note}')

        drift, unmatched = [], []
        for h in hq:
            best, score = None, 0.0
            for num, stem, mopts in mq:
                sim = similarity(h['question'], stem) * 0.6 + option_overlap(h['options'], mopts) * 0.4
                if sim > score:
                    best, score = (num, mopts), sim
            if not best or score < 0.5:
                unmatched.append(h)
                continue
            num, mopts = best
            for letter, mtext in mopts.items():
                htext = h['options'].get(letter)
                if htext is None or norm(htext) != norm(mtext):
                    drift.append((f"{h['num']}=md Q{num}", letter, htext, mtext))
        bad += bool(drift)
        print(f"  [{'DRIFT' if drift else 'OK   '}] {len(drift)} option(s) out of sync")
        if unmatched:
            print(f"         {len(unmatched)} html question(s) had no md counterpart: "
                  + ', '.join(q['num'] for q in unmatched[:8]))
        for num, letter, htext, mtext in drift[:8]:
            print(f'         {num} {letter.upper()}')
            print(f'            html: {(htext or "(missing)")[:80]}')
            print(f'            md:   {mtext[:80]}')
    return 1 if bad else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
