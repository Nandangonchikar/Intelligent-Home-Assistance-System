import urllib2
import os
from gtts import *


def tts(thistext="hi"):
    tts=gTTS(text=thistext,lang='en')
    tts.save("proj.mp3")
    os.system("omxplayer proj.mp3")
    os.remove("proj.mp3")

tts("Turning light off     ")
print("Turning light off...")
response = urllib2.urlopen("http://192.168.43.21/LED=OFF")
