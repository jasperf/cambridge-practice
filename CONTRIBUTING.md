# Contributing

Plain HTML, CSS and JavaScript. No build step, no npm, no server. Every sheet is one self-contained file.

## Structure

```
cambridge-practice/
├── index.html                  ← Home page: a card for every sheet
├── resources.html              ← Curated external resources (YouTube, BBC Bitesize)
├── s1/                         ← Secondary 1: t4/ weekly sheets, sa2/ revision (+ focus/ drills), science/ topic drills
├── s2/                         ← Secondary 2
│   ├── t1/                     ← Term 1: w{N}/ weekly sheets + term-level revision handouts
│   ├── t2/                     ← Term 2: w{N}/ weekly sheets
│   ├── sem1/                   ← Semester 1 assessment mock papers (English, Maths ×2, Science)
│   ├── science-formula-sheets/ ← One-page SVG formula & key-fact sheets (index.html gallery)
│   ├── maths-formula-sheets/   ← One-page SVG maths formula sheets (index.html gallery)
│   └── english-revision-sheets/← One-page SVG English revision sheets (index.html gallery)
├── igcse-add-maths/            ← IGCSE Additional Maths (0606)
├── scripts/                    ← MCQ audit, shuffle and sync tools
└── docs/                       ← Documentation (state management, etc.)
```

Weekly sheets are named `term{N}-week{N}-{subject}-{topic}.html`, with a matching `.md` printable beside them. The file-by-file list for each term is in its README: [s2/t1](./s2/t1/README.md) · [s2/t2](./s2/t2/README.md) · [s2/sem1](./s2/sem1/README.md) · [science formula sheets](./s2/science-formula-sheets/README.md) · [maths formula sheets](./s2/maths-formula-sheets/README.md) · [English revision sheets](./s2/english-revision-sheets/README.md).

## Printable worksheets

Each interactive sheet has a printable markdown version in the same folder, under the same basename (`term1-week2-maths-rational-irrational.md` beside `term1-week2-maths-rational-irrational.html`). It holds the same questions, for written practice in a notebook. Revision handouts that combine several weekly sheets live one level up, in the term folder (e.g. `s2/t1/term1-maths-unit1-revision.md`).

## Local development

```bash
git clone https://github.com/jasperf/cambridge-practice.git
cd cambridge-practice

# Open any sheet directly in your browser
open s1/t4/w1/term4-week1-maths-science.html

# Or run a local server (needed for the index page links)
npx serve .
# then visit http://localhost:3000
```

## Adding a new sheet

1. Copy an existing sheet as your template and place it in the right folder (e.g. `s2/t2/w6/term2-week6-maths-topic.html`).
2. Update the questions, answers and marks.
3. Check the multiple-choice answers with the audit tools in [`scripts/`](./scripts/README.md).
4. Add a card to `index.html` and a row to the matching term README.
5. Push to `main`. GitHub Pages publishes automatically.

## Generating PDFs

The printable `.md` worksheets can be turned into a PDF locally with [pandoc](https://pandoc.org/). No PDFs are committed (see `.gitignore`).

```bash
pandoc -f gfm term1-english-unit1-revision.md -o term1-english-unit1-revision.pdf \
  --pdf-engine=xelatex -V geometry:margin=2.2cm -V fontsize=11pt -V colorlinks=true
```

`-f gfm` matters: the sheets write MCQ options as a `-` list directly under the question with no blank line before it. Pandoc's default reader needs that blank line, so without `-f gfm` the options collapse into run-on text. Chemistry sheets also need `-V mainfont="Arial Unicode MS"`, or subscripts and ion charges are dropped. Requires `pandoc` and a LaTeX engine (`xelatex`, from MacTeX or TeX Live).

## Tech

Pure HTML + CSS + JavaScript. No frameworks, no build tools, no CDN dependencies beyond Google Fonts. Every file works offline once loaded.
