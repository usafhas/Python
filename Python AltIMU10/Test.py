from SimpleCV import *
import time
c = SimpleCV.Camera()
js = SimpleCV.JpegStreamer("192.168.1.126:8080")  #starts up an http server (defaults to port 8080)
c.getImage().save(js)

while True:
  i = c.getImage()
  i.dl().text("This is a test",[50,50])
  i.save(js)
  time.sleep(0.5)
