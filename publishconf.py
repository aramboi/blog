#!/usr/bin/env python3
import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *  # noqa

SITEURL = 'https://www.angelramboi.com'
FEED_DOMAIN = SITEURL
RELATIVE_URLS = False

# DISQUS_SITENAME = 'altshiftkill'
# DISQUS_ON_PAGES = False

# PIWIK_URL = 'altshiftkill.com/pwk'
# PIWIK_SITE_ID = 1

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
