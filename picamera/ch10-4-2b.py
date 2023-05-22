#set add text on picture size

from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 180
#camera.hflip = True
camera.vflip = True
camera.start_preview()
#
camera.annotate_text = "Raspberry Pi OS"
camera.annotate_text_size = 70

sleep(3)
camera.capture("./img/ch10-4-2b.jpg")
camera.stop_preview()
