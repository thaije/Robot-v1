from RPIO import PWM
from time import sleep

servo = PWM.Servo()
servo.set_servo(17,1500)

sleep(2)

servo.stop_servo(17)

