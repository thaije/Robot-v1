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

#######################################
# General methods / methods to move the servos
#######################################


# limit a value to a min and max
def clamp(n, minN, maxN):
    return max(min(maxN, n), minN)


# stop servos
def servoCleanup():
    verticalServo.center()
    horizontalServo.center()

    # wait for the servo to center
    time.sleep(1)

    verticalServo.stop()
    horizontalServo.stop()


def test():
    print "Starting PWM"
    dtMin, dtMax = 30, 120
    dt = dtMin
    while True:
        try:
            print dt
            verticalServo.setPosition(dt)
            horizontalServo.setPosition(dt)
            dt += 10
            if dt > dtMax:
                dt = dtMin
            time.sleep(1)
        except:
            verticalServo.stop()
            horizontalServo.stop()
            print "Exiting."
            break

# Initialize the servos with the pin number, min position and max position
# (to prevent the servos from breaking themselves due to limited space)
# Vertical servo, 55 is down, 120 is up
verticalServo = Servo(pin=18, minPos=55, maxPos=120, centerPosition=62)
print "Servo 1 online"

# horizontal servo, 30 is left
horizontalServo = Servo(pin=13, minPos=30, maxPos=115, centerPosition=72)
print "Servo 2 online"


#servo2.setPosition(120)

# run a test
#test()
#servoCleanup()

def test2():
    print "Starting PWM"

    wiringpi.wiringPiSetupGpio()

    wiringpi.pinMode(18, 2)
    wiringpi.pwmSetMode(0)
    wiringpi.pwmSetClock(400)
    wiringpi.pwmSetRange(1024)
    wiringpi.pwmWrite(18, 0)

    wiringpi.pinMode(13, 2)
    wiringpi.pwmSetMode(0)
    wiringpi.pwmSetClock(400)
    wiringpi.pwmSetRange(1024)
    wiringpi.pwmWrite(13, 0)

    dtMin, dtMax = 60, 120
    dt = 72
    while True:
        try:
            print dt
            wiringpi.pwmWrite(18, dt)
            wiringpi.pwmWrite(13, dt)
            dt += 10
            if dt > dtMax:
                dt = dtMin
                time.sleep(1)
        except:
            wiringpi.pwmWrite(18, 0)
            wiringpi.pwmWrite(13, 0)
            print "Exiting."
            break


#test2()
