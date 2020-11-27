from gpiozero import LED, Button
from time import sleep

button = Button(15)
led = LED(14)
led.off()

while True:
    button.wait_for_press()
    print("You pushed the button!")
    led.on()
    sleep(3)
    led.off()
