import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class NaBLLexer(RegexLexer):
    name      = 'NaBL'
    aliases   = ['nabl']
    filenames = ['*.nab']

    tokens = {
        'root': [
            (words(('namespaces','rules','defines','non-unique','unique','module',
                    'refers to','otherwise','scopes','in','subsequent scope','where',
                    'has','type','imports','from','of'), suffix=r'\b'), Keyword),
            (r'"[^"^\n]*"', Literal.String),
            (r'[\w_-]+', Name.Variable),
            (r'[\.\,\|\[\]\(\)\{\}\<\>\;\:]', Text.Punctuation),
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
