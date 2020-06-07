#Danny Vu
#2.23.16

import pygame, sys
from pygame.locals import *
import random
pygame.init()
theScreen = pygame.display.set_mode((800,600))

####################
# Your code starts here..
"""
window.fill((200,100,0))
pygame.draw.line(window,black,(400,500),(200,300),5)
pygame.draw.circle(window,blue,(200,100),50,0)
pygame.draw.rect(window,red,(400,500,100,50),0)
pygame.draw.ellipse(window,green,(400,500,100,50),10)
pentPts = [(600,150),(700,250),(650,350),(550,350),(500,250)]
pygame.draw.polygon(window,white,trapPts,0)
pygame.draw.lines(window,black,False,pentPts,10)
pygame.draw.arc(window,green,(0,0,800,600),3.14,6.28,20)
"""
# Your code ends here
##################
def setTitle():
    mousePos = pygame.mouse.get_pos()
    pygame.display.set_caption("( " + str(mousePos[0])+", " + str(mousePos[1])+" )")

def Star(window,x,y):
    star = (255,255,200)
    starPts = [(x,y),(x-6,y+18),(x+10,y+7),(x-10,y+7),(x+6,y+18)]
    pygame.draw.polygon(window,star,starPts,3)
    
def StarrySky(window):
    for a in range(0,20):
        x = random.randint(10,790)
        y = random.randint(20,300)
        Star(window,x,y)

    

def drawSnowman(window):
    #setting window
    white = (255,255,255)
    window.fill((0,0,30))
    
    #moon
    moon = (255,255,200)
    pygame.draw.circle(window,moon,(150,100),100,0)
    pygame.draw.circle(window,(0,0,30),(225,100),100,0)
    
    #stars
    StarrySky(window)
    
    #ground
    ground = (38, 26, 13)
    pygame.draw.rect(window,ground,(0,330,800,300),0)
    
    #bottom circle
    snow = (255,255,255)
    pygame.draw.ellipse(window,snow,(330,400,200,200),0)
    
    #middle circle
    pygame.draw.ellipse(window,snow,(350,300,160,150),0)
    
    #head circle
    pygame.draw.ellipse(window,snow,(380,220,110,120),0)
    
    #hat
    hat = (0, 128, 255)
    stripe = (255,255,255)
    basePts = [(410,190),(520,270),(510,290),(400,210)]
    pygame.draw.polygon(window,hat,basePts,0)
    topPts = [(460,170),(520,220),(500,250),(430,200)]
    pygame.draw.polygon(window,hat,topPts,0)
    midPts = [(430,190),(505,250),(500,260),(420,200)]
    pygame.draw.polygon(window,stripe,midPts,0)
    
    #eyes
    eyes = (50,155,50)
    pygame.draw.circle(window,eyes,(420,260),5,0)
    pygame.draw.circle(window,(0,0,0),(420,260),6,1)
    pygame.draw.circle(window,eyes,(450,260),5,0)
    pygame.draw.circle(window,(0,0,0),(450,260),6,1)
    
    #nose
    nose = (255, 128, 0)
    nosePts = [(435,270),(405,290),(435,285)]
    pygame.draw.polygon(window,nose,nosePts,0)
    
    #mouth
    mouth = (26, 13, 0)
    pygame.draw.circle(window,mouth,(460,290),4,0)
    pygame.draw.circle(window,(0,0,0),(460,290),5,1)
    pygame.draw.circle(window,mouth,(452,300),4,0)
    pygame.draw.circle(window,(0,0,0),(452,300),5,1)    
    pygame.draw.circle(window,mouth,(442,303),4,0)
    pygame.draw.circle(window,(0,0,0),(442,303),5,1)
    pygame.draw.circle(window,mouth,(430,305),4,0)
    pygame.draw.circle(window,(0,0,0),(430,305),5,1)
    pygame.draw.circle(window,mouth,(418,303),4,0)
    pygame.draw.circle(window,(0,0,0),(418,303),5,1)
    pygame.draw.circle(window,mouth,(400,290),4,0)
    pygame.draw.circle(window,(0,0,0),(400,290),5,1)
    pygame.draw.circle(window,mouth,(408,300),4,0)
    pygame.draw.circle(window,(0,0,0),(408,300),5,1)
    
    #arms
    arms = (153, 102, 51)
    pygame.draw.line(window,arms,(370,360),(300,295),10)   #right arm
    pygame.draw.line(window,arms,(490,360),(560,295),10)   #left arm
    
    #fingers right arm
    pygame.draw.line(window,arms,(302,297),(280,305),5)
    pygame.draw.line(window,arms,(302,297),(280,295),5)
    pygame.draw.line(window,arms,(302,297),(285,285),5)
    pygame.draw.line(window,arms,(302,297),(295,280),5)
    pygame.draw.line(window,arms,(302,297),(305,280),5)
    
    #fingers left arm
    pygame.draw.line(window,arms,(558,297),(575,305),5)
    pygame.draw.line(window,arms,(558,297),(575,295),5)
    pygame.draw.line(window,arms,(558,297),(560,285),5)
    pygame.draw.line(window,arms,(558,297),(550,280),5)
    pygame.draw.line(window,arms,(558,297),(540,280),5)

def drawTree(window):
    #trunk
    trunk = (153, 102, 51)
    pygame.draw.rect(window,trunk,(85,490,60,40),0)
    #tree
    tree = (0,150,0)
    treetop = [(115,230),(65,315),(165,315)]
    pygame.draw.polygon(window,tree,treetop,0)
    treemid = [(115,280),(45,400),(185,400)]
    pygame.draw.polygon(window,tree,treemid,0)
    treebottom = [(115,350),(15,495),(215,495)]
    pygame.draw.polygon(window,tree,treebottom,0)
    
    
    
    
    



def CreatedBy(window):
   basicFont = pygame.font.SysFont(None, 32)
   text = basicFont.render("Created by: Danny Vu", True, (255,255,255))
   textRect = text.get_rect()
   textRect.x = 800 - textRect.width
   textRect.y = 600 - textRect.height
   window.blit(text,textRect)
   
# Event loop
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
            
    setTitle()
    drawSnowman(theScreen)
    drawTree(theScreen)
    CreatedBy(theScreen)
    
    pygame.display.flip()

