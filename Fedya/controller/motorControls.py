import XboxController
import time

# start controller module
xboxCont = XboxController.XboxController(
    controllerCallBack = None,
    joystickNo = 0,
    deadzone= 0.1,
    scale = 1,
    invertYAxis = False)

# catch X and Y changes in left thumb stick
def leftThumbX(value):
	print "left thumb X changed"

def leftThumbY(value):
	print "left thumb Y changed"

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
		time.sleep(1)

except KeyboardInterrupt:
        print "User cancelled"

except:
        print "Unexpected error:", sys.exc_info()[0]
	raise

finally:
	xboxCont.stop()