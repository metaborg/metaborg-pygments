import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class FJLexer(RegexLexer):
    name      = 'Featherweight Java'
    aliases   = ['fj']
    filenames = ['*.fj']

    tokens = {
        'root': [
            (r'\d+', Number),
            (words(('class','extends','new','return'), suffix=r'\b'), Keyword),
            (words(('super','this'), suffix=r'\b'), Literal),
            (r'\.', Operator),
            (r'(\{|\}|\(|\)|;)', Punctuation),
            (r'.', Text),
        ]
    }
