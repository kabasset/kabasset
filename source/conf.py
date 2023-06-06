# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from datetime import datetime
import locale

project = 'Antoine Basset'
release = '1.0'
author = 'Antoine Basset'
language = 'en'
locale.setlocale(locale.LC_TIME, 'en_US.utf8')

now = datetime.now()
init_year = 2023
copyright_years = now.year if now.year == init_year else f'{init_year}-{now.year}'
copyright = f'{copyright_years}, Antoine Basset'
# FIXME use html_last_updated_fmt if working
copyright += f'. Last updated on {now.strftime("%A, %B %d, %Y")}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.githubpages']
source_suffix = '.rst'
templates_path = ['_templates']
master_doc = 'index'
exclude_patterns = ['_build']
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_theme_path = ['_themes']
html_favicon = 'favicon.png'
html_css_files = ['custom.css']

html_use_index = False
html_permalinks = False
html_copy_source = False
html_show_sourcelink = False
html_show_copyright = True

html_theme_options = {
    # 'fixed_sidebar': True,  # Cannot search if window is too small
    'show_relbars': True,
}

# -- Options for BibTeX ------------------------------------------------------
# https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html#configuration

extensions.append('sphinxcontrib.bibtex')
bibtex_bibfiles = ['journals.bib', 'proceedings.bib', 'theses.bib']
bibtex_default_style = 'unsrt'
