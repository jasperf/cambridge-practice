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
    out='s2/sem1/sem1-bahasa-indonesia-vocab-2',
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
    back='../../index.html',
)


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
              'do not matter and hyphens are optional (<em>kupu-kupu</em> = <em>kupu kupu</em>). Press '
              '<strong>Check</strong> or <strong>Enter</strong>. The <strong>Hint</strong> button describes '
              'the word in other words &mdash; it never contains the answer itself.'),
        groups=[
            ('Kelas &amp; sekolah &middot; Classroom &amp; school', [
                w('door', ['pintu'],
                  'You open it to walk into the room and close it behind you.'),
                w('desk', ['meja', 'meja tulis'],
                  'A flat top on legs that you work at in the classroom.'),
                w('book', ['buku'],
                  'It has pages and you read it.'),
                w('pen', ['pulpen', 'pen', 'pena'],
                  'You write with this; it uses ink and never needs sharpening.'),
                w('pencil', ['pensil'],
                  'You write with this; it makes a grey line and needs sharpening.'),
                w('map', ['peta'],
                  'A drawing that shows where countries, cities and roads are.'),
                w('classroom', ['kelas', 'ruang kelas', 'ruangkelas'],
                  'The room where you have lessons with your teacher.'),
                w('school', ['sekolah'],
                  'The place you go every morning to learn, with teachers and lessons.'),
                w('eraser', ['penghapus'],
                  'It removes pencil marks when you make a mistake.'),
                w('dictionary', ['kamus'],
                  'A thick book that lists words and their meanings in two languages.'),
            ]),
            ('Iklan &amp; belanja &middot; Advertisements &amp; shopping', [
                w('advertisement', ['iklan'],
                  'A short text or picture that tries to make you buy something.'),
                w('to buy', ['membeli', 'beli'],
                  'The verb for paying money to get something.'),
                w('to sell', ['menjual', 'jual'],
                  'The verb for giving something away in exchange for money.'),
                w('cheap', ['murah'],
                  'Adjective for something that costs very little money.'),
                w('expensive', ['mahal'],
                  'Adjective for something that costs a lot of money.'),
                w('new', ['baru'],
                  'The opposite of old (lama).'),
                w('quality', ['kualitas', 'mutu'],
                  'How good or bad something is; advertisements always say theirs is high.'),
                w('shop', ['toko'],
                  'A place where you can buy things; the mall is full of them.'),
            ]),
            ('Kata tanya &middot; Question words', [
                w('where', ['di mana', 'dimana'],
                  'Ask this question word to learn about a place.',
                  placeholder='di &hellip;'),
                w('who', ['siapa'],
                  'Ask this question word to learn about a person.'),
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
                w('singa', ['lion'],
                  'The big cat sometimes called the king of the jungle.'),
                w('kucing', ['cat'],
                  'A small pet that says meow and chases mice.'),
                w('anjing', ['dog'],
                  'A pet that barks at strangers and wags its tail.'),
                w('burung', ['bird'],
                  'An animal with feathers and wings that can usually fly.'),
                w('kupu-kupu', ['butterfly'],
                  'An insect with big colourful wings; it used to be a caterpillar.'),
                w('ular', ['snake'],
                  'A long thin reptile with no legs; some of them are poisonous.'),
                w('buaya', ['crocodile'],
                  'A big green reptile with a long snout and many teeth that lives in rivers.'),
                w('badak', ['rhinoceros', 'rhino'],
                  'A huge grey animal with a horn on its nose.'),
            ]),
            ('Bagian tubuh &middot; Body parts', [
                w('sayap', ['wing', 'wings'],
                  'A bird flaps these to fly.'),
                w('tanduk', ['horn'],
                  'The hard pointed thing on the head of a rhinoceros or a bull.'),
                w('kaki', ['leg', 'legs', 'foot', 'feet'],
                  'The limbs an animal walks on; you have two of them.'),
            ]),
            ('Kata sifat &middot; Adjectives', [
                w('besar', ['big', 'large'],
                  'An elephant is ___; an ant is not.'),
                w('kecil', ['small', 'little'],
                  'An ant is ___; an elephant is not.'),
                w('tinggi', ['tall', 'high'],
                  'A giraffe is ___; a tortoise is not.'),
                w('lucu', ['funny', 'cute'],
                  'When something makes you laugh, you say it is ___.'),
            ]),
            ('Kata kerja &middot; Verbs', [
                w('makan', ['eat', 'to eat', 'eating'],
                  'You do this three times a day, with rice and vegetables.'),
                w('minum', ['drink', 'to drink', 'drinking'],
                  'You do this with water when you are thirsty.'),
                w('tidur', ['sleep', 'to sleep', 'sleeping'],
                  'You do this in your bed at night with your eyes closed.'),
                w('bermain', ['play', 'to play', 'playing'],
                  'Children do this in the playground; football is one way to do it.'),
            ]),
            ('Kata tanya &middot; Question words', [
                w('bagaimana', ['how'],
                  'Ask this question word to learn the way something is done.'),
            ]),
        ],
    ),
]
