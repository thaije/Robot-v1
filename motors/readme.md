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
- Black: Ground rpi
- Red: 6v on pinout board
- Yellow: BCM pin 18

#### Servo 2:
- Black: Ground rpi
- Red: 6v on pinout board
- Yellow: BCM pin 13


# DC Motors
- File: sne73SoftwarePWM.py
- Tutorial from: http://www.knight-of-pi.org/simple-dc-motor-board-for-the-raspberry-pi-with-ic-l293-and-software-pulse-width-modulation/ 

### Parts
- sne73 chip
- external 6v battery
- pinout board
- 2 dc motors

### Wiring
- See photos in folder for wiring
- sne73 flipped to right, pins mentioned are board pins
- Pin 16 - sne73 left 7
- Pin 18 - sne73 left 1
- Pin 19 - sne73 right 7
- Pin 21 - sne73 right 8
- Pin 22 - sne73 left 2
- Pin 23 - sne73 right 2
- Pin 2 (5v) - sne73 right 1
- Connect 6v external power to pinout board
- Connect pinout board + to sne73 left 8
- Pinout board ground to RPI ground
- Pinout board ground to: sne73 left 4 / 5 / sne73 right 4 / 5
- DC motor 1 green to sne73 right 3
- DC motor 1 yellow to sne73 right 6
- DC motor 2 green to sne73 left 3
- DC motor 2 yellow to sne73 left 6


#### DC motor 1:
pinForward, pinBackward, pinControl):
Motor(16, 22, 18) (Board pins)

#### DC motor 2:
pinForward, pinBackward, pinControl):
Motor(23, 19, 21) (Board pins)


# Extra needed parts:
- PWM adafruit shield
- ultrasonic sensor (3?)
- power connect cable
- stronger motor shield (sne73 can handle max 650ma, stall for motors is 2600ma)
- dc motors with encoder
- motor clamps 
- usb microphone