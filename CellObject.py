import pygame
import random
import time
import math

class Cell():
    state = False
    def __init__(self,row,column,width,s,r,co):
        self.row = row*width
        self.column = column*width
        self.width = width
        self.screen = s
        self.ROW = r
        self.COLUMN = co


    def drawz(self,col,mode=True):
        screen = self.screen
        pygame.draw.rect(screen,col,[self.row,self.column,self.width,self.width])
        if mode:
            pygame.display.update()

    def rainbowDraw(self,I,frequency= .3):
        RR = math.sin(frequency*I + 0) * 127 + 128
        #GG = math.sin(frequency*I + 0) * 127 + 128
        #BB = math.sin(frequency*I + 0) * 127 + 128
        pygame.draw.rect(self.screen,(RR,0,0),[self.row,self.column,self.width,self.width])
        pygame.display.update()

    def gen_cords(self,l,item):
        for i,rows in enumerate(l,0):
            for j,columns in enumerate(rows,0):
                try:
                    if item == columns:
                        return i,j
                except:
                    continue

    def neighbors(self,l,item):
        xindex = self.gen_cords(l,item)[0]
        yindex = self.gen_cords(l,item)[1]
        stack = {}
        if xindex > 1:
            stack.update({l[xindex-2][yindex]:l[xindex-1][yindex]})
        if xindex < self.ROW-2:
            stack.update({l[xindex+2][yindex]:l[xindex+1][yindex]})
        if yindex > 1:
            stack.update({l[xindex][yindex-2]:l[xindex][yindex-1]})
        if yindex < self.COLUMN-2:
            stack.update({l[xindex][yindex+2]:l[xindex][yindex+1]})
        return stack

    def drawCircle(self,col):
        screen = self.screen
        pygame.draw.ellipse(screen,col,[self.row,self.column,self.width+2,self.width+2])
        pygame.display.update()
