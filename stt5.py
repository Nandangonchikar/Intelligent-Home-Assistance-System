import os
from gtts import gTTS
import speech_recognition as sr

print("recording...")
os.system("arecord -D hw:1,0 -d 5 -r 48000 -f S16_LE file.wav")
print("processing...")
r = sr.Recognizer()
with sr.AudioFile("file.wav") as source:
    audio = r.listen(source)
    a=r.recognize_google(audio)
    print("you said: ")
    print(a)

with open("speech.txt", "w") as f:  #, encoding="utf-8" if we want to choose encoding
    f.write(a)
    
os.system("python2 /home/pi/Nandas/command.py")
