#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Angel Ramboi'
SITENAME = u'Angel Ramboi'
SITEURL = 'http://localhost:8000'
FEED_DOMAIN = SITEURL
TAGLINE = u'coder, gamer, geek'

PATH = 'content'

TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 15

THEME = 'theme/pure-single/'
COVER_IMG_URL = '/images/alt-bg.png'
FAVICON_URL = '/images/alt-favicon.png'
PROFILE_IMG_URL = '/images/me.jpg'

MENUITEMS = [
    ('Archive', '/archives.html'),
    # ('About', '/about.html'),
]

SOCIAL = (
    ('twitter', 'https://twitter.com/AngelRamboi'),
    ('github', 'https://github.com/aramboi'),
    ('rss', 'http://altshiftkill.com/feeds/all.atom.xml'),
)

DISPLAY_PAGES_ON_MENU = False

RELATIVE_URLS = False
