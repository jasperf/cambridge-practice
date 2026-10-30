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
├── index.html                  ← Home page: a card for every sheet
├── resources.html              ← Curated external resources (YouTube, BBC Bitesize)
├── s1/                         ← Secondary 1: t4/ weekly sheets, sa2/ revision (+ focus/ drills), science/ topic drills
├── s2/                         ← Secondary 2
│   ├── t1/                     ← Term 1: w{N}/ weekly sheets + term-level revision handouts
│   ├── t2/                     ← Term 2: w{N}/ weekly sheets
│   ├── science-formula-sheets/ ← One-page SVG formula & key-fact sheets (index.html gallery)
│   └── english-revision-sheets/← One-page SVG English revision sheets (index.html gallery)
├── igcse-add-maths/            ← IGCSE Additional Maths (0606)
├── scripts/                    ← MCQ audit, shuffle and sync tools
└── docs/                       ← Documentation (state management, etc.)
```

Weekly sheets are named `term{N}-week{N}-{subject}-{topic}.html`, with a matching `.md` printable beside them. For the file-by-file list of a term, see its README: [s2/t1](./s2/t1/README.md) · [s2/t2](./s2/t2/README.md) · [science formula sheets](./s2/science-formula-sheets/README.md) · [English revision sheets](./s2/english-revision-sheets/README.md).

## Printable Worksheets (Parallel Path)

In addition to the interactive HTML sheets, **printable markdown worksheets** are available for classroom use where students write answers in notebooks with pen and paper. Each one sits in the same weekly folder as its interactive sheet, under the same basename — `term1-week2-maths-rational-irrational.md` beside `term1-week2-maths-rational-irrational.html`. They contain the exact same questions, in a format suitable for printing or copying into notebooks.

Use the printable versions for **written practice/exams** and the interactive versions for **self-assessment with hints and instant feedback**.

Revision handouts that combine several weekly sheets live one level up, in the term folder (e.g. `s2/t1/term1-maths-unit1-revision.md`).

See the term READMEs ([s2/t1](./s2/t1/README.md), [s2/t2](./s2/t2/README.md)) for the full index.

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

## Generating PDFs

The printable `.md` worksheets can be turned into a PDF locally with [pandoc](https://pandoc.org/) — no PDFs are committed to the repo (see `.gitignore`), so generate one whenever you need it:

```bash
pandoc -f gfm term1-english-unit1-revision.md -o term1-english-unit1-revision.pdf \
  --pdf-engine=xelatex -V geometry:margin=2.2cm -V fontsize=11pt -V colorlinks=true
```

`-f gfm` matters: these sheets write MCQ options as a `-` list directly under the question line with no blank line before it (as GitHub renders it). Pandoc's default markdown reader needs that blank line to start a list, so without `-f gfm` the options collapse into run-on paragraph text instead of bullets. Requires `pandoc` and a LaTeX engine (`xelatex`, from a TeX distribution like MacTeX/TeX Live) installed locally.

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
| Science (Why Atoms Bond, Covalent & Metallic Bonding) | Secondary 2 | ✅ Term 1 Week 4 |
| Mathematics (Expressions & Formulae) | Secondary 2 | ✅ Term 1 Week 5 |
| English Unit Test 1 Revision (Sentence Types & Reading Comprehension) | Secondary 2 | ✅ Unit Test 1, 26 Aug 2026 |
| Science Unit Test 1 Revision (Atomic Structure, Periodic Table & Bonding) | Secondary 2 | ✅ Unit Test 1, 26 Aug 2026 |
| Science Unit Test 2 (Plant Biology) | Secondary 2 | ✅ Term 1 Week 7 · Unit Test 2, 10 Sep 2026 |
| English Unit Test 2 (Viewpoints & Arguments, Past Continuous, Subject–Verb Agreement) | Secondary 2 | ✅ Term 1 Week 7 · Unit Test 2, 10 Sep 2026 |
| Mathematics Unit Test 2 Practice Test (Expressions & Formulae) | Secondary 2 | ✅ Unit Test 2 retest, 16 Sep 2026 |
| Mathematics Unit Test 3 (Decimals, Percentages & Rounding) | Secondary 2 | ✅ Term 1 Week 8 · Unit Test 3 |
| Mathematics Unit 3 Follow-up (Bounds & Powers) | Secondary 2 | ✅ Term 1 Week 8 · After Unit Test 3 |
| Mathematics Unit 3 Retest (Bounds & Significant Figures) | Secondary 2 | ✅ Term 1 Week 8 · After the Follow-up |
| Mathematics Unit 3 Practice Test (20 Open Questions) | Secondary 2 | ✅ Term 1 Week 8 · After the Retest |
| Mathematics Unit 4.2 (Simultaneous Equations) | Secondary 2 | ✅ Term 1 Week 8 · Workbook Exercise 4.2 |
| Mathematics Unit 4.3 (Linear Inequalities) | Secondary 2 | ✅ Term 2 Week 1 · 5–9 October |
| Mathematics Unit 5.1–5.2 (Calculating Angles) | Secondary 2 | ✅ Term 2 Week 2 · 12–16 October |
| Mathematics Unit Test 1 Practice (Linear Inequalities & Angles) | Secondary 2 | ✅ Term 2 Week 3 · Unit Test 1, 20 Oct 2026 |
| English Unit Test 1 (Persuasive & Emotive Language, Grammar, Reading, Short Story, Spelling) | Secondary 2 | ✅ Term 2 Week 3 · Unit Test 1, 28 Oct 2026 |
| Mathematics Unit Test 2 Practice (Angles, Shapes & Measurements) | Secondary 2 | ✅ Term 2 Week 5 · Unit Test 2, 3 Nov 2026 |
| Science Unit 3: Density (Solids, Liquids & Gases) | Secondary 2 | ✅ Term 2 Week 4 · 26–30 October |
| Science Unit 3: Sound Waves & Thermal Energy | Secondary 2 | ✅ Term 2 Week 4 · 26–30 October |
| Science Unit 3: Electricity (Circuits, V = IR, Series & Parallel) | Secondary 2 | ✅ Term 2 Week 4 · 26–30 October |
| English UN Day Writing Project (Zimbabwe/Sweden coaching guide) | Secondary 2 | ✅ Term 2 · Draft due 23 Oct, final due 20 Nov |

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
