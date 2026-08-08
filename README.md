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
├── resources.html                    ← Curated external resources (YouTube, BBC Bitesize)
├── s1/                              ← Secondary 1
│   ├── t4/                          ← Term 4
│   │   ├── w1/                      ← Week 1
│   │   │   └── term4-week1-maths-science.html
│   │   └── w6/                      ← Week 6
│   │       ├── term4-week6-science.html
│   │       └── term4-week6-english.html
│   ├── sa2/                         ← SA2 revision
│   │   ├── focus/                   ← Topic focus drills (one topic at a time)
│   │   │   ├── term4-sa2-science-respiration.html    ← Respiration & Blood (15 Q)
│   │   │   ├── term4-sa2-science-atomic.html         ← Atoms & Chemical Reactions (15 Q)
│   │   │   ├── term4-sa2-science-forces.html        ← Health, Speed & Forces (15 Q)
│   │   │   ├── term4-sa2-science-earth-space.html   ← Earth, Ecosystems & Space (15 Q)
│   │   │   ├── term4-sa2-science-gases.html         ← Gases, Liquids & Chromatography (15 Q)
│   │   │   └── term4-sa2-science-light.html         ← Light, Reflection & Colour (13 Q)
│   │   ├── term4-sa2-maths.html          ← SA2 revision (all units, 42 q, 60 marks)
│   │   ├── term4-sa2-english.html        ← SA2 revision (parts of speech & clauses, 40 q, 40 marks)
│   │   └── term4-sa2-science.html        ← SA2 revision (all topics, 42 q, 50 marks)
│   ├── science/                     ← Topic-specific drills
│   │   ├── circuits.html                 ← Electric Circuits (16 q, 26 marks, interactive SVG)
│   │   ├── chemical-reactions.html       ← Chemical Reactions & Particle Model (17 q, 25 marks)
│   │   └── forces-speed-pressure.html    ← Forces, Speed & Pressure (17 q, 25 marks)
├── s2/                              ← Secondary 2
│   └── t1/                          ← Term 1
│       ├── README.md                     ← Printable worksheets TOC & index
│       ├── term1-maths-rational-irrational.md    ← Printable worksheet (16 q, 20 marks)
│       ├── term1-maths-indices-standard-form.md  ← Printable worksheet (37 q, 49 marks)
│       ├── term1-science-ionic-bonding.md        ← Printable worksheet (21 q, 25 marks)
│       ├── w2/                      ← Week 2 (interactive versions)
│       │   ├── term1-week2-atomic-structure-periodic.html  ← Atomic Structure & Periodic Table (16 q, 20 marks, interactive)
│       │   ├── term1-week2-maths-rational-irrational.html  ← Rational & Irrational Numbers (16 q, 20 marks)
│       │   └── term1-week2-maths-indices-standard-form.html ← Indices & Standard Form (37 q, 49 marks)
│       └── w3/                      ← Week 3 (interactive versions)
│           └── term1-week3-science-ionic-bonding.html  ← Why Elements React & Ionic Bonding (21 q, 25 marks, interactive)
├── igcse-add-maths/                 ← IGCSE Additional Maths (0606)
│   └── circular-measure.html        ← Circular Measure: Radians & Degrees (16 q, 23 marks, interactive)
├── igcse/                           ← IGCSE (planned)
│   └── ...
├── docs/
│   ├── README.md                     ← Documentation index
│   └── state-management.md          ← State object and score tracking explained
└── README.md
```

## Printable Worksheets (Parallel Path)

In addition to the interactive HTML sheets, **printable markdown worksheets** are available in `s2/t1/` for classroom use where students write answers in notebooks with pen and paper. These contain the exact same questions as the interactive versions but in a format suitable for printing or copying into notebooks.

Use the printable versions for **written practice/exams** and the interactive versions for **self-assessment with hints and instant feedback**.

See [s2/t1/README.md](./s2/t1/README.md) for the table of contents of all printable documents.

## Adding a New Sheet

1. Create a new HTML file in the appropriate folder (e.g. `s1/t4/w1/term4-week2.html`)
2. Copy an existing sheet as your starting template
3. Update questions, answers, and marks
4. Update `index.html` to include the new sheet
5. Push to `main` — GitHub Pages publishes automatically

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

### Cambridge Secondary 1

| Subject | Level | Status |
|---------|-------|--------|
| Mathematics (Data & Statistics) | Secondary 1 | ✅ Term 4 Week 1 |
| Science (Electromagnets) | Secondary 1 | ✅ Term 4 Week 1 |
| Science (Renewable Energy) | Secondary 1 | ✅ Term 4 Week 6 |
| English (Active & Passive Voice) | Secondary 1 | ✅ Term 4 Week 6 |
| Mathematics SA2 Revision (all units) | Secondary 1 | ✅ SA2 Exam 21 May 2026 |
| English SA2 Revision (parts of speech & clauses) | Secondary 1 | ✅ SA2 Exam 21 May 2026 |
| Science SA2 Revision (all topics) | Secondary 1 | ✅ SA2 Exam 22 May 2026 |
| Science SA2 Focus — Respiration & Blood | Secondary 1 | ✅ Section B drill |
| Science SA2 Focus — Atoms & Chemical Reactions | Secondary 1 | ✅ Section C drill |
| Science SA2 Focus — Health, Speed & Forces | Secondary 1 | ✅ Section D drill |
| Science SA2 Focus — Earth, Ecosystems & Space | Secondary 1 | ✅ Section E drill |
| Science SA2 Focus — Gases, Liquids & Chromatography | Secondary 1 | ✅ Section A drill |
| Science SA2 Focus — Light, Reflection & Colour | Secondary 1 | ✅ Section F drill |
| Science (Electric Circuits) | Secondary 1 | ✅ Topic drill |
| Science (Chemical Reactions & Particle Model) | Secondary 1 | ✅ Topic drill |
| Science (Forces, Speed & Pressure) | Secondary 1 | ✅ Topic drill |

### Cambridge Secondary 2

| Subject | Level | Status |
|---------|-------|--------|
| Science (Atomic Structure & Periodic Table) | Secondary 2 | ✅ Term 1 Week 2 |
| Mathematics (Rational & Irrational Numbers) | Secondary 2 | ✅ Term 1 Week 2 |
| Mathematics (Indices & Standard Form) | Secondary 2 | ✅ Term 1 Week 2 |
| Science (Why Elements React & Ionic Bonding) | Secondary 2 | ✅ Term 1 Week 3 |

### IGCSE

| Subject | Topics | Status |
|---------|--------|--------|
| Mathematics (Circular Measure — Radians & Degrees) | Additional Maths (0606) | ✅ Topic drill |
| Physics (Electricity & Magnetism) | Core + Extended | 🔜 Coming |
| Mathematics (Statistics & Probability) | Core + Extended | 🔜 Coming |

## Tech

Pure HTML + CSS + JavaScript. No frameworks, no build tools, no CDN dependencies beyond Google Fonts. Every file works offline once loaded.

---

*Maintained for Cambridge curriculum students. Not affiliated with Cambridge Assessment International Education.*
