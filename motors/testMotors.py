from time import sleep

print "Firing up engines"
import sne73SoftwarePwm as dcMotorsControl
import servoWirPWM as servoControl


try:

	dcMotorsControl.turn(1,55)
	sleep(4)
	dcMotorsControl.stop()
	sleep(1)
	dcMotorsControl.move(99)
	sleep(2)
	dcMotorsControl.move(-99)
	sleep(2)

except KeyboardInterrupt:
        print "User cancelled"

except:
        print "Unexpected error:", sys.exc_info()[0]
	raise

finally:
	print "Cleaning up.."
	dcMotorsControl.cleanup()