import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class SDF3Lexer(RegexLexer):
    name      = 'SDF3'
    aliases   = ['sdf3']
    filenames = ['*.sdf3']

    tokens = {
        'root': [
            (words(('module','imports','sorts','lexical','context-free',
                    'start-symbols','syntax','hide','text','templates',
                    'template options','tokenize','newlines','none',
                    'separating','leading','trailing','reject','prefer',
                    'avoid','priorities','bracket','left','right',
                    'non-assoc','longest-match'), suffix=r'\b'), Keyword),
            (r'(\+|\?|\*)', Operator),
            (r'"[^"^\n]*"', Literal.String),
            (r'\d+', Literal.Number),
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
