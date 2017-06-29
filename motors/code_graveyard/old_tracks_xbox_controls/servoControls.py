# Controls head with xbox controller input
# Right thumb stick
# Y-axis (id=3)
# val -100 = down, val 100 = up
# 
# X-axis (id=2)
# val 1 = right, val -1 = left

import controller.XboxController as XboxController
from time import sleep
import wiringpi2 as wiringpi
import sys

def controlCallBack(xboxControlId, value):
        print "Control Id = {}, Value = {}".format(xboxControlId, value)



# start controller module
xboxCont = XboxController.XboxController(
    controllerCallBack = controlCallBack,
    joystickNo = 0,
    deadzone= 0.2,
    scale = 1,
    invertYAxis = False)


lookspeed = 100
pan = 72
tilt = 72
minPan = 28
maxPan = 120
minTilt = 25
maxTilt = 105

tiltPin = 18
panPin = 13
wiringpi.wiringPiSetupGpio()

# setup servo pwm pins
# 18 = tilt, 13 = pan
wiringpi.pinMode(tiltPin,2)
wiringpi.pwmSetMode(0)
wiringpi.pwmSetClock(400)
wiringpi.pwmSetRange(1024)
wiringpi.pwmWrite(tiltPin,0)

wiringpi.pinMode(panPin,2)
wiringpi.pwmSetMode(0)
wiringpi.pwmSetClock(400)
wiringpi.pwmSetRange(1024)
wiringpi.pwmWrite(panPin,0)


print "testtest"
#wiringpi.pwmWrite(tiltPin,100)
#sleep(1)
#wiringpi.pwmWrite(tiltPin,30)
#sleep(1)
#wiringpi.pwmWrite(panPin,120)
#sleep(1)
#wiringpi.pwmWrite(panPin,30)
#sleep(1)

X, Y = 0, 0

# change pan/tilt of head by changing servo positions
def changeServos():
	global pan
	global tilt

	#print "Change servos:", X, ",", Y

	#while Y != 0 or X != 0:
	#print "X/Y still not zero:", X, ",", Y
	if Y != 0:
		#print round(clamp(tilt + (Y / lookspeed),minTilt,maxTilt))
		tilt = int(round(clamp(tilt + (Y / lookspeed),minTilt,maxTilt)))
		wiringpi.pwmWrite(tiltPin, tilt)

	if X != 0:		
		#print round(clamp(pan + (X / lookspeed), minPan, maxPan))
		pan = int(round(clamp(pan + (X / lookspeed), minPan, maxPan)))
		wiringpi.pwmWrite(panPin, pan)

	

# limit a value tot the [minN, maxN] region
def clamp(n, minN, maxN):
	return max(min(maxN, n), minN)
	


def rightThumbX(value):
	global X 
	X = value * 100
	changeServos()

def rightThumbY(value):
	global Y 
	# reverse Y, Y < 0 = down Y > 0 =up
	Y = value * 100
	changeServos()


# add controller callbacks
xboxCont.setupControlCallback(
	xboxCont.XboxControls.RTHUMBX,
	rightThumbX)

xboxCont.setupControlCallback(
	xboxCont.XboxControls.RTHUMBY,
	rightThumbY)


# wait for input
try:
	xboxCont.start()
	while(True):
		print "in loop"
		sleep(0.25)

except KeyboardInterrupt:
        print "User cancelled"

except:
        print "Unexpected error:", sys.exc_info()[0]
	raise

finally:
	xboxCont.stop()
	wiringpi.pwmWrite(18,0)
	wiringpi.pwmWrite(13,0)
	print "Cleaning up.."


