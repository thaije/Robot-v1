from handy_stuff.functions.functions import *
from motors.servos.servoWirPWM import Servo 
from motors.wheels.sn75SoftwarePwm import Motor
from motors.wheels.pigpio_encoder import decoder
from motors.wheels.pigpio_encoder_functions import *
from proximity_sensors.sonar.srte import sonar



class Robot:
	def __init__(self):

		# setup wheels
		self.leftWheel = Motor(23, 25, 24, diameter=9.0) 
		self.rightWheel = Motor(11, 10, 9, diameter=9.0) 
		self.wheels = [self.leftWheel, self.rightWheel]

		# setup servos
		# Vertical servo, 55 is down, 120 is up
		# horizontal servo, 30 is left
		self.verticalServo = Servo(pin=18, minPos=55, maxPos=120, centerPosition=62)
		self.horizontalServo = Servo(pin=13, minPos=30, maxPos=115, centerPosition=72)
		self.servos = [self.verticalServo, self.horizontalServo]

		# start pigpio
		pi = pigpio.pi()
		if not pi.connected:
      		exit()
		
		# Setup wheel encoders [left, right]
		decoderLeft = decoder(pi, 14, 15, callback_encoder_leftwheel)
		decoderRight = decoder(pi, 5, 6, callback_encoder_rightwheel)
		self.decoders = [decoderLeft, decoderRight]
		self.wheelTicks = [0, 0]

		# setup sonars
        # [Head sonar, right sonar, left sonar]
		self.sonars = []
        self.proximity = []
		# Head sonar
	    sonars.append(sonar(pi, None, 21))
	    # Front sonars
	    sonars.append(sonar(pi, None, 20))
	    sonars.append(sonar(pi,   26, 16))



	def set_wheel_drive_rates( self, wheels, speeds):
		if len(wheels) != len(speeds):
			raise ValueError('Number of wheels and speeds is not equal')

		for index, speed in enumerate(speeds):
			# limit the speed to [-99, 99]
			speed = clamp(speed, -99, 99)

			# set the speed of a wheel
			if speed < 0:
				wheels[i].backward(-speed)
			else if speed > 0:
				wheels[i].forward(speed)


	def callback_encoder_leftwheel(self, way):
		self.wheelTicks[0] += way


	def callback_encoder_rightwheel(self, way):
		self.wheelTicks[1] += way

    # read the proximity sensors 
    def read_proximity_sensors(self):
        # trigger the sonar
        for sonar in self.sonars:
            sonar.trigger()

        time.sleep(0.03)

        # read the sonar results
        for index, sonar in enumerate(self.sonars): 
            self.proximity[index] = sonar.read()

        return self.proximity

    # stop turning of wheels
    def stop_wheels(self, wheels):
        for wheel in wheels:
            wheel.stop()


	# stop servos
	def servo_cleanup(self, servos):
		for servo in servos:
			servos.center()

	    # wait for the servo to center
	    time.sleep(1)

	    for servo in servos:
			servos.stop()

	def decoder_cleanup(self, decoders):
		for decoder in decoders:
			 decoder.cancel()

    def sonar_cleanup(self, sonars):
        for sonar in sonars:
            sonar.cancel()

	# stop and cleanup all motors and code
	def cleanup(self):
		self.stop_wheels(self.wheels)
    	self.servo_cleanup(self.servos)
    	self.decoder_cleanup(self.decoders)
        self.sonar_cleanup(self.sonars)
    	GPIO.cleanup()
    	pi.stop()



###########################################
# Begin normal code
###########################################

	Fedya = robot()

	# get sonar readings
	proximity = Fedya.read_proximity_sensors()

	# get wheel encoder ticks
	Fedya.wheelTicks

	# set wheel speed
	Fedya.set_wheel_drive_rates([Fedya.leftWheel, Fedya.rightWheel],[v_l, v_r])

	# get servo positions
	Fedya.verticalServo.position 
	Fedya.verticalServo.minPos
	Fedya.verticalServo.centerPosition
	Fedya.verticalServo.maxPos
	Fedya.horizontalServo.position 
	Fedya.horizontalServo.minPos
	Fedya.horizontalServo.centerPosition
	Fedya.horizontalServo.maxPos

	# set servo position
	Fedya.verticalServo.setPosition(dt)
    Fedya.horizontalServo.setPosition(dt)