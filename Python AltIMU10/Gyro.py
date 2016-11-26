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
#1e = Magnometer 
#19 = Accel 

import smbus
import time
import math

i2c = smbus.SMBus(1)
GAdd = 0x6b
BAdd = 0x5d
MAdd = 0x1e
AAdd = 0x19

#
CTRL1 = 0x20
CTRL2 = 0x21
CTRL3 = 0X22
CTRL4 = 0X23
CTRL5 = 0X24
REFERENCE = 0X25
OUT_TEMP = 0X26
STATUS = 0x27
OUT_X_L = 0x28
OUT_X_H = 0x29
OUT_Y_L = 0x2A
OUT_Y_H = 0x2B
OUT_Z_L = 0x2C
OUT_Z_H = 0x2D
FIFO_CTRL = 0x2E
FIFO_SRC = 0x2F



def twoscomp( x ) : 
	if(0x8000 & x): 
		x = - (0x010000 - x)
	return x

def twoscomp24( x ) :
	if(0x800000 & x):
		x = - (0xFFFFFF - x)
	return x

def twoscomp32( x ) :
	if(0x40000000 & x):
		x = - (0x40000000 - x)
	return x

i2c.write_byte_data(GAdd, CTRL1, 0x0F) #0b01011111
i2c.write_byte_data(GAdd, CTRL4, 0x00) #2000 dps multipy by .07 for degrees

while True:
	gxh = i2c.read_byte_data(GAdd, OUT_X_H)
	gxl = i2c.read_byte_data(GAdd, OUT_X_L)
	gx = (gxh<<8)|gxl
	gyroX = twoscomp(gx)#X values Gyro
	rate_X = gyroX * .07

	gyh = i2c.read_byte_data(GAdd, OUT_Y_H)
	gyl = i2c.read_byte_data(GAdd, OUT_Y_L)
	gy = (gyh<<8)|gyl
	gyroY = twoscomp(gy)#Y values Mag
	rate_Y = gyroY * .07

	gzh = i2c.read_byte_data(GAdd, OUT_Z_H)
	gzl = i2c.read_byte_data(GAdd, OUT_Z_L)
	gz = (gzh<<8)|gzl
	gyroZ = twoscomp(gz)#Z values Mag
	rate_Z = gyroZ * .07
	print "Gyrometer Output\t", rate_X, "x\t", rate_Y, "y\t", rate_Z, "z"
	print "Gyrometer Raw\t", gyroX, "x\t", gyroY, "y\t", gyroZ, "z"
	time.sleep(1)
