import wiringpi2 as wiringpi
import time


wiringpi.wiringPiSetupGpio()



class Servo:

    def __init__(self, pin):
        """ Initialize the motor with its control pins and start pulse-width
             modulation """

        self.pin = pin
        self.pinMode = 2
        self.PwmMode = 0
        self.clock = 400
        self.range = 1024
        self.position = 0
        self.setPinMode(self.pinMode)
        self.setPwmMode(self.PwmMode)
        self.setClock(self.clock)
        self.setRange(self.range)
        self.setPosition(self.pin, self.position)

    def setPinMode(self, pinMode):
    	wiringpi.pinMode(18,2)

    def setPwmMode(self, pwmMode):
        wiringpi.pwmSetMode(mode)

    def setClock(self, clock):
		wiringpi.pwmSetClock(clock)

	def setRange(self, range):
		wiringpi.pwmSetRange(range)
	

	# set the position of the servo
	def setPosition(self, position):
		self.position = position
		wiringpi.pwmWrite(self.pin, self.position)


	def stop(self):
		self.setPosition(0)


def main2():

	print "Servo 1 online"
	servo1 = Servo(18)
	print "Servo 2 online"
	servo2 = Servo(13)


	print "Starting PWM"
	dtMin, dtMax = 60, 120
	dt = 72
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




def main():	
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

if __name__ == '__main__':
	main2()