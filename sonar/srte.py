#!/usr/bin/env python

# srte.py

# How to run:
# install according to readme
# Install pigpio http://abyz.co.uk/rpi/pigpio/download.html
# sudo pigpiod
# import srte from another file
# read_proxmity_sensors() to retrieve readings
# sudo killall pigpiod

import time
import pigpio # http://abyz.co.uk/rpi/pigpio/python.html

SOS=340.29

class sonar:
   """
   Class to read distance using a sonar ranger.

   Instantiate with the Pi, trigger GPIO, and echo GPIO.

   Trigger a reading with trigger().

   Wait long enough for the maximum echo time and get the
   reading in centimetres with read().   A reading of 999.9
   indicates no echo.

   When finished call cancel() to tidy up.
   """
   def __init__(self, pi, trigger, echo):
      self.pi = pi
      self.trig = trigger

      self._distance = 999.9
      self._one_tick = None

      if trigger is not None:
         pi.set_mode(trigger, pigpio.OUTPUT)

      pi.set_mode(echo, pigpio.INPUT)

      self._cb = pi.callback(echo, pigpio.EITHER_EDGE, self._cbf)

   def _cbf(self, gpio, level, tick):
      if level == 1:
         self._one_tick = tick
      else:
         if self._one_tick is not None:
            ping_micros = pigpio.tickDiff(self._one_tick, tick)
            self._distance = (ping_micros * SOS) / 2e4
            self._one_tick = None

   def trigger(self):
      self._distance = 999.9
      self._one_tick = None

      if self.trig is not None:
         self.pi.gpio_trigger(self.trig, 15) # 15 micros trigger pulse

   def read(self):
      return self._distance

   def cancel(self):
      self._cb.cancel()


S = []
pi = None

def setup():
    global pi
    pi = pigpio.pi()

    if not pi.connected:
      exit()

    global S
    # Head sonar
    S.append(sonar(pi, None, 21))
    # Front sonars
    S.append(sonar(pi, None, 20))
    S.append(sonar(pi,   26, 16))

    end = time.time() + 30.0

def cleanup():
   global pi
   pi.stop()

# read the proximity sensors
def read_proximity_sensors():

    # [Head sonar, right sonar, left sonar]
    proximity = []

    try:
        # trigger the sonar
        for s in S:
            s.trigger()

        time.sleep(0.03)

        # read the sonar results
        for s in S:	
            proximity.append(s.read())

    except KeyboardInterrupt:
        pass

    for s in S:
        s.cancel()

    return proximity

if __name__ == "__main__":

    # setup()
    # readings = read_proximity_sensors()
    # print readings
    # cleanup()
    test()


def test2():
    
    setup()

    end = time.time() + 30.0
    r = 1

    while time.time() < end:

        print "Reading %d" % r
        readings = read_proximity_sensors()
        print readings

        time.sleep(0.02)
        r += 1

    cleanup()

def test():
   import time
   import pigpio
   import srte

   pi = pigpio.pi()

   if not pi.connected:
      exit()

   S=[]
   # Head sonar
   S.append(srte.sonar(pi, None, 21))
   # Front sonars
   S.append(srte.sonar(pi, None, 20))
   S.append(srte.sonar(pi,   26, 16))

   end = time.time() + 30.0

   r = 1

   try:
      while time.time() < end:

     	for s in S:
            s.trigger()

        time.sleep(0.03)
	
        i = 1
        for s in S:	
            print("Sensor {} {} {:.1f}".format(i, r, s.read()))
            i += 1;

        time.sleep(0.02)

        r += 1

    except KeyboardInterrupt:
        pass

    print("\ntidying up")

    for s in S:
      s.cancel()

    pi.stop()
