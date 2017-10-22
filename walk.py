from time import sleep
import sys
import random

print "Initializing motors"
import

import motors.sn75SoftwarePwm as dcMotorControl
from motors.servoWirPWM import *
from ultrasonic_sensor.ussContinuous import *
from motors.pigpio_encoder_functions import *


# generate and send the correct commands to the robot
def _send_robot_commands( self ):
  ...
  v_l, v_r = self._uni_to_diff( v, omega )
  self.robot.set_wheel_drive_rates( v_l, v_r )

def _uni_to_diff( self, v, omega ):
  # v = translational velocity (m/s)
  # omega = angular velocity (rad/s)

  R = self.robot_wheel_radius
  L = self.robot_wheel_base_length

  v_l = ( (2.0 * v) - (omega*L) ) / (2.0 * R)
  v_r = ( (2.0 * v) + (omega*L) ) / (2.0 * R)

  return v_l, v_r



def loop():
    try:

        prevTurn = False
        direction = 0

        while True:

            distance = getDistance()

            # if an object is closer than 15 cm turn to a random side for 1 second and check again
            if distance < 40 and distance != -1:

                # find a new direction to turn to if we are meeting a new wall
                if not prevTurn:
                    direction = random.choice([-1,1])
                    prevTurn = True
		    print " %s less than 15cm, turning %s" % (distance,  direction)
		else:
		    print "Still turning"


                # turn for 1 second and restart the loop
                dcMotorControl.turn(direction, 100)
                sleep(0.6)
                dcMotorControl.stop()
                continue

            # go straight
            else:
		print "Going straight"
                prevTurn = False
                dcMotorControl.move(100)
		#sleep(0.5)
		#dcMotorControl.stop()

    except KeyboardInterrupt:
        print "User cancelled"

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

    finally:
        print "Cleaning up.."
        dcMotorControl.cleanup()
        servoCleanup()

def test():
    try:

	#dcMotorControl.move(100)
	#sleep(0.5)
	#dcMotorControl.turn(1,100)
	#sleep(0.3)
	dcMotorControl.move(60)
	sleep(5)

    except KeyboardInterrupt:
        print "User cancelled"

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

    finally:
        print "Cleaning up.."
        dcMotorControl.cleanup()
        servoCleanup()


def main():
    loop()
#    test()

if __name__ == "__main__":
    main()
