from time import sleep

print "Firing up engines"
import sne73SoftwarePwm as dcMotorControl
import servoWirPWM as servoControl


try:

	dcMotorControl.turn(1,55)
	sleep(4)
	dcMotorControl.stop()
	sleep(1)
	dcMotorControl.move(99)
	sleep(2)
	dcMotorControl.move(-99)
	sleep(2)

except KeyboardInterrupt:
        print "User cancelled"

except:
        print "Unexpected error:", sys.exc_info()[0]
	raise

finally:
	print "Cleaning up.."
	dcMotorControl.cleanup()
	servoControl.cleanup()