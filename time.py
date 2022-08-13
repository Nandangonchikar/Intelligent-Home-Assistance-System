import datetime
import os
from gtts import *


def tts(thistext="hi"):
    tts=gTTS(text=thistext,lang='en')
    tts.save("proj.mp3")
    os.system("omxplayer proj.mp3")
    os.remove("proj.mp3")


def timeStamped(fname, fmt='%H %M{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

a=timeStamped('')
print("The Time is: " +a) 
tts("The Time is: " +a  )

#with open('time.txt','w') as outf:
#outf.write(timeStamped(''))
