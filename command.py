import os
from gtts import *


def tts(thistext="hi"):
    tts=gTTS(text=thistext,lang='en')
    tts.save("proj.mp3")
    os.system("omxplayer proj.mp3")
    os.remove("proj.mp3")


with open("speech.txt", "r") as f:
    textx=f.read()

#add the keywords here
helpp=("help","what can you do")
lighton = ("turn on", " switch on", "light on")
lightoff = ("turn off", " switch off", "light off")
ocr = ("read", "this", "text")
photo=("photo","pic","picture")
music=("play","music","song")
time=("time","clock")
date=("date","month")

if any(textx.find(s)>=0 for s in helpp):
    os.system("python2 /home/pi/Nandas/help1.py")

if any(textx.find(s)>=0 for s in lighton):
    os.system("python2 /home/pi/Nandas/lighton.py")

if any(textx.find(s)>=0 for s in lightoff):
    os.system("python2 /home/pi/Nandas/lightoff.py")

    

if all(textx.find(s)>=0 for s in ocr):
    say="show me the text  "
    tts(say)
    os.system("python2 /home/pi/Nandas/ocr.py")

if any(textx.find(s)>=0 for s in photo):
    os.system("python2 /home/pi/Nandas/photo.py")

if any(textx.find(s)>=0 for s in music):
    os.system("omxplayer /home/pi/Music/a.mp3")

if any(textx.find(s)>=0 for s in time):
    os.system("python2 /home/pi/Nandas/time.py")

if any(textx.find(s)>=0 for s in date):
    os.system("python2 /home/pi/Nandas/date.py")




else:
    say="no command"
