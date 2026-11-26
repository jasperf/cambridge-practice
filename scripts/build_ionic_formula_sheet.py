"""Build the Ionic Formula Practice sheet (.html + printable .md + answers .md).

Edit the Q list below (cation, charge, anion, charge, answer, hint, reveal) and run:
    python3 scripts/build_ionic_formula_sheet.py
Output goes to s2/sem1/mocks/. The CSS is borrowed from sem1-science-bonding-ions.html,
so that file must exist. Re-run sheet_audit.py afterwards.
"""
import os
M=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','s2','sem1','mocks')+os.sep
src=open(M+'sem1-science-bonding-ions.html',encoding='utf-8').read().split('\n')
css='\n'.join(src[7:])  # from <style> line
css=css[:css.index('\n.ex-btns')]
css=css.replace('<style>','',1)
sub=str.maketrans('0123456789','₀₁₂₃₄₅₆₇₈₉')
sup=str.maketrans('0123456789+-','⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻')
def ion(sym,ch):  # ch like '2+'
    n,s=ch[:-1],ch[-1]
    return sym+(n if n!='1' else '')[:].translate(sup)+('⁺' if s=='+' else '⁻')
# (cation, charge, anion, charge, answer ascii, hint, reveal)
Q=[
('Na','1+','Cl','1-','NaCl','One 1+ cancels one 1&minus;.','Na⁺ and Cl⁻ have equal and opposite charges, so one of each: NaCl.'),
('Mg','2+','O','2-','MgO','2+ and 2&minus; already balance.','2+ and 2− cancel with one of each. Do not write Mg₂O₂: always give the simplest ratio, MgO.'),
('Mg','2+','F','1-','MgF2','How many 1&minus; ions cancel one 2+?','One Mg²⁺ needs two F⁻ to balance: MgF₂.'),
('Na','1+','O','2-','Na2O','How many 1+ ions cancel one 2&minus;?','Two Na⁺ (total 2+) balance one O²⁻: Na₂O.'),
('Al','3+','Cl','1-','AlCl3','Swap the charge numbers.','One Al³⁺ needs three Cl⁻: AlCl₃.'),
('K','1+','S','2-','K2S','Two of one ion, one of the other.','Two K⁺ (2+) balance one S²⁻: K₂S.'),
('Li','1+','N','3-','Li3N','Swap the charge numbers.','Three Li⁺ (3+) balance one N³⁻: Li₃N.'),
('Al','3+','O','2-','Al2O3','Find the smallest number both 3 and 2 divide into: 6.','Al³⁺ × 2 = 6+ and O²⁻ × 3 = 6−, so Al₂O₃.'),
('Ca','2+','N','3-','Ca3N2','Both charges are 2 and 3: the lowest common total is 6.','Ca²⁺ × 3 = 6+ and N³⁻ × 2 = 6−, so Ca₃N₂.'),
('Fe','3+','O','2-','Fe2O3','Same pattern as Al³⁺ and O²⁻.','Fe³⁺ × 2 = 6+ and O²⁻ × 3 = 6−, so Fe₂O₃.'),
]
def ions(q): return ion(q[0],q[1]), ion(q[2],q[3].replace('-','-'))
def ionfix(sym,ch): 
    n=ch[:-1]; s='⁺' if ch[-1]=='+' else '⁻'
    return sym+(n.translate(sup) if n!='1' else '')+s
cards=[];md=[];ans=[]
for i,q in enumerate(Q,1):
    a,b=ionfix(q[0],q[1]),ionfix(q[2],q[3])
    cards.append(f'''
  <div class="q-card" id="qcard-s{i}">
    <div class="q-header"><div class="q-num">Q{i}</div><div class="q-text">Write the formula of the compound made from <strong>{a}</strong> and <strong>{b}</strong>.</div><div class="q-marks">1 mark</div></div>
    <div class="q-body">
      <input type="text" class="text-input formula-input" id="s{i}-ans" placeholder="e.g. NaCl" autocomplete="off" autocapitalize="off" spellcheck="false">
      <div class="sub-row" aria-label="Subscript buttons"><span class="sub-lbl">Subscript:</span>{''.join(f'<button type="button" class="sub-btn" onclick="insSub(\'s{i}-ans\',\'{d.translate(sub)}\')">{d.translate(sub)}</button>' for d in '2345')}</div>
      <div class="q-actions">
        <button class="btn btn-check" onclick="checkFormula('s{i}','{q[4].translate(sub)}')">Check</button>
        <button class="btn btn-hint" onclick="showHint('s{i}','{q[5]}')">Hint</button>
        <button class="btn btn-reveal" onclick="revealAnswer('s{i}','<strong>{q[4].translate(sub)}</strong>. {q[6]}')">Show Answer</button>
      </div>
      <div class="feedback" id="s{i}-fb"></div>
    </div>
  </div>''')
    md.append(f'**Q{i}** (1 mark)\\\nWrite the formula of the compound made from **{a}** and **{b}**.\n\nAnswer: ____________________\n')
    ans.append(f'| Q{i} | {a} + {b} | **{q[4].translate(sub)}** | {q[6]} |')
extra='''
.sub-row { display: flex; align-items: center; gap: 6px; margin: 8px 0 12px; flex-wrap: wrap; }
.sub-lbl { font-family: var(--font-mono); font-size: 0.7rem; color: var(--text-muted); margin-right: 4px; }
.sub-btn { font-family: var(--font-mono); font-size: 0.95rem; min-width: 38px; padding: 5px 10px; border-radius: 6px; border: 1px solid var(--border); background: var(--surface2); color: var(--text); cursor: pointer; }
.sub-btn:hover { border-color: var(--sec); }
.sub-btn:disabled { opacity: 0.4; cursor: default; }
.worked { background: var(--surface2); border: 1px solid var(--border); border-left: 3px solid var(--sec); border-radius: 8px; padding: 14px 16px; margin-bottom: 22px; font-size: 0.9rem; }
.worked .f { font-family: var(--font-mono); color: var(--accent-warn); }
'''
html=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ionic Formula Practice</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,600;0,9..144,700;1,9..144,400&family=DM+Mono:wght@400;500&family=Literata:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>{css}{extra}</style>
</head>
<body>
<canvas id="confetti-canvas"></canvas>
<div class="topbar">
  <div class="topbar-left">
    <div class="logo">Student<span>'s</span> Study Hub</div>
    <div class="week-badge">Science &middot; Ionic Formulae</div>
  </div>
  <div style="display:flex;align-items:center;gap:14px;">
    <a href="../../../index.html" class="back-link">&larr; All sheets</a>
    <div class="timer-wrap">&#9201;<div class="timer" id="timer">00:00</div></div>
    <div class="score-pill"><div class="score-label">Score</div><div class="score-val" id="global-score">0 / 10</div></div>
  </div>
</div>
<div class="progress-wrap"><div class="progress-bar" id="progress-bar"></div></div>
<div class="hero">
  <div class="hero-eyebrow">Secondary 2 &middot; Science &middot; Atomic bonding</div>
  <h1>Ionic Formula<br><em>Practice</em></h1>
  <div class="hero-meta">
    <div class="hero-chip"><div class="dot"></div>10 questions &middot; self-marked &middot; 10 marks</div>
    <div class="hero-chip"><div class="dot" style="background:var(--accent-warn)"></div>About 10 minutes</div>
  </div>
  <p class="credit">Ten questions. Combine the ions into the neutral compound. Capital and lowercase letters matter: <strong>Co</strong> is cobalt, <strong>CO</strong> is carbon monoxide.</p>
</div>
<div class="main">
<div id="fo" style="--sec:var(--accent-math);--sec-rgb:79,142,247">
  <div class="section-header"><div class="section-icon">&#9878;</div><div><div class="sub-label">Q1&ndash;Q10 &middot; Atomic bonding</div><h2>Combine the ions</h2></div></div>
  <div class="facts-label">Method</div>
  <div class="worked"><strong>Total positive charge must equal total negative charge.</strong><br>
  Worked example: Ca²⁺ and Cl⁻ &mdash; two Cl⁻ are needed to balance one Ca²⁺, so the formula is <span class="f">CaCl₂</span>.<br><br>
  <strong>Quick check:</strong> swap the charge numbers and use them as subscripts, then reduce if both are divisible (Mg²⁺ + O²⁻ swaps to Mg₂O₂, which reduces to MgO).<br><br>
  For the small numbers, tap the subscript buttons or just type the digit: a typed 2 turns into ₂ automatically.</div>
  <div class="facts-label">Questions</div>
{''.join(cards)}

  <div class="section-score">
    <div class="section-score-label">FINAL SCORE</div>
    <div class="section-score-bar"><div class="section-score-fill" id="sec-fo-fill"></div></div>
    <div class="section-score-val" id="sec-fo-val">0/10</div>
  </div>
</div>
<div class="divider"></div>

<div class="results-panel" id="results-panel">
  <div class="results-grade" id="results-grade">0%</div>
  <div class="results-label" id="results-label">Keep Practising</div>
  <div class="results-breakdown" id="results-breakdown"></div>
</div>

</div>

<script>
const state = {{ answers: {{}}, correct: {{}}, startTime: Date.now() }};
const marks = {{ {', '.join(f's{i}:1' for i in range(1,11))} }};
const sections = {{ fo: {{ label: 'Ionic Formulae', qs: [{','.join(f"'s{i}'" for i in range(1,11))}] }} }};
const allQs = Object.values(sections).flatMap(s => s.qs);
const maxMarks = allQs.reduce((s,q) => s + marks[q], 0);
const SUBS = '₀₁₂₃₄₅₆₇₈₉';

function updateTimer() {{
  const e = Math.floor((Date.now()-state.startTime)/1000);
  document.getElementById('timer').textContent = `${{String(Math.floor(e/60)).padStart(2,'0')}}:${{String(e%60).padStart(2,'0')}}`;
}}
setInterval(updateTimer, 1000);

/* typed digits become subscripts */
document.querySelectorAll('.formula-input').forEach(inp => inp.addEventListener('input', () => {{
  const pos = inp.selectionStart;
  inp.value = inp.value.replace(/[0-9]/g, d => SUBS[+d]);
  try {{ inp.setSelectionRange(pos, pos); }} catch(e) {{}}
}}));

function insSub(id, ch) {{
  const inp = document.getElementById(id);
  if (inp.disabled) return;
  const a = inp.selectionStart ?? inp.value.length, b = inp.selectionEnd ?? a;
  inp.value = inp.value.slice(0, a) + ch + inp.value.slice(b);
  inp.focus(); inp.setSelectionRange(a+1, a+1);
}}

function toAscii(s) {{ return s.replace(/\\s+/g, '').replace(/[₀-₉]/g, c => SUBS.indexOf(c)); }}

function checkFormula(qid, correct) {{
  const input = document.getElementById(`${{qid}}-ans`);
  if (!input.value.trim()) {{ shakeCard(qid); return; }}
  if (state.correct[qid] !== undefined) return;
  const ok = toAscii(input.value) === toAscii(correct);
  input.disabled = true;
  input.style.borderColor = ok ? 'var(--correct)' : 'var(--wrong)';
  document.querySelectorAll(`#qcard-${{qid}} .sub-btn`).forEach(b => b.disabled = true);
  state.answers[qid] = input.value;
  markResult(qid, ok);
}}

function markResult(qid, isCorrect) {{
  state.correct[qid] = isCorrect;
  const card = document.getElementById(`qcard-${{qid}}`);
  card.classList.add(isCorrect ? 'answered-correct' : 'answered-wrong');
  if (isCorrect) card.classList.add('pulse-correct');
  const fb = document.getElementById(`${{qid}}-fb`);
  fb.className = `feedback show ${{isCorrect ? 'correct-fb' : 'wrong-fb'}}`;
  fb.innerHTML = isCorrect
    ? `✅ <strong>Correct!</strong> +${{marks[qid]}} mark`
    : `❌ <strong>Not quite.</strong> Check capitals and subscripts, then reveal the answer and balance the charges again.`;
  updateScores();
}}

function showHint(qid, hintText) {{
  const fb = document.getElementById(`${{qid}}-fb`);
  if (state.correct[qid] !== undefined) return;
  fb.className = 'feedback show hint-fb';
  fb.innerHTML = `💡 <strong>Hint:</strong> ${{hintText}}`;
}}

function revealAnswer(qid, answerText) {{
  const fb = document.getElementById(`${{qid}}-fb`);
  fb.className = 'feedback show reveal-fb';
  fb.innerHTML = `📖 <strong>Answer:</strong> ${{answerText}}`;
  if (state.correct[qid] === undefined) {{ state.correct[qid] = false; updateScores(); }}
}}

function shakeCard(qid) {{
  const card = document.getElementById(`qcard-${{qid}}`);
  card.classList.remove('shake'); void card.offsetWidth; card.classList.add('shake');
}}

function updateScores() {{
  let totalScore = 0, totalAnswered = 0;
  for (const [key, sec] of Object.entries(sections)) {{
    const secMax = sec.qs.reduce((s,q) => s+marks[q], 0);
    let secScore = 0;
    sec.qs.forEach(qid => {{
      if (state.correct[qid] === true) {{ secScore += marks[qid]; totalScore += marks[qid]; }}
      if (state.correct[qid] !== undefined) totalAnswered++;
    }});
    document.getElementById(`sec-${{key}}-fill`).style.width = (secScore/secMax)*100 + '%';
    document.getElementById(`sec-${{key}}-val`).textContent = `${{secScore}}/${{secMax}}`;
  }}
  document.getElementById('global-score').textContent = `${{totalScore}} / ${{maxMarks}}`;
  document.getElementById('progress-bar').style.width = `${{(totalAnswered/allQs.length)*100}}%`;
  if (totalAnswered === allQs.length) showResults(totalScore);
}}

function showResults(total) {{
  const pct = Math.round((total/maxMarks)*100);
  const grade = pct>=85?'🏆 Excellent!':pct>=70?'⭐ Great Job!':pct>=55?'👍 Good Effort':'📚 Keep Practising';
  const elapsed = Math.floor((Date.now()-state.startTime)/1000);
  const mins=Math.floor(elapsed/60), secs=elapsed%60;
  document.getElementById('results-grade').textContent = `${{pct}}%`;
  document.getElementById('results-label').textContent = grade;
  const bd = document.getElementById('results-breakdown');
  bd.innerHTML = `<div class="rb-chip">Score<span class="rb-val">${{total}}/${{maxMarks}}</span></div><div class="rb-chip">Time<span class="rb-val">${{mins}}m ${{secs}}s</span></div>`;
  const panel = document.getElementById('results-panel');
  panel.classList.add('show');
  panel.scrollIntoView({{ behavior:'smooth', block:'center' }});
  if (pct >= 70) launchConfetti();
  try {{ localStorage.setItem(`sem1-science-ionic-formulae_${{Date.now()}}`, JSON.stringify({{ date: new Date().toISOString(), pct, total, time: `${{mins}}m${{secs}}s` }})); }} catch(e) {{}}
}}

function launchConfetti() {{
  const canvas = document.getElementById('confetti-canvas');
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth; canvas.height = window.innerHeight;
  const colors = ['#3ecf8e','#4f8ef7','#f5a623','#e05252','#fff'];
  const pieces = Array.from({{length:120}}, (_, i) => ({{
    x:(i*53)%canvas.width, y:-((i*37)%canvas.height), w:(i%7)+4, h:(i%5)+3,
    color:colors[i%colors.length], rot:(i%6), vy:(i%4)+2, vx:((i%5)-2)*0.4, vr:((i%5)-2)*0.04
  }}));
  let frame=0;
  function draw() {{
    ctx.clearRect(0,0,canvas.width,canvas.height);
    pieces.forEach(p => {{
      ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.rot);
      ctx.fillStyle=p.color; ctx.globalAlpha=0.85;
      ctx.fillRect(-p.w/2,-p.h/2,p.w,p.h); ctx.restore();
      p.y+=p.vy; p.x+=p.vx; p.rot+=p.vr;
    }});
    frame++;
    if(frame<200) requestAnimationFrame(draw); else ctx.clearRect(0,0,canvas.width,canvas.height);
  }}
  draw();
}}

document.addEventListener('keydown', e => {{
  if (e.key !== 'Enter') return;
  const a = document.activeElement;
  if (a && a.classList.contains('text-input')) a.closest('.q-body')?.querySelector('.btn-check')?.click();
}});
</script>
</body>
</html>
'''
open(M+'sem1-science-ionic-formulae.html','w',encoding='utf-8').write(html)
head='''# Secondary 2 · Science — Ionic Formula Practice

**10 questions · 10 marks**

Ten questions. Combine the ions into the neutral compound. Q1–Q10 match the interactive sheet. Capital and lowercase letters matter: **Co** is cobalt, **CO** is carbon monoxide.

---

## Method

Total positive charge must equal total negative charge. Worked example: Ca²⁺ and Cl⁻ need two Cl⁻ to balance one Ca²⁺, so the formula is CaCl₂.

Quick check: swap the charge numbers and use them as subscripts, then reduce if both are divisible (Mg²⁺ + O²⁻ swaps to Mg₂O₂, which reduces to MgO).

---

## Questions

'''
open(M+'sem1-science-ionic-formulae.md','w',encoding='utf-8').write(head+'\n'.join(md)+'\n**Final score:** ______ / 10\n')
open(M+'sem1-science-ionic-formulae-answers.md','w',encoding='utf-8').write('# Answers — Ionic Formula Practice\n\n**10 marks** (1 mark each; capitals and subscripts must be correct).\n\n| Q | Ions | Formula | Working |\n|---|---|---|---|\n'+'\n'.join(ans)+'\n')
