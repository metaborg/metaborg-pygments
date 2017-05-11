import re
from pygments.lexer import RegexLexer, include
from pygments.filter import Filter
from pygments.token import *

Syntax = Other.Syntax

class BaseDocLexer(RegexLexer):

    tokens = {
        'lex': [
            (r'"', Syntax.Meta.Marker.Lex, 'lex-lit'),
            (r'\[', Syntax.Meta.Punctuation, 'lex-class'),
            (r'[\w_\-\']+', Syntax.Meta.Variable),
            (r'[\{\}\?\+\*\(\)]', Syntax.Meta.Punctuation),
            (r'/\*', Comment.Multiline, 'comment'),
            (r'//.*$', Comment.Singleline),
            (r'\s+', Text.Whitespace),
            (r'.', Generic.Deleted),
        ],
        'comment': [
            (r'[^*/]', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline)
        ],

        'lex-lit': [
            (r'\\', Syntax.Meta.Punctuation, 'lex-lit-escape'),
            (r'"', Syntax.Meta.Marker.Lex, '#pop'),
            (r'.', Syntax.Object),
        ],
        'lex-lit-escape': [
            (r'.', Syntax.Object, '#pop'),
        ],

        'lex-class': [
            (r'\\', Syntax.Meta.Punctuation, 'lex-class-escape'),
            (r'\]', Syntax.Meta.Punctuation, '#pop'),
            (r'\-', Syntax.Meta.Punctuation),
            (r'.', Syntax.Object.Char),
        ],
        'lex-class-escape': [
            (r'.', Syntax.Object.Char, '#pop'),
        ],

        'cf': [
            (r'\\\<', Syntax.Meta.Marker.CF, 'cf-nonterm-<'),
            (r'\\\[', Syntax.Meta.Marker.CF, 'cf-nonterm-['),
            (r'\s+', Text.Whitespace),
            (r'.', Syntax.Object),
        ],
        'cf-nonterm-<': [
            (r'\>', Syntax.Meta.Marker.CF, '#pop'), # first, because 'lex' always matches
            include('lex'),
        ],
        'cf-nonterm-[': [
            (r'\]', Syntax.Meta.Marker.CF, '#pop'), # first, because 'lex' always matches
            include('lex'),
        ],
    }

    def __init__(self, **options):
        RegexLexer.__init__(self, **options)
        self.add_filter(DocFilter())

class DocLEXLexer(BaseDocLexer):
    name      = 'DocLEX'
    aliases   = ['doc-lex']

    tokens = {
        'root': [
            include('lex')
        ],
    }

class DocCFLexer(BaseDocLexer):
    name      = 'DocCF'
    aliases   = ['doc-cf']

    tokens = {
        'root': [
            include('cf')
        ],
    }

class DocFilter(Filter):

    def __init__(self, **options):
        Filter.__init__(self, **options)

    def filter(self, lexer, stream):
        for ttype, value in stream:
            if ttype is Syntax.Meta.Marker.Lex:
                yield Syntax.Meta.Punctuation, value
            elif ttype is Syntax.Meta.Marker.CF:
                pass
            else:
                yield ttype, value
