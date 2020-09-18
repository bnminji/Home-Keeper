import paho.mqtt.client as mqtt 
import RPi.GPIO as GPIO
import time

def on_connect(client, userdata, flags, rc):
    print ("Connect with result code" + str(rc))
    client.subscribe("LED")

def on_message(client, userdata, msg):
    if "ALLON" in msg.payload:
        GPIO.output(24, True)
        GPIO.output(25, True)
        print str(msg.payload)
    if "ALLOFF" in msg.payload:
        GPIO.output(24, False)
        GPIO.output(25, False)
    if "ONEON" in msg.payload:
        GPIO.output(24, True)
    if "ONEOFF" in msg.payload:
        GPIO.output(24, False)
    if "TWOON" in msg.payload:
        GPIO.output(25, True)
    if "TWOOFF" in msg.payload:
        GPIO.output(25, False)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('localhost', 1883, 60)

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
client.loop_forever()
