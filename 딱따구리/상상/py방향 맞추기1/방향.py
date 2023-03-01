import pygame, sys, random as r
from pygame.locals import *

pygame.init()
SC = pygame.display.set_mode((600, 600))
CL = pygame.time.Clock()
BL=(0,0,0)
W=(255,255,255)
B=(0,0,255)
i=0
cnt=0
r1=Rect(100,300,100,60)
r2=Rect(400,300,100,60)
fo2=pygame.font.SysFont(None, 100)

c1=''
while True:
    SC.fill(BL)
    cnt += 1
    dr_tx=fo2.render(c1,True,W)
    SC.blit(dr_tx, (285, 180))
    if cnt>=60:
        cnt=0
        r1=Rect(100,300,100,60)
        r2=Rect(400,300,100,60)
        b=r.randint(0,1)
        if b == 0:
            r1=Rect(100,300,150,90)
        else :
            r2=Rect(400,300,150,90)
    dr_tx=fo2.render("?",True,W)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button==1:
                if b == 0:
                    c1='O'
                else :
                    c1='X'
            if event.button==3:
                if b == 1:
                    c1='O'
                else :
                    c1='X'
        if event.type == MOUSEBUTTONUP :
            r1=Rect(100,300,100,60)
            r2=Rect(400,300,100,60)
    pygame.draw.rect(SC,B,r1)
    pygame.draw.rect(SC,W,r2)
    pygame.display.update()
    CL.tick(60)