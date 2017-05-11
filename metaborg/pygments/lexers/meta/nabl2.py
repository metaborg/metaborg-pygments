import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class NaBL2Lexer(RegexLexer):
    name      = 'NaBL2'
    aliases   = ['nabl2']
    filenames = ['*.nabl2']

    tokens = {
        'root': [
            (words(('module',
                    'imports',
                    'signature',
                    'sorts',
                    'constructors',
                    'scope',
                    'occurrence',
                    'namespaces',
                    'name resolution',
                    'labels',
                    'order',
                    'well-formedness',
                    'constraint generator',
                    'rules',
                    'init',
                    'new',
                    'true',
                    'term',
                    'false',
                   ), suffix=r'\b'), Keyword),
            (r'(\=\=|\!\=|(?!\<)\:(?!\=)|\-\>|\<\-|\-.\-\>|\<\-.\-|\=.\=\>|\<\=.\=|\<\:|\<\?)', Operator),
            (r'"[^"^\n]*"', Literal.String),
            (r'\d+', Literal.Number),
            (r'[\w_\-]+\'*', Name.Variable),
            (r'([\,\;\(\)\{\}\.\^]|\[\[|\]\]|\:\=)', Punctuation),
            (r'/\*', Comment.Multiline, 'comment'),
            (r'//.*$', Comment.Singleline),
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
