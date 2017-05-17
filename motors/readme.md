### General wiring:
- Connect 6v external battery to pinout board
- Connect ground pinout board to ground rpi

# Servos
File: servoWirPWM.py

### Parts
- 2 HC 180 degree servos

### Wiring

#### Servo 1:
- Black: Ground rpi
- Red: 6v pinout board
- Yellow: BCM pin 18

#### Servo 2:
- Black: Ground rpi
- Red: 6v pinout board
- Yellow: BCM pin 13


# DC Motors
File: sne73SoftwarePWM.py

### Parts
- SN75441ONE chip
- external 6v battery
- pinout board
- 2 dc motors

### Wiring
#### DC motor 1:
pinForward, pinBackward, pinControl):
Motor(16, 22, 18) (Board pins)

#### DC motor 2:
pinForward, pinBackward, pinControl):
Motor(23, 19, 21) (Board pins)


# Extra needed parts:
- PWM adafruit shield
- ultrasonic sensor
- power connect cable
