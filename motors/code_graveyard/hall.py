# Original author : Matt Hawkins
# From http://www.raspberrypi-spy.co.uk/

# BCM pin numbering

# Import required libraries
import time
import datetime
import RPi.GPIO as GPIO

import sn75SoftwarePwm as dcMotorControl

# Counter: Revolutions * Dc motor gearbox ratio * hall effect sensor ticks
# per revolution
# Gearbox ratio is 35
# Ticks per revolution = 18 for 1 sensor, 48 for 2

# Right motor / motor 1:
# pin 17: 640 ticks per revolution
# pin 27: 640 ticks per revolution
# Together is 1280

# Left motor / motor 2:
# pin 14: 640 ticks per revolution
# pin 15: 640 ticks per revolution
# Together = 1280 ticks

motor1Ticks = 0
motor2Ticks = 0

def motor1Callback(channel):
    global motor1Ticks

    motor1Ticks += 1


def motor2Callback(channel):
    global motor2Ticks

    motor2Ticks += 1



def main():
	# test()	
	
	print "Motor 1: %d, Motor 2: %d" % (motor1Ticks, motor2Ticks)
	time.sleep(1)

	print "Starting motors"
	checkEncoders(0.88)
	

def checkEncoders(seconds):
	
	try:	
		dcMotorControl.turn(50)
		timed = 0
		while(timed < seconds):
			print "Motor 1: %d, Motor 2: %d" % (motor1Ticks, motor2Ticks)
			time.sleep(0.1)
			timed += 0.1
	
		print "stopping motors"	
		dcMotorControl.stop()   
		#dcMotorControl.cleanup()
	
		# check if it continues turning during breaking
		timed = 0
		while(timed < 1):
			print "Motor 1: %d, Motor 2: %d" % (motor1Ticks, motor2Ticks)
    	        	time.sleep(0.1)
            		timed += 0.1 
	except:
		dcMotorControl.cleanup()
	dcMotorControl.cleanup()

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



def setup():
    print("Setup GPIO pin as input on GPIO17")

    # testing
    GPIO.setup(5, GPIO.IN)
    GPIO.add_event_detect(5, GPIO.BOTH, callback=motor1Callback)

    GPIO.setup(6, GPIO.IN)
    GPIO.add_event_detect(6, GPIO.BOTH, callback=motor1Callback)

    GPIO.setup(14, GPIO.IN)
    GPIO.add_event_detect(14, GPIO.BOTH, callback=motor2Callback)

    GPIO.setup(15, GPIO.IN)
    GPIO.add_event_detect(15, GPIO.BOTH, callback=motor2Callback)



if __name__ == "__main__":
    setup()
    main()
