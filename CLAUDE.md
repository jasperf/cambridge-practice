# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Static site of self-marking exercise sheets. No build step, no npm, no server. Every file is a single self-contained HTML file that works by opening it directly in a browser.

Two content areas:
- **Cambridge curriculum sheets** (`s1/`) — maths, science, English practice for Stage 1.
- **Python programming course** (`python/`) — Arcade game-dev worksheets and a multi-part platformer project.

Live at: https://jasperf.github.io/cambridge-practice (deployed automatically from `main` via GitHub Pages).

## Directory Structure

```
s1/                          # Cambridge Stage 1
├── t4/w{N}/                 # Term 4, weekly sheets
├── sa2/                     # Summative assessment 2
└── science/                 # Topic-based science sheets

python/                      # Python programming course
├── arcade-intro.html        # Standalone Arcade fundamentals
├── sprites-graphics.html    # Standalone sprites & graphics
├── platformer/              # Multi-part platformer project
│   └── part1-project-setup.html
├── basics/                  # (planned) Python basics sheets
└── challenges/              # (planned) Challenge sheets

docs/                        # Course planning / design docs
material/                    # Source material (English, math, science)
```

## Development

```bash
# Open a sheet directly
open s1/t4/w1/term4-week1-maths-science.html
open python/arcade-intro.html

# Or serve with a local server (needed for index page links)
npx serve .
```

No install step. No linting or test suite.

## Adding a New Exercise Sheet

### Cambridge sheets
1. Copy an existing sheet as the template.
2. Place it at `s1/{section}/{filename}.html` (e.g. `s1/t4/w2/term4-week2-english.html`).
3. Update `index.html` to add a card linking to the new sheet.
4. Push to `main` — Pages deploys within ~30 seconds.

### Python sheets
1. Copy an existing Python sheet as the template.
2. Place standalone sheets in `python/`, multi-part project sheets in `python/platformer/`.
3. Update `index.html` to add a card linking to the new sheet.
4. Push to `main` — Pages deploys within ~30 seconds.

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
- Python sheets: questions `q1`–`qN`. Array `pyQs` drives score aggregation.

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
