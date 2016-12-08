"""
Gravatar plugin for Pelican
===========================

This plugin assigns the ``author_gravatar`` variable to the Gravatar URL and
makes the variable available within the article's context.
"""

#import Gravatar - causes issues when uncommented
#see about using https://github.com/gridaphobe/pyGravatar/blob/master/gravatar.py
#
import hashlib
import six
from pelican import signals

# this is used to parse out the about me from gravatar profile
# once it is working
#def parseAboutMe(input):
    # find u'aboutMe' tag
#    idxAboutMe = input.find('aboutMe')
#    if(idxAboutMe != -1):
        # get location of first ": u'" and subsequent ", u'" tags after "u'aboutMe'"
        # idxFirst = input.find(": u'", idxAboutMe+9)
#        idxFirst = idxAboutMe + 12
#        #print idxFirst
#        if(idxFirst != -1):
#            idxSecond = input.find("', u'", idxFirst+1)
            
#            if(idxSecond != -1):
#                # retrieve text between found tags
#                output = input[idxFirst:idxSecond]
#                return output

def add_gravatar(generator, metadata):

    #first check email
    if 'email' not in metadata.keys()\
        and 'AUTHOR_EMAIL' in generator.settings.keys():
            metadata['email'] = generator.settings['AUTHOR_EMAIL']

    #then add gravatar url
    if 'email' in metadata.keys():
        email_bytes = six.b(metadata['email']).lower()
        gravatar_url = "https://www.gravatar.com/avatar/" + \
                        hashlib.md5(email_bytes).hexdigest()
        metadata['author_gravatar'] = gravatar_url



def register():
    signals.article_generator_context.connect(add_gravatar)
