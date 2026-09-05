#!/usr/bin/env python3
"""Audit MCQ sheets against the two checks in CLAUDE.md.

Check 1 - answer spread: is the correct letter roughly even across A-D, with no
          long run of the same letter?
Check 2 - giveaways: does the correct option repeat the teaching material that
          sits above it (info box / key ideas / definition table) near verbatim?

Usage:  python3 scripts/mcq_audit.py s2/t1/w2/*.html
        python3 scripts/mcq_audit.py --check 2 --verbose s2/t1/**/*.html
"""
import argparse, collections, html, itertools, pathlib, re, sys

# ---------------------------------------------------------------- parsing ---

TAG = re.compile(r'<[^>]+>')
DROP = re.compile(r'<(script|style|svg)\b.*?</\1>', re.S | re.I)
STOP = set("""a an the of to in on for and or but is are was were be been being it its
this that these those with as at by from into than then so such not no any all each
one two both which what when where how why who whom while do does did has have had
you your they them their there here if can could will would should may might must
about above below over under between within during also more most other others some""".split())

def visible_text(chunk: str) -> str:
    return html.unescape(TAG.sub(' ', chunk)).replace('—', ' ').replace('–', ' ')

def words(text: str) -> list:
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP and len(w) > 2]

def parse_sheet(path: pathlib.Path):
    """Yield dicts per MCQ: qid, letter, num, question, options, correct_text, material."""
    src = DROP.sub(' ', path.read_text(encoding='utf-8'))

    # correct answer per qid, in document order
    answers = {m.group(1): m.group(2)
               for m in re.finditer(r"checkMCQ\('([^']+)','([a-f])'", src)}

    cards = list(re.finditer(r'<div class="q-card"[^>]*id="qcard-([^"]+)"', src))
    if not cards:
        cards = list(re.finditer(r'<div class="q-card"[^>]*>', src))

    out, material, cursor = [], '', 0
    for i, card in enumerate(cards):
        qid = card.group(1) if card.re.groups else None
        gap = src[cursor:card.start()]
        # a section header resets the accumulated teaching material
        if 'section-header' in gap or '<h2' in gap:
            material = gap[max(gap.rfind('section-header'), gap.rfind('<h2')):]
        else:
            material += ' ' + gap
        end = cards[i + 1].start() if i + 1 < len(cards) else len(src)
        body = src[card.start():end]
        cursor = end

        if qid is None or qid not in answers:
            continue
        opts = {m.group(1): visible_text(m.group(2)).strip()
                for m in re.finditer(
                    r"selectMCQ\('" + re.escape(qid) + r"',\s*this,\s*'([a-f])'\)\"[^>]*>(.*?)</div>\s*(?=<div class=\"mcq-opt|</div>)",
                    body, re.S)}
        if not opts:  # fallback: option letter + span text
            opts = {m.group(1): visible_text(m.group(2)).strip() for m in re.finditer(
                r"selectMCQ\('" + re.escape(qid) + r"',\s*this,\s*'([a-f])'\).*?<span>(.*?)</span>", body, re.S)}
        qtext = re.search(r'class="q-text"[^>]*>(.*?)</div>', body, re.S)
        num = re.search(r'class="q-num"[^>]*>(.*?)</div>', body, re.S)
        out.append(dict(
            qid=qid, letter=answers[qid],
            num=visible_text(num.group(1)).strip() if num else qid,
            question=re.sub(r'\s+', ' ', visible_text(qtext.group(1))).strip() if qtext else '',
            options=opts,
            correct_text=opts.get(answers[qid], ''),
            material=re.sub(r'\s+', ' ', visible_text(material)).strip(),
        ))
    return out

# ---------------------------------------------------------------- check 1 ---

def longest_run(seq):
    return max((len(list(g)) for _, g in itertools.groupby(seq)), default=0)

def predictability(seq):
    """Share of letters guessable from the previous one (a perfect abcdabcd... cycle = 1.0)."""
    if len(seq) < 6:
        return 0.0
    nxt = collections.defaultdict(collections.Counter)
    for cur, following in zip(seq, seq[1:]):
        nxt[cur][following] += 1
    hits = sum(c.most_common(1)[0][1] for c in nxt.values())
    return hits / (len(seq) - 1)

def available_letters(qs):
    """Letters a student actually sees. Not every sheet offers four options."""
    seen = collections.Counter()
    for q in qs:
        for l in q['options']:
            seen[l] += 1
    withopts = sum(1 for q in qs if q['options'])
    letters = [l for l in 'abcdef' if seen[l] >= max(1, withopts * 0.5)]
    return ''.join(letters) or 'abcd'

def check_spread(qs, letters=None):
    letters = letters or available_letters(qs)
    seq = ''.join(q['letter'] for q in qs)
    counts = collections.Counter(seq)
    n = len(seq)
    run = longest_run(seq)
    missing = [l for l in letters if counts[l] == 0]
    expected = n / len(letters)
    skewed = [l for l in letters if n >= 8 and abs(counts[l] - expected) > max(2, expected * 0.6)]
    pred = predictability(seq)
    return dict(n=n, seq=seq, counts={l: counts[l] for l in letters}, letters=letters,
                run=run, missing=missing, skewed=skewed, pred=pred,
                ok=not missing and not skewed and run <= 2 and pred < 0.85)

# ---------------------------------------------------------------- check 2 ---

def sentences(text):
    return [s for s in re.split(r'(?<=[.!?;:])\s+|•', text) if len(s.split()) > 3]

def giveaway_score(option, material):
    ow = words(option)
    if len(ow) < 3:
        return 0.0, ''
    best, src = 0.0, ''
    for sent in sentences(material):
        sw = set(words(sent))
        if not sw:
            continue
        score = sum(1 for w in ow if w in sw) / len(ow)
        # bonus for a long contiguous phrase reappearing
        for size in range(len(ow), 2, -1):
            if any(' '.join(ow[i:i + size]) in ' '.join(words(sent)) for i in range(len(ow) - size + 1)):
                score = max(score, size / len(ow))
                break
        if score > best:
            best, src = score, re.sub(r'\s+', ' ', sent).strip()
    return best, src

def check_giveaways(qs, threshold):
    hits = []
    for q in qs:
        score, src = giveaway_score(q['correct_text'], q['material'])
        if score >= threshold:
            hits.append((score, q, src))
    return sorted(hits, key=lambda h: -h[0])

# --------------------------------------------------------- integrity ---

REVEAL = re.compile(r"revealAnswer\('([^']+)','\s*([A-D])[\s&:—-]")

def check_reveals(path):
    """Reveal text usually leads with the answer letter - it must still agree
    with checkMCQ() after any reshuffle."""
    src = path.read_text(encoding='utf-8')
    ans = dict(re.findall(r"checkMCQ\('([^']+)','([a-f])'", src))
    rev = dict(REVEAL.findall(src))
    return [(q, ans[q].upper(), rev[q]) for q in ans if q in rev and ans[q].upper() != rev[q]]

# ------------------------------------------------------------------- main ---

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('files', nargs='+')
    ap.add_argument('--check', choices=['1', '2', 'both'], default='both')
    ap.add_argument('--threshold', type=float, default=0.75)
    ap.add_argument('--verbose', action='store_true')
    a = ap.parse_args()

    failed = 0
    for f in sorted(pathlib.Path(p) for p in a.files):
        qs = parse_sheet(f)
        if not qs:
            continue
        print(f'\n\033[1m{f}\033[0m  ({len(qs)} MCQ)')
        mism = check_reveals(f)
        failed += bool(mism)
        if mism:
            print(f"  [FAIL] {len(mism)} reveal(s) name the wrong letter")
            for qid, want, got in mism[:6]:
                print(f"         {qid}: answer is {want}, reveal says {got}")
        if a.check in ('1', 'both'):
            r = check_spread(qs)
            flag = 'OK ' if r['ok'] else 'FAIL'
            failed += not r['ok']
            opts = f" [{len(r['letters'])} options]" if len(r['letters']) != 4 else ''
            print(f"  [{flag}] spread {r['counts']}{opts}  longest-run={r['run']}  predictable={r['pred']:.0%}")
            print(f"         {r['seq']}")
            if r['missing']:
                print(f"         missing letters: {', '.join(l.upper() for l in r['missing'])}")
            if r['skewed']:
                print(f"         over/under-used: {', '.join(l.upper() for l in r['skewed'])}")
            if r['pred'] >= 0.85:
                print(f"         repeating cycle: the next answer is guessable from the previous one")
        if a.check in ('2', 'both'):
            hits = check_giveaways(qs, a.threshold)
            failed += bool(hits)
            print(f"  [{'FAIL' if hits else 'OK '}] giveaways: {len(hits)} question(s) >= {a.threshold:.0%} overlap")
            for score, q, src in hits:
                print(f"         {q['num']} ({q['qid']}, {q['letter'].upper()}) {score:.0%}  {q['question'][:70]}")
                if a.verbose:
                    print(f"            answer:   {q['correct_text'][:90]}")
                    print(f"            material: {src[:110]}")
    return 1 if failed else 0

if __name__ == '__main__':
    sys.exit(main())
