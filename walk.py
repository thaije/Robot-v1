from time import sleep
import sys
import random

print "Initializing motors"
import motors.sne73SoftwarePwm as dcMotorControl
from motors.servoWirPWM import *
from ultrasonic_sensor.ussContiuous import *



def loop():
    try:

        prevTurn = False
        direction = 0

        while True:

            distance = getDistance()

            # if an object is closer than 15 cm turn to a random side for 1 second and check again
            if distance < 15 and distance != -1:

                # find a new direction to turn to if we are meeting a new wall
                if not prevTurn:
                    direction = random.choice([-1,1])
                    prevTurn = True
		    print distance + " less than 15cm, turning " + direction
		else:
		    print "Still turning"
            	
		
                # turn for 1 second and restart the loop
                dcMotorControl.turn(direction, 50)
                sleep(1)
                dcMotorControl.stop()
                continue

            # go straight
            else: 
		print "Going straight"
                prevTurn = False
                dcMotorControl.forward(70)

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


if __name__ == "__main__":
    main()






