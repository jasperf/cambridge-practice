"""Spec: Secondary 2 · Semester 1 science — Mock Paper 4, the short combined paper.

Build with:  python3 scripts/build_review_sheet.py scripts/review_specs/s2_sem1_science_mock4_express.py

A concise mock (30 questions, 38 marks) covering all of Terms 1-2: three or four
questions on each topic, all new. Key-fact cards are shared with mock 2.
"""
import importlib.util
from pathlib import Path

_here = Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location('mock2', _here / 's2_sem1_science_mock2_combined.py')
_m2 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_m2)

META = dict(
    out='s2/sem1/mocks/sem1-science-mock4-express',
    title='Science Mock Paper 4 &middot; Short Combined',
    badge='Science &middot; Semester 1 Mock 4',
    eyebrow='Secondary 2 &middot; Science &middot; Semester 1 assessment &middot; short paper',
    h1='Science Mock 4<br><em>Short &amp; combined</em>',
    intro=('A shorter Semester 1 mock covering every topic from Terms 1 and 2: atoms, bonding, photosynthesis, '
           'transport and the carbon cycle, human biology, density, sound, thermal energy and electricity. '
           'There are only three or four questions on each topic, and all are new. Use <strong>Cover the notes</strong> '
           'and try each section cold before reading its key facts.'),
    md_title='Secondary 2 · Science — Semester 1 Mock Paper 4 (Short Combined)',
    md_intro=('A short practice paper for the Semester 1 assessment covering all topics from Terms 1 and 2, with '
              'three or four new questions on each. Q1–Q30 match the interactive sheet; Q31–Q33 are written '
              'questions marked by the teacher. Allow about 45 minutes for Q1–Q30 and 15 minutes for the written '
              'questions. A calculator helps. Diagrams are described in words.'),
    time_chip='About 45 minutes &middot; a calculator helps',
    storage_key='sem1-science-mock4-express',
    back='../../../index.html',
    answers_note=('Answers for Q1–Q30 (auto-marked on the interactive sheet) and a marking guide for the '
                  'written questions Q31–Q33. Keep this separate from the question sheet.'),
    extra_links=[('./sem1-science-mock3-combined.html', 'Mock paper 3'),
                 ('./sem1-science-revision.html', 'Terms 1–2 review'),
                 ('../../reference/science-formula-sheets/index.html', 'Formula sheets')],
)

SECTIONS = _m2.SECTIONS
FIG_CYL2, MD_CYL2 = _m2.FIG_CYL2, _m2.MD_CYL2
FIG_SANKEY2, MD_SANKEY2 = _m2.FIG_SANKEY2, _m2.MD_SANKEY2

Q = []
def num(id, sec, marks, q, ans, hint, reveal, unit='', tol=0, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='num', q=q, ans=ans, tol=tol, unit=unit, hint=hint, reveal=reveal, fig=fig, figmd=figmd))
def text(id, sec, marks, q, acc, hint, reveal, ph='type your answer', fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='text', q=q, acc=acc, ph=ph, hint=hint, reveal=reveal, fig=fig, figmd=figmd))
def mc(id, sec, marks, q, right, wrong, pos, hint, why, fig=None, figmd=None):
    """Multiple choice: put `right` at letter `pos`; the three wrong options fill the other slots in order."""
    L = 'abcd'; w = list(wrong); opts = []
    for i in range(4):
        opts.append(right if L[i] == pos else w.pop(0))
    Q.append(dict(id=id, sec=sec, marks=marks, kind='mcq', q=q, opts=opts, correct=pos, hint=hint,
                  reveal=f'{pos.upper()} &mdash; {why}', fig=fig, figmd=figmd))

# ---- A: atoms
num('q1','at',1,'A sodium atom has atomic number 11 and mass number 23. How many neutrons does it have?',12,
    'Mass number counts protons and neutrons together.','23 &minus; 11 = 12 neutrons.')
text('q2','at',1,'Chlorine has atomic number 17. Write its electronic structure (for example 2,8,1).',
    ['2,8,7','2.8.7','2, 8, 7','2 8 7','2-8-7'],'Fill the shells in order: 2, then 8, then the rest.',
    '2,8,7: 2 + 8 = 10, leaving 7 in the third shell.', ph='e.g. 2,8,1')
mc('q3','at',1,'An element has the electronic structure 2,8,3. Where is it in the periodic table?',
   'Group 3, Period 3',['Group 2, Period 3','Group 3, Period 2','Group 8, Period 3'],'b',
   'The number of electrons in the outer shell gives the group; the number of shells gives the period.',
   'The outer shell has 3 electrons (Group 3) and there are 3 shells in use (Period 3).')

# ---- B: bonding
text('q4','bo',1,'Calcium forms Ca&sup2;&#8314; ions and fluorine forms F&#8315; ions. Write the formula of calcium fluoride.',
    ['CaF2','CaF₂','caf2'],'Balance one 2+ charge against 1&minus; charges.',
    'CaF₂: one 2+ ion needs two 1&minus; ions to make the charges total zero.', ph='e.g. MgCl2')
mc('q5','bo',1,'A substance is shiny, has a high melting point and conducts electricity both as a solid and as a liquid. What type of structure does it have?',
   'Giant metallic',['Giant ionic','Simple molecules','Giant covalent, like diamond'],'d',
   'Which type has free electrons that can carry a current even in the solid?',
   'Metals conduct as solids because of delocalised electrons. Ionic solids cannot conduct until melted, simple molecules never conduct, and diamond has no free electrons.')
num('q6','bo',1,'An oxygen molecule is O=O, a double bond. How many pairs of electrons are shared between the two atoms?',2,
    'A double bond is made of how many pairs?','A double bond shares 2 pairs of electrons.')
mc('q7','bo',2,'Diamond has a very high melting point. Why?',
   'Every carbon atom is joined to four others by strong covalent bonds all through the structure',
   ['The forces between its molecules are weak but there are many of them','It contains delocalised electrons that hold it together','It is made of positive and negative ions that attract each other'],'a',
   'Is diamond made of separate molecules, or one big network?',
   'Diamond is one giant network of strong covalent bonds, and a lot of energy is needed to break them. It has no separate molecules, no ions and no free electrons.')

# ---- C: photosynthesis
text('q8','pp',1,'Which green pigment in the chloroplasts absorbs light for photosynthesis?',
    ['chlorophyll'],'It is what makes leaves green.','Chlorophyll.', ph='one word')
mc('q9','pp',1,'A plant grown without magnesium has yellow leaves. Why?',
   'Magnesium is needed to make chlorophyll',
   ['Magnesium is needed to make starch directly','Magnesium is a gas the plant takes from the air','Magnesium is needed to build cell walls'],'c',
   'Which green substance contains magnesium?',
   'Magnesium goes into chlorophyll. Without it the leaves cannot make enough chlorophyll, so they turn yellow and photosynthesise less.')
num('q10','pp',2,'A farmer&rsquo;s wheat yield rises from 8.0 tonnes to 9.2 tonnes after adding fertiliser. What is the percentage increase?',15,
    'Percentage increase = increase &divide; original &times; 100.',
    '9.2 &minus; 8.0 = 1.2. 1.2 &divide; 8.0 &times; 100 = 15%.', unit='%', tol=0.5)

# ---- D: transport and carbon cycle
text('q11','tr',1,'Which tissue carries water and minerals up from the roots to the leaves?',
    ['xylem','the xylem'],'Hollow tubes of dead cells.','The xylem.', ph='one word')
mc('q12','tr',1,'Which set of conditions makes a plant lose water <strong>fastest</strong> by transpiration?',
   'Hot, windy and dry',['Cool, still and humid','Cool, windy and humid','Hot, still and humid'],'a',
   'Think about what makes a puddle dry up quickly.',
   'Heat, wind and dry air all speed up evaporation from the leaf, so the plant loses water fastest.')
mc('q13','tr',1,'Which of these processes does <strong>not</strong> put carbon dioxide into the air?',
   'Photosynthesis',['Respiration','Combustion of fuels','Decomposition'],'d',
   'One of them takes carbon dioxide out of the air.',
   'Photosynthesis takes carbon dioxide out of the air. Respiration, combustion and decomposition all put it back.')

# ---- E: human biology
text('q14','hb',1,'Which organ turns spare amino acids into urea?',
    ['liver','the liver'],'It is the large organ on the right of the abdomen.','The liver.', ph='one word')
mc('q15','hb',1,'Which tube carries urine from the bladder out of the body?',
   'Urethra',['Ureter','Renal vein','Umbilical cord'],'b',
   'The ureter leads <em>to</em> the bladder.',
   'The urethra carries urine out of the bladder. The ureters carry it from the kidneys to the bladder.')
num('q16','hb',1,'A human skin cell has 46 chromosomes. How many chromosomes are in a human egg cell?',23,
    'Gametes have half the usual number.','Half of 46 is 23.')
mc('q17','hb',1,'What decides whether a baby is a boy or a girl?',
   'Whether the sperm that fertilises the egg carries an X or a Y',
   ['Whether the egg carries an X or a Y','The mother&rsquo;s diet during pregnancy','Whether the baby has 23 or 46 chromosomes'],'c',
   'Which parent can supply a Y chromosome?',
   'Every egg carries X, but a sperm carries X or Y. An X sperm gives a girl (XX) and a Y sperm gives a boy (XY).')
mc('q18','hb',2,'Why is it dangerous for a pregnant woman to drink alcohol?',
   'Alcohol passes across the placenta into the fetus&rsquo;s blood and can harm its development',
   ['Alcohol stops the placenta from forming','Alcohol makes the amniotic fluid too thin','Alcohol cannot reach the fetus but harms her kidneys instead'],'d',
   'Think about what can cross the placenta.',
   'Harmful substances such as alcohol cross the placenta, even though the two bloods never mix, and can damage the fetus as it develops.')

# ---- F: density
num('q19','de',2,'A block measures 10 cm &times; 4 cm &times; 2 cm and has a mass of 240 g. What is its density?',3,
    'Find the volume first, then divide the mass by it.','V = 10 &times; 4 &times; 2 = 80 cm&sup3;, so &rho; = 240 &divide; 80 = 3 g/cm&sup3;.', unit='g/cm³', tol=0.05)
num('q20','de',2,'The small metal object in the diagram has a mass of 120 g. Use the diagram to find its density.',8,
    'First find its volume from the rise in water level.','Volume = 75 &minus; 60 = 15 cm&sup3;. &rho; = 120 &divide; 15 = 8 g/cm&sup3;.', unit='g/cm³', tol=0.05, fig=FIG_CYL2, figmd=MD_CYL2)
mc('q21','de',1,'Wood has a density of 0.6 g/cm&sup3; and water has a density of 1.0 g/cm&sup3;. What happens to a piece of wood placed in water?',
   'It floats',['It sinks','It dissolves','It hangs in the middle'],'a',
   'Compare the two densities.','The wood is less dense than water, so it floats.')

# ---- G: sound
num('q22','wa',1,'A sound wave has a frequency of 250 Hz. What is its period?',0.004,
    'T = 1 &divide; f.','T = 1 &divide; 250 = 0.004 s.', unit='s', tol=1e-6)
mc('q23','wa',1,'Sound is a longitudinal wave. What does that mean?',
   'The vibrations are along the direction the wave travels',
   ['The vibrations are at right angles to the direction of travel','The wave carries matter from the source to the listener','The wave can travel through a vacuum'],'c',
   'Think of a slinky being pushed and pulled along its length.',
   'In a longitudinal wave the particles vibrate backwards and forwards along the direction of travel, making compressions and rarefactions.')
mc('q24','wa',2,'Two loudspeakers play the same note, but at one spot in the room the sound is very quiet. What is the best explanation?',
   'The crest of one wave meets the trough of the other there, so they cancel (destructive interference)',
   ['The two waves meet crest to crest there, so they add up','The frequency of the note drops at that spot','The air at that spot absorbs all the energy of the sound'],'b',
   'What happens when a crest meets a trough?',
   'Waves that arrive out of step cancel each other out. This is destructive interference, so the sound is quiet.')

# ---- H: thermal energy
mc('q25','th',1,'A saucepan has a metal base and a plastic handle. Why?',
   'Metal is a good conductor, so heat reaches the food; plastic is a poor conductor, so the handle stays cooler',
   ['Metal is a good insulator, so heat stays in the pan','Plastic conducts heat better, so the handle warms up evenly','Metal radiates heat upward and plastic reflects it'],'d',
   'Which material do you want to carry heat, and which to block it?',
   'Metal conducts the heat from the cooker to the food. Plastic is an insulator, so the handle stays safe to hold.')
num('q26','th',2,'Use the Sankey diagram for the motor. What percentage of the input energy becomes useful kinetic energy?',62.5,
    'Useful &divide; total input &times; 100.','500 &divide; 800 &times; 100 = 62.5%.', unit='%', tol=0.05, fig=FIG_SANKEY2, figmd=MD_SANKEY2)
text('q27','th',1,'Warm water rises in a saucepan and cooler water sinks to replace it. What is this method of heat transfer called?',
    ['convection'],'It happens in liquids and gases.','Convection.', ph='one word')

# ---- I: electricity
num('q28','el',2,'A 15 &Omega; resistor is connected across a 6 V battery. What current flows through it?',0.4,
    'I = V &divide; R.','I = 6 &divide; 15 = 0.4 A.', unit='A', tol=0.001)
mc('q29','el',1,'Two lamps are connected in <strong>parallel</strong> to a battery. One lamp breaks. What happens to the other?',
   'It stays lit',['It goes out','It gets dimmer','It gets much brighter and then burns out'],'a',
   'Does the other lamp still have a complete loop?',
   'Each branch of a parallel circuit has its own loop and the full voltage, so the other lamp keeps working.')
mc('q30','el',1,'How should a voltmeter be connected to measure the voltage across a lamp?',
   'In parallel with the lamp',['In series with the lamp','In series with the battery only','Either way, it makes no difference'],'c',
   'A voltmeter compares the two sides of a component.',
   'A voltmeter goes across (in parallel with) the component. An ammeter is the one connected in series.')

WRITTEN = [
  (31, 4, 'Draw dot-and-cross diagrams to show how a lithium atom (2,1) and a fluorine atom (2,7) form ions. Show the electron arrangement and the charge on each ion, then write the formula of the compound.',
   'Li&#8314; drawn as 2 electrons with the outer electron gone [1]; F&#8315; drawn as 2,8 with the gained electron shown in a different symbol [1]; charges + and &minus; shown in square brackets [1]; formula LiF, because one 1+ balances one 1&minus; [1].'),
  (32, 4, 'A motor takes in 600 J of electrical energy and lifts a load, gaining 420 J of useful energy. Use the idea of conservation of energy to say what happens to the other 180 J, and calculate how efficient the motor is.',
   'Energy is never created or destroyed [1]; the other 180 J is transferred as wasted energy, mainly heat (and some sound), which spreads into the surroundings [1]; efficiency = useful &divide; total [1] = 420 &divide; 600 = 70% [1].'),
  (33, 4, 'Explain how the fetus gets oxygen and food from its mother and how its waste is removed. Why can harmful substances still reach the fetus even though the two blood supplies do not mix?',
   'Oxygen and nutrients diffuse from the mother&rsquo;s blood into the fetus&rsquo;s blood across the placenta [1]; carbon dioxide and urea diffuse back the other way and the mother&rsquo;s body removes them [1]; the umbilical cord carries the blood between the fetus and placenta [1]; the placenta is thin and lets small molecules through, so alcohol, nicotine and some viruses can cross too [1].'),
]
