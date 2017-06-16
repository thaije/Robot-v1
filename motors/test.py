
import time
import pigpio

import rotary_encoder
import sne73SoftwarePwm as dcMotorControl


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

decoder = rotary_encoder.decoder(pi, 5, 6, callback)
#decoder = rotary_encoder.decoder(pi, 27, 17, callback)


print "Starting motors"
checkEncoders(0.8)


time.sleep(1)

decoder.cancel()

pi.stop()
