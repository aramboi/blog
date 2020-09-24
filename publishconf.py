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

ACKEE_TAG = '<script async src="https://a.angelramboi.com/a.js" data-ackee-server="https://a.angelramboi.com" data-ackee-domain-id="57e37041-c751-4008-b25e-fc87059487b7"></script>'
