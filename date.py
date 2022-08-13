import datetime
import os
from gtts import *


def tts(thistext="hi"):
    tts=gTTS(text=thistext,lang='en')
    tts.save("proj.mp3")
    os.system("omxplayer proj.mp3")
    os.remove("proj.mp3")

def timeStamped(fname, fmt='%d %m %Y{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

a=timeStamped('')
print("The date is :" +a)
tts("The date is :" +a   )
#with open('date.txt','w') as outf:
 #   outf.write(timeStamped(''))
