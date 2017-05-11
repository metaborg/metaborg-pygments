import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class DynSemLexer(RegexLexer):
    name      = 'DynSem'
    aliases   = ['dynsem', 'ds']
    filenames = ['*.ds']

    tokens = {
        'root': [
            (words(('module','imports','signature', 'sorts', 'sort aliases',
                    'variables','arrows','rules','where','constructors',
                    'true','false','native','operators','datatypes',
                    'implicit','List','Map','fresh','allkeys','allvalues',
                    'try','or','case','of','otherwise', 'components'), suffix=r'\b'), Keyword),
            (r'(--\>|\:\:|==|=\>|=!=\>)', Operator),
            (r'"[^"^\n]*"', Literal.String),
            (r'\d+', Literal.Number),
            (r'[\w_-]+', Name.Variable),
            (r'[\,\|\[\]\(\)\{\}\;]', Text.Punctuation),
            (r'/\*', Comment.Multiline, 'comment'),
            (r'//.*?$', Comment.Singleline),
            (r'\s+', Text.Whitespace),
            (r'.', Text),
        ],
        'comment': [
            (r'[^*/]', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline)
        ],
    }
