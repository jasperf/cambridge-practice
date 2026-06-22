# Cambridge Practice — Agent Context

## Project

Interactive self-marking exercise sheets for Cambridge Secondary 1, IGCSE, and A-Level students. Each sheet is a single self-contained HTML file. No build tools, no frameworks, no CDN dependencies beyond Google Fonts. Everything works offline once loaded.

**Live site:** https://jasperf.github.io/cambridge-practice (auto-deployed from `main` via GitHub Pages)

**Stack:** Pure HTML5 + CSS3 + vanilla JavaScript. No build step, no package manager, no server.

## Structure

```
cambridge-practice/
├── index.html              ← home page / subject index (update when adding sheets)
├── resources.html          ← curated external resources (YouTube, BBC Bitesize)
├── README.md               ← project overview
├── AGENTS.md               ← this file
├── SETUP.md                ← setup and deployment guide
├── CLAUDE.md               ← legacy agent instructions
├── LICENSE                 ← MIT license
├── material/               ← source documents (PDFs, docs, images)
│   └── convert.sh          ← ImageMagick batch convert script
├── docs/                   ← technical documentation
│   ├── README.md           ← docs index
│   └── state-management.md ← state object and scoring explained
├── s1/                     ← Secondary 1 sheets
│   ├── sa2/                ← Summer Assessment 2 revision
│   │   ├── focus/          ← focused topic drills
│   │   ├── term4-sa2-maths.html
│   │   ├── term4-sa2-english.html
│   │   └── term4-sa2-science.html
│   ├── science/             ← topic-specific drills
│   │   └── circuits.html   ← Electric Circuits (interactive SVG)
│   └── t4/                 ← Term 4
│       ├── w1/             ← Week 1
│       │   └── term4-week1-maths-science.html
│       └── w6/             ← Week 6
│           ├── term4-week6-english.html
│           └── term4-week6-science.html
└── igcse/                  ← IGCSE (planned)
```

## Commands

```bash
# Preview any sheet directly in browser (no server needed)
open s1/t4/w1/term4-week1-maths-science.html

# Or serve locally for index page links to work
npx serve .                    # install once: npm i -g serve
python3 -m http.server 3000   # Python 3
php -S localhost:3000         # PHP
# Then visit http://localhost:3000

# Git workflow
git add .
git commit -m "Add Week N: Subject exercises"
git push                          # auto-deploys to GitHub Pages
```

## Conventions

- One HTML file per exercise sheet — fully self-contained with inline CSS and JS
- No external dependencies except Google Fonts (Fraunces, Literata, DM Mono)
- Answers checked client-side; no server, no login, no tracking
- File naming: flexible but follow patterns like `term{N}-week{N}-{subject}.html` or `{level}/{term}/{week}/{name}.html`
- **Always update `index.html`** when adding a new sheet
- Card classes: `.math` (blue), `.sci` (green), `.eng` (amber) for subject color-coding

### Sheet Header Pattern (all sheets must follow this)

Every sheet — regardless of subject or course — must use the same topbar/header structure:

```html
<canvas id="confetti-canvas"></canvas>

<div class="topbar">
  <div class="topbar-left">
    <div class="logo">Student<span>'s</span> Study Hub</div>
    <div class="week-badge">Subject · Topic</div>
  </div>
  <div style="display:flex;align-items:center;gap:14px;">
    <a href="path/to/index.html" class="back-link">&larr; All sheets</a>
    <div class="timer-wrap"><span style="font-size:0.85rem;">&#9201;</span><div class="timer" id="timer">00:00</div></div>
    <div class="score-pill"><div class="score-label">Score</div><div class="score-val" id="global-score">0 / N</div></div>
  </div>
</div>
<div class="progress-wrap"><div class="progress-bar" id="progress-bar"></div></div>
```

Key rules:
- Logo is always `Student<span>'s</span> Study Hub` — never a course-specific name
- Topbar uses `<div>`, not `<header>`
- Always include a back-link, timer, and score pill in the right side
- Confetti canvas goes right after `<body>` with `id="confetti-canvas"`
- Hero section uses `<div class="hero">`, not `<section>` or `<main>` wrappers
- Main content area uses `<div class="main">`, not `<main>`

### Question Card Pattern (all sheets must follow this)

Every question card must have:
1. **Marks badge** in the header: `<span class="q-marks">N mark(s)</span>`
2. **Check/Hint/Reveal buttons** using proper CSS classes (never inline styles):
```html
<div class="q-actions">
  <button class="btn btn-check" onclick="checkMCQ('q1','b','Q1')">Check</button>
  <button class="btn btn-hint" onclick="showHint('q1', 'Hint text')">Hint</button>
  <button class="btn btn-reveal" onclick="revealAnswer('q1', 'Answer text')">Show Answer</button>
</div>
<div class="feedback" id="q1-fb"></div>
```
3. **Actions before feedback** — the `q-actions` div must come before the `feedback` div
4. **Every question needs a Check button** — selecting an MCQ option should not auto-check; the student clicks Check when ready
5. **maxMarks must match** the actual sum of `marks` object values — verify this when creating sheets

### Question IDs
- Math: `m1`, `m2`, ..., `mN`
- Science: `s1`, `s2`, ..., `sN`
- English: `e1`, `e2`, ..., `eN`

### CSS Design Tokens (defined in `:root` on every sheet)
```css
--bg, --surface, --surface2, --border    /* Dark theme layers */
--accent-math, --accent-sci, --accent-warn, --accent-danger
--text, --text-muted, --text-dim        /* Typography */
--correct, --wrong                       /* Answer feedback */
--font-display, --font-body, --font-mono
--radius, --shadow                       /* UI */
```

### Required CSS Classes for Question Actions
Every sheet must define these button classes (never use inline styles on buttons):
- `.btn` — base button styling (mono font, padding, border-radius, transition)
- `.btn-check` — primary action button (green for science, blue for math)
- `.btn-hint` — subtle hint button (surface background, muted text)
- `.btn-reveal` — minimal show-answer button (transparent, dim text)
- `.q-actions` — flex container for the button row
- `.q-marks` — marks badge in question header

### JavaScript State Pattern
- Central `state` object: `{ answers, correct, totalMarks, maxMarks, startTime }`
- Supporting arrays: `mathQs`, `sciQs`, `engQs` for score aggregation
- Marks object: `marks = { m1: 2, m2: 1, ... }` keyed by question ID
- All UI derives from state; DOM is just a representation
- Persistence via `localStorage` with timestamped keys

### Common Functions
- `selectMCQ(qid, el, val)` — track selection
- `checkMCQ(qid, correctVal, label)` — single choice
- `checkMulti(qid, correctValsArray, label)` — multi-select
- `checkNum(qid, correctVal, label, tolerance)` — numeric with tolerance
- `showHint(qid, hintText)`, `revealAnswer(qid, answerText)`
- `markResult(qid, isCorrect, label)` — update UI and state
- `updateScores()` — recalculate and update score displays
- `showResults(score)` — display final panel with confetti
- `launchConfetti()` — canvas-based animation

## Constraints

- Do not introduce build steps, bundlers, or npm dependencies
- Do not add frameworks (React, Vue, etc.)
- Keep each exercise sheet self-contained — no shared JS files
- Do not mention the AI tool used to assist with this project by name
- **Do not add AI tool co-authorship to commit messages**
- **Never use "Co-Authored-By: Mistral Vibe" or similar in any commit message**
- **Do not include "Generated by Mistral Vibe." in commit messages**
- ** `.DS_Store` and `material/` folder are gitignored **

## Git

- Atomic commits: one logical change per commit — one new sheet, one fix, or one index update, never bundled together
- GitHub Pages: auto-deploys from `main` branch within ~30 seconds of push
- After push, the site (GitHub free site) will be deployed, which takes some time. Use `gh` CLI tool to check deployment status.
