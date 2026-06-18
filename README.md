# Cambridge Secondary & IGCSE Practice

Interactive self-marking exercise sheets for Cambridge Secondary 1, IGCSE, and A-Level students.

## Live Site

👉 **[jasperf.github.io/cambridge-practice](https://jasperf.github.io/cambridge-practice)**

## What's Inside

Each exercise sheet is a single self-contained HTML file with:
- Multiple choice and numeric answer questions
- Instant answer checking with correct/wrong feedback
- Hints and worked answer reveals
- Live score tracker and session timer
- No dependencies, no server required — pure HTML/CSS/JS

## Structure

```
cambridge-practice/
├── index.html                        ← Home page / subject index
├── s1/                              ← Secondary 1
│   └── t4/                          ← Term 4
│       ├── w1/                      ← Week 1
│       │   └── term4-week1-maths-science.html
│       └── w6/                      ← Week 6
│           ├── term4-week6-science.html
│           └── term4-week6-english.html
├── s1/sa2/
│   ├── term4-sa2-maths.html          ← SA2 revision (all units, 42 q, 60 marks)
│   ├── term4-sa2-english.html        ← SA2 revision (parts of speech & clauses, 40 q, 40 marks)
│   └── term4-sa2-science.html        ← SA2 revision (all topics, 42 q, 50 marks)
├── s1/science/
│   ├── circuits.html                 ← Electric Circuits topic drill (16 q, 26 marks, interactive SVG)
│   └── chemical-reactions.html       ← Chemical Reactions & Particle Model drill (17 q, 25 marks, interactive particle animator)
├── igcse/
│   └── ...
├── docs/
│   ├── README.md                     ← Documentation index
│   └── state-management.md          ← State object and score tracking explained
└── README.md
```

## Adding a New Sheet

1. Create a new HTML file in the appropriate folder (e.g. `s1/t4/w1/term4-week2.html`)
2. Copy an existing sheet as your starting template
3. Update questions, answers, and marks
4. Push to `main` — GitHub Pages publishes automatically

## Local Development

```bash
# Clone the repo
git clone https://github.com/jasperf/cambridge-practice.git
cd cambridge-practice

# Open any file directly in your browser — no build step needed
open s1/t4/w1/term4-week1-maths-science.html

# Or run a simple local server (optional, for index page links)
npx serve .
# then visit http://localhost:3000
```

## Subjects Covered

| Subject | Level | Status |
|---------|-------|--------|
| Mathematics (Data & Statistics) | Secondary 1 | ✅ Term 4 Week 1 |
| Science (Electromagnets) | Secondary 1 | ✅ Term 4 Week 1 |
| Science (Renewable Energy) | Secondary 1 | ✅ Term 4 Week 6 |
| English (Active &amp; Passive Voice) | Secondary 1 | ✅ Term 4 Week 6 |
| Mathematics SA2 Revision (all units) | Secondary 1 | ✅ SA2 Exam 21 May 2026 |
| English SA2 Revision (parts of speech &amp; clauses) | Secondary 1 | ✅ SA2 Exam 21 May 2026 |
| Science SA2 Revision (all topics) | Secondary 1 | ✅ SA2 Exam 22 May 2026 |
| Science (Electric Circuits) | Secondary 1 | ✅ Topic drill |
| Science (Chemical Reactions & Particle Model) | Secondary 1 | ✅ Topic drill |
| Physics | IGCSE | 🔜 Coming |

## Tech

Pure HTML + CSS + JavaScript. No frameworks, no build tools, no CDN dependencies beyond Google Fonts. Every file works offline once loaded.

---

*Maintained for Cambridge curriculum students. Not affiliated with Cambridge Assessment International Education.*
