from gravatar import Gravatar
g = Gravatar('david.riewe@gmail.com')

def parseAboutMe(input):
    # find u'aboutMe' tag
    #print input
    idxAboutMe = input.find('aboutMe')
    #print idxAboutMe
    if(idxAboutMe != -1):
        # get location of first ": u'" and subsequent ", u'" tags after "u'aboutMe'"
        # idxFirst = input.find(": u'", idxAboutMe+9)
        idxFirst = idxAboutMe + 12
        #print idxFirst
        if(idxFirst != -1):
            idxSecond = input.find("', u'", idxFirst+1)
            
            if(idxSecond != -1):
                # retrieve text between found tags
                output = input[idxFirst:idxSecond]
                return output



str1 = str(g.profile)
result = parseAboutMe(str1)
print result


