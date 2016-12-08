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

f1 = .1 #time in ms for desired frequency 10hz
f2 = .016 #time in ms for desired frequency 60 hz
f3 = .033 #time in ms for desired frequency 30 hz
f4 = .05 #time in ms for desired frequency 20 hz

#--------------------------------------------------------------------------------------------------
def rectul_freq():
	global rectul
	
	Ctime1 = time.time()
	while((time.time() - Ctime1) <= f1):
		pass
	
	rectul = mw.create_rectangle(50,50,100,100, fill="red") # rectangle upper left
	#mw.update()

	root.after(1,rectulo)

def rectulo():
		
	Ctime1 = time.time()

	while((time.time() - Ctime1) <= f1):
		pass
				
	mw.delete(rectul)
	#mw.update()
	
	root.after(1,rectul_freq)
#-------------------------------------------------------------------------------------------------
def rectll_freq():
	global rectll
	
	Ctime2 = time.time()
	while((time.time() - Ctime2) <= f2):
		pass
	
	rectll = mw.create_rectangle(50,400,100,450, fill="red")
	#mw.update()
	root.after(1,rectllo)

def rectllo():
		
	Ctime2 = time.time()

	while((time.time() - Ctime2) <= f2):
		pass
				
	mw.delete(rectll)
	#mw.update()	
	root.after(1,rectll_freq)
#-------------------------------------------------------------------------------------------------
def rectur_freq():
	global rectur
	
	Ctime3 = time.time()
	while((time.time() - Ctime3) <= f3):
		pass
	
	rectur = mw.create_rectangle(400,50,450,100, fill="red")
	#mw.update()
	root.after(1,recturo)

def recturo():
		
	Ctime3 = time.time()

	while((time.time() - Ctime3) <= f3):
		pass
				
	mw.delete(rectur)
	#mw.update()	
	root.after(1,rectur_freq)
#-------------------------------------------------------------------------------------------------
def rectlr_freq():
	global rectlr
	
	Ctime4 = time.time()
	while((time.time() - Ctime4) <= f4):
		pass
	
	rectlr = mw.create_rectangle(400,400,450,450, fill="red")
	#mw.update()
	root.after(1,rectlro)

def rectlro():
		
	Ctime4 = time.time()

	while((time.time() - Ctime4) <= f4):
		pass
				
	mw.delete(rectlr)
	#mw.update()	
	root.after(1,rectlr_freq)
#-------------------------------------------------------------------------------------------------
def upleft():
	root.after(100,rectul_freq)
	return
def loleft():
	root.after(100,rectll_freq)
	return
def upright():
	root.after(100,rectur_freq)
	return
def loright():
	root.after(100,rectlr_freq)
	return
def update():
	while(True):
		mw.update()
		time.sleep(15)
	return
def threading():
	thread.start_new_thread(rectul_freq,() )
	thread.start_new_thread(rectll_freq,() )
	thread.start_new_thread(rectur_freq,() )
	thread.start_new_thread(rectlr_freq,() )
	thread.start_new_thread(update,())

	return


mw = Canvas(root, width = 800, height = 800) # make main window (Canvas)
mw.pack()





root.after(100,threading)
root.mainloop()
