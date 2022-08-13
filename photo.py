import cv2
import datetime
import os
import time
from gtts import *

def tts(thistext=""):
    tts=gTTS(text=thistext,lang='en')
    tts.save("proj.mp3")
    os.system("mpg321 proj.mp3")
    os.remove("proj.mp3")

cap = cv2.VideoCapture(0)
date=datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

while(True):
    tts("Say cheese...")
    print("Say cheese...")
    ret, frame = cap.read()
    #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    cv2.imshow('frame', frame)
    filename="/home/pi/Nandas/photos/capture "+ date +".jpg"
    out = cv2.imwrite(filename, frame)
    #cv2.imshow('frame', filename)
    tts("The photo has been captured..  ")
    print("The photo has been captured..")
    
    break
        
   
cap.release()
cv2.destroyAllWindows()
