from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 60



# run video
# camera.rotation=180
#camera.start_preview()
sleep(10)
#camera.stop_preview()

# take picture
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/camera/image.jpg')
camera.stop_preview()