import pygame
import random
import gc


pygame.init()

infoObject = pygame.display.Info()
#screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.FULLSCREEN)
#,pygame.FULLSCREEN
SWidth, SHeight = (500, 500)
screen = pygame.display.set_mode((SWidth,SHeight))
#screen = pygame.display.set_mode((666,666))
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
WIDTH = 10
row,column = SWidth//WIDTH,SHeight//WIDTH

class Ship():

    def __init__(self,xcord,ycord,size):
        self.xcord = xcord * size
        self.ycord = ycord * size
        self.xspeed = random.randint(-10,10)
        self.yspeed = random.randint(-10,10)
        self.roundofplay = 0
        self.probability = 50
        self.stackx = []
        self.stacky = []

    def edges(self):
        if self.ycord >= SHeight or self.ycord <= 0:
            self.yspeed *= -1
            self.yspeed += random.randint(-2,2)
        if self.xcord >= SHeight or self.xcord <= 0:
            self.xspeed *= -1
            self.xspeed += random.randint(-2,2)
        self.ycord += self.yspeed
        self.xcord += self.xspeed

    def bounce(self):
        self.yspeed *= -random.randint(1,10)
        self.xspeed *= -random.randint(1,10)

    def updateme(self):
        pygame.draw.ellipse(screen,white,[self.xcord,self.ycord,10,10])


    def drawtails(self):
        prevx,prevy = self.stackx[-1],self.stacky[-1]
        for x,y in zip(self.stackx,self.stacky):
            pygame.draw.line(screen,white,(x,y),(prevx,prevy))
            prevx,prevy = x,y
        pygame.display.update()

    def AI(self,numofruns):
        for i in range(numofruns):
            self.stackx.append(self.xcord)
            self.stacky.append(self.ycord)
            screen.fill(black)
            #pygame.time.wait(50)
            rone = random.randint(0,self.probability)
            rtwo = random.randint(0,self.probability)
            if rone == rtwo:
                self.edges()
                self.bounce()
                self.drawtails()
                self.updateme()
                pygame.display.update()
            else:
                self.edges()
                self.updateme()
                self.drawtails()

                pygame.display.update()
        return self.xcord,self.ycord

    def Usered(self,numofruns):
        for i in range(numofruns):
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.bounce()
            else:
                pass



shipCPU = Ship(10,10,10)

while True:
    shipCPU.AI(99999999)
