#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'All-Stars'
SITENAME = u'HardCoreAI'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DISPLAY_CATEGORIES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/HardCoreAI'),
        ('github', 'https://github.com/HardCoreAI'),)

GITHUB_URL = 'https://github.com/HardCoreAI'
DEFAULT_PAGINATION = 10

# Wesite Theme
THEME = "/Users/Victor_Hao/Downloads/hardcoreai_blog/blog_src/pelican-themes/clean-blog"
PLUGIN_PATHS = ["/Users/Victor_Hao/Downloads/hardcoreai_blog/blog_src/pelican-plugins"]
PLUGINS = ["render_math"]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
