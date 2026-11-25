"""Spec: Secondary 2 · Semester 1 maths — Paper 2B (calculator).

Build with:  python3 scripts/build_review_sheet.py scripts/review_specs/s2_sem1_maths_paper2b_calculator.py

A second calculator paper in the Paper 2 layout (number, percentages & bounds · algebra &
equations · Pythagoras & polygons · circles & compound shapes) with all-new questions.
Mixed MCQ and typed numbers; open "show your working" questions are printable-only.
"""

META = dict(
    out='s2/sem1/mocks/sem1-maths-paper2b-calculator',
    title='Maths Paper 2B &middot; Calculator',
    badge='Maths &middot; Paper 2B',
    eyebrow='Secondary 2 &middot; Mathematics &middot; Semester 1 assessment practice',
    h1='Paper 2B<br><em>Calculator</em>',
    md_title='Secondary 2 · Maths — Semester 1 Mock, Paper 2B (Calculator)',
    intro=('A second calculator paper with all-new questions, mixing every Semester 1 unit: number, percentages and '
           'bounds &middot; algebra and equations &middot; polygons and Pythagoras &middot; circles and compound '
           'shapes. <strong>A calculator is allowed.</strong> Work each question out on paper first, then type the '
           'number or pick the option. Use <strong>Cover the notes</strong> to test yourself before reading the key facts.'),
    md_intro=('A second calculator paper in the Paper 2 layout, with new questions. Q1–Q26 (50 marks) match the '
              'interactive sheet; allow 1 hour. Q27–Q31 are extra written questions marked by the teacher. '
              'A calculator is allowed. Diagrams are described in words and are not drawn accurately.'),
    time_chip='About 1 hour &middot; calculator allowed',
    storage_key='sem1-maths-paper2b-calculator',
    back='../../../index.html',
    answers_note='Answers for Q1–Q26 (auto-marked on the interactive sheet) and a marking guide for the written questions Q27–Q31. Keep this separate from the question sheet.',
    extra_links=[('./sem1-maths-paper2-calculator.html', 'Paper 2'),
                 ('./sem1-maths-test2-shapes-angles-algebra.html', 'Test 2 practice'),
                 ('../../reference/maths-formula-sheets/index.html', 'Formula sheets')],
)

EXPLORER_CSS = ''

WK = '../t2/w5/term2-week5-maths-unit-test2-angles-shapes-measurements.html'
W3 = '../t1/w2/term1-week2-maths-indices-standard-form.html'
W4 = '../t1/w8/term1-week8-maths-unit4-simultaneous-equations.html'

SECTIONS = [
  dict(key='nu', icon='&#37;', color='var(--accent-math)', rgba='79,142,247',
       title='Number, Percentages &amp; Bounds', label='Number & Percentages',
       src='Number &amp; Decimals', link=W3, link_label='Indices &amp; standard form sheet',
       facts=[
         ('Percentage multipliers', 'Increase by r%: multiply by 1 + r/100. Decrease by r%: multiply by 1 &minus; r/100. For two changes in a row, multiply the multipliers. Do not add the percentages.'),
         ('Repeated change', 'Value after n years = start &times; multiplier<sup>n</sup>. Round only at the very end.'),
         ('Going backwards', 'To find the original, <em>divide</em> by the multiplier. Do not add the percentage back on.'),
         ('Standard form', 'Multiply the numbers and add the powers of 10. Then change the answer back to an ordinary number if asked.'),
         ('Significant figures', 'Start counting at the first non-zero digit. Zeros before it, after the decimal point, are not significant.'),
         ('Bounds', 'A value given to the nearest 50 can be up to 25 below or above. For a safe limit use the <em>smallest</em> possible limit and the <em>largest</em> possible load.'),
       ]),
  dict(key='al', icon='&#9999;&#65039;', color='var(--accent-sci)', rgba='62,207,142',
       title='Algebra &amp; Equations', label='Algebra & Equations',
       src='Expressions &amp; Simultaneous Equations', link=W4, link_label='Simultaneous equations sheet',
       facts=[
         ('Substitute carefully', 'Write the formula, replace each letter by its number in brackets, then use the calculator. For v&sup2; you may need a square root last.'),
         ('Indices laws', 'Divide the numbers, then subtract the powers of each letter.'),
         ('Changing the subject', 'Undo the operations in the reverse order, doing the same to both sides.'),
         ('Inequalities', 'Solve like an equation, then decide whether the answer must be a whole number. Round in the direction that keeps the condition true.'),
         ('Two equations', 'Where two lines cross, both equations are true at the same time. Eliminate a letter, then put it back to find the other.'),
         ('Words to equations', 'Give each unknown a letter. Write one equation for each sentence of information.'),
       ]),
  dict(key='py', icon='&#9651;', color='var(--accent-warn)', rgba='245,166,35',
       title='Polygons &amp; Pythagoras', label='Polygons & Pythagoras',
       src='Angles, Shapes &amp; Measurements', link=WK, link_label='Unit test 2 sheet',
       facts=[
         ('Polygon angles', 'Interior angle + exterior angle = 180&deg; at each corner. The exterior angles of any polygon add to 360&deg;.'),
         ('Pythagoras', 'a&sup2; + b&sup2; = c&sup2;, where c is the longest side, opposite the right angle.'),
         ('Hypotenuse or shorter side?', 'Longest side: add the squares, then square root. A shorter side: subtract, then square root.'),
         ('Triples', 'A triangle is right-angled only if the two smaller squares add to exactly the largest square.'),
         ('Isosceles triangle', 'The line from the top, straight down to the base, makes two equal right-angled triangles and halves the base.'),
       ]),
  dict(key='ci', icon='&#9711;', color='var(--accent-math)', rgba='79,142,247',
       title='Circles &amp; Compound Shapes', label='Circles & Compound Shapes',
       src='Angles, Shapes &amp; Measurements', link=WK, link_label='Unit test 2 sheet',
       facts=[
         ('Use the &pi; button', 'Keep all the digits on screen until the final answer, then round as asked.'),
         ('Two formulas', 'Circumference = &pi; &times; diameter = 2&pi;r. Area = &pi;r&sup2;. Check whether you are given the radius or the diameter.'),
         ('Working backwards', 'To find the radius from the circumference, divide by 2&pi;. From the area, divide by &pi; and then square root.'),
         ('Perimeter of a part-circle', 'Add the curved edge and every straight edge on the outside. A straight edge where two parts join is inside the shape.'),
         ('Compound areas', 'Add the pieces, or take one piece away from a bigger shape. A ring is the large circle minus the small one.'),
       ]),
]

# ---------------------------------------------------------------- figures

INK, BLUE, AMB = '#e8eaf0', '#4f8ef7', '#f5a623'
FILL = 'rgba(79,142,247,0.16)'

def svg(vb, inner, label, mw=340):
    return f'<svg class="q-fig" viewBox="{vb}" role="img" aria-label="{label}" style="max-width:{mw}px">{inner}</svg>'

def t(x, y, s, anchor='middle', col=INK, bold=False):
    w = ' font-weight="700"' if bold else ''
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{col}" font-size="14" font-family="Literata, Georgia, serif"{w}>{s}</text>'

def shape(d): return f'<path d="{d}" fill="{FILL}" stroke="{BLUE}" stroke-width="2"/>'
def poly(p): return f'<polygon points="{p}" fill="{FILL}" stroke="{BLUE}" stroke-width="2"/>'
def ln(x1, y1, x2, y2, col=INK, w=1.5): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"/>'
def dash(x1, y1, x2, y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="1.5" stroke-dasharray="5 4"/>'

# y = 3x - 2 and y = x + 6, x 0..6, y -2..16
def gx(x): return 40 + x * 50
def gy(y): return 200 - (y + 2) * 10.5
FIG_GRAPH = svg('0 0 380 225',
    ln(gx(0), gy(0), 350, gy(0), '#7a84a0') + ln(gx(0), 10, gx(0), 205, '#7a84a0') +
    ln(gx(0), gy(-2), gx(6), gy(16), BLUE, 2) + ln(gx(0), gy(6), gx(6), gy(12), AMB, 2) +
    f'<circle cx="{gx(4)}" cy="{gy(10)}" r="9" fill="none" stroke="{INK}" stroke-width="2"/>' +
    t(gx(6) - 10, gy(16) + 4, 'y = 3x &minus; 2', 'end', BLUE, True) + t(gx(6) + 2, gy(12) - 8, 'y = x + 6', 'end', AMB, True) +
    t(gx(6), gy(0) - 6, 'x', 'middle', '#7a84a0') + t(gx(0) - 10, 18, 'y', 'end', '#7a84a0'),
    'Graph of y = 3x minus 2 and y = x plus 6. They cross at the circled point.', 380)
FIG_GRAPH_MD = 'A graph of y = 3x − 2 and y = x + 6 for x from 0 to 6. The lines cross at a circled point. Not drawn accurately.'

def right_tri(base, upright, hyp):
    return svg('0 0 320 200',
        poly('40,170 250,170 40,45') + f'<polyline points="40,150 60,150 60,170" fill="none" stroke="{INK}" stroke-width="1.5"/>' +
        t(145, 190, base) + t(30, 112, upright, 'end') + t(160, 96, hyp, 'start'),
        'A right-angled triangle with the right angle at the bottom left. Not drawn to scale.', 320)

FIG_T1 = right_tri('11 cm', '7 cm', '?')
FIG_T1_MD = 'A right-angled triangle with shorter sides 7 cm and 11 cm and an unknown hypotenuse. Not drawn to scale.'
FIG_T2 = right_tri('8.4 cm', '?', '13.5 cm')
FIG_T2_MD = 'A right-angled triangle with hypotenuse 13.5 cm, one shorter side 8.4 cm and the other shorter side unknown. Not drawn to scale.'

FIG_ISO = svg('0 0 320 200',
    poly('40,175 280,175 160,15') + dash(160, 15, 160, 175) +
    t(82, 90, '10 cm', 'end') + t(238, 90, '10 cm', 'start') + t(160, 195, '12 cm') + t(168, 100, 'h', 'start'),
    'An isosceles triangle with two equal sides of 10 cm and a base of 12 cm, with its height h drawn as a dashed line. Not drawn to scale.', 320)
FIG_ISO_MD = 'An isosceles triangle with two equal sides of 10 cm and a base of 12 cm. The height h is drawn from the top to the middle of the base. Not drawn to scale.'

FIG_SEMI = svg('0 0 320 175',
    shape('M60,150 A100,100 0 0 1 260,150 Z') + t(160, 170, '10 cm'),
    'A semicircle with diameter 10 cm. Not drawn to scale.', 320)
FIG_SEMI_MD = 'A semicircle with diameter 10 cm. Not drawn to scale.'

FIG_RS = svg('0 0 340 195',
    shape('M40,30 L220,30 A60,60 0 0 1 220,150 L40,150 Z') + dash(220, 30, 220, 150) +
    t(130, 22, '12 cm') + t(30, 95, '8 cm', 'end'),
    'A rectangle 12 cm by 8 cm with a semicircle added on one 8 cm side. Not drawn to scale.', 340)
FIG_RS_MD = 'A rectangle 12 cm long and 8 cm tall with a semicircle added on the right-hand 8 cm side. Not drawn to scale.'

FIG_RING = svg('0 0 320 200',
    f'<path d="M160,20 A80,80 0 1 1 160,180 A80,80 0 1 1 160,20 Z M160,50 A50,50 0 1 0 160,150 A50,50 0 1 0 160,50 Z" '
    f'fill="{FILL}" fill-rule="evenodd" stroke="{BLUE}" stroke-width="2"/>' +
    ln(160, 100, 240, 100) + ln(160, 100, 110, 100, AMB, 2) +
    t(205, 92, '8 cm') + t(135, 120, '5 cm', 'middle', AMB, True),
    'A ring between two circles with the same centre. The outer radius is 8 cm and the inner radius is 5 cm. Not drawn to scale.', 320)
FIG_RING_MD = 'A ring between two circles with the same centre: outer radius 8 cm, inner radius 5 cm. Not drawn to scale.'

FIG_SQC = svg('0 0 320 215',
    f'<path d="M60,20 H220 V180 H60 Z M140,20 A80,80 0 1 0 140,180 A80,80 0 1 0 140,20 Z" '
    f'fill="rgba(245,166,35,0.25)" fill-rule="evenodd" stroke="{BLUE}" stroke-width="2"/>' +
    f'<circle cx="140" cy="100" r="80" fill="none" stroke="{BLUE}" stroke-width="2"/>' + t(140, 202, '8 cm'),
    'A square of side 8 cm with a circle inside touching all four sides. The four corner pieces are shaded. Not drawn to scale.', 320)
FIG_SQC_MD = 'A square of side 8 cm with a circle inside touching all four sides. The four corner pieces outside the circle are shaded. Not drawn to scale.'

# ---------------------------------------------------------------- questions

Q = []
def num(id, sec, marks, q, ans, hint, reveal, unit='', tol=0, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='num', q=q, ans=ans, tol=tol, unit=unit, hint=hint, reveal=reveal, fig=fig, figmd=figmd))
def mcq(id, sec, marks, q, opts, correct, hint, reveal, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='mcq', q=q, opts=opts, correct=correct, hint=hint, reveal=reveal, fig=fig, figmd=figmd))

WP = '<em>Work it out on paper first.</em> '

# ---- A: number, percentages, bounds
num('n1','nu',2, WP + 'Work out (6.2 &times; 10<sup>4</sup>) &times; (4.5 &times; 10<sup>&minus;3</sup>). Give your answer as an ordinary number.',
    279, 'Multiply 6.2 by 4.5, then add the powers: 4 + (&minus;3).', '6.2 &times; 4.5 = 27.9 and 10<sup>4</sup> &times; 10<sup>&minus;3</sup> = 10<sup>1</sup>. So 27.9 &times; 10 = 279.')
num('n2','nu',2, WP + 'A jacket costs $60. Its price goes up by 25%, then the new price goes down by 10%. What is the final price?',
    67.5, 'Use multipliers: 1.25 and 0.90.', '60 &times; 1.25 = 75. Then 75 &times; 0.9 = 67.50. Final price $67.50 (not $60 plus 15%).', unit='$', tol=0.001)
mcq('n3','nu',1, 'A car loses 8% of its value every year. Which calculation gives its value after 4 years, starting from $<em>V</em>?',
    ['<em>V</em> &times; 0.92 &times; 4', '<em>V</em> &times; 0.68', '<em>V</em> &times; 1.08<sup>4</sup>', '<em>V</em> &times; 0.92<sup>4</sup>'], 'd',
    'Losing 8% means keeping 92% each year. Repeat the multiplier.',
    'D &mdash; Keeping 92% each year means multiplying by 0.92 four times: <em>V</em> &times; 0.92<sup>4</sup>. A multiplies by 4 instead of using a power, B takes off 8% four times as a flat 32%, and C grows by 8%.')
num('n4','nu',2, WP + '$3200 is invested at 5% compound interest per year. Find the value after 3 years, to the nearest cent.',
    3704.4, 'Multiplier 1.05, three times.', '3200 &times; 1.05<sup>3</sup> = 3200 &times; 1.157625 = $3704.40.', unit='$', tol=0.001)
num('n5','nu',1, WP + 'Round 0.006 359 to 2 significant figures.',
    0.0064, 'The first significant figure is the 6.', 'The 2 significant figures are 6 and 3. The next digit is 5, so round up: 0.0064.', tol=1e-9)
num('n6','nu',2, WP + 'In a sale, every price is reduced by 20%. A television now costs $336. What was its original price?',
    420, 'The sale price is 80% of the original. Divide, do not add 20%.', '336 &divide; 0.8 = $420. (Adding 20% to 336 would give 403.20, which is wrong.)', unit='$', tol=0.001)
num('n7','nu',3, WP + 'A bridge can carry 2000 kg, correct to the nearest 50 kg. Each crate weighs 70 kg, correct to the nearest 5 kg. What is the greatest number of crates that can <strong>always</strong> be carried safely?',
    27, 'Use the lowest possible limit and the heaviest possible crate.', 'Lowest limit = 1975 kg. Heaviest crate = 72.5 kg. 1975 &divide; 72.5 = 27.2, so 27 crates (28 &times; 72.5 = 2030, too heavy).')

# ---- B: algebra and equations
num('a1','al',2, WP + 'Use <em>v</em><sup>2</sup> = <em>u</em><sup>2</sup> + 2<em>as</em> to find <em>v</em> when <em>u</em> = 3, <em>a</em> = 2.5 and <em>s</em> = 10. Give <em>v</em> to 1 decimal place.',
    7.7, 'Find v<sup>2</sup> first, then square root.', 'v<sup>2</sup> = 9 + 2 &times; 2.5 &times; 10 = 59. v = &radic;59 = 7.68&hellip; = 7.7.', tol=0.0001)
mcq('a2','al',1, 'Simplify 12<em>a</em><sup>3</sup><em>b</em><sup>4</sup> &divide; 4<em>ab</em><sup>2</sup>.',
    ['3<em>a</em><sup>2</sup><em>b</em><sup>2</sup>', '8<em>a</em><sup>2</sup><em>b</em><sup>2</sup>', '3<em>a</em><sup>4</sup><em>b</em><sup>6</sup>', '3<em>a</em><sup>3</sup><em>b</em><sup>2</sup>'], 'a',
    'Divide the numbers, then subtract the powers of each letter.',
    'A &mdash; 12 &divide; 4 = 3, a<sup>3&minus;1</sup> = a<sup>2</sup> and b<sup>4&minus;2</sup> = b<sup>2</sup>. B subtracts the numbers, C adds the powers, and D forgets to subtract the 1 from the power of a.')
num('a3','al',2, WP + 'The area of a trapezium is <em>A</em> = &frac12;(<em>a</em> + <em>b</em>)<em>h</em>. Find <em>b</em> when <em>A</em> = 60, <em>a</em> = 7 and <em>h</em> = 8.',
    8, 'Put in the numbers first, then solve for b.', '60 = &frac12;(7 + b) &times; 8 = 4(7 + b). So 7 + b = 15 and b = 8.', unit='')
num('a4','al',2, WP + 'A plumber charges $25 plus $12 per hour. Mia can spend at most $100. What is the greatest <strong>whole</strong> number of hours she can pay for?',
    6, 'Solve 25 + 12h &le; 100, then think about whole hours.', '12h &le; 75, so h &le; 6.25. Whole hours only, so 6 (7 hours would cost $109).', unit='hours')
num('a5','al',2, 'The graph shows <em>y</em> = 3<em>x</em> &minus; 2 and <em>y</em> = <em>x</em> + 6. Solve the equations algebraically and find the <em>y</em>-value where the lines meet.',
    10, 'Set 3x &minus; 2 equal to x + 6.', '3x &minus; 2 = x + 6, so 2x = 8 and x = 4. Then y = 4 + 6 = 10. The lines meet at (4, 10).', fig=FIG_GRAPH, figmd=FIG_GRAPH_MD)
mcq('a6','al',1, 'Three pens and two books cost $13. One pen and one book cost $5. Using <em>p</em> for a pen and <em>b</em> for a book, which pair of equations is correct?',
    ['3<em>p</em> + 2<em>b</em> = 5 and <em>p</em> + <em>b</em> = 13', '3<em>p</em> + 2<em>b</em> = 13 and <em>p</em> + <em>b</em> = 5', '5<em>pb</em> = 13 and <em>p</em> + <em>b</em> = 5', '2<em>p</em> + 3<em>b</em> = 13 and <em>p</em> + <em>b</em> = 5'], 'b',
    'Each equation pairs the right quantity with the right total.',
    'B &mdash; Three pens (3<em>p</em>) and two books (2<em>b</em>) cost $13, and one of each costs $5. A swaps the totals, C writes a product, and D swaps the numbers of pens and books.')
num('a7','al',2, WP + 'Solve the equations from the previous question. How much do 2 pens and 5 books cost altogether?',
    16, 'Make the pen amounts match: use p + b = 5 to write p = 5 &minus; b.', 'From p + b = 5: p = 5 &minus; b. Then 3(5 &minus; b) + 2b = 13, so 15 &minus; b = 13 and b = 2, p = 3. Cost = 2 &times; 3 + 5 &times; 2 = $16.', unit='$')

# ---- C: polygons and Pythagoras
mcq('p1','py',2, 'Each interior angle of a regular polygon is 156&deg;. How many sides does the polygon have?',
    ['12', '15', '18', '24'], 'b',
    'Find the exterior angle first, then divide 360&deg; by it.',
    'B &mdash; Exterior angle = 180 &minus; 156 = 24&deg;. Number of sides = 360 &divide; 24 = 15. The number 24 is the exterior angle, not the number of sides.')
num('p2','py',2, WP + 'A right-angled triangle has shorter sides 7 cm and 11 cm. Find the hypotenuse to 1 decimal place.',
    13.0, 'Add the squares, then square root.', '7<sup>2</sup> + 11<sup>2</sup> = 49 + 121 = 170. &radic;170 = 13.04&hellip; = 13.0 cm.', unit='cm', tol=0.0001, fig=FIG_T1, figmd=FIG_T1_MD)
num('p3','py',2, WP + 'A right-angled triangle has hypotenuse 13.5 cm and one shorter side 8.4 cm. Find the other side to 1 decimal place.',
    10.6, 'This time subtract the squares.', '13.5<sup>2</sup> &minus; 8.4<sup>2</sup> = 182.25 &minus; 70.56 = 111.69. &radic;111.69 = 10.57&hellip; = 10.6 cm.', unit='cm', tol=0.0001, fig=FIG_T2, figmd=FIG_T2_MD)
mcq('p4','py',1, 'Which three lengths make a <strong>right-angled</strong> triangle?',
    ['5, 10, 12', '6, 8, 11', '7, 24, 25', '9, 12, 16'], 'c',
    'Square the two smaller numbers, add them, and compare with the square of the largest.',
    'C &mdash; 7<sup>2</sup> + 24<sup>2</sup> = 49 + 576 = 625 = 25<sup>2</sup>. For A, 25 + 100 = 125 &ne; 144. For B, 36 + 64 = 100 &ne; 121. For D, 81 + 144 = 225 &ne; 256.')
num('p5','py',3, WP + 'An isosceles triangle has two equal sides of 10 cm and a base of 12 cm. Find its area.',
    48, 'Drop the height from the top: it halves the base. Use Pythagoras for h.', 'Half the base = 6 cm. h = &radic;(10<sup>2</sup> &minus; 6<sup>2</sup>) = &radic;64 = 8 cm. Area = &frac12; &times; 12 &times; 8 = 48 cm<sup>2</sup>.', unit='cm&sup2;', fig=FIG_ISO, figmd=FIG_ISO_MD)

# ---- D: circles and compound shapes
num('c1','ci',2, WP + 'A circle has circumference 40 cm. Find its radius to 1 decimal place.',
    6.4, 'Circumference = 2&pi;r, so r = C &divide; 2&pi;.', 'r = 40 &divide; (2&pi;) = 6.366&hellip; = 6.4 cm.', unit='cm', tol=0.0001)
num('c2','ci',2, WP + 'A circular pond has an area of 120 m<sup>2</sup>. Find its radius to 1 decimal place.',
    6.2, 'Area = &pi;r<sup>2</sup>, so r<sup>2</sup> = A &divide; &pi;.', 'r<sup>2</sup> = 120 &divide; &pi; = 38.197&hellip; and r = 6.18&hellip; = 6.2 m.', unit='m', tol=0.0001)
num('c3','ci',2, WP + 'Find the perimeter of a semicircle with diameter 10 cm. Give your answer to 1 decimal place.',
    25.7, 'The curved edge is half a circumference. Do not forget the straight edge.', 'Curved edge = &frac12; &times; &pi; &times; 10 = 15.708. Add the diameter: 15.708 + 10 = 25.7 cm.', unit='cm', tol=0.0001, fig=FIG_SEMI, figmd=FIG_SEMI_MD)
num('c4','ci',2, WP + 'A shape is a 12 cm by 8 cm rectangle with a semicircle on one 8 cm side. Find its area to 1 decimal place.',
    121.1, 'Rectangle plus semicircle. The diameter of the semicircle is 8 cm.', 'Rectangle = 12 &times; 8 = 96. Semicircle radius 4: &frac12; &times; &pi; &times; 4<sup>2</sup> = 25.13. Total = 121.1 cm<sup>2</sup>.', unit='cm&sup2;', tol=0.0001, fig=FIG_RS, figmd=FIG_RS_MD)
num('c5','ci',2, WP + 'A ring lies between two circles with the same centre. The outer radius is 8 cm and the inner radius is 5 cm. Find the area of the ring to 1 decimal place.',
    122.5, 'Big circle minus small circle.', 'Area = &pi;(8<sup>2</sup> &minus; 5<sup>2</sup>) = &pi; &times; 39 = 122.5 cm<sup>2</sup>.', unit='cm&sup2;', tol=0.0001, fig=FIG_RING, figmd=FIG_RING_MD)
mcq('c6','ci',2, 'A circle fits exactly inside a square of side 8 cm. What is the total area of the four corner pieces outside the circle, to 1 decimal place?',
    ['13.7 cm&sup2;', '50.3 cm&sup2;', '38.9 cm&sup2;', '27.4 cm&sup2;'], 'a',
    'Square minus circle. The circle has diameter 8 cm, so what is its radius?',
    'A &mdash; Square = 64. Circle radius 4: &pi; &times; 4<sup>2</sup> = 50.27. Corners = 64 &minus; 50.27 = 13.7 cm<sup>2</sup>. B is the circle itself, C uses a semicircle and D doubles the answer.',
    fig=FIG_SQC, figmd=FIG_SQC_MD)
num('c7','ci',3, WP + 'A bicycle wheel has diameter 66 cm. How many <strong>complete</strong> turns does it make when the bicycle travels 1 km?',
    482, 'Find the circumference in cm. 1 km = 100 000 cm.', 'Circumference = &pi; &times; 66 = 207.35 cm. 100 000 &divide; 207.35 = 482.3, so 482 complete turns.')

# ---------------------------------------------------------------- written (printable only)

WRITTEN = [
  (27, 4, 'The Sun is 1.5 &times; 10<sup>8</sup> km from the Earth. Light travels at 3.0 &times; 10<sup>5</sup> km per second. (a) How many seconds does light take to reach the Earth? (b) Write this in minutes, to 1 decimal place.',
   '(a) Time = distance &divide; speed = (1.5 &times; 10<sup>8</sup>) &divide; (3.0 &times; 10<sup>5</sup>) [1] = 500 seconds [1]. (b) 500 &divide; 60 [1] = 8.3 minutes [1].'),
  (28, 4, 'A car is worth $18 000 and loses 12% of its value each year. (a) Find its value after 3 years, to the nearest dollar. (b) After how many whole years will it first be worth less than $9000? Show your working.',
   '(a) 18 000 &times; 0.88<sup>3</sup> [1] = $12 267 [1]. (b) Try values of n: n = 5 gives $9498, which is not enough; n = 6 gives $8358 [1], so 6 years [1].'),
  (29, 5, 'A rectangular lawn is 18 m by 11 m, both correct to the nearest metre. (a) Write the lower and upper bounds of each length. (b) Work out the smallest and largest possible area. (c) Can the owner be certain that 200 m<sup>2</sup> of turf is enough? Explain.',
   '(a) 17.5 &le; length &lt; 18.5 and 10.5 &le; width &lt; 11.5 [2]. (b) Smallest = 17.5 &times; 10.5 = 183.75 m<sup>2</sup> and largest = 18.5 &times; 11.5 = 212.75 m<sup>2</sup> [2]. (c) No, because the largest possible area, 212.75 m<sup>2</sup>, is more than 200 m<sup>2</sup> [1].'),
  (30, 5, 'A television screen is 80 cm wide and 45 cm high. (a) Find the length of its diagonal to 1 decimal place. (b) It is packed in a box whose longest inside length is 91 cm. Will the television fit along the diagonal of the box? Explain.',
   '(a) 80<sup>2</sup> + 45<sup>2</sup> = 6400 + 2025 = 8425 [1]; &radic;8425 [1] = 91.8 cm [1]. (b) The diagonal, 91.8 cm, is longer than 91 cm [1], so it will not fit [1].'),
  (31, 5, 'A window is a rectangle 1.2 m wide and 1.8 m high with a semicircle of diameter 1.2 m on top. (a) Find the perimeter of the whole window to 2 decimal places. (b) Find its area to 2 decimal places.',
   '(a) Curved edge = &frac12; &times; &pi; &times; 1.2 = 1.885 [1]. Straight edges = 1.8 + 1.8 + 1.2 = 4.8 [1]. Perimeter = 6.69 m [1]. (b) Rectangle = 1.2 &times; 1.8 = 2.16 and semicircle = &frac12; &times; &pi; &times; 0.6<sup>2</sup> = 0.565 [1]. Area = 2.73 m<sup>2</sup> [1].'),
]
