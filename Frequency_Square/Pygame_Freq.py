# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame
import sys
import time
import thread

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Frequency Display")
pygame.display.update()
#clock = pygame.time.Clock()


#----------Setup Colors-----------------------------------------
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
#---------------------------------------------------------
f1 = 1 #time in ms for desired frequency 10hz
f2 = .008 #time in ms for desired frequency 60 hz
f3 = .016 #time in ms for desired frequency 30 hz
f4 = .025 #time in ms for desired frequency 20 hz
#---------------------------------------------------------

def rectul(): #rectangle upper left of screen
    Ctime1 = time.time()
    while((time.time() - Ctime1) <= f1):
		pass
    rectul = pygame.draw.rect(screen, red, (50,50,50,50), 0)#upper left
    pygame.display.update(rectul)
    #pygame.display.flip()
    Ctime1 = time.time()
    while((time.time() - Ctime1) <= f1):
		pass
    rectul = pygame.draw.rect(screen, white, (50,50,50,50), 0)#upper left
    pygame.display.update(rectul)
    #pygame.display.flip()
    return

def rectur(): #rectangle upper right of screen
    Ctime1 = time.time()
    while((time.time() - Ctime1) <= f2):
		pass
    rectur = pygame.draw.rect(screen, red, (200,50,50,50), 0)#upper left
    pygame.display.update(rectur)
    #pygame.display.flip()
    Ctime1 = time.time()
    while((time.time() - Ctime1) <= f2):
		pass
    rectur = pygame.draw.rect(screen, white, (200,50,50,50), 0)#upper left
    pygame.display.update(rectur)
    #pygame.display.flip()
    return



screen.fill(white)
pygame.display.flip()
#--------Main Infinite Loop -------------------------
while (True):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();
                
    #initialize screen
    screen.fill(white)
    
    
    #Drawings go here
    thread.start_new_thread(rectul,() )
    thread.start_new_thread(rectur,() )
    
    #update display
    pygame.display.flip()
    
    #refresh rate 60/s
    #clock.tick(60)   
    
pygame.quit()
