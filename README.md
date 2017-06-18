# Robot
Raspberry pi robot using 

# Dependencies
- RPIO
- RPi.GPIO
- pigpio
- pyyaml

# Parts:
- Raspberry pi 2b
- 2 V-tec 6v 177 RPM DC motors (https://eckstein-shop.de/V-TEC-6V-Mini-25D-DC-Motor-Getriebe-Motor-Stirnradgetriebe-mit-Encoder-177-RPM-EN)
- 2 Pololu Wheel 90×10mm Pair - Black
- SN754410 H-bridge for DC motor control
- Castor/ ball wheel
- 2 Hitec HS-422 180 degree servo's with pan-tilt set
- Raspberry pi v2 camera mounted on pan-tilt set
- 3 HC-SR04 sonars, 1 mounted on pan-tilt set, 2 mounted at front at a 20°. 
- Xiaomi 10000 mAh powerbank for rpi
- 3300 mAh NiMh battery for servos / dc motors 
- 2 Pinout boards
- Pinout cables


#Todo
## Todo
- Align motors (ticks per revolution)
- Make calibration method for motors
- Offline speech synthesis (espeak) on rpi
- Offline speech recognition (cmu sphinx) on rpi
- Connect / test MPU
- Connect pi camera to opencv / simplecv
- Build slam

## Todo (optional)
- Add manual control option with Xbox controller
- Online/API speech synthesis (wave net)
- Online/API speech recognition (wave net)
- Monocular slam

## Done
- Mounted sonars / camera on head
- Write readme for sonars
- Tested distance sensors
- setup remote access
- Tested encoders
- Test new DC motors
- Extend robot frame for DC motors, balanced
- Mount wheels, DC motors, batteries
- Connected servos
- Tested servos
- Connected DC motors
- Tested DC motors
- Connected / tested speaker
- Connected / tested mic
