"""Spec: Secondary 2 · Semester 1 maths — Gaps drill: the algebra slips found the day before the assessment.

Build with:  python3 scripts/build_review_sheet.py scripts/review_specs/s2_sem1_maths_gaps.py

Every question is a typed number (no multiple choice) because the point is to write
the working on paper first. Questions that ask for an expression ask for its value at
a chosen n, so the sheet can still mark it. The open "show your working" questions
are printable-only (WRITTEN).
"""

META = dict(
    out='s2/sem1/mocks/sem1-maths-gaps',
    title='Maths Gaps Drill &middot; Practice',
    badge='Maths &middot; Gaps Drill',
    eyebrow='Secondary 2 &middot; Mathematics &middot; Semester 1 topic drill',
    h1='Seven algebra slips<br><em>to fix tonight</em>',
    md_title='Secondary 2 · Maths — Gaps Drill',
    intro=('Seven spots where marks are easy to lose: writing expressions in <em>n</em>, simplifying surds, '
           'surds in brackets, zero and negative powers, indices in fractions, brackets and signs, and mixed '
           'numbers with powers. <strong>Write every answer on paper first</strong>, then type only the final '
           'number. Where a question asks for an expression, write the expression down, then type its value for '
           'the number given. Use <strong>Cover the notes</strong> to test yourself before you read the key facts.'),
    md_intro=('A practice sheet on seven topics where marks are easy to lose. Write every answer in your '
              'notebook. Q1–Q34 match the interactive sheet (each has one number as its answer); Q35–Q41 are '
              'written questions for you to show full working. No calculator is needed.'),
    time_chip='About 35 minutes &middot; no calculator',
    storage_key='sem1-maths-gaps',
    back='../../../index.html',
    answers_note='Answers for Q1–Q34 (auto-marked on the interactive sheet) and a marking guide for the written questions Q35–Q41. Keep this separate from the question sheet.',
    extra_links=[('./sem1-maths-paper1-non-calculator.html', 'Paper 1'),
                 ('../../reference/maths-formula-sheets/index.html', 'Formula sheets')],
)

EXPLORER_CSS = '''
.ftable { border-collapse: collapse; margin: 6px 0 14px; font-size: 0.9rem; }
.ftable th, .ftable td { border: 1px solid var(--border); padding: 6px 14px; text-align: center; }
.ftable th { background: var(--surface2); font-family: var(--font-mono); font-size: 0.76rem; color: var(--text-muted); }
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
         ('&ldquo;Squares&rdquo; is a power', '<strong>Squares</strong> means &ldquo;to the power 2&rdquo; and <strong>cubes</strong> means &ldquo;to the power 3&rdquo;. A <strong>square root</strong> or <strong>cube root</strong> uses the root sign. They are different words and different operations.'),
         ('Rule from a table', 'The value at <em>0</em> is the fixed charge. The jump from one column to the next is the amount for each extra unit. So <span class="f">cost = fixed + jump &times; units</span>.'),
         ('Check with a number', 'To test an expression, put in a small number for <em>n</em>, follow the words step by step, and see if both routes give the same answer.'),
       ]),
  dict(key='su', icon='&#8730;', color='var(--accent-sci)', rgba='62,207,142',
       title='Simplifying Surds', label='Simplifying Surds',
       src='Rational &amp; Irrational Numbers', link=W2, link_label='Rational &amp; irrational sheet',
       facts=[
         ('The splitting rule', '<span class="f">&radic;(a &times; b) = &radic;a &times; &radic;b</span>. It works because squaring both sides gives a &times; b.'),
         ('Use the largest square factor', 'Look for the biggest of <em>4, 9, 16, 25, 36, 49, 64, 81, 100</em> that divides the number. The root of that square comes out as a whole number in front.'),
         ('Check by squaring', 'Square the number in front, then multiply by the number under the root. You should get the number you started with. Example: 2&radic;5 &rarr; 2&sup2; &times; 5 = 20.'),
         ('Adding surds', 'Surds add like terms only when the part under the root matches: 3&radic;2 + 4&radic;2 = 7&radic;2. Simplify each one first to see if they match.'),
         ('When it stays', 'If no square number (except 1) divides it, the root is already in its simplest form.'),
       ]),
  dict(key='sb', icon='&#128208;', color='var(--accent-warn)', rgba='245,166,35',
       title='Surds in Brackets', label='Surds in Brackets',
       src='Rational &amp; Irrational Numbers', link=W2, link_label='Rational &amp; irrational sheet',
       facts=[
         ('Expand as usual', 'Multiply every term in the first bracket by every term in the second. Remember <span class="f">&radic;n &times; &radic;n = n</span>.'),
         ('Difference of two squares', '<span class="f">(a + b)(a &minus; b) = a&sup2; &minus; b&sup2;</span>. The two middle terms are opposites, so they cancel.'),
         ('Why it matters', 'When the middle terms cancel, the surds disappear. The answer can be a whole number even though the brackets contain a surd.'),
         ('No calculator', 'Leave answers as surds or whole numbers. Never turn &radic;n into a rounded decimal.'),
       ]),
  dict(key='pw', icon='&#10024;', color='var(--accent-math)', rgba='79,142,247',
       title='Zero, Negative &amp; Powers of 10', label='Zero & Negative Powers',
       src='Indices &amp; Standard Form', link=W3, link_label='Indices &amp; standard form sheet',
       facts=[
         ('Zero power', 'Any number (except 0) to the power 0 is <strong>1</strong>.'),
         ('Negative power', '<span class="f">x<sup>&minus;n</sup> = 1 &divide; x<sup>n</sup></span>. It is a <em>fraction</em>, not a negative number, and <strong>x<sup>&minus;1</sup> is not x</strong>.'),
         ('Multiplying by 10<sup>n</sup>', 'Multiplying by 10<sup>3</sup> makes the number bigger (digits move three places up). Multiplying by 10<sup>&minus;3</sup> is the same as <em>dividing</em> by 10<sup>3</sup>.'),
         ('Dividing by 10<sup>&minus;n</sup>', 'Dividing by 10<sup>&minus;n</sup> is the same as <em>multiplying</em> by 10<sup>n</sup>. Two minuses make it bigger, not smaller.'),
         ('Comparing', 'The more negative the power, the <em>smaller</em> the number: 10<sup>&minus;1</sup> = 0.1, 10<sup>&minus;2</sup> = 0.01, and so on.'),
       ]),
  dict(key='ix', icon='&#128208;', color='var(--accent-sci)', rgba='62,207,142',
       title='Indices &amp; Fractions', label='Indices & Fractions',
       src='Indices &amp; Standard Form', link=W3, link_label='Indices &amp; standard form sheet',
       facts=[
         ('Three laws', 'Multiply: <em>add</em> the powers. Divide: <em>subtract</em> the powers. Power of a power: <em>multiply</em> the powers.'),
         ('Numbers and letters separately', 'Work out the numbers first, then deal with each letter by itself.'),
         ('Cube or square the whole bracket', 'In (3m<sup>2</sup>)<sup>4</sup> the power outside applies to the <em>3</em> as well as to the m<sup>2</sup>.'),
         ('A negative power in a fraction', 'An answer such as y<sup>&minus;5</sup> is written as <span class="f">1/y<sup>5</sup></span> when the question wants a fraction.'),
         ('&ldquo;Show that&rdquo; layout', 'Top first, bottom second, then combine. Write each step on its own line.'),
       ]),
  dict(key='br', icon='&#9999;&#65039;', color='var(--accent-warn)', rgba='245,166,35',
       title='Brackets, Signs &amp; Equations', label='Brackets & Signs',
       src='Expressions &amp; Simultaneous Equations', link=W4, link_label='Simultaneous equations sheet',
       facts=[
         ('Two brackets', 'Multiply every term by every term, then collect the like terms in the middle. A grid or arrows help you not miss one.'),
         ('Signs', 'A negative times a negative is positive. A minus in front of a bracket changes <em>every</em> sign inside it.'),
         ('Equivalent expressions', 'Expand each one fully. Two expressions are equivalent only if they come out exactly the same.'),
         ('Subtracting equations', 'Put the second equation in brackets first. The minus then applies to <strong>every</strong> term, including the right-hand side.'),
         ('Then substitute back', 'After finding one letter, put it into either original equation to find the other, then check it in the <em>other</em> equation.'),
       ]),
  dict(key='mn', icon='&#189;', color='var(--accent-math)', rgba='79,142,247',
       title='Mixed Numbers &amp; Powers', label='Mixed Numbers',
       src='Fractions', link=W5, link_label='Fractions sheet',
       facts=[
         ('Convert first', 'Change mixed numbers to <em>improper fractions</em> before you square, multiply or divide. Never square the whole part and the fraction part separately.'),
         ('Dividing', 'To divide by a fraction, flip the second fraction and multiply.'),
         ('Order of working', 'Powers first, then multiplication and division, then adding and subtracting.'),
       ]),
]

# ---------------------------------------------------------------- questions

Q = []
def num(id, sec, marks, q, ans, hint, reveal, unit='', tol=0, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='num', q=q, ans=ans, tol=tol, unit=unit, hint=hint, reveal=reveal, fig=fig, figmd=figmd))

WP = '<em>Write it on paper first.</em> '

# ---- A: expressions in n
num('e1','ex',2, WP + 'Mia thinks of a number, <em>n</em>. She <strong>adds 6</strong>, then <strong>multiplies the result by 5</strong>. Write her expression. What is its value when <em>n</em> = 4?',
    50, 'Do the steps in order with n = 4. What happens to the 6?', 'Expression: 5(<em>n</em> + 6). When n = 4: 5 &times; 10 = 50.')
num('e2','ex',2, WP + 'Leo thinks of <em>n</em>. He <strong>multiplies it by 2</strong>, then <strong>cubes</strong> the result, then <strong>adds 7</strong>. Write his expression. What is its value when <em>n</em> = 2?',
    71, 'Cubes means power 3, not a cube root. Which part gets cubed?', 'Expression: (2<em>n</em>)<sup>3</sup> + 7. When n = 2: 4<sup>3</sup> + 7 = 64 + 7 = 71.')
num('e3','ex',2, WP + 'Ana thinks of <em>n</em>. She <strong>divides it by 2</strong>, <strong>cubes</strong> the result, then <strong>subtracts 1</strong>. Write her expression. What is its value when <em>n</em> = 6?',
    26, 'Divide first, then cube the whole result.', 'Expression: (<em>n</em>/2)<sup>3</sup> &minus; 1. When n = 6: 3<sup>3</sup> &minus; 1 = 27 &minus; 1 = 26.')
num('e4','ex',2, WP + 'A shop hires bikes for a fixed fee plus a daily amount. The table shows the cost. How much does it cost to hire a bike for <strong>10 days</strong>?',
    59, 'Day 0 is the fixed fee. How much does each extra day add?', 'Fixed fee $9, plus $5 a day. 9 + 5 &times; 10 = 59.', unit='$',
    fig='<table class="ftable"><tr><th>Days</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><th>Cost ($)</th><td>9</td><td>14</td><td>19</td><td>24</td><td>29</td></tr></table>',
    figmd='Table. Days 0, 1, 2, 3, 4. Cost in $: 9, 14, 19, 24, 29.')
num('e5','ex',1, WP + 'Using the same table, write an expression for the cost of hiring a bike for <em>d</em> days. What is its value when <em>d</em> = 20?',
    109, 'Fixed fee + daily amount &times; d.', 'Expression: 9 + 5<em>d</em>. When d = 20: 9 + 100 = 109.', unit='$',
    fig='<table class="ftable"><tr><th>Days</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><th>Cost ($)</th><td>9</td><td>14</td><td>19</td><td>24</td><td>29</td></tr></table>',
    figmd='Same table as Q4.')

# ---- B: simplifying surds
num('u1','su',1, WP + 'Simplify &radic;90 and write it as <em>a</em>&radic;10. Find <em>a</em>.',
    3, 'Which square number divides 90?', '&radic;90 = &radic;(9 &times; 10) = 3&radic;10, so a = 3. Check: 3<sup>2</sup> &times; 10 = 90.')
num('u2','su',1, WP + 'Simplify &radic;72 and write it as <em>a</em>&radic;2. Find <em>a</em>.',
    6, 'Use the <em>largest</em> square factor of 72. It is bigger than 9.', '&radic;72 = &radic;(36 &times; 2) = 6&radic;2, so a = 6. Check: 6<sup>2</sup> &times; 2 = 72.')
num('u3','su',1, WP + 'A student writes &radic;18 = 9&radic;2. Write the correct simplified form as <em>a</em>&radic;2. What should <em>a</em> be?',
    3, 'The 9 is a square number, so its root should come out, not 9 itself.', '&radic;18 = &radic;(9 &times; 2) = &radic;9 &times; &radic;2 = 3&radic;2, so a = 3. Check: 3<sup>2</sup> &times; 2 = 18, but 9<sup>2</sup> &times; 2 = 162.')
num('u4','su',2, WP + 'Work out (4&radic;3)<sup>2</sup>.',
    48, 'Square the 4 and square the &radic;3 separately, then multiply.', '(4&radic;3)<sup>2</sup> = 4<sup>2</sup> &times; (&radic;3)<sup>2</sup> = 16 &times; 3 = 48.')
num('u5','su',2, WP + 'Simplify &radic;12 + &radic;27 and write it as <em>a</em>&radic;3. Find <em>a</em>.',
    5, 'Simplify each root first. Then add the numbers in front.', '&radic;12 = 2&radic;3 and &radic;27 = 3&radic;3. Sum: 5&radic;3, so a = 5.')
num('u6','su',1, WP + 'Simplify &radic;175 and write it as <em>a</em>&radic;7. Find <em>a</em>.',
    5, 'Is 25 a factor of 175?', '&radic;175 = &radic;(25 &times; 7) = 5&radic;7, so a = 5.')

# ---- C: surds in brackets
num('b1','sb',1, WP + 'If <em>n</em> = 8, then &radic;<em>n</em> + 5 in simplest form is <em>a</em>&radic;2 + 5. Find <em>a</em>.',
    2, 'Simplify &radic;8 first.', '&radic;8 = &radic;(4 &times; 2) = 2&radic;2, so &radic;8 + 5 = 2&radic;2 + 5 and a = 2. You cannot add 2&radic;2 and 5.')
num('b2','sb',2, WP + 'Expand and simplify (&radic;7 + 2)(&radic;7 &minus; 2).',
    3, 'Four terms. What happens to the two middle ones?', '7 &minus; 2&radic;7 + 2&radic;7 &minus; 4 = 7 &minus; 4 = 3.')
num('b3','sb',1, WP + 'Expand (&radic;<em>n</em> + 4)(&radic;<em>n</em> &minus; 4). What is its value when <em>n</em> = 40?',
    24, 'Difference of two squares: (a + b)(a &minus; b) = a<sup>2</sup> &minus; b<sup>2</sup>.', '(&radic;n + 4)(&radic;n &minus; 4) = n &minus; 16. When n = 40: 40 &minus; 16 = 24.')
num('b4','sb',2, WP + 'Expand (&radic;<em>n</em> + 9)(&radic;<em>n</em> &minus; 9). It simplifies to <em>n</em> &minus; <em>k</em>. Find <em>k</em>.',
    81, 'The middle terms cancel. What is 9 &times; 9?', '&radic;n &times; &radic;n = n, the middle terms cancel, and 9 &times; 9 = 81. So the answer is n &minus; 81, and k = 81.')

# ---- D: zero, negative and powers of 10
num('p1','pw',1, WP + 'Write 4<sup>&minus;2</sup> as a decimal.',
    0.0625, 'A negative power means a fraction: 1 divided by what?', '4<sup>&minus;2</sup> = 1/4<sup>2</sup> = 1/16 = 0.0625.', tol=1e-6)
num('p2','pw',2, WP + 'y = <em>x</em><sup>0</sup> &minus; <em>x</em><sup>&minus;1</sup> + <em>x</em><sup>&minus;2</sup>. Find <em>y</em> when <em>x</em> = 10. Give a decimal.',
    0.91, 'x<sup>0</sup> = 1. x<sup>&minus;1</sup> = 1/x, which is not x. And x<sup>&minus;2</sup> = 1/x<sup>2</sup>.', 'y = 1 &minus; 0.1 + 0.01 = 0.91.', tol=1e-6)
num('p3','pw',2, WP + 'Work out 350 &divide; 10<sup>&minus;2</sup>.',
    35000, 'Dividing by 10<sup>&minus;2</sup> is the same as multiplying by what?', '350 &divide; 10<sup>&minus;2</sup> = 350 &times; 10<sup>2</sup> = 35 000.')
num('p4','pw',1, WP + 'How many times bigger is 10<sup>&minus;3</sup> than 10<sup>&minus;5</sup>? Write both as decimals first.',
    100, '10<sup>&minus;3</sup> = 0.001 and 10<sup>&minus;5</sup> = 0.00001.', '0.001 &divide; 0.00001 = 100. So 10<sup>&minus;3</sup> is the bigger one, by a factor of 100.')
num('p5','pw',2, WP + '0.07 &divide; 10<sup><em>k</em></sup> = 700. Find <em>k</em>.',
    -4, 'The answer is much bigger than 0.07, so dividing must make it bigger. What kind of power does that?', '0.07 &times; 10<sup>4</sup> = 700, so dividing by 10<sup>&minus;4</sup> gives 700 and k = &minus;4.')
num('p6','pw',1, WP + '6000 &divide; 10<sup><em>k</em></sup> = 0.6. Find <em>k</em>.',
    4, 'How many places does the decimal point move?', '6000 &divide; 10 000 = 0.6, so 10<sup>4</sup> and k = 4.')

# ---- E: indices and fractions
num('i1','ix',1, WP + '15<em>a</em><sup>6</sup> &divide; 3<em>a</em><sup>2</sup> = 5<em>a</em><sup><em>k</em></sup>. Find <em>k</em>.',
    4, 'Subtract the powers: 6 &minus; 2.', '15 &divide; 3 = 5 and a<sup>6</sup> &divide; a<sup>2</sup> = a<sup>4</sup>, so k = 4.')
num('i2','ix',2, WP + '10<em>a</em><sup>2</sup> &divide; 15<em>a</em><sup>9</sup> simplifies to 2/(3<em>a</em><sup><em>k</em></sup>). Find <em>k</em>.',
    7, 'The top power is smaller than the bottom power, so some a is left on the bottom.', '10/15 = 2/3 and a<sup>2&minus;9</sup> = a<sup>&minus;7</sup> = 1/a<sup>7</sup>. So the answer is 2/(3a<sup>7</sup>), and k = 7.')
num('i3','ix',2, WP + '(4<em>n</em><sup>3</sup> &times; 6<em>n</em><sup>5</sup>) &divide; (2<em>n</em><sup>2</sup>)<sup>3</sup> simplifies to <em>an</em><sup><em>b</em></sup>. Find <em>a</em> + <em>b</em>.',
    5, 'Top first, then bottom, then combine. Cube the 2 as well.', 'Top: 24n<sup>8</sup>. Bottom: (2n<sup>2</sup>)<sup>3</sup> = 8n<sup>6</sup>. Combine: 3n<sup>2</sup>. So a = 3, b = 2 and a + b = 5.')
num('i4','ix',1, WP + '(2<em>n</em><sup>2</sup>)<sup>3</sup> = <em>an</em><sup><em>b</em></sup>. Find <em>a</em> + <em>b</em>.',
    14, 'The power 3 applies to the 2 as well.', '(2n<sup>2</sup>)<sup>3</sup> = 2<sup>3</sup> &times; n<sup>6</sup> = 8n<sup>6</sup>, so a + b = 8 + 6 = 14.')

# ---- F: brackets, signs and equations
num('r1','br',1, WP + '(<em>x</em> + 6)(<em>x</em> + 2) = <em>x</em><sup>2</sup> + <em>bx</em> + 12. Find <em>b</em>.',
    8, 'Add the two middle terms.', 'x<sup>2</sup> + 2x + 6x + 12 = x<sup>2</sup> + 8x + 12, so b = 8.')
num('r2','br',2, WP + '(<em>y</em> + 8)(<em>y</em> &minus; 5) = <em>y</em><sup>2</sup> + <em>by</em> &minus; 40. Find <em>b</em>.',
    3, 'The middle terms are &minus;5y and +8y.', 'y<sup>2</sup> &minus; 5y + 8y &minus; 40 = y<sup>2</sup> + 3y &minus; 40, so b = 3.')
num('r3','br',2, WP + '(2<em>y</em> + 3)(3<em>y</em> &minus; 4) = 6<em>y</em><sup>2</sup> + <em>by</em> &minus; 12. Find <em>b</em>. (It can be negative.)',
    1, 'Middle terms: 2y &times; &minus;4 and 3 &times; 3y.', '6y<sup>2</sup> &minus; 8y + 9y &minus; 12 = 6y<sup>2</sup> + y &minus; 12, so b = 1.')
num('r4','br',1, WP + '3(4<em>y</em> + 2) = 6(2<em>y</em> + <em>k</em>). Find <em>k</em>.',
    1, 'Expand both sides.', '3(4y + 2) = 12y + 6 and 6(2y + k) = 12y + 6k, so 6k = 6 and k = 1.')
num('r5','br',2, WP + '4<em>x</em> + 5<em>y</em> = 26 and 4<em>x</em> &minus; 2<em>y</em> = 12. <strong>Subtract the second equation from the first.</strong> You get <em>ay</em> = <em>c</em>. Find <em>a</em> + <em>c</em>.',
    21, 'Put the second equation in brackets. 5y &minus; (&minus;2y) = ?', '(4x + 5y) &minus; (4x &minus; 2y) = 7y and 26 &minus; 12 = 14. So 7y = 14, a = 7, c = 14 and a + c = 21.')
num('r6','br',2, WP + 'Now solve the same pair: 4<em>x</em> + 5<em>y</em> = 26 and 4<em>x</em> &minus; 2<em>y</em> = 12. Find <em>x</em> + <em>y</em>.',
    6, 'Find y, then put it back into one equation to find x.', '7y = 14 gives y = 2. Then 4x + 10 = 26, so x = 4. Check in the second: 16 &minus; 4 = 12. x + y = 6.')

# ---- G: mixed numbers and powers
num('m1','mn',2, WP + 'Work out (1&frac12;)<sup>2</sup> + 2&frac23; &divide; 1&frac13;. Give a decimal.',
    4.25, 'Convert to improper fractions. Power first, then the division, then add.', '(3/2)<sup>2</sup> = 9/4 = 2.25. 8/3 &divide; 4/3 = 2. Total: 4.25.', tol=1e-6)
num('m2','mn',1, WP + 'Work out (2&frac12;)<sup>2</sup> as a decimal.',
    6.25, 'Write 2&frac12; as an improper fraction first.', '2&frac12; = 5/2 and (5/2)<sup>2</sup> = 25/4 = 6.25.', tol=1e-6)
num('m3','mn',2, WP + 'Work out (2&frac12;)<sup>2</sup> &minus; 1&frac34; &times; 2/7. Give a decimal.',
    5.75, 'Multiplication before subtraction. 1&frac34; = 7/4.', '(5/2)<sup>2</sup> = 6.25. 7/4 &times; 2/7 = 0.5. So 6.25 &minus; 0.5 = 5.75.', tol=1e-6)

# ---------------------------------------------------------------- written (printable only)

WRITTEN = [
  (35, 3, 'Show that (3<em>n</em><sup>2</sup> &times; 8<em>n</em><sup>5</sup>) &divide; (2<em>n</em><sup>3</sup>)<sup>2</sup> simplifies to 6<em>n</em>. Show the top, the bottom, then combine.',
   'Top: 3 &times; 8 = 24 and n<sup>2</sup> &times; n<sup>5</sup> = n<sup>7</sup>, so 24n<sup>7</sup> [1]. Bottom: (2n<sup>3</sup>)<sup>2</sup> = 4n<sup>6</sup> [1]. Combine: 24n<sup>7</sup> &divide; 4n<sup>6</sup> = 6n [1].'),
  (36, 3, 'Simplify &radic;98 + &radic;50 &minus; &radic;32. Give your answer as <em>a</em>&radic;2.',
   '&radic;98 = 7&radic;2 [1]; &radic;50 = 5&radic;2 and &radic;32 = 4&radic;2 [1]; 7 + 5 &minus; 4 = 8, so 8&radic;2 [1].'),
  (37, 4, 'Expand and simplify. (a) (<em>x</em> + 7)(<em>x</em> &minus; 2) &nbsp; (b) (3<em>y</em> &minus; 2)(2<em>y</em> + 5)',
   '(a) x<sup>2</sup> &minus; 2x + 7x &minus; 14 [1] = x<sup>2</sup> + 5x &minus; 14 [1]. (b) 6y<sup>2</sup> + 15y &minus; 4y &minus; 10 [1] = 6y<sup>2</sup> + 11y &minus; 10 [1].'),
  (38, 3, 'A taxi charges $8 plus $6 for each kilometre. (a) Write an expression for the cost of a journey of <em>k</em> km. (b) A journey costs $62. How many kilometres is it? Show your working.',
   '(a) 8 + 6k [1]. (b) 8 + 6k = 62 [1], 6k = 54, so k = 9 km [1].'),
  (39, 3, 'Solve the simultaneous equations 5<em>x</em> + 3<em>y</em> = 29 and 2<em>x</em> + 3<em>y</em> = 17. Show how you eliminate a letter and check your answer.',
   'Subtract the second from the first: 3x = 12 [1], so x = 4 [1]. Then 8 + 3y = 17, y = 3, and the check 5(4) + 3(3) = 29 works [1].'),
  (40, 3, 'A student says that when <em>x</em> = 5, <em>x</em><sup>&minus;1</sup> = 5. (a) Explain the mistake. (b) Work out <em>x</em><sup>0</sup> &minus; <em>x</em><sup>&minus;1</sup> + <em>x</em><sup>&minus;2</sup> when <em>x</em> = 5.',
   '(a) x<sup>&minus;1</sup> means 1/x, so 5<sup>&minus;1</sup> = 1/5 = 0.2, not 5 [1]. (b) 1 &minus; 0.2 + 0.04 [1] = 0.84 [1].'),
  (41, 3, 'Write an expression for the number you get when you <strong>subtract 5</strong> from <em>n</em>, <strong>divide by 4</strong>, then <strong>square</strong> the result. Explain why brackets are needed, and why a square root sign would be wrong. Then find its value when <em>n</em> = 13.',
   '((n &minus; 5)/4)<sup>2</sup> [1]. Brackets are needed because the dividing and squaring apply to the whole (n &minus; 5), and squaring means power 2, not a square root [1]. When n = 13: (8/4)<sup>2</sup> = 2<sup>2</sup> = 4 [1].'),
]
