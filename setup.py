from setuptools import setup, find_packages
setup(
    name = "metaborg-pygments",
    version = "0.1.dev",
    packages = find_packages(),
    install_requires = ['Pygments>=2'],
    entry_points = {
        'pygments.lexers' : [
            'aterm    = metaborg.pygments.lexers:ATermLexer',
            'entity   = metaborg.pygments.lexers:EntityLexer',
            'esv      = metaborg.pygments.lexers:ESVLexer',
            'fj       = metaborg.pygments.lexers:FJLexer',
            'lmr      = metaborg.pygments.lexers:LMRLexer',
            'nabl     = metaborg.pygments.lexers:NaBLLexer',
            'pcf      = metaborg.pygments.lexers:PCFLexer',
            'sdf3     = metaborg.pygments.lexers:SDF3Lexer',
            'stratego = metaborg.pygments.lexers:StrategoLexer',
        ],
    },
)
