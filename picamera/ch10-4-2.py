#set resolution

from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 180
#camera.hflip = True
camera.vflip = True

camera.resolution = (2592 , 1944)
camera.framerate = 15

camera.start_preview()
sleep(5)
camera.capture("./img/ch10-4-2.jpg")
camera.stop_preview()
