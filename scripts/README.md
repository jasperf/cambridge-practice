# scripts

Local audit helpers for the authoring rules in `CLAUDE.md` (*Writing
Multiple-Choice Questions* and *Check the totals*). Plain Python 3, no dependencies, no build step —
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

## `mcq_shuffle.py` — apply the fix

```bash
python3 scripts/mcq_shuffle.py --dry-run s2/t1/w3/term1-week3-science-ionic-bonding.html
python3 scripts/mcq_shuffle.py s2/t1/w3/term1-week3-science-ionic-bonding.html
```

Moves option *text* between fixed letter slots to hit a target sequence that
is balanced, has no run over two, and scores under 55% predictable. It then
updates the `checkMCQ()` letter and the leading letter of `revealAnswer()`,
and re-syncs the `.md` printable.

It **refuses to run** on a sheet whose reveal text cross-references another
option by letter ("Option A describes respiration"), because a permutation
would silently invalidate that prose. Reshuffle those by hand.

It does not touch question wording, so it cannot fix a check-2 giveaway —
that is always a human edit.

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

`--fix` reorders the `.md` options to match the html rather than the other
way round. It is derived from the html each time, so it is idempotent and
will repair a half-applied shuffle:

```bash
python3 scripts/mcq_sync.py --fix s2/t1/w3/*.html
python3 scripts/mcq_sync.py s2/t1/w3/*.html   # re-run to confirm
```

**Run it after every shuffle**, before committing.

## `sheet_audit.py` — do the shown totals match the real ones?

```bash
python3 scripts/sheet_audit.py s2/t2/w4/*.html
python3 scripts/sheet_audit.py $(find s1 s2 igcse-add-maths -name '*.html')
```

The score is computed at runtime from the sheet's `marks` object, but the
totals a student *sees* are typed by hand, and they go stale when questions
are added or re-weighted. This takes `marks` as the source of truth and
checks it against:

- each question's `N marks` badge;
- the header chip (`48 questions · self-marked · 50 marks`);
- the initial score pill (`0 / 50`) and each section pill (`0/13`, against
  the questions listed for that section in `const sections`);
- a hard-coded `maxMarks: { math: 23, sci: 22 }` on older sheets;
- the sheet's card chips in the root `index.html` (`42 questions`, `60 marks`).

Question cards with no `marks` entry are listed as info, not errors:
unscored written cards such as `wr1` are legitimate. It does not read the
`.md` printable or the term README tables, so check those by hand when a
total changes. Exits non-zero if any sheet has a mismatch.

## `build_review_sheet.py` — generate a review sheet from a spec

```bash
python3 scripts/build_review_sheet.py scripts/review_specs/s2_sem1_science_revision.py
```

Unlike the tools above, this one **writes** files. A review sheet covers several
topics. For each topic it shows key-fact cards, then an optional interactive
explorer, then auto-marked questions. The page has a *Cover the notes* toggle
that blurs the facts. From one spec the builder writes three files: the `.html`,
the `.md` printable (with the written questions added) and the `-answers.md`.
The output is ordinary self-contained HTML, the same as every hand-made sheet,
so nothing in the site depends on the script.

A spec is a plain Python file in `review_specs/`. It defines `META`,
`SECTIONS` (with their key facts), `Q` (the questions) and `WRITTEN`. It can
also define `EXPLORERS` / `EXPLORER_CSS` / `EXPLORER_JS`. The docstring at the
top of `build_review_sheet.py` lists the fields. To make a new review page,
copy an existing spec, change `META['out']` and the content, then build.
**Edit the spec, not the generated files**, because a rebuild overwrites them.

Run the usual checks on the result afterwards. The builder does not shuffle
anything for you: set each MCQ's `correct` letter so the spread passes check 1.
