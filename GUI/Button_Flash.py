# -*- coding: utf-8 -*-
"""
Created on Thu May 26 20:34:57 2016

@author: Heath
"""

from Tkinter import *

master = Tk()

def callback():
    print "click!"
    
mw = Canvas(master, width = 800, height = 800) # make main window (Canvas)


b = Button(master, text="OK", command=callback)
b.config(activebackground="RED")
b.config(bg="BLUE")
b.flash()
b.pack()

mainloop()