"""Spec: Secondary 2 · Semester 1 maths — Gaps Drill 2: the whole revision pack in one sheet, all-new numbers.

Build with:  python3 scripts/build_review_sheet.py scripts/review_specs/s2_sem1_maths_gaps2.py

Covers every topic in the student's own revision pack: expressions in n, simplifying surds,
surds in brackets, a powers table + zero/negative powers + powers of 10, indices in fractions,
brackets/signs/simultaneous equations, mixed numbers with powers, and rational vs irrational
numbers (incl. the integers-inside-rationals Venn diagram). No calculator.
"""

META = dict(
    out='s2/sem1/mocks/sem1-maths-gaps2',
    title='Maths Gaps Drill 2 &middot; Practice',
    badge='Maths &middot; Gaps Drill 2',
    eyebrow='Secondary 2 &middot; Mathematics &middot; Semester 1 topic drill',
    h1='Gaps Drill 2<br><em>all eight topics, new numbers</em>',
    md_title='Secondary 2 · Maths — Gaps Drill 2',
    intro=('The same eight topics as the first Gaps Drill, with all-new numbers: expressions in <em>n</em>, '
           'simplifying surds, surds in brackets, zero, negative and powers of 10, indices in fractions, '
           'brackets and simultaneous equations, mixed numbers with powers, and rational and irrational numbers. '
           '<strong>Write every answer on paper first</strong>, then type only the final number (or pick a letter). '
           'Use <strong>Cover the notes</strong> to test yourself before you read the key facts. No calculator.'),
    md_intro=('A second practice sheet on the eight topics where marks are easy to lose. Write every answer in your '
              'notebook. Q1–Q45 match the interactive sheet; Q46–Q52 are written questions for you to show full '
              'working. No calculator is needed.'),
    time_chip='About 50 minutes &middot; no calculator',
    storage_key='sem1-maths-gaps2',
    back='../../../index.html',
    answers_note='Answers for Q1–Q45 (auto-marked on the interactive sheet) and a marking guide for the written questions Q46–Q52. Keep this separate from the question sheet.',
    extra_links=[('./sem1-maths-gaps.html', 'Gaps Drill 1'),
                 ('../../reference/maths-formula-sheets/index.html', 'Formula sheets')],
)

EXPLORER_CSS = '''
.ftable { border-collapse: collapse; margin: 6px 0 14px; font-size: 0.9rem; }
.ftable th, .ftable td { border: 1px solid var(--border); padding: 6px 14px; text-align: center; }
.ftable th { background: var(--surface2); font-family: var(--font-mono); font-size: 0.76rem; color: var(--text-muted); }
.ex-btns { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 12px; }
.ex-btn { font-family: var(--font-mono); font-size: 0.8rem; padding: 7px 12px; border-radius: 6px; border: 1px solid var(--border); background: var(--surface2); color: var(--text); cursor: pointer; }
.ex-btn:hover { border-color: var(--sec); }
.ex-btn.on { background: rgba(var(--sec-rgb),0.18); border-color: var(--sec); }
#vn-dot { transition: cx 0.8s ease, cy 0.8s ease; }
@media (prefers-reduced-motion: reduce) { #vn-dot { transition: none; } }
#dsq-range { width: 100%; max-width: 420px; accent-color: var(--sec); }
'''

W1 = '../t1/w5/term1-week5-maths-expressions-formulae.html'
W2 = '../t1/w2/term1-week2-maths-rational-irrational.html'
W3 = '../t1/w2/term1-week2-maths-indices-standard-form.html'
W4 = '../t1/w8/term1-week8-maths-unit4-simultaneous-equations.html'
W5 = '../t2/w8/term2-week8-maths-unit8-fractions.html'

SECTIONS = [
  dict(key='ex', icon='&#128221;', color='var(--accent-math)', rgba='79,142,247',
       title='Words to Expressions in <em>n</em>', label='Expressions in n',
       src='Expressions &amp; Formulae', link=W1, link_label='Expressions &amp; formulae sheet',
       facts=[
         ('Do the steps in order', 'Each <em>then</em> works on the <strong>whole</strong> result so far. &ldquo;Subtract 1, then double&rdquo; is <span class="f">2(n &minus; 1)</span>, not 2n &minus; 1.'),
         ('Brackets', 'If a step applies to a <em>sum or difference</em>, that part goes in brackets. Without them, only the last term gets the step.'),
         ('&ldquo;Squares&rdquo; is a power', '<strong>Squares</strong> means &ldquo;to the power 2&rdquo; and <strong>cubes</strong> means &ldquo;to the power 3&rdquo;. A <strong>square root</strong> uses the root sign. Different words, different operations.'),
         ('Rule from a table', 'The value at <em>0</em> is the fixed charge. The jump from one column to the next is the amount for each extra unit. So <span class="f">cost = fixed + jump &times; units</span>.'),
         ('Check with a number', 'Put a small number in for <em>n</em>, follow the words step by step, and see if the expression gives the same answer.'),
       ]),
  dict(key='su', icon='&#8730;', color='var(--accent-sci)', rgba='62,207,142',
       title='Simplifying Surds', label='Simplifying Surds',
       src='Rational &amp; Irrational Numbers', link=W2, link_label='Rational &amp; irrational sheet',
       facts=[
         ('The splitting rule', '<span class="f">&radic;(a &times; b) = &radic;a &times; &radic;b</span>.'),
         ('Use the largest square factor', 'Look for the biggest of <em>4, 9, 16, 25, 36, 49, 64, 81, 100</em> that divides the number. Its root comes out as a whole number in front.'),
         ('Check by squaring', 'Square the number in front, then multiply by the number under the root. You should get the number you started with.'),
         ('Adding surds', 'Surds add like terms only when the part under the root matches: 3&radic;2 + 4&radic;2 = 7&radic;2. Simplify each one first.'),
         ('When it stays', 'If no square number (except 1) divides it, the root is already in its simplest form.'),
       ]),
  dict(key='sb', icon='&#128208;', color='var(--accent-warn)', rgba='245,166,35',
       title='Surds in Brackets', label='Surds in Brackets',
       src='Rational &amp; Irrational Numbers', link=W2, link_label='Rational &amp; irrational sheet',
       facts=[
         ('Expand as usual', 'Multiply every term in the first bracket by every term in the second. Remember <span class="f">&radic;n &times; &radic;n = n</span>.'),
         ('Difference of two squares', '<span class="f">(a + b)(a &minus; b) = a&sup2; &minus; b&sup2;</span>. The two middle terms are opposites, so they cancel.'),
         ('Why it matters', 'When the middle terms cancel, the surds vanish. The answer can be a whole number even though the brackets hold a surd.'),
         ('No calculator', 'Leave answers as surds or whole numbers. Never turn &radic;n into a rounded decimal.'),
       ]),
  dict(key='pw', icon='&#10024;', color='var(--accent-math)', rgba='79,142,247',
       title='Powers, Zero, Negative &amp; Powers of 10', label='Powers & Negative Powers',
       src='Indices &amp; Standard Form', link=W3, link_label='Indices &amp; standard form sheet',
       facts=[
         ('Use the table', 'Powers of the same base: multiply means <em>add</em> the powers (7<sup>2</sup> &times; 7<sup>4</sup> = 7<sup>6</sup>), divide means <em>subtract</em>. A table of powers lets you read the answer off.'),
         ('Zero power', 'Any number (except 0) to the power 0 is <strong>1</strong>.'),
         ('Negative power', '<span class="f">x<sup>&minus;n</sup> = 1 &divide; x<sup>n</sup></span>. It is a <em>fraction</em>, not a negative number, and <strong>x<sup>&minus;1</sup> is not x</strong>.'),
         ('Multiplying by 10<sup>n</sup>', 'Multiplying by 10<sup>3</sup> makes a number 1000 times bigger. Multiplying by 10<sup>&minus;3</sup> is the same as <em>dividing</em> by 1000.'),
         ('Dividing by 10<sup>&minus;n</sup>', 'Dividing by 10<sup>&minus;n</sup> is the same as <em>multiplying</em> by 10<sup>n</sup>. Two minuses make it bigger.'),
       ]),
  dict(key='ix', icon='&#128208;', color='var(--accent-sci)', rgba='62,207,142',
       title='Indices &amp; Fractions', label='Indices & Fractions',
       src='Indices &amp; Standard Form', link=W3, link_label='Indices &amp; standard form sheet',
       facts=[
         ('Three laws', 'Multiply: <em>add</em> the powers. Divide: <em>subtract</em> the powers. Power of a power: <em>multiply</em> the powers.'),
         ('Numbers and letters separately', 'Work out the numbers first, then deal with each letter by itself.'),
         ('Cube or square the whole bracket', 'In (3m<sup>2</sup>)<sup>4</sup> the power outside applies to the <em>3</em> as well as to the m<sup>2</sup>.'),
         ('A negative power in a fraction', 'An answer such as y<sup>&minus;5</sup> is written as <span class="f">1/y<sup>5</sup></span> when the question wants a fraction.'),
       ]),
  dict(key='br', icon='&#9999;&#65039;', color='var(--accent-warn)', rgba='245,166,35',
       title='Brackets, Signs &amp; Equations', label='Brackets & Signs',
       src='Expressions &amp; Simultaneous Equations', link=W4, link_label='Simultaneous equations sheet',
       facts=[
         ('Two brackets', 'Multiply every term by every term, then collect the like terms in the middle.'),
         ('Signs', 'A negative times a negative is positive. A minus in front of a bracket changes <em>every</em> sign inside it.'),
         ('Subtracting equations', 'Put the second equation in brackets first. The minus then applies to <strong>every</strong> term, including the right-hand side.'),
         ('Then substitute back', 'After finding one letter, put it into an original equation to find the other, then check it in the <em>other</em> equation.'),
       ]),
  dict(key='mn', icon='&#189;', color='var(--accent-math)', rgba='79,142,247',
       title='Mixed Numbers &amp; Powers', label='Mixed Numbers',
       src='Fractions', link=W5, link_label='Fractions sheet',
       facts=[
         ('Convert first', 'Change mixed numbers to <em>improper fractions</em> before you square, multiply or divide. Never square the whole part and the fraction part separately.'),
         ('Dividing', 'To divide by a fraction, flip the second fraction and multiply.'),
         ('Order of working', 'Powers first, then multiplication and division, then adding and subtracting.'),
       ]),
  dict(key='ra', icon='&#960;', color='var(--accent-sci)', rgba='62,207,142',
       title='Rational &amp; Irrational Numbers', label='Rational & Irrational',
       src='Rational &amp; Irrational Numbers', link=W2, link_label='Rational &amp; irrational sheet',
       facts=[
         ('The pizza picture', 'A <strong>rational</strong> number is a pizza you can cut fairly: 3 slices out of 4 is 3/4. An <strong>irrational</strong> number can never be cut fairly, however small the slices. There is always a crumb left over. &pi; is that impossible pizza.'),
         ('Rational', 'Can be written as a fraction of two integers (the bottom is not 0). Whole numbers, terminating decimals like 0.25 and recurring decimals like 0.2525&hellip; are all rational.'),
         ('Irrational', 'Cannot be written as a fraction. The decimal never ends and never repeats. Examples: &pi;, &radic;2, &radic;8.'),
         ('Roots that fool you', '&radic;49 = 7 and &#8731;27 = 3 are whole numbers, so they are <strong>rational</strong>. &radic;8 and &#8731;10 are not perfect roots, so they are <strong>irrational</strong>.'),
         ('The Venn diagram', 'Integers sit <em>inside</em> the rational numbers (every integer is a fraction over 1). Irrational numbers sit <em>outside</em> the rational circle altogether.'),
       ]),
]

# ---------------------------------------------------------------- questions

Q = []
def num(id, sec, marks, q, ans, hint, reveal, unit='', tol=0, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='num', q=q, ans=ans, tol=tol, unit=unit, hint=hint, reveal=reveal, fig=fig, figmd=figmd))
def mcq(id, sec, marks, q, opts, correct, hint, reveal, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='mcq', q=q, opts=opts, correct=correct, hint=hint, reveal=reveal, fig=fig, figmd=figmd))

WP = '<em>Write it on paper first.</em> '

KAYAK_FIG = ('<table class="ftable"><tr><th>Days</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr>'
             '<tr><th>Cost ($)</th><td>12</td><td>19</td><td>26</td><td>33</td><td>40</td></tr></table>')
KAYAK_MD = 'Table. Days 0, 1, 2, 3, 4. Cost in $: 12, 19, 26, 33, 40.'

POW_FIG = ('<table class="ftable"><tr><th>Power</th><td>7<sup>2</sup></td><td>7<sup>3</sup></td><td>7<sup>4</sup></td><td>7<sup>5</sup></td><td>7<sup>6</sup></td></tr>'
           '<tr><th>Value</th><td>49</td><td>343</td><td>2 401</td><td>16 807</td><td>117 649</td></tr></table>')
POW_MD = 'Table of powers of 7: 7² = 49, 7³ = 343, 7⁴ = 2 401, 7⁵ = 16 807, 7⁶ = 117 649.'

VENN_FIG = ('<svg viewBox="0 0 320 170" style="max-width:340px;width:100%;margin:6px 0 12px" role="img" '
            'aria-label="A small circle A labelled integers inside a bigger circle B labelled rational numbers">'
            '<rect x="2" y="2" width="316" height="166" rx="10" fill="none" stroke="currentColor" opacity="0.25"/>'
            '<ellipse cx="140" cy="88" rx="118" ry="70" fill="rgba(79,142,247,0.12)" stroke="#4f8ef7" stroke-width="2"/>'
            '<ellipse cx="102" cy="92" rx="58" ry="40" fill="rgba(62,207,142,0.18)" stroke="#3ecf8e" stroke-width="2"/>'
            '<text x="102" y="96" text-anchor="middle" font-size="13" fill="currentColor">A: integers</text>'
            '<text x="212" y="52" text-anchor="middle" font-size="13" fill="currentColor">B: rational</text>'
            '<text x="288" y="150" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.7">irrational</text></svg>')
VENN_MD = 'Venn diagram. Circle A (integers) is drawn inside circle B (rational numbers). Irrational numbers lie outside circle B.'

# ---- A: expressions in n
num('e1','ex',2, WP + 'Sam thinks of a number, <em>n</em>. He <strong>subtracts 3</strong>, then <strong>multiplies the result by 4</strong>. Write his expression. What is its value when <em>n</em> = 9?',
    24, 'Do the steps in order with n = 9. What happens to the 3?', 'Expression: 4(<em>n</em> &minus; 3). When n = 9: 4 &times; 6 = 24.')
num('e2','ex',2, WP + 'Zara thinks of <em>n</em>. She <strong>multiplies it by 3</strong>, <strong>squares</strong> the result, then <strong>subtracts 5</strong>. Write her expression. What is its value when <em>n</em> = 2?',
    31, 'Squares means power 2. Which part gets squared?', 'Expression: (3<em>n</em>)<sup>2</sup> &minus; 5. When n = 2: 6<sup>2</sup> &minus; 5 = 36 &minus; 5 = 31.')
mcq('e3','ex',1, 'Raj thinks of <em>n</em>. He <strong>adds 4</strong>, <strong>divides by 2</strong>, then <strong>cubes</strong> the result. Which expression is his?',
    ['(<em>n</em> + 4)/2<sup>3</sup>', '<em>n</em> + 4/2<sup>3</sup>', '((<em>n</em> + 4)/2)<sup>3</sup>', '(<em>n</em> + 4)/2 &times; 3'], 'c',
    'The cube applies to the whole result of adding and dividing.',
    'C &mdash; The cube is the last step, so it goes outside a bracket around (n + 4)/2. In option A only the 2 is cubed.')
num('e4','ex',2, WP + 'A shop hires kayaks for a fixed fee plus a daily amount. The table shows the cost. How much does it cost to hire a kayak for <strong>8 days</strong>?',
    68, 'Day 0 is the fixed fee. How much does each extra day add?', 'Fixed fee $12, plus $7 a day. 12 + 7 &times; 8 = 68.', unit='$', fig=KAYAK_FIG, figmd=KAYAK_MD)
num('e5','ex',1, WP + 'Using the same table, an expression for the cost of <em>d</em> days is 12 + 7<em>d</em>. What is its value when <em>d</em> = 15?',
    117, 'Put 15 in for d, then multiply before you add.', '12 + 7 &times; 15 = 12 + 105 = 117.', unit='$', fig=KAYAK_FIG, figmd='Same table as Q4.')

# ---- B: simplifying surds
num('u1','su',1, WP + 'Simplify &radic;150 and write it as <em>a</em>&radic;6. Find <em>a</em>.',
    5, 'Which square number divides 150?', '&radic;150 = &radic;(25 &times; 6) = 5&radic;6, so a = 5. Check: 5<sup>2</sup> &times; 6 = 150.')
num('u2','su',1, WP + 'Simplify &radic;98 and write it as <em>a</em>&radic;2. Find <em>a</em>.',
    7, 'Use the largest square factor of 98. Try 49.', '&radic;98 = &radic;(49 &times; 2) = 7&radic;2, so a = 7.')
mcq('u3','su',1, 'A student writes &radic;45 = 9&radic;5. What is the correct simplified form?',
    ['3&radic;5', '9&radic;5', '5&radic;3', '15&radic;3'], 'a',
    'The 9 is a square number, so its root should come out, not 9 itself.',
    'A &mdash; &radic;45 = &radic;(9 &times; 5) = 3&radic;5. Check: 3<sup>2</sup> &times; 5 = 45, but 9<sup>2</sup> &times; 5 = 405.')
num('u4','su',2, WP + 'Work out (5&radic;2)<sup>2</sup>.',
    50, 'Square the 5 and square the &radic;2 separately, then multiply.', '(5&radic;2)<sup>2</sup> = 5<sup>2</sup> &times; (&radic;2)<sup>2</sup> = 25 &times; 2 = 50.')
num('u5','su',2, WP + 'Simplify &radic;75 + &radic;12 and write it as <em>a</em>&radic;3. Find <em>a</em>.',
    7, 'Simplify each root first. Then add the numbers in front.', '&radic;75 = 5&radic;3 and &radic;12 = 2&radic;3. Sum: 7&radic;3, so a = 7.')
num('u6','su',1, WP + 'Simplify &radic;80 and write it as <em>a</em>&radic;5. Find <em>a</em>.',
    4, 'Is 16 a factor of 80?', '&radic;80 = &radic;(16 &times; 5) = 4&radic;5, so a = 4.')

# ---- C: surds in brackets
num('b1','sb',1, WP + 'If <em>n</em> = 18, then &radic;<em>n</em> &minus; 4 in simplest form is <em>a</em>&radic;2 &minus; 4. Find <em>a</em>.',
    3, 'Simplify &radic;18 first.', '&radic;18 = &radic;(9 &times; 2) = 3&radic;2, so a = 3. You cannot subtract 4 from 3&radic;2.')
num('b2','sb',2, WP + 'Expand and simplify (&radic;11 + 3)(&radic;11 &minus; 3).',
    2, 'Four terms. What happens to the two middle ones?', '11 &minus; 3&radic;11 + 3&radic;11 &minus; 9 = 11 &minus; 9 = 2.')
num('b3','sb',1, WP + 'Expand (&radic;<em>n</em> + 6)(&radic;<em>n</em> &minus; 6). What is its value when <em>n</em> = 50?',
    14, 'Difference of two squares: (a + b)(a &minus; b) = a<sup>2</sup> &minus; b<sup>2</sup>.', '(&radic;n + 6)(&radic;n &minus; 6) = n &minus; 36. When n = 50: 50 &minus; 36 = 14.')
num('b4','sb',2, WP + 'Expand (&radic;<em>n</em> + 7)(&radic;<em>n</em> &minus; 7). It simplifies to <em>n</em> &minus; <em>k</em>. Find <em>k</em>.',
    49, 'The middle terms cancel. What is 7 &times; 7?', '&radic;n &times; &radic;n = n, the middle terms cancel, and 7 &times; 7 = 49. So the answer is n &minus; 49, and k = 49.')
mcq('b5','sb',2, 'Tom says: &ldquo;If <em>n</em> is an integer, then (&radic;<em>n</em> + 3)(&radic;<em>n</em> &minus; 3) is also an integer.&rdquo; Is he correct?',
    ['No. It still has a surd in it.', 'No. It is only an integer when <em>n</em> is a square number.',
     'Yes, but only when <em>n</em> is bigger than 9.', 'Yes. It simplifies to <em>n</em> &minus; 9, which is always an integer.'], 'd',
    'Expand it. What happens to the middle terms?',
    'D &mdash; The middle terms cancel, leaving n &minus; 9. An integer minus 9 is always an integer, even when n is not a square number. Try n = 12: 12 &minus; 9 = 3.')

# ---- D: powers
num('p1','pw',2, WP + 'Use the table of powers of 7. Work out 343 &times; 2 401.',
    823543, 'Write each number as a power of 7, then add the powers. Then read the table.', '343 = 7<sup>3</sup> and 2 401 = 7<sup>4</sup>. So the product is 7<sup>7</sup> = 7 &times; 117 649 = 823 543.',
    fig=POW_FIG, figmd=POW_MD)
num('p2','pw',2, WP + 'Use the table. Work out 117 649 &divide; 343.',
    343, '7<sup>6</sup> &divide; 7<sup>3</sup>: subtract the powers.', '7<sup>6</sup> &divide; 7<sup>3</sup> = 7<sup>3</sup> = 343.', fig=POW_FIG, figmd='Same table as Q17.')
mcq('p3','pw',2, 'Use the table. Work out 343 &divide; 16 807 as a fraction in its simplest form.',
    ['1/16 464', '1/49', '1/14', '49'], 'b',
    '343 is 7<sup>3</sup> and 16 807 is 7<sup>5</sup>. Subtract the powers.',
    'B &mdash; 7<sup>3</sup> &divide; 7<sup>5</sup> = 7<sup>&minus;2</sup> = 1/7<sup>2</sup> = 1/49. Option D flips the fraction.', fig=POW_FIG, figmd='Same table as Q17.')
num('p4','pw',1, WP + 'Write 5<sup>&minus;2</sup> as a decimal.',
    0.04, 'A negative power means a fraction: 1 divided by what?', '5<sup>&minus;2</sup> = 1/5<sup>2</sup> = 1/25 = 0.04.', tol=1e-6)
num('p5','pw',2, WP + 'y = <em>x</em><sup>0</sup> &minus; <em>x</em><sup>&minus;1</sup> + <em>x</em><sup>&minus;2</sup>. Find <em>y</em> when <em>x</em> = 4. Give a decimal.',
    0.8125, 'x<sup>0</sup> = 1. x<sup>&minus;1</sup> = 1/x. x<sup>&minus;2</sup> = 1/x<sup>2</sup>.', 'y = 1 &minus; 0.25 + 0.0625 = 0.8125.', tol=1e-6)
num('p6','pw',2, WP + 'Work out 4 800 &divide; 10<sup>&minus;3</sup>.',
    4800000, 'Dividing by 10<sup>&minus;3</sup> is the same as multiplying by what?', '4 800 &divide; 10<sup>&minus;3</sup> = 4 800 &times; 10<sup>3</sup> = 4 800 000.')
num('p7','pw',2, WP + '0.09 &divide; 10<sup><em>k</em></sup> = 9 000. Find <em>k</em>.',
    -5, 'The answer is much bigger than 0.09, so dividing must make it bigger. What kind of power does that?', '0.09 &times; 10<sup>5</sup> = 9 000, so dividing by 10<sup>&minus;5</sup> gives 9 000 and k = &minus;5.')
num('p8','pw',1, WP + '7 200 &divide; 10<sup><em>k</em></sup> = 0.72. Find <em>k</em>.',
    4, 'How many places does the decimal point move?', '7 200 &divide; 10 000 = 0.72, so 10<sup>4</sup> and k = 4.')

# ---- E: indices and fractions
num('i1','ix',1, WP + '24<em>a</em><sup>8</sup> &divide; 6<em>a</em><sup>3</sup> = 4<em>a</em><sup><em>k</em></sup>. Find <em>k</em>.',
    5, 'Subtract the powers: 8 &minus; 3.', '24 &divide; 6 = 4 and a<sup>8</sup> &divide; a<sup>3</sup> = a<sup>5</sup>, so k = 5.')
num('i2','ix',2, WP + '12<em>a</em><sup>3</sup> &divide; 18<em>a</em><sup>8</sup> simplifies to 2/(3<em>a</em><sup><em>k</em></sup>). Find <em>k</em>.',
    5, 'The top power is smaller than the bottom power, so some a is left on the bottom.', '12/18 = 2/3 and a<sup>3&minus;8</sup> = a<sup>&minus;5</sup> = 1/a<sup>5</sup>. So the answer is 2/(3a<sup>5</sup>), and k = 5.')
num('i3','ix',2, WP + '(3<em>n</em><sup>5</sup> &times; 8<em>n</em><sup>2</sup>) &divide; (2<em>n</em><sup>2</sup>)<sup>2</sup> simplifies to <em>an</em><sup><em>b</em></sup>. Find <em>a</em> + <em>b</em>.',
    9, 'Top first, then bottom, then combine. Square the 2 as well.', 'Top: 24n<sup>7</sup>. Bottom: (2n<sup>2</sup>)<sup>2</sup> = 4n<sup>4</sup>. Combine: 6n<sup>3</sup>. So a = 6, b = 3 and a + b = 9.')
num('i4','ix',1, WP + '(3<em>n</em><sup>2</sup>)<sup>3</sup> = <em>an</em><sup><em>b</em></sup>. Find <em>a</em> + <em>b</em>.',
    33, 'The power 3 applies to the 3 as well.', '(3n<sup>2</sup>)<sup>3</sup> = 3<sup>3</sup> &times; n<sup>6</sup> = 27n<sup>6</sup>, so a + b = 27 + 6 = 33.')

# ---- F: brackets, signs and equations
num('r1','br',1, WP + '(<em>x</em> + 5)(<em>x</em> + 4) = <em>x</em><sup>2</sup> + <em>bx</em> + 20. Find <em>b</em>.',
    9, 'Add the two middle terms.', 'x<sup>2</sup> + 4x + 5x + 20 = x<sup>2</sup> + 9x + 20, so b = 9.')
num('r2','br',2, WP + '(<em>y</em> + 9)(<em>y</em> &minus; 4) = <em>y</em><sup>2</sup> + <em>by</em> &minus; 36. Find <em>b</em>.',
    5, 'The middle terms are &minus;4y and +9y.', 'y<sup>2</sup> &minus; 4y + 9y &minus; 36 = y<sup>2</sup> + 5y &minus; 36, so b = 5.')
num('r3','br',2, WP + '(3<em>y</em> + 2)(2<em>y</em> &minus; 5) = 6<em>y</em><sup>2</sup> + <em>by</em> &minus; 10. Find <em>b</em>. (It can be negative.)',
    -11, 'Middle terms: 3y &times; &minus;5 and 2 &times; 2y.', '6y<sup>2</sup> &minus; 15y + 4y &minus; 10 = 6y<sup>2</sup> &minus; 11y &minus; 10, so b = &minus;11.')
num('r4','br',1, WP + '5(2<em>y</em> + 3) = 10(<em>y</em> + <em>k</em>). Find <em>k</em>. Give a decimal.',
    1.5, 'Expand both sides.', '5(2y + 3) = 10y + 15 and 10(y + k) = 10y + 10k, so 10k = 15 and k = 1.5.', tol=1e-6)
mcq('r5','br',2, 'Which expression is the same as 2(3<em>x</em> &minus; 4) &minus; (<em>x</em> &minus; 5)?',
    ['5<em>x</em> &minus; 3', '5<em>x</em> &minus; 13', '7<em>x</em> &minus; 13', '7<em>x</em> &minus; 3'], 'a',
    'The minus in front of the second bracket changes every sign inside it.',
    'A &mdash; 6x &minus; 8 &minus; x + 5 = 5x &minus; 3. Option B forgets that &minus;(&minus;5) = +5. Options C and D forget to change the sign of x.')
num('r6','br',2, WP + '5<em>x</em> + 2<em>y</em> = 23 and 5<em>x</em> &minus; 3<em>y</em> = 3. <strong>Subtract the second equation from the first.</strong> You get <em>ay</em> = <em>c</em>. Find <em>a</em> + <em>c</em>.',
    25, 'Put the second equation in brackets. 2y &minus; (&minus;3y) = ?', '(5x + 2y) &minus; (5x &minus; 3y) = 5y and 23 &minus; 3 = 20. So 5y = 20, a = 5, c = 20 and a + c = 25.')
num('r7','br',2, WP + 'Now solve the same pair: 5<em>x</em> + 2<em>y</em> = 23 and 5<em>x</em> &minus; 3<em>y</em> = 3. Find <em>x</em> + <em>y</em>.',
    7, 'Find y, then put it back into one equation to find x.', '5y = 20 gives y = 4. Then 5x + 8 = 23, so x = 3. Check in the second: 15 &minus; 12 = 3. x + y = 7.')

# ---- G: mixed numbers and powers
num('m1','mn',2, WP + 'Work out (3&frac12;)<sup>2</sup> &minus; 2&frac14; &divide; 1&frac12;. Give a decimal.',
    10.75, 'Convert to improper fractions. Power first, then the division, then subtract.', '(7/2)<sup>2</sup> = 49/4 = 12.25. 9/4 &divide; 3/2 = 9/4 &times; 2/3 = 1.5. So 12.25 &minus; 1.5 = 10.75.', tol=1e-6)
num('m2','mn',2, WP + 'Work out (5&frac12;)<sup>2</sup> + 2&frac23; &times; &frac34;. Give a decimal.',
    32.25, 'Power first. 2&frac23; = 8/3.', '(11/2)<sup>2</sup> = 121/4 = 30.25. 8/3 &times; 3/4 = 2. Total: 32.25.', tol=1e-6)
num('m3','mn',2, WP + 'Work out (1&frac14;)<sup>2</sup> + 4&frac12; &divide; 1&frac15;. Give a decimal.',
    5.3125, '1&frac14; = 5/4, 4&frac12; = 9/2 and 1&frac15; = 6/5.', '(5/4)<sup>2</sup> = 25/16 = 1.5625. 9/2 &divide; 6/5 = 9/2 &times; 5/6 = 45/12 = 3.75. Total: 5.3125.', tol=1e-6)
num('m4','mn',2, WP + 'Work out (7&frac12;)<sup>2</sup> &minus; 2&#8532; &times; 5/6. Give a decimal.',
    54.25, 'Multiplication before subtraction. 2&#8532; = 12/5.', '(15/2)<sup>2</sup> = 225/4 = 56.25. 12/5 &times; 5/6 = 2. So 56.25 &minus; 2 = 54.25.', tol=1e-6)
mcq('m5','mn',1, 'What is (2&frac12;)<sup>2</sup>?',
    ['4.25', '5', '4.5', '6.25'], 'd',
    'Write 2&frac12; as an improper fraction first.',
    'D &mdash; 2&frac12; = 5/2 and (5/2)<sup>2</sup> = 25/4 = 6.25. Option A is the common slip: 2<sup>2</sup> + (&frac12;)<sup>2</sup> = 4.25.')

# ---- H: rational and irrational
mcq('ra1','ra',1, 'Which of these numbers is <strong>irrational</strong>?',
    ['&radic;81', '0.151515&hellip;', '&radic;12', '&#8731;64'], 'c',
    'Which one is not a perfect root and not a fraction?',
    'C &mdash; &radic;12 is not a perfect square, so its decimal never ends or repeats. &radic;81 = 9, &#8731;64 = 4 and 0.1515&hellip; = 5/33 are all rational.')
mcq('ra2','ra',1, 'Which of these numbers is <strong>rational</strong>?',
    ['&radic;20', '&pi;', '&#8731;9', '&#8731;125'], 'd',
    'Work out each root. Which one is a whole number?',
    'D &mdash; &#8731;125 = 5, a whole number, so it is rational. &radic;20, &#8731;9 and &pi; are irrational.')
mcq('ra3','ra',2, 'Which list contains <strong>only</strong> rational numbers?',
    ['&radic;36, 0.3737&hellip;, 5/9, &#8731;8', '&radic;36, &pi;/4, 5/9, &#8731;8', '&radic;27, 0.3737&hellip;, 5/9, &#8731;8', '&radic;36, 0.3737&hellip;, &#8731;20, 5/9'], 'a',
    'Check each list for a number that is not a fraction or a perfect root.',
    'A &mdash; &radic;36 = 6, 0.3737&hellip; is recurring, 5/9 is a fraction and &#8731;8 = 2. B has &pi;/4, C has &radic;27 and D has &#8731;20, all irrational.')
mcq('ra4','ra',2, 'In the Venn diagram, circle A (integers) sits inside circle B (rational numbers). Where does &#8731;64 go?',
    ['Outside B', 'Inside B but outside A', 'On the edge of A', 'Inside A'], 'd',
    'Work out &#8731;64 first. Is the answer a whole number?',
    'D &mdash; &#8731;64 = 4, an integer, so it goes inside A (and so also inside B).', fig=VENN_FIG, figmd=VENN_MD)
mcq('ra5','ra',2, 'Using the same Venn diagram, where does 3 4/9 go?',
    ['Inside A', 'Outside B', 'Inside B but outside A', 'On the edge of B'], 'c',
    'It is a fraction, but is it a whole number?',
    'C &mdash; 3 4/9 = 31/9 is rational, but it is not a whole number. So it is inside B but outside A.', fig=VENN_FIG, figmd='Same Venn diagram as Q44.')

# ---------------------------------------------------------------- explorers

EXPLORERS = {
  'sb': '''<div class="explorer">
  <h3>&#128208; Do the surds really disappear?</h3>
  <p class="ex-note">Slide <em>n</em>. The product (&radic;n + 3)(&radic;n &minus; 3) is always <strong>n &minus; 9</strong>, even when &radic;n is not a whole number.</p>
  <input type="range" id="dsq-range" min="1" max="60" value="12" aria-label="Value of n">
  <svg class="ex-svg wide" id="dsq-svg" viewBox="0 0 440 90" role="img" aria-label="Bar showing n and the amount n minus 9"></svg>
  <div class="ex-readout" id="dsq-read"></div>
</div>''',
  'ra': '''<div class="explorer">
  <h3>&#960; Where does it live?</h3>
  <p class="ex-note">Pick a number. The dot moves to its region of the Venn diagram.</p>
  <div class="ex-btns" id="vn-btns">
    <button class="ex-btn on" data-v="18">18</button><button class="ex-btn" data-v="4.2">4.2</button>
    <button class="ex-btn" data-v="s49">&radic;49</button><button class="ex-btn" data-v="s8">&radic;8</button>
    <button class="ex-btn" data-v="pi">&pi;</button><button class="ex-btn" data-v="m">2 3/11</button>
    <button class="ex-btn" data-v="c30">&#8731;30</button>
  </div>
  <svg class="ex-svg wide" id="vn-svg" viewBox="0 0 320 170" role="img" aria-label="Venn diagram: integers inside rational numbers, irrational outside">
    <rect x="2" y="2" width="316" height="166" rx="10" fill="none" stroke="currentColor" opacity="0.25"/>
    <ellipse cx="140" cy="88" rx="118" ry="70" fill="rgba(79,142,247,0.12)" stroke="#4f8ef7" stroke-width="2"/>
    <ellipse cx="102" cy="92" rx="58" ry="40" fill="rgba(62,207,142,0.18)" stroke="#3ecf8e" stroke-width="2"/>
    <text x="102" y="120" text-anchor="middle" font-size="12" fill="currentColor">A: integers</text>
    <text x="212" y="40" text-anchor="middle" font-size="12" fill="currentColor">B: rational</text>
    <text x="288" y="150" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.7">irrational</text>
    <circle id="vn-dot" cx="102" cy="82" r="7" fill="#f5a623"/>
  </svg>
  <div class="ex-readout" id="vn-read"></div>
</div>''',
}

EXPLORER_JS = r'''
(function() {
  var r = document.getElementById('dsq-range');
  if (r) {
    var svg = document.getElementById('dsq-svg'), out = document.getElementById('dsq-read');
    var draw = function() {
      var n = +r.value, w = 380 / 60;
      svg.innerHTML = '<rect x="10" y="10" width="' + (n*w) + '" height="26" fill="#4f8ef7" opacity="0.5"/>' +
        '<text x="14" y="28" font-size="12" fill="currentColor">n = ' + n + '</text>' +
        '<rect x="10" y="48" width="' + (Math.max(n-9,0)*w) + '" height="26" fill="#3ecf8e" opacity="0.7"/>' +
        '<text x="14" y="66" font-size="12" fill="currentColor">n &#8722; 9 = ' + (n-9) + '</text>';
      var s = Math.sqrt(n), perfect = Number.isInteger(s);
      out.innerHTML = '&#8730;' + n + ' is ' + (perfect ? 'the whole number ' + s : 'irrational (about ' + s.toFixed(3) + ')') +
        '. The product is <strong>' + n + ' &#8722; 9 = ' + (n-9) + '</strong>, an integer either way.';
    };
    r.addEventListener('input', draw); draw();
  }
  var dot = document.getElementById('vn-dot');
  if (dot) {
    var INFO = {
      '18': [102, 82, 'integers (inside A)', '18 is a whole number, so it is an integer, and therefore rational too.'],
      '4.2': [170, 100, 'rational but not an integer (inside B, outside A)', '4.2 = 21/5 is a fraction, but it is not a whole number.'],
      's49': [88, 100, 'integers (inside A)', '&#8730;49 = 7, a whole number.'],
      's8': [270, 100, 'irrational (outside B)', '&#8730;8 is not a perfect square, so it can never be written as a fraction.'],
      'pi': [250, 60, 'irrational (outside B)', '&pi; never ends and never repeats: the impossible pizza.'],
      'm': [175, 70, 'rational but not an integer (inside B, outside A)', '2 3/11 = 25/11 is a fraction of integers.'],
      'c30': [270, 70, 'irrational (outside B)', '30 is not a perfect cube, so &#8731;30 is irrational.']
    };
    var btns = document.querySelectorAll('#vn-btns .ex-btn'), rd = document.getElementById('vn-read');
    var pick = function(b) {
      var d = INFO[b.getAttribute('data-v')];
      btns.forEach(function(x) { x.classList.remove('on'); }); b.classList.add('on');
      dot.setAttribute('cx', d[0]); dot.setAttribute('cy', d[1]);
      rd.innerHTML = '<strong>' + b.innerHTML + '</strong> is ' + d[2] + '. ' + d[3];
    };
    btns.forEach(function(b) { b.addEventListener('click', function() { pick(b); }); });
    pick(btns[0]);
  }
})();
'''

# ---------------------------------------------------------------- written (printable only)

WRITTEN = [
  (46, 3, 'Show that (3<em>n</em><sup>5</sup> &times; 8<em>n</em><sup>2</sup>) &divide; (2<em>n</em><sup>2</sup>)<sup>2</sup> simplifies to 6<em>n</em><sup>3</sup>. Show the top, the bottom, then combine.',
   'Top: 3 &times; 8 = 24 and n<sup>5</sup> &times; n<sup>2</sup> = n<sup>7</sup>, so 24n<sup>7</sup> [1]. Bottom: (2n<sup>2</sup>)<sup>2</sup> = 4n<sup>4</sup> [1]. Combine: 24n<sup>7</sup> &divide; 4n<sup>4</sup> = 6n<sup>3</sup> [1].'),
  (47, 3, 'Simplify &radic;98 + &radic;50 &minus; &radic;32. Give your answer as <em>a</em>&radic;2.',
   '&radic;98 = 7&radic;2 [1]; &radic;50 = 5&radic;2 and &radic;32 = 4&radic;2 [1]; 7 + 5 &minus; 4 = 8, so 8&radic;2 [1].'),
  (48, 4, 'If <em>n</em> = 12, find in simplest surd form: (a) &radic;<em>n</em> + 3 &nbsp; (b) &radic;<em>n</em> &minus; 3 &nbsp; (c) (&radic;<em>n</em> + 3)(&radic;<em>n</em> &minus; 3)',
   '(a) &radic;12 = 2&radic;3, so 2&radic;3 + 3 [1]. (b) 2&radic;3 &minus; 3 [1]. (c) Expand: 12 &minus; 3&radic;12 + 3&radic;12 &minus; 9 [1] = 3 [1].'),
  (49, 3, 'Tom says: &ldquo;If <em>n</em> is an integer, then (&radic;<em>n</em> + 3)(&radic;<em>n</em> &minus; 3) is also an integer.&rdquo; Investigate whether Tom is correct. Explain your reasoning, and test it with one value of <em>n</em> that is not a square number.',
   'Expand: (&radic;n + 3)(&radic;n &minus; 3) = n &minus; 3&radic;n + 3&radic;n &minus; 9 [1]. The middle terms cancel, leaving n &minus; 9 [1]. An integer minus 9 is an integer, so Tom is correct. Test, e.g. n = 7: 7 &minus; 9 = &minus;2 [1].'),
  (50, 3, 'Draw two circles, A (integers) inside B (rational numbers). Place these numbers in the correct region: 18, 4.2, 2 3/11, &radic;49, &#8731;30. Say which one is irrational and why.',
   'A circle A inside circle B [1]. 18 and &radic;49 (= 7) inside A; 4.2 and 2 3/11 inside B but outside A [1]. &#8731;30 goes outside B because 30 is not a perfect cube, so its decimal never ends or repeats [1].'),
  (51, 3, 'A taxi charges $8 plus $6 for each kilometre. (a) Write an expression for the cost of a journey of <em>k</em> km. (b) A journey costs $62. How many kilometres is it? Show your working.',
   '(a) 8 + 6k [1]. (b) 8 + 6k = 62 [1], 6k = 54, so k = 9 km [1].'),
  (52, 3, 'A student says that when <em>x</em> = 5, <em>x</em><sup>&minus;1</sup> = 5. (a) Explain the mistake. (b) Work out <em>x</em><sup>0</sup> &minus; <em>x</em><sup>&minus;1</sup> + <em>x</em><sup>&minus;2</sup> when <em>x</em> = 5.',
   '(a) x<sup>&minus;1</sup> means 1/x, so 5<sup>&minus;1</sup> = 1/5 = 0.2, not 5 [1]. (b) 1 &minus; 0.2 + 0.04 [1] = 0.84 [1].'),
]
