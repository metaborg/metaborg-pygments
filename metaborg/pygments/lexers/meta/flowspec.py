import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class FlowSpecLexer(RegexLexer):
    name      = 'FlowSpec'
    aliases   = ['flowspec']
    filenames = ['*.flo']

    tokens = {
        'root': [
            (words(('module',
                    'imports',
                    'external',
                    'control-flow rules',
                    'root',
                    'start',
                    'end',
                    'entry',
                    'exit',
                    'node',
                    'this',
                    'properties',
                    'types',
                    'name',
                    'term',
                    'position',
                    'int',
                    'string',
                    'float',
                    'bool',
                    'Map',
                    'Set',
                    'lattices',
                    'where',
                    'type',
                    'lub',
                    'top',
                    'bottom',
                    'glb',
                    'leq',
                    'geq',
                    'nleq',
                    'if',
                    'lthen',
                    'else',
                    'match',
                    'with',
                    'true',
                    'false',
                   ), suffix=r'\b'), Keyword),
            (r'(\=\=|\!\=|\&\&|\|\||\!|\<|\<\=|\>|\>\=|\+|\-|\*|\/|\%|\||\<\-|\|\-\>|\\\/|\\|\/\\|\=\>)', Operator),
            (r'"[^"^\n]*"', Literal.String),
            (r'\d+', Literal.Number),
            (r'[\w_\-]+\'*', Name.Variable),
            (r'([\,\|\=\.])', Punctuation),
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
