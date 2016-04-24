# Pygments Lexers for Spoofax Languages

This package adds syntax coloring support for Spoofax meta-languages and research languages to [Pygments](http://pygments.org/). The languages can be used in [Sphinx](http://www.sphinx-doc.org/) documentation, and in LaTeX documents, using the [Minted](https://www.ctan.org/tex-archive/macros/latex/contrib/minted/) package.

## Usage

To install the package, run

    python setup.py install

or add the following line to the `requirements.txt` of a project

    git+https://github.com/metaborg/metaborg-pygments#egg=metaborg-pygments

## Development

To develop the package, run

    python setup.py develop

which will make the source tree appear as a locally installed package.
