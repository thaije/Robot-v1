import time
import pigpio

HALL=17

pi = pigpio.pi()

pi.set_mode(HALL, pigpio.INPUT)
pi.set_pull_up_down(HALL, pigpio.PUD_UP)

start = time.time()

while (time.time() - start) < 60:
    print("Hall = {}".format(pi.read(HALL)))
    time.sleep(0.2)

pi.stop()

