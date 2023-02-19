import pygame, sys
from pygame.locals import *

pygame.init()
SU = pygame.display.set_mode((300, 400))
CL = pygame.time.Clock()

BL=(0,0,0)
W=(255,255,255)
R=(255,0,0)
G=(0,255,0)
B=(0,0,255)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    SU.fill(W)
    for c in range(4):
        c=25+c*(250/3)
        pygame.draw.line(SU,BL,[c,25],[c,350])
    for co in range(4):
        co=25+co*((400-75)/3)
        pygame.draw.line(SU,BL,[25,co],[275,co])
    for ev in pygame.event.get():
        if ev.tipe.key == K_7:
            rec=Rect(50,50,100,100)
            pygame.drow.rect(SU,R,rec)
    pygame.display.update()
    CL.tick(1)
