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

ANALYTICS_TAGS = """<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "6badc6d8d8874100b4e1dde83a4f5f51"}'></script><!-- End Cloudflare Web Analytics -->"""
