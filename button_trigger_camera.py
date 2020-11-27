import picamera
from gpiozero import LED, Button
from time import sleep
import time

# Configure buttons/indicators.
button = Button(15)
led = LED(14)
led.off()

# Start the camera in preview mode.
camera = picamera.PiCamera()

# try:
camera.start_preview()

waiting_for_button = True
while waiting_for_button:
    button.wait_for_press()
    print("You pushed the button! Photo taken")
    led.on()
    image_date = time.strftime("%Y%m%d")
    image_time = time.strftime("%H%M%S")
    image_name = 'image_' + image_date + '-' + image_time + '.jpg'
    camera.capture('/home/pi/BeachCaptures/' + image_name)
    sleep(1)
    led.off()
    waiting_for_button = False
    f = open('/home/pi/BeachCaptures/image_log_2.txt',"a+")
    f.write(image_name + ',' + image_date + ',' + image_time)
    f.write('\n')
    f.close()

# finally:    
camera.stop_preview()
camera.close()

