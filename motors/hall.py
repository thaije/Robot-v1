# Original author : Matt Hawkins
# From http://www.raspberrypi-spy.co.uk/

# BCM pin numbering

# Import required libraries
import time
import datetime
import RPi.GPIO as GPIO

import sne73SoftwarePwm as dcMotorControl

# Counter: Revolutions * Dc motor gearbox ratio * hall effect sensor ticks
# per revolution
# Gearbox ratio is 35
# Ticks per revolution = 18 for 1 sensor, 48 for 2

# Right motor / motor 2:
# pin 17: 628 ticks per revolution
# pin 27: 628 ticks per revolution
# Together is 1256

# Left motor / motor 1:
# pin 5: 650 ticks per revolution
# pin 6: 650 ticks per revolution
# Together = 1300 ticks

motor1Ticks = 0
motor2Ticks = 0

def motor1Callback(channel):
    global motor1Ticks

    motor1Ticks += 1


def motor2Callback(chanel):
    global motor2Ticks

    motor2Ticks += 1



def main():
    test()


def test():
    # Wrap main content in a try block so we can
    # catch the user pressing CTRL-C and run the
    # GPIO cleanup function. This will also prevent
    # the user seeing lots of unnecessary error
    # messages.

    global motor1Ticks
    global motor2Ticks

    try:
        dcMotorControl.move(50)
        t_end = time.time() + 0.77
        while time.time() < t_end:
            time.sleep(0.001)

        dcMotorControl.stop()

        print "Motor 1 (right) ticks: %d " % (motor1Ticks)
        print "Motor 2 (left) ticks: %d " % (motor2Ticks)


    except KeyboardInterrupt:
        dcMotorControl.cleanup()
        # Reset GPIO settings
        #GPIO.cleanup()

    dcMotorControl.cleanup()

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


# testing
GPIO.setup(17, GPIO.IN)
GPIO.add_event_detect(17, GPIO.RISING, callback=motor1Callback)

#GPIO.setup(27, GPIO.IN)
#GPIO.add_event_detect(27, GPIO.BOTH, callback=motor1Callback)

#GPIO.setup(5, GPIO.IN)
#GPIO.add_event_detect(5, GPIO.BOTH, callback=motor2Callback)

#GPIO.setup(6, GPIO.IN)
#GPIO.add_event_detect(6, GPIO.BOTH, callback=motor2Callback)



if __name__ == "__main__":
    main()
