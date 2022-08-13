from gtts import *
import time
import os


def tts(thistext="hi"):
    tts=gTTS(text=thistext,lang='en')
    tts.save("proj.mp3")
    os.system("mpg321 proj.mp3")
    os.remove("proj.mp3")

tts("here is what i can  do I can click a photo,read text ,turn lights on and off")
print("here is what i can  do")
print("I can click a photo,read text ,turn lights on and off and much more..")

