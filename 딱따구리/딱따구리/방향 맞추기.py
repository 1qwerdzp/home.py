import pygame, sys, random as r
from pygame.locals import *

pygame.init()
SC = pygame.display.set_mode((600, 600))
CL = pygame.time.Clock()

BL=(0,0,0)
W=(255,255,255)
R=(255,0,0)
G=(0,255,0)
B=(0,0,255)

d=('UP', "DONE","LEFT","RIGHT")
i=0
cnt=0

r1=Rect(250,200,100,60)
r2=Rect(250,400,100,60)
r3=Rect(100,300,100,60)
r4=Rect(400,300,100,60)
c1=G
c2=G
c3=G
c4=G

fo=pygame.font.SysFont(None, 36)
fo2=pygame.font.SysFont(None, 60)
u_tx=fo.render("UP",True,W)
d_tx=fo.render("DONE",True,W)
l_tx=fo.render("LEFT",True,W)
r_tx=fo.render("RIGHT",True,W)

while True:
    SC.fill(W)
    cnt += 1
    if cnt>=60:
        cnt=0
        i=r.randint(0,3)
    dr_tx=fo2.render(d[i],True,BL)
    SC.blit(dr_tx,(250,100))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_UP:
                if i == 0:
                    c1=B
                else :
                    c1=R
            if event.key==K_DOWN:
                if i == 1:
                    c2=B
                else :
                    c2=R
            if event.key==K_LEFT:
                if i == 2:
                    c3=B
                else :
                    c3=R
            if event.key==K_RIGHT:
                if i == 3:
                    c4=B
                else :
                    c4=R
        if event.type == KEYUP :
            c1,c2,c3,c4 = G,G,G,G
    pygame.draw.rect(SC,c1,r1)
    pygame.draw.rect(SC,c2,r2)
    pygame.draw.rect(SC,c3,r3)
    pygame.draw.rect(SC,c4,r4)

    SC.blit(u_tx,(285,220))
    SC.blit(d_tx,(260,420))
    SC.blit(l_tx,(120,320))
    SC.blit(r_tx,(410,320))

    pygame.display.update()
    CL.tick(60)