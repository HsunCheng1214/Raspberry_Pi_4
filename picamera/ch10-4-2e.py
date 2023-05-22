#set Contrast

from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 180
#camera.hflip = True
camera.vflip = True

camera.start_preview()
camera.brightness = 70
camera.contrast = 60
sleep(3)
camera.capture("./img/ch10-4-2e.jpg")
camera.stop_preview()
