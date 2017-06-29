# Uses decoder class to keep track of the movement 
# of the wheels

import time
import pigpio

import pigpio_encoder
import sn75SoftwarePwm as dcMotorControl

# One rotation is 360 ticks
# Forwards is positive, backwards is negative

leftEncoderTicks = 0
rightEncoderTicks = 0
pi = None

# update left wheel encoder ticks
def callbackLeftWheel(way):
   global leftEncoderTicks

   leftEncoderTicks += way

   print("left={}".format(leftEncoderTicks))

# update right wheel encoder ticks
def callbackRightWheel(way):
   global rightEncoderTicks

   rightEncoderTicks += way

   print("right={}".format(rightEncoderTicks))
   

# stop the decoders
def cleanupEncoders():
   time.sleep(1)
   global decoderLeft
   global decoderRight

   decoderLeft.cancel()
   decoderRight.cancel()

   global pi
   pi.stop()


def checkEncoders(seconds):
   
   try:  
      motor1 = Motor(23, 25, 24, 9.0) 
      motor2 = Motor(11, 10, 9, 9.0) 
      motors = [motor1, motor2]

      dcMotorControl.set_wheel_drive_rates(motors, 70, 70)
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

      dcMotorControl.cleanup([motor1, motor2])
   except:
      dcMotorControl.cleanup([motor1, motor2])



def encoderTest():
   # setup the encoders when the script is imported
   pi = pigpio.pi()

   decoderLeft = pigpio_encoder.decoder(pi, 14, 15, callbackLeftWheel)
   decoderRight = pigpio_encoder.decoder(pi, 5, 6, callbackRightWheel)

   print "Starting motors"
   checkEncoders(0.88)

   decoderLeft.cancel()
   decoderRight.cancel()
   pi.stop()

#encoderTest()
