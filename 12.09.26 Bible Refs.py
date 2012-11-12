import os

import yaml
from jinja2 import Environment, FileSystemLoader

current_dir = os.path.dirname(os.path.realpath(__file__))

yaml_file = open(os.path.join(current_dir, '12.09.26 Bible Refs.yaml'))

books = [
    'General',

    'Genesis',
    'Exodus',
    'Leviticus',
    'Numbers',
    'Deuteronomy',

    'Joshua',
    'Ruth',
    '1 Samuel',
    '2 Samuel',
    '1 Kings',
    '2 Kings',
    '1 Chronicles',
    '2 Chronicles',

    'Ezra',
    'Nehemiah',
    'Tobit',
    'Tobias',
    'Judith',
    'Esther',
    '1 Maccabees',
    '2 Maccabees',

    'Job',
    'Psalms',
    'Proverbs',
    'Ecclesiastes',
    'Song of Solomon',
    'Wisdom',
    'Sirach',

    'Isaiah',
    'Jeremiah',
    'Lamentations',
    'Baruch',
    'Ezekiel',
    'Daniel',

    'Hosea',
    'Joel',
    'Amos',
    'Obadiah',
    'Jonah',
    'Micah',
    'Nahum',
    'Habakkuk',
    'Zephaniah',
    'Haggai',
    'Zechariah',
    'Malachi',

    'Matthew',
    'Mark',
    'Luke',
    'John',

    'Acts',

    'Romans',
    '1 Corinthians',
    '2 Corinthians',
    'Galatians',
    'Ephesians',
    'Philippians',
    'Colossians',
    '1 Thessalonians',
    '2 Thessalonians',
    '1 Timothy',
    '2 Timothy',
    'Titus',
    'Philemon',

    'Hebrews',
    'James',
    '1 Peter',
    '2 Peter',
    '1 John',
    '2 John',
    '3 John',
    'Jude',

    'Revelation',
]


class Reference(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
refs = []
for ref in yaml.load_all(yaml_file.read()):
    book = ref['bible'].get('book') or 'General'
    source = ref['ref'].get('source')
    if ' by ' in source:
        sub_source = source[source.find(' by '):]
        source = source[:source.find(' by ')]
    else:
        sub_source = ''
    r = Reference(
        book=book,
        passage=ref['bible'].get('passage'),
        quote=ref['bible'].get('quote'),
        expln=ref['bible'].get('expln'),
        text=ref['ref'].get('text'),
        source=source,
        sub_source=sub_source,
        image=ref['ref'].get('image')
    )
    refs.append(r)
refs.sort(key=lambda ref: books.index(ref.book))

loader = FileSystemLoader(current_dir)
env = Environment(trim_blocks=True, loader=loader)
context = {
    'refs': refs,
}
html = env.get_template('12.09.26 Bible Refs.html.jinja2').render(**context)
print html
