"""Spec: Secondary 2 · Semester 1 science — Bonding & Ions practice (a focused drill on one topic).

Build with:  python3 scripts/build_review_sheet.py scripts/review_specs/s2_sem1_science_bonding_ions.py
"""
import math

META = dict(
    out='s2/sem1/sem1-science-bonding-ions',
    title='Bonding &amp; Ions &middot; Practice',
    badge='Science &middot; Bonding &amp; Ions',
    eyebrow='Secondary 2 &middot; Science &middot; Term 1 topic drill',
    h1='Bonding &amp; Ions<br><em>step by step</em>',
    md_title='Secondary 2 · Science — Bonding & Ions Practice',
    intro=('One topic, taken slowly: how atoms turn into ions, how to write ionic formulae, why ionic '
           'compounds behave as they do, then covalent and metallic bonding and how to tell the three '
           'apart. Each section starts with its key facts, and three explorers let you watch electrons move '
           'and balance charges yourself. Use <strong>Cover the notes</strong> to test yourself first.'),
    md_intro=('A focused practice sheet on bonding and ions: forming ions, ionic formulae, ionic compounds, '
              'covalent bonding, and metallic bonding with how to tell the types apart. Q1–Q36 match the '
              'interactive sheet; Q37–Q42 are written questions marked by the teacher. Diagrams are '
              'described in words.'),
    time_chip='About 35 minutes &middot; periodic table helps',
    storage_key='sem1-science-bonding-ions',
    back='../../index.html',
    answers_note='Answers for Q1–Q36 (auto-marked on the interactive sheet) and a marking guide for the written questions Q37–Q42. Keep this separate from the question sheet.',
    extra_links=[('../sem1/sem1-science-revision.html', 'Terms 1–2 science review'),
                 ('../science-formula-sheets/index.html', 'Formula sheets')],
)

W3 = '../t1/w3/term1-week3-science-ionic-bonding.html'
W4 = '../t1/w4/term1-week4-science-covalent-metallic-bonding.html'
PT = ('../science-formula-sheets/svg/science-diagram-periodic-table.svg', 'Periodic table')

SECTIONS = [
  dict(key='io', icon='&#9883;', color='var(--accent-math)', rgba='79,142,247',
       title='From Atoms to Ions', label='Atoms to Ions',
       src='Term 1 &middot; Week 3', link=W3, link2=PT,
       facts=[
         ('Why atoms react', 'Every atom &ldquo;wants&rdquo; a full outer shell. The noble gases (Group 8) already have one, so they hardly react. Other atoms lose, gain or share electrons to get there.'),
         ('What an ion is', 'A charged particle made when an atom loses or gains <em>electrons</em>. The protons never change, so the element stays the same.'),
         ('Which way?', 'Metals have few outer electrons and <strong>lose</strong> them &rarr; <span class="f">positive ions</span>. Non-metals have nearly full outer shells and <strong>gain</strong> electrons &rarr; <span class="f">negative ions</span>.'),
         ('The charge from the group', 'Groups 1, 2, 3 &rarr; <span class="f">1+, 2+, 3+</span><br>Groups 5, 6, 7 &rarr; <span class="f">3&minus;, 2&minus;, 1&minus;</span><br>Group 4 and Group 8 do not usually form ions.'),
         ('Counting electrons in an ion', 'Start from the atomic number (protons). A + charge means that many electrons fewer; a &minus; charge means that many more. Example: Li&#8314; has 3 protons and 2 electrons.'),
         ('Naming ions', 'A metal ion keeps its name: lithium &rarr; lithium ion. A non-metal ion ends in <strong>-ide</strong>: bromine &rarr; bromide, phosphorus &rarr; phosphide.'),
       ]),
  dict(key='fo', icon='&#9878;', color='var(--accent-math)', rgba='79,142,247',
       title='Writing Ionic Formulae', label='Ionic Formulae',
       src='Term 1 &middot; Week 3', link=W3,
       facts=[
         ('The one rule', 'An ionic compound has no overall charge: <span class="f">total + charge = total &minus; charge</span>.'),
         ('Step by step', '1. Write each ion&rsquo;s charge.<br>2. Find the smallest number both charges go into.<br>3. Use enough of each ion to reach it.'),
         ('Worked example', 'Al&sup3;&#8314; and S&sup2;&#8315;: 3 and 2 both go into 6. Two Al&sup3;&#8314; give 6+, three S&sup2;&#8315; give 6&minus; &rarr; <span class="f">Al&#8322;S&#8323;</span>.'),
         ('Equal charges', 'If the charges are the same size, one of each is enough: Ba&sup2;&#8314; with S&sup2;&#8315; &rarr; <span class="f">BaS</span>, not Ba&#8322;S&#8322;.'),
         ('Reading a formula', 'The small number counts the ion just before it. A missing number means one. The charges are never written in the formula.'),
         ('Naming the compound', 'Metal first, then the non-metal with <strong>-ide</strong>: KBr is potassium bromide.'),
       ]),
  dict(key='ic', icon='&#129482;', color='var(--accent-sci)', rgba='62,207,142',
       title='Ionic Compounds', label='Ionic Compounds',
       src='Term 1 &middot; Week 3', link=W3,
       facts=[
         ('The bond', 'Ionic bonding is the strong <em>electrostatic attraction</em> between oppositely charged ions.'),
         ('Giant lattice', 'The ions pack in a huge, regular 3D pattern. Each ion is surrounded by ions of the opposite charge, pulling on it from every side.'),
         ('Melting points', 'To melt the lattice, a huge number of strong attractions must be overcome, so ionic compounds melt at high temperatures and are solid at room temperature.'),
         ('Conducting', 'A current needs charged particles that can <em>move</em>. Solid: the ions are locked in place, so no current. Molten or dissolved in water: the ions are free, so it conducts.'),
         ('No molecules', 'An ionic compound is not made of separate molecules. NaCl is a <em>ratio</em> (one Na&#8314; for every Cl&#8315;), not one small particle.'),
       ]),
  dict(key='co', icon='&#128279;', color='var(--accent-warn)', rgba='245,166,35',
       title='Covalent Bonding', label='Covalent Bonding',
       src='Term 1 &middot; Week 4', link=W4,
       facts=[
         ('Sharing', 'Two non-metal atoms each put one electron into a <strong>shared pair</strong>. One shared pair is one covalent bond. The pair counts towards the outer shell of <em>both</em> atoms.'),
         ('How many bonds?', 'An atom makes as many bonds as the electrons it is short of a full shell. Hydrogen (1 short) makes 1. Carbon (2,4: 4 short) makes 4.'),
         ('Double bonds', 'Two shared pairs between the same two atoms make a <strong>double bond</strong>: 4 shared electrons. An atom that is 2 short can fill its shell this way.'),
         ('Dot-and-cross', 'Draw one atom&rsquo;s electrons as dots and the other&rsquo;s as crosses. Each shared pair sits where the two outer shells overlap.'),
         ('Simple molecules', 'The bonds <em>inside</em> a molecule are strong, but the forces <em>between</em> molecules are weak. Little energy separates them: low melting and boiling points.'),
         ('No current', 'Molecules have no overall charge and no free electrons, so covalent substances do not conduct, even when melted.'),
       ]),
  dict(key='me', icon='&#9881;', color='var(--accent-warn)', rgba='245,166,35',
       title='Metallic Bonding &amp; Telling Them Apart', label='Metallic & Comparing',
       src='Term 1 &middot; Week 4', link=W4,
       facts=[
         ('Metallic bonding', 'Metal atoms give up their outer electrons to the whole structure. Positive metal ions sit in layers in a &ldquo;sea&rdquo; of <strong>delocalised</strong> electrons, and the two attract.'),
         ('Conducting', 'The delocalised electrons drift through the metal when a voltage is applied, so metals conduct as solids and when melted.'),
         ('Bending', 'Layers of ions can slide over each other while the sea of electrons keeps holding them together, so metals bend and can be hammered into shape.'),
         ('Spot the type', '<span class="f">metal + non-metal &rarr; ionic</span><br><span class="f">non-metal + non-metal &rarr; covalent</span><br><span class="f">metal(s) only &rarr; metallic</span>'),
       ]),
]

# ---------------------------------------------------------------- figures

MONO = 'font-family="DM Mono, monospace"'


def _lattice():
    s = ['<svg class="q-fig" viewBox="0 0 300 190" role="img" aria-label="A grid of particles in rows: positive and negative ones alternate in every direction" style="max-width:300px">']
    for r in range(4):
        for c in range(6):
            x, y = 50 + c * 40, 35 + r * 40
            pos = (r + c) % 2 == 0
            col = '#4f8ef7' if pos else '#f5a623'
            s.append(f'<circle class="draw" cx="{x}" cy="{y}" r="{13 if pos else 16}" stroke="{col}" stroke-width="2" fill="none" pathLength="1"/>')
            s.append(f'<text x="{x}" y="{y}" font-size="15" fill="{col}" text-anchor="middle" dominant-baseline="central" {MONO}>{"+" if pos else "&#8722;"}</text>')
    s.append('</svg>')
    return ''.join(s)


def _sea():
    s = ['<svg class="q-fig" viewBox="0 0 300 190" role="img" aria-label="Rows of positive particles, all the same, with many small negative dots scattered between them" style="max-width:300px">',
         '<rect class="fill" x="20" y="14" width="260" height="162" rx="10" fill="rgba(79,142,247,0.10)"/>']
    for r in range(3):
        for c in range(5):
            x, y = 50 + c * 50, 45 + r * 50
            s.append(f'<circle class="draw" cx="{x}" cy="{y}" r="16" stroke="#3ecf8e" stroke-width="2" fill="none" pathLength="1"/>')
            s.append(f'<text x="{x}" y="{y}" font-size="15" fill="#3ecf8e" text-anchor="middle" dominant-baseline="central" {MONO}>+</text>')
    pts = [(75, 30), (125, 68), (178, 28), (225, 72), (32, 95), (100, 118), (150, 75), (268, 120), (75, 168), (200, 165),
           (250, 30), (125, 160), (175, 118), (30, 150), (270, 70), (225, 125)]
    for x, y in pts:
        s.append(f'<circle class="fill" cx="{x}" cy="{y}" r="3.5" fill="#e8eaf0"/>')
    s.append('</svg>')
    return ''.join(s)


def _cl2():
    s = ['<svg class="q-fig" viewBox="0 0 300 200" role="img" aria-label="Dot-and-cross diagram of a chlorine molecule: two overlapping outer shells, one shared pair in the overlap, and three more pairs around each atom" style="max-width:300px">']
    L, R, cy, r = 110, 190, 100, 58
    s.append(f'<circle class="draw" cx="{L}" cy="{cy}" r="{r}" stroke="#4f8ef7" stroke-width="2" fill="none" pathLength="1"/>')
    s.append(f'<circle class="draw" cx="{R}" cy="{cy}" r="{r}" stroke="#f5a623" stroke-width="2" fill="none" pathLength="1"/>')
    s.append(f'<text x="{L}" y="{cy}" font-size="18" fill="#e8eaf0" text-anchor="middle" dominant-baseline="central" {MONO}>Cl</text>')
    s.append(f'<text x="{R}" y="{cy}" font-size="18" fill="#e8eaf0" text-anchor="middle" dominant-baseline="central" {MONO}>Cl</text>')

    def dot(x, y):
        s.append(f'<circle class="fill" cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#4f8ef7"/>')

    def cross(x, y):
        s.append(f'<path class="draw" d="M{x-4:.1f} {y-4:.1f} L{x+4:.1f} {y+4:.1f} M{x+4:.1f} {y-4:.1f} L{x-4:.1f} {y+4:.1f}" stroke="#f5a623" stroke-width="2" fill="none" pathLength="1"/>')

    dot(150, 90)
    cross(150, 110)
    for cx, draw_fn, angles in ((L, dot, (90, 180, 270)), (R, cross, (90, 0, 270))):
        for a in angles:
            t = math.radians(a)
            x, y = cx + r * math.cos(t), cy + r * math.sin(t)
            ox, oy = -math.sin(t) * 9, math.cos(t) * 9
            draw_fn(x + ox, y + oy)
            draw_fn(x - ox, y - oy)
    s.append(f'<text x="150" y="190" font-size="11" fill="#7a84a0" text-anchor="middle" {MONO}>outer shells only</text></svg>')
    return ''.join(s)


FIG_LATTICE, FIG_SEA, FIG_CL2 = _lattice(), _sea(), _cl2()

# ---------------------------------------------------------------- questions

Q = []
def num(id, sec, marks, q, ans, hint, reveal, unit='', tol=0, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='num', q=q, ans=ans, tol=tol, unit=unit, hint=hint, reveal=reveal, fig=fig, figmd=figmd))
def text(id, sec, marks, q, acc, hint, reveal, ph='type your answer', fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='text', q=q, acc=acc, ph=ph, hint=hint, reveal=reveal, fig=fig, figmd=figmd))
def mcq(id, sec, marks, q, opts, correct, hint, reveal, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='mcq', q=q, opts=opts, correct=correct, hint=hint, reveal=reveal, fig=fig, figmd=figmd))

# ---- A: atoms to ions
num('s1','io',1,'Calcium has atomic number 20 and forms Ca²⁺ ions. How many <strong>electrons</strong> does one Ca²⁺ ion have?',18,
    'A 2+ ion has lost two electrons. How many did the atom have?','20 − 2 = 18 electrons (2,8,8). It still has 20 protons.', unit='electrons')
text('s2','io',2,'Sulfur has atomic number 16. Write the electronic structure of the sulfide ion, S²⁻.',
    ['2,8,8','2.8.8','2, 8, 8','2 8 8','2-8-8'],'Write the atom first (16 electrons), then add the electrons it gains.',
    'Sulfur is 2,8,6. It gains two electrons, so S²⁻ is 2,8,8: a full outer shell, like argon.', ph='e.g. 2,8,1')
mcq('s3','io',1,'A particle has 12 protons and 10 electrons. What is it?',
    ['A neon atom, Ne','A magnesium ion, Mg²⁺','An oxide ion, O²⁻','A magnesium ion, Mg²⁻'],'b',
    'The protons tell you the element. Then compare the protons with the electrons.',
    'B — 12 protons makes it magnesium. Two fewer electrons than protons means a charge of 2+. (Neon and O²⁻ also have 10 electrons, but not 12 protons.)')
num('s4','io',1,'Nitrogen has the electronic structure 2,5. How many electrons does a nitrogen atom <strong>gain</strong> when it forms an ion?',3,
    'How many more does the outer shell need to hold 8?','5 + 3 = 8, so it gains 3 electrons and becomes N³⁻ (a nitride ion).', unit='electrons')
text('s5','io',1,'What is the name of the ion that a fluorine atom forms?',
    ['fluoride','fluoride ion','a fluoride ion','the fluoride ion','f-','f−'],'Non-metal ions change their ending.','Fluoride (F⁻)', ph='one word')
mcq('s6','io',1,'Which two ions <strong>both</strong> have the electronic structure 2,8?',
    ['K⁺ and Cl⁻','Li⁺ and Be²⁺','Mg²⁺ and S²⁻','Al³⁺ and F⁻'],'d',
    'Work out each ion: atomic number, then add or take away electrons.',
    'D — Al (13) loses 3 → 10 electrons; F (9) gains 1 → 10 electrons. Both are 2,8. K⁺ and Cl⁻ are 2,8,8; Li⁺ and Be²⁺ are 2; S²⁻ is 2,8,8.')
mcq('s7','io',1,'A potassium atom (atomic number 19) becomes a K⁺ ion. Which statement is true?',
    ['It loses one electron and still has 19 protons.','It gains one proton, which makes it positive.','It loses one proton and becomes argon.','It gains one electron, which makes it positive.'],'a',
    'Which particles can an atom lose or gain in a reaction?',
    'A — Only electrons move. Losing one negative electron leaves one more proton than electrons, so the charge is 1+. The 19 protons keep it potassium.')
num('s8','io',2,'An ion X³⁻ has 10 electrons. What is the atomic number of element X?',7,
    'A 3− ion has gained 3 electrons. How many did the atom have?','10 − 3 = 7 electrons in the atom, so 7 protons: X is nitrogen.')

# ---- B: formulae
text('s9','fo',1,'Lithium forms Li⁺ ions and sulfur forms S²⁻ ions. Write the formula of lithium sulfide.',
    ['Li2S','Li₂S'],'How many 1+ ions balance one 2− ion?','Li₂S: two Li⁺ (2+) balance one S²⁻ (2−).', ph='e.g. NaCl')
text('s10','fo',1,'Aluminium forms Al³⁺ ions and fluorine forms F⁻ ions. Write the formula of aluminium fluoride.',
    ['AlF3','AlF₃'],'How many 1− ions balance one 3+ ion?','AlF₃: one Al³⁺ (3+) balances three F⁻ (3−).', ph='e.g. NaCl')
text('s11','fo',2,'Calcium forms Ca²⁺ ions and nitrogen forms N³⁻ ions. Write the formula of calcium nitride.',
    ['Ca3N2','Ca₃N₂'],'What is the smallest number that both 2 and 3 go into?',
    'Ca₃N₂: three Ca²⁺ give 6+, two N³⁻ give 6−.', ph='e.g. CaCl2')
text('s12','fo',2,'Aluminium forms Al³⁺ ions and oxygen forms O²⁻ ions. Write the formula of aluminium oxide.',
    ['Al2O3','Al₂O₃'],'Find the smallest number both 3 and 2 go into, then count the ions.',
    'Al₂O₃: two Al³⁺ give 6+, three O²⁻ give 6−.', ph='e.g. CaCl2')
text('s13','fo',1,'Sodium is in Group 1 and oxygen is in Group 6. Write the formula of sodium oxide.',
    ['Na2O','Na₂O'],'First use the groups to work out each ion’s charge.','Na⁺ and O²⁻, so two Na⁺ balance one O²⁻: Na₂O.', ph='e.g. NaCl')
mcq('s14','fo',1,'What is the name of the compound CaBr₂?',
    ['Calcium dibromine','Bromine calcide','Calcium bromide','Calcium bromate'],'c',
    'Which element is named first, and how does the non-metal’s name change?',
    'C — Calcium bromide: the metal keeps its name and bromine becomes bromide. The “2” is not said in the name of an ionic compound.')
mcq('s15','fo',1,'A student writes the formula of magnesium fluoride as MgF. What is wrong?',
    ['The charges do not balance: one Mg²⁺ needs two F⁻, so it is MgF₂.','The fluorine should be written first: FMg.','It should be Mg₂F, because magnesium has two outer electrons.','Fluorine forms 2− ions, so it should be MgF.'],'a',
    'Write the two charges and add them up.',
    'A — Mg²⁺ + F⁻ leaves 1+ left over. Two F⁻ ions are needed: MgF₂.')
text('s16','fo',1,'Barium chloride has the formula BaCl₂. Chloride ions are Cl⁻. What is the charge on a barium ion? (Type it like 2+ or 1−.)',
    ['2+','+2','ba2+','2 +'],'Two Cl⁻ ions give a total of 2−. What must balance that?',
    '2+: two Cl⁻ give 2−, so the single barium ion must be Ba²⁺. (Barium is in Group 2.)', ph='e.g. 3+')

# ---- C: ionic compounds
text('s17','ic',1,'The diagram shows how the particles are arranged in a solid. What type of bonding holds it together?',
    ['ionic','ionic bonding','ionic bond','ionic bonds','an ionic lattice','ionic lattice'],
    'Look at the charges on neighbouring particles.',
    'Ionic: positive and negative ions alternate in a regular lattice, held by attraction between opposite charges.',
    ph='one word', fig=FIG_LATTICE,
    figmd='A grid of 24 particles in 4 rows. Positive (+) and negative (−) particles alternate in every row and every column.')
mcq('s18','ic',1,'Four substances were tested. Which one is most likely to be an ionic compound?',
    ['Melts at −7 °C; never conducts','Melts at 1083 °C; conducts as a solid and as a liquid','Melts at 3550 °C; never conducts','Melts at 714 °C; conducts only when melted or dissolved'],'d',
    'Which one has charged particles that are only free to move once it melts?',
    'D — A high melting point plus conducting only when molten or dissolved is the pattern of an ionic compound. B is a metal (copper), A is a covalent molecule (bromine).')
mcq('s19','ic',2,'Sodium chloride is still solid at 700 °C. Which explanation is best?',
    ['The covalent bond inside each NaCl molecule is very hard to break.','Millions of strong attractions between Na⁺ and Cl⁻ ions all have to be overcome.','The electrons in sodium chloride are stuck in a sea and cannot escape.','Sodium and chlorine atoms have no charge, so they do not move apart.'],'b',
    'Is sodium chloride made of molecules? What holds each ion in place?',
    'B — There are no NaCl molecules. Each ion is pulled on from every side by oppositely charged ions, and all of those attractions must be overcome to melt the lattice.')
text('s20','ic',1,'Copper chloride solution conducts electricity. Which particles carry the charge through the solution?',
    ['ions','the ions','charged ions','copper and chloride ions','copper ions and chloride ions','cu2+ and cl-'],
    'They are charged, and dissolving set them free.','Ions (Cu²⁺ and Cl⁻), which can move once dissolved. It is not electrons that flow through the solution.', ph='one word')
mcq('s21','ic',1,'A crystal of salt is hit with a hammer and shatters, instead of bending. Why?',
    ['The hammer breaks the covalent bonds between the atoms.','Salt has a sea of electrons that is easily lost.','When a layer shifts, ions with the same charge end up side by side and repel.','The ions melt where the hammer hits.'],'c',
    'Picture the lattice: what lines up after one layer slides by one ion?',
    'C — Sliding one layer puts + next to + and − next to −. These repel, so the crystal splits apart. A metal has no such problem, because its sea of electrons keeps holding the layers.')
mcq('s22','ic',1,'Potassium bromide is dissolved in water and two electrodes are dipped in. Which way do the K⁺ ions move?',
    ['Towards the positive electrode','They stay in one place in the lattice','Up to the surface of the water','Towards the negative electrode'],'d',
    'Opposite charges attract.',
    'D — K⁺ is positive, so it is attracted to the negative electrode. The Br⁻ ions move the other way, to the positive electrode.')

# ---- D: covalent
num('s23','co',1,'In ammonia, one nitrogen atom (2,5) bonds covalently to hydrogen atoms. How many hydrogen atoms does it join to?',3,
    'How many electrons is nitrogen short of a full outer shell? Each hydrogen provides one.',
    'Nitrogen is 3 short, so it makes 3 bonds, one to each of 3 hydrogen atoms: NH₃.', unit='atoms')
text('s24','co',1,'Carbon makes four bonds and chlorine makes one. Write the formula of the molecule formed from one carbon atom and chlorine.',
    ['CCl4','CCl₄'],'How many chlorine atoms does it take to use up carbon’s four bonds?','CCl₄: four chlorine atoms, one on each of carbon’s four bonds.', ph='e.g. CH4')
num('s25','co',2,'A methane molecule, CH₄, has four single covalent bonds. How many electrons are shared in the molecule altogether?',8,
    'Count the shared pairs first, then the electrons.','4 bonds × 2 electrons each = 8 shared electrons.', unit='electrons')
num('s26','co',1,'The diagram shows the outer shells in a chlorine molecule, Cl₂. How many electrons are in the outer shell of the <strong>left</strong> atom, counting the shared pair?',8,
    'The shared pair counts for both atoms.','6 of its own unshared electrons + the 2 in the shared pair = 8: a full outer shell.',
    unit='electrons', fig=FIG_CL2,
    figmd='Two overlapping circles, each labelled Cl. In the overlap: one dot and one cross (the shared pair). Around the rest of the left circle: three pairs of dots. Around the right circle: three pairs of crosses.')
mcq('s27','co',2,'Water boils at 100 °C but sodium chloride melts at 801 °C. Why is water’s value so much lower?',
    ['Covalent bonds are weak, so the O–H bonds break at 100 °C.','Water molecules are charged, so they push each other apart.','Water has fewer electrons than sodium chloride.','Boiling only separates whole water molecules, and the forces between them are weak.'],'d',
    'When water boils, are the O–H bonds broken? What is pulled apart?',
    'D — Steam is still H₂O, so no covalent bonds break. Only the weak forces between molecules are overcome, which takes little energy. Melting NaCl means breaking strong ionic attractions.')
mcq('s28','co',1,'Which substance is made of covalent molecules?',
    ['Potassium oxide','Calcium','Sulfur dioxide','Lithium fluoride'],'c',
    'Look for a compound made only of non-metals.',
    'C — Sulfur and oxygen are both non-metals, so they share electrons. Potassium oxide and lithium fluoride are ionic (metal + non-metal); calcium is a metal.')
text('s29','co',1,'In a nitrogen molecule, N₂, the two atoms share <strong>three</strong> pairs of electrons. What is this kind of bond called?',
    ['triple','triple bond','a triple bond','triple covalent bond','a triple covalent bond','triple covalent'],
    'One pair is a single bond, two pairs a double bond...','A triple bond (6 shared electrons). Each nitrogen was 3 short of a full shell.', ph='e.g. single bond')
num('s30','co',1,'A carbon dioxide molecule is O=C=O: carbon has a double bond to each oxygen. How many shared <strong>pairs</strong> of electrons are in the molecule?',4,
    'How many pairs make one double bond?','2 double bonds × 2 pairs = 4 shared pairs (8 electrons). Carbon makes 4 bonds in total.', unit='pairs')

# ---- E: metallic and comparing
mcq('s31','me',1,'The diagram shows the particles in a solid. What type of bonding does it show?',
    ['Ionic','Metallic','Covalent','None: these are separate noble gas atoms'],'b',
    'Are all the big particles the same charge? What are the small dots?',
    'B — Metallic: identical positive ions with free electrons spread between them. In an ionic lattice the charges would alternate.',
    fig=FIG_SEA,
    figmd='Three rows of five identical positive (+) particles, with small dots (electrons) scattered in the spaces between them.')
mcq('s32','me',2,'Solid copper conducts electricity, but solid copper chloride does not. Why?',
    ['Copper chloride has no charged particles in it.','Copper atoms are smaller, so the current squeezes through.','Copper has electrons that are free to move; the ions in solid copper chloride are held in place.','Chloride ions block the flow of protons.'],'c',
    'Which charged particles can move in each solid?',
    'C — Copper’s delocalised electrons can drift through it. Copper chloride is full of ions, but in the solid they cannot move, so no current flows until it melts or dissolves.')
text('s33','me',1,'Brass is an alloy of copper and zinc. What type of bonding holds brass together?',
    ['metallic','metallic bonding','metallic bond','metallic bonds'],'Copper and zinc: metal or non-metal?','Metallic: an alloy contains only metals.', ph='one word')
mcq('s34','me',1,'Which substance is matched with the correct type of bonding?',
    ['Magnesium: metallic','Calcium chloride: covalent','Ammonia: ionic','Carbon dioxide: metallic'],'a',
    'Sort each substance into metal only, metal + non-metal, or non-metals only.',
    'A — Magnesium is a metal element, so metallic. Calcium chloride is ionic (metal + non-metal); ammonia and carbon dioxide are covalent (non-metals only).')
text('s35','me',1,'Substance X melts at 1538 °C, conducts both as a solid and when melted, and can be hammered into thin sheets. What type of bonding does it have?',
    ['metallic','metallic bonding','metallic bond'],'Which type conducts even as a solid?','Metallic (it is iron). Conducting as a solid and bending without breaking both come from the sea of electrons.', ph='one word')
text('s36','me',1,'Substance Y melts at −114 °C and does not conduct electricity as a solid or as a liquid. What type of bonding does it have?',
    ['covalent','covalent bonding','covalent bond','covalent molecules','simple covalent','simple molecular','molecular'],
    'A very low melting point means weak forces between particles.','Covalent: small molecules with weak forces between them, and no ions or free electrons to carry a current.', ph='one word')

WRITTEN = [
  (37, 3, 'Draw dot-and-cross diagrams to show how a magnesium atom (2,8,2) and an oxygen atom (2,6) form ions. Show all the shells, the electrons that move, and the charge on each ion.',
   'Mg²⁺ drawn as 2,8 (outer shell empty/removed) [1]; O²⁻ drawn as 2,8 with the two gained electrons shown as a different symbol [1]; both in square brackets with 2+ and 2− charges [1].'),
  (38, 3, 'Draw a dot-and-cross diagram for a molecule of ammonia, NH₃. Show outer shells only.',
   'N in the middle with three H atoms, each overlapping the N shell [1]; each overlap holds one dot and one cross (a shared pair) [1]; nitrogen also has one unshared pair, so 8 electrons in its outer shell, and each H has 2 [1].'),
  (39, 2, 'Carbon has the electronic structure 2,4. Explain why carbon does not usually form ions, and how it gets a full outer shell instead.',
   'Losing or gaining four electrons would take too much energy / is too many to move [1]; it shares four pairs of electrons in four covalent bonds (e.g. CH₄) [1].'),
  (40, 4, 'Molten sodium chloride and solid copper both conduct electricity. Solid sodium chloride and liquid water do not. Explain all four results using the particles in each.',
   'Molten NaCl: ions free to move and carry charge [1]; copper: delocalised electrons free to move [1]; solid NaCl: ions fixed in the lattice [1]; water: neutral molecules, no ions or free electrons (pure water) [1].'),
  (41, 3, 'Use labelled diagrams to explain why a sheet of metal can be bent, but a crystal of an ionic compound shatters when it is hit.',
   'Metal: layers of positive ions slide, the sea of electrons keeps holding them, so it bends [1]; ionic: one layer shifts so like charges line up [1]; like charges repel and the crystal splits [1].'),
  (42, 4, 'Four substances were tested. P: melts at 98 °C, conducts as a solid and a liquid. Q: melts at 1418 °C, conducts only when melted or dissolved. R: boils at −183 °C, never conducts. S: melts at 660 °C, can be hammered flat, conducts as a solid. Give the type of bonding in each, with one reason.',
   'P metallic: conducts as a solid (it is sodium) [1]; Q ionic: high melting point and conducts only when its ions are free [1]; R covalent: very low boiling point, no charged particles (oxygen) [1]; S metallic: malleable and conducts as a solid (aluminium) [1].'),
]

# ---------------------------------------------------------------------------
# Explorers. None of them shows a value that a question on the sheet asks for:
# the transfer animation uses NaCl and MgO, and the charge balancer uses
# made-up ions M and X and only names a formula once the student balances it.
# ---------------------------------------------------------------------------

EXPLORERS = {
  'io': '''<div class="explorer">
  <h3>&#9883; Electron Transfer</h3>
  <p class="ex-note">Pick a metal and a non-metal, then press <strong>Transfer</strong>. Dots are the metal&rsquo;s electrons; crosses are the non-metal&rsquo;s.</p>
  <div class="ex-btns">
    <button class="ex-btn on" data-pair="nacl">Sodium + chlorine</button>
    <button class="ex-btn" data-pair="mgo">Magnesium + oxygen</button>
    <button class="ex-btn go" id="tr-go">Transfer &rarr;</button>
    <button class="ex-btn" id="tr-reset">Reset</button>
  </div>
  <svg class="ex-svg wide" id="tr-svg" viewBox="0 0 440 230" role="img" aria-label="Two atoms; the metal's outer electrons move across to the non-metal"></svg>
  <div class="ex-readout" id="tr-read"></div>
</div>''',
  'fo': '''<div class="explorer">
  <h3>&#9878; Charge Balancer</h3>
  <p class="ex-note">M is a made-up metal and X a made-up non-metal. Choose their charges, then add ions until the charges cancel with as few ions as possible.</p>
  <div class="ex-row">
    <div class="ex-controls">
      <label for="cb-p">Charge on M</label>
      <select id="cb-p" class="ex-select"><option value="1">1+</option><option value="2" selected>2+</option><option value="3">3+</option></select>
      <div class="ex-btns"><button class="ex-btn" data-cb="m+">+ M</button><button class="ex-btn" data-cb="m-">&minus; M</button></div>
      <label for="cb-n">Charge on X</label>
      <select id="cb-n" class="ex-select"><option value="1">1&minus;</option><option value="2">2&minus;</option><option value="3" selected>3&minus;</option></select>
      <div class="ex-btns"><button class="ex-btn" data-cb="x+">+ X</button><button class="ex-btn" data-cb="x-">&minus; X</button></div>
    </div>
    <svg class="ex-svg" id="cb-svg" viewBox="0 0 360 140" style="max-width:400px" role="img" aria-label="The M and X ions you have added"></svg>
  </div>
  <div class="ex-readout" id="cb-read"></div>
</div>''',
  'ic': '''<div class="explorer">
  <h3>&#128161; Can It Conduct?</h3>
  <p class="ex-note">An ionic compound between two electrodes wired to a bulb. Switch between solid and melted and watch the ions.</p>
  <div class="ex-btns">
    <button class="ex-btn on" data-state="solid">Solid</button>
    <button class="ex-btn" data-state="melt">Melted</button>
  </div>
  <svg class="ex-svg wide" id="lc-svg" viewBox="0 0 440 220" role="img" aria-label="Ions between two electrodes, with a bulb in the circuit">
    <path d="M84 40 V22 H206 M234 22 H356 V40" stroke="#7a84a0" stroke-width="2" fill="none"/>
    <circle id="lc-glow" cx="220" cy="22" r="24" fill="#f5a623" opacity="0"/>
    <circle cx="220" cy="22" r="12" fill="#1e2336" stroke="#e8eaf0" stroke-width="2"/>
    <path d="M212 14 L228 30 M228 14 L212 30" stroke="#e8eaf0" stroke-width="1.6"/>
    <line x1="140" y1="12" x2="140" y2="32" stroke="#e8eaf0" stroke-width="2.5"/><line x1="148" y1="16" x2="148" y2="28" stroke="#e8eaf0" stroke-width="5"/>
    <rect x="96" y="48" width="248" height="160" rx="6" fill="rgba(62,207,142,0.06)" stroke="#2a3050"/>
    <rect x="80" y="40" width="8" height="150" fill="#7a84a0"/><rect x="352" y="40" width="8" height="150" fill="#7a84a0"/>
    <g id="lc-ions"></g>
  </svg>
  <div class="ex-readout" id="lc-read"></div>
</div>''',
}

EXPLORER_CSS = '''
.ex-btns { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 12px; }
.ex-btn { font-family: var(--font-mono); font-size: 0.76rem; padding: 7px 12px; border-radius: 6px; border: 1px solid var(--border); background: var(--surface2); color: var(--text); cursor: pointer; }
.ex-btn:hover { border-color: var(--sec); }
.ex-btn.on { background: rgba(var(--sec-rgb),0.18); border-color: var(--sec); }
.ex-btn.go { background: var(--sec); color: #0f1117; border-color: var(--sec); font-weight: 600; }
.ex-btn:disabled { opacity: 0.45; cursor: default; }
.ex-select { font-family: var(--font-mono); font-size: 0.85rem; padding: 6px 8px; border-radius: 6px; background: var(--surface2); color: var(--text); border: 1px solid var(--border); max-width: 120px; }
#tr-svg .mv { transition: transform 1.2s cubic-bezier(0.45,0,0.25,1); }
#tr-svg .fade { transition: opacity 0.6s ease; }
@media (prefers-reduced-motion: reduce) { #tr-svg .mv, #tr-svg .fade { transition: none; } }
'''

EXPLORER_JS = r'''
const REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const SUBN = n => n === 1 ? '' : String(n).split('').map(d => '₀₁₂₃₄₅₆₇₈₉'[d]).join('');

// ---- Electron Transfer
(function() {
  const svg = document.getElementById('tr-svg');
  if (!svg) return;
  const PAIRS = {
    nacl: { m: ['Na', [2,8,1], 'sodium'], n: ['Cl', [2,8,7], 'chlorine'], k: 1, name: 'NaCl' },
    mgo:  { m: ['Mg', [2,8,2], 'magnesium'], n: ['O', [2,6], 'oxygen'], k: 2, name: 'MgO' },
  };
  const RAD = [22, 40, 58], MX = 110, NX = 330, CY = 118;
  const dotBtns = svg.parentNode.querySelectorAll('[data-pair]');
  const go = document.getElementById('tr-go');
  let cur = 'nacl', moving = [];
  const at = (cx, r, deg) => [cx + r*Math.cos(deg*Math.PI/180), CY + r*Math.sin(deg*Math.PI/180)];
  const dot = (x, y, cls='') => `<circle class="${cls}" cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="4.5" fill="#4f8ef7"/>`;
  const cross = (x, y) => `<path d="M${x-4} ${y-4} L${x+4} ${y+4} M${x+4} ${y-4} L${x-4} ${y+4}" stroke="#f5a623" stroke-width="2.2"/>`;
  const shellAngles = n => n === 2 ? [-90, 90] : Array.from({length: n}, (_, j) => 22.5 + j*45);
  const ions = sh => sh.join(',');
  function draw() {
    const P = PAIRS[cur], k = P.k, [ms, msh] = P.m, [ns, nsh] = P.n;
    let s = '';
    // metal: inner shells, then the outer shell (which empties)
    msh.forEach((n, i) => {
      const r = RAD[i], outer = i === msh.length - 1;
      s += `<circle class="${outer ? 'fade m-outer' : ''}" cx="${MX}" cy="${CY}" r="${r}" fill="none" stroke="#4a5270" stroke-width="1.5"/>`;
      if (!outer) shellAngles(n).forEach(a => { const [x, y] = at(MX, r, a); s += dot(x, y); });
    });
    // non-metal: inner shells full, outer shell with k empty slots facing the metal
    nsh.forEach((n, i) => {
      const r = RAD[i], outer = i === nsh.length - 1;
      s += `<circle cx="${NX}" cy="${CY}" r="${r}" fill="none" stroke="#4a5270" stroke-width="1.5"/>`;
      if (!outer) { shellAngles(n).forEach(a => { const [x, y] = at(NX, r, a); s += cross(x, y); }); return; }
      const base = 180 - (k-1)*22.5;
      for (let j = k; j < 8; j++) { const [x, y] = at(NX, r, base + j*45); s += cross(x, y); }
    });
    s += `<circle cx="${MX}" cy="${CY}" r="13" fill="#f5a623"/><text x="${MX}" y="${CY}" font-size="12" fill="#0f1117" text-anchor="middle" dominant-baseline="central" font-family="DM Mono, monospace" font-weight="600">${ms}</text>`;
    s += `<circle cx="${NX}" cy="${CY}" r="13" fill="#f5a623"/><text x="${NX}" y="${CY}" font-size="12" fill="#0f1117" text-anchor="middle" dominant-baseline="central" font-family="DM Mono, monospace" font-weight="600">${ns}</text>`;
    // the electrons that will move: start on the metal's outer shell, facing right
    moving = [];
    const mr = RAD[msh.length-1], nr = RAD[nsh.length-1], base = 180 - (k-1)*22.5;
    for (let j = 0; j < k; j++) {
      const [x0, y0] = at(MX, mr, -(k-1)*22.5 + j*45), [x1, y1] = at(NX, nr, base - j*45 + (k-1)*45);
      s += `<g class="mv" id="tr-e${j}">${dot(x0, y0)}</g>`;
      moving.push([x1 - x0, y1 - y0]);
    }
    // brackets and charges, hidden until the transfer
    const br = (cx, r, label) => `<g class="fade br" opacity="0"><path d="M${cx-r-6} ${CY-r-6} h-7 v${2*r+12} h7 M${cx+r+6} ${CY-r-6} h7 v${2*r+12} h-7" stroke="#e8eaf0" stroke-width="2" fill="none"/><text x="${cx+r+18}" y="${CY-r-2}" font-size="15" fill="#3ecf8e" font-family="DM Mono, monospace">${label}</text></g>`;
    s += br(MX, RAD[msh.length-2], (k > 1 ? k : '') + '+') + br(NX, nr, (k > 1 ? k : '') + '−');
    svg.innerHTML = s;
    go.disabled = false;
    document.getElementById('tr-read').innerHTML = `<strong>${ms}</strong> ${ions(msh)} &nbsp;&middot;&nbsp; <strong>${ns}</strong> ${ions(nsh)}<br>The ${P.m[2]} atom has ${k} outer electron${k > 1 ? 's' : ''}; the ${P.n[2]} atom is ${k} short of a full shell. Press Transfer.`;
  }
  function transfer() {
    const P = PAIRS[cur], k = P.k, [ms, msh] = P.m, [ns, nsh] = P.n;
    go.disabled = true;
    moving.forEach(([dx, dy], j) => { document.getElementById('tr-e' + j).style.transform = `translate(${dx}px, ${dy}px)`; });
    setTimeout(() => {
      svg.querySelector('.m-outer').setAttribute('opacity', '0');
      svg.querySelectorAll('.br').forEach(b => b.setAttribute('opacity', '1'));
      const after = nsh.slice(); after[after.length-1] += k;
      document.getElementById('tr-read').innerHTML = `<strong>${ms}${k > 1 ? '²' : ''}⁺</strong> ${ions(msh.slice(0, -1))} &nbsp;&middot;&nbsp; <strong>${ns}${k > 1 ? '²' : ''}⁻</strong> ${ions(after)}<br>Both ions now have a full outer shell. The ${k}+ and ${k}− attract: <strong>${P.name}</strong>.`;
    }, REDUCED ? 0 : 1250);
  }
  dotBtns.forEach(b => b.addEventListener('click', () => { dotBtns.forEach(o => o.classList.toggle('on', o === b)); cur = b.dataset.pair; draw(); }));
  go.addEventListener('click', transfer);
  document.getElementById('tr-reset').addEventListener('click', draw);
  draw();
})();

// ---- Charge Balancer
(function() {
  const svg = document.getElementById('cb-svg');
  if (!svg) return;
  const pc = document.getElementById('cb-p'), nc = document.getElementById('cb-n');
  let m = 1, x = 1;
  const gcd = (a, b) => b ? gcd(b, a % b) : a;
  function ion(cx, cy, label, col) {
    return `<circle cx="${cx}" cy="${cy}" r="21" fill="${col}22" stroke="${col}" stroke-width="2"/><text x="${cx}" y="${cy}" font-size="12" fill="${col}" text-anchor="middle" dominant-baseline="central" font-family="DM Mono, monospace">${label}</text>`;
  }
  function draw() {
    const p = +pc.value, n = +nc.value;
    let s = '';
    for (let i = 0; i < m; i++) s += ion(36 + i*58, 38, 'M' + (p > 1 ? p : '') + '+', '#4f8ef7');
    for (let i = 0; i < x; i++) s += ion(36 + i*58, 102, 'X' + (n > 1 ? n : '') + '−', '#f5a623');
    svg.innerHTML = s;
    const tp = m*p, tn = x*n;
    let msg;
    if (tp === tn) msg = gcd(m, x) === 1
      ? `<span style="color:var(--correct)">Balanced, with the fewest ions.</span> Formula: <strong>M${SUBN(m)}X${SUBN(x)}</strong>`
      : 'Balanced, but not the smallest set. Can you take away ions and still balance?';
    else msg = tp > tn ? 'Too much positive charge. Add an X or take away an M.' : 'Too much negative charge. Add an M or take away an X.';
    document.getElementById('cb-read').innerHTML = `Total positive: <strong>+${tp}</strong> &nbsp;&middot;&nbsp; total negative: <strong>−${tn}</strong><br>${msg}`;
  }
  svg.parentNode.parentNode.querySelectorAll('[data-cb]').forEach(b => b.addEventListener('click', () => {
    const a = b.dataset.cb;
    if (a === 'm+' && m < 6) m++; if (a === 'm-' && m > 1) m--;
    if (a === 'x+' && x < 6) x++; if (a === 'x-' && x > 1) x--;
    draw();
  }));
  [pc, nc].forEach(sel => sel.addEventListener('change', () => { m = 1; x = 1; draw(); }));
  draw();
})();

// ---- Can It Conduct?
(function() {
  const grp = document.getElementById('lc-ions');
  if (!grp) return;
  const btns = grp.closest('.explorer').querySelectorAll('[data-state]');
  const glow = document.getElementById('lc-glow');
  let melted = false;
  const ions = [];
  for (let r = 0; r < 4; r++) for (let c = 0; c < 6; c++) {
    const pos = (r + c) % 2 === 0, hx = 125 + c*38, hy = 74 + r*36;
    const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    const col = pos ? '#4f8ef7' : '#f5a623';
    g.innerHTML = `<circle r="${pos ? 10 : 12}" fill="${col}33" stroke="${col}" stroke-width="1.8"/><text font-size="13" fill="${col}" text-anchor="middle" dominant-baseline="central" font-family="DM Mono, monospace">${pos ? '+' : '−'}</text>`;
    grp.appendChild(g);
    ions.push({ g, hx, hy, x: hx, y: hy, vx: 0, vy: 0, ph: Math.random()*6.28 });
  }
  function place(o) { o.g.setAttribute('transform', `translate(${o.x.toFixed(1)} ${o.y.toFixed(1)})`); }
  function readout() {
    glow.setAttribute('opacity', melted ? '0.75' : '0');
    document.getElementById('lc-read').innerHTML = melted
      ? 'Melted: the lattice has broken up and the ions <strong>move freely</strong>. Moving charges make a current, so the bulb lights.'
      : 'Solid: every ion only <strong>vibrates on the spot</strong>, held by its neighbours. No charge can travel, so the bulb stays off.';
  }
  function scatter() { ions.forEach(o => { o.x = 110 + Math.random()*220; o.y = 64 + Math.random()*130; place(o); }); }
  let t = 0, last = performance.now();
  function frame(now) {
    const dt = Math.min(0.05, (now - last)/1000); last = now; t += dt;
    ions.forEach(o => {
      if (!melted) { o.x = o.hx + 1.8*Math.sin(t*14 + o.ph); o.y = o.hy + 1.8*Math.cos(t*11 + o.ph); }
      else {
        o.vx += (Math.random() - 0.5)*120*dt; o.vy += (Math.random() - 0.5)*120*dt;
        o.vx = Math.max(-40, Math.min(40, o.vx)); o.vy = Math.max(-40, Math.min(40, o.vy));
        o.x += o.vx*dt; o.y += o.vy*dt;
        if (o.x < 110 || o.x > 330) { o.vx = -o.vx; o.x = Math.max(110, Math.min(330, o.x)); }
        if (o.y < 62 || o.y > 194) { o.vy = -o.vy; o.y = Math.max(62, Math.min(194, o.y)); }
      }
      place(o);
    });
    requestAnimationFrame(frame);
  }
  btns.forEach(b => b.addEventListener('click', () => {
    btns.forEach(o => o.classList.toggle('on', o === b));
    melted = b.dataset.state === 'melt';
    if (!melted) ions.forEach(o => { o.x = o.hx; o.y = o.hy; o.vx = o.vy = 0; place(o); });
    else if (REDUCED) scatter();
    readout();
  }));
  ions.forEach(place); readout();
  if (!REDUCED) requestAnimationFrame(frame);
})();
'''
