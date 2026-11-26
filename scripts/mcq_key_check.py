#!/usr/bin/env python3
"""Check that each MCQ's answer key agrees with its own reveal text.

Per question it compares three things:
  1. the letter in checkMCQ('qid','x',...)
  2. the leading letter in revealAnswer('qid','X &mdash; ...')
  3. which option's wording the reveal explanation overlaps with most

Flags: key/reveal letter mismatch (definite), reveal text that best matches a
different option than the key (likely), and, for a sibling *-answers.md, a
letter that differs from the key (definite).

Usage: python3 scripts/mcq_key_check.py [-v] file.html [...]
Exit status 1 if any definite problem is found. Dependency-free.
"""
import html, re, sys
from pathlib import Path

STOP = set("the a an and or of to in is are it its be so that this which for with as at by on from because not no "
           "than then can will plants plant leaf".split())


def words(s):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s)).lower()
    return {w for w in re.findall(r"[a-z0-9]+", s) if w not in STOP and len(w) > 2}


def check(path):
    src = Path(path).read_text(encoding="utf-8")
    definite, likely, n = [], [], 0
    unparsed = []
    answers_md = Path(path).with_name(Path(path).stem + "-answers.md")
    md_keys = {}
    if answers_md.exists():
        for m in re.finditer(r"^\|\s*Q(\d+)\s*\|\s*([A-Da-d])\s*\|", answers_md.read_text(encoding="utf-8"), re.M):
            md_keys[int(m.group(1))] = m.group(2).lower()

    cards = re.finditer(r'<div class="q-card" id="qcard-(\w+)">(.*?)<div class="feedback"', src, re.S)
    for m in cards:
        qid, body = m.groups()
        k = re.search(r"checkMCQ\('%s','(\w)'" % qid, body)
        if not k:
            continue
        n += 1
        key = k.group(1).lower()
        opts = {}
        for line in body.splitlines():
            o = re.search(r"selectMCQ\('%s',\s*this,\s*'(\w)'\)(.*)" % qid, line)
            if o:
                t = re.sub(r"<div class=\"opt-indicator\">[A-Da-d]?</div>", "", o.group(2))
                opts[o.group(1)] = re.sub(r"^[^>]*>", "", t, count=1)
        if not opts:
            unparsed.append(qid)
            continue
        rv = re.search(r"revealAnswer\('%s','(.*?)'\)\"" % qid, body, re.S)
        num = int(re.sub(r"\D", "", qid) or 0)
        if key not in opts:
            definite.append(f"{qid}: key '{key}' is not one of the options {sorted(opts)}")
            continue
        if num in md_keys and md_keys[num] != key:
            definite.append(f"{qid}: html key {key.upper()} but {answers_md.name} says {md_keys[num].upper()}")
        if not rv:
            continue
        text = rv.group(1)
        lead = re.match(r"\s*([A-Da-d])\s*(?:&mdash;|—|-|:)", text)
        if lead and lead.group(1).lower() != key:
            definite.append(f"{qid}: key {key.upper()} but reveal starts '{lead.group(1).upper()}'")
        # Which option does the explanation talk about? Ignore sentences that
        # explicitly name another letter ("Option B is respiration").
        expl = re.sub(r"^\s*[A-Da-d]\s*(?:&mdash;|—|-|:)", "", text)
        expl = re.sub(r"[^.]*\b[Oo]ption [A-D]\b[^.]*\.?", "", expl)
        ew = words(expl)
        scores = {l: len(ew & words(t)) / max(1, len(words(t))) for l, t in opts.items()}
        best = max(scores, key=scores.get)
        if best != key and scores[best] >= 0.4 and scores[key] <= scores[best] / 2:
            likely.append(f"{qid}: key {key.upper()} but reveal text overlaps option {best.upper()} more "
                          f"({scores[best]:.0%} vs {scores[key]:.0%}) - read it")
    return n, definite, likely, unparsed


def main(argv):
    files = [a for a in argv if not a.startswith("-")]
    if not files:
        print(__doc__)
        return 2
    bad = 0
    for f in files:
        n, d, l, u = check(f)
        if not n:
            continue
        status = "FAIL" if d else ("WARN" if l else "ok")
        print(f"[{status:4}] {f}  ({n} MCQ)")
        for x in d:
            print("   DEFINITE", x)
        for x in l:
            print("   likely  ", x)
        if u:
            print("   unparsed (options not found):", ", ".join(u))
        bad += bool(d)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
