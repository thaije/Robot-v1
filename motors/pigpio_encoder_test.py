
import time
import pigpio

import pigpio_encoder
import sn75SoftwarePwm as dcMotorControl

# One rotation is 360 ticks
# Forwards is positive, backwards is negative

pos = 0

def callback(way):

   global pos

   pos += way

   print("pos={}".format(pos))
   


def checkEncoders(seconds):
   
   try:  
      dcMotorControl.move(50)
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



pi = pigpio.pi()

decoder = pigpio_encoder.decoder(pi, 14, 15, callback)
#decoder = pigpio_encoder.decoder(pi, 17, 27, callback)


print "Starting motors"
checkEncoders(0.75)


time.sleep(1)

decoder.cancel()

pi.stop()
