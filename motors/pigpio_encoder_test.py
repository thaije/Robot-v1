
import time
import pigpio

import pigpio_encoder
import sn75SoftwarePwm as dcMotorControl

# One rotation is 360 ticks
# Forwards is positive, backwards is negative

leftEncoderTicks = 0
rightEncoderTicks = 0


# update left wheel encoder ticks
def callbackLeft(way):
   global leftEncoderTicks

   leftEncoderTicks += way

   print("left={}".format(leftEncoderTicks))

# update right wheel encoder ticks
def callbackRight(way):
   global rightEncoderTicks

   rightEncoderTicks += way

   print("right={}".format(rightEncoderTicks))
   

# stop the decoders
def cleanupEncoders():
   global decoderLeft
   global decoderRight

   decoderLeft.cancel()
   decoderRight.cancel()

   global pi
   pi.stop()


def checkEncoders(seconds):
   
   try:  
      dcMotorControl.set_wheel_drive_rates(0, 50)
      timed = 0
      while(timed < seconds):
         time.sleep(0.1)
         timed += 0.1
   
      print "stopping motors" 
      dcMotorControl.stop()   
      dcMotorControl.cleanup()
   
      # check if it continues turning during breaking
      timed = 0
      while(timed < 1):
         time.sleep(0.1)
         timed += 0.1 
   except:
      dcMotorControl.cleanup()


# setup the encoders when the script is imported
pi = pigpio.pi()

decoderLeft = pigpio_encoder.decoder(pi, 14, 15, callbackLeft)
decoderRight = pigpio_encoder.decoder(pi, 5, 6, callbackRight)


print "Starting motors"
checkEncoders(0.88)


time.sleep(1)

decoderLeft.cancel()
decoderRight.cancel()

pi.stop()
