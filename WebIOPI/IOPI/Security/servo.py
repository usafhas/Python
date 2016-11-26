import webiopi
from RPIO import PWM
servo = PWM.Servo()

# Set servo on GPIO17 to 2000µs (2.0ms)
servo.set_servo(24, 2000)

webiopi.runLoop()

server.stop()

GPIO = webiopi.GPIO

def left():
	

def right():

def set_speed(speed):
	GPIO.pulseRatio(24, speed)

GPIO.setFunction(24, GPIO.PWM)

set_speed(0.5)
stop()
server.addMacro(left)
server.addMacro(right)
