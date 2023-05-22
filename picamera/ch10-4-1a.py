#camera preview & take picture

from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 180
#camera.hflip = True
camera.vflip = True
camera.start_preview()
sleep(5)
#
camera.capture("./img/ch10-4-1a.jpg")

camera.stop_preview()
