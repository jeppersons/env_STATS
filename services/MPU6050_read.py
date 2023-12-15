from adafruit_mpu6050 import MPU6050
import time

mpu6050=MPU6050.mpu6050(0x68)


#define a function to read sensor data
def read_sensor_data():
    #Read Values
    accelerometer_data = mpu6050.get_accel_data()
    




