#!/usr/bin/env python3

AUTHOR = 'Angel Ramboi'
SITENAME = 'Angel Ramboi'
SITEURL = 'http://localhost:8000'
FEED_DOMAIN = SITEURL
TAGLINE = 'coder, gamer, geek'

PATH = 'content'

TIMEZONE = 'Europe/Bucharest'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 15

THEME = 'theme/pure-single/'
COVER_IMG_URL = '/images/alt-bg.png'
FAVICON_URL = '/images/alt-favicon.png'
PROFILE_IMG_URL = '/images/me.jpg'

MENUITEMS = [
    ('Archive', '/archives.html'),
    # ('About', '/pages/about.html'),
]

SOCIAL = (
    ('twitter', 'https://twitter.com/angelramboi'),
    ('github', 'https://github.com/aramboi'),
    ('rss', 'http://www.angelramboi.com/feeds/all.atom.xml'),
)

DISPLAY_PAGES_ON_MENU = False

RELATIVE_URLS = False

PLUGINS = ['extended_sitemap']
