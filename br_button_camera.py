import picamera
from gpiozero import LED, Button
import time
import os

# Configure buttons/indicators.
button = Button(23)
led = LED(24)
led.off()
print("LED off...")
# check for existence of image folder, Create if doesn't exist.
folder_path = '/home/pi/Documents/BeachCaptures' + time.strftime("%Y%m%d")

if os.path.isdir(folder_path) == False:
    os.mkdir(folder_path)

print("Made new folder...")

exit

# Start the camera.
camera = picamera.PiCamera()
camera.start_preview()

print("Preview done...")
try:
    while True:
        button.wait_for_press()
        led.on()
        image_date = time.strftime("%Y%m%d")
        image_time = time.strftime("%H%M%S")
        image_name = 'image_' + image_date + '-' + image_time + '.jpg'
        camera.capture(folder_path + '/' + image_name)
        print("Write image...")
        waiting_for_button = False
        f = open(folder_path + '/' + 'image_log_2.txt',"a+")
        f.write(image_name + ',' + image_date + ',' + image_time)
        f.write('\n')
        f.close()
        print("Write log...")
        time.sleep(1)
        led.off()

finally:    
    camera.stop_preview()
    camera.close()

