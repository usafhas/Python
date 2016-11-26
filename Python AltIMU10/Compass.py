import smbus
import time

i2c = smbus.SMBus(1)
GAddress = 0x6b
BAddress = 0x5d
MAddress = 0x1e
AAddress = 0x19
#Magnometer
Out_x_hm = 0x09
Out_x_lm = 0x08
Out_y_hm = 0x0B
Out_y_lm = 0x0A
Out_z_hm = 0x0D
Out_z_lm = 0x0C

#Accelerometer
Out_x_ha = 0x29
Out_x_la = 0x28
Out_y_ha = 0x2B
Out_y_la = 0x2A
Out_z_ha = 0x2C
Out_z_la = 0x2D

MFIFO_CTRL = 0x2E
Default = 0x00 #Default/Bypass
FIFO = 0x40 #FIFO 0x20
MCTRL1 = 0x20
MCTRL5 = 0x24
	
while True:
	i2c.write_byte_data(MAddress,0x1F, 0xC0)
	time.sleep(.1)
	i2c.write_byte_data(MAddress,0x02, 0x00)
	i2c.write_byte_data(MAddress,0x2E,Default)

	#i2c.write_word_data(MAddress,0x2E,Default)
	time.sleep(.1)
	i2c.write_byte_data(MAddress,0x2E,FIFO)
	time.sleep(.1)
	i2c.write_byte_data(MAddress,MCTRL1,0x97)
	i2c.write_byte_data(MAddress,MCTRL5, 0x0C)
        
	Mag2 = i2c.read_byte_data(MAddress,Out_x_lm)
	Mag1 = i2c.read_byte_data(MAddress,Out_x_hm)
	Mag4 = i2c.read_byte_data(MAddress,Out_y_lm)
	Mag3 = i2c.read_byte_data(MAddress,Out_y_hm)
	Mag6 = i2c.read_byte_data(MAddress,Out_z_lm)
	Mag5 = i2c.read_byte_data(MAddress,Out_z_hm)
		
	Acc2 = i2c.read_byte_data(AAddress,Out_x_la)
	Acc1 = i2c.read_byte_data(AAddress,Out_x_ha)
	Acc4 = i2c.read_byte_data(AAddress,Out_y_la)
	Acc3 = i2c.read_byte_data(AAddress,Out_y_ha)
	Acc6 = i2c.read_byte_data(AAddress,Out_z_la)
	Acc5 = i2c.read_byte_data(AAddress,Out_z_ha)

	Magx = (Mag1 << 8) + Mag2
	Magy = (Mag3 << 8) + Mag4
	Magz = (Mag5 << 8) + Mag6
	Accx = (Acc1 << 8) + Acc2
	Accy = (Acc3 << 8) + Acc4
	Accz = (Acc5 << 8) + Acc6
	print "Magnemometer   ", Magx, "x ", Magy, "y ", Magz, "z "
	print "Accelerometer  ", Accx, "x ", Accy, "y ", Accz, "z "
