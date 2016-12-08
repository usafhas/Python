# Created by Heath Spidle
# 25 May 2016
# University of Texas at San Antonio
# GUI to flash squares at desired frequency for use with Brain Control Interfacing (BCI) SSVEP
# Created in virtualenv Frequency_Square

from Tkinter import *
import ttk 
import time

root = Tk() # create root window
root.title("SSVEP Frequency Generator")


mw = Canvas(root, width = 800, height = 800) # make main window (Canvas)
mw.pack()

rectul = mw.create_rectangle(50,50,100,100, fill="red") # rectangle upper left
rectll = mw.create_rectangle(50,400,100,450, fill="red")
rectur = mw.create_rectangle(400,50,450,100, fill="red")
rectrr = mw.create_rectangle(400,400,450,450, fill="red")


root.mainloop() # end of program




