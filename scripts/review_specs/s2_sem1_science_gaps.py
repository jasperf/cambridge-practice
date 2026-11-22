"""Spec: Secondary 2 · Semester 1 science — Gaps drill: the SA2 revision topics the other sheets miss.

Build with:  python3 scripts/build_review_sheet.py scripts/review_specs/s2_sem1_science_gaps.py

The excretory system, plant transport, the carbon cycle and giant structures are
not in the class slides, so these facts follow the Cambridge Lower Secondary
Stage 9 syllabus (see docs/s2-sem1-science-coverage-gaps.md). Conservation of
energy recaps the class's "3.3 Conserve Energy" slides and adds energy transfers.
"""

META = dict(
    out='s2/sem1/mocks/sem1-science-gaps',
    title='Science Gaps Drill &middot; Practice',
    badge='Science &middot; Gaps Drill',
    eyebrow='Secondary 2 &middot; Science &middot; Semester 1 topic drill',
    h1='Five topics<br><em>to close the gaps</em>',
    md_title='Secondary 2 · Science — Gaps Drill',
    intro=('Five topics from the Semester 1 science revision list that the other sheets hardly touch: the '
           'excretory system, how water moves through a plant, the carbon cycle, conservation of energy, and '
           'simple versus giant structures. Each section starts with its key facts. Three explorers sit at the '
           'end of their sections, after the questions: a kidney filter, a transpiration lab and a carbon '
           'cycle you can run yourself. Use <strong>Cover the notes</strong> to test yourself first.'),
    md_intro=('A practice sheet on five revision topics the other sheets cover only lightly: the human '
              'excretory system, absorption, transport and transpiration in plants, the carbon cycle, '
              'conservation of energy, and simple and giant structures. Q1–Q37 match the interactive sheet; '
              'Q38–Q43 are written questions marked by the teacher. Diagrams are described in words. The '
              'class slides do not cover most of these topics, so check the facts against your class notes.'),
    time_chip='About 35 minutes',
    storage_key='sem1-science-gaps',
    back='../../../index.html',
    answers_note='Answers for Q1–Q37 (auto-marked on the interactive sheet) and a marking guide for the written questions Q38–Q43. Keep this separate from the question sheet.',
    extra_links=[('./sem1-science-revision.html', 'Terms 1–2 science review'),
                 ('./sem1-science-bonding-ions.html', 'Bonding & Ions practice'),
                 ('../../reference/science-formula-sheets/index.html', 'Formula sheets')],
)

EXPLORERS_LAST = True

PB = '../t1/w7/term1-week7-science-unit-test2-plant-biology.html'

SECTIONS = [
  dict(key='ex', icon='&#129658;', color='var(--accent-math)', rgba='79,142,247',
       title='The Excretory System', label='Excretory System',
       src='Human Biology',
       link='https://ed.ted.com/lessons/how-do-your-kidneys-work-emma-bryce', link_label='Video: how kidneys work',
       facts=[
         ('Excretion', 'Removing the <em>waste made by chemical reactions</em> inside the body&rsquo;s cells. The lungs excrete carbon dioxide, the skin loses some in sweat, and the kidneys excrete urea in urine.'),
         ('Urea', 'When the body has more amino acids (from protein) than it needs, the <strong>liver</strong> breaks them down into <em>urea</em>. The blood carries urea to the kidneys. If it builds up, it is poisonous.'),
         ('The urinary system', 'Two <strong>kidneys</strong> filter the blood. Each sends urine down a <strong>ureter</strong> to the <strong>bladder</strong>, which stores it. Urine leaves the body through the <strong>urethra</strong>.'),
         ('Blood in, blood out', 'The <em>renal artery</em> brings blood to each kidney. The <em>renal vein</em> takes the cleaned blood away.'),
         ('How a kidney filters', 'About a million tiny tubes called <strong>nephrons</strong> filter the blood. Useful things (all the glucose, most of the water, the salts the body needs) are <em>taken back</em> into the blood. Urea, extra water and extra salt stay behind as urine.'),
         ('Water balance', 'The kidneys keep the water in the blood steady. They take back more water when the body is short of it, and less when there is plenty.'),
       ]),
  dict(key='pt', icon='&#127807;', color='var(--accent-sci)', rgba='62,207,142',
       title='Absorption, Transport &amp; Transpiration', label='Plant Transport',
       src='Plant Biology',
       link=PB, link_label='Plant Biology unit test',
       link2=('https://www.youtube.com/results?search_query=veritasium+why+trees+are+out+to+get+you', 'Video'),
       facts=[
         ('Root hair cells', 'Each has a long, thin outgrowth that pokes between soil particles. Millions of them give the root a huge <em>surface area</em> for taking in water (by <strong>osmosis</strong>) and mineral ions.'),
         ('Xylem', 'Long, hollow tubes of dead cells with strong walls. They carry <strong>water and minerals</strong> from the roots, up the stem, to the leaves. Water in xylem only goes <em>up</em>. The walls also help hold the plant up.'),
         ('Phloem', 'Tubes of living cells that carry <strong>dissolved sugar</strong> made in the leaves to every part that needs it: growing tips, roots, fruits and stores. Phloem carries sap both up and down.'),
         ('Transpiration', 'Water evaporates inside the leaf and escapes as water vapour through tiny pores called <strong>stomata</strong>. As water leaves the top, more is pulled up the xylem behind it, like drinking through a straw.'),
         ('Stomata', 'Each stoma is opened and closed by two <em>guard cells</em>. Open stomata let carbon dioxide in for photosynthesis, but water vapour gets out the same way. Most close in the dark.'),
         ('What speeds it up', 'Transpiration is faster when it is <span class="f">hotter</span>, <span class="f">windier</span>, <span class="f">drier</span> (low humidity) and <span class="f">brighter</span>.'),
       ]),
  dict(key='cc', icon='&#9851;', color='var(--accent-sci)', rgba='62,207,142',
       title='The Carbon Cycle', label='Carbon Cycle',
       src='Plant Biology',
       link=PB, link_label='Plant Biology unit test',
       link2=('https://www.youtube.com/results?search_query=fuseschool+what+is+the+carbon+cycle', 'Video'),
       facts=[
         ('Where carbon is stored', 'In the air as <em>carbon dioxide</em>; in living things as glucose, starch, fats and proteins; in dead matter; and in <em>fossil fuels</em> (coal, oil and gas) and limestone rock.'),
         ('Photosynthesis', 'Plants take carbon dioxide from the air and build it into glucose:<br><span class="f">carbon dioxide + water &rarr; glucose + oxygen</span>'),
         ('Respiration', 'Plants, animals and microorganisms all respire, all the time, and give carbon dioxide back to the air:<br><span class="f">glucose + oxygen &rarr; carbon dioxide + water</span>'),
         ('Feeding', 'When an animal eats a plant or another animal, the carbon compounds pass along the food chain.'),
         ('Decomposers', '<strong>Bacteria and fungi</strong> feed on dead organisms and waste. As they respire, the carbon goes back into the air as carbon dioxide.'),
         ('Fossil fuels and combustion', 'Living things buried millions of years ago, where decomposers could not reach them, slowly became coal, oil and gas. <strong>Combustion</strong> (burning) releases their carbon as carbon dioxide in a few seconds.'),
       ]),
  dict(key='en', icon='&#9889;', color='var(--accent-warn)', rgba='245,166,35',
       title='Conservation of Energy', label='Conservation of Energy',
       src='Thermal Energy',
       link='../t2/w4/term2-week4-science-unit3-sound-thermal-energy.html', link_label='Sound &amp; thermal energy sheet',
       facts=[
         ('The law', 'Energy is <strong>never created or destroyed</strong>. It is only <em>transferred</em> from one store to another, or spread out into the surroundings.'),
         ('Stores', 'Energy can be stored as <span class="f">chemical</span> (food, fuel, batteries), <span class="f">kinetic</span> (moving things), <span class="f">gravitational potential</span> (raised things), <span class="f">elastic</span> (stretched springs) and <span class="f">thermal</span> (hot things).'),
         ('Useful and wasted', 'Every device transfers some energy usefully and some in ways we do not want. <span class="f">energy in = useful energy out + wasted energy out</span>'),
         ('Where the waste goes', 'Wasted energy usually ends up <em>heating the surroundings</em> a little. It is spread so thinly that it is very hard to use again.'),
         ('Sankey diagrams', 'An arrow diagram where the <em>width</em> of each arrow shows the amount of energy. The input is on the left, useful energy goes straight on, and wasted energy bends away.'),
         ('Conserving heat (3.3)', 'Insulation, double glazing and curtains slow the heat lost from a building, so the heating does less work. That saves money and cuts greenhouse gases.'),
       ]),
  dict(key='gs', icon='&#128142;', color='var(--accent-warn)', rgba='245,166,35',
       title='Simple &amp; Giant Structures', label='Simple & Giant Structures',
       src='Chemical Structures',
       link='./sem1-science-bonding-ions.html', link_label='Bonding &amp; Ions drill',
       link2=('https://www.youtube.com/results?search_query=fuseschool+what+are+giant+chemical+structures', 'Video'),
       facts=[
         ('Simple molecules', 'Small groups of atoms such as H&#8322;O, CO&#8322;, O&#8322; and CH&#8324;. The covalent bonds <em>inside</em> each molecule are strong, but the forces <em>between</em> molecules are weak, so they melt and boil at low temperatures.'),
         ('Giant covalent structures', 'Huge networks in which every atom is joined to its neighbours by covalent bonds. There are no separate molecules. Melting means breaking millions of strong bonds, so the melting point is very high.'),
         ('Diamond', 'Carbon. Every atom is bonded to <strong>four</strong> others in a rigid 3D network. Extremely hard. No free electrons, so it does not conduct.'),
         ('Graphite', 'Carbon. Every atom is bonded to <strong>three</strong> others in flat sheets. The forces between the sheets are weak. The fourth outer electron of each atom is free to move along the sheets.'),
         ('Silicon dioxide', 'The main compound in sand and quartz. A giant covalent structure like diamond, so it is hard and melts at about 1700 &deg;C.'),
         ('Other giant structures', 'Ionic compounds (giant ionic lattices) and metals (giant metallic lattices) are giant structures too. Only simple molecules have low melting points.'),
       ]),
]

# ---------------------------------------------------------------- figures

MONO = 'font-family="DM Mono, monospace"'


def _urinary():
    s = ['<svg class="q-fig" viewBox="0 0 300 270" role="img" aria-label="The urinary system with four numbered parts: two kidneys, two tubes down to a bag, and one tube out of the bag" style="max-width:300px">']
    s.append('<path class="draw" d="M150 20 V250" stroke="#e74c3c" stroke-width="3" fill="none" pathLength="1" opacity="0.35"/>')
    s.append('<path class="draw" d="M162 20 V250" stroke="#4f8ef7" stroke-width="3" fill="none" pathLength="1" opacity="0.35"/>')
    for cx in (92, 220):
        s.append(f'<ellipse class="draw" cx="{cx}" cy="78" rx="26" ry="40" stroke="#e8a090" stroke-width="2.5" fill="none" pathLength="1"/>')
    s.append('<path class="draw" d="M104 108 C 112 140, 128 160, 140 178" stroke="#f5a623" stroke-width="2.5" fill="none" pathLength="1"/>')
    s.append('<path class="draw" d="M208 108 C 200 140, 184 160, 172 178" stroke="#f5a623" stroke-width="2.5" fill="none" pathLength="1"/>')
    s.append('<path class="draw" d="M128 182 C 120 210, 140 222, 156 222 C 172 222, 192 210, 184 182 Z" stroke="#f5a623" stroke-width="2.5" fill="none" pathLength="1"/>')
    s.append('<path class="draw" d="M156 222 V256" stroke="#f5a623" stroke-width="2.5" fill="none" pathLength="1"/>')
    for (x1, y1, x2, y2, n) in ((60, 70, 30, 70, '3'), (196, 140, 252, 140, '1'), (186, 200, 252, 200, '4'), (160, 245, 220, 245, '2')):
        s.append(f'<path class="draw" d="M{x1} {y1} L{x2} {y2}" stroke="#7a84a0" stroke-width="1.2" fill="none" pathLength="1"/>')
        tx = x2 - 10 if x2 < x1 else x2 + 10
        s.append(f'<text x="{tx}" y="{y2}" font-size="15" fill="#e8eaf0" text-anchor="middle" dominant-baseline="central" {MONO}>{n}</text>')
    s.append(f'<text x="150" y="12" font-size="10" fill="#7a84a0" text-anchor="middle" {MONO}>main artery and vein</text></svg>')
    return ''.join(s)


def _sankey():
    s = ['<svg class="q-fig" viewBox="0 0 380 220" role="img" aria-label="Sankey diagram for an electric motor: 500 J in; 350 J kinetic straight on; 120 J heat and an unknown amount of sound bend downwards" style="max-width:380px">']
    s.append('<path class="draw" d="M20 90 H150" stroke="#4f8ef7" stroke-width="100" fill="none" pathLength="1" opacity="0.85"/>')
    s.append('<path class="draw" d="M150 75 H300" stroke="#3ecf8e" stroke-width="70" fill="none" pathLength="1" opacity="0.85"/>')
    s.append('<polygon class="fill" points="300,32 340,75 300,118" fill="#3ecf8e" opacity="0.85"/>')
    s.append('<path class="draw" d="M150 122 H180 Q 212 122 212 154 V188" stroke="#f5a623" stroke-width="24" fill="none" pathLength="1" opacity="0.85"/>')
    s.append('<polygon class="fill" points="196,188 228,188 212,206" fill="#f5a623" opacity="0.85"/>')
    s.append('<path class="draw" d="M150 137 Q 158 137 158 148 V192" stroke="#e8a090" stroke-width="6" fill="none" pathLength="1"/>')
    s.append('<polygon class="fill" points="152,192 164,192 158,202" fill="#e8a090"/>')
    for x, y, t, a in ((80, 90, 'Electrical', 'middle'), (80, 106, '500 J', 'middle'), (232, 75, 'Kinetic 350 J', 'middle'),
                       (236, 172, 'Heat 120 J', 'start'), (146, 214, 'Sound ? J', 'end')):
        s.append(f'<text x="{x}" y="{y}" font-size="12" fill="#0f1117" text-anchor="{a}" dominant-baseline="central" {MONO}>{t}</text>'
                 if y < 120 else
                 f'<text x="{x}" y="{y}" font-size="12" fill="#e8eaf0" text-anchor="{a}" dominant-baseline="central" {MONO}>{t}</text>')
    s.append('</svg>')
    return ''.join(s)


FIG_URINARY, FIG_SANKEY = _urinary(), _sankey()
MD_URINARY = ('Two bean-shaped organs at the top, one on each side of a main artery and vein. A thin tube runs down from each '
              'to a bag in the middle at the bottom, and one tube leads out of the bag. Label 3 points to the left bean-shaped '
              'organ; label 1 to the right-hand tube running down to the bag; label 4 to the bag; label 2 to the tube leading out of the bag.')
MD_SANKEY = ('A Sankey diagram for an electric motor. Input: 500 J electrical. Straight on: 350 J kinetic. Bending '
             'downwards: 120 J heat, and a thin arrow labelled "Sound ? J".')

# ---------------------------------------------------------------- questions

Q = []
def num(id, sec, marks, q, ans, hint, reveal, unit='', tol=0, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='num', q=q, ans=ans, tol=tol, unit=unit, hint=hint, reveal=reveal, fig=fig, figmd=figmd))
def text(id, sec, marks, q, acc, hint, reveal, ph='type your answer', fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='text', q=q, acc=acc, ph=ph, hint=hint, reveal=reveal, fig=fig, figmd=figmd))
def mcq(id, sec, marks, q, opts, correct, hint, reveal, fig=None, figmd=None):
    Q.append(dict(id=id, sec=sec, marks=marks, kind='mcq', q=q, opts=opts, correct=correct, hint=hint, reveal=reveal, fig=fig, figmd=figmd))

# ---- A: excretory system
num('s1','ex',1,'The diagram shows the urinary system. Which number labels a <strong>ureter</strong>?',1,
    'A ureter joins a kidney to the bladder.','1: the tube from the right kidney down to the bladder.',
    fig=FIG_URINARY, figmd=MD_URINARY)
num('s2','ex',1,'In the same diagram, which number labels the part where urine is <strong>stored</strong> until you go to the toilet?',4,
    'It is the bag at the bottom.','4: the bladder. (3 is a kidney, 1 a ureter and 2 the urethra.)')
text('s3','ex',1,'Which organ turns extra amino acids into urea?',
    ['liver','the liver','liver cells'],'It is not the kidney: the kidney only removes the urea.',
    'The liver. The blood then carries the urea to the kidneys.', ph='one word')
text('s4','ex',1,'Name <strong>one</strong> substance that is in the blood entering a healthy kidney but is <strong>not</strong> found in the urine.',
    ['glucose','sugar','protein','proteins','red blood cells','blood cells','red blood cell','amino acids','white blood cells','platelets'],
    'Think of something the body needs and takes back, or something too big to filter.',
    'Glucose (all of it is taken back into the blood). Proteins and blood cells are also accepted: they are too big to be filtered out.')
num('s5','ex',2,'The two kidneys filter about <strong>180 litres</strong> of fluid out of the blood each day, but only about <strong>1.5 litres</strong> leaves the body as urine. How many litres are taken back into the blood each day?',178.5,
    'Filtered minus what leaves as urine.','180 − 1.5 = 178.5 litres are taken back. The kidneys return almost everything they filter.', unit='litres', tol=0.05)
num('s6','ex',1,'Using the numbers in Q5, what <strong>percentage</strong> of the filtered fluid is taken back into the blood? Give your answer to the nearest whole number.',99,
    'Divide the amount taken back by the amount filtered, then multiply by 100.','178.5 ÷ 180 × 100 = 99.2%, so about 99%.', unit='%', tol=0.5)
mcq('s7','ex',2,'After a long football match on a hot day, a player passes only a little urine, and it is dark yellow. Why?',
    ['The kidneys have stopped filtering the blood until the body cools down.','The player made more urea while running, and urea is dark.','The player lost a lot of water in sweat, so the kidneys took more water back into the blood.','The bladder has shrunk in the heat, so it holds less urine.'],'c',
    'Where did the water go during the match? What do the kidneys do when the body is short of water?',
    'C — Sweating lost a lot of water, so the kidneys take more back. The same urea is dissolved in less water, so the urine is darker and there is less of it.')
mcq('s8','ex',1,'Which of these is <strong>not</strong> an example of excretion?',
    ['Breathing out carbon dioxide','Getting rid of undigested food as faeces','Passing urine that contains urea','Losing urea in sweat'],'b',
    'Excretion removes waste <em>made by the body&rsquo;s own cells</em>. Was the food ever inside a cell?',
    'B — Undigested fibre never entered the body’s cells; it just passed through the gut. That is called egestion. The other three remove waste made by cell reactions.')

# ---- B: plant transport
text('s9','pt',1,'A stick of celery stands in red ink for a day. When it is cut across, small red dots show in the stem. Which tissue are the red dots?',
    ['xylem','the xylem','xylem vessels','xylem tubes','xylem vessel'],
    'Which tubes carry water up from the bottom of the stem?',
    'Xylem: the coloured water was pulled up the xylem tubes.', ph='one word')
text('s10','pt',1,'Aphids are small insects that pierce a plant&rsquo;s stem and drink the sweet, sugary sap. Which tissue do they feed from?',
    ['phloem','the phloem','phloem tubes','phloem vessels','phloem cells'],
    'Which tissue carries the sugar made in the leaves?','Phloem, which carries dissolved sugar from the leaves.', ph='one word')
mcq('s11','pt',2,'A plant is dug up and moved to a new pot. Many of its root hairs are torn off, and the plant wilts for a few days. Why?',
    ['The roots can no longer make glucose by photosynthesis.','The phloem is broken, so no water can reach the leaves.','The plant has lost its stomata, so water escapes faster.','With less surface area, the roots take in water more slowly than the leaves lose it.'],'d',
    'What job does all that root-hair surface do?',
    'D — Root hairs give a huge surface for absorbing water. With fewer of them, water comes in more slowly than transpiration takes it out, so the cells lose water and the plant droops until new hairs grow.')
mcq('s12','pt',1,'When would a tree lose water <strong>fastest</strong>?',
    ['A hot, dry, windy afternoon','A cool, still, damp night','A cold, foggy, still morning','A warm, humid evening after rain'],'a',
    'Look for the conditions that make water evaporate fastest from wet washing.',
    'A — Heat, dry air, wind and daylight (stomata open) all speed up transpiration. Every other choice has damp air, darkness, cold or no wind.')
num('s13','pt',1,'In a potometer, an air bubble in the tube moves <strong>18 mm in 6 minutes</strong> as the shoot takes up water. What is the rate, in mm per minute?',3,
    'Distance ÷ time.','18 ÷ 6 = 3 mm per minute.', unit='mm/min')
num('s14','pt',2,'A potted plant (with the soil covered in plastic) weighs <strong>250.0 g</strong>. Four hours later it weighs <strong>241.6 g</strong>. How much water did it lose <strong>per hour</strong>?',2.1,
    'First find the total mass lost, then share it over the hours.','250.0 − 241.6 = 8.4 g in 4 hours, so 8.4 ÷ 4 = 2.1 g per hour.', unit='g per hour', tol=0.01)
mcq('s15','pt',2,'Four leaves were hung up for a day. Leaf P had nothing on it. Leaf Q had petroleum jelly (waterproof) on its <strong>top</strong> surface, leaf R on its <strong>bottom</strong> surface, and leaf S on both. P and Q lost almost the same mass; R and S lost very little. What does this show?',
    ['Water is lost through the top of a leaf, not the bottom.','Petroleum jelly makes leaves gain mass.','Most of the stomata are on the lower surface of the leaf.','Leaves lose the same mass whatever is covered.'],'c',
    'Covering which surface made the big difference?',
    'C — Blocking the bottom surface (R) stopped most of the water loss, but blocking the top (Q) made almost no difference. So most stomata are on the underside, which is shaded and cooler.')
text('s16','pt',1,'Water moves from the soil into a root hair cell through its partially permeable membrane. What is this process called?',
    ['osmosis'],'It is the special name for water moving across a membrane.','Osmosis.', ph='one word')

# ---- C: carbon cycle
text('s17','cc',1,'Which process is the only one in the carbon cycle that takes carbon dioxide <strong>out</strong> of the air?',
    ['photosynthesis'],'Respiration, combustion and decomposition all do the opposite.',
    'Photosynthesis. Respiration, decomposition and combustion all add carbon dioxide to the air.', ph='one word')
text('s18','cc',1,'Fallen leaves on a forest floor slowly rot away. Which group of living things breaks them down and returns their carbon to the air?',
    ['decomposers','decomposer','bacteria and fungi','fungi and bacteria','bacteria','fungi','microorganisms','microbes'],
    'They feed on dead things.','Decomposers: bacteria and fungi. They respire, releasing the carbon as carbon dioxide.')
mcq('s19','cc',1,'Carbon atoms in grass end up in the muscles of a cow. Which process moved them?',
    ['Photosynthesis','Combustion','Decomposition','Feeding'],'d',
    'How did the grass get inside the cow?',
    'D — The cow ate (fed on) the grass, digested it and used the carbon compounds to build its own body.')
mcq('s20','cc',2,'An area of rainforest is burned and cleared for farmland. What happens to the carbon dioxide in the air?',
    ['It falls, because burning uses up carbon dioxide.','It rises, because burning releases carbon dioxide and fewer trees are left to photosynthesise.','It stays the same, because the farm animals breathe in the extra carbon dioxide.','It rises, but only for the day the trees are burning.'],'b',
    'There are two effects: one from the burning, one from what is missing afterwards.',
    'B — Combustion releases the trees’ carbon as carbon dioxide, and with the trees gone, less carbon dioxide is taken back out by photosynthesis. Animals give out carbon dioxide, they do not take it in.')
mcq('s21','cc',1,'Why did some dead plants from 300 million years ago become coal instead of rotting away?',
    ['They were buried where there was little oxygen, so decomposers could not break them down.','They were too big for decomposers to eat.','There were no bacteria or fungi on Earth yet.','The plants had already turned into carbon dioxide.'],'a',
    'What do decomposers need in order to respire?',
    'A — Buried in mud and water with almost no oxygen, the plants did not decompose. Heat and pressure turned them into coal over millions of years.')
num('s22','cc',2,'The carbon dioxide in the air was about <strong>280 ppm</strong> (parts per million) in the year 1750 and about <strong>420 ppm</strong> in 2025. What is the <strong>percentage increase</strong>?',50,
    'Increase ÷ starting value × 100.','420 − 280 = 140. 140 ÷ 280 × 100 = 50%.', unit='%', tol=0.5)
text('s23','cc',1,'Hydrogencarbonate indicator is orange-red at normal carbon dioxide levels, <strong>yellow</strong> when carbon dioxide rises and <strong>purple</strong> when it falls. A tube with pondweed in the indicator is left in bright light for 6 hours. What colour does it turn?',
    ['purple'],'In bright light, which is faster: photosynthesis or respiration?',
    'Purple: photosynthesis takes in carbon dioxide faster than respiration gives it out, so the level falls.', ph='one colour')
text('s24','cc',1,'An identical tube is wrapped in foil so no light reaches it. What colour does it turn after 6 hours?',
    ['yellow'],'Which process stops in the dark, and which carries on?',
    'Yellow: there is no photosynthesis in the dark, but the pondweed keeps respiring, so carbon dioxide builds up.', ph='one colour')

# ---- D: conservation of energy
num('s25','en',1,'A kettle transfers <strong>2400 J</strong> of energy each second. <strong>2040 J</strong> heats the water and the rest heats the kettle and the air around it. How much energy is wasted each second?',360,
    'Energy in = useful + wasted.','2400 − 2040 = 360 J wasted each second.', unit='J')
num('s26','en',2,'The Sankey diagram is for an electric motor. How much energy is transferred as <strong>sound</strong>?',30,
    'All the arrows out must add up to the arrow in.','500 − 350 − 120 = 30 J of sound.', unit='J', fig=FIG_SANKEY, figmd=MD_SANKEY)
mcq('s27','en',1,'A student says: &ldquo;My phone battery went flat because the energy got used up.&rdquo; Which is the best correction?',
    ['The energy is still in the battery, but it is now the wrong kind.','The energy went back into the plug socket.','Some energy is destroyed every time a phone is used.','The energy was transferred, mostly ending up as a little heat in the surroundings.'],'d',
    'Can energy ever disappear?',
    'D — Energy cannot be destroyed. The chemical store in the battery was transferred by electricity into light, sound and, in the end, the thermal store of the surroundings.')
mcq('s28','en',2,'A ball is dropped and bounces lower each time until it stops. What has happened to its energy?',
    ['It was destroyed when the ball hit the floor.','It is still stored in the ball as gravitational potential energy.','It was transferred to the surroundings as heat and sound at each bounce.','It turned into extra mass in the ball.'],'c',
    'What can you hear at each bounce? What would a very sensitive thermometer show?',
    'C — At each bounce some energy is transferred as sound and as heat (in the ball, the floor and the air). The total amount of energy is the same; it is just spread out.')
text('s29','en',1,'A torch is switched on. In which energy store does the energy start?',
    ['chemical','chemical store','the chemical store','chemical energy','chemical energy store','chemical potential'],
    'What is inside the batteries?','The chemical store of the batteries.', ph='one word')
mcq('s30','en',1,'Double glazing has two panes of glass with a gap of air or gas between them. Why does it keep a house warmer?',
    ['The trapped gas is a poor conductor, so less heat is lost through the window by conduction.','The second pane reflects all the heat back into the room.','Two panes let in twice as much sunlight.','The gas creates new heat as the sun shines on it.'],'a',
    'Is a gas a good or a poor conductor of heat?',
    'A — Gases are poor conductors. The gap is too narrow for much convection, so heat escapes through the window much more slowly.')

# ---- E: simple and giant structures
text('s31','gs',1,'Substance K melts at 1710 &deg;C. It does not conduct electricity, solid or melted, and it does not dissolve in water. What kind of structure does it have?',
    ['giant covalent','giant covalent structure','a giant covalent structure','giant covalent network','macromolecular','giant molecular','giant covalent lattice'],
    'A very high melting point rules out simple molecules. No conducting even when melted rules out ions and metals.',
    'Giant covalent (it is silicon dioxide). Ionic compounds conduct when melted, and metals conduct as solids.', ph='e.g. giant ionic')
text('s32','gs',1,'Substance L melts at &minus;182 &deg;C and is a gas at room temperature. What kind of structure does it have?',
    ['simple molecular','simple molecules','simple covalent','simple molecule','molecular','small molecules','simple covalent molecules','covalent molecules','simple'],
    'Only one kind of structure has weak forces between its particles.',
    'Simple molecular (it is methane, CH₄). Only weak forces between the molecules have to be overcome.', ph='e.g. giant ionic')
mcq('s33','gs',2,'Diamond and graphite are both pure carbon. Why does graphite conduct electricity but diamond does not?',
    ['Graphite contains carbon ions that can move.','In graphite each atom uses only three outer electrons in bonds, so one per atom can move.','Diamond’s bonds are too strong for electricity to break.','Graphite has a lower melting point, so it is partly liquid.'],'b',
    'A current needs charged particles that can move. How many bonds does each carbon make in each form?',
    'B — Carbon has four outer electrons. In diamond all four are in bonds. In graphite only three are, so the fourth can move along the sheets and carry a current. Neither contains ions.')
mcq('s34','gs',1,'Why does a graphite pencil leave a grey line on paper?',
    ['The covalent bonds in graphite break very easily.','Graphite melts from the heat of rubbing.','Graphite reacts with the paper.','Sheets of carbon atoms slide off, because the forces between the sheets are weak.'],'d',
    'What holds one sheet to the next?',
    'D — The bonds inside each sheet are strong, but the sheets are only weakly held together. Rubbing slides sheets off onto the paper.')
num('s35','gs',2,'Silicon dioxide has the formula SiO₂. In its giant structure each silicon atom bonds to <strong>4</strong> oxygen atoms. How many silicon atoms does each oxygen atom bond to?',2,
    'The formula says there are twice as many oxygen atoms as silicon atoms. Count the Si–O bonds both ways.',
    'Each Si makes 4 bonds to O. There are 2 O for every Si, so the 4 bonds are shared between 2 oxygens: 4 ÷ 2 = 2 bonds each, one to each of 2 silicon atoms.', unit='atoms')
text('s36','gs',1,'Which form of carbon is used on the tips of drills that cut through rock?',
    ['diamond','diamonds'],'Which form of carbon is the hardest?','Diamond: its rigid network of strong bonds makes it the hardest natural substance.', ph='one word')
mcq('s37','gs',2,'Carbon and silicon are in the same group, yet carbon dioxide is a gas and silicon dioxide is a hard solid. Why?',
    ['CO₂ is made of small separate molecules with weak forces between them; SiO₂ is one giant network of covalent bonds.','The bonds in CO₂ are ionic and the bonds in SiO₂ are covalent.','Silicon atoms are heavier, so SiO₂ cannot become a gas.','CO₂ has double bonds, which are weaker than single bonds.'],'a',
    'To turn each one into a gas, what has to be overcome?',
    'A — Boiling CO₂ only overcomes the weak forces between molecules. Melting SiO₂ means breaking strong covalent bonds all through the giant structure. Both contain only covalent bonds.')

WRITTEN = [
  (38, 3, 'Draw and label the human urinary system. Include the kidneys, ureters, bladder, urethra, renal artery and renal vein, and add arrows to show which way urine flows.',
   'Kidneys, ureters, bladder and urethra drawn joined in the right order [1]; renal artery and renal vein shown going to and from a kidney [1]; arrows from kidney down the ureter to the bladder and out through the urethra [1].'),
  (39, 4, 'Describe the journey of a water molecule from the soil to the air around a leaf. Use the words root hair cell, osmosis, xylem, evaporation and stomata.',
   'Enters a root hair cell from the soil by osmosis [1]; moves across the root into the xylem [1]; carried up the stem in the xylem to the leaf [1]; evaporates inside the leaf and leaves as water vapour through the stomata (transpiration) [1].'),
  (40, 4, 'Draw a carbon cycle with four stores: the air, plants, animals and fossil fuels. Label arrows with photosynthesis, respiration, feeding, decomposition and combustion.',
   'Photosynthesis: air → plants [1]; respiration: plants and animals → air, and feeding: plants → animals [1]; decomposition: dead plants and animals → air (via decomposers) [1]; combustion: fossil fuels → air [1].'),
  (41, 3, 'Plan an investigation to find out how wind speed affects the rate of transpiration. Say what you will change, what you will measure, and two things you will keep the same.',
   'Change the wind speed, e.g. a fan at different settings or distances [1]; measure the distance a potometer bubble moves, or mass lost, in a set time [1]; keep the same: e.g. the same plant or leaf size, temperature, light and humidity, and the same time [1].'),
  (42, 3, 'A filament bulb transfers 60 J of energy each second, but only 6 J is light. Draw a Sankey diagram for it, and explain where the other 54 J goes. Why is an LED bulb better?',
   'Sankey: 60 J in, a thin 6 J light arrow straight on and a wide 54 J heat arrow bending away, widths roughly to scale [1]; the 54 J heats the bulb and then the surrounding air; it is not destroyed [1]; an LED transfers more of its energy as light and wastes less as heat, so it needs less energy for the same light [1].'),
  (43, 4, 'Explain why diamond is very hard and does not conduct electricity, while graphite is soft and slippery and does conduct. Refer to the bonds in each.',
   'Diamond: each carbon bonded to four others in a rigid 3D network, so it is hard [1]; all outer electrons used in bonds, none free, so no conducting [1]; graphite: bonded to three others in sheets with weak forces between the sheets, so the sheets slide [1]; one free electron per carbon moves along the sheets, so it conducts [1].'),
]

# ---------------------------------------------------------------------------
# Explorers sit after each section's questions (EXPLORERS_LAST), so they can
# show the ideas freely: a kidney filtering blood, a leaf that transpires, and
# a carbon cycle you drive yourself.
# ---------------------------------------------------------------------------

EXPLORERS = {
  'ex': '''<div class="explorer">
  <h3>&#129658; Kidney Filter</h3>
  <p class="ex-note">Blood flows into the kidney from the left. Watch where each kind of particle goes, then change the day and watch the urine in the bladder.</p>
  <div class="ex-btns">
    <button class="ex-btn on" data-day="normal">Normal day</button>
    <button class="ex-btn" data-day="hot">Hot day, lots of sweating</button>
    <button class="ex-btn" data-day="drink">Drank lots of water</button>
    <button class="ex-btn" id="kf-empty">Empty bladder</button>
  </div>
  <svg class="ex-svg wide" id="kf-svg" viewBox="0 0 440 250" role="img" aria-label="Blood flows through a kidney; some particles carry on in the blood, others go down the ureter into the bladder">
    <path d="M0 70 H440" stroke="rgba(231,76,60,0.25)" stroke-width="34"/>
    <rect x="170" y="38" width="100" height="64" rx="24" fill="rgba(232,160,144,0.18)" stroke="#e8a090" stroke-width="2"/>
    <text x="220" y="30" font-size="11" fill="#e8a090" text-anchor="middle" font-family="DM Mono, monospace">kidney (nephrons)</text>
    <text x="8" y="104" font-size="10" fill="#7a84a0" font-family="DM Mono, monospace">renal artery</text>
    <text x="432" y="104" font-size="10" fill="#7a84a0" text-anchor="end" font-family="DM Mono, monospace">renal vein</text>
    <path d="M220 102 V170" stroke="rgba(245,166,35,0.35)" stroke-width="12"/>
    <text x="232" y="140" font-size="10" fill="#7a84a0" font-family="DM Mono, monospace">ureter</text>
    <clipPath id="kf-clip"><path d="M180 172 C 172 214, 198 236, 220 236 C 242 236, 268 214, 260 172 Z"/></clipPath>
    <rect id="kf-urine" x="170" y="236" width="100" height="0" fill="#f2dc6b" clip-path="url(#kf-clip)"/>
    <path d="M180 172 C 172 214, 198 236, 220 236 C 242 236, 268 214, 260 172 Z" fill="none" stroke="#f5a623" stroke-width="2"/>
    <text x="276" y="214" font-size="10" fill="#7a84a0" font-family="DM Mono, monospace">bladder</text>
    <g id="kf-parts"></g>
    <g font-size="10" font-family="DM Mono, monospace" fill="#e8eaf0">
      <circle cx="16" cy="140" r="6" fill="#e74c3c"/><text x="28" y="144">blood cell</text>
      <rect x="11" y="156" width="10" height="10" fill="#f5a623"/><text x="28" y="165">glucose</text>
      <circle cx="16" cy="182" r="4" fill="#4f8ef7"/><text x="28" y="186">water</text>
      <path d="M16 197 l5 9 h-10 z" fill="#b48cf2"/><text x="28" y="207">urea</text>
    </g>
  </svg>
  <div class="ex-readout" id="kf-read"></div>
</div>''',
  'pt': '''<div class="explorer">
  <h3>&#127807; Transpiration Lab</h3>
  <p class="ex-note">Water rises up the xylem and escapes from the leaf as vapour. Change the conditions and watch the rate.</p>
  <div class="ex-row">
    <svg class="ex-svg" id="tp-svg" viewBox="0 0 260 260" role="img" aria-label="A plant: water drops rise up the stem and leave the leaf as vapour">
      <path d="M20 222 H240" stroke="#7a5a3a" stroke-width="3"/>
      <path d="M130 222 L104 252 M130 222 L130 256 M130 222 L158 250 M104 252 l-10 4 M158 250 l10 3" stroke="#c9a46a" stroke-width="2" fill="none"/>
      <path d="M130 222 V80" stroke="#3ecf8e" stroke-width="10"/>
      <path d="M130 222 V80" stroke="rgba(79,142,247,0.35)" stroke-width="3"/>
      <path d="M130 84 C 160 40, 220 40, 240 70 C 210 104, 160 104, 130 84 Z" fill="rgba(62,207,142,0.25)" stroke="#3ecf8e" stroke-width="2"/>
      <path d="M130 84 C 100 50, 46 52, 24 80 C 52 108, 100 106, 130 84 Z" fill="rgba(62,207,142,0.25)" stroke="#3ecf8e" stroke-width="2"/>
      <g id="tp-stomata"></g>
      <g id="tp-drops"></g>
      <text x="140" y="170" font-size="10" fill="#7a84a0" font-family="DM Mono, monospace">xylem</text>
    </svg>
    <div class="ex-controls">
      <label for="tp-t">Temperature: <span id="tp-tv"></span></label>
      <input type="range" id="tp-t" min="5" max="35" value="20">
      <label for="tp-w">Wind: <span id="tp-wv"></span></label>
      <input type="range" id="tp-w" min="0" max="3" value="0">
      <label for="tp-h">Humidity: <span id="tp-hv"></span></label>
      <input type="range" id="tp-h" min="20" max="95" value="50">
      <div class="ex-btns" style="margin-top:6px"><button class="ex-btn on" data-light="1">Daytime</button><button class="ex-btn" data-light="0">Night</button></div>
    </div>
  </div>
  <div class="ex-readout" id="tp-read"></div>
</div>''',
  'cc': '''<div class="explorer">
  <h3>&#9851; Run the Carbon Cycle</h3>
  <p class="ex-note">Each dot is a load of carbon. Press a process to move carbon from one store to another, and keep an eye on the carbon dioxide in the air.</p>
  <div class="ex-btns">
    <button class="ex-btn" data-cc="photo">Photosynthesis</button>
    <button class="ex-btn" data-cc="resp">Respiration</button>
    <button class="ex-btn" data-cc="feed">Feeding</button>
    <button class="ex-btn" data-cc="death">Death &amp; waste</button>
    <button class="ex-btn" data-cc="decomp">Decomposition</button>
    <button class="ex-btn" data-cc="fossil">Fossilisation</button>
    <button class="ex-btn" data-cc="burn">Combustion</button>
    <button class="ex-btn" id="cc-reset">Reset</button>
  </div>
  <svg class="ex-svg wide" id="cc-svg" viewBox="0 0 440 260" role="img" aria-label="Five carbon stores: air, plants, animals, dead matter and fossil fuels, with carbon dots moving between them"></svg>
  <div class="ex-readout" id="cc-read"></div>
</div>''',
}

EXPLORER_CSS = '''
.ex-btns { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 12px; }
.ex-btn { font-family: var(--font-mono); font-size: 0.76rem; padding: 7px 12px; border-radius: 6px; border: 1px solid var(--border); background: var(--surface2); color: var(--text); cursor: pointer; }
.ex-btn:hover { border-color: var(--sec); }
.ex-btn.on { background: rgba(var(--sec-rgb),0.18); border-color: var(--sec); }
.ex-btn:disabled { opacity: 0.45; cursor: default; }
#tp-svg { max-width: 300px; }
#kf-urine { transition: height 0.4s ease, y 0.4s ease, fill 0.8s ease; }
'''

EXPLORER_JS = r'''
const REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const NS = 'http://www.w3.org/2000/svg';

// ---- Kidney Filter
(function() {
  const svg = document.getElementById('kf-svg');
  if (!svg) return;
  const grp = document.getElementById('kf-parts'), urine = document.getElementById('kf-urine');
  const btns = svg.closest('.explorer').querySelectorAll('[data-day]');
  const WATER_OUT = { normal: 0.3, hot: 0.1, drink: 0.6 };
  const NOTE = {
    normal: 'A normal day: the kidneys take back most of the water.',
    hot: 'Hot day: water is being lost in sweat, so the kidneys take back almost all the water that reaches them.',
    drink: 'Lots to drink: the blood has extra water, so more of it is let through into the urine.',
  };
  let day = 'normal', parts = [], tSpawn = 0, inB = { water: 0, urea: 0 };
  function shape(type) {
    const el = document.createElementNS(NS, type === 'glucose' ? 'rect' : type === 'urea' ? 'path' : 'circle');
    if (type === 'cell') { el.setAttribute('r', 6); el.setAttribute('fill', '#e74c3c'); }
    if (type === 'water') { el.setAttribute('r', 4); el.setAttribute('fill', '#4f8ef7'); }
    if (type === 'glucose') { el.setAttribute('width', 9); el.setAttribute('height', 9); el.setAttribute('x', -4.5); el.setAttribute('y', -4.5); el.setAttribute('fill', '#f5a623'); }
    if (type === 'urea') { el.setAttribute('d', 'M0 -5 l5 9 h-10 z'); el.setAttribute('fill', '#b48cf2'); }
    grp.appendChild(el);
    return el;
  }
  function spawn() {
    const r = Math.random();
    const type = r < 0.45 ? 'water' : r < 0.65 ? 'urea' : r < 0.82 ? 'glucose' : 'cell';
    let out = false;
    if (type === 'urea') out = Math.random() < 0.85;
    if (type === 'water') out = Math.random() < WATER_OUT[day];
    parts.push({ type, out, x: -8, y: 58 + Math.random()*24, el: shape(type) });
  }
  function bladder() {
    const tot = inB.water + inB.urea;
    const h = Math.min(64, tot * 0.9);
    urine.setAttribute('y', 236 - h); urine.setAttribute('height', h);
    const c = tot ? inB.urea / tot : 0.3;
    const k = Math.max(0, Math.min(1, (c - 0.2) / 0.6));
    const mix = (a, b) => Math.round(a + (b - a) * k);
    urine.setAttribute('fill', `rgb(${mix(246,200)},${mix(232,120)},${mix(140,30)})`);
    const shade = k < 0.33 ? 'pale' : k < 0.66 ? 'yellow' : 'dark yellow';
    document.getElementById('kf-read').innerHTML = `${NOTE[day]}<br>In the bladder: <strong>${inB.water}</strong> water &middot; <strong>${inB.urea}</strong> urea &middot; <strong>0</strong> glucose &middot; <strong>0</strong> blood cells. Urine: <strong>${shade}</strong>.`;
  }
  let last = performance.now();
  function frame(now) {
    const dt = Math.min(0.05, (now - last) / 1000); last = now;
    tSpawn += dt;
    if (tSpawn > 0.22) { tSpawn = 0; spawn(); }
    parts = parts.filter(p => {
      if (p.out && p.x >= 220) {
        p.x = 220 + (p.x - 220) * 0.8;
        p.y += 70 * dt;
        if (p.y > 222) { inB[p.type]++; p.el.remove(); bladder(); return false; }
      } else {
        p.x += 80 * dt;
        if (p.x > 450) { p.el.remove(); return false; }
      }
      p.el.setAttribute('transform', `translate(${p.x.toFixed(1)} ${p.y.toFixed(1)})`);
      return true;
    });
    requestAnimationFrame(frame);
  }
  btns.forEach(b => b.addEventListener('click', () => {
    btns.forEach(o => o.classList.toggle('on', o === b)); day = b.dataset.day;
    if (REDUCED) { inB = { water: Math.round(WATER_OUT[day] * 40), urea: 12 }; }
    bladder();
  }));
  document.getElementById('kf-empty').addEventListener('click', () => { inB = { water: 0, urea: 0 }; bladder(); });
  if (REDUCED) { inB = { water: 12, urea: 12 }; bladder(); } else { bladder(); requestAnimationFrame(frame); }
})();

// ---- Transpiration Lab
(function() {
  const svg = document.getElementById('tp-svg');
  if (!svg) return;
  const T = document.getElementById('tp-t'), W = document.getElementById('tp-w'), Hm = document.getElementById('tp-h');
  const lightBtns = svg.closest('.explorer').querySelectorAll('[data-light]');
  const drops = document.getElementById('tp-drops'), stomata = document.getElementById('tp-stomata');
  const WIND = ['still', 'light breeze', 'windy', 'gale'];
  let light = true, rate = 0, acc = 0, ds = [];
  const ST = [[165, 74], [195, 66], [212, 78], [98, 72], [68, 70], [52, 84]];
  function drawStomata() {
    stomata.innerHTML = ST.map(([x, y]) => `<ellipse cx="${x}" cy="${y}" rx="5" ry="${light ? 3 : 0.8}" fill="#0f1117" stroke="#3ecf8e" stroke-width="1.2"/>`).join('');
  }
  function update() {
    const t = +T.value, w = +W.value, h = +Hm.value;
    document.getElementById('tp-tv').textContent = t + ' °C';
    document.getElementById('tp-wv').textContent = WIND[w];
    document.getElementById('tp-hv').textContent = h + '%';
    const open = light ? 1 : 0.12;
    rate = open * (0.4 + (t - 5) / 20) * (1 + 0.45 * w) * (1.15 - h / 100);
    const g = (rate * 6).toFixed(1);
    const bar = '█'.repeat(Math.max(1, Math.round(rate * 6)));
    document.getElementById('tp-read').innerHTML = `Stomata: <strong>${light ? 'open' : 'mostly closed'}</strong><br>Water lost: <strong>${g} g per hour</strong> <span style="color:var(--accent-sci)">${bar}</span>`;
    drawStomata();
  }
  function addDrop(kind) {
    const c = document.createElementNS(NS, 'circle');
    c.setAttribute('r', kind === 'up' ? 3 : 2.5);
    c.setAttribute('fill', kind === 'up' ? '#4f8ef7' : '#9ec5ff');
    drops.appendChild(c);
    if (kind === 'up') return { kind, x: 130, y: 222, el: c };
    const [sx, sy] = ST[Math.floor(Math.random() * ST.length)];
    return { kind, x: sx, y: sy, vx: (sx > 130 ? 1 : -1) * (10 + 18 * +W.value) * (0.6 + Math.random()), vy: -18 - Math.random() * 14, life: 1, el: c };
  }
  let last = performance.now();
  function frame(now) {
    const dt = Math.min(0.05, (now - last) / 1000); last = now;
    acc += dt * rate * 4;
    while (acc > 1) { acc -= 1; ds.push(addDrop('up')); }
    ds = ds.filter(d => {
      if (d.kind === 'up') {
        d.y -= 70 * dt;
        if (d.y < 86) { d.el.remove(); ds.push(addDrop('vap')); return false; }
      } else {
        d.x += d.vx * dt; d.y += d.vy * dt; d.life -= dt * 0.8;
        d.el.setAttribute('opacity', Math.max(0, d.life).toFixed(2));
        if (d.life <= 0) { d.el.remove(); return false; }
      }
      d.el.setAttribute('cx', d.x.toFixed(1)); d.el.setAttribute('cy', d.y.toFixed(1));
      return true;
    });
    requestAnimationFrame(frame);
  }
  [T, W, Hm].forEach(el => el.addEventListener('input', update));
  lightBtns.forEach(b => b.addEventListener('click', () => { lightBtns.forEach(o => o.classList.toggle('on', o === b)); light = b.dataset.light === '1'; update(); }));
  update();
  if (!REDUCED) requestAnimationFrame(frame);
})();

// ---- Run the Carbon Cycle
(function() {
  const svg = document.getElementById('cc-svg');
  if (!svg) return;
  const S = {
    air:    { x: 220, y: 34,  label: 'Air (CO₂)', col: '#7a84a0' },
    plants: { x: 70,  y: 128, label: 'Plants', col: '#3ecf8e' },
    animals:{ x: 370, y: 128, label: 'Animals', col: '#f5a623' },
    dead:   { x: 160, y: 222, label: 'Dead matter', col: '#c9a46a' },
    fossil: { x: 340, y: 222, label: 'Fossil fuels', col: '#e8a090' },
  };
  const START = { air: 8, plants: 10, animals: 5, dead: 5, fossil: 16 };
  const MOVES = {
    photo:  [['air', 'plants', 2]],
    resp:   [['plants', 'air', 1], ['animals', 'air', 1]],
    feed:   [['plants', 'animals', 1]],
    death:  [['plants', 'dead', 1], ['animals', 'dead', 1]],
    decomp: [['dead', 'air', 2]],
    fossil: [['dead', 'fossil', 1]],
    burn:   [['fossil', 'air', 3]],
  };
  const NOTE = {
    photo: 'Photosynthesis: plants take carbon dioxide out of the air and build it into glucose.',
    resp: 'Respiration: plants and animals release carbon dioxide back to the air.',
    feed: 'Feeding: carbon compounds pass from plants to the animals that eat them.',
    death: 'Death and waste: dead plants, dead animals and droppings pile up.',
    decomp: 'Decomposition: bacteria and fungi feed on dead matter and respire, releasing carbon dioxide.',
    fossil: 'Fossilisation: buried without oxygen for millions of years, dead matter becomes coal, oil or gas.',
    burn: 'Combustion: burning fossil fuels releases millions of years of stored carbon in moments.',
  };
  let n = { ...START }, busy = false, msg = 'Press a process to begin.';
  const LINKS = [['air','plants'],['plants','animals'],['plants','dead'],['animals','dead'],['dead','air'],['animals','air'],['dead','fossil'],['fossil','air']];
  function draw() {
    let s = '';
    LINKS.forEach(([a, b]) => { s += `<line x1="${S[a].x}" y1="${S[a].y}" x2="${S[b].x}" y2="${S[b].y}" stroke="#2a3050" stroke-width="2" stroke-dasharray="4 4"/>`; });
    for (const k in S) {
      const o = S[k], heavy = k === 'air' ? Math.min(0.6, 0.08 + n.air * 0.025) : 0.14;
      s += `<rect x="${o.x - 58}" y="${o.y - 22}" width="116" height="44" rx="9" fill="${k === 'air' ? `rgba(231,76,60,${heavy.toFixed(2)})` : 'rgba(30,35,54,0.95)'}" stroke="${o.col}" stroke-width="2"/>`;
      s += `<text x="${o.x}" y="${o.y - 5}" font-size="11" fill="#e8eaf0" text-anchor="middle" font-family="DM Mono, monospace">${o.label}</text>`;
      s += `<text x="${o.x}" y="${o.y + 12}" font-size="12" fill="${o.col}" text-anchor="middle" font-family="DM Mono, monospace" font-weight="600">${n[k] ? '●'.repeat(Math.min(n[k], 8)) + (n[k] > 8 ? '…' : '') : '—'} ${n[k]}</text>`;
    }
    s += '<g id="cc-fly"></g>';
    svg.innerHTML = s;
    const d = n.air - START.air;
    const trend = d > 0 ? `<span style="color:var(--wrong)">up ${d} on the start</span>` : d < 0 ? `<span style="color:var(--correct)">down ${-d} on the start</span>` : 'the same as at the start';
    document.getElementById('cc-read').innerHTML = `${msg}<br>Carbon dioxide in the air: <strong>${n.air}</strong> loads, ${trend}.`;
  }
  function run(key) {
    if (busy) return;
    const moves = MOVES[key].filter(([a]) => n[a] > 0);
    if (!moves.length) { msg = 'Nothing left in that store to move.'; draw(); return; }
    busy = true; msg = NOTE[key];
    const fly = document.getElementById('cc-fly'), dots = [];
    moves.forEach(([a, b, k]) => {
      const m = Math.min(k, n[a]);
      for (let i = 0; i < m; i++) {
        const c = document.createElementNS(NS, 'circle');
        c.setAttribute('r', 6); c.setAttribute('fill', S[b].col);
        fly.appendChild(c);
        dots.push({ c, a, b, delay: i * 0.15 });
      }
    });
    const t0 = performance.now(), dur = REDUCED ? 0 : 900;
    function step(now) {
      let done = true;
      dots.forEach(d => {
        let p = dur ? ((now - t0) / dur - d.delay) : 1;
        p = Math.max(0, Math.min(1, p)); if (p < 1) done = false;
        const e = p < 0.5 ? 2*p*p : 1 - Math.pow(-2*p + 2, 2)/2;
        d.c.setAttribute('cx', S[d.a].x + (S[d.b].x - S[d.a].x) * e);
        d.c.setAttribute('cy', S[d.a].y + (S[d.b].y - S[d.a].y) * e);
      });
      if (!done) { requestAnimationFrame(step); return; }
      dots.forEach(d => { n[d.a]--; n[d.b]++; });
      busy = false; draw();
    }
    requestAnimationFrame(step);
  }
  svg.closest('.explorer').querySelectorAll('[data-cc]').forEach(b => b.addEventListener('click', () => run(b.dataset.cc)));
  document.getElementById('cc-reset').addEventListener('click', () => { n = { ...START }; msg = 'Back to the start.'; draw(); });
  draw();
})();
'''
