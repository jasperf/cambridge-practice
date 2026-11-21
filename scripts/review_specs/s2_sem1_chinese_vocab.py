"""Spec: Secondary 2 · Chinese — Vocabulary Drill (English ↔ Chinese).

Build with:  python3 scripts/build_vocab_drill.py scripts/review_specs/s2_sem1_chinese_vocab.py

40 typed-answer questions from the Semester 1 Chinese revision worksheet
(Seasons, Occupations, Shopping from Easy Steps to Chinese 3), practised in
both directions: 20 English -> Chinese characters and 20 Chinese -> English.
No word repeats. Typed answers only, hints describe the word without giving
it away. Chinese punctuation is ignored when matching.
"""

META = dict(
    out='s2/sem1/sem1-chinese-vocab',
    title='Chinese Vocabulary Drill &middot; Semester 1',
    badge='Chinese &middot; Vocabulary Drill',
    eyebrow='Secondary 2 &middot; Chinese L2 &middot; Semester 1 Vocabulary',
    h1='Vocabulary Drill<br><em>English &harr; Chinese</em>',
    credit=('40 words from the Semester 1 Chinese revision worksheet &mdash; weather and seasons, jobs and places, '
            'clothes and shopping, and the writing words &mdash; practised in both directions. Section A: type the '
            'Chinese characters. Section B: type the English meaning of the characters (no pinyin, as in the exam; it appears with the answer). '
            'Press Check (or Enter), and use Hint for a description in other words.'),
    md_title='Secondary 2 &middot; Chinese — Vocabulary Drill',
    md_intro=('40 words from the Semester 1 Chinese revision worksheet — weather and seasons, jobs and places, '
              'clothes and shopping, and the writing words — practised in both directions: Section A is English '
              '→ Chinese characters, Section B is Chinese → English. Write your answers in the blanks; the answer '
              'sheet lists every accepted answer.'),
    answers_note=('Answers for the Chinese Vocabulary Drill, both directions. On the interactive sheet '
                  '(sem1-chinese-vocab.html) the marking is automatic and accepts every answer listed here.'),
    storage_key='sem1-chinese-vocab',
    back='../../index.html',
    lang=dict(
        ask_target='Type the Chinese characters for',
        ask_source='What does <em>{w}</em> mean in English?',
        help_target='(Write the {noun} in characters, not pinyin.)',
        help_source='(Read the characters, no pinyin. What is it in English?)',
        chip_target='EN &rarr; ZH',
        chip_source='ZH &rarr; EN',
        placeholder='汉字 / characters&hellip;',
        strip='。，、！？；：…',
        extra_css=("body, .text-input, .q-text, .q-en, .info-box { font-family: var(--font-body), 'PingFang SC', "
                   "'Hiragino Sans GB', 'Noto Sans SC', 'Microsoft YaHei', sans-serif; }\n"
                   ".text-input { font-family: var(--font-body), 'PingFang SC', 'Noto Sans SC', 'Microsoft YaHei', sans-serif; }"),
    ),
)


def zh(en, ans, hint):
    return dict(a=en, ans=ans, hint=hint)


def en(word, py, ans, hint):
    # pinyin is shown only in the revealed answer, never in the question (the exam shows characters only)
    return dict(a=word, ans=ans, hint=hint, note=f' Pinyin: {py}.')


SECTIONS = [
    dict(
        key='en', anchor='en',
        tab='&#128203; A &middot; English &rarr; Chinese',
        icon='&#128203;', dir='en-id',
        label='Section A &middot; English &rarr; Chinese',
        title='Write it in Chinese',
        score_label='SECTION A &mdash; ENGLISH &rarr; CHINESE',
        js_label='English \\u2192 Chinese',
        info=('Type the <strong>Chinese characters</strong> (simplified) for each English word, using your pinyin '
              'keyboard. Press <strong>Check</strong> or <strong>Enter</strong>. The <strong>Hint</strong> button '
              'describes the word in other words and tells you how many characters it has &mdash; it never '
              'contains the answer itself.'),
        groups=[
            ('天气与季节 &middot; Weather &amp; seasons', [
                zh('spring', ['春天'], 'The season when flowers open and it gets warmer. 2 characters.'),
                zh('summer', ['夏天'], 'The hottest season of the year. 2 characters.'),
                zh('autumn', ['秋天'], 'The season between summer and winter when leaves fall. 2 characters.'),
                zh('winter', ['冬天'], 'The coldest season. 2 characters.'),
                zh('warm (comfortably)', ['暖和'], 'Not cold, a pleasant temperature in spring. 2 characters.'),
                zh('cool (pleasantly)', ['凉快'], 'Not hot, a fresh feeling in autumn. 2 characters.'),
                zh('umbrella', ['雨伞'], 'You hold it over your head when it rains. 2 characters.'),
            ]),
            ('职业与地点 &middot; Jobs &amp; places', [
                zh('doctor', ['医生'], 'The person who treats sick patients. 2 characters.'),
                zh('lawyer', ['律师'], 'A person who helps people with the law. 2 characters.'),
                zh('manager', ['经理'], 'The person in charge of a team at a company. 2 characters.'),
                zh('hospital', ['医院'], 'The building where sick people are treated. 2 characters.'),
                zh('law firm', ['律师事务所'], 'The office where lawyers work. 5 characters.'),
                zh('shop', ['商店'], 'A place where you go to buy things. 2 characters.'),
            ]),
            ('服装与购物 &middot; Clothes &amp; shopping', [
                zh('leather shoes', ['皮鞋'], 'Smart shoes made from animal skin. 2 characters.'),
                zh('high-heeled shoes', ['高跟鞋'], 'Shoes with a tall heel. 3 characters.'),
                zh('trainers / sports shoes', ['运动鞋'], 'The shoes you wear to play sport. 3 characters.'),
                zh('school bag', ['书包'], 'You carry your books to school in it. 2 characters.'),
                zh('coat / jacket', ['外套'], 'You wear it over your clothes when it is cold. 2 characters.'),
            ]),
            ('写作词语 &middot; Writing words', [
                zh('shopping', ['购物'], 'The activity of going out to buy things. 2 characters.'),
                zh('together', ['一起'], 'Doing something with other people. 2 characters.'),
            ]),
        ],
    ),
    dict(
        key='zh', anchor='zh',
        tab='&#128214; B &middot; Chinese &rarr; English',
        icon='&#128214;', dir='id-en',
        label='Section B &middot; Chinese &rarr; English',
        title='Write it in English',
        score_label='SECTION B &mdash; CHINESE &rarr; ENGLISH',
        js_label='Chinese \\u2192 English',
        placeholder='English&hellip;',
        info=('Type the <strong>English</strong> meaning of each Chinese word. There is no pinyin in the '
              'question, as in the exam; it appears when you reveal the answer. Capital letters do not matter. Press <strong>Check</strong> or '
              '<strong>Enter</strong>. The <strong>Hint</strong> button describes the meaning in other words.'),
        groups=[
            ('天气与季节 &middot; Weather &amp; seasons', [
                en('热', 'rè', ['hot', 'it is hot', 'very hot'], 'The feeling of a summer day in Jakarta.'),
                en('冷', 'lěng', ['cold', 'it is cold', 'very cold'], 'The feeling of winter, the opposite of hot.'),
                en('下雨', 'xià yǔ', ['rain', 'to rain', 'it rains', 'it is raining', 'raining', 'rains'],
                   'Water falling from the clouds, so you need an umbrella.'),
            ]),
            ('职业与地点 &middot; Jobs &amp; places', [
                en('公司', 'gōngsī', ['company', 'a company', 'firm', 'business'],
                   'A business where many employees work and a manager runs a team.'),
            ]),
            ('服装与购物 &middot; Clothes &amp; shopping', [
                en('衣服', 'yīfu', ['clothes', 'clothing', 'clothes (general)', 'a piece of clothing', 'garment'],
                   'What you wear on your body each day.'),
                en('一双', 'yì shuāng', ['a pair', 'a pair of', 'pair', 'one pair', 'a pair (of shoes)'],
                   'The measure word you use for shoes, because they come two at a time.'),
                en('一件', 'yí jiàn', ['a piece', 'a piece of', 'one piece', 'a piece (of clothing)', 'piece', 'an item'],
                   'The measure word you use for one coat or one shirt.'),
                en('多少钱', 'duōshao qián', ['how much', 'how much money', 'how much is it', 'how much does it cost', 'how much is this', 'how much is that'],
                   'The question you ask a shop assistant about the price.'),
                en('太贵了', 'tài guì le', ['too expensive', 'it is too expensive', "it's too expensive", 'so expensive', 'very expensive', 'too dear'],
                   'What you say when the price is higher than you want to pay.'),
                en('便宜', 'piányi', ['cheap', 'inexpensive', 'cheaper', 'low price'],
                   'The opposite of expensive.'),
                en('合适', 'héshì', ['suitable', 'fits well', 'fit', 'a good fit', 'appropriate', 'just right', 'right', 'fits'],
                   'Shoes that are the right size and style for you are this.'),
                en('价格', 'jiàgé', ['price', 'the price', 'cost'],
                   'The number written on a tag in a shop.'),
            ]),
            ('写作词语 &middot; Writing words', [
                en('打算', 'dǎsuàn', ['plan', 'plan to', 'to plan', 'intend', 'intend to', 'to intend', 'be going to'],
                   'What you do when you decide what to do tomorrow.'),
                en('准备', 'zhǔnbèi', ['prepare', 'to prepare', 'get ready', 'to get ready', 'be ready', 'intend', 'intend to', 'plan to', 'prepare to'],
                   'To get ready, for example how much money to bring.'),
                en('觉得', 'juéde', ['think', 'feel', 'to think', 'to feel', 'think that', 'feel that', 'i think', 'to think/feel'],
                   'The verb that starts your opinion in a sentence.'),
                en('后来', 'hòulái', ['later', 'afterwards', 'afterward', 'after that', 'then', 'later on', 'after'],
                   'A word that links two events in a story, the second one after the first.'),
                en('因为……所以……', 'yīnwèi … suǒyǐ …', ['because so', 'because therefore', 'because ... so ...', 'because...so...', 'because … so …', 'because……so……', 'because, so', 'because/so', 'because so'],
                   'A pair of words: the first gives the reason, the second gives the result.'),
                en('虽然……但是……', 'suīrán … dànshì …', ['although but', 'although however', 'although ... but ...', 'although...but...', 'although … but …', 'although……but……', 'although, but', 'although/but', 'though but'],
                   'A pair of words that shows a contrast between two ideas.'),
            ]),
            ('时间与感受 &middot; Time &amp; feelings', [
                en('星期六', 'xīngqīliù', ['saturday', 'on saturday'], 'The sixth day of the Chinese week, the start of the weekend.'),
                en('开心', 'kāixīn', ['happy', 'glad', 'cheerful', 'pleased', 'joyful', 'in a good mood'],
                   'How you feel after a fun day of shopping.'),
            ]),
        ],
    ),
]
