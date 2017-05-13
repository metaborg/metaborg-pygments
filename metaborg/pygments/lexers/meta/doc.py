import re
from pygments.lexer import RegexLexer, include
from pygments.filter import Filter
from pygments.token import *

Syntax = Other.Syntax

class BaseDocLexer(RegexLexer):

    tokens = {
        'lex': [
            (r'"', Syntax.Lex.Punctuation.Quote, 'lex-lit'),
            (r'\[', Syntax.Lex.Punctuation, 'lex-class'),
            (r'[\w_\-\']+', Syntax.Lex.Variable),
            (r'[\{\}\(\)]', Syntax.Lex.Punctuation),
            (r'[\?\+\*]', Syntax.Lex.Operator),
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
            (r'"', Syntax.Lex.Punctuation.Quote, '#pop'),
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

        'base-cf': [
            (r'\s+', Text.Whitespace),
            (r'[\w][\w_\-]*', Syntax.CF.Keyword), # heuristic to detect keywords
            (r'[\!\@\#\$\%\^\&\(\)\|\<\>\.\?\+\*\[\]\-\_\:\;\"\'\,\\\{\}\=\~\`]+', Syntax.CF.Punctuation),
            (r'.', Syntax.CF),
        ],
        'cf-<': [
            (r'\<', Syntax.CF.Punctuation.Quote, 'cf-nonterm-<'),
            include('base-cf'),
        ],
        'cf-[': [
            (r'\[', Syntax.CF.Punctuation.Quote, 'cf-nonterm-['),
            include('base-cf'),
        ],
        'cf-nonterm-<': [
            (r'\>', Syntax.CF.Punctuation.Quote, '#pop'), # first, because 'lex' always matches
            include('lex'),
        ],
        'cf-nonterm-[': [
            (r'\]', Syntax.CF.Punctuation.Quote, '#pop'), # first, because 'lex' always matches
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

class DocCFPointyLexer(BaseDocLexer):
    name      = 'DocCFPointy'
    aliases   = ['doc-cf-<']

    tokens = {
        'root': [
            include('cf-<'),
        ],
    }

class DocCFSquareLexer(BaseDocLexer):
    name      = 'DocCFSquare'
    aliases   = ['doc-cf-[']

    tokens = {
        'root': [
            include('cf-['),
        ],
    }

class DocFilter(Filter):

    def __init__(self, **options):
        Filter.__init__(self, **options)

    def filter(self, lexer, stream):
        for ttype, value in stream:
            if ttype in [Syntax.CF.Punctuation.Quote]:
                pass
            else:
                yield ttype, value

