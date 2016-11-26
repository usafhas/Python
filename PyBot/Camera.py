from SimpleCV import *
import time
import IMU
import math

c = SimpleCV.Camera()
js = SimpleCV.JpegStreamer(“0.0.0.0:8080”,.5) #starts up an http server (defaults to port 8080)
c.getImage().save(js)

while True:
IMU.Initialize()
DTC = time.strftime(“%d/%m/%Y %H:%M:%S”)
temp = str((IMU.TempdegC()))
ro = IMU.Yroll()
pit = IMU.Xpitch()
alt = str((IMU.altitudem()))
accX = str(int(pit))
accY = str(int(ro))
head = str(int(IMU.heading()))

#tilthead = str(int(IMU.Tiltheading()))
i = c.getImage()
i.drawText(DTC, 500,430, color=Color.WHITE)
i.drawText(“Temp ” +temp+”C”, 20,415, color=Color.WHITE)
i.drawText(“Altitude “+ alt+ “m”,20,430, color=Color.WHITE)
i.drawText(“Pitch ” + accX + “:Roll ” + accY, 20,400, color=Color.WHITE)
i.drawText(“Heading ” + head + “deg”, 480,15, color=Color.WHITE)
####################################################
HUDlayer = DrawingLayer((i.width, i.height))
center_point = (i.width/2,i.height/2)

rolll = HUDlayer.line(center_point,((i.width/2)-40,(i.height/2)-(math.sin(ro)*30)),color=Color.BLACK, width=3)
rollr = HUDlayer.line(center_point,((i.width/2)+40,(i.height/2)+(math.sin(ro)*30)),color=Color.BLACK, width=3)
pointer = HUDlayer.circle(center_point, 10, color=Color.BLACK)
# pitch = HUDlayer.circle((i.width/2,i.height/2+math.sin(pit)*30),10,color=Color.BLACK)
zero = HUDlayer.line((i.width/2-20,i.height/2+math.sin(pit)*30),(i.width/2+20,i.height/2+math.sin(pit)*30), color=Color.BLACK, width=3)

ten = HUDlayer.line((i.width/2-15,i.height/2+math.sin(pit)*30+math.sin(10)*30),(i.width/2+15,i.height/2+math.sin(pit)*30+math.sin(10)*30), color=Color.BLACK, width=3)

mten = HUDlayer.line((i.width/2-15,i.height/2+math.sin(pit)*30-math.sin(10)*30),(i.width/2+15,i.height/2+math.sin(pit)*30-math.sin(10)*30), color=Color.BLACK, width=3)

i.addDrawingLayer(HUDlayer)
i.applyLayers()
##########################################################
#i.drawText(“Comp-Heading ” + tilthead + “deg”, 480,25, color=Color.WHITE)
i.save(js)

time.sleep(0.1)