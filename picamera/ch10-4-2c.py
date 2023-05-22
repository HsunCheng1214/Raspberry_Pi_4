#text color & background color

from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()
#camera.rotation = 180
#camera.hflip = True
camera.vflip = True
camera.start_preview()

#set color
camera.annotate_text = "Raspberry Pi OS"
camera.annotate_text_size = 70
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')

sleep(3)
camera.capture("./img/ch10-4-2c.jpg")
camera.stop_preview()
