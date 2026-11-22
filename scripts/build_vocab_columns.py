#!/usr/bin/env python3
"""Build the per-topic Bahasa Indonesia column tests (.html + .md + -answers.md).

    python3 scripts/build_vocab_columns.py

Each test uses the same two-column layout as the word list
(s2/sem1/mocks/sem1-bahasa-indonesia-wordlist.html): the given word on the
left, a typed answer on the right. Part A is English -> Indonesian, Part B is
Indonesian -> English (shuffled with a fixed seed). 1 mark per word, auto-marked.

The words, and every accepted alternative (`ida` / `ena`), are read from the
DATA array in the word list, so the tests stay in sync with it. TOPICS below
says which word-list groups, plus any single extra words, go into each test.
Re-running overwrites the generated files.
"""
import html as _html
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOCKS = ROOT / 's2/sem1/mocks'
WORDLIST = MOCKS / 'sem1-bahasa-indonesia-wordlist.html'

# group titles are the word list's own; `extra` pulls single words from other groups.
TOPICS = [
    dict(slug='school', title='School & classroom', id_title='Kelas & sekolah',
         blurb='chairs, boards, desks, the teacher and describing the class',
         groups=['Kelas & sekolah · Classroom & school'],
         extra=['rapi', 'nyaman', 'sekolah', 'umur']),
    dict(slug='prepositions', title='Prepositions of place', id_title='Preposisi',
         blurb='on, under, in front of, between, behind, beside and more',
         groups=['Preposisi · Prepositions of place'],
         extra=['di sisi kanan', 'di sisi kiri']),
    dict(slug='ads', title='Advertisements', id_title='Teks iklan',
         blurb='product, title, price, discount, contact and the question words',
         groups=['Teks iklan · Advertisements', 'Iklan & kata tanya · Ads & question words',
                 'Kata baru dalam iklan · New words in the ads'],
         extra=['di mana']),
    dict(slug='animals', title='Animals & body parts', id_title='Hewan & bagian tubuh',
         blurb='animal names, plus wings, claws, fins, ears, eyes and more',
         groups=['Hewan · Animals', 'Hewan & bagian tubuh · Animals & body parts',
                 'Bagian tubuh hewan · Animal body parts'],
         extra=[]),
]


def load_data():
    for line in WORDLIST.read_text(encoding='utf-8').splitlines():
        if line.startswith('const DATA = '):
            return json.loads(line[len('const DATA = '):].rstrip().rstrip(';'))
    raise SystemExit('DATA not found in the word list')


def en_accepts(w):
    out = []
    for e in [w['en']] + w['ena']:
        out.append(e)
        if '/' in e:
            out += [p.strip() for p in e.split('/')]
    return list(dict.fromkeys(out))


def id_accepts(w):
    return [w['id']] + w['ida']


def esc(s):
    return _html.escape(s, quote=False)


CSS = """
:root {
  --bg: #0f1117; --surface: #181c27; --surface2: #1e2336; --border: #2a3050;
  --accent: #f5a623; --accent-math: #4f8ef7; --accent-sci: #3ecf8e; --accent-warn: #f5a623;
  --text: #e8eaf0; --text-muted: #7a84a0; --text-dim: #4a5270;
  --correct: #2ecc71; --wrong: #e74c3c;
  --font-display: 'Fraunces', Georgia, serif; --font-body: 'Literata', Georgia, serif; --font-mono: 'DM Mono', monospace;
  --radius: 10px;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { background: var(--bg); color: var(--text); font-family: var(--font-body); font-size: 16px; line-height: 1.6; min-height: 100vh; }
.topbar { position: sticky; top: 0; z-index: 100; background: rgba(15,17,23,0.92); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between; padding: 0 28px; height: 56px; gap: 12px; }
.topbar-left { display: flex; align-items: center; gap: 14px; }
.logo { font-family: var(--font-display); font-size: 1.15rem; font-weight: 700; letter-spacing: -0.3px; }
.logo span { color: var(--accent); }
.week-badge { font-family: var(--font-mono); font-size: 0.7rem; background: var(--surface2); border: 1px solid var(--border); color: var(--text-muted); padding: 3px 10px; border-radius: 20px; }
.back-link { font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-muted); text-decoration: none; }
.back-link:hover { color: var(--accent-math); }
.score-pill { display: flex; align-items: center; gap: 10px; background: var(--surface); border: 1px solid var(--border); border-radius: 24px; padding: 5px 16px 5px 10px; }
.score-label { font-family: var(--font-mono); font-size: 0.66rem; letter-spacing: 1px; text-transform: uppercase; color: var(--text-dim); }
.score-val { font-family: var(--font-display); font-weight: 600; font-size: 1.05rem; color: var(--accent); }
.hero, .main { max-width: 900px; margin: 0 auto; padding-left: 28px; padding-right: 28px; }
.hero { padding-top: 48px; padding-bottom: 12px; }
.eyebrow { font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 2px; text-transform: uppercase; color: var(--text-dim); margin-bottom: 12px; }
h1 { font-family: var(--font-display); font-size: clamp(2rem, 5vw, 3.2rem); font-weight: 700; line-height: 1.1; letter-spacing: -1px; margin-bottom: 14px; }
h1 em { font-style: italic; color: var(--accent); }
.credit { font-size: 0.92rem; color: var(--text-muted); max-width: 660px; margin-bottom: 14px; }
.hero-chips { display: flex; gap: 8px 22px; flex-wrap: wrap; }
.hero-chip { display: flex; align-items: center; gap: 7px; font-size: 0.85rem; color: var(--text-muted); }
.hero-chip .dot { width: 8px; height: 8px; border-radius: 50%; background: var(--accent); }
.main { padding-bottom: 80px; }
.section-head { display: flex; align-items: center; gap: 14px; margin: 40px 0 14px; flex-wrap: wrap; }
.section-head h2 { font-family: var(--font-display); font-size: 1.45rem; font-weight: 600; flex: 1; min-width: 220px; }
.section-head .sub { font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-muted); letter-spacing: 1px; text-transform: uppercase; }
.dir-en { color: var(--accent-math); } .dir-id { color: var(--accent-warn); }
.info-box { background: var(--surface2); border-left: 3px solid var(--accent); border-radius: 0 6px 6px 0; padding: 10px 14px; font-size: 0.88rem; color: var(--text-muted); margin-bottom: 14px; }
.info-box em { color: var(--accent); }
.btns { display: flex; gap: 8px; flex-wrap: wrap; margin: 0 0 8px; }
.btn { font-family: var(--font-mono); font-size: 0.74rem; padding: 7px 14px; border-radius: 6px; border: 1px solid var(--border); background: var(--surface2); color: var(--text-muted); cursor: pointer; }
.btn:hover { border-color: var(--accent); color: var(--text); }
.btn.primary { background: var(--accent); color: #0f1117; border-color: var(--accent); }
.btn.primary:hover { opacity: .85; color: #0f1117; }
.sub-head { font-family: var(--font-display); font-size: 1.05rem; font-weight: 600; color: var(--accent); margin: 26px 0 10px; padding-bottom: 6px; border-bottom: 1px solid var(--border); }
.list { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.row { display: contents; }
.cell { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 8px 16px; min-height: 48px; display: flex; align-items: center; flex-wrap: wrap; gap: 4px 10px; }
.cell.given { font-family: var(--font-display); font-size: 1.05rem; font-weight: 600; }
.given.en-side { color: var(--accent-math); } .given.id-side { color: var(--accent-warn); }
.cell.answer { padding: 4px 6px 4px 8px; gap: 6px; flex-wrap: nowrap; }
.cell.answer input { flex: 1; min-width: 0; background: transparent; border: none; outline: none; color: var(--text); font-family: var(--font-body); font-size: 1rem; padding: 6px 6px; }
.cell.answer input::placeholder { color: var(--text-dim); font-family: var(--font-mono); font-size: 0.74rem; }
.cell.answer:focus-within { border-color: var(--accent); }
.cell.answer.right { border-color: rgba(46,204,113,0.55); background: rgba(46,204,113,0.07); }
.cell.answer.wrong { border-color: rgba(231,76,60,0.55); background: rgba(231,76,60,0.07); }
.cell.answer.shake { animation: shake .3s; }
@keyframes shake { 25% { transform: translateX(-4px); } 75% { transform: translateX(4px); } }
.mini { font-family: var(--font-mono); font-size: 0.68rem; padding: 4px 8px; border-radius: 5px; border: 1px solid var(--border); background: var(--surface2); color: var(--text-muted); cursor: pointer; flex-shrink: 0; }
.mini:hover { border-color: var(--accent); color: var(--text); }
.fb { font-family: var(--font-mono); font-size: 0.78rem; flex-shrink: 0; max-width: 55%; text-align: right; }
.fb.ok { color: var(--correct); } .fb.no { color: var(--wrong); } .fb.hint { color: var(--text-muted); }
.divider { height: 1px; background: var(--border); margin: 52px 0 0; }
.result { display: none; margin-top: 40px; background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 26px 28px; text-align: center; }
.result.show { display: block; }
.result .big { font-family: var(--font-display); font-size: 2.6rem; font-weight: 700; color: var(--accent); }
.result p { color: var(--text-muted); margin-top: 4px; }
@media (max-width: 600px) {
  .topbar { padding: 10px 16px; height: auto; flex-wrap: wrap; row-gap: 8px; }
  .hero, .main { padding-left: 16px; padding-right: 16px; }
  .topbar-left { flex-direction: column; align-items: flex-start; gap: 3px; }
  h1 { font-size: 1.8rem; }
  .cell { padding-left: 12px; padding-right: 12px; }
  .cell.answer { flex-wrap: wrap; }
  .fb { max-width: 100%; text-align: left; }
}
@media print { .btns, .topbar { display: none; } body { background: #fff; color: #000; } }
"""

JS = r"""
const DATA = __DATA__;
const marks = __MARKS__;
const sections = __SECTIONS__;
const allQs = Object.values(sections).flatMap(s => s.qs);
const maxMarks = allQs.reduce((s, q) => s + marks[q], 0);
const state = { correct: {}, startTime: Date.now() };

function esc(s) { return String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }
function normalise(s) {
  return s.toLowerCase().trim().replace(/[’‘]/g, "'").replace(/[.,!?'"]/g, '').replace(/-/g, ' ').replace(/\s+/g, ' ').trim();
}
function stripArticle(s) { return s.replace(/^(a|an|the) /, ''); }
function isMatch(typed, accepted) {
  const t = normalise(typed), ts = stripArticle(t);
  return accepted.some(a => { const n = normalise(a); return n === t || n === ts || stripArticle(n) === ts; });
}

const byId = {};
function index() { DATA.partA.forEach(g => g.qs.forEach(q => { q.part = 'a'; byId[q.qid] = q; })); DATA.partB.forEach(q => { q.part = 'b'; byId[q.qid] = q; }); }

function pattern(q) {
  return q.ans[0].split('').map((c, i) => (i === 0 || c === ' ' || c === '-' || c === '/') ? c : '_').join('');
}

function lock(qid, ok, text) {
  const input = document.getElementById(qid + '-ans');
  input.disabled = true;
  document.getElementById('cell-' + qid).classList.add(ok ? 'right' : 'wrong');
  const fb = document.getElementById(qid + '-fb');
  fb.className = 'fb ' + (ok ? 'ok' : 'no');
  fb.textContent = text;
  const hb = document.querySelector('[data-hint="' + qid + '"]'); if (hb) hb.remove();
}

function check(qid) {
  const input = document.getElementById(qid + '-ans');
  const q = byId[qid];
  if (state.correct[qid] !== undefined) return;
  if (!input.value.trim()) { const c = document.getElementById('cell-' + qid); c.classList.remove('shake'); void c.offsetWidth; c.classList.add('shake'); return; }
  const ok = isMatch(input.value, q.ans);
  state.correct[qid] = ok;
  lock(qid, ok, ok ? '✓' : '✗ ' + q.show);
  updateScores();
}

function showAnswer(qid) {
  if (state.correct[qid] !== undefined) return;
  state.correct[qid] = false;
  lock(qid, false, '✗ ' + byId[qid].show);
}

function updateScores() {
  const got = allQs.reduce((s, q) => s + (state.correct[q] ? marks[q] : 0), 0);
  document.getElementById('global-score').textContent = got + ' / ' + maxMarks;
  ['a', 'b'].forEach(p => {
    const qs = allQs.filter(q => byId[q].part === p);
    document.getElementById('sec-' + p + '-val').textContent = qs.reduce((s, q) => s + (state.correct[q] ? marks[q] : 0), 0) + '/' + qs.length;
  });
  if (allQs.every(q => state.correct[q] !== undefined)) showResults(got);
}

function showResults(got) {
  const r = document.getElementById('result');
  const pct = Math.round(got / maxMarks * 100);
  const secs = Math.round((Date.now() - state.startTime) / 1000);
  r.querySelector('.big').textContent = got + ' / ' + maxMarks;
  r.querySelector('p').textContent = pct + '% · ' + Math.floor(secs / 60) + ' min ' + (secs % 60) + ' s · ' +
    (pct >= 90 ? 'Excellent — you know this topic.' : pct >= 70 ? 'Good. Retry the words you missed.' : 'Keep practising: use the word list, then try again.');
  r.classList.add('show');
}

document.addEventListener('keydown', e => {
  if (e.key !== 'Enter' || !e.target.dataset || !e.target.dataset.q) return;
  e.preventDefault();
  const cur = e.target;
  check(cur.dataset.q);
  const inputs = Array.from(document.querySelectorAll('.cell.answer input:not(:disabled)'));
  const nxt = inputs.find(i => cur.compareDocumentPosition(i) & Node.DOCUMENT_POSITION_FOLLOWING);
  if (nxt) nxt.focus();
});
document.addEventListener('click', e => {
  const h = e.target.closest('[data-hint]');
  if (h) { const q = byId[h.dataset.hint]; const fb = document.getElementById(q.qid + '-fb'); fb.className = 'fb hint'; fb.textContent = pattern(q); return; }
  const b = e.target.closest('[data-act]');
  if (!b) return;
  const qs = allQs.filter(q => byId[q].part === b.dataset.part);
  if (b.dataset.act === 'check') qs.forEach(check);
  else if (b.dataset.act === 'show') { qs.forEach(q => { if (document.getElementById(q + '-ans').value.trim()) check(q); else showAnswer(q); }); updateScores(); }
  else if (b.dataset.act === 'reset') location.reload();
});
index(); updateScores();
"""


def build_data(topic, groups):
    sel = [(g['title'], list(g['words'])) for g in groups if g['title'] in topic['groups']]
    extras = [w for g in groups for w in g['words'] if w['id'] in topic['extra']]
    if extras:
        sel.append(('More words · Kata tambahan', extras))
    n = 0
    part_a, flat = [], []
    for title, ws in sel:
        qs = []
        for w in ws:
            n += 1
            qs.append(dict(qid='v%d' % n, id=w['id'], en=w['en'], ans=id_accepts(w),
                           show=' / '.join(id_accepts(w)), _w=w))
        part_a.append(dict(title=title, qs=qs))
        flat += qs
    N = len(flat)
    order = flat[:]
    random.Random(topic['slug']).shuffle(order)
    part_b = []
    for i, q in enumerate(order):
        w = q['_w']
        part_b.append(dict(qid='v%d' % (N + i + 1), id=w['id'], en=w['en'], ans=en_accepts(w),
                           show=' / '.join([w['en']] + w['ena'][:2]), _w=w))
    return part_a, part_b, N


def strip_private(o):
    if isinstance(o, dict):
        return {k: strip_private(v) for k, v in o.items() if k != '_w'}
    if isinstance(o, list):
        return [strip_private(x) for x in o]
    return o


def row_html(q, part):
    given = q['en'] if part == 'a' else q['id']
    cls = 'en-side' if part == 'a' else 'id-side'
    ph = 'type the Indonesian' if part == 'a' else 'type the English'
    return (f'<div class="row" id="qcard-{q["qid"]}">'
            f'<div class="cell given {cls}">{esc(given)}</div>'
            f'<div class="cell answer" id="cell-{q["qid"]}">'
            f'<input type="text" id="{q["qid"]}-ans" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="{ph}" data-q="{q["qid"]}">'
            f'<span class="fb" id="{q["qid"]}-fb"></span>'
            f'<button class="mini" type="button" data-hint="{q["qid"]}">hint</button>'
            '</div></div>')


def build_html(topic, part_a, part_b, N):
    list_a = ''.join(f'<h3 class="sub-head">{esc(g["title"])}</h3><div class="list">' +
                     ''.join(row_html(q, 'a') for q in g['qs']) + '</div>' for g in part_a)
    list_b = '<div class="list">' + ''.join(row_html(q, 'b') for q in part_b) + '</div>'
    total = 2 * N
    marks = {q['qid']: 1 for g in part_a for q in g['qs']}
    marks.update({q['qid']: 1 for q in part_b})
    data = json.dumps(strip_private(dict(partA=part_a, partB=part_b)), ensure_ascii=False).replace('</', '<\\/')
    marks_js = '{ ' + ', '.join('%s:1' % k for k in marks) + ' }'
    secs = {'a': [q['qid'] for g in part_a for q in g['qs']], 'b': [q['qid'] for q in part_b]}
    secs_js = '{\n  a: { qs: %s },\n  b: { qs: %s }\n}' % (json.dumps(secs['a']), json.dumps(secs['b']))
    js = JS.replace('__DATA__', data).replace('__MARKS__', marks_js).replace('__SECTIONS__', secs_js)
    base = 'sem1-bahasa-indonesia-columns-' + topic['slug']
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bahasa Indonesia &middot; {esc(topic['title'])} Column Test</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,600;0,9..144,700;1,9..144,400&family=DM+Mono:wght@400;500&family=Literata:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="topbar">
  <div class="topbar-left">
    <div class="logo">Student<span>'s</span> Study Hub</div>
    <div class="week-badge">Bahasa Indonesia &middot; {esc(topic['title'])}</div>
  </div>
  <div class="score-pill"><div class="score-label">Score</div><div class="score-val" id="global-score">0 / {total}</div></div>
  <a href="../../../index.html" class="back-link">&larr; All sheets</a>
</div>
<div class="hero">
  <div class="eyebrow">Secondary 2 &middot; Bahasa Indonesia Level 1 &middot; Semester 1 Vocabulary</div>
  <h1>{esc(topic['title'])}<br><em>{esc(topic['id_title'])}</em></h1>
  <p class="credit">{N} words &mdash; {topic['blurb']} &mdash; in the same two columns as the word list, but now you type the answer. Part A is English &rarr; Indonesian, Part B is Indonesian &rarr; English. Press Enter to check a row.</p>
  <div class="hero-chips">
    <div class="hero-chip"><div class="dot"></div>{total} questions &middot; self-marked &middot; {total} marks</div>
    <div class="hero-chip"><div class="dot" style="background:var(--accent-math)"></div>Typed answers only &mdash; no multiple choice</div>
  </div>
</div>
<div class="main">
  <section id="a">
    <div class="section-head"><h2>Part A &middot; English &rarr; Indonesian</h2><div class="sub dir-en">Score <span id="sec-a-val">0/{N}</span></div></div>
    <div class="info-box">Read the <em>English</em> word on the left and type the Indonesian on the right. Capitals and hyphens do not matter. <em>hint</em> shows the first letter and the length.</div>
    <div class="btns">
      <button class="btn primary" data-act="check" data-part="a">Check Part A</button>
      <button class="btn" data-act="show" data-part="a">Show answers</button>
      <button class="btn" data-act="reset" data-part="a">Start again</button>
    </div>
    <div id="list-a">{list_a}</div>
  </section>
  <div class="divider"></div>
  <section id="b">
    <div class="section-head"><h2>Part B &middot; Indonesian &rarr; English</h2><div class="sub dir-id">Score <span id="sec-b-val">0/{N}</span></div></div>
    <div class="info-box">Read the <em>Indonesian</em> word on the left and type the English on the right. Words are in a different order from Part A. Where a word has more than one meaning, any one correct meaning is accepted.</div>
    <div class="btns">
      <button class="btn primary" data-act="check" data-part="b">Check Part B</button>
      <button class="btn" data-act="show" data-part="b">Show answers</button>
      <button class="btn" data-act="reset" data-part="b">Start again</button>
    </div>
    <div id="list-b">{list_b}</div>
  </section>
  <div class="result" id="result"><div class="big"></div><p></p></div>
</div>
<script>{js}</script>
</body>
</html>
"""
    (MOCKS / (base + '.html')).write_text(page, encoding='utf-8')


def build_md(topic, part_a, part_b, N):
    base = 'sem1-bahasa-indonesia-columns-' + topic['slug']
    total = 2 * N
    L = [f"# Secondary 2 · Bahasa Indonesia — {topic['title']} ({topic['id_title']})", '',
         f"**Semester 1 vocabulary · column test · {total} questions · {total} marks**", '',
         f"{N} words — {topic['blurb']} — in two columns. Part A: write the Indonesian. "
         "Part B: write the English. 1 mark per word. Capital letters and hyphens do not matter. "
         f"The answer sheet is `{base}-answers.md`.", '', '---', '',
         f'## Part A · English → Indonesian (Q1–Q{N})', '']
    for g in part_a:
        L += [f"### {g['title']}", '', '| Q | English | Indonesian |', '|---|---------|------------|']
        L += [f"| {q['qid'][1:]} | {q['en']} | ____________________ |" for q in g['qs']]
        L.append('')
    L += ['---', '', f'## Part B · Indonesian → English (Q{N+1}–Q{total})', '',
          '| Q | Indonesian | English |', '|---|------------|---------|']
    L += [f"| {q['qid'][1:]} | {q['id']} | ____________________ |" for q in part_b]
    L.append('')
    (MOCKS / (base + '.md')).write_text('\n'.join(L), encoding='utf-8')

    A = [f"# Secondary 2 · Bahasa Indonesia — {topic['title']} — Answers", '',
         f"Answers for the {topic['title']} column test. On the interactive sheet ({base}.html) "
         "the marking is automatic and accepts every spelling listed here.", '',
         '| Q | Given | Accepted answers |', '|---|-------|------------------|']
    for g in part_a:
        A += [f"| {q['qid'][1:]} | {q['en']} | {' / '.join(q['ans'])} |" for q in g['qs']]
    A += [f"| {q['qid'][1:]} | {q['id']} | {' / '.join(a for a in q['ans'] if '/' not in a)} |" for q in part_b]
    A.append('')
    (MOCKS / (base + '-answers.md')).write_text('\n'.join(A), encoding='utf-8')


def main():
    groups = load_data()
    for t in TOPICS:
        part_a, part_b, N = build_data(t, groups)
        build_html(t, part_a, part_b, N)
        build_md(t, part_a, part_b, N)
        print(f"{t['slug']}: {N} words, {2 * N} marks")


if __name__ == '__main__':
    main()
