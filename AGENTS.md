# Cambridge Practice — Agent Context

## Project

Interactive self-marking exercise sheets for Cambridge Secondary 1, IGCSE, and A-Level students. Each sheet is a single self-contained HTML file. No build tools, no frameworks, no CDN dependencies beyond Google Fonts. Everything works offline once loaded.

Live site: https://jasperf.github.io/cambridge-practice

## Structure

```
cambridge-practice/
├── index.html              ← home page / subject index (update when adding sheets)
├── s1/                     ← Secondary 1
│   └── t4/w1/             ← term / week folders
├── igcse/                  ← IGCSE (planned)
└── assets/                 ← shared CSS (future)
```

## Conventions

- One HTML file per exercise sheet — fully self-contained with inline CSS and JS
- No external dependencies except Google Fonts
- Answers checked client-side; no server, no login, no tracking
- File naming: `term{N}-week{N}-{subject}.html`
- Always update `index.html` when adding a new sheet

## Style

- Dark theme with CSS custom properties defined in `:root`
- Fonts: Fraunces (display), Literata (body), DM Mono (mono/labels)
- Accent colours: `--accent` blue, `--accent2` green, `--accent3` amber
- Cards use `.math`, `.sci`, `.eng` modifier classes for colour-coded top borders

## Constraints

- Do not introduce build steps, bundlers, or npm dependencies
- Do not add frameworks (React, Vue, etc.)
- Keep each exercise sheet self-contained — no shared JS files
- Do not mention the AI tool used to assist with this project by name

## Git

- Atomic commits: one logical change per commit — one new sheet, one fix, or one index update, never bundled together.
