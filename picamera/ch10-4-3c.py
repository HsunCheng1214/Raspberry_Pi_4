# Exposure

from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 180
#camera.hflip = True
camera.vflip = True

camera.start_preview()
camera.exposure_mode = "beach"
sleep(3)
camera.capture("./img/ch10-4-3c.jpg")
camera.stop_preview()
