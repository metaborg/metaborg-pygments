import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class StatixLexer(RegexLexer):
    name      = 'Statix'
    aliases   = ['statix']
    filenames = ['*.stx', '*.stxtest']

    tokens = {
        'root': [
            (words(('_PathEmpty',
                    '_PathStep',
                    'and',
                    'astId'
                    'constraints',
                    'constructors',
                    'decl',
                    'div',
                    'false',
                    'filter',
                    'imports',
                    'in',
                    'int',
                    'label',
                    'labels',
                    'list',
                    'maps',
                    'max',
                    'min',
                    'mod',
                    'module',
                    'name-resolution',
                    'namespace',
                    'namespaces',
                    'new',
                    'occurrence',
                    'path',
                    'query',
                    'ref',
                    'relations',
                    'resolve',
                    'rules',
                    'scope',
                    'signature',
                    'sorts',
                    'string',
                    'true',
                    'with',
                   ), suffix=r'\b'), Keyword),
            (r'(\=\=|\!\=|\:\=|\-\>|\-[\w]+\-\>|\|\-\>|\#(\=|\\\=|\>\=|\=\<|\<|\>))', Operator),
            (r'"[^"^\n]*"', Literal.String),
            (r'\d+', Literal.Number),
            (r'[\w_\-]+\'*', Name.Variable),
            (r'([\,\;\:\(\)\{\}\.\^]|\[\[|\]\]|\-\>)', Punctuation),
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
