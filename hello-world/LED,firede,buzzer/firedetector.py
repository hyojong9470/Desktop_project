#TRUE가 ON FALSE 가 OFF
import RPi.GPIO as GPIO
from gpiozero import Buzzer
import time

LED = 16
flame = 2
buzzer = Buzzer(21)

GPIO.setmode(GPIO.BCM)
GPIO.setup(flame, GPIO.IN)  #불꽃은 입력
GPIO.setup(LED, GPIO.OUT)   #LED는 출력

print("LED STaRT\n")


try:
    for i in range(1,50):
        state = GPIO.input(flame) # state 가 0이면 불 / 1이면 불x
        if state==0:
            print("불이야!\n")
            buzzer.on()
            GPIO.output(LED, True)
        else:
            print("불 아니네....휴\n")
            buzzer.off()
            GPIO.output(LED, False)
    
        print(i)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

