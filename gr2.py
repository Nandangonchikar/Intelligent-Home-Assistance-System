import os
from gtts import *
import serial
import RPi.GPIO as GPIO
import os, time
GPIO.setmode(GPIO.BOARD)

tts=gTTS(text="Warning: Gas is leaking. switching the exhaust on",lang='en')
print("Warning: Gas is leaking. switching the exhaust on")
tts.save("proj.mp3")
os.system("mpg321 proj.mp3")
os.remove("proj.mp3")

ser  = serial.Serial("/dev/ttyS0", baudrate=9600,timeout=1)


ser.write('AT'+'\r\n')
rcv = ser.read(10)
print rcv
time.sleep(1)

ser.write('AT+CMGF=1'+'\r\n')
rcv = ser.read(10)
print rcv
time.sleep(1)

ser.write('AT+CMGS="8861419515"'+'\r\n')
rcv = ser.read(10)
print rcv
time.sleep(10)

print("sending message to 8861419515")
ser.write('Warning: Gas is leaking. switching the exhaust on'+'\r\n')
rcv = ser.read(10)
print rcv


ser.write("\x1A")
for i in range(10):
    rcv = ser.read(10)
    print rcv
print("the message has been sent")
