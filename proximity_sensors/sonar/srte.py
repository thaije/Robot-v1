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
      self.SOS=340.29
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
            self._distance = (ping_micros * self.SOS) / 2e4
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



#####################################################
# General functions
#####################################################


def initialize_default_sonars(pi):
    print "Initializing default sonars"
    sonars = []

    # Head sonar
    sonars.append(sonar(pi, None, 21))
    # Front sonars
    sonars.append(sonar(pi, None, 20))
    sonars.append(sonar(pi,   26, 16))

    return sonars


# read the proximity sensors 
def read_proximity_sensors(sonars):
    print "Read sonars"

    # trigger the sonars
    for sonar in sonars:
        sonar.trigger()

    time.sleep(0.03)

    # read the sonar results
    proximity = []
    for sonar in sonars: 
        proximity.append(sonar.read())

    return proximity


def cleanup_sonars(sonars):
    print "Cleaning up sonars"
    for sonar in sonars:
        sonar.cancel()


# test with externally initialized sonars and no cleanup
def test_sonars_external(sonars):
    print "Testing sonars for 5s"
    end = time.time() + 5.0
    r = 1

    while time.time() < end:
        print "Reading %d" % r
        readings = read_proximity_sensors(sonars)
        print readings

        time.sleep(0.02)
        r += 1


# test without having to set anything up
def test_sonars_allin():
    pi = pigpio.pi()
    sonars = initialize_default_sonars(pi)
    test_sonars_external(sonars)
    cleanup_sonars(sonars)
    pi.stop()
