# M6050 code.
# Adapted from https://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with-raspberry-pi
# With additional help from https://circuitdigest.com/microcontroller-projects/mpu6050-gyro-sensor-interfacing-with-raspberry-pi/

import smbus #SMBUS module of I2C
import string
import time
import os

# M6050 resgisters and addresses.

PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47
TEMP_OUT_H = 0x41

def MPU_init():
    # Write to sample rate register.
    bus.write_byte_data(device_address, SMPLRT_DIV, 7)
    
    # Write to power management register.
    bus.write_byte_data(device_address, PWR_MGMT_1, 1)
    
    # Write to configuration register.
    bus.write_byte_data(device_address, CONFIG, 0)
    
    # Write to gyro configuration register.
    bus.write_byte_data(device_address, GYRO_CONFIG, 24)
    
    # Write to interupt enable register.
    bus.write_byte_data(device_address, INT_ENABLE, 1)
    

def read_raw_data(addr):
    # Values are 16 bits.
    high = bus.read_byte_data(device_address, addr)
    low = bus.read_byte_data(device_address, addr+1)
    
    # Concatenate bytes.
    value = ((high << 8) | low)
    
    # Convert to signed.
    if (value > 32768):
        value = value - 65536
    return value
    
bus = smbus.SMBus(1)
device_address = 0x68

folder_path = '/home/pi/Documents/BeachCaptures' + time.strftime("%Y%m%d")

if os.path.isdir(folder_path) == False:
    os.mkdir(folder_path)
    print("Created folder")

m6050_log_file = 'm6050_log_' + time.strftime("%H%M%S") + '.csv'

MPU_init()

while True:
    f = open(folder_path + '/' + m6050_log_file,"a+")
    
    # Read accelerometer raw data.
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)
    
    # Read gyro raw values.
    gyro_x = read_raw_data(ACCEL_XOUT_H)
    gyro_y = read_raw_data(ACCEL_YOUT_H)
    gyro_z = read_raw_data(ACCEL_ZOUT_H)
    
    # Read raw tempreture values.
    temp = read_raw_data(TEMP_OUT_H)
    
    # Not sure why doing this still - to be investigated.
    ax = acc_x/16384.0
    ay = acc_y/16384.0
    az = acc_z/16384.0

    gx = gyro_x/131.0
    gy = gyro_y/131.0
    gz = gyro_z/131.0

    t = (temp / 340.0) + 36.53

    log_time = time.strftime("%H%M%S")
    f.write(str(gx) + ',' + str(gy) + ',' + str(gz) + ',' + str(ax) + ',' + str(ay) + ',' + str(az) + ',' + str(t) + ',' + log_time)
    f.write('\n')
    f.close()
    print()     
    time.sleep(1)
    