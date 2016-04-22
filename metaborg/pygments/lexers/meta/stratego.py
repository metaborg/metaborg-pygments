import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class StrategoLexer(RegexLexer):
    name      = 'Stratego'
    aliases   = ['stratego', 'str']
    filenames = ['*.str']

    tokens = {
        'root': [
            (words(('module','imports','strategies','rules','where',
                    'with','signature','constructors','sorts','not',
                    'one','some','all','let','in','end','external',
                    'call','if','then','else','switch','case','otherwise',
                    'rec'), suffix=r'\b'), Keyword),
            (r'(\+|\?|!)', Operator),
            (r'"[^"^\n]*"', Literal.String),
            (r'\d+', Literal.Number),
            (r'[\w_-]+', Name.Variable),
            (r'[\,\|\[\]\(\)\{\}\<\>\;\:\=]', Text.Punctuation),
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
