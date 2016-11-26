#Heath Spidle
#RaspberryPi Python code for Pololu AltIMU-10 v3
#
#
#sudo i2cdetect -y 1
# 0 1 2 3 4 5 6 7 8 9 a b c d e f
#00: — — — — — — — — — — — — —
#10: — — — — — — — — — 19 — UU — — 1e —
#20: — — — — — — — — — — — — — — — —
#30: — — — — — — — — — — — UU — — — —
#40: — — — — — — — — — — — — — — — —
#50: — — — — — — — — — — — — — 5d — —
#60: — — — — — — — — — — — 6b — — — —
#70: — — — — — — — —
#6b = Gyro
#5d = Barometer
#1e = Magnometer
#19 = Accel

import smbus
import time
import math
#import numpy as np
i2c = smbus.SMBus(1)
GAdd = 0x6b
BAdd = 0x5d
MAdd = 0x1e
AAdd = 0x19

# Accel registers

ACCEL_CTRL_REG1_A = 0x20 # 00000111 rw
ACCEL_CTRL_REG2_A = 0x21 # 00000000 rw
ACCEL_CTRL_REG3_A = 0x22 # 00000000 rw
ACCEL_CTRL_REG4_A = 0x23 # 00000000 rw
ACCEL_CTRL_REG5_A = 0x24 # 00000000 rw
ACCEL_CTRL_REG6_A = 0x25 # 00000000 rw
ACCEL_REFERENCE_A = 0x26 # 00000000 r
ACCEL_STATUS_REG_A = 0x27 # 00000000 r
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

LSM303_MAGGAIN_1_3 = 0x20, # +/- 1.3
LSM303_MAGGAIN_1_9 = 0x40, # +/- 1.9
LSM303_MAGGAIN_2_5 = 0x60, # +/- 2.5
LSM303_MAGGAIN_4_0 = 0x80, # +/- 4.0
LSM303_MAGGAIN_4_7 = 0xA0, # +/- 4.7
LSM303_MAGGAIN_5_6 = 0xC0, # +/- 5.6
LSM303_MAGGAIN_8_1 = 0xE0 # +/- 8.1

#Gyrometer Registers
L3DG20_CTRL1 = 0x20
L3DG20_CTRL2 = 0x21
L3DG20_CTRL3 = 0X22
L3DG20_CTRL4 = 0X23
L3DG20_CTRL5 = 0X24
L3DG20_REFERENCE = 0X25
L3DG20_OUT_TEMP = 0X26
L3DG20_STATUS = 0x27
L3DG20_OUT_X_L = 0x28
L3DG20_OUT_X_H = 0x29
L3DG20_OUT_Y_L = 0x2A
L3DG20_OUT_Y_H = 0x2B
L3DG20_OUT_Z_L = 0x2C
L3DG20_OUT_Z_H = 0x2D
L3DG20_FIFO_CTRL = 0x2E
L3DG20_FIFO_SRC = 0x2F

#Barometer/Altimeter
LPS331AP_CTRL_REG1 = 0x20
RES_ADDR = 0x10
LPS331AP_CTRL_REG2 = 0x21
Tempo1 = 0x2B #l ->
Tempo2 = 0x2C
Preso1 = 0x28 # ref -> l -> h
Preso2 = 0x29
Preso3 = 0x2A

k = .90
AA = 0.98
M_PI = 3.14159265358979323846
RAD_TO_DEG = 57.29578
def twoscomp( x ) :
#if(0x8000 & x):
# x = (x- 0x010000)
if (x > 32767):
x = x – 65536
return x
#return n if n < 32768 else n – 65536 # 2’s complement signed
def twoscomp24( x ) :
if(0x800000 & x):
x = – (0xFFFFFF – x)
return x

def twoscomp32( x ) :
if(0x40000000 & x):
x = – (0x40000000 – x)
return x

def altitudef() :
p = Pressuremb()
altf = (1 – ((p/1013.25)**0.190284)) *145366.45
return altf
def altitudem() :
p = Pressuremb()
altm = altitudef() * .3048
return altm

def TempdegC():
temp1 = i2c.read_byte_data(BAdd, Tempo1)
temp2 = i2c.read_byte_data(BAdd, Tempo2)
temp = (temp2 << 8) + temp1
temp = twoscomp(temp)
temp_DegC = 42.5 + temp/(120*4)
return temp_DegC

def Pressuremb():
press1 = i2c.read_byte_data(BAdd, Preso1)
press2 = i2c.read_byte_data(BAdd, Preso2)
press3 = i2c.read_byte_data(BAdd, Preso3)
press_hw = (press3<<16)|(press2<<8)|(press1)
press_hw = twoscomp32(press_hw)
pressure_mb = press_hw/4096
return pressure_mb

def Gyro_X():
gxh = i2c.read_byte_data(GAdd, L3DG20_OUT_X_H)
gxl = i2c.read_byte_data(GAdd, L3DG20_OUT_X_L)
gx = (gxh<<8)|gxl
gyroX = twoscomp(gx)#X values Gyro
rate_X = gyroX * .07
return rate_X
def Gyro_Y():
gyh = i2c.read_byte_data(GAdd, L3DG20_OUT_Y_H)
gyl = i2c.read_byte_data(GAdd, L3DG20_OUT_Y_L)
gy = (gyh<<8)|gyl
gyroY = twoscomp(gy)#Y values Mag
rate_Y = gyroY * .07
return rate_Y
def Gyro_Z():
gzh = i2c.read_byte_data(GAdd, L3DG20_OUT_Z_H)
gzl = i2c.read_byte_data(GAdd, L3DG20_OUT_Z_L)
gz = (gzh<<8)|gzl
gyroZ = twoscomp(gz)#Z values Mag
rate_Z = gyroZ * .07
return rate_Z

def Mag_X():
mxh = i2c.read_byte_data(MAdd, MAG_OUT_X_H_M)
mxl = i2c.read_byte_data(MAdd, MAG_OUT_X_L_M)
mx = (mxh<<8)|mxl
magX = twoscomp(mx)#X values Mag
return magX
def Mag_Y():
myh = i2c.read_byte_data(MAdd, MAG_OUT_Y_H_M)
myl = i2c.read_byte_data(MAdd, MAG_OUT_Y_L_M)
my = (myh<<8)|myl
magY = twoscomp(my) #Y values Mag
return magY
def Mag_Z():
mzh = i2c.read_byte_data(MAdd, MAG_OUT_Z_H_M)
mzl = i2c.read_byte_data(MAdd, MAG_OUT_Z_L_M)
mz = (mzh<<8)|mzl
magZ = twoscomp(mz) #Z Values Mag
return magZ
def heading_old():
x = Mag_X()
y = Mag_Y()
z = Mag_Z()
heading = ((x**2)+(y**2)+(z**2))**0.5
return heading
#Direction (y>0) = 90 – [arcTAN(x/y)]*180/
#Direction (y<0) = 270 – [arcTAN(x/y)]*180/
#Direction (y=0, x<0) = 180.0
#Direction (y=0, x>0) = 0.0
#return n if n < 32768 else n – 65536 # 2’s complement signed

def Acc_X():
axh = i2c.read_byte_data(AAdd, ACCEL_OUT_X_L_A)
axl = i2c.read_byte_data(AAdd, ACCEL_OUT_X_H_A)
ax = ((axh<<8)|axl)
accX = twoscomp(ax)#X values ACC
if(accX > 0):
accX = accX*10
return accX *(.001) #>> 4
def Acc_Y():
ayh = i2c.read_byte_data(AAdd, ACCEL_OUT_Y_L_A)
ayl = i2c.read_byte_data(AAdd, ACCEL_OUT_Y_H_A)
ay = ((ayh<<8)|ayl)
accY = twoscomp(ay)#Y values ACC

return accY*(.001) #>> 4
def Acc_Z():
azh = i2c.read_byte_data(AAdd, ACCEL_OUT_Z_L_A)
azl = i2c.read_byte_data(AAdd, ACCEL_OUT_Z_H_A)
az = ((azh<<8)|azl)
accZ = twoscomp(az)#Z values ACC
return accZ *(.001) #>> 4
def AccXangle():
AXangle = (math.atan2(Acc_X(),Acc_Y()))*RAD_TO_DEG
if(AXangle > 180):
AXangle -= 360.0
return AXangle
def AccYangle():
AYangle = (math.atan2(Acc_Z(),Acc_Y()))*RAD_TO_DEG
if(AYangle > 180):
AYangle -= 360.0
return AYangle
def heading():
Mheading = 180*math.atan2(Mag_X(), Mag_Y())/M_PI
if(Mheading<0):
Mheading += 360
return Mheading
#Direction (y>0) = 90 – [arcTAN(x/y)]*180/
#Direction (y<0) = 270 – [arcTAN(x/y)]*180/
#Direction (y=0, x<0) = 180.0
#Direction (y=0, x>0) = 0.0

def Tiltheading():
pitch = math.asin(Acc_X())
roll = math.asin(Acc_Y()/math.cos(pitch))

xh = Mag_X() * math.cos(pitch) + Mag_Z() * math.sin(pitch)
yh = Mag_X() * math.sin(roll) * math.sin(pitch) + Mag_Y() * math.cos(roll) – Mag_Z() * math.sin(roll) * math.cos(pitch)
zh = -Mag_X() * math.cos(roll) * math.sin(pitch) + Mag_Y() * math.sin(roll) + Mag_Z() * math.cos(roll) * math.cos(pitch)

TMheading = 180 * math.atan2(yh,xh)/M_PI
if(yh >=0 ):
return TMheading
else:
return (360 + TMheading)

def Xpitch():
ax1 = (180/M_PI)*math.atan2(Acc_X(),((Acc_Y()**2+Acc_Z()**2)**.5))
ax2 = (180/M_PI)*math.atan2(Acc_X(),((Acc_Y()**2+Acc_Z()**2)**.5))
ax3 = (180/M_PI)*math.atan2(Acc_X(),((Acc_Y()**2+Acc_Z()**2)**.5))
axa = (ax1 + ax2 + ax3)/3
#return (180/M_PI)*math.atan2(Acc_X(),(Acc_Y()**2+Acc_Z()**2)**.5)
#ax = (180/M_PI)*math.asin(Acc_X())
return axa

def Yroll():
ay1 = (180/M_PI)*math.atan2(Acc_Y(),((Acc_X()**2+Acc_Z()**2)**.5))
ay2 = (180/M_PI)*math.atan2(Acc_Y(),((Acc_X()**2+Acc_Z()**2)**.5))
ay3 = (180/M_PI)*math.atan2(Acc_Y(),((Acc_X()**2+Acc_Z()**2)**.5))
aya = (ay1 + ay2 + ay3)/3
#aya = (180/M_PI)*(math.atan2(Acc_Y(),Acc_Z()))
#ay = (180/M_PI)*math.asin(Acc_Y())
return aya

anglex = [Xpitch(),0,0]
angley = [Yroll(),0,0]
def tPitch():
gx1 = Gyro_X()
gx2 = Gyro_X()
gx3 = Gyro_X()
gx = (gx1 + gx2 + gx3)/3
anglex[1] = (1-k)*Xpitch() + (k)*(gx*.03 + anglex[0])
anglex[0]=anglex[1]
return anglex[1]
def tRoll():
gy1 = Gyro_Y()
gy2 = Gyro_Y()
gy3 = Gyro_Y()
gy = (gy1 + gy2 + gy3)/3
angley[1] = (1-k)*Yroll() + (k)*(gy*.03 + angley[0])
angley[0] = angley[1]
return angley[1]

def Initialize():
#Accelerometer
i2c.write_byte_data(AAdd, ACCEL_CTRL_REG1_A, 0x27) #initialise the Accelerometer
i2c.write_byte_data(AAdd, ACCEL_CTRL_REG4_A, 0x40)
#Magnometer
i2c.write_byte_data(MAdd, MAG_MR_REG_M, 0x00) #initialise the Magnetometer
#Gyroscope
i2c.write_byte_data(GAdd, L3DG20_CTRL1, 0x0F) #0b01011111
i2c.write_byte_data(GAdd, L3DG20_CTRL4, 0x00) #2000 dps multipy by .07 for degrees
#Barometer
i2c.write_byte_data(BAdd,LPS331AP_CTRL_REG1,0x00)
i2c.write_byte_data(BAdd,RES_ADDR,0x7A)
i2c.write_byte_data(BAdd,LPS331AP_CTRL_REG1,0x84)
i2c.write_byte_data(BAdd,LPS331AP_CTRL_REG2,0x01)
return -1