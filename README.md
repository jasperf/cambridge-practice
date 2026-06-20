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

The **Python Game Development course** sheets also include hands-on coding projects using the Arcade library.

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
│   └── python/                       ← Legacy directory (empty)
├── python/                          ← Python Game Development Course
│   ├── README.md                    ← Course overview, setup guide, learning path
│   ├── index.html                   ← Python course landing page
│   ├── arcade-intro.html            ← Arcade basics (10 marks)
│   ├── sprites-graphics.html         ← Sprites & Graphics (10 marks)
│   ├── basics/
│   │   └── movement-physics.html     ← Movement & Physics (10 marks)
│   ├── platformer/
│   │   ├── part1-project-setup.html  ← Project Setup (10 marks)
│   │   ├── part2-player.html        ← Player Class & Movement (10 marks)
│   │   └── part3-platforms.html      ← Platforms & Collision (10 marks)
│   └── challenges/                   ← Practice exercises (planned)
├── igcse/                           ← IGCSE (planned)
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

### Python Game Development

| Course | Topics | Status |
|--------|--------|--------|
| Arcade Introduction | Setup, first window, game loop | ✅ 10 marks |
| Sprites & Graphics | Loading images, Sprite class, scaling | ✅ 10 marks |
| Movement & Physics | Velocity, position, keyboard input | ✅ 10 marks |
| Platformer Part 1 | Project setup, Game class, constants | ✅ 10 marks |
| Platformer Part 2 | Player class, keyboard controls | ✅ 10 marks |
| Platformer Part 3 | Platforms, SpriteLists, collision | ✅ 10 marks |
| Platformer Parts 4-9 | Jumping, camera, coins, enemies, levels, polish | 🔜 Coming |
| Challenge Sheets | Debugging, code tracing, puzzles | 🔜 Planned |

### IGCSE

| Subject | Topics | Status |
|---------|--------|--------|
| Physics (Electricity & Magnetism) | Core + Extended | 🔜 Coming |
| Mathematics (Statistics & Probability) | Core + Extended | 🔜 Coming |

## Tech

Pure HTML + CSS + JavaScript. No frameworks, no build tools, no CDN dependencies beyond Google Fonts. Every file works offline once loaded.

The Python course requires Python 3.8+ and the Arcade library (`pip3 install arcade`).

---

*Maintained for Cambridge curriculum students. Not affiliated with Cambridge Assessment International Education.*
