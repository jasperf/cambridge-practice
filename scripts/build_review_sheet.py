#!/usr/bin/env python3
"""Build a self-contained review sheet (.html + .md printable + -answers.md) from a spec.

    python3 scripts/build_review_sheet.py scripts/review_specs/s2_sem1_science_revision.py

A review sheet covers several topics. Each topic section has a grid of key-fact
cards, an optional interactive explorer, then auto-marked questions (MCQ, typed
number or typed word). The printable adds the written questions that the html
cannot mark.

The spec is a plain Python file defining:

  META        dict: out (basename, repo-relative), title, badge, eyebrow, h1,
              md_title, intro, md_intro, time_chip, storage_key, back,
              answers_note, extra_links [(href, label), ...]
  SECTIONS    list of dicts: key, icon, color, rgba, title, label, src, link,
              optional link2 (href, label), facts [(heading, html), ...]
  Q           list of question dicts (see the num/text/mcq helpers in the spec)
  WRITTEN     list of (number, marks, question, marking guide) — printable only
  EXPLORERS   optional dict: section key -> raw html placed after the facts
  EXPLORER_CSS / EXPLORER_JS   optional strings appended to the page

The output is ordinary static HTML with no dependencies beyond Google Fonts,
like every other sheet. Re-running the builder overwrites all three files, so
edit the spec rather than the generated files. Afterwards run the usual checks:
mcq_audit.py, mcq_sync.py and sheet_audit.py.
"""
import html as H
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LETTERS = 'abcd'


def load(path):
    spec = importlib.util.spec_from_file_location('review_spec', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def js_str(s):
    """Text for a single-quoted JS string inside a double-quoted onclick attribute."""
    return s.replace('\\', '\\\\').replace("'", '’').replace('"', '&quot;')


SUP = str.maketrans('0123456789+-−', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻')
SUB = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')


def to_md(s):
    """Html fragment -> GFM text."""
    s = re.sub(r'<sup>(.*?)</sup>', lambda m: m.group(1).translate(SUP), s)
    s = re.sub(r'<sub>(.*?)</sub>', lambda m: m.group(1).translate(SUB), s)
    s = re.sub(r'</?(strong|b)>', '**', s)
    s = re.sub(r'</?(em|i)>', '*', s)
    s = re.sub(r'<br\s*/?>', ' · ', s)
    s = re.sub(r'<[^>]+>', '', s)
    return H.unescape(s).strip()


def mark_label(n):
    return f'{n} mark' + ('s' if n != 1 else '')


# ---------------------------------------------------------------- html parts

def q_card(q, n):
    qid = q['id']
    head = (f'    <div class="q-header"><div class="q-num">Q{n}</div><div class="q-text">{q["q"]}</div>'
            f'<div class="q-marks">{mark_label(q["marks"])}</div></div>\n')
    body = '    <div class="q-body">\n'
    if q.get('fig'):
        body += '      ' + q['fig'] + '\n'
    if q['kind'] == 'num':
        body += (f'      <div class="num-row"><input type="number" step="any" class="num-input" id="{qid}-ans" '
                 f'placeholder="Enter answer..."><span class="num-unit">{q.get("unit", "")}</span></div>\n')
        check = f"checkNum('{qid}',{q['ans']},'Q{n}',{q.get('tol', 0)})"
    elif q['kind'] == 'text':
        body += (f'      <input type="text" class="text-input" id="{qid}-ans" placeholder="{q.get("ph", "")}" '
                 f'autocomplete="off">\n')
        acc = ','.join("'" + js_str(a) + "'" for a in q['acc'])
        check = f"checkText('{qid}',[{acc}],'Q{n}')"
    else:
        body += f'      <div class="mcq-options" id="{qid}-opts">\n'
        for letter, opt in zip(LETTERS, q['opts']):
            body += (f'        <div class="mcq-opt" onclick="selectMCQ(\'{qid}\', this, \'{letter}\')">'
                     f'<div class="opt-indicator"></div><span>{opt}</span></div>\n')
        body += '      </div>\n'
        check = f"checkMCQ('{qid}','{q['correct']}','Q{n}')"
    body += ('      <div class="q-actions">\n'
             f'        <button class="btn btn-check" onclick="{check}">Check</button>\n'
             f'        <button class="btn btn-hint" onclick="showHint(\'{qid}\',\'{js_str(q["hint"])}\')">Hint</button>\n'
             f'        <button class="btn btn-reveal" onclick="revealAnswer(\'{qid}\',\'{js_str(q["reveal"])}\')">Show Answer</button>\n'
             '      </div>\n'
             f'      <div class="feedback" id="{qid}-fb"></div>\n'
             '    </div>\n')
    return f'  <!-- Q{n} -->\n  <div class="q-card" id="qcard-{qid}">\n{head}{body}  </div>\n\n'


def build_html(spec):
    M, S, Q = spec.META, spec.SECTIONS, spec.Q
    explorers = getattr(spec, 'EXPLORERS', {})
    total = sum(q['marks'] for q in Q)
    num = {q['id']: i + 1 for i, q in enumerate(Q)}
    out = [PAGE_HEAD.replace('%TITLE%', M['title']).replace('%EXTRA_CSS%', getattr(spec, 'EXPLORER_CSS', ''))]
    out.append(f'''<body>
<canvas id="confetti-canvas"></canvas>
<div class="topbar">
  <div class="topbar-left">
    <div class="logo">Student<span>'s</span> Study Hub</div>
    <div class="week-badge">{M['badge']}</div>
  </div>
  <div style="display:flex;align-items:center;gap:14px;">
    <a href="{M['back']}" class="back-link">&larr; All sheets</a>
    <div class="timer-wrap">&#9201;<div class="timer" id="timer">00:00</div></div>
    <div class="score-pill"><div class="score-label">Score</div><div class="score-val" id="global-score">0 / {total}</div></div>
  </div>
</div>
<div class="progress-wrap"><div class="progress-bar" id="progress-bar"></div></div>
<div class="hero">
  <div class="hero-eyebrow">{M['eyebrow']}</div>
  <h1>{M['h1']}</h1>
  <div class="hero-meta">
    <div class="hero-chip"><div class="dot"></div>{len(Q)} questions &middot; self-marked &middot; {total} marks</div>
    <div class="hero-chip"><div class="dot" style="background:var(--accent-warn)"></div>{M['time_chip']}</div>
  </div>
  <p class="credit">{M['intro']}</p>
  <button class="btn btn-cover" id="cover-btn" onclick="toggleCover()">&#128584; Cover the notes</button>
</div>
''')
    out.append('<div class="section-tabs">\n')
    for s in S:
        out.append(f'  <a href="#{s["key"]}" class="sub-tab">{s["icon"]} {s["title"]}</a>\n')
    out.append('</div>\n<div class="main">\n\n')

    for si, s in enumerate(S):
        qs = [q for q in Q if q['sec'] == s['key']]
        first, last = num[qs[0]['id']], num[qs[-1]['id']]
        smax = sum(q['marks'] for q in qs)
        letter = chr(ord('A') + si)
        links = f'<a class="src-link" href="{s["link"]}" target="_blank" rel="noopener">Full sheet &rarr;</a>'
        if s.get('link2'):
            links += f' <a class="src-link" href="{s["link2"][0]}" target="_blank" rel="noopener">{s["link2"][1]} &rarr;</a>'
        out.append(f'<div id="{s["key"]}" style="--sec:{s["color"]};--sec-rgb:{s["rgba"]}">\n')
        out.append(f'  <div class="section-header"><div class="section-icon">{s["icon"]}</div><div>'
                   f'<div class="sub-label">Section {letter} &middot; Q{first}&ndash;Q{last} &middot; {s["src"]}</div>'
                   f'<h2>{s["title"]}</h2></div><div class="src-links">{links}</div></div>\n')
        out.append('  <div class="facts-label">Key facts</div>\n  <div class="facts">\n')
        for h, body in s['facts']:
            out.append(f'    <div class="fact" onclick="this.classList.toggle(\'peek\')"><h4>{h}</h4><div class="fact-body">{body}</div></div>\n')
        out.append('  </div>\n')
        if s['key'] in explorers:
            out.append('  ' + explorers[s['key']] + '\n')
        out.append('  <div class="facts-label">Check yourself</div>\n')
        for q in qs:
            out.append(q_card(q, num[q['id']]))
        out.append(f'''  <div class="section-score">
    <div class="section-score-label">SECTION {letter} &mdash; {H.escape(s['label'].upper())}</div>
    <div class="section-score-bar"><div class="section-score-fill" id="sec-{s['key']}-fill"></div></div>
    <div class="section-score-val" id="sec-{s['key']}-val">0/{smax}</div>
  </div>
</div>
<div class="divider"></div>

''')

    out.append('''<div class="results-panel" id="results-panel">
  <div class="results-grade" id="results-grade">0%</div>
  <div class="results-label" id="results-label">Keep Practising</div>
  <div class="results-breakdown" id="results-breakdown"></div>
</div>

</div>

<script>
const state = { answers: {}, correct: {}, startTime: Date.now() };

''')
    out.append('const marks = { ' + ', '.join(f"{q['id']}:{q['marks']}" for q in Q) + ' };\n\n')
    out.append('const sections = {\n' + ',\n'.join(
        f"  {s['key']}: {{ label: '{js_str(s['label'])}', qs: [" +
        ','.join(f"'{q['id']}'" for q in Q if q['sec'] == s['key']) + '] }' for s in S) + '\n};\n')
    out.append(PAGE_SCRIPT.replace('%KEY%', M['storage_key']))
    out.append(getattr(spec, 'EXPLORER_JS', ''))
    out.append('</script>\n</body>\n</html>\n')
    return ''.join(out)


# ---------------------------------------------------------------- markdown

def build_md(spec, answers_name):
    M, S, Q, W = spec.META, spec.SECTIONS, spec.Q, spec.WRITTEN
    total = sum(q['marks'] for q in Q)
    wtotal = sum(w[1] for w in W)
    num = {q['id']: i + 1 for i, q in enumerate(Q)}
    o = [f"# {M['md_title']}\n\n",
         f"**{len(Q)} questions · {total} marks** (+ {len(W)} written questions, {wtotal} marks)\n\n",
         f"{M['md_intro']}\n\n---\n\n"]
    for si, s in enumerate(S):
        o.append(f"## Section {chr(65 + si)}: {to_md(s['title'])}\n\n### Key facts\n\n")
        for h, body in s['facts']:
            o.append(f"- **{to_md(h)}:** {to_md(body)}\n")
        o.append('\n### Questions\n\n')
        for q in (q for q in Q if q['sec'] == s['key']):
            o.append(f"**Q{num[q['id']]}** ({mark_label(q['marks'])})\\\n{to_md(q['q'])}\n")
            if q.get('figmd'):
                o.append(f"\n**Diagram:** {q['figmd']}\n")
            if q['kind'] == 'mcq':
                for L, opt in zip('ABCD', q['opts']):
                    o.append(f"- {L}) {to_md(opt)}\n")
            else:
                unit = (' ' + to_md(q['unit'])) if q.get('unit') else ''
                o.append(f"\nAnswer: ____________________{unit}\n")
            o.append('\n')
        o.append('---\n\n')
    o.append(f"## Written questions\n\nAnswer these in your notebook. They are not on the interactive sheet.\n\n")
    for n, mk, text, _ in W:
        o.append(f"**Q{n}** ({mark_label(mk)})\\\n{text}\n\n")
    o.append(f"---\n\n*Note: Q1–Q{len(Q)} match the interactive sheet's questions exactly, so they can be "
             f"self-checked there. Q{W[0][0]}–Q{W[-1][0]} are written questions for the notebook and are not "
             f"auto-marked. Answers and a marking guide are in [`{answers_name}`](./{answers_name}).*\n")
    return ''.join(o)


def build_answers(spec):
    M, S, Q, W = spec.META, spec.SECTIONS, spec.Q, spec.WRITTEN
    num = {q['id']: i + 1 for i, q in enumerate(Q)}
    o = [f"# {M['md_title']} — Answers\n\n{M['answers_note']}\n\n---\n\n"]
    for si, s in enumerate(S):
        o.append(f"## Section {chr(65 + si)}: {to_md(s['title'])}\n\n")
        for q in (q for q in Q if q['sec'] == s['key']):
            rev = to_md(q['reveal'])
            if q['kind'] == 'mcq':
                L = q['correct'].upper()
                opt = to_md(q['opts'][LETTERS.index(q['correct'])])
                rev = re.sub(r'^[A-D]\s*—\s*', '', rev)
                o.append(f"**Q{num[q['id']]}** ({mark_label(q['marks'])}): **{L}**: {opt} {rev}\n\n")
            else:
                o.append(f"**Q{num[q['id']]}** ({mark_label(q['marks'])}): {rev}\n\n")
    o.append('## Written questions: marking guide\n\n')
    for n, mk, _, guide in W:
        o.append(f"**Q{n}** ({mark_label(mk)}): {guide}\n\n")
    return ''.join(o)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    spec = load(sys.argv[1])
    base = ROOT / spec.META['out']
    answers = base.name + '-answers.md'
    files = {base.with_suffix('.html'): build_html(spec),
             base.with_suffix('.md'): build_md(spec, answers),
             base.parent / answers: build_answers(spec)}
    for path, text in files.items():
        path.write_text(text, encoding='utf-8')
        print('wrote', path.relative_to(ROOT))


# ---------------------------------------------------------------- templates

PAGE_HEAD = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%TITLE%</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,600;0,9..144,700;1,9..144,400&family=DM+Mono:wght@400;500&family=Literata:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>:root {
  --bg: #0f1117; --surface: #181c27; --surface2: #1e2336; --border: #2a3050;
  --accent: #3ecf8e; --accent-math: #4f8ef7; --accent-sci: #3ecf8e; --accent-warn: #f5a623;
  --text: #e8eaf0; --text-muted: #7a84a0; --text-dim: #4a5270;
  --correct: #2ecc71; --wrong: #e74c3c;
  --font-display: 'Fraunces', Georgia, serif; --font-body: 'Literata', Georgia, serif; --font-mono: 'DM Mono', monospace;
  --radius: 10px;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { background: var(--bg); color: var(--text); font-family: var(--font-body); font-size: 16px; line-height: 1.7; min-height: 100vh; overflow-x: hidden; }
body::before { content: ''; position: fixed; inset: 0; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E"); pointer-events: none; z-index: 0; opacity: 0.6; }
.topbar { position: sticky; top: 0; z-index: 100; background: rgba(15,17,23,0.92); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between; padding: 0 28px; height: 58px; gap: 16px; }
.topbar-left { display: flex; align-items: center; gap: 14px; }
.logo { font-family: var(--font-display); font-size: 1.15rem; font-weight: 700; color: var(--text); letter-spacing: -0.3px; }
.logo span { color: var(--accent); }
.week-badge { font-family: var(--font-mono); font-size: 0.7rem; background: var(--surface2); border: 1px solid var(--border); color: var(--text-muted); padding: 3px 10px; border-radius: 20px; letter-spacing: 0.5px; }
.back-link { font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-muted); text-decoration: none; }
.back-link:hover { color: var(--accent-math); }
.score-pill { display: flex; align-items: center; gap: 10px; background: var(--surface); border: 1px solid var(--border); border-radius: 24px; padding: 5px 16px 5px 10px; }
.score-label { font-family: var(--font-mono); font-size: 0.7rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; }
.score-val { font-family: var(--font-display); font-size: 1.1rem; font-weight: 600; color: var(--accent); min-width: 52px; text-align: right; }
.progress-wrap { height: 3px; background: var(--border); }
.progress-bar { height: 100%; background: linear-gradient(90deg, var(--accent-math), var(--accent-sci), var(--accent-warn)); width: 0%; transition: width 0.6s cubic-bezier(0.34,1.56,0.64,1); }
.hero { position: relative; z-index: 1; padding: 52px 28px 24px; max-width: 900px; margin: 0 auto; }
.hero-eyebrow { font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 2px; text-transform: uppercase; color: var(--text-dim); margin-bottom: 12px; }
.hero h1 { font-family: var(--font-display); font-size: clamp(2rem, 5vw, 3.2rem); font-weight: 700; line-height: 1.1; letter-spacing: -1px; margin-bottom: 14px; }
.hero h1 em { font-style: italic; color: var(--accent); }
.hero-meta { display: flex; gap: 20px; flex-wrap: wrap; margin-top: 18px; }
.hero-chip { display: flex; align-items: center; gap: 7px; font-size: 0.85rem; color: var(--text-muted); }
.hero-chip .dot { width: 8px; height: 8px; border-radius: 50%; background: var(--accent); }
.credit { font-size: 0.88rem; color: var(--text-muted); margin-top: 12px; max-width: 720px; }
.btn-cover { margin-top: 16px; background: var(--surface2); border: 1px solid var(--border); color: var(--text); }
.btn-cover:hover { border-color: var(--accent); }
body.cover .btn-cover { border-color: var(--accent-warn); color: var(--accent-warn); }
.section-tabs { position: sticky; top: 58px; z-index: 50; background: rgba(15,17,23,0.92); backdrop-filter: blur(12px); max-width: 100%; padding: 10px max(28px, calc((100% - 844px) / 2)); display: flex; gap: 8px; overflow-x: auto; scrollbar-width: none; border-bottom: 1px solid var(--border); }
.sub-tab { font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.3px; padding: 6px 12px; border-radius: 6px; border: 1px solid var(--border); background: var(--surface); color: var(--text-muted); text-decoration: none; transition: all 0.2s; white-space: nowrap; }
.sub-tab:hover { border-color: var(--accent); color: var(--text); }
.main { position: relative; z-index: 1; max-width: 900px; margin: 0 auto; padding: 0 28px 80px; }
.main > div[id] { scroll-margin-top: 120px; }
.section-header { display: flex; align-items: center; gap: 14px; margin: 44px 0 18px; flex-wrap: wrap; }
.section-icon { width: 42px; height: 42px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; flex-shrink: 0; background: rgba(var(--sec-rgb),0.15); }
.section-header h2 { font-family: var(--font-display); font-size: 1.45rem; font-weight: 600; letter-spacing: -0.3px; }
.section-header .sub-label { font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-muted); letter-spacing: 1px; text-transform: uppercase; margin-top: 2px; }
.src-links { margin-left: auto; display: flex; gap: 8px; flex-wrap: wrap; }
.src-link { font-family: var(--font-mono); font-size: 0.7rem; color: var(--text-muted); text-decoration: none; border: 1px solid var(--border); border-radius: 6px; padding: 5px 10px; }
.src-link:hover { color: var(--sec); border-color: var(--sec); }
.facts-label { font-family: var(--font-mono); font-size: 0.7rem; letter-spacing: 1.5px; text-transform: uppercase; color: var(--sec); margin: 6px 0 10px; }
.facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 10px; margin-bottom: 26px; }
.fact { background: var(--surface2); border: 1px solid var(--border); border-top: 3px solid var(--sec); border-radius: 8px; padding: 12px 14px; font-size: 0.86rem; line-height: 1.6; cursor: default; }
.fact h4 { font-family: var(--font-mono); font-size: 0.7rem; font-weight: 500; letter-spacing: 1px; text-transform: uppercase; color: var(--text-muted); margin-bottom: 6px; }
.fact em { color: var(--sec); }
.fact .f { font-family: var(--font-mono); font-size: 0.82rem; color: var(--accent-warn); }
.fact-body { transition: filter 0.25s, opacity 0.25s; }
body.cover .fact { cursor: pointer; }
body.cover .fact:not(.peek) .fact-body { filter: blur(6px); opacity: 0.5; user-select: none; }
.explorer { background: linear-gradient(135deg, rgba(var(--sec-rgb),0.07), rgba(var(--sec-rgb),0.02)); border: 1px solid var(--border); border-radius: 12px; padding: 18px 20px; margin: 0 0 28px; }
.explorer h3 { font-family: var(--font-display); font-size: 1.1rem; margin-bottom: 2px; }
.ex-note { font-size: 0.84rem; color: var(--text-muted); margin-bottom: 14px; }
.ex-row { display: flex; gap: 18px; flex-wrap: wrap; align-items: center; }
.ex-svg { width: 100%; max-width: 420px; background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; display: block; }
.ex-svg.wide { max-width: 100%; }
.ex-controls { flex: 1 1 220px; display: flex; flex-direction: column; gap: 6px; min-width: 0; }
.ex-controls label { font-family: var(--font-mono); font-size: 0.74rem; color: var(--text-muted); }
.ex-controls input[type=range] { width: 100%; accent-color: var(--sec); }
.ex-readout { font-family: var(--font-mono); font-size: 0.8rem; line-height: 1.7; background: var(--surface2); border: 1px solid var(--border); border-radius: 6px; padding: 10px 12px; margin-top: 6px; color: var(--text); }
.ex-readout strong { color: var(--sec); }
.q-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); margin-bottom: 14px; overflow: hidden; transition: border-color 0.3s; animation: slideIn 0.35s ease both; }
.q-card.answered-correct { border-color: var(--correct); }
.q-card.answered-wrong { border-color: var(--wrong); }
.q-header { display: flex; align-items: flex-start; gap: 14px; padding: 16px 20px 12px; border-bottom: 1px solid var(--border); }
.q-num { font-family: var(--font-mono); font-size: 0.72rem; background: var(--surface2); border: 1px solid var(--border); color: var(--text-muted); padding: 3px 8px; border-radius: 4px; flex-shrink: 0; margin-top: 2px; }
.q-text { font-size: 0.96rem; color: var(--text); flex: 1; line-height: 1.6; }
.q-marks { font-family: var(--font-mono); font-size: 0.7rem; color: var(--accent); background: rgba(62,207,142,0.1); border: 1px solid rgba(62,207,142,0.2); padding: 3px 8px; border-radius: 4px; flex-shrink: 0; white-space: nowrap; }
.q-body { padding: 14px 20px; }
.mcq-options { display: flex; flex-direction: column; gap: 8px; }
.mcq-opt { display: flex; align-items: center; gap: 12px; background: var(--surface2); border: 1.5px solid var(--border); border-radius: 7px; padding: 10px 14px; cursor: pointer; transition: all 0.18s; font-size: 0.92rem; user-select: none; }
.mcq-opt:hover:not(.disabled) { border-color: var(--accent); }
.mcq-opt.selected { border-color: var(--accent); background: rgba(62,207,142,0.1); }
.mcq-opt.correct { border-color: var(--correct); background: rgba(46,204,113,0.1); }
.mcq-opt.wrong { border-color: var(--wrong); background: rgba(231,76,60,0.08); }
.mcq-opt.disabled { cursor: default; }
.opt-indicator { width: 20px; height: 20px; border-radius: 50%; border: 2px solid var(--border); flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; transition: all 0.2s; }
.mcq-opt.selected .opt-indicator { border-color: var(--accent); background: var(--accent); color: #0f1117; }
.mcq-opt.correct .opt-indicator { border-color: var(--correct); background: var(--correct); color: #fff; }
.mcq-opt.wrong .opt-indicator { border-color: var(--wrong); background: var(--wrong); color: #fff; }
.num-row { display: flex; gap: 10px; align-items: center; flex-wrap: wrap; }
.num-input { width: 130px; background: var(--surface2); border: 1.5px solid var(--border); border-radius: 6px; color: var(--text); font-family: var(--font-mono); font-size: 1.05rem; padding: 9px 12px; text-align: center; transition: border-color 0.2s; outline: none; }
.num-input:focus { border-color: var(--accent); }
.num-input.correct { border-color: var(--correct); }
.num-input.wrong { border-color: var(--wrong); }
.num-unit { font-size: 0.85rem; color: var(--text-muted); }
.text-input { font-family: var(--font-mono); font-size: 0.95rem; background: var(--surface2); border: 1.5px solid var(--border); color: var(--text); border-radius: 7px; padding: 10px 14px; width: 100%; max-width: 320px; outline: none; transition: border-color 0.18s; }
.text-input:focus { border-color: var(--accent); }
.text-input:disabled { opacity: 0.75; }
.q-actions { display: flex; gap: 8px; margin-top: 14px; flex-wrap: wrap; }
.btn { font-family: var(--font-mono); font-size: 0.78rem; letter-spacing: 0.3px; padding: 8px 16px; border-radius: 6px; border: none; cursor: pointer; transition: all 0.18s; }
.btn-check { background: var(--accent); color: #0f1117; }
.btn-check:hover { opacity: 0.85; transform: translateY(-1px); }
.btn-hint { background: var(--surface2); border: 1px solid var(--border); color: var(--text-muted); }
.btn-hint:hover { border-color: var(--accent-warn); color: var(--accent-warn); }
.btn-reveal { background: transparent; border: 1px solid var(--border); color: var(--text-dim); font-size: 0.72rem; }
.btn-reveal:hover { color: var(--text-muted); }
.feedback { display: none; margin-top: 12px; padding: 10px 14px; border-radius: 6px; font-size: 0.88rem; line-height: 1.6; }
.feedback.show { display: block; }
.feedback.correct-fb { background: rgba(46,204,113,0.1); border: 1px solid rgba(46,204,113,0.3); color: #7ef5b0; }
.feedback.wrong-fb { background: rgba(231,76,60,0.1); border: 1px solid rgba(231,76,60,0.3); color: #f5a0a0; }
.feedback.hint-fb { background: rgba(245,166,35,0.08); border: 1px solid rgba(245,166,35,0.2); color: var(--accent-warn); }
.feedback.reveal-fb { background: rgba(122,132,160,0.1); border: 1px solid var(--border); color: var(--text-muted); }
.section-score { display: flex; align-items: center; gap: 12px; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 12px 16px; margin-top: 24px; }
.section-score-label { font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-muted); flex: 1; }
.section-score-val { font-family: var(--font-display); font-size: 1.2rem; font-weight: 600; color: var(--sec, var(--accent)); }
.section-score-bar { flex: 2; height: 6px; background: var(--border); border-radius: 3px; overflow: hidden; }
.section-score-fill { height: 100%; background: var(--sec, var(--accent)); width: 0%; transition: width 0.8s cubic-bezier(0.34,1.56,0.64,1); border-radius: 3px; }
.results-panel { display: none; background: var(--surface); border: 1px solid var(--accent); border-radius: 14px; padding: 32px; margin-top: 40px; text-align: center; animation: popIn 0.5s cubic-bezier(0.34,1.56,0.64,1); }
.results-panel.show { display: block; }
.results-grade { font-family: var(--font-display); font-size: 4rem; font-weight: 700; line-height: 1; margin-bottom: 8px; }
.results-label { font-size: 0.9rem; color: var(--text-muted); margin-bottom: 24px; }
.results-breakdown { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }
.rb-chip { background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; padding: 12px 20px; font-family: var(--font-mono); font-size: 0.78rem; }
.rb-chip .rb-val { font-size: 1.6rem; font-family: var(--font-display); font-weight: 600; display: block; margin-top: 4px; }
.timer-wrap { display: flex; align-items: center; gap: 8px; }
.timer { font-family: var(--font-mono); font-size: 0.85rem; color: var(--text-muted); }
#confetti-canvas { position: fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:999; }
.divider { height: 1px; background: var(--border); margin: 48px 0; position: relative; }
.divider::after { content: '\00a7'; position: absolute; left: 50%; top: 50%; transform: translate(-50%,-50%); background: var(--bg); padding: 0 12px; color: var(--text-dim); font-family: var(--font-display); }
.q-fig { display: block; width: 100%; max-width: 380px; margin: 0 0 16px; background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; }
.q-fig .draw { stroke-dasharray: 1; stroke-dashoffset: 1; }
.q-fig .fill { fill-opacity: 0; }
.q-fig.drawn .draw { animation: drawIn 1.1s ease forwards; }
.q-fig.drawn .fill { animation: fillIn 0.6s ease 0.9s forwards; }
.q-fig text { opacity: 0; }
.q-fig.drawn text { animation: fadeIn 0.5s ease 0.8s forwards; }
@keyframes drawIn { to { stroke-dashoffset: 0; } }
@keyframes fillIn { to { fill-opacity: 1; } }
@keyframes fadeIn { to { opacity: 1; } }
@keyframes slideIn { from { opacity:0; transform:translateY(12px); } to { opacity:1; transform:translateY(0); } }
@keyframes popIn { from { opacity:0; transform:scale(0.92) translateY(20px); } to { opacity:1; transform:scale(1) translateY(0); } }
@keyframes shake { 0%,100%{transform:translateX(0)} 20%{transform:translateX(-6px)} 40%{transform:translateX(6px)} 60%{transform:translateX(-4px)} 80%{transform:translateX(4px)} }
@keyframes pulse-ok { 0%{box-shadow:0 0 0 0 rgba(62,207,142,0.4)} 70%{box-shadow:0 0 0 10px rgba(62,207,142,0)} 100%{box-shadow:0 0 0 0 rgba(62,207,142,0)} }
.shake { animation: shake 0.4s ease; }
.pulse-correct { animation: pulse-ok 0.6s ease; }
@media (prefers-reduced-motion: reduce) {
  .q-fig .draw { stroke-dasharray: none; stroke-dashoffset: 0; }
  .q-fig .fill { fill-opacity: 1; }
  .q-fig text { opacity: 1; }
  .q-fig.drawn .draw, .q-fig.drawn .fill, .q-fig.drawn text { animation: none; }
}
@media (max-width: 600px) {
  .topbar { padding: 10px 16px; height: auto; flex-wrap: wrap; row-gap: 8px; }
  .topbar-left { flex-direction: column; align-items: flex-start; gap: 3px; }
  .section-tabs { top: 0; position: relative; padding: 10px 16px; }
  .hero, .main { padding-left: 16px; padding-right: 16px; }
  .hero h1 { font-size: 1.8rem; }
  .src-links { margin-left: 0; }
  .q-header, .q-body { padding-left: 14px; padding-right: 14px; }
  .explorer { padding: 14px; }
  .results-panel { padding: 20px; }
  .results-grade { font-size: 2.8rem; }
}
%EXTRA_CSS%
</style>
</head>
'''

PAGE_SCRIPT = r'''
const allQs = Object.values(sections).flatMap(s => s.qs);
const maxMarks = allQs.reduce((s,q) => s + marks[q], 0);

function updateTimer() {
  const e = Math.floor((Date.now()-state.startTime)/1000);
  document.getElementById('timer').textContent = `${String(Math.floor(e/60)).padStart(2,'0')}:${String(e%60).padStart(2,'0')}`;
}
setInterval(updateTimer, 1000);

function toggleCover() {
  const on = document.body.classList.toggle('cover');
  document.querySelectorAll('.fact.peek').forEach(f => f.classList.remove('peek'));
  document.getElementById('cover-btn').innerHTML = on ? '&#128064; Show the notes' : '&#128584; Cover the notes';
}

function selectMCQ(qid, el) {
  if (state.correct[qid] !== undefined) return;
  const opts = document.querySelectorAll(`#${qid}-opts .mcq-opt`);
  opts.forEach(o => { o.classList.remove('selected'); o.querySelector('.opt-indicator').textContent = ''; });
  el.classList.add('selected');
  el.querySelector('.opt-indicator').textContent = '✓';
  const match = el.getAttribute('onclick').match(/'([a-d])'\)/);
  if (match) state.answers[qid] = match[1];
}

function checkMCQ(qid, correctVal, label) {
  const selected = state.answers[qid];
  if (!selected) { shakeCard(qid); return; }
  if (state.correct[qid] !== undefined) return;
  const opts = document.querySelectorAll(`#${qid}-opts .mcq-opt`);
  const isCorrect = selected === correctVal;
  opts.forEach(opt => {
    opt.classList.add('disabled');
    const m = opt.getAttribute('onclick').match(/'([a-d])'\)/);
    const v = m ? m[1] : null;
    if (v === correctVal) opt.classList.add('correct');
    else if (opt.classList.contains('selected') && !isCorrect) opt.classList.add('wrong');
  });
  markResult(qid, isCorrect);
}

function checkNum(qid, correctVal, label, tolerance=0) {
  const input = document.getElementById(`${qid}-ans`);
  if (!input || input.value === '') { shakeCard(qid); return; }
  if (state.correct[qid] !== undefined) return;
  const val = parseFloat(input.value);
  const isCorrect = Math.abs(val - correctVal) <= tolerance + 1e-9;
  input.classList.add(isCorrect ? 'correct' : 'wrong');
  input.disabled = true;
  markResult(qid, isCorrect);
}

function normalise(s) {
  return s.toLowerCase().trim().replace(/[.,!?]+$/, '').replace(/[’‘]/g, "'").replace(/[“”"]/g, '').replace(/\s+/g, ' ');
}

function checkText(qid, accepted, label) {
  const input = document.getElementById(`${qid}-ans`);
  const typed = input.value;
  if (!typed.trim()) { shakeCard(qid); return; }
  if (state.correct[qid] !== undefined) return;
  const isCorrect = accepted.map(normalise).includes(normalise(typed));
  input.disabled = true;
  input.style.borderColor = isCorrect ? 'var(--correct)' : 'var(--wrong)';
  state.answers[qid] = typed;
  markResult(qid, isCorrect);
}

function markResult(qid, isCorrect) {
  state.correct[qid] = isCorrect;
  const card = document.getElementById(`qcard-${qid}`);
  card.classList.add(isCorrect ? 'answered-correct' : 'answered-wrong');
  if (isCorrect) card.classList.add('pulse-correct');
  const fb = document.getElementById(`${qid}-fb`);
  fb.className = `feedback show ${isCorrect ? 'correct-fb' : 'wrong-fb'}`;
  fb.innerHTML = isCorrect
    ? `✅ <strong>Correct!</strong> +${marks[qid]} mark${marks[qid]>1?'s':''}`
    : `❌ <strong>Not quite.</strong> Reveal the answer, then look back at the key facts above.`;
  updateScores();
}

function showHint(qid, hintText) {
  const fb = document.getElementById(`${qid}-fb`);
  if (state.correct[qid] !== undefined) return;
  fb.className = 'feedback show hint-fb';
  fb.innerHTML = `💡 <strong>Hint:</strong> ${hintText}`;
}

function revealAnswer(qid, answerText) {
  const fb = document.getElementById(`${qid}-fb`);
  fb.className = 'feedback show reveal-fb';
  fb.innerHTML = `📖 <strong>Answer:</strong> ${answerText}`;
  if (state.correct[qid] === undefined) { state.correct[qid] = false; updateScores(); }
}

function shakeCard(qid) {
  const card = document.getElementById(`qcard-${qid}`);
  card.classList.remove('shake'); void card.offsetWidth; card.classList.add('shake');
}

function updateScores() {
  let totalScore = 0, totalAnswered = 0;
  for (const [key, sec] of Object.entries(sections)) {
    const secMax = sec.qs.reduce((s,q) => s+marks[q], 0);
    let secScore = 0;
    sec.qs.forEach(qid => {
      if (state.correct[qid] === true) { secScore += marks[qid]; totalScore += marks[qid]; }
      if (state.correct[qid] !== undefined) totalAnswered++;
    });
    document.getElementById(`sec-${key}-fill`).style.width = (secScore/secMax)*100 + '%';
    document.getElementById(`sec-${key}-val`).textContent = `${secScore}/${secMax}`;
  }
  document.getElementById('global-score').textContent = `${totalScore} / ${maxMarks}`;
  document.getElementById('progress-bar').style.width = `${(totalAnswered/allQs.length)*100}%`;
  if (totalAnswered === allQs.length) showResults(totalScore);
}

function showResults(total) {
  const pct = Math.round((total/maxMarks)*100);
  const grade = pct>=85?'🏆 Excellent!':pct>=70?'⭐ Great Job!':pct>=55?'👍 Good Effort':'📚 Keep Practising';
  const elapsed = Math.floor((Date.now()-state.startTime)/1000);
  const mins=Math.floor(elapsed/60), secs=elapsed%60;
  document.getElementById('results-grade').textContent = `${pct}%`;
  document.getElementById('results-label').textContent = grade;
  const bd = document.getElementById('results-breakdown');
  bd.innerHTML = '';
  for (const [key, sec] of Object.entries(sections)) {
    const secMax = sec.qs.reduce((s,q) => s+marks[q], 0);
    const secScore = sec.qs.reduce((s,q) => s + (state.correct[q] ? marks[q] : 0), 0);
    bd.innerHTML += `<div class="rb-chip">${sec.label}<span class="rb-val">${secScore}/${secMax}</span></div>`;
  }
  bd.innerHTML += `<div class="rb-chip">Time<span class="rb-val">${mins}m ${secs}s</span></div>`;
  const panel = document.getElementById('results-panel');
  panel.classList.add('show');
  panel.scrollIntoView({ behavior:'smooth', block:'center' });
  if (pct >= 70) launchConfetti();
  try { localStorage.setItem(`%KEY%_${Date.now()}`, JSON.stringify({ date: new Date().toISOString(), pct, total, time: `${mins}m${secs}s` })); } catch(e) {}
}

function launchConfetti() {
  const canvas = document.getElementById('confetti-canvas');
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth; canvas.height = window.innerHeight;
  const colors = ['#3ecf8e','#4f8ef7','#f5a623','#e05252','#fff'];
  const pieces = Array.from({length:120}, (_, i) => ({
    x:(i*53)%canvas.width, y:-((i*37)%canvas.height), w:(i%7)+4, h:(i%5)+3,
    color:colors[i%colors.length], rot:(i%6), vy:(i%4)+2, vx:((i%5)-2)*0.4, vr:((i%5)-2)*0.04
  }));
  let frame=0;
  function draw() {
    ctx.clearRect(0,0,canvas.width,canvas.height);
    pieces.forEach(p => {
      ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.rot);
      ctx.fillStyle=p.color; ctx.globalAlpha=0.85;
      ctx.fillRect(-p.w/2,-p.h/2,p.w,p.h); ctx.restore();
      p.y+=p.vy; p.x+=p.vx; p.rot+=p.vr;
    });
    frame++;
    if(frame<200) requestAnimationFrame(draw); else ctx.clearRect(0,0,canvas.width,canvas.height);
  }
  draw();
}

document.addEventListener('keydown', e => {
  if (e.key !== 'Enter') return;
  const a = document.activeElement;
  if (a && (a.classList.contains('num-input') || a.classList.contains('text-input'))) a.closest('.q-body')?.querySelector('.btn-check')?.click();
});

// Diagrams draw themselves in as they scroll into view
(function() {
  const figs = document.querySelectorAll('.q-fig');
  if (!('IntersectionObserver' in window)) { figs.forEach(f => f.classList.add('drawn')); return; }
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('drawn'); io.unobserve(e.target); } });
  }, { threshold: 0.25 });
  figs.forEach(f => io.observe(f));
})();
'''

if __name__ == '__main__':
    main()
