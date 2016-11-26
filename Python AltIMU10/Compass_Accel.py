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

# Accel registers

ACCEL_CTRL_REG1_A = 0x20   # 00000111   rw
ACCEL_CTRL_REG2_A = 0x21   # 00000000   rw
ACCEL_CTRL_REG3_A = 0x22   # 00000000   rw
ACCEL_CTRL_REG4_A = 0x23   # 00000000   rw
ACCEL_CTRL_REG5_A = 0x24   # 00000000   rw
ACCEL_CTRL_REG6_A = 0x25   # 00000000   rw
ACCEL_REFERENCE_A = 0x26   # 00000000   r
ACCEL_STATUS_REG_A = 0x27   # 00000000   r
ACCEL_OUT_X_L_A = 0x28
ACCEL_OUT_X_H_A = 0x29
ACCEL_OUT_Y_L_A = 0x2A
ACCEL_OUT_Y_H_A = 0x2B
ACCEL_OUT_Z_L_A = 0x2C
ACCEL_OUT_Z_H_A = 0x2D
ACCEL_FIFO_CTRL_REG_A = 0x2E
ACCEL_FIFO_SRC_REG_A = 0x2F
ACCEL_INT1_CFG_A = 0x30
ACCEL_INT1_SOURCE_A = 0x31
ACCEL_INT1_THS_A = 0x32
ACCEL_INT1_DURATION_A = 0x33
ACCEL_INT2_CFG_A = 0x34
ACCEL_INT2_SOURCE_A = 0x35
ACCEL_INT2_THS_A = 0x36
ACCEL_INT2_DURATION_A = 0x37
ACCEL_CLICK_CFG_A = 0x38
ACCEL_CLICK_SRC_A = 0x39
ACCEL_CLICK_THS_A = 0x3A
ACCEL_TIME_LIMIT_A = 0x3B
ACCEL_TIME_LATENCY_A = 0x3C
ACCEL_TIME_WINDOW_A = 0x3D

#Mag registers

MAG_CRA_REG_M = 0x00
MAG_CRB_REG_M = 0x01
MAG_MR_REG_M = 0x02
MAG_OUT_X_H_M = 0x03
MAG_OUT_X_L_M = 0x04
MAG_OUT_Z_H_M = 0x05
MAG_OUT_Z_L_M = 0x06
MAG_OUT_Y_H_M = 0x07
MAG_OUT_Y_L_M = 0x08
MAG_SR_REG_Mg = 0x09
MAG_IRA_REG_M = 0x0A
MAG_IRB_REG_M = 0x0B
MAG_IRC_REG_M = 0x0C
MAG_TEMP_OUT_H_M = 0x06
MAG_TEMP_OUT_L_M = 0x05

#LSM303_REGISTER_MAG_CRB_REG_M (Mag Gain) values

LSM303_MAGGAIN_1_3 = 0x20,  # +/- 1.3
LSM303_MAGGAIN_1_9 = 0x40,  # +/- 1.9
LSM303_MAGGAIN_2_5 = 0x60,  # +/- 2.5
LSM303_MAGGAIN_4_0 = 0x80,  # +/- 4.0
LSM303_MAGGAIN_4_7 = 0xA0,  # +/- 4.7
LSM303_MAGGAIN_5_6 = 0xC0,  # +/- 5.6
LSM303_MAGGAIN_8_1 = 0xE0   # +/- 8.1

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

def heading(x,y,z):
	heading = ((x**2)+(y**2)+(z**2))**0.5
	return heading

i2c.write_byte_data(AAdd, ACCEL_CTRL_REG1_A, 0x27) #initialise the Accelerometer
i2c.write_byte_data(AAdd, ACCEL_CTRL_REG4_A, 0x40)

i2c.write_byte_data(MAdd, MAG_MR_REG_M, 0x00) #initialise the Magnetometer

while True:
	mxh = i2c.read_byte_data(MAdd, MAG_OUT_X_H_M)
	mxl = i2c.read_byte_data(MAdd, MAG_OUT_X_L_M)
	mx = (mxh<<8)|mxl
	magX = twoscomp(mx)#X values Mag

	myh = i2c.read_byte_data(MAdd, MAG_OUT_Y_H_M)
	myl = i2c.read_byte_data(MAdd, MAG_OUT_Y_L_M)
	my = (myh<<8)|myl
	magY = twoscomp(my) #Y values Mag

	mzh = i2c.read_byte_data(MAdd, MAG_OUT_Z_H_M)
	mzl = i2c.read_byte_data(MAdd, MAG_OUT_Z_L_M)
	mz = (mzh<<8)|mzl
	magZ = twoscomp(mz) #Z Values Mag

	print "Magnometer\t heading ", heading(magX,magY,magZ), "\t x ", magX, " y ", magY, " z ", magZ
	
	axl = i2c.read_byte_data(AAdd, ACCEL_OUT_X_L_A)
	axh = i2c.read_byte_data(AAdd, ACCEL_OUT_X_H_A)
	ax = (axh<<8)|axl
	accX = twoscomp(ax)#X values ACC

	ayl = i2c.read_byte_data(AAdd, ACCEL_OUT_Y_L_A)
	ayh = i2c.read_byte_data(AAdd, ACCEL_OUT_Y_H_A)
	ay = (ayh<<8)|ayl
	accY = twoscomp(ay)#Y values ACC

	azl = i2c.read_byte_data(AAdd, ACCEL_OUT_Z_L_A)
	azh = i2c.read_byte_data(AAdd, ACCEL_OUT_Z_H_A)
	az = (azh<<8)|azl
	accZ = twoscomp(az)#Z values ACC

	print "Accelerometer Output\t G total ", heading(accX,accY,accZ), "\t Gx ", accX, " Gy ", accY, " Gz ", accZ

	time.sleep(1)
