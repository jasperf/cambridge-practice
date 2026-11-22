# Documentation

This directory contains technical documentation for the Cambridge Practice interactive worksheets project.

---

## Table of Contents

| File | Description |
|------|-------------|
| [state-management.md](state-management.md) | Explains how the interactive test sheets track user answers, correctness, and scores in real-time. Covers the state object structure, state flow, how state is updated and consumed, persistence via localStorage, and the single source of truth principle. |
| [s2-sem1-science-coverage-gaps.md](s2-sem1-science-coverage-gaps.md) | Checks the S2 Science SA2 revision list against the sheets on the site, topic by topic. Lists what is missing or thin before the 27 November paper (excretory system, carbon cycle, transpiration and transport, conservation of energy, simple vs giant structures) and the to-do list for a gaps drill. |

---

## About This Project

The Cambridge Practice project provides **interactive, self-marking exercise sheets** for Cambridge Secondary 1, IGCSE, and A-Level students. Each worksheet is a standalone HTML file with:

- No build tools or frameworks required
- No CDN dependencies (except Google Fonts)
- Full offline functionality once loaded
- Instant answer checking with hints
- Score tracking and progress visualization
- Results persistence via localStorage

---

## Documentation Structure

Files in this `docs/` directory provide:

- **Architecture explanations** - How the interactive features work under the hood
- **Code patterns** - Reusable patterns used across worksheets
- **Reference guides** - For maintaining and extending the codebase

---

## Adding New Documentation

When adding new documentation:

1. Create a new `.md` file in this directory
2. Add it to the Table of Contents above
3. Follow the existing format and style
4. Keep explanations concise and code-focused

---

## See Also

- [Main README](../README.md) - Project overview
- [Contributing](../CONTRIBUTING.md) - Structure, local development, adding sheets, PDFs
- [SETUP.md](../SETUP.md) - Detailed setup and development guide
- [AGENTS.md](../AGENTS.md) - Agent instructions and workflows
