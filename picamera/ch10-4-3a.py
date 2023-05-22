# image_effect

from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 180
#camera.hflip = True
camera.vflip = True
camera.start_preview()


camera.annotate_text = "negative"
camera.annotate_text_size = 50
camera.image_effect = "negative"
sleep(3)
camera.capture("./img/ch10-4-3a.jpg")
camera.stop_preview()
