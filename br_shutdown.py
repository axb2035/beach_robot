from gpiozero import Button
import os

Button(25).wait_for_press()
print("Shutting down...")
os.system("sudo poweroff -f")
