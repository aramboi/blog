#!/usr/bin/env python3
import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *  # noqa

SITEURL = 'https://www.angelramboi.com'
FEED_DOMAIN = SITEURL
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

OUTPUT_PATH = 'docs/'
DELETE_OUTPUT_DIRECTORY = True
