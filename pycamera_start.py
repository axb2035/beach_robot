import picamera
from time import sleep

# Start the camera in preview mode for 10 seconds.
camera = picamera.PiCamera()
camera.start_preview()
sleep(10)
camera.stop_preview()