import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pirPin = 23

GPIO.setup(pirPin, GPIO.IN)
print "Waiting for sensor to settle"
time.sleep(2)
print "Detecting motion"

try:
    while True:
        if GPIO.input(pirPin):
            print "Motion detected!"
        else:
            print "No motion"
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print "HC-SR501 motion detection end"
