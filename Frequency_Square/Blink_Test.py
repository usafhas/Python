# Created by Heath Spidle
# 25 May 2016
# University of Texas at San Antonio
# GUI to flash squares at desired frequency for use with Brain Control Interfacing (BCI) SSVEP
# Created in virtualenv Frequency_Square

from Tkinter import *
import ttk 
import time
import thread

root = Tk() # create root window
root.title("SSVEP Frequency Generator")

f1 = .01 #time in ms for desired frequency

def rectul_freq():
	global rectul
	
	Ctime = time.time()
	while((time.time() - Ctime) <= f1):
		pass
	
	rectul = mw.create_rectangle(50,50,100,100, fill="red") # rectangle upper left

	root.after(1,rectulo)

def rectulo():
		
	Ctime = time.time()

	while((time.time() - Ctime) <= f1):
		pass
				
	mw.delete(rectul)
	
	

	root.after(1,rectul_freq)




mw = Canvas(root, width = 800, height = 800) # make main window (Canvas)
mw.pack()



root.after(100,rectul_freq)
root.mainloop() # end of program

