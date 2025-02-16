import math,sys,numpy,pygame
from pygame.locals import KEYDOWN,MOUSEBUTTONDOWN,QUIT
pygame.init()
screen=pygame.display.set_mode((400, 300))
pygame.display.set_caption('A Dance of Fire and Ice 2')
clock=pygame.time.Clock()
k=0
fl=0
BPM=135
dir=1
FPS=60
tiles_ang=[0,0,0,0,math.pi/3,0,-math.pi/3,0]
while True:
    clock.tick(FPS)
    screen.fill("purple")
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN or event.type==MOUSEBUTTONDOWN:
            if k>tiles_ang[0]+math.pi/6*14:
                print("Very Late!")
            elif k>tiles_ang[0]+math.pi/6*12.75:
                print("LPerfect!")
                fl=0 if fl==1 else 1
                k-=math.pi+tiles_ang[0]
                tiles_ang.pop(0)
            elif k>tiles_ang[0]+math.pi/6*11.25:
                print("Perfect!")
                fl=0 if fl==1 else 1
                k-=math.pi+tiles_ang[0]
                tiles_ang.pop(0)
            elif k>tiles_ang[0]+math.pi/6*10:
                print("EPerfect!")
                fl=0 if fl==1 else 1
                k-=math.pi+tiles_ang[0]
                tiles_ang.pop(0)
            else:
                print("Very Early!")
    if k>tiles_ang[0]+math.pi/6*18:
        pygame.quit()
        sys.exit()
    px=182.5
    py=162.5
    ang=0
    for i in tiles_ang:
        pygame.draw.polygon(screen,(127,127,127),[(px,py),(px+17.5*numpy.cos(ang),py+17.5*numpy.sin(ang)),(px+17.5*numpy.cos(ang)+25*numpy.sin(ang),py+17.5*numpy.sin(ang)-25*numpy.cos(ang)),(px+25*numpy.sin(ang),py-25*numpy.cos(ang))])
        ang+=i
        pygame.draw.circle(screen,(127,127,127),(px+12.5*numpy.sin(ang-i)+17.5*numpy.cos(ang-i),py-12.5*numpy.cos(ang-i)+17.5*numpy.sin(ang-i)),12.5)
        px+=12.5*numpy.sin(ang-i)+17.5*numpy.cos(ang-i)-12.5*numpy.cos(math.pi/2-ang)
        py+=-12.5*numpy.cos(ang-i)+17.5*numpy.sin(ang-i)+12.5*numpy.sin(math.pi/2-ang)
        pygame.draw.polygon(screen,(127,127,127),[(px,py),(px+17.5*numpy.cos(ang),py+17.5*numpy.sin(ang)),(px+17.5*numpy.cos(ang)+25*numpy.sin(ang),py+17.5*numpy.sin(ang)-25*numpy.cos(ang)),(px+25*numpy.sin(ang),py-25*numpy.cos(ang))])
        px+=20*numpy.cos(ang)
        py+=20*numpy.sin(ang)
    if(fl==0):
        pygame.draw.circle(screen,"red",(200+40*numpy.cos(k*dir),150+40*numpy.sin(k*dir)),10)
        pygame.draw.circle(screen,"blue",(200,150),10)
        k+=math.pi/3600*BPM
    if(fl==1):
        pygame.draw.circle(screen,"blue",(200+40*numpy.cos(k*dir),150+40*numpy.sin(k*dir)),10)
        pygame.draw.circle(screen,"red",(200,150),10)
        k+=math.pi/3600*BPM
    pygame.display.update()