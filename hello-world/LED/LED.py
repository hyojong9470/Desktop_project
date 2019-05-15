import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
print("LED STaRT\n")

for i in range(1,11):
    print(i)
    GPIO.output(16, True)
    time.sleep(1)
    GPIO.output(16, False)
    time.sleep(1)

print("END LED")

GPIO.cleanup()
