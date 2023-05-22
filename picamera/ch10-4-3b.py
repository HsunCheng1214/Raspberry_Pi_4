# White Balance

from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 180
#camera.hflip = True
camera.vflip = True

camera.start_preview()
camera.awb_mode = "shade"
sleep(3)
camera.capture("./img/ch10-4-3b.jpg")
camera.stop_preview()
