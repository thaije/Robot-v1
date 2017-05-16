import controller.XboxController as XboxController
from time import sleep
import motors.sne73SoftwarePwm as tracksContr




try:

	tracksContr.turn(1,55)
	sleep(4)
	tracksContr.stop()
	sleep(1)
	tracksContr.move(99)
	sleep(2)
	tracksContr.move(-99)
	sleep(2)

except KeyboardInterrupt:
        print "User cancelled"

except:
        print "Unexpected error:", sys.exc_info()[0]
	raise

finally:
	print "Cleaning up.."
	tracksContr.cleanup()