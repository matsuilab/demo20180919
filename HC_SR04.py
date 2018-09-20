import time
import RPi.GPIO as GPIO
import smbus
import math

def measure(sensor):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    #sokkyo
    TRIG = 5
    ECHO = 6
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, GPIO.LOW)

    time.sleep(0.3)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    while GPIO.input(ECHO) == 0:
        startTime = time.time()
    while GPIO.input(ECHO) == 1:
        stopTime = time.time()
        
    timepassed = stopTime - startTime
    distance = timepassed * 17000
    GPIO.cleanup()
    return distance