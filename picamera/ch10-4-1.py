#camera preview

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
#camera.hflip = True
#camera.vflip = True
camera.start_preview()
sleep(5)
camera.stop_preview()
