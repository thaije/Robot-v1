# sudo apt-get install python-picamera


import picamera
from time import sleep

camera = picamera.PiCamera()
# the camera has been mounted upside down so flip it
camera.vflip = True
camera.brightness = 60 # tested during night

# take a picture:
# camera.capture('image.jpg')

# capture video 
# camera.start_recording('video.h264')
# sleep(5)
# camera.stop_recording()

# Stream video
# connect from outside with ssh to camera

# See an preview (stop with Ctrl+D)
camera.start_preview()
sleep(3)
camera.stop_preview()