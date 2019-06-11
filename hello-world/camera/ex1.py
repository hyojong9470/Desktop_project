from time import sleep
from picamera import PiCamera

with PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()

    sleep(2)
    camera.capture("/var/www/html/image.jpg")