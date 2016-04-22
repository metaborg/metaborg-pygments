import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class PCFLexer(RegexLexer):
    name      = 'PCF'
    aliases   = ['pcf']
    filenames = ['*.pcf']

    tokens = {
        'root': [
            (r'\d+', Number),
            (words(('else','in','ifz','fun','fix','let','then'), suffix=r'\b'), Keyword),
            (r'(=|\+|-|\*|/|->)', Operator),
            (r'.', Text),
        ]
    }
