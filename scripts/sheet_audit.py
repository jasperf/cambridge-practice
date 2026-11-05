#!/usr/bin/env python3
"""Check that the totals a sheet *shows* match the marks it actually scores.

The `marks` object in each sheet's <script> is the source of truth: the score
is computed from it at runtime. Everything else is hand-typed and goes stale
when questions are added or re-weighted. This compares it with:

  - the per-question badge   <div class="q-marks">2 marks</div>
  - the hero chip            "48 questions · self-marked · 50 marks"
  - the initial score pill   id="global-score">0 / 50<
  - section score pills      id="sec-xx-val">0/8<  (against the questions
                             listed for that key in `const sections`)
  - a hard-coded maxMarks    maxMarks: { math: 23, sci: 22 }  (older sheets;
                             subject is the qid's leading letters)
  - the sheet's card chips   "42 questions" / "60 marks" in the root index.html

It also lists question cards with no entry in `marks` (as info: unscored
written cards like `wr1` are legitimate) and `marks` entries with no card.

Usage:
  python3 scripts/sheet_audit.py s2/t2/w4/*.html
  python3 scripts/sheet_audit.py $(find s1 s2 igcse-add-maths -name '*.html')

Sheets without a `marks` object (galleries, index pages) are skipped.
Exits non-zero if any sheet has a mismatch.
"""
import re
import sys
from pathlib import Path

NUM = r'(\d+(?:\.\d+)?)'


def fmt(n):
    return str(int(n)) if float(n).is_integer() else str(n)


def card_blocks(text):
    """qid -> the HTML of its question card (up to the next card)."""
    starts = [(m.start(), m.group(1)) for m in re.finditer(r'id="qcard-(\w+)"', text)]
    blocks = {}
    for i, (pos, qid) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
        blocks[qid] = text[pos:end]
    return blocks


def audit(path):
    text = Path(path).read_text(encoding='utf-8')
    m = re.search(r'const marks\s*=\s*\{([^}]*)\}', text)
    if not m:
        return None
    marks = {k: float(v) for k, v in re.findall(r'(\w+)\s*:\s*' + NUM, m.group(1))}
    blocks = card_blocks(text)
    scored = [q for q in blocks if q in marks]
    total = sum(marks[q] for q in scored)
    problems, notes = [], []

    # Cards vs marks entries
    unscored = [q for q in blocks if q not in marks]
    if unscored:
        notes.append(f"cards not in marks (unscored): {', '.join(unscored)}")
    orphans = [q for q in marks if q not in blocks]
    if orphans:
        problems.append(f"marks entries with no question card: {', '.join(orphans)}")

    # Per-question badge
    for q in scored:
        b = re.search(r'class="q-marks"[^>]*>\s*' + NUM + r'\s*marks?\b', blocks[q])
        if b and float(b.group(1)) != marks[q]:
            problems.append(f"{q}: badge says {b.group(1)} mark(s), marks object says {fmt(marks[q])}")

    # Hero chip: "N questions ... M marks" (first one on the page)
    h = re.search(r'(\d+)\s+(?:auto-marked\s+)?questions?\b[^<]{0,60}?' + NUM + r'\s+marks', text)
    if h:
        nq, nm = int(h.group(1)), float(h.group(2))
        if nq != len(scored):
            problems.append(f"header says {nq} questions, sheet has {len(scored)} scored")
        if nm != total:
            problems.append(f"header says {fmt(nm)} marks, questions add up to {fmt(total)}")

    # Initial global score pill (0 / 0 means it is filled in by JS: fine)
    g = re.search(r'id="global-score"[^>]*>\s*0\s*/\s*(\d+)\s*<', text)
    if g and int(g.group(1)) not in (0, total):
        problems.append(f"score pill starts at 0 / {g.group(1)}, total is {fmt(total)}")

    # Section pills: each must match the marks of the questions in its section
    pills = {k: int(v) for k, v in re.findall(r'id="sec-([\w-]+?)-(?:val|score)"[^>]*>\s*0\s*/\s*(\d+)\s*<', text)}
    sm = re.search(r'const sections\s*=\s*\{(.*?)\n\};', text, re.S)
    sections = {}
    if sm:
        for key, qs in re.findall(r'(\w+)\s*:\s*(?:\{[^{}]*?qs\s*:\s*)?\[([^\]]*)\]', sm.group(1)):
            sections[key] = re.findall(r"['\"](\w+)['\"]", qs)
    for key, shown in pills.items():
        if key in sections:
            actual = sum(marks.get(q, 0) for q in sections[key])
            if shown != actual:
                problems.append(f"section '{key}' shows 0/{shown}, its questions add up to {fmt(actual)}")
    if pills and not any(k in sections for k in pills) and sum(pills.values()) != total:
        problems.append(f"section pills sum to {sum(pills.values())}, total is {fmt(total)}")

    # Hard-coded maxMarks per subject (older sheets)
    mm = re.search(r'maxMarks\s*:\s*\{([^}]*)\}', text)
    if mm:
        declared = {k: float(v) for k, v in re.findall(r'(\w+)\s*:\s*' + NUM, mm.group(1))}
        prefix = {'math': 'm', 'sci': 's', 'eng': 'e'}
        for subj, val in declared.items():
            p = prefix.get(subj, subj[0])
            actual = sum(marks[q] for q in scored if re.fullmatch(p + r'\d+', q))
            if actual != val:
                problems.append(f"maxMarks.{subj} = {fmt(val)}, its questions add up to {fmt(actual)}")

    # Home page card chips ("42 questions", "60 marks") for this sheet. A sheet
    # with two subjects may have a card per subject, so a subject subtotal
    # (questions grouped by leading letters: m1, s1, e1...) is accepted too.
    groups = {}
    for q in scored:
        groups.setdefault(re.match(r'[a-z]+', q).group(0), []).append(q)
    ok_n = {len(scored)} | {len(g) for g in groups.values()}
    ok_m = {total} | {sum(marks[q] for q in g) for g in groups.values()}
    for chips in index_cards().get(Path(path).resolve(), []):
        for num, kind in chips:
            if kind == 'questions' and int(num) not in ok_n:
                problems.append(f"index.html card says {num} questions, sheet has {len(scored)}")
            if kind == 'marks' and float(num) not in ok_m:
                problems.append(f"index.html card says {num} marks, sheet has {fmt(total)}")

    return len(scored), total, problems, notes


_INDEX = None


def index_cards():
    """Resolved sheet path -> list of [(number, 'questions'|'marks'), ...] per card."""
    global _INDEX
    if _INDEX is None:
        _INDEX = {}
        index = Path(__file__).resolve().parent.parent / 'index.html'
        if index.exists():
            text = index.read_text(encoding='utf-8')
            for href, body in re.findall(r'<a href="([^"]+\.html)"[^>]*class="card[^"]*"[^>]*>(.*?)</a>', text, re.S):
                chips = re.findall(r'class="chip">\s*(\d+)\s+(questions|marks)\s*<', body)
                if chips:
                    _INDEX.setdefault((index.parent / href).resolve(), []).append(chips)
    return _INDEX


def main(argv):
    paths = [a for a in argv if a.endswith('.html')]
    if not paths:
        print(__doc__.strip().split('Usage:')[1].strip())
        return 2
    failed = 0
    for p in sorted(paths):
        r = audit(p)
        if r is None:
            continue
        n, total, problems, notes = r
        status = 'FAIL' if problems else 'ok  '
        print(f"{status} {p}  ({n} questions, {fmt(total)} marks)")
        for line in problems:
            print(f"     ✗ {line}")
        for line in notes:
            print(f"     · {line}")
        failed += bool(problems)
    print(f"\n{failed} sheet(s) with mismatched totals")
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
