# image_effect

from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 180
#camera.hflip = True
camera.vflip = True
camera.start_preview()


camera.annotate_text = "colorswap"
camera.annotate_text_size = 50
camera.image_effect = "colorswap"
sleep(5)
camera.capture("./img/ch10-4-3.jpg")
camera.stop_preview()
