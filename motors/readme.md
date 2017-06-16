### General wiring:
- Connect 6v external battery to pinout board
- Connect ground pinout board to ground rpi

# Servos
File: servoWirPWM.py

### Parts
- 2 HC 180 degree servos
- external 6v battery
- pinout board

### Wiring

#### Servo 1:
- Black: Ground pinout board
- Red: 6v on pinout board
- Yellow: BCM pin 18

#### Servo 2:
- Black: Ground pinout board
- Red: 6v on pinout board
- Yellow: BCM pin 13


# DC Motors
- File: sne73SoftwarePWM.py
- Tutorial from: http://www.knight-of-pi.org/simple-dc-motor-board-for-the-raspberry-pi-with-ic-l293-and-software-pulse-width-modulation/ 

### Parts
- sne73 chip
- external 6v battery (shared with servos)
- pinout board
- 2 dc motors
- 2 Hall sensor encoders for the dc motors

### Wiring
- See photos in folder for wiring
- sne73 flipped to right, pins mentioned are board pins
- BCM pin 23 - sne73 left 7
- BCM pin 24 - sne73 left 1
- BCM pin 10 - sne73 right 7
- BCM pin 9 - sne73 right 8
- BCM pin 25 - sne73 left 2
- BCM pin 11 - sne73 right 2
- Pin 2 (5v) - sne73 right 1
- Connect 6v external power to pinout board
- Connect pinout board + to sne73 left 8
- Pinout board ground to RPI ground
- Pinout board ground to: sne73 left 4 / 5 / sne73 right 4 / 5
- DC motor 1 green to sne73 right 3
- DC motor 1 yellow to sne73 right 6
- DC motor 2 green to sne73 left 3
- DC motor 2 yellow to sne73 left 6

#### Encoder wiring
- 3v3 pin (pin 1) to pinout board (not same side as 6v)
- ground from rpi to pinout board
- 3v3 input pins from encoders to pinout board +
- ground pins from encoders to pinout board ground
- Right motor encoder output 1 (yellow) to BCM 17 / pin 11
- Right motor encoder output 2 (green) to BCM 27 / pin 13
- Left motor encoder ouput 1 (yellow) to BCM 5 / pin 29
- Left motor encoder ouput 2 (green) to BCM 6 / pin 31

#### DC motor 1:
pinForward, pinBackward, pinControl):
motor1 = Motor(23, 25, 24) (BCM pins)

#### DC motor 2:
pinForward, pinBackward, pinControl):
motor2 = Motor(11, 10, 9) (BCM pins)


# Extra needed parts:
- PWM adafruit shield
- ultrasonic sensor (3?)
- stronger motor shield (sne73 can handle max 650ma, stall for motors is 2600ma)
- motor clamps 
- Laser?