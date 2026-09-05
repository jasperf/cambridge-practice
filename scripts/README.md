# scripts

Local audit helpers for the MCQ authoring rules in `CLAUDE.md` → *Writing
Multiple-Choice Questions*. Plain Python 3, no dependencies, no build step —
they only read the sheets, they never modify them.

## `mcq_audit.py` — the two authoring checks

```bash
# audit one term
python3 scripts/mcq_audit.py s2/t1/**/*.html

# just the answer spread, or just the giveaways
python3 scripts/mcq_audit.py --check 1 s2/t1/w2/*.html
python3 scripts/mcq_audit.py --check 2 --verbose s2/t1/w3/*.html

# audit everything
python3 scripts/mcq_audit.py $(find s1 s2 igcse-add-maths -name '*.html')
```

Exits non-zero if any sheet fails, so it can gate a commit.

**Check 1 — answer spread.** Reads the correct letter from each `checkMCQ()`
call and reports the distribution, the longest run of one letter, and a
*predictability* score. The letter set is taken from the options the sheet
actually renders, so a three-option sheet is not scolded for never using D.

Predictability is the share of answers guessable from the previous one. It
catches the failure that a plain distribution check misses: `abcdabcdabcd…`
is a perfectly even spread and still lets a student walk the whole sheet
without reading a question. Anything ≥85% is flagged; deliberately shuffled
sheets land near 50%.

**Check 2 — giveaways.** For each question it compares the correct option
against the teaching material above it (info boxes, key-ideas paragraphs,
definition tables), resetting at each section header, and reports the best
sentence-level word overlap. `--threshold` defaults to 0.75; `--verbose`
prints the answer and the sentence it echoes so you can judge it.

This one needs a human. A 100% hit on a definition question is a real
problem; a 75% hit where the answer merely shares vocabulary with the
material often is not. `CLAUDE.md` allows one or two straight recall
questions per sheet as a warm-up — the script counts them, it does not
decide.

## `mcq_sync.py` — keep the printable in step

```bash
python3 scripts/mcq_sync.py s2/t1/**/*.html
```

Reordering options in an `.html` to fix the spread silently desyncs the
`.md` printable next to it. This compares the two, option by option.

It aligns questions by their wording rather than their number, because a
printable is often a superset of the interactive sheet — extra short-answer
questions shift its numbering — and it normalises `<sub>`/`<sup>` markup
against the unicode glyphs the `.md` uses (`Na<sup>+</sup>` vs `Na⁺`), so
chemistry sheets do not report drift that isn't there. A printable with no
options at all is reported as free-response and skipped.

**Run it after every shuffle**, before committing.
