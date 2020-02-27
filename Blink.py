#Description: This is a program that turns LED on and off for every
#300 ms.
#importing the module
import RPi.GPIO as GPIO
import time

#disable the warning
GPIO.setwarnings(False)
#Pin numbering
GPIO.setmode(GPIO.BCM)
#set up the channel. configure pin 18 as output
GPIO.setup(18, GPIO.OUT)
try:
    while True:
        GPIO.output(18, True)
        time.sleep(0.3)
        GPIO.output(18, False)
        time.sleep(0.3)
finally:
        GPIO.cleanup()
