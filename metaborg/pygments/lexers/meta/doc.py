import re
from pygments.lexer import RegexLexer, include
from pygments.filter import Filter
from pygments.token import *

Syntax = Other.Syntax

class BaseDocLexer(RegexLexer):

    tokens = {
        'lex': [
            (r'"', Syntax.Lex.Marker, 'lex-lit'),
            (r'\[', Syntax.Lex.Punctuation, 'lex-class'),
            (r'[\w_\-\']+', Syntax.Lex.Variable),
            (r'[\{\}\?\+\*\(\)]', Syntax.Lex.Punctuation),
            (r'/\*', Comment.Multiline, 'comment'),
            (r'//.*$', Comment.Singleline),
            (r'\s+', Text.Whitespace),
            (r'.', Syntax.Lex),
        ],
        'comment': [
            (r'[^*/]', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline)
        ],

        'lex-lit': [
            (r'\\', Syntax.Lex.Punctuation, 'lex-lit-escape'),
            (r'"', Syntax.Lex.Marker, '#pop'),
            (r'.', Syntax.Lex.Literal),
        ],
        'lex-lit-escape': [
            (r'.', Syntax.Lex.Literal, '#pop'),
        ],

        'lex-class': [
            (r'\\', Syntax.Lex.Punctuation, 'lex-class-escape'),
            (r'\]', Syntax.Lex.Punctuation, '#pop'),
            (r'\-', Syntax.Lex.Punctuation),
            (r'.', Syntax.Lex.Char),
        ],
        'lex-class-escape': [
            (r'.', Syntax.Lex.Char, '#pop'),
        ],

        'cf': [
            (r'\\\<', Syntax.CF.Marker, 'cf-nonterm-<'),
            (r'\\\[', Syntax.CF.Marker, 'cf-nonterm-['),
            (r'\s+', Text.Whitespace),
            (r'[\w][\w_\-]*', Syntax.CF.Keyword), # heuristic to detect keywords
            (r'[\!\@\#\$\%\^\&\(\)\|\<\>\.\?\+\*\[\]\-\_\:\;\"\'\,\\\{\}\=\~\`]+', Syntax.CF.Punctuation),
            (r'.', Syntax.CF),
        ],
        'cf-nonterm-<': [
            (r'\>', Syntax.CF.Marker, '#pop'), # first, because 'lex' always matches
            include('lex'),
        ],
        'cf-nonterm-[': [
            (r'\]', Syntax.CF.Marker, '#pop'), # first, because 'lex' always matches
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
            if ttype is Syntax.Lex.Marker:
                yield Syntax.Lex.Punctuation, value
            elif ttype is Syntax.CF.Marker:
                pass
            else:
                yield ttype, value
