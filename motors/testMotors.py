from time import sleep
import sys

print "Initializing motors"
import sne73SoftwarePwm as dcMotorControl
from servoWirPWM import *


try:

    #dcMotorControl.turn(1, 55)
    #sleep(4)
    #dcMotorControl.stop()
    #sleep(1)
    #dcMotorControl.move(99)
    dcMotorControl.motor1.forward(99)
    sleep(2)



    #dcMotorControl.stop()
    #dcMotorControl.move(-99)
    #sleep(2)
    #verticalServo.setPosition(100)
    #sleep(2)
    print "test"

except KeyboardInterrupt:
    print "User cancelled"

except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

finally:
    print "Cleaning up.."
    dcMotorControl.cleanup()
    servoCleanup()
