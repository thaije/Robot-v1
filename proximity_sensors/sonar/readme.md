# Parts:
- (3x) HC-SR04
- cables
- pinout board
- 2k resistor and 1k resistor (or 3x 1k resistor) for each sonar

# Pinout:
- Pinout from: https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
- Code from pigpio
- See parameters.yaml

## General wiring
- 3v3 to pinout board +
- Rpi ground to pinout ground
- BCM pin 26 to pinout row (this is your trigger pin)

##  Sonar 1 (head)
- Ground to pinout ground
- Vcc to pinout +
- Trigger to pinout trigger row
- echo to BCM 21

## Sonar 2 (front left as seen from robot)
- Same as Sonar 1 except for Echo
- Echo to BCM 20

## Sonar 3 (front right)
- Same as Sonar 1 except for Echo
- Echo to BCM 16
