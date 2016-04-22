import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class ATermLexer(RegexLexer):
    name      = 'ATerm'
    aliases   = ['aterm']
    filenames = ['*.aterm']

    tokens = {
        'root': [
            (r'"[^"^\n]*"', Literal.String),
            (r'\d+', Literal.Number),
            (r'[\.\,\|\[\]\(\)\{\}]', Text.Punctuation),
            (r'\s+', Text.Whitespace),
            (r'.', Text),
            ],
        }
