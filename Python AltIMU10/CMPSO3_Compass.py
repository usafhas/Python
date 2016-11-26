#Heath Spidle
#RaspberryPi Python code for Pololu AltIMU-10 v3
#LSM303 DLHC Compass
#
#sudo i2cdetect -y 1
#     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
#00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
#10: -- -- -- -- -- -- -- -- -- 19 -- UU -- -- 1e -- 
#20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
#30: -- -- -- -- -- -- -- -- -- -- -- UU -- -- -- -- 
#40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
#50: -- -- -- -- -- -- -- -- -- -- -- -- -- 5d -- -- 
#60: -- -- -- -- -- -- -- -- -- -- -- 6b -- -- -- -- 
#70: -- -- -- -- -- -- -- --  
#6b = Gyro
#5d = Barometer
#1e = Accel/Magnometer       

import smbus
import time

bus = smbus.SMBus(1)
GAddress = 0x6b
BAddress = 0x5d
MAddress = 0x1e

def bearing255():
	bear = bus.read_byte_data(MAddress, 1)
	return bear

def bearing3599():
	bear1 = bus.read_byte_data(MAddress, 2)
	bear2 = bus.read_byte_data(MAddress, 3)
	bear = (bear1 << 8) + bear2
	bear = bear/10.0
	return bear

while True:
	bearing = bearing3599()
	bear255 = bearing255()

	print bearing
	print bear255
	time.sleep(1)
