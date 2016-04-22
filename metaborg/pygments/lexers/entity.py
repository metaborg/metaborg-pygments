import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class EntityLexer(RegexLexer):
    name      = 'Entity'
    aliases   = ['entity']
    filenames = ['*.ent']

    tokens = {
        'root': [
            (words(('module','entity','function','return','import',
                    'var'), suffix=r'\b'), Keyword),
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
