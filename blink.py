from gpiozero import LED
from time import sleep

led=LED(18)

while True:
    led.on()
    print("on")
    sleep(2)
    led.off()
    print("off")
    sleep(1)

