"""Spec: Secondary 2 · Bahasa Indonesia — Vocabulary Drill 2 (English ↔ Indonesian).

Build with:  python3 scripts/build_vocab_drill.py scripts/review_specs/s2_sem1_bahasa_vocab_2.py

A second set of 40 typed-answer questions from the same three Semester 1 units
as Drill 1 — Unit 1 Di Dalam Kelasku (classroom), Unit 2 Teks Iklan
(advertisements) and Unit 3 Mengenal Hewan (animals) — practised in both
directions. None of the 40 words repeat Drill 1. As with every vocab drill:
typed answers only, no multiple choice, hints describe the word without
giving it away.
"""

META = dict(
    out='s2/sem1/mocks/sem1-bahasa-indonesia-vocab-2',
    title='Bahasa Indonesia Vocabulary Drill 2 &middot; Semester 1',
    badge='Bahasa Indonesia &middot; Vocabulary Drill 2',
    eyebrow='Secondary 2 &middot; Bahasa Indonesia Level 1 &middot; Semester 1 Vocabulary',
    h1='Vocabulary Drill 2<br><em>English &harr; Indonesian</em>',
    credit=('A second set of 40 words from the Semester 1 units &mdash; Unit 1 <em>Di Dalam Kelasku</em> '
            '(classroom), Unit 2 <em>Teks Iklan</em> (advertisements) and Unit 3 <em>Mengenal Hewan</em> '
            '(animals) &mdash; practised in both directions, with no overlap with Vocabulary Drill 1. '
            'Type the translation, press Check (or Enter), and use Hint for a description in other words.'),
    md_title='Secondary 2 &middot; Bahasa Indonesia — Vocabulary Drill 2',
    md_intro=('A second set of 40 words from the three Semester 1 units — Unit 1 *Di Dalam Kelasku*, '
              'Unit 2 *Teks Iklan* and Unit 3 *Mengenal Hewan* — practised in both directions. None of '
              'the words repeat Vocabulary Drill 1. Write your answers in the blanks; the answer sheet '
              'lists every accepted spelling.'),
    answers_note=('Answers for Vocabulary Drill 2, both directions. On the interactive sheet '
                  '(sem1-bahasa-indonesia-vocab-2.html) the marking is automatic and accepts every '
                  'spelling listed here.'),
    storage_key='sem1-bahasa-indonesia-vocab-2',
    back='../../../index.html',
)

HAIWAN_A = 'Tulis nama hewan bahasa Indonesia untuk'
HAIWAN_B = '(Write the Indonesian name of the animal &ldquo;{0}&rdquo;.)'


def w(en, ans, hint, **kw):
    q = dict(a=en, ans=ans, hint=hint)
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
              'do not matter and hyphens are optional (<em>tempat pensil</em> = <em>tempat-pensil</em>). Press '
              '<strong>Check</strong> or <strong>Enter</strong>. The <strong>Hint</strong> button describes '
              'the word in other words &mdash; it never contains the answer itself.'),
        groups=[
            ('Kelas &amp; sekolah &middot; Classroom &amp; school', [
                w('book', ['buku'], 'It has pages and you read it.'),
                w('pencil case', ['tempat pensil', 'tempat-pensil'],
                  'A small box or bag that holds your pens and pencils.'),
                w("teacher's desk", ['meja guru', 'meja-guru'],
                  'The table at the front where the teacher sits and works.'),
                w("student's desk", ['meja siswa', 'meja-siswa'],
                  'The table you sit at to do your work in class.'),
                w('cupboard', ['lemari'], 'A tall piece of furniture with doors where things are stored.'),
                w('plant', ['tanaman'], 'It is green, grows in a pot by the window and needs water.'),
                w('notice board', ['papan pengumuman', 'papan-pengumuman'],
                  'A board on the wall where posters and messages are pinned.'),
                w('loudspeaker', ['pengeras suara', 'pengeras-suara'],
                  'It makes sounds and announcements louder so everyone can hear.'),
            ]),
            ('Tentang kelas &middot; Describing the class', [
                w('neat', ['rapi'], 'When everything is in its place and nothing is messy.'),
                w('comfortable', ['nyaman'], 'How you feel on a soft chair in a cool room.'),
                w('school', ['sekolah'],
                  'The place you go every morning to learn, with teachers and lessons.'),
                w('age', ['umur', 'usia'], 'The number of years old you are.',
                  reveal='&lt;em&gt;umur&lt;/em&gt; = age (usia also works).'),
                w('right side', ['di sisi kanan', 'sisi kanan', 'kanan'],
                  'The opposite of the left side, where most people hold a pen.',
                  placeholder='di &hellip;'),
                w('left side', ['di sisi kiri', 'sisi kiri', 'kiri'],
                  'The opposite of the right side.', placeholder='di &hellip;'),
                w('where', ['di mana', 'dimana'],
                  'Ask this question word to learn about a place.',
                  placeholder='di &hellip;'),
            ]),
            ('Hewan &middot; Animals', [
                w('duck', ['bebek'], 'A bird that swims on ponds and says quack.',
                  ask_prefix=HAIWAN_A, help=HAIWAN_B.format('duck')),
                w('goat', ['kambing'], 'A farm animal with a beard that climbs rocks and eats grass.',
                  ask_prefix=HAIWAN_A, help=HAIWAN_B.format('goat')),
                w('cow', ['sapi'], 'A farm animal that gives us milk and says moo.',
                  ask_prefix=HAIWAN_A, help=HAIWAN_B.format('cow')),
                w('chicken', ['ayam'], 'A farm bird that lays eggs and says cluck.',
                  ask_prefix=HAIWAN_A, help=HAIWAN_B.format('chicken')),
                w('deer', ['rusa'], 'A shy brown forest animal; the males have antlers.',
                  ask_prefix=HAIWAN_A, help=HAIWAN_B.format('deer')),
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
            ('Hewan &middot; Animals', [
                w('singa', ['lion'], 'The big cat sometimes called the king of the jungle.'),
                w('kucing', ['cat'], 'A small pet that says meow and chases mice.'),
                w('anjing', ['dog'], 'A pet that barks at strangers and wags its tail.'),
                w('ular', ['snake'], 'A long thin reptile with no legs; some of them are poisonous.'),
                w('tupai', ['squirrel'], 'A small animal with a bushy tail that climbs trees and collects nuts.'),
            ]),
            ('Bagian tubuh hewan &middot; Animal body parts', [
                w('sayap', ['wing', 'wings'], 'A bird flaps these to fly.'),
                w('tanduk', ['horn', 'horns'], 'The hard pointed thing on the head of a bull or a deer.'),
                w('kaki', ['leg', 'legs', 'foot', 'feet'],
                  'The limbs an animal walks on; a cat has four of them.'),
                w('kumis', ['whiskers', 'whisker', 'moustache', 'mustache'],
                  'The long stiff hairs on the face of a cat.'),
                w('taring', ['fang', 'fangs', 'tusk', 'tusks'],
                  'A long sharp tooth of a tiger or a snake.'),
                w('cangkang', ['shell'], 'The hard cover on the back of a tortoise.'),
                w('cakar', ['claw', 'claws'], 'The sharp curved nail of a cat or a tiger.'),
                w('sirip', ['fin', 'fins'], 'A fish uses these to swim.'),
                w('sisik', ['scale', 'scales'], 'The small hard plates that cover a fish or a snake.'),
                w('punuk', ['hump'], 'The lump on the back of a camel.'),
                w('bulu', ['fur', 'feather', 'feathers', 'hair'],
                  'The soft covering on a cat, or on a bird.',
                  reveal='&lt;em&gt;fur&lt;/em&gt; / &lt;em&gt;feathers&lt;/em&gt; (bulu).'),
            ]),
            ('Kata sifat &amp; perbandingan &middot; Adjectives &amp; comparing', [
                w('kecil', ['small', 'little'], 'An ant is ___; an elephant is not.'),
                w('pendek', ['short'], 'The opposite of tall (tinggi); a tortoise is ___.'),
                w('ringan', ['light'],
                  'A feather is ___; the opposite of heavy (berat).',
                  tail='&mdash; think weight, not brightness.',
                  help='(What is &ldquo;ringan&rdquo; in English?)',
                  reveal='&lt;em&gt;light&lt;/em&gt; (ringan, in the sense of weight).'),
                w('lebih', ['more', 'more than', '-er', 'er'],
                  'The word in &ldquo;Gajah ___ besar dari kelinci&rdquo; that makes a comparison.',
                  reveal='&lt;em&gt;more&lt;/em&gt; (lebih), as in &lt;em&gt;lebih besar dari&lt;/em&gt; = bigger than.'),
            ]),
        ],
    ),
]
