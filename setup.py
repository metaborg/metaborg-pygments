from setuptools import setup, find_packages

meta_lexers = [
    'aterm    = metaborg.pygments.lexers.meta:ATermLexer',
    'esv      = metaborg.pygments.lexers.meta:ESVLexer',
    'nabl     = metaborg.pygments.lexers.meta:NaBLLexer',
    'nabl2    = metaborg.pygments.lexers.meta:NaBL2Lexer',
    'sdf3     = metaborg.pygments.lexers.meta:SDF3Lexer',
    'statix   = metaborg.pygments.lexers.meta:StatixLexer',
    'stratego = metaborg.pygments.lexers.meta:StrategoLexer',
    'dynsem   = metaborg.pygments.lexers.meta:DynSemLexer',
    'doc-lex  = metaborg.pygments.lexers.meta:DocLEXLexer',
    'doc-cf-[ = metaborg.pygments.lexers.meta:DocCFSquareLexer',
    'doc-cf-< = metaborg.pygments.lexers.meta:DocCFPointyLexer',
]

lexers = [
    'entity   = metaborg.pygments.lexers:EntityLexer',
    'fj       = metaborg.pygments.lexers:FJLexer',
    'lmr      = metaborg.pygments.lexers:LMRLexer',
    'pcf      = metaborg.pygments.lexers:PCFLexer',
]

setup(
    name = "metaborg-pygments",
    version = "0.1.dev6",
    packages = find_packages(),
    install_requires = ['Pygments>=2'],
    entry_points = {
        'pygments.lexers' : meta_lexers + lexers,
    },
)
