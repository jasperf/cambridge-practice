"""Spec: Secondary 2 · Semester 1 maths — Test 2 practice: Shapes, Angles & Algebra.

Build with:  python3 scripts/build_review_sheet.py scripts/review_specs/s2_sem1_maths_test2_shapes_angles_algebra.py

A fresh paper in the same layout as the Test 2 revision sheet (compound shapes with
pi = 22/7, angles, surds, indices, algebra) with all-new numbers. Every auto-marked
question is a typed number; the open "show your working" questions are printable-only.
"""

META = dict(
    out='s2/sem1/mocks/sem1-maths-test2-shapes-angles-algebra',
    title='Maths Test 2 &middot; Shapes, Angles &amp; Algebra',
    badge='Maths &middot; Test 2',
    eyebrow='Secondary 2 &middot; Mathematics &middot; Semester 1 assessment practice',
    h1='Shapes, Angles<br><em>&amp; Algebra</em>',
    md_title='Secondary 2 · Maths — Test 2: Shapes, Angles & Algebra',
    intro=('Five topics: compound shapes (with &pi; = 22/7), angles, simplifying surds, indices and powers of 10, '
           'and expressions, brackets and equations. <strong>No calculator.</strong> Work each question out on '
           'paper first, then type only the final number. Type decimals or whole numbers, '
           'with a minus sign where needed. Use <strong>Cover the notes</strong> to test yourself before reading the key facts.'),
    md_intro=('A practice paper for the Test 2 topics: compound shapes (π = 22/7), angles, surds, indices and '
              'algebra. Write every answer in your notebook. Q1–Q34 match the interactive sheet (each has one '
              'number as its answer); Q35–Q40 are written questions for you to show full working. '
              'No calculator is needed.'),
    time_chip='About 40 minutes &middot; no calculator',
    storage_key='sem1-maths-test2-shapes-angles-algebra',
    back='index.html',
    answers_note='Answers for Q1–Q34 (auto-marked on the interactive sheet) and a marking guide for the written questions Q35–Q40. Keep this separate from the question sheet.',
    extra_links=[('./sem1-maths-paper1-non-calculator.html', 'Paper 1'),
                 ('./sem1-maths-gaps.html', 'Gaps drill'),
                 ('../../reference/maths-formula-sheets/index.html', 'Formula sheets')],
)

EXPLORER_CSS = '''
.ftable { border-collapse: collapse; margin: 6px 0 14px; font-size: 0.9rem; }
.ftable th, .ftable td { border: 1px solid var(--border); padding: 6px 14px; text-align: center; }
.ftable th { background: var(--surface2); font-family: var(--font-mono); font-size: 0.76rem; color: var(--text-muted); }
'''

WK = '../t2/w5/term2-week5-maths-unit-test2-angles-shapes-measurements.html'
W1 = '../t1/w5/term1-week5-maths-expressions-formulae.html'
W2 = '../t1/w2/term1-week2-maths-rational-irrational.html'
W3 = '../t1/w2/term1-week2-maths-indices-standard-form.html'
W4 = '../t1/w8/term1-week8-maths-unit4-simultaneous-equations.html'

SECTIONS = [
  dict(key='cs', icon='&#9711;', color='var(--accent-math)', rgba='79,142,247',
       title='Compound Shapes (&pi; = 22/7)', label='Compound Shapes',
       src='Angles, Shapes &amp; Measurements', link=WK, link_label='Unit test 2 sheet',
       facts=[
         ('Take &pi; = 22/7', 'Radii of 7, 14 and 21 make the 7 cancel, so the answers come out neat.'),
         ('Circle parts', 'Circumference = 2&pi;r. A semicircle edge is &pi;r and a quarter-circle edge is &frac12;&pi;r. Area = &pi;r&sup2;, so a semicircle is &frac12;&pi;r&sup2; and a quarter circle is &frac14;&pi;r&sup2;.'),
         ('Perimeter', 'The distance round the <em>outside</em> only. A straight edge where two parts join is inside the shape, so leave it out.'),
         ('Radius, not diameter', 'If the diameter is given, halve it first.'),
         ('Cut-out pieces', 'Area of a trapezium = &frac12; &times; (sum of the parallel sides) &times; height. For a shape with a piece cut out, find the whole area and subtract the piece.'),
       ]),
  dict(key='an', icon='&#8736;', color='var(--accent-sci)', rgba='62,207,142',
       title='Angles', label='Angles',
       src='Angles, Shapes &amp; Measurements', link=WK, link_label='Unit test 2 sheet',
       facts=[
         ('Sums to remember', 'Triangle 180&deg;, quadrilateral 360&deg;, angles on a straight line 180&deg;, angles round a point 360&deg;.'),
         ('Isosceles triangle', 'The two base angles are equal.'),
         ('Exterior angle of a triangle', 'Equals the sum of the two opposite interior angles.'),
         ('Regular polygon', 'Sum of interior angles = (n &minus; 2) &times; 180&deg;. Divide by n for one angle.'),
         ('Parallel lines', 'Co-interior angles add to 180&deg;. Alternate and corresponding angles are equal.'),
         ('Shapes fitting together', 'Use one angle rule at each corner of the big shape to find what is left for the other piece.'),
       ]),
  dict(key='su', icon='&#8730;', color='var(--accent-warn)', rgba='245,166,35',
       title='Simplifying Surds', label='Simplifying Surds',
       src='Rational &amp; Irrational Numbers', link=W2, link_label='Rational &amp; irrational sheet',
       facts=[
         ('Splitting rule', '<span class="f">&radic;(a &times; b) = &radic;a &times; &radic;b</span>. Use the largest square factor (4, 9, 16, 25, 36, 49, 64, 81, 100).'),
         ('Check by squaring', 'a&radic;b is right if a&sup2; &times; b gives the number you started with.'),
         ('Adding surds', 'Simplify each one first. Then add only if the part under the root matches.'),
         ('Squaring a surd', '(a&radic;b)&sup2; = a&sup2; &times; b. And (&radic;b + c)(&radic;b &minus; c) = b &minus; c&sup2;.'),
       ]),
  dict(key='ix', icon='&#10024;', color='var(--accent-math)', rgba='79,142,247',
       title='Indices &amp; Powers of 10', label='Indices & Powers of 10',
       src='Indices &amp; Standard Form', link=W3, link_label='Indices &amp; standard form sheet',
       facts=[
         ('Zero and negative powers', 'x<sup>0</sup> = 1 and x<sup>&minus;n</sup> = 1 &divide; x<sup>n</sup>. A negative power is a <em>fraction</em>, not a negative number.'),
         ('Dividing by 10<sup>&minus;n</sup>', 'Is the same as multiplying by 10<sup>n</sup>.'),
         ('Laws', 'Multiply: add the powers. Divide: subtract the powers. Power of a power: multiply the powers. The power outside a bracket applies to the number too.'),
       ]),
  dict(key='al', icon='&#9999;&#65039;', color='var(--accent-sci)', rgba='62,207,142',
       title='Expressions, Brackets &amp; Equations', label='Expressions & Equations',
       src='Expressions &amp; Simultaneous Equations', link=W4, link_label='Simultaneous equations sheet',
       facts=[
         ('Words to expressions', 'Do the steps in order and use brackets when a step applies to a sum or difference.'),
         ('Rule from a table', 'Cost = value at 0 + jump &times; number of units.'),
         ('Two brackets', 'Multiply every term by every term, then collect the middle terms.'),
         ('Subtracting equations', 'Put the second equation in brackets so the minus applies to every term.'),
       ]),
]

# ---------------------------------------------------------------- figures

INK, BLUE, AMB = '#e8eaf0', '#4f8ef7', '#f5a623'
FILL = 'rgba(79,142,247,0.16)'

def svg(vb, inner, label, mw=380):
    return f'<svg class="q-fig" viewBox="{vb}" role="img" aria-label="{label}" style="max-width:{mw}px">{inner}</svg>'

def t(x, y, s, anchor='middle', col=INK, bold=False):
    w = ' font-weight="700"' if bold else ''
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{col}" font-size="14" font-family="Literata, Georgia, serif"{w}>{s}</text>'

def ang(x, y, s): return t(x, y, s, 'middle', AMB, True)
def pt(x, y, s, a='middle'): return t(x, y, s, a, INK, True)
def shape(d): return f'<path d="{d}" fill="{FILL}" stroke="{BLUE}" stroke-width="2"/>'
def poly(p): return f'<polygon points="{p}" fill="{FILL}" stroke="{BLUE}" stroke-width="2"/>'
def dash(x1, y1, x2, y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="1.5" stroke-dasharray="5 4"/>'
def ln(x1, y1, x2, y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="2"/>'

FIG_RECT = svg('-30 0 350 235',
    shape('M40,20 L166,20 A98,98 0 0 1 166,216 L40,216 Z') + dash(166, 20, 166, 216) +
    t(103, 13, '18 cm') + t(30, 122, '28 cm', 'end'),
    'A rectangle 18 cm by 28 cm with a semicircle added on one 28 cm side. Not drawn to scale.', 320)
FIG_RECT_MD = 'A rectangle 18 cm long and 28 cm tall with a semicircle added on the right-hand 28 cm side (the diameter of the semicircle is 28 cm). Not drawn to scale.'

FIG_TRAP = svg('-30 0 410 215',
    shape('M40,180 L320,180 L215,40 L40,40 A70,70 0 0 1 40,180 Z') + dash(40, 40, 40, 180) +
    pt(30, 36, 'D', 'end') + pt(215, 30, 'C') + pt(332, 196, 'B', 'start') + pt(30, 196, 'A', 'end') +
    t(127, 30, '35 cm') + t(180, 205, '56 cm') + t(22, 115, '28 cm', 'end') + t(285, 105, '35 cm', 'start'),
    'Trapezium ABCD with a semicircle cut out of the side AD. Not drawn to scale.')
FIG_TRAP_MD = 'Trapezium ABCD: A bottom-left, B bottom-right, C top-right, D top-left. AB = 56 cm, DC = 35 cm, BC = 35 cm, AD = 28 cm. A semicircle with diameter AD is cut out. Not drawn to scale.'

FIG_TWO = svg('0 0 320 215',
    shape('M110,15 A67,67 0 0 1 110,149 A22.4,22.4 0 0 1 110,194 Z') +
    t(98, 85, '42 mm', 'end') + t(98, 176, '14 mm', 'end'),
    'Two semicircles with diameters 42 mm and 14 mm joined along one straight line. Not drawn to scale.', 320)
FIG_TWO_MD = 'Two semicircles on the same straight line, diameters 42 mm and 14 mm, joined end to end. Not drawn to scale.'

FIG_QTR = svg('0 0 320 225',
    shape('M240,200 A180,180 0 0 0 60,20 L240,20 Z') +
    '<path d="M60,20 L60,200 L240,200" fill="none" stroke="#e8eaf0" stroke-width="1.5" stroke-dasharray="5 4"/>' +
    t(150, 13, '28 cm') + t(256, 115, '28 cm', 'start') + pt(52, 208, 'A', 'end') + pt(246, 216, 'B', 'start') +
    pt(246, 16, 'C', 'start') + pt(52, 16, 'D', 'end'),
    'Square ABCD with a quarter circle centre A cut out. Not drawn to scale.', 320)
FIG_QTR_MD = 'Square ABCD with side 28 cm. A quarter circle of radius 28 cm, centre A, is cut out. The shaded region is what is left. Not drawn to scale.'

FIG_ISO = svg('0 0 320 190', poly('160,20 40,170 280,170') + ang(160, 58, '50°') + ang(72, 164, 'x') + ang(248, 164, 'x'),
    'Isosceles triangle with apex angle 50 degrees and two equal base angles x. Not drawn to scale.', 320)
FIG_ISO_MD = 'Isosceles triangle. The angle at the top is 50°. The two base angles are both x. Not drawn to scale.'

FIG_QUAD = svg('0 0 320 210', poly('60,30 270,50 290,175 40,160') + ang(80, 56, '88°') + ang(246, 70, '72°') +
    ang(262, 160, '120°') + ang(72, 146, 'x'),
    'Quadrilateral with angles 88, 72, 120 degrees and x. Not drawn to scale.', 320)
FIG_QUAD_MD = 'Quadrilateral with interior angles 88°, 72°, 120° and x. Not drawn to scale.'

FIG_EXT = svg('0 0 380 200', poly('60,170 230,170 140,40') + ln(230, 170, 340, 170) + ang(98, 164, '47°') +
    ang(138, 78, '58°') + ang(256, 156, 'x'),
    'Triangle with interior angles 47 and 58 degrees; one side extended to make exterior angle x. Not drawn to scale.')
FIG_EXT_MD = 'Triangle with two interior angles 47° and 58°. The base is extended and x is the exterior angle at the right-hand end. Not drawn to scale.'

FIG_PAR = svg('0 0 380 200', ln(30, 60, 350, 60) + ln(30, 140, 350, 140) + ln(120, 185, 240, 15) +
    f'<polyline points="70,53 80,60 70,67" fill="none" stroke="{INK}" stroke-width="2"/>'
    f'<polyline points="70,133 80,140 70,147" fill="none" stroke="{INK}" stroke-width="2"/>' +
    ang(240, 82, '124°') + ang(182, 128, 'x'),
    'Two parallel lines crossed by a straight line; one angle is 124 degrees and x is between the parallel lines. Not drawn to scale.')
FIG_PAR_MD = 'Two parallel lines (marked with arrows) crossed by a transversal. Between the lines, on the right of the transversal, one angle is 124° (just below the upper line) and x is just above the lower line. Not drawn to scale.'

FIG_FIT = svg('0 0 400 225',
    '<polygon points="200,20 40,195 360,195" fill="none" stroke="#e8eaf0" stroke-width="2"/>'
    f'<polygon points="200,20 40,195 285,195 190,120" fill="{FILL}" stroke="{BLUE}" stroke-width="2"/>'
    f'<polyline points="190,31 200,42 210,31" fill="none" stroke="{INK}" stroke-width="1"/>' +
    pt(155, 150, 'A') + pt(250, 150, 'B') + pt(200, 12, 'T') + pt(30, 205, 'L', 'end') + pt(285, 213, 'N') +
    pt(372, 205, 'R', 'start') + pt(178, 118, 'M', 'end') +
    ang(186, 64, '35°') + ang(78, 188, '45°') + ang(255, 188, '40°') + ang(160, 104, '240°'),
    'A right-angled triangle TLR split into shape A (quadrilateral TLNM) and shape B (quadrilateral TMNR). Not drawn to scale.', 400)
FIG_FIT_MD = 'Right-angled triangle TLR (right angle at T) split into two quadrilaterals. Shape A is TLNM with angles T = 35°, L = 45°, N = 40° and reflex angle M = 240°. Shape B is TMNR. L, N and R are on a straight line. Not drawn to scale.'
FITTXT = ('Shapes <strong>A</strong> (quadrilateral TLNM) and <strong>B</strong> (quadrilateral TMNR) fit together to make a '
          'right-angled triangle TLR, with the right angle at T. In shape A the angle at T is 35&deg;, at L is 45&deg;, '
          'at N is 40&deg; and the <strong>reflex</strong> angle at M is 240&deg;. ')

TBL = ('<table class="ftable"><tr><th>Months</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr>'
       '<tr><th>Cost ($)</th><td>15</td><td>21</td><td>27</td><td>33</td><td>39</td></tr></table>')
TBL_MD = 'Table. Months 0, 1, 2, 3, 4. Cost in $: 15, 21, 27, 33, 39.'

# ---------------------------------------------------------------- questions

Q = []
def num(id, sec, marks, q, ans, hint, reveal, unit='', tol=0, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='num', q=q, ans=ans, tol=tol, unit=unit, hint=hint, reveal=reveal, fig=fig, figmd=figmd))

WP = '<em>Write it on paper first.</em> '

# ---- A: compound shapes
num('c1','cs',2, WP + 'A shape is a rectangle 18 cm by 28 cm with a semicircle added on one of the 28 cm sides (so the semicircle has diameter 28 cm). Find its perimeter.',
    108, 'Radius first. The side where the semicircle joins is inside the shape.', 'Radius = 14 cm. Curved edge = 22/7 &times; 14 = 44 cm. Perimeter = 18 + 18 + 28 + 44 = 108 cm.', unit='cm', fig=FIG_RECT, figmd=FIG_RECT_MD)
num('c2','cs',2, WP + 'Find the area of the same shape.',
    812, 'Rectangle plus semicircle.', 'Rectangle = 18 &times; 28 = 504. Semicircle = &frac12; &times; 22/7 &times; 14<sup>2</sup> = 308. Area = 504 + 308 = 812 cm<sup>2</sup>.', unit='cm&sup2;', fig=FIG_RECT, figmd='Same shape as Q1.')
num('c3','cs',2, WP + 'A semicircle is removed from trapezium ABCD. AB is parallel to DC, and AD is perpendicular to both. AB = 56 cm, DC = 35 cm, BC = 35 cm and AD = 28 cm (the diameter of the semicircle). Find the perimeter of the shaded region.',
    170, 'The straight edge AD is cut away, so it is not part of the perimeter.', 'Radius = 14 cm. Curved edge = 22/7 &times; 14 = 44 cm. Perimeter = 56 + 35 + 35 + 44 = 170 cm.', unit='cm', fig=FIG_TRAP, figmd=FIG_TRAP_MD)
num('c4','cs',3, WP + 'Find the area of the shaded region in the same figure.',
    966, 'Whole trapezium, then subtract the semicircle.', 'Trapezium = &frac12; &times; (35 + 56) &times; 28 = 1274. Semicircle = &frac12; &times; 22/7 &times; 14<sup>2</sup> = 308. Shaded area = 1274 &minus; 308 = 966 cm<sup>2</sup>.', unit='cm&sup2;', fig=FIG_TRAP, figmd='Same figure as Q3.')
num('c5','cs',2, WP + 'Two semicircles with diameters 42 mm and 14 mm are joined along a straight line, as shown. Find the perimeter of the whole shape.',
    144, 'Two curved edges, plus the straight edge that is the two diameters end to end.', 'Curved edges: 22/7 &times; 21 = 66 and 22/7 &times; 7 = 22. Straight edge = 42 + 14 = 56. Perimeter = 66 + 22 + 56 = 144 mm.', unit='mm', fig=FIG_TWO, figmd=FIG_TWO_MD)
num('c6','cs',2, WP + 'Find the area of the same shape.',
    770, 'Add the two semicircle areas: &frac12;&pi;r<sup>2</sup> each.', 'Area = &frac12; &times; 22/7 &times; (21<sup>2</sup> + 7<sup>2</sup>) = 11/7 &times; 490 = 770 mm<sup>2</sup>.', unit='mm&sup2;', fig=FIG_TWO, figmd='Same shape as Q5.')
num('c7','cs',2, WP + 'ABCD is a square of side 28 cm. A quarter circle of radius 28 cm, centre A, is cut out. Find the perimeter of the shaded region.',
    100, 'The shaded region has one curved edge and two straight sides.', 'Curved edge = &frac14; &times; 2 &times; 22/7 &times; 28 = 44 cm. Straight edges BC and CD = 28 + 28 = 56 cm. Perimeter = 44 + 56 = 100 cm.', unit='cm', fig=FIG_QTR, figmd=FIG_QTR_MD)
num('c8','cs',2, WP + 'Find the area of the shaded region in the same figure.',
    168, 'Square minus quarter circle.', 'Square = 28<sup>2</sup> = 784. Quarter circle = &frac14; &times; 22/7 &times; 28<sup>2</sup> = 616. Shaded area = 784 &minus; 616 = 168 cm<sup>2</sup>.', unit='cm&sup2;', fig=FIG_QTR, figmd='Same figure as Q7.')

# ---- B: angles
num('a1','an',1, WP + 'The triangle is isosceles with an apex angle of 50&deg;. Find <em>x</em>.',
    65, 'The two base angles share what is left of 180&deg;.', 'Base angles share 180 &minus; 50 = 130&deg;, so x = 130 &divide; 2 = 65&deg;.', unit='&deg;', fig=FIG_ISO, figmd=FIG_ISO_MD)
num('a2','an',1, WP + 'Find <em>x</em> in the quadrilateral.',
    80, 'Angles in a quadrilateral add to 360&deg;.', 'x = 360 &minus; 88 &minus; 72 &minus; 120 = 80&deg;.', unit='&deg;', fig=FIG_QUAD, figmd=FIG_QUAD_MD)
num('a3','an',1, WP + 'Find the exterior angle <em>x</em>.',
    105, 'Exterior angle = sum of the two opposite interior angles.', 'x = 47 + 58 = 105&deg;.', unit='&deg;', fig=FIG_EXT, figmd=FIG_EXT_MD)
num('a4','an',2, WP + 'Find the size of one interior angle of a regular polygon with 10 sides.',
    144, 'Sum of interior angles = (n &minus; 2) &times; 180. Then divide by n.', 'Sum = (10 &minus; 2) &times; 180 = 1440&deg;. One angle = 1440 &divide; 10 = 144&deg;.', unit='&deg;')
num('a5','an',1, WP + 'A straight line crosses two parallel lines. One angle is 124&deg;. Find <em>x</em>.',
    56, 'Both angles lie between the parallel lines on the same side of the crossing line.', '124&deg; and x are co-interior angles, so they add to 180&deg;. x = 180 &minus; 124 = 56&deg;.', unit='&deg;', fig=FIG_PAR, figmd=FIG_PAR_MD)
num('a6','an',1, WP + FITTXT + 'Find the angle of shape B at T.',
    55, 'The big angle at T is 90&deg;. Shape A takes some of it.', 'B = 90 &minus; 35 = 55&deg;.', unit='&deg;', fig=FIG_FIT, figmd=FIG_FIT_MD)
num('a7','an',1, WP + 'Using the same figure, find the angle of shape B at M.',
    120, 'Angles round a point add to 360&deg;.', 'B = 360 &minus; 240 = 120&deg;.', unit='&deg;', fig=FIG_FIT, figmd='Same figure as Q14.')
num('a8','an',1, WP + 'Using the same figure, find the angle of shape B at N.',
    140, 'L, N and R lie on a straight line.', 'B = 180 &minus; 40 = 140&deg;.', unit='&deg;', fig=FIG_FIT, figmd='Same figure as Q14.')
num('a9','an',1, WP + 'Using the same figure, find the angle of shape B at R.',
    45, 'Look at the whole triangle TLR.', 'Triangle TLR: R = 180 &minus; 90 &minus; 45 = 45&deg;. Check: 55 + 120 + 140 + 45 = 360. &#10003;', unit='&deg;', fig=FIG_FIT, figmd='Same figure as Q14.')

# ---- C: surds
num('s1','su',1, WP + 'Simplify &radic;98 and write it as <em>a</em>&radic;2. Find <em>a</em>.',
    7, 'Which square number divides 98?', '98 = 49 &times; 2, so &radic;98 = 7&radic;2 and a = 7.')
num('s2','su',1, WP + 'Simplify &radic;45 and write it as <em>a</em>&radic;5. Find <em>a</em>.',
    3, 'Is 9 a factor of 45?', '45 = 9 &times; 5, so &radic;45 = 3&radic;5 and a = 3.')
num('s3','su',2, WP + 'Work out (3&radic;5)<sup>2</sup>.',
    45, 'Square the 3 and square the &radic;5, then multiply.', '3<sup>2</sup> &times; (&radic;5)<sup>2</sup> = 9 &times; 5 = 45.')
num('s4','su',2, WP + 'Simplify &radic;12 + &radic;75 and write it as <em>a</em>&radic;3. Find <em>a</em>.',
    7, 'Simplify each root first, then add the numbers in front.', '&radic;12 = 2&radic;3 and &radic;75 = 5&radic;3. Sum = 7&radic;3, so a = 7.')
num('s5','su',2, WP + 'Expand and simplify (&radic;13 + 2)(&radic;13 &minus; 2).',
    9, 'Difference of two squares.', '(&radic;13)<sup>2</sup> &minus; 2<sup>2</sup> = 13 &minus; 4 = 9.')

# ---- D: indices
num('i1','ix',1, WP + 'Write 2<sup>&minus;3</sup> as a decimal.',
    0.125, 'A negative power means 1 divided by the positive power.', '2<sup>&minus;3</sup> = 1 &divide; 8 = 0.125.', tol=1e-6)
num('i2','ix',2, WP + '<em>y</em> = <em>x</em><sup>0</sup> + <em>x</em><sup>&minus;1</sup> &minus; <em>x</em><sup>&minus;2</sup>. Find <em>y</em> when <em>x</em> = 2. Give a decimal.',
    1.25, 'x<sup>0</sup> = 1, x<sup>&minus;1</sup> = 1/x, x<sup>&minus;2</sup> = 1/x<sup>2</sup>.', '1 + 1/2 &minus; 1/4 = 1 + 0.5 &minus; 0.25 = 1.25.', tol=1e-6)
num('i3','ix',2, WP + 'Work out 460 &divide; 10<sup>&minus;2</sup>.',
    46000, 'Dividing by 10<sup>&minus;2</sup> is the same as multiplying by what?', 'Dividing by 10<sup>&minus;2</sup> is multiplying by 100. 460 &times; 100 = 46 000.')
num('i4','ix',2, WP + '0.4 &divide; 10<sup><em>k</em></sup> = 4000. Find <em>k</em>.',
    -4, 'The answer is much bigger than 0.4, so what kind of power is it?', '0.4 &times; 10<sup>4</sup> = 4000, so dividing by 10<sup>&minus;4</sup> gives 4000 and k = &minus;4.')
num('i5','ix',1, WP + '20<em>a</em><sup>9</sup> &divide; 5<em>a</em><sup>4</sup> = 4<em>a</em><sup><em>k</em></sup>. Find <em>k</em>.',
    5, 'Subtract the powers.', '20 &divide; 5 = 4 and a<sup>9&minus;4</sup> = a<sup>5</sup>. k = 5.')
num('i6','ix',1, WP + '(2<em>n</em><sup>3</sup>)<sup>4</sup> = <em>an</em><sup><em>b</em></sup>. Find <em>a</em> + <em>b</em>.',
    28, 'The power 4 applies to the 2 as well.', '2<sup>4</sup> = 16 and (n<sup>3</sup>)<sup>4</sup> = n<sup>12</sup>. So 16n<sup>12</sup> and a + b = 16 + 12 = 28.')

# ---- E: expressions, brackets, equations
num('e1','al',2, WP + 'Sam thinks of <em>n</em>. He <strong>subtracts 2</strong>, <strong>squares</strong> the result, then <strong>multiplies by 3</strong>. Write his expression. What is its value when <em>n</em> = 6?',
    48, 'Squares means power 2. Which part gets squared?', 'Expression: 3(n &minus; 2)<sup>2</sup>. When n = 6: 3 &times; 4<sup>2</sup> = 3 &times; 16 = 48.')
num('e2','al',2, WP + 'A gym charges a joining fee plus a monthly amount. The table shows the cost. How much does it cost for 9 months?',
    69, 'The value at 0 months is the joining fee. How much does each month add?', 'Joining fee 15, then 6 for each month. Cost = 15 + 6 &times; 9 = 69.', unit='$', fig=TBL, figmd=TBL_MD)
num('e3','al',1, WP + '(<em>x</em> + 8)(<em>x</em> &minus; 3) = <em>x</em><sup>2</sup> + <em>bx</em> &minus; 24. Find <em>b</em>.',
    5, 'Add the two middle terms.', '&minus;3x + 8x = 5x, so b = 5.')
num('e4','al',2, WP + '(2<em>y</em> + 3)(3<em>y</em> &minus; 7) = 6<em>y</em><sup>2</sup> + <em>by</em> &minus; 21. Find <em>b</em>. (It can be negative.)',
    -5, 'Middle terms: 2y &times; (&minus;7) and 3 &times; 3y.', '&minus;14y + 9y = &minus;5y, so b = &minus;5.')
num('e5','al',2, WP + '5<em>x</em> + 2<em>y</em> = 26 and 5<em>x</em> &minus; 3<em>y</em> = 11. <strong>Subtract the second equation from the first.</strong> You get <em>ay</em> = <em>c</em>. Find <em>a</em> + <em>c</em>.',
    20, 'Put the second equation in brackets. 2y &minus; (&minus;3y) = ?', '(5x + 2y) &minus; (5x &minus; 3y) = 5y and 26 &minus; 11 = 15. So 5y = 15, a = 5, c = 15 and a + c = 20.')
num('e6','al',2, WP + 'Now solve the same pair: 5<em>x</em> + 2<em>y</em> = 26 and 5<em>x</em> &minus; 3<em>y</em> = 11. Find <em>x</em> &times; <em>y</em>.',
    12, 'Find y first, then put it back to find x.', '5y = 15 so y = 3. Then 5x + 6 = 26, so x = 4. Check: 20 &minus; 9 = 11. &#10003; x &times; y = 12.')

# ---------------------------------------------------------------- written (printable only)

WRITTEN = [
  (35, 3, 'A rectangle is 24 cm by 14 cm. A semicircle of diameter 14 cm is cut out of one short end. Using &pi; = 22/7, show that the area of the remaining shape is 259 cm<sup>2</sup>.',
   'Rectangle = 24 &times; 14 = 336 cm<sup>2</sup> [1]. Radius 7 cm, so semicircle = &frac12; &times; 22/7 &times; 7<sup>2</sup> = 77 cm<sup>2</sup> [1]. Remaining area = 336 &minus; 77 = 259 cm<sup>2</sup> [1].'),
  (36, 3, 'Triangle ABC is isosceles with AB = AC and angle BAC = 56&deg;. BC is extended to D. (a) Find angle ABC. (b) Find angle ACD, giving a reason.',
   '(a) Base angles share 180 &minus; 56 = 124&deg;, so ABC = 62&deg; [1]. (b) ACB is also 62&deg; [1]. Angles on a straight line add to 180&deg;, so ACD = 118&deg; [1]. (Check: exterior angle = 56 + 62 = 118&deg;.)'),
  (37, 3, 'Simplify &radic;147 + &radic;27 &minus; &radic;48. Give your answer as <em>a</em>&radic;3.',
   '&radic;147 = 7&radic;3, &radic;27 = 3&radic;3 and &radic;48 = 4&radic;3 [2 for all three, 1 for two]. 7 + 3 &minus; 4 = 6, so 6&radic;3 [1].'),
  (38, 3, 'Show that (3<em>n</em><sup>4</sup> &times; 8<em>n</em><sup>5</sup>) &divide; (2<em>n</em><sup>3</sup>)<sup>2</sup> simplifies to 6<em>n</em><sup>3</sup>. Show the top, the bottom, then combine.',
   'Top: 3 &times; 8 = 24 and n<sup>4</sup> &times; n<sup>5</sup> = n<sup>9</sup>, so 24n<sup>9</sup> [1]. Bottom: (2n<sup>3</sup>)<sup>2</sup> = 4n<sup>6</sup> [1]. Combine: 24n<sup>9</sup> &divide; 4n<sup>6</sup> = 6n<sup>3</sup> [1].'),
  (39, 3, 'A taxi charges $5 plus $3 for each kilometre. (a) Write an expression for the cost of <em>k</em> km. (b) A journey costs $38. How many kilometres is it? Show your working.',
   '(a) 5 + 3k [1]. (b) 5 + 3k = 38 [1], 3k = 33, so k = 11 km [1].'),
  (40, 3, 'Solve 3<em>x</em> + 4<em>y</em> = 26 and 3<em>x</em> + <em>y</em> = 11. Show how you eliminate a letter and check your answer.',
   'The x terms match, so subtract: 3y = 15 [1], y = 5 [1]. Then 3x + 5 = 11, so x = 2. Check in the first equation: 6 + 20 = 26 [1].'),
]
