#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'related_posts', 'tag_cloud']

RELATED_POSTS_MAX = 10
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_TAGS_INLINE = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

AUTHOR = 'Hacker Space Tech'
ABOUT_ME = 'We a motivated group of hardware hackers who like learning about technology and building cool things.  To learn more about the display above <a href="http://hackerspacetech.com/building-a-16x32-neopixel-display.html">Click Here</a>.  To learn more about the Hacker Stars at Hacker Space Tech <a href="/pages/hacker-stars.html">Click Here</a><br><br>'
#ABOUT_ME = 'Electronics Tech with over 20 years of experience in the computer industry.  I enjoy building micro-controlled projects, programming and web development.  <a href="/pages/bio.html"> read my full bio here</a>
#AVATAR = '/images/avatar2.jpg'
AVATAR = '/images/animatedlogocropped.gif'
SITENAME = 'HackerSpaceTech'
SITEURL = 'http://www.hackerspacetech.com'
#SITELOGO = 'images/animatedlogo.gif'
#SITELOGOSIZE = 50cd 
BANNER = '/images/banners/mainbanner3.png'
BANNER_ALL_PAGES = True
USE_PAGER = True
BOOTSTRAP_NAVBAR_INVERSE = False
BOOTSTRAP_THEME = 'united'
TWITTER_USERNAME = 'hackerspacetech'
TWITTER_WIDGET_ID = '571543237362335744'
ADDTHIS_PROFILE = 'driewe'
USE_FOLDER_AS_CATEGORY = True
PATH = 'content'

THEME = "pelican-themes/pelican-bootstrap3"
PYGMENTS_STYLE = 'solarizeddark'
BOOTSTRAP_FLUID = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None
SHOW_ARTICLE_AUTHOR = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Blog', '/category/blog.html'),
    ('Meetups', '/pages/meetups.html'),
    ('Classes', '/pages/classes.html'),
    ('Arduino Crash Course','http://freecourse.hackerspacetech.com'),
    ('Hacker Stars', '/pages/hacker-stars.html'),
    ('Tutorials', '/pages/tutorials.html'),
    ('Contact', '/pages/contact.html')
)

# Blogroll
LINKS = (('Free Arduino Class', 'http://freecourse.hackerspacetech.com'),
        ('Register For PEA', 'http://programmingelectronics.com/hackerspacetech'),
        ('HackerSpaceTech Meetup', 'http://www.meetup.com/hackerspacetech'),
        ('Fadecandy 16x32 Project', 'http://hackerspacetech.com/16x32-NeoPixel-FadeCandy-Display/'),
        ('Infra Red Controlled Robot', 'http://hackerspacetech.com/RemoteControlRobotIR/'),
        ('TheLab.ms', 'https://thelab.ms/'),
        ('Dallas Maker Space', 'https://dallasmakerspace.org/'),
        ('Hackster.io', 'https://www.hackster.io/driewe'),)

# Social widget
SOCIAL = (('twitter', 'http://www.twitter.com/hackerspacetech'),
          ('linkedin', 'http://www.linkedin.com/in/driewe'),
          ('github', 'http://www.github.com/driewe'),
          ('facebook', 'http://www.facebook.com/HackerSpaceTech'),
          ('youtube', 'https://www.youtube.com/channel/UCxScU-1pFpDndfqXOLqwrUw'),
          ('quora', 'https://www.quora.com/profile/David-Riewe'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-47432237-2"