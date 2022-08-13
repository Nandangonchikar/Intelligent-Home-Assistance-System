import paho.mqtt.client as mqtt
import time
from gtts import *
import serial
import RPi.GPIO as GPIO
import os, time

#ser  = serial.Serial("/dev/ttyS0", baudrate=9600,timeout=1)


    

 #The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    a=msg.payload
    print ("a")
    if a=="0":        #rain sensor
        print (str(msg.payload))
        os.system("python2 /home/pi/Nandas/gr1.py")

        
        
    elif a=="1":        #gas sensor
        print (str(msg.payload))
        
        os.system("python2 /home/pi/Nandas/gr2.py")
        
 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.43.203", 1883, 60)

client.loop_forever()





