# Secondary 2 · Semester 1 Assessment — Mock Papers

Full-length practice papers for the Semester 1 assessments, **Monday 23 – Friday 27 November 2026** (each exam finishes at 11:00). Each paper pulls together every topic taught in Term 1 and Term 2 so far, with all-new questions.

Every paper comes in three files with the same basename:

- **`.html`**: the interactive sheet. Every question is auto-marked (multiple choice, a typed number or a typed word). Diagrams draw themselves in as you scroll.
- **`.md`**: the printable paper. It has the same questions in the same order, plus **written questions** at the end that are not on the interactive sheet (explanations, P.E.E.E. paragraphs, constructions, extended writing). These are marked by the teacher.
- **`-answers.md`**: answers to every auto-marked question and a marking guide for the written questions. It is kept separate, so the question paper can be handed out on its own.

## Exam timetable

| Day | Exam | Mock paper |
|-----|------|------------|
| Mon 23 Nov | Chinese (Writing + Reading) | — |
| Tue 24 Nov | Bahasa Indonesia (Reading & Understanding + Writing) | — |
| Wed 25 Nov | English (Levels 2 and 3: one standardised paper) | English Level 2/3 |
| Thu 26 Nov | Mathematics (two standardised papers) | Maths Paper 1 + Paper 2 |
| Fri 27 Nov | Science (one standardised paper) | Science |

## Papers

| Paper | Covers | Auto-marked | Written | Printable | Interactive | Answers |
|-------|--------|-------------|---------|-----------|-------------|---------|
| **English Level 2/3** | Sentence types & punctuation · Reading two texts with P.E.E.E. · Viewpoints & arguments · Persuasive & emotive language | 41 Qs · 48 marks (33 MCQ) | Q42–Q45 · 38 marks | [.md](./sem1-english-level23-mock.md) | [.html](./sem1-english-level23-mock.html) | [answers](./sem1-english-level23-mock-answers.md) |
| **Maths Paper 1: Number & Algebra** | Unit 1 (rational & irrational, indices, standard form) · Unit 2 (expressions & formulae) · Unit 3 (decimals, percentages, rounding & bounds) | 32 Qs · 44 marks (10 MCQ) | Q33–Q37 · 20 marks | [.md](./sem1-maths-paper1-number-algebra.md) | [.html](./sem1-maths-paper1-number-algebra.html) | [answers](./sem1-maths-paper1-number-algebra-answers.md) |
| **Maths Paper 2: Equations & Geometry** | Unit 4 (simultaneous equations, inequalities) · Unit 5 (angles, polygons, constructions, Pythagoras) · Unit 7.1–7.2 (circles, compound shapes) | 31 Qs · 49 marks (6 MCQ) | Q32–Q36 · 22 marks | [.md](./sem1-maths-paper2-equations-geometry.md) | [.html](./sem1-maths-paper2-equations-geometry.html) | [answers](./sem1-maths-paper2-equations-geometry-answers.md) |
| **Science** | Atoms & bonding · Plant biology · Density · Sound waves & thermal energy · Electricity | 39 Qs · 48 marks (17 MCQ) | Q40–Q45 · 24 marks | [.md](./sem1-science-mock.md) | [.html](./sem1-science-mock.html) | [answers](./sem1-science-mock-answers.md) |

### English Level 2/3

Section A covers the four sentence types, FANBOYS, MOTH, semicolons and comma rules (Term 1 Unit 1). Section B is a student magazine article, *Dig In: Why Every School Needs a Garden*, with questions on viewpoint, simile, juxtaposition, statistics, expert opinion, rule of three, concession, anecdote, repetition, a P.E.E.E. *Explore* step and imperatives. Section C is a parent’s reply, *Gardens Can Wait*, with questions on claim, evidence and transitions (Term 1 Unit Test 2), followed by questions comparing the two texts. Section D applies persuasive and emotive techniques to new sentences (Term 2 Unit Test 1). The printable adds a P.E.E.E. paragraph, a comparison of how the two writers use concession, sentence rewriting and a 300-word persuasive speech or letter (20 marks). Both texts are original. Only the Level 2/3 paper is written; the Level 1 format (three shorter papers) is not covered here.

### Mathematics

The two papers split the course by unit, so each can be timed as one sitting of about 60 minutes. Paper 1 uses no calculator for Section A and allows one for Q25–Q32. Paper 2 needs a calculator, a ruler and compasses (the construction question is in the printable only). Both papers draw their diagrams in as you scroll: number lines, an area model, a lift loaded with boxes, a pair of lines crossing on a graph, parallel lines, polygons, a ladder, circles and compound shapes. Diagrams are not to scale.

### Science

Section A covers atomic structure, electronic structure, the periodic table and ionic, covalent and metallic bonding. Section B covers photosynthesis, chlorophyll, uses of glucose, magnesium and nitrate, and the pondweed and starch-test investigations. Sections C–E cover density (including displacement and why ice floats), waves read from a graph, sound, heat and temperature, convection and conduction, V = IR, and series and parallel circuits. The printable adds six written questions: a dot-and-cross diagram, conduction in molten salt, the pondweed data, why a steel ship floats, sound in a vacuum, and series versus parallel lamps.

## Checks

All four interactive sheets pass `scripts/mcq_audit.py` (spread of correct letters and no answers given away in the teaching boxes), and their printables are in sync according to `scripts/mcq_sync.py`.

## Structure

```
s2/sem1/
├── README.md
├── sem1-english-level23-mock.html                ← Interactive (English Level 2/3)
├── sem1-english-level23-mock.md                  ← Printable + Q42–Q45 written
├── sem1-english-level23-mock-answers.md          ← Answers + marking guide
├── sem1-maths-paper1-number-algebra.html         ← Interactive (Maths Paper 1, Units 1–3)
├── sem1-maths-paper1-number-algebra.md           ← Printable + Q33–Q37 written
├── sem1-maths-paper1-number-algebra-answers.md   ← Answers + marking guide
├── sem1-maths-paper2-equations-geometry.html     ← Interactive (Maths Paper 2, Units 4, 5, 7)
├── sem1-maths-paper2-equations-geometry.md       ← Printable + Q32–Q36 written
├── sem1-maths-paper2-equations-geometry-answers.md ← Answers + marking guide
├── sem1-science-mock.html                        ← Interactive (Science)
├── sem1-science-mock.md                          ← Printable + Q40–Q45 written
└── sem1-science-mock-answers.md                  ← Answers + marking guide
```
