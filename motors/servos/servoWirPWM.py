import wiringpi2 as wiringpi
import time
from handy_stuff.functions.functions import * 

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
        self.pwmRange = 1024
        self.centerPosition = centerPosition
        self.setPinMode(self.pinMode)
        self.setPwmMode(self.PwmMode)
        self.setClock(self.clock)
        self.setRange(self.pwmRange)
        self.setPosition(self.centerPosition)

    def setPinMode(self, pinMode):
        self.pinMode = pinMode
        wiringpi.pinMode(self.pin, 2)

    def setPwmMode(self, pwmMode):
        self.pwmMode = pwmMode
        wiringpi.pwmSetMode(pwmMode)

    def setClock(self, clock):
        self.clock = clock
        wiringpi.pwmSetClock(clock)

    def setRange(self, pwmRange):
        self.pwmRange = pwmRange
        wiringpi.pwmSetRange(pwmRange)

    # set the position of the servo
    def setPosition(self, position):
        position = clamp(position, self.minPos, self.maxPos)
        self.position = position
        wiringpi.pwmWrite(self.pin, self.position)

    def center(self):
        self.setPosition(self.centerPosition)

    def stop(self):
        wiringpi.pwmWrite(self.pin, 0)



#############################################################
# General functions
#############################################################

def initialize_default_servos():
    print "Initializing default servos"
    verticalServo = Servo(pin=18, minPos=55, maxPos=120, centerPosition=62)
    horizontalServo = Servo(pin=13, minPos=30, maxPos=115, centerPosition=72)

    return [verticalServo, horizontalServo]


def cleanup_servos(servos):
    print "Cleaning up servos"
    for servo in servos:
        servo.center()

        # wait for the servo to center
        time.sleep(1)

        for servo in servos:
            servo.stop()


# test with externally initialized servos and no cleanup
def test_servos_external(servos):
    print "Testing Servos"
    dtMin, dtMax = 30, 120
    dt = dtMin
    while True:
        try:
            print dt
            servos[0].setPosition(dt)
            servos[1].setPosition(dt)
            dt += 10
            if dt > dtMax:
                dt = dtMin
            time.sleep(1)
        except:
            servos[0].stop()
            servos[1].stop()
            print "Exiting."
            break


# test without having to set anything up
def test_servos_allin():
    servos = initialize_default_servos()
    test_servos_external(servos)
    cleanup_servos(servos)
