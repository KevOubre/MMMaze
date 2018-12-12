import random
import time
import pygame

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)

class Player():
    stack = []
    Size = 0
    def __init__(self,row,column,width,s):
        self.row = row
        self.column = column
        self.width = width
        self.speed = width
        self.screen = s

    def isvalid(self,offsetx=0,offsety=0):
        screen = self.screen
        try:
            return True if sum(screen.get_at((self.row+offsetx,self.column+offsety))) > 256 else False
        except:
            pass

    def checkmove(self,mode="p1"):
        if mode == 'p1':
            screen = self.screen
            key = pygame.key.get_pressed()
            dist = self.speed
            if key[pygame.K_DOWN] and self.isvalid(offsety=dist): # down key
                self.column += dist # move down
                time.sleep(.05)
            if key[pygame.K_UP] and self.isvalid(offsety=-dist): # up key
                self.column -= dist # move up
                time.sleep(.05)
            if key[pygame.K_RIGHT] and self.isvalid(offsetx=dist): # right key
                self.row += dist # move right
                time.sleep(.05)
            if key[pygame.K_LEFT] and self.isvalid(offsetx=-dist): # left key
                self.row -= dist # move left
                time.sleep(.05)


            pygame.draw.rect(screen,red,[self.row,self.column,self.width,self.width])
            self.stack.append((self.row,self.column))

        else:
            screen = self.screen
            key = pygame.key.get_pressed()
            dist = self.speed
            if key[pygame.K_s] and self.isvalid(offsety=dist): # down key
                self.column += dist # move down
                time.sleep(.05)
            if key[pygame.K_w] and self.isvalid(offsety=-dist): # up key
                self.column -= dist # move up
                time.sleep(.05)
            if key[pygame.K_d] and self.isvalid(offsetx=dist): # right key
                self.row += dist # move right
                time.sleep(.05)
            if key[pygame.K_a] and self.isvalid(offsetx=-dist): # left key
                self.row -= dist # move left
                time.sleep(.05)


            pygame.draw.rect(screen,(0,255,0),[self.row,self.column,self.width,self.width])
            self.stack.append((self.row,self.column))

    def drawmove(self,mode=True):

        for s in self.stack:
            xx = s[0]
            yy = s[1]
            pygame.draw.rect(self.screen,red if mode else (0,255,0),[xx,yy,self.width,self.width])
            pygame.display.update()
            pygame.time.wait(10)

        for s in reversed(self.stack):
            xx = s[0]
            yy = s[1]
            pygame.draw.rect(self.screen,white,[xx,yy,self.width,self.width])
            pygame.display.update()

        for s in self.stack:
            xx = s[0]
            yy = s[1]
            pygame.draw.rect(self.screen,red if mode else (0,255,0),[xx,yy,self.width,self.width])
            pygame.display.update()
            pygame.time.wait(0)
            
        self.Size = len(self.stack)
        self.stack.clear()
        pygame.event.pump()
        pygame.time.wait(1000)


    def AIneighbors(self,MWidth,Mheight,xc,yc):
        stackx = []
        stacky = []
        dist = self.speed
        if xc > 0 and self.isvalid(offsetx=-dist):
            #stack.update({l[self.row-2][self.column]:l[self.row-1][self.column]})

            stackx.append(self.row-dist)
            stacky.append(self.column)
        if xc < MWidth -10 and self.isvalid(offsetx=dist):
            #stack.update({l[self.row+2][self.column]:l[self.row+1][self.column]})


            stackx.append(self.row+dist)
            stacky.append(self.column)
        if yc > 0 and self.isvalid(offsety=-dist):
            #stack.update({l[self.row][self.column-2]:l[self.row][self.column-1]})


            stackx.append(self.row)
            stacky.append(self.column-dist)
        if yc < Mheight - 10 and self.isvalid(offsety=dist):
            #stack.update({l[self.row][self.column+2]:l[self.row][self.column+1]})

            stackx.append(self.row)
            stacky.append(self.column+dist)
        stack = list(zip(stackx,stacky))

        return stack

    def backtracking(self,MW,MH,goal):
        xcord = self.row
        ycord = self.column
        pygame.draw.rect(self.screen,red,[xcord,ycord,self.width,self.width])
        pygame.display.update()
        stack = [(xcord,ycord)]
        visited = [(xcord,ycord)]
        cords = (xcord,ycord)
        while len(stack) >= 1:
            #time.sleep(.5)
            pygame.display.update()
            adjacent = self.AIneighbors(MW,MH,cords[0],cords[1])
            if self.row == goal[0] and self.column == goal[1]:
                break
            if len(adjacent) >= 1:
                cords = adjacent[0]
                print(cords)
                xcord = cords[0]
                ycord = cords[1]
                pygame.draw.rect(self.screen,red,[xcord,ycord,self.width,self.width])
                pygame.display.update()
                stack.append(cords)
                visited.append(cords)
            else:
                cords = stack.pop()

    def shadows(self):
        s = pygame.Surface((500, 500))

        # first, "erase" the surface by filling it with a color and
        # setting this color as colorkey, so the surface is empty
        s.fill(white)
        s.set_colorkey(white)

        pygame.draw.circle(s, (255, 0, 0), (25, 25), 25, 2)

        # after drawing the circle, we can set the
        # alpha value (transparency) of the surface
        s.set_alpha(10)

        x, y = pygame.mouse.get_pos()
        self.screen.blit(s, (self.row-15,self.column-15))

