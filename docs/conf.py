# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from sphinx_typlog_theme import __version__
from sphinx_typlog_theme import add_badge_roles, add_github_roles

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
source_suffix = '.rst'

master_doc = 'index'

# General information about the project.
project = u'Sphinx Typlog Theme'
copyright = u'2017, Hsiaoming Yang'
author = u'Hsiaoming Yang'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_typlog_theme'
html_theme_options = {
    'color': '#E8371A',
    'logo': 'typlog-512.png',
    'navs': [
        {
            'url': 'https://typlog.com',
            'title': 'Typlog'
        },
        {
            'url': 'https://github.com/typlog',
            'title': 'GitHub'
        }
    ],
    'description': 'A sphinx theme designed by Typlog.',
    'github_user': 'lepture',
    'github_repo': 'authlib',
    'meta_html': '<meta name="generator" content="sphinx">',
}
html_theme_path = [".."]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_sidebars = {
    '**': [
        'project.html',
        'localtoc.html',
        'relations.html',
        'sponsors.html',
        'searchbox.html',
    ]
}


def setup(app):
    add_badge_roles(app)
    add_github_roles(app, 'lepture/authlib')
