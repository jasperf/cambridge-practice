"""Spec: Secondary 2 · Semester 1 science — Mock Paper 2, the combined paper.

Build with:  python3 scripts/build_review_sheet.py scripts/review_specs/s2_sem1_science_mock2_combined.py

A second full mock for the Semester 1 assessment, wider than mock 1: it folds in
every topic on the SA revision list, including the ones only the gaps drill and
the t2/w7 unit tests cover — the excretory system, absorption, transport and
transpiration, the carbon cycle, conservation of energy, simple versus giant
structures, and chromosomes, genes and inheritance. All questions are new; none
repeats mock 1, the review page, the bonding drill or the gaps drill.
"""

META = dict(
    out='s2/sem1/mocks/sem1-science-mock2-combined',
    title='Science Mock Paper 2 &middot; Combined',
    badge='Science &middot; Semester 1 Mock 2',
    eyebrow='Secondary 2 &middot; Science &middot; Semester 1 assessment &middot; second paper',
    h1='Science Mock 2<br><em>Everything, combined</em>',
    intro=('A second Semester 1 mock that combines every topic on the revision list: atoms, bonding and '
           'giant structures, photosynthesis, transport and the carbon cycle, the excretory system, '
           'chromosomes and inheritance, fetal development and the mother&rsquo;s health, density, sound and '
           'interference, thermal energy and conservation of energy, and electricity with circuit symbols. The questions are all new, so take mock 1 first. Use <strong>Cover the notes</strong> '
           'and try each section cold before reading its key facts.'),
    md_title='Secondary 2 · Science — Semester 1 Mock Paper 2 (Combined)',
    md_intro=('A second full practice paper for the Semester 1 assessment, combining every topic on the '
              'revision list — including the ones only the gaps drill covers: the excretory system, plant '
              'transport, the carbon cycle, conservation of energy, simple versus giant structures, and '
              'chromosomes and inheritance, fetal development and the mother’s health, and interference of '
              'sound. All questions are new. Q1–Q52 match the interactive sheet; '
              'Q53–Q58 are written questions marked by the teacher. Allow about 80 minutes for Q1–Q52 '
              'and 30 minutes for the written questions. Diagrams are described in words.'),
    time_chip='About 80 minutes &middot; a calculator helps',
    storage_key='sem1-science-mock2-combined',
    back='index.html',
    answers_note=('Answers for Q1–Q52 (auto-marked on the interactive sheet) and a marking guide for the '
                  'written questions Q53–Q58. Keep this separate from the question sheet.'),
    extra_links=[('./sem1-science-mock.html', 'Mock paper 1'),
                 ('./sem1-science-revision.html', 'Terms 1–2 review'),
                 ('./sem1-science-gaps.html', 'Gaps drill'),
                 ('../../reference/science-formula-sheets/index.html', 'Formula sheets')],
)

T1W2 = '../t1/w2/term1-week2-atomic-structure-periodic.html'
T1W7 = '../t1/w7/term1-week7-science-unit-test2-plant-biology.html'
T2W4D = '../t2/w4/term2-week4-science-unit3-density.html'
T2W4S = '../t2/w4/term2-week4-science-unit3-sound-thermal-energy.html'
T2W4E = '../t2/w4/term2-week4-science-unit3-electricity.html'
T2W7 = '../t2/w7/term2-week7-science-unit-test-electricity-human-biology.html'

SECTIONS = [
  dict(key='at', icon='&#9883;', color='var(--accent-math)', rgba='79,142,247',
       title='Atoms &amp; the Periodic Table', label='Atoms & Periodic Table',
       src='Chemical structures &amp; properties', link=T1W2,
       facts=[
         ('Inside an atom', 'Protons (+1) and neutrons (no charge) in the nucleus; electrons (&minus;1) in shells around it. In a neutral atom, electrons = protons.'),
         ('Two numbers', '<span class="f">atomic number = protons</span><br><span class="f">mass number = protons + neutrons</span>'),
         ('Filling shells', 'For the first 20 elements the shells hold <span class="f">2, 8, 8, 2</span>. Phosphorus (15) is 2,8,5: 2 + 8 + 5.'),
         ('Reading the table', 'Group = electrons in the outer shell. Period = shells in use. Ions have full outer shells, so count their electrons before working out numbers.'),
         ('Trends', 'Group 1 metals lose their outer electron and are more reactive going <em>down</em>. Group 7 non-metals gain one electron and are less reactive going down.'),
       ]),
  dict(key='bo', icon='&#128279;', color='var(--accent-math)', rgba='79,142,247',
       title='Bonding &amp; Chemical Structures', label='Bonding & Structures',
       src='Chemical bonding &middot; giant structures', link='./sem1-science-bonding-ions.html',
       facts=[
         ('Ionic bonding', 'Metal + non-metal. Electrons move from metal to non-metal; the opposite charges attract. Groups 1/2/3 form 1+/2+/3+ ions; Groups 5/6/7 form 3&minus;/2&minus;/1&minus;.'),
         ('Naming ionic compounds', 'Metal first, then the non-metal with its name changed: <em>lithium bromide</em>, <em>calcium chloride</em>.'),
         ('Writing formulae', 'Total + = total &minus;. Al&sup3;&#8314; and O&sup2;&#8315; give <span class="f">Al&#8322;O&#8323;</span>; Li&#8314; and Br&#8315; give LiBr.'),
         ('Covalent bonding', 'Non-metal + non-metal share pairs of electrons. A single bond = 1 pair, a double bond = 2 pairs. In CO&#8322; the carbon makes two double bonds.'),
         ('Metallic bonding', 'Positive ions in a sea of <span class="f">delocalised electrons</span> — which is what carries a current.'),
         ('Simple vs giant', 'Simple molecules (H&#8322;O, CH&#8324;) have weak forces <em>between</em> molecules and low melting points. Giant covalent structures (diamond, graphite, SiO&#8322;) have strong bonds throughout, so very high melting points. Graphite has one free electron per atom and weak forces between its sheets.'),
       ]),
  dict(key='pp', icon='&#127807;', color='var(--accent-sci)', rgba='62,207,142',
       title='Photosynthesis &amp; Minerals', label='Photosynthesis & Minerals',
       src='Plant biology', link=T1W7,
       facts=[
         ('The equation', '<span class="f">carbon dioxide + water &rarr; glucose + oxygen</span>, with light energy absorbed by chlorophyll in the <em>chloroplasts</em>.'),
         ('Uses of glucose', 'Respiration, and turned into <em>starch</em> (storage), <em>cellulose</em> (cell walls), proteins and fats and oils.'),
         ('Minerals', 'Magnesium goes into chlorophyll; nitrate makes protein. Fertiliser raises the yield.'),
         ('Starch test', 'Boil the leaf in water, warm it in ethanol (to remove the green colour), rinse, add iodine: <span class="f">blue-black = starch is present</span>.'),
         ('Light investigation', 'Pondweed bubbles oxygen faster with more light: move the lamp closer and count the bubbles per minute, keeping everything else the same.'),
       ]),
  dict(key='tr', icon='&#128167;', color='var(--accent-sci)', rgba='62,207,142',
       title='Transport, Transpiration &amp; the Carbon Cycle', label='Transport & Carbon Cycle',
       src='Plant biology &middot; gap topic', link='./sem1-science-gaps.html',
       facts=[
         ('Xylem', 'Hollow tubes of dead cells carrying <span class="f">water and minerals up</span> from the roots.'),
         ('Phloem', 'Tubes of living cells carrying <span class="f">dissolved sugar</span> from the leaves to wherever it is needed, up or down.'),
         ('Transpiration', 'Water evaporates inside the leaf and leaves as vapour through the <em>stomata</em>. Root hairs take water in by osmosis; the xylem stream pulls more water up.'),
         ('Stomata', 'Opened and closed by guard cells. Faster water loss when it is hotter, windier, drier and brighter. Many close in the dark.'),
         ('Carbon cycle', 'Photosynthesis takes carbon dioxide <em>out</em> of the air. Respiration, decomposition (by bacteria and fungi) and combustion put it <em>back</em>. Feeding passes carbon along food chains; fossil fuels store it.'),
       ]),
  dict(key='hb', icon='&#129516;', color='var(--accent-math)', rgba='79,142,247',
       title='Human Biology: Excretion &amp; Inheritance', label='Human Biology',
       src='Human biology &middot; gap topic', link=T2W7,
       facts=[
         ('Excretion', 'Removing waste made by the body&rsquo;s own cells. The lungs excrete CO&#8322;; the <strong>liver</strong> turns spare amino acids into <strong>urea</strong>; the kidneys put urea into urine.'),
         ('Urinary system', 'Kidneys filter blood (renal artery in, renal vein out) &rarr; each kidney&rsquo;s urine goes down a <em>ureter</em> to the <em>bladder</em>, out through the <em>urethra</em>.'),
         ('Nephrons', 'Filter everything except cells and protein, then take back <em>all the glucose</em>, most water and the salts the body needs.'),
         ('DNA, genes, chromosomes', 'DNA is the twisted-ladder molecule; a <span class="f">gene</span> is a section that codes for one feature; genes sit on <span class="f">chromosomes</span> in the nucleus.'),
         ('Pregnancy', 'The fetus grows in the uterus, cushioned by amniotic fluid, and is joined to the <span class="f">placenta</span> by the <em>umbilical cord</em>. Oxygen and nutrients pass from the mother&rsquo;s blood to the fetus&rsquo;s blood, and carbon dioxide and urea pass back. The bloods never mix, but harmful substances (nicotine, carbon monoxide, alcohol, some viruses) can cross too.'),
         ('Inheritance', 'Body cells have 46 chromosomes (23 pairs). <em>Meiosis</em> makes gametes with 23 each. Egg always carries X; sperm carries X or Y, so the <span class="f">sperm decides the sex</span>: XX girl, XY boy — a 50/50 chance.'),
       ]),
  dict(key='de', icon='&#129482;', color='var(--accent-warn)', rgba='245,166,35',
       title='Density', label='Density',
       src='Chemical structures &middot; properties', link=T2W4D,
       facts=[
         ('The formula', '<span class="f">&rho; = m &divide; V</span>, rearranged to m = &rho; &times; V and V = m &divide; &rho;.'),
         ('Volumes', 'Regular block: l &times; w &times; h. Odd object: drop it in a measuring cylinder; the rise in mL is its volume in cm&sup3; (1 mL = 1 cm&sup3;).'),
         ('Units', '<span class="f">1 g/cm&sup3; = 1000 kg/m&sup3;</span>. Water is 1 g/cm&sup3;.'),
         ('Float or sink', 'Less dense than the liquid: floats. Denser: sinks. A solid can float on a denser liquid (iron floats on mercury).'),
         ('Heating', 'Particles spread out: mass unchanged, volume bigger, so <span class="f">density falls</span> — which is why warm air rises.'),
       ]),
  dict(key='wa', icon='&#127925;', color='var(--accent-warn)', rgba='245,166,35',
       title='Sound &amp; Waves', label='Sound & Waves',
       src='Sound', link=T2W4S,
       facts=[
         ('Two kinds of wave', 'Transverse: vibrations at right angles to travel (light, water ripples). Longitudinal: vibrations along the direction of travel (sound: compressions and rarefactions).'),
         ('Measurements', 'Amplitude: middle line to a crest. Wavelength: crest to crest. Frequency: waves per second, in Hz.'),
         ('Period', '<span class="f">T = 1 &divide; f</span>. A wave with period 0.005 s has f = 1 &divide; 0.005 = 200 Hz.'),
         ('Loud and quiet', 'Bigger amplitude = louder. Higher frequency = higher pitch.'),
         ('Superposition', 'Crest meets crest: add. Crest meets trough: subtract or cancel.'),
         ('Interference', 'Two waves meeting add up. In step (crest with crest): <span class="f">constructive</span>, a bigger wave and a louder sound. Out of step (crest with trough): <span class="f">destructive</span>, they cancel and the sound gets quieter.'),
       ]),
  dict(key='th', icon='&#128293;', color='var(--accent-warn)', rgba='245,166,35',
       title='Thermal Energy &amp; Conservation', label='Thermal Energy',
       src='Thermal energy', link=T2W4S,
       facts=[
         ('Heat flows hot &rarr; cold', 'Temperature is the average energy of the particles; thermal energy is the total and depends on mass too.'),
         ('Three transfers', 'Conduction: particle to particle, best in metals. Convection: warm liquid or gas rises, cool sinks. Radiation: infrared needs no particles, so it crosses empty space.'),
         ('Evaporation', 'The fastest particles escape from a surface at any temperature, cooling what is left behind.'),
         ('Conservation of energy', '<span class="f">Energy is never created or destroyed</span> — only transferred. energy in = useful out + wasted out, and the waste ends up heating the surroundings.'),
         ('Sankey diagrams', 'The arrow widths show the amounts. Everything out must add up to what went in.'),
       ]),
  dict(key='el', icon='&#9889;', color='var(--accent-warn)', rgba='245,166,35',
       title='Electricity', label='Electricity',
       src='Electricity', link=T2W4E,
       facts=[
         ('Ohm&rsquo;s law', '<span class="f">V = I &times; R</span>, so I = V &divide; R and R = V &divide; I. Volts, amps, ohms.'),
         ('Series', 'One loop, same current everywhere, voltages add, <span class="f">R = R&#8321; + R&#8322;</span>. Break anywhere and everything stops.'),
         ('Parallel', 'Each branch gets the full voltage; branch currents add up. A break in one branch leaves the others working.'),
         ('Circuit symbols', 'Cell: a long and a short line. Switch: a gap with a lever. Lamp: a circle with a cross. Resistor: a rectangle. Ammeter: a circle with A. Voltmeter: a circle with V.'),
         ('Meters', 'Ammeter in <em>series</em>; voltmeter in <em>parallel</em> across the component.'),
       ]),
]

# ---------------------------------------------------------------- figures

MONO = 'font-family="DM Mono, monospace"'

FIG_CYL2 = ('<svg class="q-fig" viewBox="0 0 280 210" role="img" aria-label="Two measuring cylinders: water at 60 mL, '
            'then at 75 mL with a small metal object inside" style="max-width:300px">'
            '<path class="draw" d="M50 30 V185 H110 V30" stroke="#7a84a0" stroke-width="2" fill="none" pathLength="1"/>'
            '<rect class="fill" x="52" y="94" width="56" height="90" fill="rgba(79,142,247,0.35)"/>'
            '<path class="draw" d="M50 94 H64" stroke="#4f8ef7" stroke-width="2" fill="none" pathLength="1"/>'
            '<text x="80" y="200" font-size="12" fill="#7a84a0" text-anchor="middle" ' + MONO + '>before</text>'
            '<text x="22" y="98" font-size="12" fill="#e8eaf0" text-anchor="middle" ' + MONO + '>60</text>'
            '<path class="draw" d="M170 30 V185 H230 V30" stroke="#7a84a0" stroke-width="2" fill="none" pathLength="1"/>'
            '<rect class="fill" x="172" y="70" width="56" height="114" fill="rgba(79,142,247,0.35)"/>'
            '<path class="draw" d="M170 70 H184" stroke="#4f8ef7" stroke-width="2" fill="none" pathLength="1"/>'
            '<path class="draw" d="M192 150 h16 M200 150 v10 M196 150 a5 5 0 1 1 6 0" stroke="#f5a623" stroke-width="3" fill="none" pathLength="1"/>'
            '<text x="200" y="200" font-size="12" fill="#7a84a0" text-anchor="middle" ' + MONO + '>after</text>'
            '<text x="256" y="74" font-size="12" fill="#e8eaf0" text-anchor="middle" ' + MONO + '>75</text>'
            '<text x="140" y="20" font-size="11" fill="#7a84a0" text-anchor="middle" ' + MONO + '>readings in mL</text></svg>')
FIG_SYM = ('<svg class="q-fig" viewBox="0 0 300 120" role="img" aria-label="Two circuit symbols on a wire: X is a circle '
           'with a cross inside, Y is a circle with the letter V inside" style="max-width:320px">'
           '<path class="draw" d="M10 55 H58 M102 55 H178 M222 55 H290" stroke="#7a84a0" stroke-width="2" fill="none" pathLength="1"/>'
           '<circle class="fill" cx="80" cy="55" r="22" stroke="#e8eaf0" stroke-width="2" fill="none"/>'
           '<path class="draw" d="M64 39 L96 71 M96 39 L64 71" stroke="#e8eaf0" stroke-width="2" fill="none" pathLength="1"/>'
           '<text x="80" y="100" font-size="14" fill="#f5a623" text-anchor="middle" ' + MONO + '>X</text>'
           '<circle class="fill" cx="200" cy="55" r="22" stroke="#e8eaf0" stroke-width="2" fill="none"/>'
           '<text x="200" y="56" font-size="18" fill="#e8eaf0" text-anchor="middle" dominant-baseline="central" ' + MONO + '>V</text>'
           '<text x="200" y="100" font-size="14" fill="#f5a623" text-anchor="middle" ' + MONO + '>Y</text></svg>')
MD_SYM = 'Part of a circuit diagram: symbol X is a circle with a cross inside it; symbol Y is a circle with the letter V inside it.'

MD_CYL2 = 'A measuring cylinder reads 60 mL before a small metal object goes in and 75 mL after.'

FIG_SANKEY2 = (
    '<svg class="q-fig" viewBox="0 0 380 230" role="img" aria-label="Sankey diagram for an electric motor: '
    '800 J electrical in; 500 J kinetic straight on; 240 J heat and an unknown amount of sound bend downwards" '
    'style="max-width:380px">'
    '<path class="draw" d="M20 90 H150" stroke="#4f8ef7" stroke-width="100" fill="none" pathLength="1" opacity="0.85"/>'
    '<path class="draw" d="M150 72 H300" stroke="#3ecf8e" stroke-width="66" fill="none" pathLength="1" opacity="0.85"/>'
    '<polygon class="fill" points="300,39 340,72 300,105" fill="#3ecf8e" opacity="0.85"/>'
    '<path class="draw" d="M150 121 H180 Q 214 121 214 154 V188" stroke="#f5a623" stroke-width="30" fill="none" '
    'pathLength="1" opacity="0.85"/>'
    '<polygon class="fill" points="199,188 229,188 214,206" fill="#f5a623" opacity="0.85"/>'
    '<path class="draw" d="M150 141 Q 160 141 160 152 V192" stroke="#e8a090" stroke-width="8" fill="none" pathLength="1"/>'
    '<polygon class="fill" points="156,192 164,192 160,202" fill="#e8a090"/>'
    '<text x="85" y="86" font-size="12" fill="#0f1117" text-anchor="middle" dominant-baseline="central" ' + MONO + '>Electrical</text>'
    '<text x="85" y="102" font-size="12" fill="#0f1117" text-anchor="middle" dominant-baseline="central" ' + MONO + '>800 J</text>'
    '<text x="234" y="70" font-size="12" fill="#0f1117" text-anchor="middle" dominant-baseline="central" ' + MONO + '>Kinetic 500 J</text>'
    '<text x="238" y="172" font-size="12" fill="#e8eaf0" text-anchor="start" dominant-baseline="central" ' + MONO + '>Heat 240 J</text>'
    '<text x="146" y="224" font-size="12" fill="#e8eaf0" text-anchor="end" dominant-baseline="central" ' + MONO + '>Sound ? J</text>'
    '</svg>')
MD_SANKEY2 = ('A Sankey diagram for an electric motor. Input: 800 J electrical. Straight on: 500 J kinetic. '
              'Bending downwards: 240 J heat, and a thin arrow labelled "Sound ? J".')

# ---------------------------------------------------------------- questions

Q = []
def num(id, sec, marks, q, ans, hint, reveal, unit='', tol=0, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='num', q=q, ans=ans, tol=tol, unit=unit, hint=hint, reveal=reveal, fig=fig, figmd=figmd))
def text(id, sec, marks, q, acc, hint, reveal, ph='type your answer', fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='text', q=q, acc=acc, ph=ph, hint=hint, reveal=reveal, fig=fig, figmd=figmd))
def mcq(id, sec, marks, q, opts, correct, hint, reveal, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='mcq', q=q, opts=opts, correct=correct, hint=hint, reveal=reveal, fig=fig, figmd=figmd))

# ---- A: atoms & the periodic table
num('s1','at',1,'A calcium atom has atomic number 20 and mass number 40. How many neutrons are in its nucleus?',20,
    'The mass number counts protons and neutrons together.','40 − 20 = 20 neutrons')
text('s2','at',1,'Phosphorus has atomic number 15. Write its electronic structure (for example 2,8,1).',
    ['2,8,5','2.8.5','2, 8, 5','2 8 5','2-8-5'],'Fill the shells in order: 2, then 8, then the rest.',
    '2,8,5: 2 + 8 = 10 in the first two shells, leaving 5 in the third.', ph='e.g. 2,8,1')
num('s3','at',1,'An oxygen atom (atomic number 8) gains two electrons to become an oxide ion, O&sup2;&#8315;. How many <strong>electrons</strong> does the ion have altogether?',10,
    'Start from the number of electrons in the atom, then add what it gained.',
    'The atom has 8 electrons; the ion gains 2 more, so 10 electrons — a full 2,8 shell.')
mcq('s4','at',2,'Which of these metals is the <strong>most</strong> reactive?',
    ['Magnesium — Group 2, Period 3','Sodium — Group 1, Period 3','Potassium — Group 1, Period 4','Calcium — Group 2, Period 4'],'c',
    'Group 1 metals lose their outer electron more easily than Group 2 metals, and it gets easier further down.',
    'C — Potassium loses its single outer electron most easily: it is in Group 1, one period below sodium, so its outer electron is further from the nucleus and leaves more readily.')

# ---- B: bonding & structures
text('s5','bo',1,'What is the name of the compound made from lithium ions (Li&#8314;) and bromide ions (Br&#8315;)?',
    ['lithium bromide'],'Metal first, then the non-metal with its name changed.',
    'Lithium bromide (LiBr).', ph='two words')
mcq('s6','bo',1,'Which of these substances is held together by <strong>ionic</strong> bonds?',
    ['Sodium chloride (NaCl)','Methane (CH&#8324;)','Water (H&#8322;O)','Oxygen (O&#8322;)'],'a',
    'Which one is a metal joined to a non-metal?',
    'A — Sodium is a metal and chlorine a non-metal, so electrons are transferred and the opposite charges attract. The others are covalent molecules.')
num('s7','bo',1,'In carbon dioxide, O=C=O, the carbon atom makes a <strong>double</strong> bond to each oxygen. How many <strong>pairs</strong> of electrons are shared in total?',4,
    'Each double bond is two shared pairs, and there are two double bonds.',
    '2 bonds × 2 pairs = 4 shared pairs of electrons.')
text('s8','bo',1,'Aluminium forms Al&sup3;&#8314; ions and oxygen forms O&sup2;&#8315; ions. Write the formula of aluminium oxide.',
    ['Al2O3','Al₂O₃','al2o3'],'Balance 3+ charges against 2− charges.',
    'Al₂O₃: two 3+ ions give 6+; three 2− ions give 6−.', ph='e.g. MgCl2')
mcq('s9','bo',2,'Substance X boils at 56 &deg;C. It does not conduct electricity, as a solid or as a liquid. What kind of structure does X have?',
    ['A giant covalent structure','A giant ionic lattice','A giant metallic lattice','Simple molecules'],'d',
    'Only one kind of structure melts and boils at low temperatures. What does that say about the forces between its particles?',
    'D — Simple molecules have weak forces between the molecules, so they boil low. Giant structures (covalent, ionic or metallic) all have strong bonds throughout and high melting points.')
mcq('s10','bo',2,'Graphite feels slippery and is used as a lubricant in locks and hinges. Why?',
    ['The bonds inside each sheet of atoms break very easily.','The bonds inside each sheet are strong, but the forces holding one sheet to the next are weak, so the sheets slide.','Graphite contains water between its layers.','Graphite is a metal, and metals bend.'],'b',
    'Rubbing graphite makes it feel slippery. What gives way: the sheets themselves, or the packing between them?',
    'B — Each sheet is a strong network of covalent bonds, which is why the sheets stay whole. What gives way is the weak attraction between sheets, so they slide over each other.')

# ---- C: photosynthesis & minerals
text('s11','pp',1,'Plants turn some of the glucose they make into an insoluble carbohydrate for <strong>storage</strong>. What is it called?',
    ['starch'],'It is what the iodine test looks for.',
    'Starch.', ph='one word')
mcq('s12','pp',1,'Fertiliser is added to soil to help a plant grow. Which of these is <strong>not</strong> a mineral ion that fertiliser supplies?',
    ['Nitrate','Magnesium','Potassium','Carbon dioxide'],'d',
    'Three of these are dissolved ions taken in by the roots. One of them is a gas.',
    'D — Plants get their carbon from carbon dioxide in the air, through the leaves, not from the soil. The mineral ions supply nitrogen, magnesium and potassium.')
mcq('s13','pp',1,'A leaf is tested with iodine solution and it turns blue-black. What does that show?',
    ['The leaf contains glucose','The leaf contains starch','The leaf contains chlorophyll','The leaf has no minerals left in it'],'b',
    'What colour does iodine go when it meets starch?',
    "B — Iodine turns blue-black with starch, so the leaf has been photosynthesising and storing the glucose as starch.")
mcq('s14','pp',1,'Two identical tubes of pondweed are set up in the same water at the same temperature. One stands in bright daylight, the other in a dark box. After an hour the dark tube has produced no bubbles. Why?',
    ['The pondweed in the dark has stopped respiring','Bubbles only come from warm water','Without light the pondweed cannot photosynthesise, so it makes no oxygen','Dark water dissolves the bubbles'],'c',
    'What does the pondweed need from the light, and what gas do the bubbles contain?',
    'C — The bubbles are oxygen made by photosynthesis. Light is the energy source, so in the dark no photosynthesis happens and no oxygen is made.')
num('s15','pp',1,'A student counts 36 oxygen bubbles from pondweed in 4 minutes. How many is that per minute?',9,
    'Share the bubbles over the minutes.','36 ÷ 4 = 9 bubbles per minute', unit='per minute')
num('s16','pp',2,'A maize field yields 6.0 tonnes without fertiliser. With a nitrate fertiliser the yield is 7.5 tonnes. What is the percentage increase?',25,
    'Percentage increase = increase ÷ original × 100.',
    '7.5 − 6.0 = 1.5. 1.5 ÷ 6.0 × 100 = 25%', unit='%', tol=0.5)

# ---- D: transport, transpiration & carbon cycle
mcq('s17','tr',2,'In spring, a potato plant sends stored sugar from the swollen stem (the potato) up to its new shoots. Which tissue carries the sugar?',
    ['Xylem','Phloem','Both xylem and phloem together','Neither — sugar moves by diffusion'],'b',
    'Which tube carries dissolved sugar — and in which directions?',
    'B — Phloem carries dissolved sugar up and down, from stores to wherever it is needed. Xylem only carries water and minerals upward.')
text('s18','tr',1,'What is the name for the loss of water vapour from the leaves of a plant?',
    ['transpiration','transporation'],'Water out through the stomata, pulling the stream up behind it.',
    'Transpiration.', ph='one word')
mcq('s19','tr',2,'Most plants close their stomata at night. Why does this help them?',
    ['With no light there is no photosynthesis, so open stomata would only lose water','Open stomata let oxygen escape at night','The guard cells shrink in cold air, whether the plant wants it or not','Closing stomata warms the leaf up'],'a',
    'What does a plant take in through open stomata during the day, and what does it lose?',
    'A — In daylight the plant needs carbon dioxide for photosynthesis, so losing water through open stomata is worth it. In the dark there is nothing to gain, so closing the stomata saves water.')
text('s20','tr',1,'Name the process by which plants, animals and decomposers all return carbon dioxide to the air.',
    ['respiration'],'It happens in every living cell, day and night.',
    'Respiration: glucose + oxygen → carbon dioxide + water.', ph='one word')
num('s21','tr',1,'A coal-fired power station releases 9000 tonnes of carbon dioxide in a year. The trees and plants nearby remove 3000 tonnes of it by photosynthesis. How many tonnes are added to the air overall?',6000,
    'Subtract what is taken back out.',
    '9000 − 3000 = 6000 tonnes are added to the air.', unit='tonnes')

# ---- E: human biology — excretion & inheritance
text('s22','hb',1,'Which blood vessel carries the filtered, cleaned blood away from a kidney?',
    ['renal vein','the renal vein','a renal vein'],'Artery in, vein out.',
    'The renal vein. The renal artery brings the blood in to be filtered.', ph='two words')
mcq('s23','hb',2,'Which of these would you normally expect to find in the urine of a healthy person?',
    ['Glucose and protein','Red blood cells and glucose','Water, urea and salts','Protein and red blood cells'],'d',
    'The kidneys take back everything the body still needs. What is left over?',
    'D — Urine is water, urea and the salts the body does not need. Glucose is all taken back, and protein and blood cells are too big to be filtered out in the first place.')
num('s24','hb',1,'A cat has 38 chromosomes in each of its body cells. How many chromosomes are in one cat sperm cell?',19,
    'A gamete carries half the body-cell number.',
    'Half of 38: sperm cells carry 19 chromosomes.')
text('s25','hb',1,'What is the name for a section of DNA that codes for a single feature, such as eye colour?',
    ['gene','a gene','genes'],'One rung-set of the twisted ladder.',
    'A gene.', ph='one word')
mcq('s26','hb',1,'A human egg is fertilised by a sperm carrying a <strong>Y</strong> chromosome. What will the baby be?',
    ['A girl, because the egg always carries X','A boy: his chromosomes will be XY','A girl: her chromosomes will be XY','A boy: his chromosomes will be YY'],'b',
    'What does the egg contribute, and what do X plus Y make?',
    'B — The egg always carries X. X (egg) + Y (sperm) = XY, which is a boy.')
num('s27','hb',2,'About 400 babies are born at a hospital. Given a 50/50 chance for each, roughly how many of them are girls?',200,
    'Half of 400.',
    'About 200 girls (and about 200 boys).')

text('s28','hb',1,'After a baby is born, a midwife clamps and cuts the tube that joined the baby to the placenta. What is this tube called?',
    ['umbilical cord','the umbilical cord','umbilical'],'It is attached at the baby&rsquo;s navel.',
    'The umbilical cord.', ph='two words')
mcq('s29','hb',2,'The blood of a mother and her fetus never mix, yet oxygen still gets from her blood to the fetus. How?',
    ['Blood flows straight from her arteries into the fetus&rsquo;s heart','The fetus breathes in air from the amniotic fluid','Oxygen diffuses across the thin placenta from her blood into the fetus&rsquo;s blood','Oxygen is carried through the amniotic fluid by the uterus wall'],'c',
    'Where do the two blood supplies come close together, and what moves from the higher concentration to the lower?',
    'C — The placenta is a thin exchange surface where the two blood supplies lie side by side, so oxygen diffuses from her blood into the fetus&rsquo;s. The fetus does not breathe air, and the bloods do not mix.')
mcq('s30','hb',2,'A woman smokes throughout her pregnancy. Why is this a risk to her baby?',
    ['The smoke fills the fetus&rsquo;s lungs with tar','Carbon monoxide crosses the placenta and lowers the oxygen the fetus&rsquo;s blood can carry, so the baby may be born small','Nicotine makes the amniotic fluid too thick for the fetus to move','The smoke shortens the umbilical cord'],'b',
    'Think about what passes across the placenta, and what the fetus needs from the mother&rsquo;s blood.',
    'B — Harmful substances in the mother&rsquo;s blood, such as carbon monoxide and nicotine, cross the placenta. Less oxygen reaches the fetus, which slows its growth. The fetus does not breathe in smoke.')

# ---- F: density
num('s31','de',2,'A block of wood measures 5 cm &times; 4 cm &times; 3 cm and has a mass of 90 g. What is its density?',1.5,
    'Find the volume first, then divide the mass by it.',
    'V = 5 × 4 × 3 = 60 cm³, so ρ = 90 ÷ 60 = 1.5 g/cm³.', unit='g/cm³', tol=0.05)
num('s32','de',1,'Use the diagram to find the volume of the small metal object.',15,
    'How far did the water level rise?',
    '75 − 60 = 15 mL, so the volume is 15 cm³.', unit='cm³', tol=0.05, fig=FIG_CYL2, figmd=MD_CYL2)
num('s33','de',1,'Aluminium has a density of 2.7 g/cm&sup3;. What is that in kg/m&sup3;?',2700,
    'One g/cm³ is how many kg/m³?',
    '2.7 × 1000 = 2700 kg/m³', unit='kg/m³')
mcq('s34','de',1,'Iron has a density of 7.9 g/cm&sup3; and mercury is a liquid metal with a density of 13.6 g/cm&sup3;. An iron cube is dropped into a bowl of mercury. What happens?',
    ['It floats','It sinks to the bottom','It dissolves','It hangs exactly in the middle'],'a',
    'Compare the two densities.',
    'A — 7.9 g/cm³ is less than 13.6 g/cm³, so the iron floats, even though it would sink in water.')
mcq('s35','de',2,'On a hot day, the air just above a sun-baked road ripples as it rises. Why does warm air rise?',
    ['Warm air is made of lighter particles than cool air','Warm air is pulled up by the Sun','The road pushes the air away from itself as it expands','The warm air expands, becomes less dense than the cool air around it, and cooler air sinks beneath it and pushes it up'],'d',
    'What happens to the mass of a parcel of air, and to its volume, as it warms?',
    'D — The mass stays the same but the volume grows, so the density falls. Cool, denser air sinks underneath and lifts the warm air — that is convection.')

# ---- G: sound & waves
num('s36','wa',1,'A wave has a period of 0.005 s. What is its frequency?',200,
    'Frequency is 1 divided by the period.',
    'f = 1 ÷ 0.005 = 200 Hz', unit='Hz')
mcq('s37','wa',1,'A student wants to make a note sound <strong>louder</strong> without changing its pitch. What should they change?',
    ['Increase the amplitude of the vibration','Increase the frequency of the vibration','Decrease the wavelength','Make the sound travel faster'],'a',
    'Which measurement decides loudness, and which decides pitch?',
    'A — A bigger amplitude carries more energy, so the note is louder. Frequency decides pitch, so it must stay the same.')
mcq('s38','wa',1,'Which of these travels as a <strong>transverse</strong> wave?',
    ['Sound from a drum','Light from the Sun','The push-and-pull of a slinky sound model','An echo coming back'],'b',
    'Which one vibrates at right angles to its direction of travel?',
    'B — Light vibrates at right angles to the direction it travels. Sound — and its slinky model — is longitudinal.')
num('s39','wa',1,'Two water waves meet. One is a crest of amplitude 3 cm; the other, at the same moment and place, is a trough of amplitude 3 cm. What is the amplitude where they meet?',0,
    'A trough is a crest upside-down. Do they add or subtract?',
    '3 cm up meets 3 cm down: they cancel exactly, so the amplitude is 0.', unit='cm')

mcq('s40','wa',1,'Two loudspeakers play the same note. At one spot in the room the crests of the two sound waves arrive together. What does a listener there hear?',
    ['No sound, because the waves cancel','A higher-pitched note','A louder note of the same pitch','A quieter note of lower pitch'],'c',
    'When two waves are in step, do they add or cancel? And does the frequency change?',
    'C — Waves in step add up, which is constructive interference: a bigger amplitude, so a louder sound. The frequency has not changed, so the pitch is the same.')
mcq('s41','wa',2,'Noise-cancelling headphones listen to the noise around you and play a second sound that is an exact upside-down copy of it. Why does the noise get quieter?',
    ['Where crest meets trough the two waves cancel (destructive interference), so the combined amplitude is smaller','The second sound has a higher frequency, so the ear cannot hear it','The two waves add up and the headphones absorb the extra energy','The headphones lower the pitch of the noise, so it travels more slowly'],'a',
    'An upside-down copy of a wave has a trough exactly where the original has a crest.',
    'A — The copy has a trough wherever the noise has a crest, so the two waves cancel. This is destructive interference: the amplitude drops and the sound is quieter.')

# ---- H: thermal energy & conservation
mcq('s42','th',2,'A metal bench and a wooden bench have BOTH been sitting in the same room for hours, at exactly the same temperature. The metal one feels much colder to sit on. Why?',
    ['Metal is naturally at a lower temperature than wood','Wood stores more heat than metal, so it feels warmer','Wood is at a higher temperature than metal at all times','Metal conducts heat away from your body faster than wood does, so your nerves sense a bigger heat loss'],'d',
    'The two surfaces are at the same temperature, so the difference is in how fast heat leaves <em>you</em>.',
    'D — Conduction: your body loses heat to the metal much faster than to the wood, even at the same temperature. Wood is a poor conductor, so it feels warmer.')
mcq('s43','th',1,'There is almost nothing between the Sun and the Earth. By which method does the Sun&rsquo;s energy still reach us?',
    ['Conduction','Convection','Radiation','Evaporation'],'c',
    'One of these needs no particles at all.',
    'C — Infrared radiation travels through empty space. Conduction and convection both need particles; evaporation is not a way for heat to cross a vacuum.')
text('s44','th',1,'Hand sanitiser dries on your hands and your skin feels cooler. Which process cooled your skin?',
    ['evaporation'],'The liquid particles that escape are the fastest ones.',
    'Evaporation: the fastest particles escape as vapour, taking energy with them, so what is left behind cools.', ph='one word')
num('s45','th',2,'Use the Sankey diagram. How much energy is transferred as <strong>sound</strong>?',60,
    'Everything out must add up to what went in.',
    '800 − 500 − 240 = 60 J of sound.', unit='J', fig=FIG_SANKEY2, figmd=MD_SANKEY2)
num('s46','th',2,'A kettle transfers 2000 J of energy every second. 1600 J of each second heats the water. What <strong>percentage</strong> of the energy is useful?',80,
    'Useful ÷ total × 100.',
    '1600 ÷ 2000 × 100 = 80%', unit='%', tol=0.5)

# ---- I: electricity
num('s47','el',2,'Two resistors, 3 &Omega; and 9 &Omega;, are joined in series with a 12 V battery. What current flows?',1,
    'In series the resistances add. Then use Ohm&rsquo;s law.',
    'R = 3 + 9 = 12 Ω, so I = V ÷ R = 12 ÷ 12 = 1 A.', unit='A', tol=0.01)
num('s48','el',1,'A lamp carries a current of 0.25 A when the voltage across it is 5 V. What is its resistance?',20,
    'Which rearrangement of V = I × R gives R?',
    'R = V ÷ I = 5 ÷ 0.25 = 20 Ω', unit='Ω', tol=0.05)
num('s49','el',1,'Two identical lamps are wired in parallel. The current through each lamp is 0.4 A. What current flows from the battery?',0.8,
    'Branch currents add up.',
    '0.4 + 0.4 = 0.8 A', unit='A', tol=0.01)
mcq('s50','el',1,'Two lamps are wired in <strong>series</strong> with one battery. One lamp&rsquo;s filament breaks. What happens to the other lamp?',
    ['It goes out too — the loop is broken and no current can flow','It stays lit at the same brightness','It glows brighter than before','It flickers on and off'],'a',
    'How many loops does a series circuit have?',
    'A — A series circuit is one single loop. A break anywhere stops the current everywhere — which is one reason houses are wired in parallel.')
mcq('s51','el',1,'Which meter is connected in <strong>series</strong> in a circuit to measure current?',
    ['A voltmeter','Either meter works','An ammeter','A switch, briefly closed'],'c',
    'Which meter needs the current to flow through itself?',
    'C — The ammeter measures the current flowing through it, so it sits in series on the wire. The voltmeter connects across a component, in parallel.')

mcq('s52','el',2,'The diagram shows part of a circuit. Symbol X is a circle with a cross inside it and symbol Y is a circle with the letter V inside it. What are X and Y?',
    ['X is a resistor and Y is an ammeter','X is a cell and Y is a voltmeter','X is a lamp and Y is an ammeter','X is a lamp and Y is a voltmeter'],'d',
    'A cross in a circle is a light source. Which meter is shown by the letter V?',
    'D — A circle with a cross is the symbol for a lamp, and a circle with V is a voltmeter. A resistor is a rectangle, a cell is a long and a short line, and an ammeter has an A in the circle.',
    fig=FIG_SYM, figmd=MD_SYM)

WRITTEN = [
  (53, 4, 'Draw dot-and-cross diagrams to show how a magnesium atom (2,8,2) and an oxygen atom (2,6) form ions. Show the electron arrangement and the charge on each ion, then write the formula of the compound.',
   'Mg²⁺ drawn as 2,8 with both outer electrons gone [1]; O²⁻ drawn as 2,8 with the two gained electrons shown as a different symbol [1]; charges +2 and −2 shown in square brackets [1]; formula MgO, because one 2+ balances one 2− [1].'),
  (54, 3, 'A hot air balloon is held upright and then its burner heats the air inside the envelope. Use what you know about particles, density and floating to explain why the balloon rises.',
   'Heating makes the air particles move faster and spread apart [1]; the same mass of air now fills a bigger volume, so the air inside is less dense than the cooler air outside [1]; the denser air sinks below and pushes the balloon up, like a solid floating on a liquid [1].'),
  (55, 4, 'Plan an investigation into how <strong>temperature</strong> affects the rate of transpiration in a plant. Name the independent variable, the dependent variable, two control variables, and say what result you expect.',
   'Independent: the temperature, e.g. a water bath or room at different temperatures [1]; dependent: water lost, e.g. mass lost by the plant, or how far a potometer bubble moves in a set time [1]; two controls: the same plant or leaf size, the same light intensity, the same humidity/wind, the same timing [1]; expected: warmer → faster transpiration [1].'),
  (56, 4, 'A blade of grass takes carbon dioxide out of the air. A rabbit eats the grass, a fox eats the rabbit, and later all three are dead. Describe how the carbon gets into the grass, how it reaches the fox, and how it returns to the air.',
   'Photosynthesis builds the carbon into glucose in the grass [1]; the carbon compounds pass along the food chain by feeding — grass to rabbit, rabbit to fox [1]; after death, decomposers (bacteria and fungi) feed on the remains and respire, releasing the carbon as carbon dioxide [1]; a fourth process that also returns carbon to the air is respiration by each living organism along the way (or combustion) [1].'),
  (57, 4, 'On a cold day Shanti drinks two large glasses of water; on a hot day, playing football, she drinks almost none. Describe what her kidneys do differently on the two days, and what happens to her urine.',
   'The kidneys keep the water content of the blood steady [1]; on the cold day there is spare water, so nephrons take less water back — more, paler urine [1]; on the hot day she loses water in sweat, so the kidneys take more water back into the blood [1]; so she produces little urine, and it is darker because the same urea is dissolved in less water [1].'),
  (58, 5, 'Draw a circuit diagram with a cell, a switch and two lamps in <strong>series</strong>. Then explain what happens to both lamps if the switch is opened, and explain why houses are wired in parallel rather than series.',
   'Cell, switch and two lamps drawn in one single loop with correct symbols [1]; opening the switch breaks the one loop, so both lamps go out — a series circuit has no other path for the current [1]; in parallel, each branch gets the full voltage so lamps are fully bright [1]; each lamp or appliance can be switched on and off independently [1]; a break in one branch does not stop the others working [1].'),
]
