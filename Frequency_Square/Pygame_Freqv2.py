# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame
import sys
import time
import threading

#QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_X11InitThreads)
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
f1 = .05 #time in ms for desired frequency 10hz
f2 = .008 #time in ms for desired frequency 60 hz
f3 = .016 #time in ms for desired frequency 30 hz
f4 = .025 #time in ms for desired frequency 20 hz
#---------------------------------------------------------

def rectul(): #rectangle upper left of screen
#    Ctime1 = time.time()
#    while((time.time() - Ctime1) <= f1):
#		pass
    time.sleep(f1)
    rectul = pygame.draw.rect(screen, red, (50,50,50,50), 0)#upper left
    pygame.display.update(rectul)
    #pygame.display.flip()
#    Ctime1 = time.time()
#    while((time.time() - Ctime1) <= f1):
#		pass
    time.sleep(f1)
    rectul = pygame.draw.rect(screen, white, (50,50,50,50), 0)#upper left
    pygame.display.update(rectul)
    #pygame.display.flip()
    return

def rectur(): #rectangle upper right of screen
#    Ctime1 = time.time()
#    while((time.time() - Ctime1) <= f2):
#		pass
    time.sleep(f2)
    rectur = pygame.draw.rect(screen, red, (400,50,50,50), 0)#upper left
    pygame.display.update(rectur)
    #pygame.display.flip()
#    Ctime1 = time.time()
#    while((time.time() - Ctime1) <= f2):
#		pass
    time.sleep(f2)
    rectur = pygame.draw.rect(screen, white, (400,50,50,50), 0)#upper left
    pygame.display.update(rectur)
    #pygame.display.flip()
    return

def rectlr(): #rectangle upper right of screen
#    Ctime1 = time.time()
#    while((time.time() - Ctime1) <= f3):
#		pass
    time.sleep(f3)
    rectlr = pygame.draw.rect(screen, red, (400,400,50,50), 0)#upper left
    pygame.display.update(rectlr)
    #pygame.display.flip()
#    Ctime1 = time.time()
#    while((time.time() - Ctime1) <= f3):
#		pass
    time.sleep(f3)
    rectlr = pygame.draw.rect(screen, white, (400,400,50,50), 0)#upper left
    pygame.display.update(rectlr)
    #pygame.display.flip()
    return

def rectll(): #rectangle upper left of screen
#    Ctime1 = time.time()
#    while((time.time() - Ctime1) <= f4):
#		pass
    time.sleep(f4)
    rectll = pygame.draw.rect(screen, red, (50,400,50,50), 0)#upper left
    pygame.display.update(rectll)
    #pygame.display.flip()
#    Ctime1 = time.time()
#    while((time.time() - Ctime1) <= f4):
#		pass
    time.sleep(f4)
    rectll = pygame.draw.rect(screen, white, (50,400,50,50), 0)#upper left
    pygame.display.update(rectll)
    #pygame.display.flip()
    return

def check():
	for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();
	return

basicfont = pygame.font.SysFont(None, 24)
text1 = basicfont.render('10Hz', True, (255, 0, 0), (255, 255, 255))
text4 = basicfont.render('20Hz', True, (255, 0, 0), (255, 255, 255))
text3 = basicfont.render('30Hz', True, (255, 0, 0), (255, 255, 255))
text2 = basicfont.render('60Hz', True, (255, 0, 0), (255, 255, 255))


screen.fill(white)

screen.blit(text1,(50,110))
screen.blit(text2,(400,110))
screen.blit(text3,(400,460))
screen.blit(text4,(50,460))



pygame.display.flip()
#--------Main Infinite Loop -------------------------
while (True):
    checkt = threading.Thread(target=check,args=())
    checkt.start()
                
    #initialize screen
    #screen.fill(white)
    
    
    #Drawings go here
    rectult = threading.Thread(target=rectul,args=())

    recturt = threading.Thread(target=rectur,args=())
    
    rectllt = threading.Thread(target=rectll,args=())
    
    rectlrt = threading.Thread(target=rectlr,args=())
    rectlrt.start()
    rectult.start()
    recturt.start()
    rectllt.start()
    
    #update display
    #pygame.display.flip()
    
    #refresh rate 60/s
    #clock.tick(60)   
    
pygame.quit()
