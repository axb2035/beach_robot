import serial
import time
import string
import os

import pynmea2

folder_path = '/home/pi/Documents/BeachCaptures' + time.strftime("%Y%m%d")

if os.path.isdir(folder_path) == False:
    os.mkdir(folder_path)
    print("Created folder")

gps_log_file = 'gps_log_' + time.strftime("%H%M%S") + '.csv'

while True:
    f = open(folder_path + '/' + gps_log_file,"a+")
    port="/dev/serial0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline().decode("utf-8")
    #print(newdata)
    
    if newdata[0:6] == "$GPRMC":
        log_time = time.strftime("%H%M%S")
        newmsg = pynmea2.parse(newdata)
        lat = newmsg.latitude
        lng = newmsg.longitude
        gps = "Longitude: " + str(lng) + " Latitude: " + str(lat) + ' Time: ' + log_time
        f.write(str(lng) + ',' + str(lat) + ',' + log_time)
        f.write('\n')
        f.close()