from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(21)

for i in range(1,9):
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)

    