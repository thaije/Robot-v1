
from time import sleep

import sne73SoftwarePwm as dcMotorControl
import hall as wheelEncoders


# Values to correct speed of motors
# [forward, backward, right, left]
motorCalibration = [1.0, 1.0, 1.0, 1.0]


def calibrateMotors(speed, turn = False):

	wheelEncoders.motor1Ticks = 0
	wheelEncoders.motor2Ticks = 0

	try:
		if turn:
			dcMotorControl.turn(speed)
		else:
			dcMotorControl.move(speed)
		sleep(2)
		dcMotorControl.stop()
		return wheelEncoders.motor1Ticks / wheelEncoders.motor2Ticks

	except:
		dcMotorControl.stop()
        print "Unexpected error during motor calibration:", sys.exc_info()[0]
        raise



def calibrate():
	global motorCalibration

	motorCalibration[0] = calibrateMotors(100)
	motorCalibration[1] = calibrateMotors(-100)
	motorCalibration[2] = calibrateMotors(100, turn = True)
	motorCalibration[3] = calibrateMotors(-100, turn = True)

	print "Results:"
	print motorCalibration


def main():
	calibrate()

if __name__ == "__main__":
    main()




Right = 3400
Left = 2900

3400 / 2900 = 

100 / 3400


Right / left

