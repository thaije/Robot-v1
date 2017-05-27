#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#       Hall Effect Sensor
#
# This script tests the sensor on GPIO17.
#
# Author : Matt Hawkins
# Date   : 03/04/2017
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import required libraries
import time
import datetime
import RPi.GPIO as GPIO

import sne73SoftwarePwm as dcMotorControl


def sensorCallback(channel):
    # Called if sensor output changes
    timestamp = time.time()
    stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
    print "Sensor low" + stamp

    #if GPIO.input(channel):
        # No magnet
    #    print("Sensor HIGH " + stamp)
    #else:
        # Magnet
    #    print("Sensor LOW " + stamp)


def main():
  # Wrap main content in a try block so we can
  # catch the user pressing CTRL-C and run the
  # GPIO cleanup function. This will also prevent
  # the user seeing lots of unnecessary error
  # messages.

    try:
        dcMotorControl.move(99)
        # Loop until users quits with CTRL-C
        while True:
            time.sleep(0.1)

    except KeyboardInterrupt:
        dcMotorControl.cleanup()
        # Reset GPIO settings
        #GPIO.cleanup()

# Tell GPIO library to use GPIO references
#GPIO.setmode(GPIO.BCM)

print("Setup GPIO pin as input on GPIO17")

# Set Switch GPIO as input
# Pull high by default
#GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) # or down?
#GPIO.add_event_detect(11, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

#GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(13, GPIO.BOTH, callback=sensorCallback, bouncetime=200)


#GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(13, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

#GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(13, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

GPIO.setup(11, GPIO.IN)
GPIO.add_event_detect(11, GPIO.FALLING, callback=sensorCallback)



if __name__ == "__main__":
    main()
