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
pa=['0']
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
                if int(pa.count('1'))!=1:
                    if p==0:
                        p1+=[1]
                        tx1=font.render("1", True, (0, 0, 0))
                    else :
                        p2+=[1]
                        tx1=font.render("2", True, (0, 0, 0))
                    pa+=['1']
                    
            if 120<x<190 and 30<y<120 and int(pa.count('2'))!=1:
                if p==0:
                    p1+=[2]
                    tx2=font.render("1", True, (0, 0, 0))
                else :
                    p2+=[2]
                    tx2=font.render("2", True, (0, 0, 0))
                pa+=['2']
                
            if 210<x<280 and 30<y<120 and int(pa.count('3'))!=1:
                if p==0:
                    p1+=[3]
                    tx3=font.render("1", True, (0, 0, 0))
                else :
                    p2+=[3]
                    tx3=font.render("2", True, (0, 0, 0))
                pa+=['3']
                
            if 30<x<100 and 140<y<230 and int(pa.count('4'))!=1:
                if p==0:
                    p1+=[4]
                    tx4=font.render("1", True, (0, 0, 0))
                else :
                    p2+=[4]
                    tx4=font.render("2", True, (0, 0, 0))
                pa+=['4']
                
            if 120<x<190 and 140<y<230 and int(pa.count('5'))!=1:
                if p==0:
                    p1+=[5]
                    tx5=font.render("1", True, (0, 0, 0))
                else :
                    p2+=[5]
                    tx5=font.render("2", True, (0, 0, 0))
                pa+=['5']
                
            if 210<x<280 and 140<y<230 and int(pa.count('6'))!=1:
                if p==0:
                    p1+=[6]
                    tx6=font.render("1", True, (0, 0, 0))
                else :
                    p2+=[6]
                    tx6=font.render("2", True, (0, 0, 0))
                pa+=['6']
                
            if 30<x<100 and 250<y<340 and int(pa.count('7'))!=1:
                if p==0:
                    p1+=[7]
                    tx7=font.render("1", True, (0, 0, 0))
                else  :
                    p2+=[7]
                    tx7=font.render("2", True, (0, 0, 0))
                pa+=['7']
                
            if 120<x<190 and 250<y<340 and int(pa.count('8'))!=1:
                if p==0:
                    p1+=[8]
                    tx8=font.render("1", True, (0, 0, 0))
                else  :
                    p2+=[8]
                    tx8=font.render("2", True, (0, 0, 0))
                pa+=['8']
                
            if 210<x<280 and 250<y<340 and int(pa.count('9'))!=1:
                if p==0:
                    p1+=[9]
                    tx9=font.render("1", True, (0, 0, 0))
                else :
                    p2+=[9]
                    tx9=font.render("2", True, (0, 0, 0))
                pa+=['9']
                
            if len(p1)>len(p2) :
                p=1
                print(pa)
            else :
                p=0
        if event.type == MOUSEBUTTONDOWN:
            if event.button and 9<len(pa):
                asd=font.render("It did not the match ends", True, (0, 0, 0))
                SC.blit('asd', (0, 0))
    if int(pa.count('1'))==1 :
        SC.blit(tx1, (20+m, 20+m1))
    if int(pa.count('2'))==1 :
        SC.blit(tx2, (110+m, 20+m1))
    if int(pa.count('3'))==1 :
        SC.blit(tx3, (200+m, 20+m1))
    if int(pa.count('4'))==1 :
        SC.blit(tx4, (20+m, 130+m1))
    if int(pa.count('5'))==1 :
        SC.blit(tx5, (110+m, 130+m1))
    if int(pa.count('6'))==1 :
        SC.blit(tx6, (200+m, 130+m1))
    if int(pa.count('7'))==1 :
        SC.blit(tx7, (20+m, 240+m1))
    if int(pa.count('8'))==1 :
        SC.blit(tx8, (110+m, 240+m1))
    if int(pa.count('9'))==1 :
        SC.blit(tx9, (200+m, 240+m1))

    pygame.display.update()
    CL.tick(0.5)

