#!/usr/bin/env python3
"""Reshuffle MCQ option order so the correct answer is spread across A-D.

Moves the option *text* between fixed letter slots, then updates the
checkMCQ() letter and the leading letter of the revealAnswer() text to match.
Re-syncs the .md printable beside the sheet by reordering its options to
match the new html order (via mcq_sync --fix), so the two never drift.

It refuses to run on a sheet whose reveal text cross-references other options
by letter ("Option A describes respiration") - those have to be reworded by
hand, and a blind permutation would silently invalidate them.

Usage:  python3 scripts/mcq_shuffle.py s2/t1/w3/term1-week3-science-ionic-bonding.html
        python3 scripts/mcq_shuffle.py --dry-run <file.html>
"""
import argparse, collections, pathlib, random, re, sys, zlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from mcq_audit import parse_sheet, check_spread, available_letters, predictability, longest_run

CROSSREF = re.compile(r'\b(?:option|choice)\s+[A-D]\b', re.I)

NUM = re.compile(r'-?\d+(?:\.\d+)?')

def ordered_options(q):
    """True when the options read as a scale ("1 clause / 2 clauses / 3 clauses",
    "30 / 45 / 60 / 90"). Their order carries meaning, so the answer letter is
    fixed by the content and reshuffling them looks like a mistake."""
    texts = [q['options'][l] for l in sorted(q['options'])]
    if len(texts) < 3:
        return False
    firsts = [NUM.search(t) for t in texts]
    if not all(firsts):
        return False
    v = [float(m.group()) for m in firsts]
    return len(set(v)) == len(v) and (v == sorted(v) or v == sorted(v, reverse=True))

def target_sequence(qs, letters, seed, pinned):
    """A balanced letter sequence with no run > 2 and a low predictability score.

    Not every question offers every letter - a sheet can mix four-option and
    three-option questions - so a candidate is only usable if each question can
    actually host the letter it is handed. Pinned questions keep the letter they
    already have; the rest are chosen to even out the totals around them."""
    rng = random.Random(seed)
    n = len(qs)
    allowed = [set(q['options']) or set(letters) for q in qs]
    fixed = {i: q['letter'] for i, q in enumerate(qs) if q['qid'] in pinned}
    free = [i for i in range(n) if i not in fixed]
    counts = collections.Counter(fixed.values())
    pool = []
    for _ in free:                       # hand each slot to the scarcest letter
        l = min(letters, key=lambda x: (counts[x], x))
        counts[l] += 1
        pool.append(l)
    # A short sheet cannot reach 55%: with only a handful of transitions, most
    # letters are followed by exactly one other, so the score is dominated by
    # sample size rather than by a guessable pattern. Fall back to the bar the
    # audit actually fails on rather than looping forever.
    for pred_max in (0.55, 0.85):
        for _ in range(20000):
            rng.shuffle(pool)
            cand = dict(fixed)
            cand.update(zip(free, pool))
            if any(cand[i] not in allowed[i] for i in range(n)):
                continue
            seq = ''.join(cand[i] for i in range(n))
            if longest_run(seq) <= 2 and predictability(seq) < pred_max:
                return seq
    raise SystemExit('could not build a target sequence')

def option_blocks(body, qid):
    """(letter, whole div, inner html) for each option, in document order."""
    pat = re.compile(
        r'(<div class="mcq-opt"[^>]*onclick="selectMCQ\(\s*\'' + re.escape(qid) +
        r"'\s*,\s*this\s*,\s*'([a-f])'\)\"[^>]*>)(.*?)(</div>\s*(?=<div class=\"mcq-opt|</div>))", re.S)
    return [(m.group(2), m, ) for m in pat.finditer(body)], pat

def shuffle_html(src, targets):
    """Permute option text between letter slots so each qid's answer lands on its target."""
    changed = {}
    for qid, want in targets.items():
        opts_pat = re.compile(
            r'(<div class="mcq-options"[^>]*id="' + re.escape(qid) + r'-opts"[^>]*>)(.*?)(</div>\s*<div class="q-actions")', re.S)
        m = opts_pat.search(src)
        if not m:
            continue
        inner = m.group(2)
        opt_pat = re.compile(r'<div class="mcq-opt".*?</div>\s*(?=<div class="mcq-opt"|\s*$)', re.S)
        divs = opt_pat.findall(inner)
        letters = [re.search(r"selectMCQ\(\s*'[^']+'\s*,\s*this\s*,\s*'([a-f])'\)", d).group(1) for d in divs]
        cur = re.search(r"checkMCQ\(\s*'" + re.escape(qid) + r"'\s*,\s*'([a-f])'", src).group(1)
        if cur == want:
            continue
        order = list(range(len(divs)))
        i, j = letters.index(cur), letters.index(want)
        order[i], order[j] = order[j], order[i]
        rebuilt = []
        for pos, src_idx in enumerate(order):
            d = divs[src_idx]
            d = re.sub(r"(selectMCQ\(\s*'[^']+'\s*,\s*this\s*,\s*')[a-f]('\))", r'\g<1>' + letters[pos] + r'\g<2>', d)
            # Some sheets print the letter in the bullet instead of leaving it
            # empty. That belongs to the slot, not to the option text, so it
            # stays put while the text around it moves.
            d = re.sub(r'(class="opt-indicator"[^>]*>)[A-F](</div>)',
                       r'\g<1>' + letters[pos].upper() + r'\g<2>', d)
            rebuilt.append(d)
        # Re-use the sheet's own indentation so the diff is the reordering only.
        ind = re.match(r'\s*\n(\s*)', inner)
        pad = ind.group(1) if ind else '        '
        close = re.search(r'\n(\s*)$', inner)
        new_inner = '\n' + pad + ('\n' + pad).join(x.strip() for x in rebuilt) + '\n' + (close.group(1) if close else '      ')
        src = src[:m.start(2)] + new_inner + src[m.end(2):]
        src = re.sub(r"(checkMCQ\(\s*'" + re.escape(qid) + r"'\s*,\s*')[a-f](')", r'\g<1>' + want + r'\g<2>', src)
        # Only a letter followed by a dash is the answer letter; a reveal that
        # opens with a real word ("A compass &mdash; its needle...") must not
        # have its first character rewritten.
        src = re.sub(r"(revealAnswer\(\s*'" + re.escape(qid) + r"'\s*,\s*'\s*)[A-D](\s*(?:&mdash;|&ndash;|[\u2013\u2014]))",
                     r'\g<1>' + want.upper() + r'\g<2>', src)
        changed[qid] = (cur, want)
    return src, changed

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('file'); ap.add_argument('--seed', type=int)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--pin', default='', help='comma-separated qids to leave on their current letter')
    a = ap.parse_args()
    path = pathlib.Path(a.file)
    src = path.read_text(encoding='utf-8')

    if CROSSREF.search(src):
        raise SystemExit(f'{path}: reveal text cross-references options by letter - reshuffle by hand')

    qs = parse_sheet(path)
    letters = available_letters(qs)
    # Derived from the filename so it stays reproducible, but two sheets of the
    # same length do not end up with the same answer sequence.
    seed = a.seed if a.seed is not None else zlib.crc32(path.name.encode())
    pinned = {q['qid'] for q in qs if ordered_options(q)}
    pinned |= {p.strip() for p in a.pin.split(',') if p.strip()}
    if pinned:
        print(f"  pinned {len(pinned)} question(s) with ordered options: "
              f"{', '.join(q['qid'] for q in qs if q['qid'] in pinned)}")
    seq = target_sequence(qs, letters, seed, pinned)
    targets = {q['qid']: seq[i] for i, q in enumerate(qs)}

    before = {q['qid']: q['letter'] for q in qs}
    new_src, changed = shuffle_html(src, targets)

    print(f'{path}: {len(changed)} question(s) moved')
    print(f"  before {''.join(before[q['qid']] for q in qs)}")
    print(f'  after  {seq}')
    if a.dry_run:
        return 0
    path.write_text(new_src, encoding='utf-8')

    md = path.with_suffix('.md')
    if md.exists() and changed:
        import mcq_sync
        mcq_sync.FIX = True
        mcq_sync.main([str(path)])
    return 0

if __name__ == '__main__':
    sys.exit(main())
