from gpiozero import LED
from time import sleep

led = LED(18)  # pin numbers and GPIO/gpiozero numbers are different!

while True:
    led.on()
    sleep(1.5)
    led.off()
    sleep(1.5)
