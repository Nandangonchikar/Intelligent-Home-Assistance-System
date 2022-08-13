import numpy as np
import cv2
import RPi.GPIO as GPIO
import imutils
import os
import pytesseract
from PIL import Image
from gtts import *

def tts(thistext=""):
    tts=gTTS(text=thistext,lang='en')
    tts.save("proj.mp3")
    os.system("omxplayer proj.mp3")
    os.remove("proj.mp3")
    
cap = cv2.VideoCapture(0)
GPIO.setmode(GPIO.BOARD)            # choose BCM or BOARD  
GPIO.setup(40, GPIO.IN,pull_up_down=GPIO.PUD_UP)              # set a port/pin as an input  
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(38,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setwarnings(False)
tts("allign the camera and press the button ")

while True:
    ret, img = cap.read()
    #img = cv2.resize(img,(480,360))
    if (GPIO.input(40)==False):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       # cv2.imshow('gray',gray)
        binary= cv2.threshold(gray, 100, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] 
        #cv2.imshow('bin',binary)
        med= cv2.medianBlur(binary,3)
        #cv2.imshow('med',med)
        text=pytesseract.image_to_string(gray,lang='eng')
        print(text)
        if(text!="/0"):
            with open("ocrdata.txt", "w") as f:  #, encoding="utf-8" if we want to choose encoding
                f.write(text)
            print("The Text found is:" +text)
            tts("The Text found is:"+text)
        else:
            tts("no text found..")
        
    cv2.imshow('img', img)
    k = cv2.waitKey(1)
cv2.destroyAllWindows()
cap.release()

