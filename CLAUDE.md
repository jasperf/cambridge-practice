# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Static site of self-marking exercise sheets. No build step, no npm, no server. Every file is a single self-contained HTML file that works by opening it directly in a browser.

Content:
- **Cambridge curriculum sheets** (`s1/`) — maths, science, English practice for Stage 1.

Live at: https://jasperf.github.io/cambridge-practice (deployed automatically from `main` via GitHub Pages).

## Directory Structure

```
s1/                          # Cambridge Stage 1
├── t4/w{N}/                 # Term 4, weekly sheets
├── sa2/                     # Summative assessment 2
└── science/                 # Topic-based science sheets

docs/                        # Course planning / design docs
material/                    # Source material (English, math, science)
```

## Development

```bash
# Open a sheet directly
open s1/t4/w1/term4-week1-maths-science.html

# Or serve with a local server (needed for index page links)
npx serve .
```

No install step. No linting or test suite.

## Generating a PDF from a printable `.md` sheet

Revision handouts (e.g. `s2/t1/term1-english-unit1-revision.md`) are plain GFM Markdown. To generate a PDF, use `pandoc` with `xelatex`:

```bash
pandoc -f gfm term1-english-unit1-revision.md -o term1-english-unit1-revision.pdf \
  --pdf-engine=xelatex -V geometry:margin=2.2cm -V fontsize=11pt -V colorlinks=true
```

**`-f gfm` is required, not optional.** These sheets write MCQ options as a `-` list directly under the question line with no blank line in between (matching GitHub's rendering, since GFM lets a list interrupt a paragraph). Pandoc's default `markdown` reader does *not* allow that — it requires a blank line before a list starts, so without `-f gfm` the options get swallowed into the question paragraph as run-on text (e.g. "...What are they? - A) ... - B) ...") instead of rendering as a bulleted list. Always spot-check the generated PDF's first MCQ question to confirm the options actually render as bullets, not inline dashes.

**Chemistry sheets need `-V mainfont="Arial Unicode MS"`.** The default Latin Modern font has no subscript/superscript digit glyphs, so xelatex silently drops them (`MgCl₂` prints as "MgCl", `Na⁺` as "Na") — with only a `Missing character` warning in the log. Any sheet using formulae or ion charges must add the font override:

```bash
pandoc -f gfm term1-science-unit1-revision.md -o term1-science-unit1-revision.pdf \
  --pdf-engine=xelatex -V mainfont="Arial Unicode MS" \
  -V geometry:margin=2.2cm -V fontsize=11pt -V colorlinks=true
```

A clean run prints no `Missing character` lines at all; if any appear, the glyphs they name are missing from the PDF.

This is an on-demand, local step — no PDF output is committed or wired into any build/deploy process (see Constraints below).

## Adding a New Exercise Sheet

### Cambridge sheets
1. Copy an existing sheet as the template.
2. Place it at `s1/{section}/{filename}.html` (e.g. `s1/t4/w2/term4-week2-english.html`).
3. Update `index.html` to add a card linking to the new sheet.
4. Update the READMEs that index the content (see below).
5. Push to `main` — Pages deploys within ~30 seconds.

### READMEs to update after adding content

New sheets/handouts are referenced in more than one README — check all that apply:

- **Root `README.md`** — the `Structure` tree, and the relevant `Subjects Covered` table (Secondary 1 / Secondary 2 / IGCSE).
- **`s2/t1/README.md`** (or an equivalent term-level index, if one exists for the term/stage you're adding to) — its worksheet table (or revision-handouts table) and its own structure diagram.
- **`index.html`** — a card in the matching subject grid (already covered above, but easy to forget when a change is "just docs").

A new revision handout that mixes an auto-marked `.html` with extra open-ended/printable-only content (e.g. extended writing tasks) should say so explicitly in these READMEs — don't let a "printable has the exact same questions as interactive" claim go stale.

## Writing Multiple-Choice Questions

Three checks before a sheet is done. The first two are easy to get wrong when questions are written top-to-bottom in one pass; the third catches what fixing the first one breaks. `scripts/` holds a dependency-free audit tool for all three.

### 1. Spread the correct answer across A–D

Write each question's options, then go back and shuffle the positions so the correct answer is roughly evenly spread over A/B/C/D, with no long run of the same letter. Writing naturally puts the correct option first (or in the same slot every time), which lets a student guess the sheet instead of the subject. Verify with the audit script rather than by eye:

```bash
python3 scripts/mcq_audit.py --check 1 s2/t1/w7/*.html
```

Aim for every letter used a comparable number of times and no more than two of the same letter in a row. A distribution with a letter at zero (e.g. `{'a': 7, 'b': 13, 'c': 13, 'd': 0}`) means a student can eliminate an option for free on every question.

**An even spread is not enough on its own.** A sheet answering `abcdabcdabcd…` is perfectly balanced and still completely guessable, so the script also reports a *predictability* score — the share of answers derivable from the previous one. Keep it well below 85%; a properly shuffled sheet sits near 50%. Shuffle to a genuinely irregular order, not to a rotating cycle.

Note that reveal text usually names the letter (`revealAnswer('e7','D &mdash; The claim&hellip;')`), and some reveals cross-reference *other* options by letter ("Option A describes respiration"). Reordering options means rewriting both, so shuffle deliberately, not with a blind permutation.

### 2. Don't answer the question in the material above it

Info boxes, `key ideas` paragraphs, definition tables/cards and diagrams sitting above a question block are there to teach — but if a question's correct option repeats one of them close to word for word, the question tests reading-off, not recall. Watch for it especially where a definition table is followed immediately by "which part is *&lt;that exact definition&gt;*?" questions.

Fixes, in order of preference:

- Ask the question about an **extract or worked example** instead of the definition (identify the part in a real paragraph, rather than match the term to its gloss).
- **Reword** so the option is not the info-box phrasing — ask for the *effect*, the *reason why*, or the *consequence of getting it wrong*.
- Move the recall-only questions to a **different section** from the box that defines them.

Keeping one or two straight definition-recall questions per sheet is fine as a warm-up. It is a problem when a whole block of them sits directly under the table that gives the answers.

Find the candidates with the same script — it scores each correct option against the teaching material above it and prints the sentence being echoed:

```bash
python3 scripts/mcq_audit.py --check 2 --verbose s2/t1/w3/*.html
```

Treat its hits as a shortlist to read, not a verdict: a 100% match on a definition question is a real problem, while a 75% match that only shares vocabulary is often fine.

### 3. Re-sync the printable after any shuffle

Most `.html` sheets have an `.md` printable beside them holding the same questions in the same option order. Reordering options in one and not the other desyncs them silently — the printable ends up with a different answer letter than the interactive sheet. After any shuffle:

```bash
python3 scripts/mcq_sync.py s2/t1/w3/*.html          # report drift
python3 scripts/mcq_sync.py --fix s2/t1/w3/*.html    # reorder the .md to match
```

To apply a fix for check 1 rather than just detect it, `scripts/mcq_shuffle.py`
reorders the options, rewrites the `checkMCQ()` letter and the reveal's leading
letter, and re-syncs the printable. It bails out on sheets whose reveals
cross-reference options by letter, and it never touches question wording — so
a check-2 giveaway is always fixed by hand.

See `scripts/README.md` for what the three tools check and how they decide.

## Exercise Sheet Architecture

Each sheet is one HTML file with inline CSS and JS — no external dependencies except Google Fonts (Fraunces, Literata, DM Mono).

**JS state object** (defined near the bottom of `<script>`):
```js
const state = {
  answers: {},           // qid → value(s)
  correct: {},           // qid → true/false
  totalMarks: { math: 0, sci: 0 },
  maxMarks: { math: N, sci: N },
  startTime: Date.now()
}
```

**Question ID conventions**:
- Cambridge sheets: math questions `m1`–`mN`, science `s1`–`sN`. Arrays `mathQs`, `sciQs` drive score aggregation.

Marks per question are in a `marks` object keyed by qid.

**DOM conventions per question card**:
- Wrapper: `id="qcard-{qid}"`
- Feedback element: `id="{qid}-fb"`
- Numeric input: `id="{qid}-ans"`
- MCQ options container: `id="{qid}-opts"`

**Check functions** (called from `onclick` in HTML):
- `checkMCQ(qid, correctVal, label)` — single-choice
- `checkMulti(qid, correctValsArray, label)` — multi-select
- `checkNum(qid, correctVal, label, tolerance)` — numeric with optional tolerance

**Supporting functions**: `selectMCQ`, `showHint`, `revealAnswer`, `markResult`, `updateScores`, `showResults`, `launchConfetti`.

## CSS Design Tokens

Defined in `:root` on every sheet and `index.html`:

| Token | Purpose |
|---|---|
| `--bg` / `--surface` / `--surface2` | Dark background layers |
| `--accent` / `--accent-math` | Blue (#4f8ef7) |
| `--accent-sci` / `--accent2` | Green (#3ecf8e) |
| `--accent-warn` / `--accent3` | Amber (#f5a623) |
| `--correct` / `--wrong` | Answer feedback colours |
| `--font-display` | Fraunces (headings) |
| `--font-body` | Literata (body text) |
| `--font-mono` | DM Mono (labels, badges, code) |

## Constraints

- Do not introduce build tools, bundlers, or npm packages.
- Keep each exercise sheet fully self-contained — no shared JS files.
- Do not add frameworks (React, Vue, etc.).
- Always update `index.html` when adding a new sheet.

## Git

- Atomic commits: one logical change per commit (e.g. one new sheet, one bug fix, one index update — not all at once).
- Do not add `Co-Authored-By: Claude` or any AI attribution to commit messages.
