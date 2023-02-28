import pygame, sys
from pygame.locals import *

pygame.init()
SC = pygame.display.set_mode((300, 400))
CL = pygame.time.Clock()
font=pygame.font.SysFont(None, 36)
BL = (0, 0, 0)
W = (255, 255, 255)
R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)
pa=[0]
p1=[]
p2=[]
p=0
while True:
    SC.fill(W)
    for c in range(4):
        c = 25 + c * (250 / 3)
        pygame.draw.line(SC, BL, [c, 25], [c, 350], 4)
    for co in range(4):
        co = 25 + co * ((400 - 75) / 3)
        pygame.draw.line(SC, BL, [25, co], [275, co], 4)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        m=250/3/2
        m1=(400-75)/3/2
        if event.type == MOUSEBUTTONDOWN :
            x, y = int(event.pos[0]), int(event.pos[1])
            print(x, y)
            if 30<x<100 and 30<y<120:
                print(1)
                if int(pa.count(1))!=1:
                    if p==0:
                        p1+=[1]
                        tx1=font.render("1", True, (0, 0, 0))
                    if p==1 :
                        p2+=[1]
                        tx1=font.render("2", True, (0, 0, 0))
                    pa+=[1]
            elif 210<x<280 and 250<y<340 and int(pa.count(9))!=1:
                print(2)
                if p==0:
                    p1+=[9]
                    tx9=font.render("1", True, (0, 0, 0))
                if p==1 :
                    p2+=[9]
                    tx9=font.render("2", True, (0, 0, 0))
                pa+=[9]
            if p==0 :
                p=1
            else :
                p=0
    if int(pa.count(1))==1 :
        SC.blit(tx1, (25+m, 25+m1))
    if int(pa.count(2))==1 :
        SC.blit(tx2, (95+m, 115+m1))
    if int(pa.count(3))==1 :
        SC.blit(tx3, (25+m, 25+m1))
    if int(pa.count(4))==1 :
        SC.blit(tx4, (25+m, 25+m1))
    if int(pa.count(5))==1 :
        SC.blit(tx5, (25+m, 25+m1))
    if int(pa.count(6))==1 :
        SC.blit(tx6, (25+m, 25+m1))
    if int(pa.count(7))==1 :
        SC.blit(tx7, (25+m, 25+m1))
    if int(pa.count(8))==1 :
        SC.blit(tx8, (25+m, 25+m1))
    if int(pa.count(9))==1 :
        SC.blit(tx9, (275+m, 335+m1))
    pygame.display.update()
    CL.tick(1)
