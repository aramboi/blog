#!/usr/bin/env python3
import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *  # noqa

SITEURL = 'https://www.angelramboi.com'
FEED_DOMAIN = SITEURL

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'docs/'

UTTERANCES_REPO = 'aramboi/blog'
UTTERANCES_MAPPING = 'title'
UTTERANCES_LABEL = 'comments'
UTTERANCES_THEME = 'github-light'

ANALYTICS_TAGS = '''<!-- Panelbear Analytics - We respect your privacy -->
<script async src="https://cdn.panelbear.com/analytics.js?site=Km4oFkEK6F6"></script>
<script>
    window.panelbear = window.panelbear || function() { (window.panelbear.q = window.panelbear.q || []).push(arguments); };
    panelbear('config', { site: 'Km4oFkEK6F6' });
</script>
'''
