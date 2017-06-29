
import motors.servos.servoWirPWM as servoControl
import motors.wheels.sn75SoftwarePwm as dcMotorControl
from motors.wheels.pigpio_encoder_functions import *
import proximity_sensors.sonar.srte as sonar



def loop():

	# get sonar readings
	proximity = read_proximity_sensors()

	# get wheel encoder ticks
	leftEncoderTicks
	rightEncoderTicks

	# set wheel speed
	dcMotorControl.set_wheel_drive_rates(v_l, v_r)

	# get servo positions
	verticalServo.position 
	verticalServo.minPos
	verticalServo.centerPosition
	verticalServo.maxPos
	horizontalServo.position 
	horizontalServo.minPos
	horizontalServo.centerPosition
	horizontalServo.maxPos

	# set servo position
	verticalServo.setPosition(dt)
    horizontalServo.setPosition(dt)


# generate and send the correct commands to the robot
def _send_robot_commands( self ):
	v_l, v_r = self._uni_to_diff( v, omega )
	self.robot.set_wheel_drive_rates( v_l, v_r )

# Change unicycle model to differential drive model
# See: https://www.toptal.com/robotics/programming-a-robot-an-introductory-tutorial
def _uni_to_diff( self, v, omega ):
	# v = translational velocity (m/s)
	# omega = angular velocity (rad/s)

	R = self.robot_wheel_radius
	L = self.robot_wheel_base_length

	v_l = ( (2.0 * v) - (omega*L) ) / (2.0 * R)
	v_r = ( (2.0 * v) + (omega*L) ) / (2.0 * R)

	return v_l, v_r


def cleanup():
	cleanupEncoders()
	dcMotorControl.cleanup()
	sonar.cleanupSonar()