
import wiringpi2 as wiringpi
import time
import pigpio
import RPi.GPIO as GPIO
import random


pi = pigpio.pi()
wiringpi.wiringPiSetupGpio()
GPIO.setmode(GPIO.BCM)

 

def initialize():
	print "intialize stuff"
	setupSonar()



def cleanupFiles():
	print "cleanup stuff"
	cleanupSonar()