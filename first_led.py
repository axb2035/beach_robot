from gpiozero import LED
import RPi.GPIO as GPIO
print(GPIO.RPI_INFO)

# GPIO.setmode(GPIO.BOARD)
# mypin = 8
# GPIO.setup(mypin, GPIO.OUT, initial=1) 

# import gpiozero
from time import sleep


led = LED(14)  # GPIO and gpiozero numbers are different!
led.on
# print(led)
# while True:
#    led.on()
print("LED on")
sleep(1)
#    led.off()
#    print("LED off")
#    sleep(1)
GPIO.cleanup()