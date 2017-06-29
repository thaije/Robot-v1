# Controls tracks with xbox controller input
# Left thumb stick
# Y-axis (id=1)
# val 1 = down, val -1 = up
# 
# X-axis (id=0)
# val 1 = right, val -1 = left
#
# Tracks speed: max(X,Y) or min(X,Y) (depends on Y<0 or Y>O)
# at Y=0 and 0<X<0 in rotate modus, tracks move in opposite directions
# at Y>0 and 0<X<0 in sway/bank/other modus, slow one track to rotate during driving

import controller.XboxController as XboxController
from time import sleep
import motors.sne73SoftwarePwm as tracksContr

# start controller module
xboxCont = XboxController.XboxController(
    controllerCallBack = None,
    joystickNo = 0,
    deadzone= 0.2,
    scale = 1,
    invertYAxis = False)

Y = 0
X = 0

# interpret the changes in X and Y of the left thumb stick
# to directions and speed of the tracks
def changeTracks():
	tracksSpeed = 0
	tracksDirection = [1, 1]
	tempX = abs(X * 100)
	
	# set the tracksSpeed to either the largest  
	# value from X or Y. 
	if Y < 0:
		tracksSpeed = min([Y,-tempX])
	elif Y > 0:
		tracksSpeed = max([Y,tempX])
	else:
		tracksSpeed = tempX
		

	# check if we are in pure rotate mode
	if Y == 0 and X != 0:
		#print ">>Rotate modus"
		tracksDirection = [-X, X]	
		#print ">> dirs:",tracksDirection	

	# else we rotate by slowing one of the tracks
	else:	

		if X == -1:
			tracksDirection = [1, -1]
		elif X == 1:
			tracksDirection = [-1, 1]
		elif X > 0 :
			tracksDirection = [1-abs(X), 1]
		elif X < 0:
			tracksDirection = [1, 1-abs(X)]
		else:
			tracksDirection = [1, 1]

	# send changes to the tracksController
	tracksContr.driveTracks(tracksDirection[0]*tracksSpeed, 
		tracksDirection[1]*tracksSpeed)	
	

def leftThumbX(value):
	global X 
	X = value
	changeTracks()

def leftThumbY(value):
	# reverse value to 1=up, -1=down (with *-1)
	global Y 
	Y = value * -100
	changeTracks()


# add controller callbacks
xboxCont.setupControlCallback(
	xboxCont.XboxControls.LTHUMBX,
	leftThumbX)

xboxCont.setupControlCallback(
	xboxCont.XboxControls.LTHUMBY,
	leftThumbY)


# start controller and get buttons
try:
	xboxCont.start()
	while(True):
		sleep(1)

except KeyboardInterrupt:
        print "User cancelled"

except:
        print "Unexpected error:", sys.exc_info()[0]
	raise

finally:
	print "Cleaning up.."
	xboxCont.stop()
	tracksContr.cleanup()