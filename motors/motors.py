# Pinout of 2 servos on RPI 2b
# servo 1: Black = ground (pin 6)
#	   Yellow = control (pin 3)
# 	   Red = ext 6v power
# servo 2: Black = ground (pin 14)
#	   Yellow = control (pin 5)
#	   Red = ext 6v power
import RPi.GPIO as GPIO

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(3, GPIO.OUT)

def main():
	p = GPIO.PWM(25, 50)
	p.start(50)
	p.ChangeDutyCycle(90)
	p.ChangeDutyCycle(100)
	p.stop()
	print "test"
	return

def cleanup():
	GPIO.cleanup()

if __name__ == "__main__":
	setup()
	main()
	cleanup()
