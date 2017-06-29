# This script uses software pwd on a sne73 chip to
# drive two dc motors (driving the tracks)

import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)

class Motor:

    def __init__(self, pinForward, pinBackward, pinControl):
        """ Initialize the motor with its control pins and start pulse-width
             modulation """

        self.pinForward = pinForward
        self.pinBackward = pinBackward
        self.pinControl = pinControl
        GPIO.setup(self.pinForward, GPIO.OUT)
        GPIO.setup(self.pinBackward, GPIO.OUT)
        GPIO.setup(self.pinControl, GPIO.OUT)
        self.pwm_forward = GPIO.PWM(self.pinForward, 100)
        self.pwm_backward = GPIO.PWM(self.pinBackward, 100)
        self.pwm_forward.start(0)
        self.pwm_backward.start(0)
        GPIO.output(self.pinControl,GPIO.HIGH) 

    def forward(self, speed):
        """ pinForward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.pwm_backward.ChangeDutyCycle(0)
        self.pwm_forward.ChangeDutyCycle(speed)    

    def backward(self, speed):
        """ pinBackward is the forward Pin, so we change its duty
             cycle according to speed. """

        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(speed)

    def stop(self):
        """ Set the duty cycle of both control pins to zero to stop the motor. """

        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(0)

# initiliase motors, motor1=left, motor2=right
motor1 = Motor(16, 22, 18)
motor2 = Motor(23, 19, 21)

# Drives the tracks 
# Input is driveTracks(LeftTrack, rightTrack), 
# with both values [-99,99], minus backward, plus forward
def driveTracks(leftTr,rightTr):
	# limit input to 99 
	leftTr = clamp(leftTr, -99, 99)
	rightTr = clamp(rightTr, -99, 99)

	print "LeftTr:", leftTr, ". RightTr:", rightTr

	if(leftTr > 0):
		motor1.forward(leftTr)
	elif(leftTr < 0):
		motor1.backward(leftTr*-1)
	else:
		motor1.stop()

	if(rightTr > 0):
		motor2.forward(rightTr)
	elif(rightTr < 0):	
		motor2.backward(rightTr*-1)
	else:
		motor2.stop()


# drive both tracks forward/backward
# s = speed [-99, 99], minus = backward
def move(s):
	s = clamp(s,-99,99)
	if s < 0:
		motor1.backward(-s)
		motor2.backward(-s)
	elif s > 0:
		motor1.forward(s)
		motor2.forward(s)

# stop turning of motors 
def stop():
	motor1.stop()
	motor2.stop()
	

# turn the tracks
# r =direction, r>0=leftturn, r<0=rightturn
# s = speed [1,99]
def turn(r,s):
	s = clamp(s,0,99)
		
	# turn left
	if r>0:
		motor1.backward(s)
		motor2.forward(s)
	elif r<0:
		motor1.forward(s)
		motor2.backward(s)
		




def clamp(n, minN, maxN):
	return max(min(maxN, n), minN)
	
def cleanup():
	stop()
	GPIO.cleanup()	

# Motor 2 test
#motor1.forward(60)
#motor2.forward(60)
#sleep(5)

# Running both
#motor1.forward(99)
#motor2.forward(99)
#sleep(5)
#motor1.backward(99)
#motor2.backward(99)
#sleep(5)

# let's see what happens
#motor1.forward(90)
#motor2.forward(90)
#sleep(5)

#cleanup()