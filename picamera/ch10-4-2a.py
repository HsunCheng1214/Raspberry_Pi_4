# add text on picture

from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 180
#camera.hflip = True
camera.vflip = True
camera.start_preview()
#
camera.annotate_text = "Raspberry Pi OS"
sleep(5)
camera.capture("./img/ch10-4-2a.jpg")
camera.stop_preview()
