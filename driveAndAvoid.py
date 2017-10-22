################################################################################
# Author: Tjalling Haije
# Date: 22nd october, 2017
# Description: Lets the robot drive around and avoid obstacles
# How to run: - sudo pigpiod
#             - sudo python driveAndAvoid.py
################################################################################


import sys
import random
import pigpio
from time import sleep

import motors.wheels.sn75SoftwarePwm as dcMotorControl
import proximity_sensors.sonar.srte as sonar

pi = False

# leftwheel, rightwheel
wheels = []
# 0 = headsonar, 1 = right, 2 = left
sonars = []
proximity = []

def loop():

    # let's go driving forward
    dcMotorControl.set_wheel_drive_rates(wheels, [50, 50])


    while True:
        read_sensors()
        print "Readings:", proximity;

        # check proximity sensor values
        if proximity[0] < 20 or proximity[1] < 20 or proximity[2] < 20:

            # backup a bit
            dcMotorControl.set_wheel_drive_rates(wheels, [-30, -30])
            sleep(1.5)
            dcMotorControl.stop_wheels(wheels)

            # check which sonar was fired
            if proximity[1] < 20:
                # go left
                dcMotorControl.set_wheel_drive_rates(wheels, [-30, 30])
                print "Object on right, go left"
                sleep(1)

            # left sonar detected thing, so go right
            elif proximity[2] < 20:
                # go right
                dcMotorControl.set_wheel_drive_rates(wheels, [-30, 30])
                print "Object on left, go right"
                sleep(1)

            else:
                print "Object in front, let's make a random turn"
                # go random direction
                direction = random.choice([-1,1])
                dcMotorControl.set_wheel_drive_rates(wheels, [30 * direction, 30 * -direction])

                # rotate for a random period between 0.1 and 2 seconds
                duration = (random.random() * (2 - 0.3)) + 0.3
                sleep(duration)


            dcMotorControl.stop_wheels(wheels)
            dcMotorControl.set_wheel_drive_rates(wheels, [50, -50])

        sleep(0.1)




def init():
    global pi, sonars, wheels

    pi = pigpio.pi()
    if not pi.connected:
        exit()

    wheels = dcMotorControl.initialize_default_motors()

    sonars = sonar.initialize_default_sonars(pi)

    #dcMotorControl.test_wheels_external(wheels)

def read_sensors():
    global proximity
    proximity = sonar.read_proximity_sensors(sonars)


def main():
    try:
        init()
        #loop()
        #sonar.test_sonars_allin()
    except KeyboardInterrupt:
        print "User cancelled"
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    finally:
        print "Cleaning up.."
        dcMotorControl.cleanup_motors(wheels)
        sonar.cleanup_sonars(sonars)
        pi.stop()


if __name__ == "__main__":
    main()
