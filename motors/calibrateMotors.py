
from time import sleep

import sne73SoftwarePwm as dcMotorControl
import hall as wheelEncoders


# Values to correct speed of motors
# [forward fast [r, l], 
#  forward normal [r, l], 
#  backward fast [r, l],
#  backward normal [r, l],
#  right fast [r, l],
#  right normal [r, l], 
#  left fast [r, l],
#  left normal [r, l]]
motorCalibration = []


def calibrateMotors(speed, turn = False):

	wheelEncoders.motor1Ticks = 0
	wheelEncoders.motor2Ticks = 0

	try:
		# test a turn or a straight piece depending on given command
		if turn:
			dcMotorControl.turn(speed)
		else:
			dcMotorControl.move(speed)
		sleep(2)
		dcMotorControl.stop()

		# Compare the progress of both wheels
		factor = wheelEncoders.motor1Ticks / wheelEncoders.motor2Ticks

		# Check which wheels goes faster, and limit one of both
		if factor > 0:
			left = 1
			right = left / right
		else: 
			right = 1 
			left = factor

		return [right, left]

	except:
		dcMotorControl.stop()
        print "Unexpected error during motor calibration:", sys.exc_info()[0]
        raise

        return False



def calibrate():
	global motorCalibration

	# forward
	motorCalibration[] = calibrateMotors(50)
	motorCalibration[] = calibrateMotors(100)
	# backward
	motorCalibration[] = calibrateMotors(-50)
	motorCalibration[] = calibrateMotors(-100)
	# turn right
	motorCalibration[] = calibrateMotors(50, turn = True)
	motorCalibration[] = calibrateMotors(100, turn = True)
	#turn left
	motorCalibration[] = calibrateMotors(-50, turn = True)
	motorCalibration[] = calibrateMotors(-100, turn = True)

	print "Results:"
	print motorCalibration


def main():
	calibrate()

if __name__ == "__main__":
    main()




Right = 3400
Left = 2900


factor = ticksRight / ticksLeft 

# Check which wheels goes faster, and limit one of both
if factor > 0:
	left = 1
	right = left / right
else: 
	right = 1 
	left = factor



