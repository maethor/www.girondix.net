#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'GirondIX'
SITENAME = u'GirondIX'
#SITEURL = 'ihttp://www.girondix.net'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = "pelican-octopress-theme"

DEFAULT_CATEGORY = "GIX"
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

SLUGIFY_SOURCE = "basename"

MENUITEMS = (('À propos', '/pages/about.html'),
        ('GIX', '/pages/gix.html'),
        ('Services', '/pages/services.html'),
        ('Tarifs', '/pages/tarifs.html'),
        ('Contact', '/pages/contact.html'))

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
