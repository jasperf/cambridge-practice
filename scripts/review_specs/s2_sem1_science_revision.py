"""Spec: Secondary 2 · Semester 1 science revision (everything from Terms 1–2).

Build with:  python3 scripts/build_review_sheet.py scripts/review_specs/s2_sem1_science_revision.py
"""

META = dict(
    out='s2/sem1/sem1-science-revision',          # basename; .html, .md and -answers.md are written
    title='Science Revision &middot; Terms 1&ndash;2',
    badge='Science &middot; Terms 1&ndash;2 Review',
    eyebrow='Secondary 2 &middot; Science &middot; Terms 1&ndash;2 review',
    h1='Science Review<br><em>Terms 1 &amp; 2</em>',
    md_title='Secondary 2 · Science — Terms 1–2 Review',
    intro=('Every science topic from Terms 1 and 2 on one page: atoms and the periodic table, bonding, '
           'plant biology, density, waves and sound, thermal energy and electricity. Each topic starts '
           'with its key facts, then a short set of self-marked questions that make you use them. '
           'Use <strong>Cover the notes</strong> to test yourself first.'),
    md_intro=('Every science topic from Terms 1 and 2: the key facts for each topic, then questions that '
              'make you use them. Q1–Q42 match the interactive sheet; Q43–Q48 are written questions '
              'marked by the teacher. Diagrams are described in words.'),
    time_chip='About 45 minutes &middot; a calculator helps',
    storage_key='sem1-science-revision',
    back='../../index.html',
    answers_note='Answers for Q1–Q42 (auto-marked on the interactive sheet) and a marking guide for the written questions Q43–Q48. Keep this separate from the question sheet.',
    extra_links=[('../sem1/sem1-science-mock.html', 'Semester 1 mock paper'),
                 ('../science-formula-sheets/index.html', 'Formula sheets')],
)

SECTIONS = [
  dict(key='at', icon='&#9883;', color='var(--accent-math)', rgba='79,142,247',
       title='Atoms &amp; the Periodic Table', label='Atoms & Periodic Table',
       src='Term 1 &middot; Week 2', link='../t1/w2/term1-week2-atomic-structure-periodic.html',
       link2=('../science-formula-sheets/svg/science-diagram-periodic-table.svg', 'Periodic table'),
       facts=[
         ('Inside an atom', 'Protons (charge +1) and neutrons (no charge) sit in the nucleus. Electrons (charge &minus;1) move in shells around it.'),
         ('Two numbers', '<span class="f">atomic number = protons</span><br>In a neutral atom, electrons = protons.<br><span class="f">mass number = protons + neutrons</span>'),
         ('Filling shells', 'For the first 20 elements the shells hold <span class="f">2, 8, 8, 2</span>. Example: nitrogen (7) is 2,5.'),
         ('Reading the table', 'Group number = how many electrons are in the outer shell. Period = how many shells are in use. Group 8 (also called Group 0 or 18), the noble gases, have a full outer shell.'),
         ('Trends', 'Group 1 metals react by <em>losing</em> their single outer electron and get more reactive further down. Group 7 non-metals react by <em>gaining</em> one electron and get less reactive further down.'),
       ]),
  dict(key='bo', icon='&#128279;', color='var(--accent-math)', rgba='79,142,247',
       title='Bonding &amp; Ions', label='Bonding & Ions',
       src='Term 1 &middot; Weeks 3&ndash;4', link='../t1/w3/term1-week3-science-ionic-bonding.html',
       link2=('../t1/w4/term1-week4-science-covalent-metallic-bonding.html', 'Covalent &amp; metallic'),
       facts=[
         ('Ionic bonding', 'A metal reacts with a non-metal. Electrons move from the metal atom to the non-metal atom, and the oppositely charged ions attract.'),
         ('Ion charges', 'Groups 1, 2, 3 lose electrons: <span class="f">1+, 2+, 3+</span>. Groups 5, 6, 7 gain electrons: <span class="f">3&minus;, 2&minus;, 1&minus;</span>. Either way the ion ends up with a full outer shell.'),
         ('Writing formulae', 'Total + charge = total &minus; charge. Ca&sup2;&#8314; with Cl&#8315; gives <span class="f">CaCl&#8322;</span> (one 2+ balances two 1&minus;).'),
         ('Covalent bonding', 'Between non-metal atoms, which share pairs of electrons. A single bond is one shared pair and a double bond is two. Examples: H&#8322;O, CO&#8322;, CH&#8324;.'),
         ('Metallic bonding', 'Positive metal ions sit in a &ldquo;sea&rdquo; of delocalised electrons. That is why metals conduct and can be bent into shape.'),
         ('Ionic compounds', 'A giant lattice of ions with high melting points. They conduct electricity only when melted or dissolved in water.'),
       ]),
  dict(key='pl', icon='&#127807;', color='var(--accent-sci)', rgba='62,207,142',
       title='Plant Biology', label='Plant Biology',
       src='Term 1 &middot; Week 7', link='../t1/w7/term1-week7-science-unit-test2-plant-biology.html',
       facts=[
         ('Photosynthesis', '<span class="f">carbon dioxide + water &rarr; glucose + oxygen</span><br>Light energy, absorbed by chlorophyll, is written above the arrow.'),
         ('Where it happens', 'In the chloroplasts of leaf cells. Carbon dioxide comes in from the air, and water comes up from the roots.'),
         ('Using the glucose', 'Glucose is used for respiration and is turned into starch, cellulose, proteins, and fats and oils.'),
         ('Minerals', 'Magnesium is part of the chlorophyll molecule. Nitrate is needed to make proteins. Fertilisers add both to the soil to raise the yield.'),
         ('Investigation 1: light', 'Pondweed in water with a lamp at different distances. Count the oxygen bubbles per minute. Keep the pondweed, the water temperature and the timing the same.'),
         ('Investigation 2: starch test', 'Boil the leaf in water, warm it in ethanol, rinse it, then add iodine solution.'),
       ]),
  dict(key='de', icon='&#129482;', color='var(--accent-warn)', rgba='245,166,35',
       title='Density', label='Density',
       src='Term 2 &middot; Week 4', link='../t2/w4/term2-week4-science-unit3-density.html',
       facts=[
         ('The formula', '<span class="f">&rho; = m &divide; V</span><br>Rearranged: <span class="f">m = &rho; &times; V</span>, <span class="f">V = m &divide; &rho;</span>. Units: g/cm&sup3;.'),
         ('Finding volume', 'Regular block: length &times; width &times; height. Irregular object: lower it into a measuring cylinder; the rise in level is its volume (1 mL = 1 cm&sup3;).'),
         ('Units', '<span class="f">1 g/cm&sup3; = 1000 kg/m&sup3;</span>. Water is 1 g/cm&sup3;.'),
         ('Float or sink', 'Less dense than the liquid: floats. Denser: sinks. Liquids that do not mix stack in layers by density.'),
         ('Heating and cooling', 'Heated particles move faster and spread out. The mass stays the same while the volume grows, so the density falls. Gases are far less dense than solids and liquids.'),
         ('Water is odd', 'Ice (0.92 g/cm&sup3;) is less dense than liquid water, because hydrogen bonds hold the molecules in an open pattern. Lakes freeze from the top down.'),
       ]),
  dict(key='wa', icon='&#127925;', color='var(--accent-warn)', rgba='245,166,35',
       title='Waves &amp; Sound', label='Waves & Sound',
       src='Term 2 &middot; Week 4', link='../t2/w4/term2-week4-science-unit3-sound-thermal-energy.html',
       facts=[
         ('Two kinds of wave', '<strong>Transverse</strong>: vibrations at right angles to the direction of travel (crests and troughs), e.g. light. <strong>Longitudinal</strong>: vibrations along the direction of travel (compressions and rarefactions), e.g. sound.'),
         ('Measuring a wave', 'Amplitude: middle line to a crest. Wavelength: one crest to the next. Frequency: waves per second, in hertz (Hz).'),
         ('Period', '<span class="f">T = 1 &divide; f</span> and <span class="f">f = 1 &divide; T</span>, with T in seconds.'),
         ('What you hear', 'Bigger amplitude: louder. Higher frequency: higher pitch.'),
         ('Superposition', 'Crest meets crest: the amplitudes add. Crest meets trough: they cancel.'),
         ('Sound needs a medium', 'Sound is passed along by vibrating particles, so it travels through solids, liquids and gases but not through a vacuum.'),
       ]),
  dict(key='th', icon='&#128293;', color='var(--accent-warn)', rgba='245,166,35',
       title='Thermal Energy', label='Thermal Energy',
       src='Term 2 &middot; Week 4', link='../t2/w4/term2-week4-science-unit3-sound-thermal-energy.html',
       facts=[
         ('Heat vs temperature', 'Temperature (&deg;C) says how hot something is: the <em>average</em> kinetic energy of its particles. Heat, or thermal energy (J), is the <em>total</em>, so it also depends on the mass.'),
         ('Which way?', 'Heat always flows from the hotter object to the colder one, until both reach the same temperature.'),
         ('Conduction', 'Vibrating particles pass energy to their neighbours. Best in solids, especially metals.'),
         ('Convection', 'In liquids and gases: warm fluid expands, becomes less dense and rises; cooler fluid sinks to take its place.'),
         ('Radiation', 'Infrared waves. It needs no particles, so it crosses empty space.'),
         ('Insulation &amp; evaporation', 'Insulators trap still air (wool, foam, double glazing). Evaporation happens at the surface at any temperature and cools the liquid left behind. Boiling happens all through a liquid at its boiling point.'),
       ]),
  dict(key='el', icon='&#9889;', color='var(--accent-warn)', rgba='245,166,35',
       title='Electricity', label='Electricity',
       src='Term 2 &middot; Week 4', link='../t2/w4/term2-week4-science-unit3-electricity.html',
       facts=[
         ('Three quantities', 'Voltage V, in volts (V): the push. Current I, in amps (A): the flow of charge. Resistance R, in ohms (&Omega;): how hard it is for current to flow.'),
         ('Ohm&rsquo;s law', '<span class="f">V = I &times; R</span><br>so <span class="f">I = V &divide; R</span> and <span class="f">R = V &divide; I</span>.'),
         ('Series', 'One loop. The current is the same everywhere. The cell&rsquo;s voltage is shared between the components. <span class="f">R = R&#8321; + R&#8322; + &hellip;</span>'),
         ('Parallel', 'Several branches. Each branch gets the full voltage. The branch currents add up to the current from the cell.'),
         ('Variable resistor', 'Turning its resistance up lets less current flow, so a lamp in series with it gets dimmer.'),
         ('Meters', 'An ammeter measures current; a voltmeter measures voltage.'),
       ]),
]

FIG_CYL = '''<svg class="q-fig" viewBox="0 0 280 210" role="img" aria-label="Two measuring cylinders: water at 50 mL, then at 68 mL with a key inside" style="max-width:300px"><path class="draw" d="M50 30 V185 H110 V30" stroke="#7a84a0" stroke-width="2" fill="none" pathLength="1"/><rect class="fill" x="52" y="110" width="56" height="74" fill="rgba(79,142,247,0.35)"/><path class="draw" d="M50 110 H64" stroke="#4f8ef7" stroke-width="2" fill="none" pathLength="1"/><text x="80" y="200" font-size="12" fill="#7a84a0" text-anchor="middle" font-family="DM Mono, monospace">before</text><text x="22" y="114" font-size="12" fill="#e8eaf0" text-anchor="middle" font-family="DM Mono, monospace">50</text><path class="draw" d="M170 30 V185 H230 V30" stroke="#7a84a0" stroke-width="2" fill="none" pathLength="1"/><rect class="fill" x="172" y="81" width="56" height="103" fill="rgba(79,142,247,0.35)"/><path class="draw" d="M170 81 H184" stroke="#4f8ef7" stroke-width="2" fill="none" pathLength="1"/><path class="draw" d="M190 165 h22 M212 165 v8 M205 165 v6 M184 165 a6 6 0 1 1 6 0" stroke="#f5a623" stroke-width="3" fill="none" pathLength="1"/><text x="200" y="200" font-size="12" fill="#7a84a0" text-anchor="middle" font-family="DM Mono, monospace">after</text><text x="256" y="85" font-size="12" fill="#e8eaf0" text-anchor="middle" font-family="DM Mono, monospace">68</text><text x="140" y="20" font-size="11" fill="#7a84a0" text-anchor="middle" font-family="DM Mono, monospace">readings in mL</text></svg>'''

FIG_JAR = '''<svg class="q-fig" viewBox="0 0 300 210" role="img" aria-label="A jar with a layer of oil floating on water, and a plastic bead about to be dropped in" style="max-width:300px"><path class="draw" d="M60 40 V190 H180 V40" stroke="#7a84a0" stroke-width="2" fill="none" pathLength="1"/><rect class="fill" x="62" y="120" width="116" height="68" fill="rgba(79,142,247,0.35)"/><rect class="fill" x="62" y="80" width="116" height="40" fill="rgba(245,166,35,0.3)"/><circle class="fill" cx="120" cy="22" r="8" fill="#e05252"/><text x="120" y="22" font-size="10" fill="#fff" text-anchor="middle" dominant-baseline="central" font-family="DM Mono, monospace">?</text><text x="196" y="104" font-size="12" fill="#f5a623" font-family="DM Mono, monospace">oil 0.92</text><text x="196" y="158" font-size="12" fill="#4f8ef7" font-family="DM Mono, monospace">water 1.00</text><text x="136" y="26" font-size="12" fill="#e8eaf0" font-family="DM Mono, monospace">bead 0.96</text><text x="250" y="200" font-size="10" fill="#7a84a0" text-anchor="middle" font-family="DM Mono, monospace">g/cm³</text></svg>'''

Q = []
def num(id, sec, marks, q, ans, hint, reveal, unit='', tol=0, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='num', q=q, ans=ans, tol=tol, unit=unit, hint=hint, reveal=reveal, fig=fig, figmd=figmd))
def text(id, sec, marks, q, acc, hint, reveal, ph='type your answer', fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='text', q=q, acc=acc, ph=ph, hint=hint, reveal=reveal, fig=fig, figmd=figmd))
def mcq(id, sec, marks, q, opts, correct, hint, reveal, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='mcq', q=q, opts=opts, correct=correct, hint=hint, reveal=reveal, fig=fig, figmd=figmd))

# ---- A: atoms
num('s1','at',1,'A potassium atom has atomic number 19 and mass number 39. How many neutrons are in its nucleus?',20,
    'The mass number counts protons and neutrons together.','39 − 19 = 20 neutrons')
text('s2','at',1,'A chlorine atom (atomic number 17) gains one electron to become a chloride ion, Cl⁻. Write the electronic structure of the <strong>ion</strong>.',
    ['2,8,8','2.8.8','2, 8, 8','2 8 8','2-8-8'],'Write the atom’s structure first, then add one electron to the outer shell.',
    'Chlorine is 2,8,7. One extra electron gives 2,8,8: a full outer shell, like argon.', ph='e.g. 2,8,1')
num('s3','at',1,'An element has the electronic structure 2,8,3. Which <strong>group</strong> of the periodic table is it in?',3,
    'Look only at the last number.','Group 3: three electrons in the outer shell. (It is aluminium, in Period 3.)')
mcq('s4','at',2,'Fluorine is more reactive than chlorine, and chlorine is more reactive than bromine. Which explanation is correct?',
    ['Bromine has more electrons in its outer shell, so it is already more stable.',
     'Fluorine has the most protons, so its nucleus pulls hardest.',
     'Fluorine’s outer shell is closest to the nucleus, so an incoming electron is attracted most strongly.',
     'Bromine atoms are smaller, so there is no room for an extra electron.'],'c',
    'Group 7 atoms react by gaining an electron. How far from the nucleus does that electron land?',
    'C — Going down Group 7 each atom has one more shell, so the outer shell is further from the nucleus and pulls less strongly on an extra electron. Fluorine, at the top, pulls hardest.')
num('s5','at',1,'A neutral atom has 15 electrons and 16 neutrons. What is its mass number?',31,
    'In a neutral atom, how many protons go with 15 electrons?','15 protons + 16 neutrons = 31 (it is phosphorus).')
mcq('s6','at',1,'Which electronic structure belongs to an element that hardly reacts at all?',
    ['2,8,8','2,8,7','2,8,1','2,8,8,1'],'a','Which atom has nothing to gain, lose or share?',
    'A — 2,8,8 is argon, a noble gas. Its outer shell is already full.')

# ---- B: bonding
text('s7','bo',1,'Aluminium has atomic number 13. What is the charge on an aluminium ion? (Type it like 2+ or 1−.)',
    ['3+','+3','al3+','3 +'],'Work out its electronic structure, then its group.','3+: aluminium (2,8,3) loses its 3 outer electrons.', ph='e.g. 2+')
text('s8','bo',1,'Potassium forms K⁺ ions and oxygen forms O²⁻ ions. Write the formula of potassium oxide.',
    ['K2O','K₂O'],'How many 1+ ions balance one 2− ion?','K₂O: two 1+ ions balance one 2− ion.', ph='e.g. NaCl')
text('s9','bo',2,'Magnesium forms Mg²⁺ ions and nitrogen forms N³⁻ ions. Write the formula of magnesium nitride.',
    ['Mg3N2','Mg₃N₂'],'Find the smallest number that both 2 and 3 go into.',
    'Mg₃N₂: three Mg²⁺ give 6+, two N³⁻ give 6−, so the charges cancel.', ph='e.g. CaCl2')
mcq('s10','bo',1,'Which pair of elements would join by a <strong>covalent</strong> bond?',
    ['Sodium and fluorine','Magnesium and oxygen','Copper and zinc','Hydrogen and chlorine'],'d',
    'Covalent bonds form between two non-metals.',
    'D — Hydrogen and chlorine are both non-metals, so they share a pair of electrons (HCl). Sodium fluoride and magnesium oxide are ionic; copper and zinc are both metals.')
num('s11','bo',1,'An oxygen molecule, O₂, is held together by a <strong>double</strong> covalent bond. How many electrons are shared between the two atoms?',4,
    'Count pairs first, then electrons.','A double bond is 2 shared pairs, so 4 electrons.')
mcq('s12','bo',2,'Solid sodium chloride does not conduct electricity, but melted sodium chloride does. Why?',
    ['Melting releases free electrons from the chlorine atoms.',
     'In the solid the ions are locked in place; in the liquid they can move and carry charge.',
     'Melting turns the ionic bonds into covalent bonds.',
     'The solid has no charged particles in it at all.'],'b',
    'What are the charged particles in an ionic compound, and can they move?',
    'B — The ions themselves carry the current. They can only flow once the lattice breaks up on melting (or dissolving).')

# ---- C: plants
mcq('s13','pl',1,'A plant is kept in a dark cupboard for two days. One of its leaves is then tested with iodine solution. What do you see?',
    ['The leaf turns blue-black all over.','The iodine stays orange-brown.','The leaf turns bright green.','Only the veins turn blue-black.'],'b',
    'Can the plant photosynthesise in the dark? What happens to its stored starch?',
    'B — With no light there is no photosynthesis, and the plant uses up its stored starch. No starch, so the iodine stays orange-brown.')
text('s14','pl',1,'Plants turn some of their glucose into which substance to build strong cell walls?',
    ['cellulose'],'It is one of the uses of glucose, and it is not starch.','Cellulose')
num('s15','pl',1,'A field gives 4.0 tonnes of wheat without fertiliser and 5.2 tonnes with a nitrate fertiliser. By what percentage did the yield go up?',30,
    'Percentage increase = increase ÷ original × 100.','1.2 ÷ 4.0 × 100 = 30%', unit='%')
mcq('s16','pl',1,'A plant grows in soil with no nitrate. What would you expect to see?',
    ['Its leaves turn blue-black.','It makes extra starch and grows faster.','Its roots stop taking in water.','Slow, stunted growth.'],'d',
    'What does a plant build from nitrate, and what is that needed for?',
    'D — Without nitrate the plant cannot make enough protein, and protein is needed to build new cells, so growth is poor.')
num('s17','pl',1,'In the pondweed investigation, 54 bubbles are counted in 3 minutes. How many bubbles is that per minute?',18,
    'Share the bubbles equally between the minutes.','54 ÷ 3 = 18 bubbles per minute', unit='per minute')
mcq('s18','pl',1,'Which change would make the pondweed give off <strong>fewer</strong> bubbles per minute?',
    ['Moving the lamp further away','Moving the lamp closer','Using a brighter bulb','Adding a second lamp beside the first'],'a',
    'Which change gives the pondweed less light?',
    'A — Moving the lamp away lowers the light intensity, so photosynthesis slows and less oxygen is made.')

# ---- D: density
num('s19','de',2,'A metal block measures 5 cm × 4 cm × 2.5 cm and has a mass of 135 g. What is its density?',2.7,
    'Find the volume first.','V = 5 × 4 × 2.5 = 50 cm³, so ρ = 135 ÷ 50 = 2.7 g/cm³ (aluminium).', unit='g/cm³', tol=0.01)
num('s20','de',1,'Gold has a density of 19.3 g/cm³. What is the volume of a 386 g gold bar?',20,
    'Which rearrangement gives V?','V = m ÷ ρ = 386 ÷ 19.3 = 20 cm³', unit='cm³', tol=0.05)
num('s21','de',1,'A key is dropped into a measuring cylinder of water. Use the diagram to find the volume of the key.',18,
    'How far did the level rise?','68 − 50 = 18 mL, which is 18 cm³', unit='cm³', fig=FIG_CYL,
    figmd='A measuring cylinder reads 50 mL before the key goes in and 68 mL after.')
num('s22','de',1,'Cooking oil has a density of 0.92 g/cm³. What is that in kg/m³?',920,
    'How many kg/m³ is 1 g/cm³?','0.92 × 1000 = 920 kg/m³', unit='kg/m³')
mcq('s23','de',2,'A plastic bead (0.96 g/cm³) is dropped into the jar in the diagram. Where does it end up?',
    ['It floats on top of the oil.','It sinks to the bottom of the jar.','It sinks through the oil and floats on top of the water.','It floats halfway up the oil layer.'],'c',
    'Compare the bead with each liquid in turn.',
    'C — 0.96 is more than 0.92, so the bead sinks through the oil. 0.96 is less than 1.00, so it floats on the water and rests where the layers meet.',
    fig=FIG_JAR, figmd='A jar holds a layer of oil (0.92 g/cm³) floating on water (1.00 g/cm³).')
text('s24','de',1,'A metal ball just fits through a ring. After the ball is heated it no longer fits. Does its density increase, decrease or stay the same?',
    ['decrease','decreases','it decreases','decreased','goes down'],'What happens to its mass? What happens to its volume?',
    'Decreases: the mass is unchanged but the volume is bigger, so m ÷ V is smaller.', ph='one word')

# ---- E: waves
num('s25','wa',1,'A tuning fork vibrates at 50 Hz. What is the period of one vibration?',0.02,
    'Period and frequency are each 1 divided by the other.','T = 1 ÷ 50 = 0.02 s', unit='s', tol=0.0001)
num('s26','wa',1,'One wave passes a point every 0.25 s. What is the frequency?',4,
    'How many 0.25 s fit into one second?','f = 1 ÷ 0.25 = 4 Hz', unit='Hz')
num('s27','wa',1,'Two water waves meet crest to crest. One has an amplitude of 3 cm and the other 4 cm. What is the amplitude where they meet?',7,
    'Crest on crest: do they add or cancel?','3 + 4 = 7 cm', unit='cm')
mcq('s28','wa',1,'A guitar string is plucked again, harder, on the same note. How does the sound change?',
    ['It sounds higher, because the frequency goes up.','It sounds lower, because the wavelength gets longer.','It sounds louder and higher.','It sounds louder, but the pitch stays the same.'],'d',
    'Plucking harder changes the size of the vibration, not how often it happens.',
    'D — A harder pluck gives a bigger amplitude, so the sound is louder. The note, the frequency, is unchanged, so the pitch is the same.')
text('s29','wa',1,'A slinky is pushed and pulled along its length. What are the stretched-out parts, where the coils are furthest apart, called?',
    ['rarefactions','rarefaction','rarefractions','rarefraction'],'The squashed parts are compressions.','Rarefactions', ph='one word')
mcq('s30','wa',1,'An electric bell rings inside a sealed glass jar. A pump slowly removes the air. What do you hear?',
    ['The ringing gets quieter and quieter, until it can hardly be heard.','The ringing gets louder, because nothing gets in the way.','The ringing gets higher in pitch.','No change: sound passes through glass.'],'a',
    'What carries a sound from the bell to the glass?',
    'A — As air is removed there are fewer particles to pass the vibrations on, so less sound reaches you. In a perfect vacuum there would be none.')

# ---- F: thermal
mcq('s31','th',2,'A sparkler burns at about 1000 °C. A full bath of water is at 40 °C. Which statement is correct?',
    ['The sparkler has more thermal energy, because it is hotter.',
     'The bath has more thermal energy: its particles move more slowly, but there are vastly more of them.',
     'They have the same thermal energy, because both are hot.',
     'The bath has a higher temperature, because it is bigger.'],'b',
    'Temperature is an average; thermal energy is a total.',
    'B — The sparkler is hotter (higher average energy per particle), but the huge mass of bath water stores far more energy in total.')
num('s32','th',1,'A mug of tea at 70 °C is left in a room at 25 °C. At what temperature does the tea stop losing heat? (Assume the room stays at 25 °C.)',25,
    'Heat flows until there is no temperature difference.','25 °C: once the tea matches the room, there is no more heat flow.', unit='°C')
text('s33','th',1,'You feel the warmth of a campfire on your face, even though the air between you is cool. Which way of transferring heat is this?',
    ['radiation','infrared radiation','infrared','thermal radiation'],'It does not need the air to carry it.','Radiation (infrared)', ph='one word')
mcq('s34','th',1,'Why does double glazing help keep a room warm?',
    ['The two panes reflect all the heat back into the room.','Glass is a good conductor, so it spreads the heat evenly.','The thin gap of air between the panes conducts heat badly and is too narrow to circulate.','It stops infrared from the Sun getting in.'],'c',
    'What is between the two panes?',
    'C — Still air conducts heat very poorly, and the gap is too narrow for convection currents, so heat escapes slowly.')
mcq('s35','th',2,'You step out of a swimming pool on a windy day and feel cold, even though the air is warm. Why?',
    ['The fastest water particles escape from your skin as vapour, taking energy with them.','The wind is colder than the air.','The water on your skin is boiling away.','Cold flows from the water into your body.'],'a',
    'Which water particles are most likely to leave the surface?',
    'A — This is evaporation. The most energetic particles leave, so the average energy of what remains drops and your skin cools. Wind carries the vapour away, which speeds it up.')
text('s36','th',1,'In which state of matter can convection <strong>not</strong> happen?',
    ['solid','solids','a solid','in solids','in a solid'],'Convection needs the particles themselves to move from place to place.','Solids: the particles can only vibrate in place.', ph='one word')

# ---- G: electricity
num('s37','el',1,'A 6 V battery is connected across a 3 Ω resistor. What current flows?',2,
    'Which form of Ohm’s law gives I?','I = V ÷ R = 6 ÷ 3 = 2 A', unit='A')
num('s38','el',1,'A current of 0.2 A flows through a 45 Ω resistor. What is the voltage across it?',9,
    'Which form of Ohm’s law gives V?','V = I × R = 0.2 × 45 = 9 V', unit='V', tol=0.01)
num('s39','el',1,'Three resistors, 5 Ω, 7 Ω and 12 Ω, are joined in series. What is their total resistance?',24,
    'In series, resistances simply add.','5 + 7 + 12 = 24 Ω', unit='Ω')
num('s40','el',2,'The three resistors from Q39 are connected to a 12 V battery. What current flows?',0.5,
    'Use the total resistance from Q39.','I = V ÷ R = 12 ÷ 24 = 0.5 A', unit='A', tol=0.001)
mcq('s41','el',1,'How should a voltmeter be connected to measure the voltage across a lamp?',
    ['In series with the lamp, on the same wire.','In series with the cell, before the lamp.','Anywhere in the circuit, as long as the switch is closed.','In parallel, with one lead on each side of the lamp.'],'d',
    'A voltmeter compares the two ends of a component.',
    'D — The voltmeter goes across the lamp, in parallel. It is the ammeter that goes in series.')
mcq('s42','el',1,'Why are the lights in a house wired in parallel rather than in series?',
    ['Parallel circuits use less current altogether.','Each light gets the full mains voltage and can be switched on or off without the others.','In parallel the bulbs share the voltage, so they last longer.','Series circuits cannot carry mains electricity.'],'b',
    'Think about what happens to the other lights when one is switched off.',
    'B — Every parallel branch gets the full voltage, so each lamp is fully bright, and a broken or switched-off lamp does not break the circuit for the others.')

WRITTEN = [
  (43, 3, 'Draw dot-and-cross diagrams to show how a lithium atom (2,1) and a fluorine atom (2,7) form ions. Show the electron arrangement and the charge on each ion.',
   'Li⁺ drawn as 2 (one shell, outer electron gone) [1]; F⁻ drawn as 2,8 with the gained electron shown as a different symbol [1]; charges + and − shown, in square brackets [1].'),
  (44, 3, 'Ice floats on water, and a pond freezes from the top down. Explain why, and say why this matters for fish living in the pond.',
   'Ice is less dense than liquid water [1]; hydrogen bonds hold the molecules in an open pattern, so the same mass takes up more volume [1]; the ice layer stays on top and insulates the water below, which stays liquid, so fish survive [1].'),
  (45, 4, 'Plan an investigation into how light intensity affects the rate of photosynthesis in pondweed. Name the independent variable, the dependent variable, two control variables, and say what result you expect.',
   'Independent: distance of lamp / light intensity [1]; dependent: bubbles of oxygen per minute [1]; two controls, e.g. same pondweed, same water temperature, same counting time [1]; expected: closer lamp → more bubbles per minute (up to a limit) [1].'),
  (46, 3, 'Draw a transverse wave and label one wavelength and the amplitude. Then draw a second wave with the same amplitude but twice the frequency, and say how the two would sound different.',
   'Wavelength marked crest to crest (or trough to trough) [1]; amplitude marked from the middle line to a crest [1]; second wave has crests twice as close together and sounds higher-pitched but equally loud [1].'),
  (47, 3, 'A takeaway coffee cup has a double wall with air trapped between the layers. Explain how this design slows heat loss by conduction and convection, and why the lid also helps.',
   'Trapped air is a poor conductor, so little heat conducts through the wall [1]; the air layer is thin/still, so convection currents cannot form [1]; the lid stops warm air and vapour rising away (convection and evaporation) [1].'),
  (48, 4, 'Draw a circuit diagram with a cell, two lamps in parallel, an ammeter measuring the total current and a voltmeter across one lamp. Then explain what happens to the other lamp if one lamp breaks.',
   'Two lamps on separate branches [1]; ammeter in series in the main part of the circuit [1]; voltmeter in parallel across one lamp [1]; the other lamp stays lit, because its branch is still a complete loop [1].'),
]

# ---------------------------------------------------------------------------
# Explorers: optional interactive panels, placed after a section's key facts.
# Values are raw HTML; EXPLORER_JS is appended to the page script.
# None of them shows a value that a question on the sheet asks for.
# ---------------------------------------------------------------------------

EXPLORERS = {
  'at': '''<div class="explorer">
  <h3>&#9883; Shell Builder</h3>
  <p class="ex-note">Slide through the first 20 elements and watch the electrons fill the shells.</p>
  <div class="ex-row">
    <svg class="ex-svg" id="atom-svg" viewBox="0 0 240 240" style="max-width:260px" role="img" aria-label="Electron shell diagram of the chosen element"></svg>
    <div class="ex-controls">
      <label for="atom-z">Atomic number: <span id="atom-z-val">11</span></label>
      <input type="range" id="atom-z" min="1" max="20" value="11">
      <div class="ex-readout" id="atom-read"></div>
    </div>
  </div>
</div>''',
  'pl': '''<div class="explorer">
  <h3>&#127807; A Leaf at Work</h3>
  <p class="ex-note">What goes in, what comes out, and where the energy comes from.</p>
  <svg class="ex-svg wide" viewBox="0 0 440 230" role="img" aria-label="Animated leaf: light from the Sun and carbon dioxide from the air go in, water comes up the stem, oxygen bubbles out">
    <circle cx="48" cy="44" r="22" fill="#f5a623"/>
    <g class="rays" stroke="#f5a623" stroke-width="2.5" stroke-dasharray="6 8"><path d="M74 58 L170 100"/><path d="M66 74 L160 124"/><path d="M80 44 L182 80"/></g>
    <text x="48" y="88" font-size="11" fill="#f5a623" text-anchor="middle" font-family="DM Mono, monospace">light</text>
    <path d="M220 215 C 222 180, 222 150, 220 132" stroke="#3ecf8e" stroke-width="4" fill="none"/>
    <path d="M150 110 C 180 50, 280 40, 300 100 C 280 160, 180 165, 150 110 Z" fill="rgba(62,207,142,0.28)" stroke="#3ecf8e" stroke-width="2"/>
    <path d="M155 110 C 200 100, 250 98, 296 100" stroke="#3ecf8e" stroke-width="1.5" fill="none" opacity="0.7"/>
    <text x="225" y="122" font-size="12" fill="#e8eaf0" text-anchor="middle" font-family="DM Mono, monospace">glucose</text>
    <g class="flow-in" stroke="#7a84a0" stroke-width="2" stroke-dasharray="5 6" fill="none"><path d="M420 132 L304 112"/><path d="M420 150 L298 122"/></g>
    <text x="372" y="172" font-size="11" fill="#7a84a0" text-anchor="middle" font-family="DM Mono, monospace">carbon dioxide</text>
    <text x="372" y="186" font-size="11" fill="#7a84a0" text-anchor="middle" font-family="DM Mono, monospace">from the air</text>
    <path class="flow-up" d="M232 215 L232 140" stroke="#4f8ef7" stroke-width="2.5" stroke-dasharray="5 6" fill="none"/>
    <text x="300" y="214" font-size="11" fill="#4f8ef7" text-anchor="middle" font-family="DM Mono, monospace">water from the roots</text>
    <g fill="none" stroke="#e8eaf0" stroke-width="1.5"><circle class="bub b1" cx="290" cy="62" r="5"/><circle class="bub b2" cx="304" cy="70" r="4"/><circle class="bub b3" cx="280" cy="70" r="3.5"/></g>
    <text x="330" y="30" font-size="11" fill="#e8eaf0" text-anchor="middle" font-family="DM Mono, monospace">oxygen out</text>
  </svg>
</div>''',
  'de': '''<div class="explorer">
  <h3>&#129482; Float or Sink?</h3>
  <p class="ex-note">Set the mass and volume of a block and drop it into water (1.00 g/cm&sup3;). Each dot is 10 g of matter.</p>
  <div class="ex-row">
    <svg class="ex-svg" id="dens-svg" viewBox="0 0 300 240" style="max-width:340px" role="img" aria-label="A tank of water with a block that floats or sinks">
      <rect x="20" y="30" width="260" height="200" fill="none" stroke="#7a84a0" stroke-width="2"/>
      <rect x="21" y="80" width="258" height="149" fill="rgba(79,142,247,0.28)"/>
      <line x1="21" y1="80" x2="279" y2="80" stroke="#4f8ef7" stroke-width="2"/>
      <g id="dens-block" style="transition: transform 0.9s cubic-bezier(0.34,1.3,0.64,1)"></g>
    </svg>
    <div class="ex-controls">
      <label for="dens-m">Mass: <span id="dens-m-val">60</span> g</label>
      <input type="range" id="dens-m" min="10" max="200" step="10" value="60">
      <label for="dens-v">Volume: <span id="dens-v-val">80</span> cm&sup3;</label>
      <input type="range" id="dens-v" min="10" max="100" step="10" value="80">
      <div class="ex-readout" id="dens-read"></div>
    </div>
  </div>
</div>''',
  'wa': '''<div class="explorer">
  <h3>&#127925; Wave Maker</h3>
  <p class="ex-note">Change the amplitude and the frequency. The red dot shows how one particle moves as the wave passes.</p>
  <svg class="ex-svg wide" id="wave-svg" viewBox="0 0 600 200" role="img" aria-label="A moving transverse wave">
    <line x1="0" y1="100" x2="600" y2="100" stroke="#2a3050" stroke-width="1.5" stroke-dasharray="4 6"/>
    <line x1="300" y1="10" x2="300" y2="190" stroke="#2a3050" stroke-width="1"/>
    <path id="wave-path" stroke="#f5a623" stroke-width="3" fill="none"/>
    <circle id="wave-dot" cx="300" cy="100" r="7" fill="#e05252"/>
  </svg>
  <div class="ex-row" style="margin-top:12px">
    <div class="ex-controls">
      <label for="wave-a">Amplitude: <span id="wave-a-val">2</span> cm</label>
      <input type="range" id="wave-a" min="1" max="4" step="1" value="2">
    </div>
    <div class="ex-controls">
      <label for="wave-f">Frequency: <span id="wave-f-val">1</span> Hz</label>
      <input type="range" id="wave-f" min="0.5" max="3" step="0.5" value="1">
    </div>
    <div class="ex-readout" id="wave-read" style="flex:1 1 220px"></div>
  </div>
</div>''',
  'el': '''<div class="explorer">
  <h3>&#9889; Ohm&rsquo;s Law Circuit</h3>
  <p class="ex-note">Change the battery voltage and the resistance. Watch the moving charges and the lamp.</p>
  <div class="ex-row">
    <svg class="ex-svg" id="ohm-svg" viewBox="0 0 360 230" style="max-width:380px" role="img" aria-label="A circuit with a battery, resistor, lamp and ammeter">
      <path id="ohm-loop" d="M40 40 H320 V190 H40 Z" stroke="#7a84a0" stroke-width="2.5" fill="none"/>
      <rect x="28" y="96" width="24" height="28" fill="#1e2336"/>
      <line x1="24" y1="100" x2="56" y2="100" stroke="#e8eaf0" stroke-width="3"/>
      <line x1="31" y1="114" x2="49" y2="114" stroke="#e8eaf0" stroke-width="5"/>
      <text x="12" y="112" font-size="11" fill="#7a84a0" font-family="DM Mono, monospace" text-anchor="middle">+</text>
      <rect x="150" y="30" width="60" height="20" fill="#1e2336" stroke="#e8eaf0" stroke-width="2.5"/>
      <text x="180" y="22" font-size="12" fill="#7a84a0" text-anchor="middle" font-family="DM Mono, monospace" id="ohm-rlab">R</text>
      <circle id="ohm-glow" cx="320" cy="115" r="30" fill="#f5a623" opacity="0.3"/>
      <circle cx="320" cy="115" r="13" fill="#1e2336" stroke="#e8eaf0" stroke-width="2.5"/>
      <path d="M311 106 L329 124 M329 106 L311 124" stroke="#e8eaf0" stroke-width="2"/>
      <circle cx="180" cy="190" r="14" fill="#1e2336" stroke="#e8eaf0" stroke-width="2.5"/>
      <text x="180" y="191" font-size="13" fill="#e8eaf0" text-anchor="middle" dominant-baseline="central" font-family="DM Mono, monospace">A</text>
      <text x="180" y="222" font-size="12" fill="#3ecf8e" text-anchor="middle" font-family="DM Mono, monospace" id="ohm-alab"></text>
      <g id="ohm-charges"></g>
    </svg>
    <div class="ex-controls">
      <label for="ohm-v">Battery voltage: <span id="ohm-v-val">6</span> V</label>
      <input type="range" id="ohm-v" min="1.5" max="12" step="1.5" value="6">
      <label for="ohm-r">Resistance: <span id="ohm-r-val">4</span> &Omega;</label>
      <input type="range" id="ohm-r" min="2" max="20" step="2" value="4">
      <div class="ex-readout" id="ohm-read"></div>
    </div>
  </div>
</div>''',
}

EXPLORER_CSS = '''
.rays path, .flow-in path, .flow-up { animation: dashFlow 1.2s linear infinite; }
.flow-up { animation-direction: reverse; }
.bub { animation: bubbleUp 2.4s ease-in infinite; }
.b2 { animation-delay: 0.8s; } .b3 { animation-delay: 1.6s; }
@keyframes dashFlow { to { stroke-dashoffset: -28; } }
@keyframes bubbleUp { 0% { transform: translateY(0); opacity: 0; } 20% { opacity: 1; } 100% { transform: translateY(-46px); opacity: 0; } }
.orbit { transform-origin: 120px 120px; animation: spin linear infinite; }
.e-pop { animation: ePop 0.35s ease both; }
@keyframes spin { to { transform: rotate(360deg); } }
@keyframes ePop { from { opacity: 0; transform: scale(0.2); } to { opacity: 1; transform: scale(1); } }
@media (prefers-reduced-motion: reduce) { .rays path, .flow-in path, .flow-up, .bub, .orbit, .e-pop { animation: none; } }
'''

EXPLORER_JS = r'''
const REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// ---- Shell Builder
(function() {
  const EL = ['Hydrogen H','Helium He','Lithium Li','Beryllium Be','Boron B','Carbon C','Nitrogen N','Oxygen O','Fluorine F','Neon Ne',
              'Sodium Na','Magnesium Mg','Aluminium Al','Silicon Si','Phosphorus P','Sulfur S','Chlorine Cl','Argon Ar','Potassium K','Calcium Ca'];
  const svg = document.getElementById('atom-svg'), slider = document.getElementById('atom-z');
  if (!svg) return;
  function shells(z) { const caps = [2,8,8,2], out = []; let left = z; for (const c of caps) { if (left <= 0) break; out.push(Math.min(c,left)); left -= c; } return out; }
  function draw() {
    const z = +slider.value, [name, sym] = EL[z-1].split(' '), sh = shells(z);
    document.getElementById('atom-z-val').textContent = z;
    let s = `<circle cx="120" cy="120" r="17" fill="#f5a623"/><text x="120" y="120" font-size="12" fill="#0f1117" text-anchor="middle" dominant-baseline="central" font-family="DM Mono, monospace" font-weight="600">${sym}</text>`;
    let k = 0;
    sh.forEach((n, i) => {
      const r = 34 + i*24;
      s += `<g class="orbit" style="animation-duration:${10+i*6}s"><circle cx="120" cy="120" r="${r}" fill="none" stroke="#4a5270" stroke-width="1.5"/>`;
      for (let j = 0; j < n; j++) {
        const a = -Math.PI/2 + j*2*Math.PI/n, x = 120 + r*Math.cos(a), y = 120 + r*Math.sin(a);
        s += `<circle class="e-pop" style="animation-delay:${(k++)*0.04}s;transform-origin:${x}px ${y}px" cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="4.5" fill="#4f8ef7"/>`;
      }
      s += '</g>';
    });
    svg.innerHTML = s;
    document.getElementById('atom-read').innerHTML = `<strong>${name} (${sym})</strong><br>${z} proton${z>1?'s':''}, ${z} electron${z>1?'s':''}<br>Electronic structure: <strong>${sh.join(',')}</strong>`;
  }
  slider.addEventListener('input', draw); draw();
})();

// ---- Float or Sink?
(function() {
  const m = document.getElementById('dens-m'), v = document.getElementById('dens-v'), g = document.getElementById('dens-block');
  if (!g) return;
  function draw() {
    const mass = +m.value, vol = +v.value, rho = mass/vol;
    document.getElementById('dens-m-val').textContent = mass;
    document.getElementById('dens-v-val').textContent = vol;
    const side = 24 + vol*0.48, x = 150 - side/2;
    let top;
    if (rho < 1) top = 80 - side*(1-rho); else if (rho > 1) top = 228 - side; else top = 150 - side/2;
    let dots = '';
    const n = mass/10, cols = Math.ceil(Math.sqrt(n)), step = side/(cols+1);
    for (let i = 0; i < n; i++) dots += `<circle cx="${(step*(1 + i%cols)).toFixed(1)}" cy="${(step*(1 + Math.floor(i/cols))).toFixed(1)}" r="2.6" fill="#0f1117"/>`;
    g.innerHTML = `<rect width="${side}" height="${side}" rx="3" fill="#f5a623" stroke="#e8eaf0" stroke-width="1.5"/>${dots}`;
    g.style.transform = `translate(${x}px, ${top}px)`;
    const verdict = rho < 1 ? 'less dense than water, so it <strong>floats</strong>' : rho > 1 ? 'denser than water, so it <strong>sinks</strong>' : 'the same as water, so it <strong>hovers</strong> wherever you leave it';
    document.getElementById('dens-read').innerHTML = `&rho; = ${mass} &divide; ${vol} = <strong>${rho.toFixed(2)} g/cm&sup3;</strong><br>That is ${verdict}.`;
  }
  m.addEventListener('input', draw); v.addEventListener('input', draw); draw();
})();

// ---- Wave Maker
(function() {
  const path = document.getElementById('wave-path'), dot = document.getElementById('wave-dot');
  if (!path) return;
  const a = document.getElementById('wave-a'), f = document.getElementById('wave-f');
  const bars = (n, max) => '&#9646;'.repeat(n) + '<span style="opacity:.3">' + '&#9646;'.repeat(max-n) + '</span>';
  function readout() {
    const A = +a.value, F = +f.value, T = 1/F;
    document.getElementById('wave-a-val').textContent = A;
    document.getElementById('wave-f-val').textContent = F;
    document.getElementById('wave-read').innerHTML = `T = 1 &divide; ${F} = <strong>${+T.toFixed(2)} s</strong><br>Loudness ${bars(A,4)}<br>Pitch&nbsp;&nbsp;&nbsp; ${bars(F*2,6)}`;
  }
  const t0 = performance.now();
  function frame(now) {
    const t = REDUCED ? 0 : (now - t0)/1000, A = +a.value*20, F = +f.value, lam = 240/F;
    let d = '';
    for (let x = 0; x <= 600; x += 4) { const y = 100 - A*Math.sin(2*Math.PI*(F*t - x/lam)); d += (x ? 'L' : 'M') + x + ' ' + y.toFixed(1); }
    path.setAttribute('d', d);
    dot.setAttribute('cy', (100 - A*Math.sin(2*Math.PI*(F*t - 300/lam))).toFixed(1));
    if (!REDUCED) requestAnimationFrame(frame);
  }
  a.addEventListener('input', () => { readout(); if (REDUCED) frame(0); });
  f.addEventListener('input', () => { readout(); if (REDUCED) frame(0); });
  readout(); requestAnimationFrame(frame);
})();

// ---- Ohm's Law Circuit
(function() {
  const loop = document.getElementById('ohm-loop'), grp = document.getElementById('ohm-charges');
  if (!loop) return;
  const v = document.getElementById('ohm-v'), r = document.getElementById('ohm-r');
  const L = loop.getTotalLength(), N = 16, dots = [];
  for (let i = 0; i < N; i++) { const c = document.createElementNS('http://www.w3.org/2000/svg','circle'); c.setAttribute('r','4'); c.setAttribute('fill','#4f8ef7'); grp.appendChild(c); dots.push(c); }
  let offset = 0, last = performance.now();
  const current = () => +v.value / +r.value;
  function readout() {
    const V = +v.value, R = +r.value, I = V/R;
    document.getElementById('ohm-v-val').textContent = V;
    document.getElementById('ohm-r-val').textContent = R;
    document.getElementById('ohm-rlab').textContent = R + ' Ω';
    document.getElementById('ohm-alab').textContent = I.toFixed(2) + ' A';
    document.getElementById('ohm-glow').setAttribute('opacity', Math.min(0.9, 0.05 + I/3).toFixed(2));
    document.getElementById('ohm-glow').setAttribute('r', (16 + Math.min(1, I/3)*20).toFixed(1));
    document.getElementById('ohm-read').innerHTML = `I = V &divide; R = ${V} &divide; ${R} = <strong>${+I.toFixed(3)} A</strong><br>${I >= 2 ? 'A large current: the lamp glows brightly.' : I >= 0.6 ? 'A moderate current: the lamp is lit.' : 'A small current: the lamp is dim.'}`;
  }
  function frame(now) {
    const dt = Math.min(0.05, (now - last)/1000); last = now;
    if (!REDUCED) offset = (offset + current()*40*dt) % L;
    dots.forEach((c, i) => { const p = loop.getPointAtLength((offset + i*L/N) % L); c.setAttribute('cx', p.x.toFixed(1)); c.setAttribute('cy', p.y.toFixed(1)); });
    if (!REDUCED) requestAnimationFrame(frame);
  }
  v.addEventListener('input', readout); r.addEventListener('input', readout);
  readout(); requestAnimationFrame(frame);
})();
'''
