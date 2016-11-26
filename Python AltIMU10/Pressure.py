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

CTRL_REG1 = 0x20
RES_ADDR = 0x10
CTRL_REG2 = 0x21
Tempo1 = 0x2B #l ->
Tempo2 = 0x2C
Preso1 = 0x28 # ref -> l -> h
Preso2 = 0x29
Preso3 = 0x2A

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
def altitudef( p ) :
	altf = (1 - ((p/1013.25)**0.190284)) *145366.45
	return altf
def altitudem( p ) :
	altm = altitudef(p) * .3048
	return altm

while True:
	i2c.write_byte_data(BAdd,CTRL_REG1,0x00)
	i2c.write_byte_data(BAdd,RES_ADDR,0x7A)
	i2c.write_byte_data(BAdd,CTRL_REG1,0x84)
	i2c.write_byte_data(BAdd,CTRL_REG2,0x01)
	time.sleep(.5)
	temp1 = i2c.read_byte_data(BAdd, Tempo1)
	temp2 = i2c.read_byte_data(BAdd, Tempo2)
	temp = (temp2 << 8) + temp1
	temp = twoscomp(temp)
	temp_DegC = 42.5 + temp/(120*4)
	
	press1 = i2c.read_byte_data(BAdd, Preso1)
	press2 = i2c.read_byte_data(BAdd, Preso2)
	press3 = i2c.read_byte_data(BAdd, Preso3)
#	press_hw = ((press3 << 16)+ press2 << 8) + press1
	press_hw = (press3<<16)|(press2<<8)|(press1)
	press_hw = twoscomp32(press_hw)
	pressure_mb = press_hw/4096
	print temp_DegC, "C \t ", pressure_mb, "mb\t ", altitudef(pressure_mb), "Alt ft \t ", altitudem(pressure_mb), "Alt m"
	
