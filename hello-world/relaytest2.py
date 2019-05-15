import RPi.GPIO as GPIO
from time import sleep
led_pin = 17
relay_pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(relay_pin, GPIO.OUT)


for i in range(1,3):
    print("Turn on\n")
    GPIO.output(relay_pin, GPIO.HIGH) #False 가 켜짐
    sleep(2)
    print("Turn off\n")
    GPIO.output(relay_pin, GPIO.LOW) # True 는 꺼짐
    sleep(2)

print("종료\n")
GPIO.cleanup()
