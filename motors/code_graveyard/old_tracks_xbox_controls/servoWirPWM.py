import wiringpi2 as wiringpi
import time


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
	main()