#!/usr/bin/env python3
"""Build a vocabulary drill (.html + .md printable + -answers.md) from a spec.

    python3 scripts/build_vocab_drill.py scripts/review_specs/s2_sem1_bahasa_vocab_2.py
    python3 scripts/build_vocab_drill.py --only-md scripts/review_specs/s2_sem1_bahasa_vocab.py

A vocabulary drill is a set of typed-answer translation questions in two
directions (English -> the target language and back), grouped by theme. All
questions are 1 mark and there is no multiple choice anywhere — so
mcq_audit.py / mcq_shuffle.py do not apply; run sheet_audit.py and update the
root index.html card if the totals ever change.

The spec is a plain Python file defining:

  META      dict: out (repo-relative basename, no extension), title, badge,
            eyebrow, h1, credit (html), md_title, md_intro, answers_note,
            storage_key, back
  SECTIONS  list of dicts: key, anchor, tab, icon (html entity), dir
            ('en-id' or 'id-en'), title, label, score_label, js_label,
            info (html info-box), md_title (markdown section heading),
            md_info (plain text), placeholder (input placeholder),
            groups: list of (group_title_html, [question dicts])

A question dict:

  a            the word asked about (shown inside <em> in the question)
  ans          list of accepted answers; ans[0] is the canonical one
  hint         description in other words — must not contain the answer
  display      optional canonical form shown in the reveal (default ans[0])
  ask          optional full override of the question sentence (html)
  ask_prefix   optional override of 'Tulis kata bahasa Indonesia untuk'
               (the hand-written drill used '... nama hewan ...' for animals)
  tail         optional extra words appended to the question (html)
  help         optional override of the grey parenthetical (html)
  placeholder  optional per-question input placeholder
  fmt          optional dict of extra {fields} for a LANG help_source template (e.g. pinyin)

META may also carry an optional `lang` dict to adapt the builder to another
language (defaults are Indonesian): ask_target, ask_source ({w}), help_target
({noun}, {w}), help_source ({w} plus any q['fmt'] fields), chip_target,
chip_source, placeholder, strip (extra characters ignored when matching, e.g.
Chinese punctuation) and extra_css (appended inside <style>, e.g. CJK fonts).
  note         optional extra words appended to the reveal text

The page is the same as the hand-written first drill
(s2/sem1/mocks/sem1-bahasa-indonesia-vocab.html): identical CSS and scoring JS,
question ids v1..vN, 1 mark each. Re-running overwrites the files, so edit
the spec rather than the generated sheets. `--only-md` writes just the .md
and -answers.md (used for the first drill, whose .html predates the builder).
"""
import html as _html
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANG = {}  # optional per-spec overrides, set from META['lang'] in main() (see the docstring)


def load(path):
    spec = importlib.util.spec_from_file_location('vocab_spec', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def esc(s):
    return _html.escape(s, quote=False)


def js(s):
    """Text inside a single-quoted JS string in a double-quoted attribute."""
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('"', '&quot;')


def untag(s):
    """Html fragment -> plain text (for the markdown printable)."""
    s = re.sub(r'<[^>]+>', '', s)
    return _html.unescape(s).strip()


CSS = """<style>:root {
  --bg: #0f1117; --surface: #181c27; --surface2: #1e2336; --border: #2a3050;
  --accent: #f5a623; --accent-math: #4f8ef7; --accent-sci: #3ecf8e; --accent-warn: #f5a623;
  --text: #e8eaf0; --text-muted: #7a84a0; --text-dim: #4a5270;
  --correct: #2ecc71; --wrong: #e74c3c;
  --font-display: 'Fraunces', Georgia, serif; --font-body: 'Literata', Georgia, serif; --font-mono: 'DM Mono', monospace;
  --radius: 10px;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { background: var(--bg); color: var(--text); font-family: var(--font-body); font-size: 16px; line-height: 1.7; min-height: 100vh; }
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
.progress-bar { height: 100%; background: linear-gradient(90deg, var(--accent), var(--accent-sci)); width: 0%; transition: width 0.6s cubic-bezier(0.34,1.56,0.64,1); }
.hero { position: relative; z-index: 1; padding: 52px 28px 24px; max-width: 900px; margin: 0 auto; }
.hero-eyebrow { font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 2px; text-transform: uppercase; color: var(--text-dim); margin-bottom: 12px; }
.hero h1 { font-family: var(--font-display); font-size: clamp(2rem, 5vw, 3.2rem); font-weight: 700; line-height: 1.1; letter-spacing: -1px; margin-bottom: 14px; }
.hero h1 em { font-style: italic; color: var(--accent); }
.hero-meta { display: flex; gap: 20px; flex-wrap: wrap; margin-top: 18px; }
.hero-chip { display: flex; align-items: center; gap: 7px; font-size: 0.85rem; color: var(--text-muted); }
.hero-chip .dot { width: 8px; height: 8px; border-radius: 50%; background: var(--accent); }
.credit { font-size: 0.82rem; color: var(--text-muted); margin-top: 10px; }
.section-tabs { position: relative; z-index: 1; max-width: 900px; margin: 0 auto; padding: 16px 28px 24px; display: flex; gap: 8px; flex-wrap: wrap; }
.sub-tab { font-family: var(--font-mono); font-size: 0.75rem; letter-spacing: 0.5px; padding: 7px 16px; border-radius: 6px; border: 1px solid var(--border); background: var(--surface); color: var(--text-muted); text-decoration: none; transition: all 0.2s; }
.sub-tab:hover { border-color: var(--accent); color: var(--text); }
.main { position: relative; z-index: 1; max-width: 900px; margin: 0 auto; padding: 0 28px 80px; }
.section-header { display: flex; align-items: center; gap: 14px; margin: 44px 0 20px; }
.section-icon { width: 42px; height: 42px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; flex-shrink: 0; background: rgba(245,166,35,0.15); }
.section-header h2 { font-family: var(--font-display); font-size: 1.45rem; font-weight: 600; letter-spacing: -0.3px; }
.section-header .sub-label { font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-muted); letter-spacing: 1px; text-transform: uppercase; margin-top: 2px; }
.info-box { background: var(--surface2); border-left: 3px solid var(--accent); border-radius: 0 6px 6px 0; padding: 10px 14px; font-size: 0.88rem; color: var(--text-muted); margin-bottom: 16px; line-height: 1.6; }
.info-box em { font-style: italic; color: var(--accent); }
.q-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); margin-bottom: 14px; overflow: hidden; transition: border-color 0.3s; animation: slideIn 0.35s ease both; }
.q-card.answered-correct { border-color: var(--correct); }
.q-card.answered-wrong { border-color: var(--wrong); }
.q-header { display: flex; align-items: flex-start; gap: 14px; padding: 16px 20px 12px; border-bottom: 1px solid var(--border); }
.q-num { font-family: var(--font-mono); font-size: 0.72rem; background: var(--surface2); border: 1px solid var(--border); color: var(--text-muted); padding: 3px 8px; border-radius: 4px; flex-shrink: 0; margin-top: 2px; }
.q-text { font-size: 0.96rem; color: var(--text); flex: 1; line-height: 1.6; }
.q-text em { font-style: italic; color: var(--accent); }
.q-en { color: var(--text-dim); font-size: 0.82rem; }
.q-marks { font-family: var(--font-mono); font-size: 0.7rem; color: var(--accent); background: rgba(245,166,35,0.1); border: 1px solid rgba(245,166,35,0.2); padding: 3px 8px; border-radius: 4px; flex-shrink: 0; white-space: nowrap; }
.dir-chip { font-family: var(--font-mono); font-size: 0.66rem; letter-spacing: 0.5px; padding: 3px 8px; border-radius: 4px; flex-shrink: 0; margin-top: 2px; white-space: nowrap; }
.dir-en-id { background: rgba(79,142,247,0.12); color: var(--accent-math); border: 1px solid rgba(79,142,247,0.3); }
.dir-id-en { background: rgba(245,166,35,0.12); color: var(--accent-warn); border: 1px solid rgba(245,166,35,0.3); }
.q-body { padding: 14px 20px; }
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
.section-score-val { font-family: var(--font-display); font-size: 1.2rem; font-weight: 600; color: var(--accent); }
.section-score-bar { flex: 2; height: 6px; background: var(--border); border-radius: 3px; overflow: hidden; }
.section-score-fill { height: 100%; background: linear-gradient(90deg, var(--accent), var(--accent-sci)); width: 0%; transition: width 0.8s cubic-bezier(0.34,1.56,0.64,1); border-radius: 3px; }
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
.divider::after { content: '\\00a7'; position: absolute; left: 50%; top: 50%; transform: translate(-50%,-50%); background: var(--bg); padding: 0 12px; color: var(--text-dim); font-family: var(--font-display); }
@keyframes slideIn { from { opacity:0; transform:translateY(12px); } to { opacity:1; transform:translateY(0); } }
@keyframes popIn { from { opacity:0; transform:scale(0.92) translateY(20px); } to { opacity:1; transform:scale(1) translateY(0); } }
@keyframes shake { 0%,100%{transform:translateX(0)} 20%{transform:translateX(-6px)} 40%{transform:translateX(6px)} 60%{transform:translateX(-4px)} 80%{transform:translateX(4px)} }
@keyframes pulse-math { 0%{box-shadow:0 0 0 0 rgba(245,166,35,0.4)} 70%{box-shadow:0 0 0 10px rgba(245,166,35,0)} 100%{box-shadow:0 0 0 0 rgba(245,166,35,0)} }
.shake { animation: shake 0.4s ease; }
.pulse-correct { animation: pulse-math 0.6s ease; }
.sub-head { font-family: var(--font-display); font-size: 1.05rem; font-weight: 600; color: var(--accent); margin: 28px 0 12px; padding-bottom: 6px; border-bottom: 1px solid var(--border); }
@media (max-width: 600px) {
  .topbar { padding: 10px 16px; height: auto; flex-wrap: wrap; row-gap: 8px; }
  .topbar-left { flex-direction: column; align-items: flex-start; gap: 3px; }
  .hero, .section-tabs, .main { padding-left: 16px; padding-right: 16px; }
  .hero h1 { font-size: 1.8rem; }
  .main { padding-bottom: 60px; }
  .results-panel { padding: 20px; }
  .results-grade { font-size: 2.8rem; }
}
</style>"""


def q_text(sec, q):
    """The question sentence, html (without the grey help span)."""
    if 'ask' in q:
        return q['ask']
    word = esc(q['a'])
    if sec['dir'] == 'en-id':
        prefix = q.get('ask_prefix', LANG.get('ask_target', 'Tulis kata bahasa Indonesia untuk'))
        out = f'{prefix} <em>{word}</em>.'
    else:
        out = LANG.get('ask_source', 'Apa arti <em>{w}</em> dalam bahasa Inggris?').format(w=word)
    if 'tail' in q:
        out += ' ' + q['tail']
    return out


def q_help(sec, q):
    """The grey parenthetical under the question, html."""
    if 'help' in q:
        return q['help']
    word = esc(q['a'])
    if sec['dir'] == 'en-id':
        canon = q.get('display', q['ans'][0])
        noun = 'words' if ' ' in canon else 'word'
        return LANG.get('help_target', '(Write the Indonesian {noun} for &ldquo;{w}&rdquo;.)').format(noun=noun, w=word)
    return LANG.get('help_source', '(What is &ldquo;{w}&rdquo; in English?)').format(w=word, **q.get('fmt', {}))


def q_reveal(sec, q):
    if 'reveal' in q:
        return q['reveal']
    display = esc(q.get('display', q['ans'][0]))
    note = esc(q.get('note', ''))
    if sec['dir'] == 'en-id':
        return f'&lt;em&gt;{display}&lt;/em&gt; = {esc(q["a"])}.{note}'
    return f'&lt;em&gt;{display}&lt;/em&gt; ({esc(q["a"])}).{note}'


def q_card(sec, q, n, qid):
    dirn = sec['dir']
    chip_cls = 'dir-en-id' if dirn == 'en-id' else 'dir-id-en'
    chip_label = LANG.get('chip_target', 'EN &rarr; ID') if dirn == 'en-id' else LANG.get('chip_source', 'ID &rarr; EN')
    placeholder = q.get('placeholder', sec.get('placeholder', LANG.get('placeholder', 'bahasa Indonesia&hellip;')))
    answers = ','.join(f"'{js(a)}'" for a in q['ans'])
    return (f'  <!-- Q{n} -->\n'
            f'  <div class="q-card" id="qcard-{qid}">\n'
            f'    <div class="q-header"><div class="q-num">Q{n}</div>'
            f'<div class="q-text">{q_text(sec, q)} <span class="q-en">{q_help(sec, q)}</span></div>'
            f'<span class="dir-chip {chip_cls}">{chip_label}</span>'
            f'<div class="q-marks">1 mark</div></div>\n'
            f'    <div class="q-body">\n'
            f'      <input type="text" class="text-input" id="{qid}-ans" placeholder="{placeholder}" autocomplete="off">\n'
            f'      <div class="q-actions">\n'
            f'        <button class="btn btn-check" onclick="checkText(\'{qid}\',[{answers}],\'Q{n}\')">Check</button>\n'
            f'        <button class="btn btn-hint" onclick="showHint(\'{qid}\',\'{js(q["hint"])}\')">Hint</button>\n'
            f'        <button class="btn btn-reveal" onclick="revealAnswer(\'{qid}\',\'{q_reveal(sec, q)}\')">Show Answer</button>\n'
            f'      </div>\n'
            f'      <div class="feedback" id="{qid}-fb"></div>\n'
            f'    </div>\n'
            f'  </div>\n')


def number_sections(sections):
    """Attach numbering: per section, first/last qid and the qid list."""
    n = 0
    for sec in sections:
        sec.pop('first_q', None)
        sec['qids'] = []
        for _title, qs in sec['groups']:
            for _q in qs:
                n += 1
                sec['qids'].append(f'v{n}')
        sec['first_q'] = n - len(sec['qids']) + 1
        sec['last_q'] = n
    return n


JS = '''
const state = { answers: {}, correct: {}, startTime: Date.now() };

const marks = { __MARKS__ };

const sections = {
__SECTIONS__
};

const allQs = Object.values(sections).flatMap(s => s.qs);
const maxMarks = allQs.reduce((s,q) => s + marks[q], 0);

function updateTimer() {
  const e = Math.floor((Date.now()-state.startTime)/1000);
  document.getElementById('timer').textContent = `${String(Math.floor(e/60)).padStart(2,'0')}:${String(e%60).padStart(2,'0')}`;
}
setInterval(updateTimer, 1000);

function normalise(s) {
  return s.toLowerCase().trim().replace(/[.,!?]+$/, '').replace(/[\\u2019\\u2018]/g, "'").replace(/[\\u201c\\u201d"]/g, '').replace(/\\s+/g, ' ');
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
    ? `\\u2705 <strong>Correct!</strong> +${marks[qid]} mark${marks[qid]>1?'s':''}`
    : `\\u274c <strong>Not quite.</strong> Check the hint or reveal the answer, then try to understand why.`;
  updateScores();
}

function showHint(qid, hintText) {
  const fb = document.getElementById(`${qid}-fb`);
  if (state.correct[qid] !== undefined) return;
  fb.className = 'feedback show hint-fb';
  fb.innerHTML = `\\ud83d\\udca1 <strong>Hint:</strong> ${hintText}`;
}

function revealAnswer(qid, answerText) {
  const fb = document.getElementById(`${qid}-fb`);
  fb.className = 'feedback show reveal-fb';
  fb.innerHTML = `\\ud83d\\udcd6 <strong>Answer:</strong> ${answerText}`;
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
    const fill = document.getElementById(`sec-${key}-fill`);
    const val = document.getElementById(`sec-${key}-val`);
    if (fill) fill.style.width = (secScore/secMax)*100 + '%';
    if (val) val.textContent = `${secScore}/${secMax}`;
  }
  document.getElementById('global-score').textContent = `${totalScore} / ${maxMarks}`;
  document.getElementById('progress-bar').style.width = `${(totalAnswered/allQs.length)*100}%`;
  if (totalAnswered === allQs.length) showResults(totalScore);
}

function showResults(total) {
  const pct = Math.round((total/maxMarks)*100);
  const grade = pct>=85?'\\ud83c\\udfc6 Excellent!':pct>=70?'\\u2b50 Great Job!':pct>=55?'\\ud83d\\udc4d Good Effort':'\\ud83d\\udcda Keep Practising';
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
  try { localStorage.setItem('__STORAGEKEY__' + '_' + Date.now(), JSON.stringify({ date: new Date().toISOString(), pct, total, time: `${mins}m${secs}s` })); } catch(e) {}
}

function launchConfetti() {
  const canvas = document.getElementById('confetti-canvas');
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth; canvas.height = window.innerHeight;
  const colors = ['#3ecf8e','#4f8ef7','#f5a623','#e05252','#fff'];
  const pieces = Array.from({length:120}, (_, i) => ({
    x:(i*53)%canvas.width, y:-((i*37)%canvas.height),
    w:(i%7)+4, h:(i%5)+3,
    color:colors[i%colors.length],
    rot:(i%6), vy:(i%4)+2, vx:((i%5)-2)*0.4, vr:((i%5)-2)*0.04
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
    if(frame<200) requestAnimationFrame(draw);
    else ctx.clearRect(0,0,canvas.width,canvas.height);
  }
  draw();
}

document.addEventListener('keydown', e => {
  if (e.key === 'Enter') {
    const active = document.activeElement;
    if (active && active.classList.contains('text-input')) {
      active.closest('.q-body')?.querySelector('.btn-check')?.click();
    }
  }
});
'''


def build_html(meta, sections):
    """Python literal interpolation — JS braces are substituted via placeholders."""
    number_sections(sections)
    total = sections[-1]['last_q']
    tabs = '\n'.join(
        f'  <a href="#{sec["anchor"]}" class="sub-tab">{sec["tab"]}</a>' for sec in sections)

    body = []
    for sec in sections:
        count = len(sec['qids'])
        body.append(f'<div id="{sec["anchor"]}">\n'
                    f'  <div class="section-header"><div class="section-icon">{sec["icon"]}</div>'
                    f'<div><div class="sub-label">{sec["label"]} &middot; Q{sec["first_q"]}&ndash;Q{sec["last_q"]}</div>'
                    f'<h2>{sec["title"]}</h2></div></div>\n'
                    f'<div class="info-box">{sec["info"]}</div>\n')
        qid_iter = iter(sec['qids'])
        n = sec['first_q'] - 1
        for title, qs in sec['groups']:
            body.append(f'<h3 class="sub-head">{title}</h3>\n')
            for q in qs:
                n += 1
                body.append(q_card(sec, q, n, next(qid_iter)))
        body.append(f'  <div class="section-score">\n'
                    f'    <div class="section-score-label">{sec["score_label"]}</div>\n'
                    f'    <div class="section-score-bar"><div class="section-score-fill" id="sec-{sec["key"]}-fill"></div></div>\n'
                    f'    <div class="section-score-val" id="sec-{sec["key"]}-val">0/{count}</div>\n'
                    f'  </div>\n'
                    f'</div>\n'
                    f'<div class="divider"></div>\n\n')

    marks_line = ', '.join(f'v{i}:1' for i in range(1, total + 1))
    js_secs = ',\n'.join(
        f"  {sec['key']}: {{ label: '{sec['js_label']}', qs: [" + ','.join(f"'{q}'" for q in sec['qids']) + '] }'
        for sec in sections)
    script = JS.replace('__MARKS__', marks_line).replace('__SECTIONS__', js_secs) \
                .replace('__STORAGEKEY__', meta['storage_key'])
    if LANG.get('strip'):  # extra characters ignored when matching typed answers (e.g. Chinese punctuation)
        script = script.replace("replace(/[.,!?]+$/, '')", "replace(/[.,!?]+$/, '').replace(/[" + LANG['strip'] + "]+/g, '')")
    css = CSS.replace('</style>', LANG['extra_css'] + '\n</style>') if LANG.get('extra_css') else CSS

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{meta['title']}</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,600;0,9..144,700;1,9..144,400&family=DM+Mono:wght@400;500&family=Literata:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
{css}
</head>
<body>
<canvas id="confetti-canvas"></canvas>
<div class="topbar">
  <div class="topbar-left">
    <div class="logo">Student<span>'s</span> Study Hub</div>
    <div class="week-badge">{meta['badge']}</div>
  </div>
  <div style="display:flex;align-items:center;gap:14px;">
    <a href="{meta['back']}" class="back-link">&larr; All sheets</a>
    <div class="timer-wrap">&#9201;<div class="timer" id="timer">00:00</div></div>
    <div class="score-pill"><div class="score-label">Score</div><div class="score-val" id="global-score">0 / {total}</div></div>
  </div>
</div>
<div class="progress-wrap"><div class="progress-bar" id="progress-bar"></div></div>
<div class="hero">
  <div class="hero-eyebrow">{meta['eyebrow']}</div>
  <h1>{meta['h1']}</h1>
  <div class="hero-meta">
    <div class="hero-chip"><div class="dot"></div>{total} questions &middot; self-marked &middot; {total} marks</div>
    <div class="hero-chip"><div class="dot" style="background:var(--accent-math)"></div>Typed answers only &mdash; no multiple choice</div>
    <div class="hero-chip"><div class="dot" style="background:var(--accent-warn)"></div>Hints describe the word, they never give it away</div>
  </div>
  <p class="credit">{meta['credit']}</p>
</div>
<div class="section-tabs">
{tabs}
</div>
<div class="main">
{''.join(body)}<div class="results-panel" id="results-panel">
  <div class="results-grade" id="results-grade">0%</div>
  <div class="results-label" id="results-label">Keep Practising</div>
  <div class="results-breakdown" id="results-breakdown"></div>
</div>

</div>

<script>{script}</script>
</body>
</html>
'''


def q_md(sec, q):
    ask = q_text(sec, q).replace('<em>', '*').replace('</em>', '*')
    return untag(ask).replace(' .', '.')


def help_md(sec, q):
    return untag(q_help(sec, q)).strip('() ')


def build_md(meta, sections):
    number_sections(sections)
    total = sections[-1]['last_q']
    stem = Path(meta['out']).name
    out = [f"# {untag(meta['md_title'])}",
           '',
           f'**Semester 1 vocabulary revision · typed answers only · {total} questions · {total} marks**',
           '', meta['md_intro'], '', '---', '']
    for i, sec in enumerate(sections):
        if i:
            out += ['---', '']
        out += [f'## {untag(sec["label"]).replace(" · ", " ")}: {untag(sec["title"])} '
                f'(Q{sec["first_q"]}&ndash;Q{sec["last_q"]})'.replace('&ndash;', '–'),
                '', untag(sec['info']), '']
        n = sec['first_q'] - 1
        for title, qs in sec['groups']:
            out += [f'### {untag(title)}', '']
            for q in qs:
                n += 1
                help_txt = help_md(sec, q)
                line = f'**Q{n}** (1 mark)\\\n{q_md(sec, q)} ({help_txt})'
                out += [line, '', 'Answer: ____________________', '']
    out += ['---', '', f'Answers: see `{stem}-answers.md` (keep it separate from this sheet).']
    return '\n'.join(out) + '\n'


def build_answers(meta, sections):
    number_sections(sections)
    out = [f'# {untag(meta["md_title"])} — Answers',
           '', meta['answers_note'], '',
           '| Q | Question | Accepted answers |',
           '|---|----------|------------------|']
    n = 0
    for sec in sections:
        for _title, qs in sec['groups']:
            for q in qs:
                n += 1
                out.append(f"| {n} | {q['a']} | {' / '.join(q['ans'])} |")
    out += ['', 'On the interactive sheet capital letters do not matter, trailing',
            'punctuation is ignored, and every spelling in the table above',
            'scores the mark. Hyphenated answers also accept the unhyphenated',
            'form (`rak buku` = `rak-buku`).']
    return '\n'.join(out) + '\n'


def main():
    flags = [a for a in sys.argv[1:] if a.startswith('--')]
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        sys.exit(f'usage: {Path(__file__).name} [--only-md] <spec.py>')
    mod = load(args[0])
    meta, sections = mod.META, mod.SECTIONS
    LANG.update(meta.get('lang', {}))
    out_base = ROOT / meta['out']
    out_base.parent.mkdir(parents=True, exist_ok=True)
    md_path = out_base.with_suffix('.md')
    md_path.write_text(build_md(meta, sections), encoding='utf-8')
    print(f'wrote {md_path.relative_to(ROOT)}')
    answers_path = out_base.with_name(out_base.name + '-answers.md')
    answers_path.write_text(build_answers(meta, sections), encoding='utf-8')
    print(f'wrote {answers_path.relative_to(ROOT)}')
    if '--only-md' in flags:
        print('html skipped (--only-md)')
    else:
        html_path = out_base.with_suffix('.html')
        html_path.write_text(build_html(meta, sections), encoding='utf-8')
        print(f'wrote {html_path.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
