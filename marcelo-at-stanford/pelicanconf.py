#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marcelo Moreira'
SITENAME = u'Marcelo @ Stanford'
SITEURL = 'http://www.stanford.edu'  # *NO* trailing slash
SITEURL_SUFFIX = '/~marcelom/pelicantest'  # *NO* trailing slash

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# My theme ignores some templates, so here they are...
ARTICLE_URL = '%s/posts/{slug}' % SITEURL_SUFFIX
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'
ARTICLE_LANG_SAVE_AS = False  # Dsiables LANG processing, all site is in English...
PAGE_URL = '%s/pages/{slug}' % SITEURL_SUFFIX
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGE_LANG_SAVE_AS = False
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAG_URL = '%s/tags/{slug}' % SITEURL_SUFFIX
TAG_SAVE_AS = 'tags/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = False
MONTH_ARCHIVE_SAVE_AS = False
DAY_ARCHIVE_SAVE_AS = False

# Themes
THEME = 'themes/marcelo'
# THEME = 'themes/myidea'
# THEME = 'themes/stanfordu'
# THEME = 'themes/cebong'
# THEME = 'themes/nmnlist'
# THEME = 'themes/mnmlist'

DISQUS_SITENAME = 'marceloatstanford'

# Show the Stanford Site Search Box
SITE_SEARCH_BOX = True
