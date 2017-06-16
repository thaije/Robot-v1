
import time
import pigpio

import rotary_encoder

pos = 0

def callback(way):

   global pos

   pos += way

   print("pos={}".format(pos))

pi = pigpio.pi()

decoder = rotary_encoder.decoder(pi, 7, 8, callback)

time.sleep(300)

decoder.cancel()

pi.stop()
