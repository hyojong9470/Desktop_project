#TRUE가 ON FALSE 가 OFF
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
print("LED STaRT\n")


try:
    for i in range(1,3):
        GPIO.output(16, False)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

