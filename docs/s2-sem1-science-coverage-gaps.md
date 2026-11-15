# S2 Science Semester Assessment — Coverage Gaps

**Paper:** Science, Friday 27 November 2026 (one paper).
**Checked against:** the S2 Science SA2 revision topic list (`material/science/s2/S2 SA Revision Pack.docx.pdf`, not tracked in git).
**Checked on:** 14 November 2026; updated 15 November 2026 after checking the class slides again.

This compares every topic on the revision list with what the S2 science sheets on the site already cover. The sheets checked were the Term 1 and Term 2 science sheets, the Semester 1 mock, the review page and the bonding drill (`s2/sem1/`), the science formula sheets, and the new Unit Test sheet (`s2/t2/w7/`). It lists what still needs work before the paper.

## Coverage by topic

| Revision topic | Status | Where it is covered |
|---|---|---|
| **Chemistry/Physics: Chemical Structures and Properties** | | |
| Atomic structure | ✅ Covered | `sem1-science-revision`, `sem1-science-mock`, formula sheet 1 |
| Periodic table and properties | ✅ Covered | same as above, plus `t1/w3` ionic bonding |
| Simple and giant molecules | ✅ Covered | `sem1-science-gaps` Section E, plus one question each in `sem1-science-bonding-ions` and `sem1-science-revision` |
| Density | ✅ Covered | `t2/w4` density sheet, mock, review |
| **Chemistry: Chemical Bonding** | | |
| Covalent bond | ✅ Covered | `t1/w4`, `sem1-science-bonding-ions` |
| Ion and ionic bond | ✅ Covered | `t1/w3`, `sem1-science-bonding-ions` |
| **Biology: Plant Biology** | | |
| Minerals | ✅ Covered | `t1/w7` Plant Biology unit test |
| Absorption, transport and transpiration | ✅ Covered | `sem1-science-gaps` Section B only |
| Photosynthesis | ✅ Covered | `t1/w7` unit test, mock, review |
| Carbon cycle | ✅ Covered | `sem1-science-gaps` Section C only |
| **Physics: Sound** | | |
| Waveform, amplitude and frequency, interference | ✅ Covered | `t2/w4` sound & thermal energy sheet |
| **Physics: Thermal Energy** | | |
| Conservation of energy | ✅ Covered | `sem1-science-gaps` Section D (energy transfers, useful and wasted energy, Sankey diagrams); also taught in class as **heat conservation** (slides 3.3 "Conserve Energy": insulation, double glazing, saving energy and cost); covered in Section E of the `t2/w4` sound & thermal energy printable and the `t2/w4` thermal-energy extra questions. |
| Heat and temperature; conduction, convection, radiation; cooling and evaporating | ✅ Covered | `t2/w4` sound & thermal energy sheet |
| **Biology: Human Biology** | | |
| Structure and function of the human excretory system | ✅ Covered | `sem1-science-gaps` Section A only |
| Chromosomes, genes and DNA | ✅ Covered | `t2/w7` Unit Test (Electricity + Human Biology) only |
| Gametes and inheritance | ✅ Covered | `t2/w7` Unit Test only |
| Fetal development and mother's health | ✅ Covered | `t2/w7` Unit Test only |
| **Physics: Electricity** | | |
| Circuit diagrams and symbols; calculating resistance, voltage and current | ✅ Covered | `t2/w4` electricity sheet, `t2/w7` Unit Test, mock, review, formula sheets |

## To do

1. ~~**Gaps drill** for the 27 November paper.~~ Done: `s2/sem1/sem1-science-gaps` (37 questions, 49 marks, plus 6 written), built from `scripts/review_specs/s2_sem1_science_gaps.py`. It covers:
   - the human excretory system (kidneys, ureters, bladder, urethra; filtering blood, urea and urine)
   - absorption, transport and transpiration in plants (root hair cells, xylem and phloem, water loss through stomata)
   - the carbon cycle (photosynthesis, respiration, combustion, decomposition)
   - conservation of energy (energy is not created or destroyed, only transferred; useful and wasted energy)
   - simple molecules vs giant structures (melting points, conductivity, examples)
2. ~~**Human Biology in the semester materials.**~~ Done: `s2/sem1/README.md` now points to the `t2/w7` Unit Test for Human Biology and has a table of revision videos, including one for each gap topic. The mock and the review page still have no Human Biology questions of their own.

## Source material note

The class slide PDFs in `material/science/` (Unit 2 Plant Biology; Atomic Structure, Periodic Table, Chemical Bonding; Human Reproduction) do **not** cover the excretory system, transpiration, the carbon cycle or giant structures. `S2 SA Revision Pack.docx.pdf` is only the two-page topic list, with no practice questions.

What the material does have:

- **Conservation of energy:** the Sound Wave, Thermal Energy and Electricity slides (`material/science/s2/t2/w4/`) have a section headed "3.3 Conversion of Energy / Conserve Energy". It teaches heat conservation (insulation, double glazing, why it matters), which is probably what the revision list means.
- **Carbon cycle:** the Plant Biology slides compare photosynthesis with respiration and mention CO₂ levels in the air. `s1/science/chemical-reactions.html` covers combustion and decomposition. There is no cycle diagram anywhere.
- **Simple vs giant structures:** one comparison row (melting point, simple molecule, giant) in `sem1-science-bonding-ions`. Nothing on diamond, graphite or sand.
- **Excretory system:** the only mention is "increased chance of kidney defects" in the Human Reproduction slides.
- **Absorption, transport and transpiration:** nothing on xylem, phloem, root hair cells or stomata.

So the excretory system and plant transport have to be written from the Cambridge Lower Secondary Stage 9 syllabus. Check the content against any class notes before relying on it.
