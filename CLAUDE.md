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
