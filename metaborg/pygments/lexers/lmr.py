import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class LMRLexer(RegexLexer):
    name      = 'LMR'
    aliases   = ['lmr']
    filenames = ['*.lmr']

    tokens = {
        'root': [
            (r'\d+', Number),
            (words(('def','do','else','extends','if','in','fun','import','let',
                    'letrec','module','new','record','then','with'), suffix=r'\b'), Keyword),
            (words(('true','false'), suffix=r'\b'), Literal),
            (words(('Int','Bool','Num'), suffix=r'\b'), Keyword.Type),
            (r'(:|=|\+|-|\*|/|->|\.)', Operator),
            (r'(\(|\)|\{|\})', Punctuation),
            (r'.', Text),
        ]
    }
