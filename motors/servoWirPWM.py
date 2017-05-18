import wiringpi2 as wiringpi
import time


wiringpi.wiringPiSetupGpio()


# Servo class with all information and methods for the wiringpi objects
class Servo:

    def __init__(self, pin, minPos, maxPos, centerPosition):
        """ Initialize the motor with its pins, min, max and 
        center positions"""

        self.pin = pin
        self.minPos = minPos
        self.maxPos = maxPos
        self.pinMode = 2
        self.PwmMode = 0
        self.clock = 400
        self.range = 1024
        self.position = 0
        self.centerPosition = self.centerPosition
        self.setPinMode(self.pinMode)
        self.setPwmMode(self.PwmMode)
        self.setClock(self.clock)
        self.setRange(self.range)
        self.setPosition(self.pin, self.position)

    def setPinMode(self, pinMode):
    	wiringpi.pinMode(self.pin,2)

    def setPwmMode(self, pwmMode):
        wiringpi.pwmSetMode(mode)

    def setClock(self, clock):
		wiringpi.pwmSetClock(clock)

	def setRange(self, range):
		wiringpi.pwmSetRange(range)
	

	# set the position of the servo
	def setPosition(self, position):
		position = clamp(position, self.minPos, self.maxPos)
		self.position = position
		wiringpi.pwmWrite(self.pin, self.position)


	def stop(self):
		self.setPosition(self.centerPosition)


#######################################
# General methods / methods to move the servos
#######################################


# limit a value to a min and max
def clamp(n, minN, maxN):
	return max(min(maxN, n), minN)


# stop servos
def cleanup():
	servo1.stop()
	servo2.stop()


def test():
	print "Starting PWM"
	dtMin, dtMax = 60, 120
	dt = dtMin
	while True:
		try:
			print dt
			servo1.setPosition(dt)
			servo2.setPosition(dt)
			dt += 10
			if dt > dtMax:
				dt = dtMin
			time.sleep(1)
		except:
			servo1.stop()
			servo2.stop()
			print "Exiting."
			break

# Initialize the servos with the pin number, min position and max position (to prevent 
# the servos from breaking themselves due to limited space)
servo1 = Servo(pin = 18, minPos = 0, maxPos = 180, centerPosition = 70)
print "Servo 1 online" # bottom servo?
servo2 = Servo(pin = 13, minPos = 0, maxPos = 180, centerPosition = 70)
print "Servo 2 online" # top servo?

# run a test
test()



def test2():	
	print "Starting PWM"
	
	wiringpi.wiringPiSetupGpio()
	
	wiringpi.pinMode(18,2)
	wiringpi.pwmSetMode(0)
	wiringpi.pwmSetClock(400)
	wiringpi.pwmSetRange(1024)
	wiringpi.pwmWrite(18,0)

	wiringpi.pinMode(13,2)
	wiringpi.pwmSetMode(0)
	wiringpi.pwmSetClock(400)
	wiringpi.pwmSetRange(1024)
	wiringpi.pwmWrite(13,0)
	
	
	dtMin, dtMax = 60, 120
	dt = 72
	while True:
		try:
			print dt
			wiringpi.pwmWrite(18,dt)
			wiringpi.pwmWrite(13,dt)
			dt += 10
			if dt > dtMax:
				dt = dtMin
			time.sleep(1)
		except:
			wiringpi.pwmWrite(18,0)
			wiringpi.pwmWrite(13,0)
			print "Exiting."
			break

