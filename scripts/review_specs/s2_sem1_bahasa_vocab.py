"""Spec: Secondary 2 · Bahasa Indonesia — Vocabulary Drill 1 (English ↔ Indonesian).

Build with:  python3 scripts/build_vocab_drill.py --only-md scripts/review_specs/s2_sem1_bahasa_vocab.py

Every word comes from the class materials in material/bahasa/s2 (unit 1 module,
unit 3 slides, SA revision pack, ad assignment slide). Rebuild all three files
with the command above (without --only-md).
"""

META = dict(
    out='s2/sem1/mocks/sem1-bahasa-indonesia-vocab',
    title='Bahasa Indonesia Vocabulary Drill &middot; Semester 1',
    badge='Bahasa Indonesia &middot; Vocabulary Drill',
    eyebrow='Secondary 2 &middot; Bahasa Indonesia Level 1 &middot; Semester 1 Vocabulary',
    h1='Vocabulary Drill<br><em>English &harr; Indonesian</em>',
    credit=('40 words from the Semester 1 units &mdash; Unit 1 <em>Di Dalam Kelasku</em> (classroom), '
            'Unit 2 <em>Teks Iklan</em> (advertisements) and Unit 3 <em>Mengenal Hewan</em> (animals) '
            '&mdash; practised in both directions. Type the translation, press Check (or Enter), and '
            'use Hint for a description in other words.'),
    md_title='Secondary 2 &middot; Bahasa Indonesia — Vocabulary Drill',
    md_intro=('40 words from the three Semester 1 units — Unit 1 *Di Dalam Kelasku* (classroom), '
              'Unit 2 *Teks Iklan* (advertisements) and Unit 3 *Mengenal Hewan* (animals) — practised '
              'in both directions. Write your answers in the blanks; the answer sheet lists every '
              'accepted spelling.'),
    answers_note=('Answers for Vocabulary Drill 1, both directions. On the interactive sheet '
                  '(sem1-bahasa-indonesia-vocab.html) the marking is automatic and accepts every '
                  'spelling listed here.'),
    storage_key='sem1-bahasa-indonesia-vocab',
    back='../../../index.html',
)

HAIWAN_A = 'Tulis nama hewan bahasa Indonesia untuk'
HAIWAN_B = '(Write the Indonesian name of the animal &ldquo;{0}&rdquo;.)'
ESP = 'di &hellip;'


def w(a, ans, hint, **kw):
    q = dict(a=a, ans=ans, hint=hint)
    q.update(kw)
    return q


SECTIONS = [
    dict(
        key='en', anchor='en',
        tab='&#128203; A &middot; English &rarr; Indonesian',
        icon='&#128203;', dir='en-id',
        label='Section A &middot; English &rarr; Indonesian',
        title='Write it in Indonesian',
        score_label='SECTION A &mdash; ENGLISH &rarr; INDONESIAN',
        js_label='English \\u2192 Indonesian',
        placeholder='bahasa Indonesia&hellip;',
        info=('Type the <strong>Indonesian</strong> word or phrase for each English word. Capital letters '
              'do not matter and hyphens are optional (<em>rak buku</em> = <em>rak-buku</em>). Press '
              '<strong>Check</strong> or <strong>Enter</strong>. The <strong>Hint</strong> button describes '
              'the word in other words &mdash; it never contains the answer itself.'),
        groups=[
            ('Kelas &amp; sekolah &middot; Classroom &amp; school', [
                w('chair', ['kursi'], 'You sit on this piece of furniture in class.'),
                w('bookshelf', ['rak buku', 'rak-buku'], 'A shelf where books are kept.'),
                w('wall clock', ['jam dinding'], 'It hangs on the wall and tells the time.'),
                w('rubbish bin', ['tempat sampah', 'tempat-sampah'],
                  'You throw rubbish into this container.'),
                w('globe', ['bola dunia'],
                  'A round model of the Earth that you find on a teacher&rsquo;s desk.'),
                w('student', ['siswa', 'pelajar'], 'A person who learns at school.',
                  reveal='&lt;em&gt;siswa&lt;/em&gt; = student (pelajar also works).'),
            ]),
            ('Preposisi &middot; Prepositions of place', [
                w('on / above', ['di atas', 'diatas', 'atas'],
                  'Use this when something rests on the top surface of something else.',
                  placeholder=ESP),
                w('under / below', ['di bawah', 'dibawah', 'bawah'],
                  'Use this when something is underneath something else.', placeholder=ESP),
                w('inside', ['di dalam', 'didalam', 'dalam'],
                  'Use this when something is within the walls of a room or container.',
                  placeholder=ESP),
                w('in front of', ['di depan', 'didepan', 'depan'],
                  'Use this when something faces the front of something else.', placeholder=ESP),
                w('between', ['di antara', 'diantara', 'antara'],
                  'Use this with two things, one on each side.', placeholder=ESP),
            ]),
            ('Teks iklan &middot; Advertisements', [
                w('product', ['produk'], 'In an advertisement, the thing being sold.'),
                w('advertisement', ['iklan'],
                  'A short text with a picture that tries to make people want a product.'),
                w('title', ['judul', 'judul iklan'],
                  'The big words at the top of an advertisement or a story.',
                  tail='(the headline of an ad)',
                  help='(Write the Indonesian word for &ldquo;title&rdquo;.)'),
                w('information', ['informasi', 'info'],
                  'Facts that tell you about a product: what it is, what it costs, where to get it.'),
            ]),
            ('Hewan &middot; Animals', [
                w('elephant', ['gajah'],
                  'The largest land animal; it has a trunk and big ears.',
                  ask_prefix=HAIWAN_A, help=HAIWAN_B.format('elephant')),
                w('giraffe', ['jerapah'], 'The animal with the longest neck.',
                  ask_prefix=HAIWAN_A, help=HAIWAN_B.format('giraffe')),
                w('monkey', ['monyet', 'kera'],
                  'A playful animal that climbs trees and eats bananas.',
                  ask_prefix=HAIWAN_A, help=HAIWAN_B.format('monkey'),
                  reveal='&lt;em&gt;monyet&lt;/em&gt; = monkey (kera also works).'),
                w('tortoise', ['kura-kura', 'kura kura'],
                  'A very slow animal that carries its house on its back.',
                  ask_prefix=HAIWAN_A, help=HAIWAN_B.format('tortoise')),
                w('rabbit', ['kelinci'],
                  'A small animal with long ears that hops and eats carrots.',
                  ask_prefix=HAIWAN_A, help=HAIWAN_B.format('rabbit')),
            ]),
        ],
    ),
    dict(
        key='id', anchor='id',
        tab='&#128302; B &middot; Indonesian &rarr; English',
        icon='&#128302;', dir='id-en',
        label='Section B &middot; Indonesian &rarr; English',
        title='What does it mean in English?',
        score_label='SECTION B &mdash; INDONESIAN &rarr; ENGLISH',
        js_label='Indonesian \\u2192 English',
        placeholder='English&hellip;',
        info=('Type the <strong>English</strong> meaning of each Indonesian word. Capital letters do not '
              'matter and articles are optional (<em>the board</em> = <em>board</em>). Press '
              '<strong>Check</strong> or <strong>Enter</strong>. The <strong>Hint</strong> button '
              'describes the word in other words &mdash; it never translates it for you.'),
        groups=[
            ('Kelas &amp; sekolah &middot; Classroom &amp; school', [
                w('papan tulis', ['board', 'whiteboard', 'white board', 'blackboard', 'black board',
                                  'the board'],
                  'The teacher writes on this at the front of the class.',
                  reveal='&lt;em&gt;board&lt;/em&gt; / &lt;em&gt;whiteboard&lt;/em&gt; (papan tulis).'),
                w('jendela', ['window'], 'You look through this to see outside.'),
                w('guru', ['teacher'], 'The person who teaches you at school.'),
                w('bersih', ['clean'],
                  'A classroom with no rubbish on the floor is ___; the opposite is kotor (dirty).'),
            ]),
            ('Preposisi &middot; Prepositions of place', [
                w('di belakang', ['behind', 'at the back', 'at the back of'],
                  'Use this when something is at the rear of something else.'),
                w('di samping', ['beside', 'besides', 'next to'],
                  'When two things touch each other, they are ___ each other.',
                  reveal='&lt;em&gt;beside&lt;/em&gt; / &lt;em&gt;next to&lt;/em&gt; (di samping).'),
                w('di tengah', ['in the middle', 'in the middle of', 'in the centre', 'in the center',
                                'middle', 'centre', 'center'],
                  'You say this when something is surrounded on all sides.',
                  reveal='&lt;em&gt;in the middle (of)&lt;/em&gt; (di tengah).'),
                w('di dekat', ['near', 'close to', 'nearby'],
                  'Use this when something is not far away.',
                  reveal='&lt;em&gt;near&lt;/em&gt; / &lt;em&gt;close to&lt;/em&gt; (di dekat).'),
            ]),
            ('Iklan &amp; kata tanya &middot; Ads &amp; question words', [
                w('kalimat ajakan', ['persuasive sentence', 'call to action', 'call-to-action',
                                     'persuasive call'],
                  'In an ad, the line that says &ldquo;Buy this now!&rdquo; is a ___.',
                  reveal='&lt;em&gt;persuasive sentence&lt;/em&gt; / &lt;em&gt;call to action&lt;/em&gt; '
                        '(kalimat ajakan).'),
                w('berapa', ['how much', 'how many'],
                  'Ask this to find out a price, a number or an amount.',
                  reveal='&lt;em&gt;how much&lt;/em&gt; / &lt;em&gt;how many&lt;/em&gt; (berapa).'),
                w('apa', ['what'], 'Ask this to find out the name or nature of a thing.'),
                w('siapa', ['who'], 'Ask this to find out which person.'),
            ]),
            ('Hewan &amp; bagian tubuh &middot; Animals &amp; body parts', [
                w('harimau', ['tiger'],
                  'A big wild cat with orange fur and black stripes.'),
                w('paruh', ['beak'],
                  'A bird uses this hard pointed mouth instead of teeth.'),
                w('belalai', ['trunk'], 'The elephant&rsquo;s long nose.'),
                w('ekor', ['tail'],
                  'The part at the very back of an animal&rsquo;s body; a happy cat waves it.'),
            ]),
            ('Kata sifat &amp; kata kerja &middot; Adjectives &amp; verbs', [
                w('cepat', ['fast', 'quick'], 'A rabbit is ___; a tortoise is not.',
                  reveal='&lt;em&gt;fast&lt;/em&gt; / &lt;em&gt;quick&lt;/em&gt; (cepat).'),
                w('lambat', ['slow'], 'A tortoise is ___; a rabbit is not.'),
                w('berat', ['heavy'],
                  'An elephant is ___; a bird is not. (This word also means &ldquo;busy&rdquo; '
                  'in other sentences.)',
                  tail='&mdash; think weight, not &ldquo;busy&rdquo;.',
                  help='(What is &ldquo;berat&rdquo; in English?)',
                  reveal='&lt;em&gt;heavy&lt;/em&gt; (berat, in the sense of weight).'),
                w('punya', ['have', 'has', 'to have'],
                  'Use this verb when something belongs to someone: &ldquo;Saya ___ buku.&rdquo;',
                  reveal='&lt;em&gt;to have&lt;/em&gt; / &lt;em&gt;has&lt;/em&gt; (punya).'),
            ]),
        ],
    ),
]
