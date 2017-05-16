# Pinout of 2 servos on RPI 2b
# servo 1: Black = ground (pin 6)
#	   Yellow = control (pin 3)
# 	   Red = ext 6v power
# servo 2: Black = ground (pin 14)
#	   Yellow = control (pin 5)
#	   Red = ext 6v power
import RPi.GPIO as GPIO
import time

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(3, GPIO.OUT)

def main():
	p = GPIO.PWM(3, 50)
	p.start(50)
	p.ChangeDutyCycle(60)
	p.ChangeDutyCycle(95)
	time.sleep(3)
	p.stop()
	print "test"

def cleanup():
	GPIO.cleanup()

if __name__ == "__main__":
	setup()
	main()
	cleanup()
