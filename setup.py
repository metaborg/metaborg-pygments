from setuptools import setup, find_packages

lexers = [
    'aterm    = metaborg.pygments.lexers.meta:ATermLexer',
    'esv      = metaborg.pygments.lexers.meta:ESVLexer',
    'nabl     = metaborg.pygments.lexers.meta:NaBLLexer',
    'sdf3     = metaborg.pygments.lexers.meta:SDF3Lexer',
    'stratego = metaborg.pygments.lexers.meta:StrategoLexer',
    'dynsem   = metaborg.pygments.lexers.meta:DynSemLexer',
]

meta_lexers = [
    'entity   = metaborg.pygments.lexers:EntityLexer',
    'fj       = metaborg.pygments.lexers:FJLexer',
    'lmr      = metaborg.pygments.lexers:LMRLexer',
    'pcf      = metaborg.pygments.lexers:PCFLexer',
]

setup(
    name = "metaborg-pygments",
    version = "0.1.dev",
    packages = find_packages(),
    install_requires = ['Pygments>=2'],
    entry_points = {
        'pygments.lexers' : lexers + meta_lexers,
    },
)
