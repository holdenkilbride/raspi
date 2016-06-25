#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import os


GPIO.setmode(GPIO.BOARD)

successLED = 7
failLED = 11
GPIO.setup(successLED,GPIO.OUT)
GPIO.setup(failLED,GPIO.OUT)



def nettest():
    hostname = "www.google.com"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        GPIO.output(successLED,True)
        GPIO.output(failLED,False)
        print "Everything is good"
        
        
    else:
        GPIO.output(successLED,False)
        GPIO.output(failLED,True)
        print "Site is down"
    
    
while (1):
    nettest()
    time.sleep(5)
    

GPIO.cleanup()
