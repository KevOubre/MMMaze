import gc
from CellObject import *
from PlayerObject import *
from Menu import Settings
import pygame
pygame.init()

rules = Settings()
infoObject = pygame.display.Info()
SWidth, SHeight = (rules["screenx"], rules["screeny"]) if rules["fullscreen"] == 0 else (infoObject.current_w, infoObject.current_h)
screen = pygame.display.set_mode((SWidth,SHeight)) if rules["fullscreen"] == 0 else  pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.FULLSCREEN)
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
WIDTH = rules["width"]
row,column = SWidth//WIDTH,SHeight//WIDTH



def prims(nap=0):
    cell = [[Cell(r,c,WIDTH,screen,row,column) for c in range(column)]for r in range(row)]
    step = random.choice(random.choice(cell))
    step.state = True
    step.drawz(white)
    stack = [step]
    visited = [step]
    counter = 0
    while counter <= len(cell):

        pygame.event.pump()
        previous = step
        time.sleep(nap)
        adjacent = step.neighbors(cell,step)
        possibleofnotvisited = [a for a in adjacent.keys() if not a.state]
        if len(possibleofnotvisited) >= 1:
            step = random.choice(possibleofnotvisited)
            step.state =True
            adjacent.get(step).drawz(white)
            visited.append(adjacent.get(step))
            visited.append(step)
            step.drawz(white)
            stack.append(step)
            counter = 0
        else:
            step = random.choice(stack)
            counter+=1
    print("done " + " prims")
    end = visited[-1]
    return visited,end


def rbacktracker(nap=0):
    cell = [[Cell(r,c,WIDTH,screen,row,column) for c in range(column)]for r in range(row)]
    step = random.choice(random.choice(cell))
    step.state = True
    step.drawz(white)
    stack = [step]
    visited = []
    while len(stack) >= 1:
        previous = step
        time.sleep(nap)
        adjacent = step.neighbors(cell,step)
        possibleofnotvisited = [a for a in adjacent.keys() if not a.state]
        if len(possibleofnotvisited) >= 1:
            step = random.choice(possibleofnotvisited)
            step.state = True
            adjacent.get(step).drawz(white)
            adjacent.get(step).state = True
            visited.append(adjacent.get(step))
            step.drawz(white)
            stack.append(step)
            visited.append(step)
        else:
            step = stack.pop()
    print("done " +" backtracker")
    end = visited[-1]
    return visited,end

def DrawText(text):
    screen.fill(black)
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render(text, 1, (255,255,0))
    screen.blit(label, (0,0))
    pygame.display.update()
    pygame.event.pump()
    pygame.time.wait(1500)


def Infinite():
    r = random.randint(0,2)
    maze = rbacktracker() if r == 0 else prims()
    active_cells = maze[0]
    end = maze[1]
    p = random.choice(active_cells)
    player = Player(p.row,p.column,p.width,screen)
    counter = 0
    start = time.time()
    timealloted = 100
    while True:
        gc.collect()
        for cells in active_cells:
            cells.drawz(white,mode=False)
        player.checkmove()
        end.drawz(blue)
        if player.row == end.row and player.column == end.column:
            print("time spent: " + str(time.time()-start))
            r = random.randint(0,1)
            player.drawmove()
            screen.fill(black)
            pygame.display.update()
            pygame.event.pump()
            DrawText("time spent: " + str(time.time()-start))
            pygame.display.update()
            counter += 1
            screen.fill(black)
            maze = rbacktracker() if r == 1 else prims()
            active_cells = maze[0]
            end = maze[1]
            p = random.choice(active_cells)
            player = Player(p.row,p.column,p.width,screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()



def ColorfulMaze(nap=0,counter=0,mode="b"):
    CHANGE = 1
    cell = [[Cell(r,c,WIDTH,screen,row,column) for c in range(column)]for r in range(row)]
    COLORS = [(i,0,0) for i in range(75,255)] + [(255-i,i,0) for i in range(0,255)] + [(0,i,0) for i in range(75,255)] + [(0,255-i,i) for i in range(0,255)] +  [(0,0,i) for i in range(75,255)]
    COLOR = COLORS[0]
    step = random.choice(random.choice(cell))
    step.state = True
    step.drawz(COLOR)
    stack = [step]
    visited = []
    while len(stack) >= 1:
        pygame.event.pump()
        previous = step
        time.sleep(nap)
        adjacent = step.neighbors(cell,step)
        possibleofnotvisited = [a for a in adjacent.keys() if not a.state]
        if len(possibleofnotvisited) >= 1:
            step = random.choice(possibleofnotvisited)
            step.state = True
            adjacent.get(step).drawz(COLOR)
            if (COLORS.index(COLOR) + CHANGE) < len(COLORS) and (COLORS.index(COLOR) + CHANGE) > 0:
                COLOR = COLORS[COLORS.index(COLOR) + CHANGE]
            else:
                CHANGE *= -1
                COLOR = COLORS[COLORS.index(COLOR) + CHANGE]
            adjacent.get(step).state = True
            visited.append(adjacent.get(step))
            step.drawz(COLOR)
            stack.append(step)
            visited.append(step)
        else:
            step = stack.pop()
            if (COLORS.index(COLOR) + CHANGE) < len(COLORS) and (COLORS.index(COLOR) + CHANGE) > 0:
                COLOR = COLORS[COLORS.index(COLOR) + CHANGE]
            else:
                CHANGE *= -1
                COLOR = COLORS[COLORS.index(COLOR) + CHANGE]
    print("done " +" backtracker")
    end = visited[-1]
    NewCell = [[1 if c.state else 0 for c in cel] for cel in cell]
    return NewCell

def ColorfulMaze2(nap=0,counter=0):
    CHANGE = 1
    cell = [[Cell(r,c,WIDTH,screen,row,column) for c in range(column)]for r in range(row)]
    COLORS = [(i,0,0) for i in range(75,255)] + [(255-i,i,0) for i in range(75,255)] + [(0,i,0) for i in range(75,255)] + [(0,255-i,i) for i in range(75,255)] +  [(0,0,i) for i in range(75,255)]
    COLOR = COLORS[0]
    step = random.choice(random.choice(cell))
    step.state = True
    step.drawz(COLOR)
    stack = [step]
    visited = []
    while counter < len(cell):
        previous = step
        time.sleep(nap)
        adjacent = step.neighbors(cell,step)
        possibleofnotvisited = [a for a in adjacent.keys() if not a.state]
        if len(possibleofnotvisited) >= 1:
            step = random.choice(possibleofnotvisited)
            step.state = True
            adjacent.get(step).drawz(COLOR)
            if (COLORS.index(COLOR) + CHANGE) < len(COLORS) and (COLORS.index(COLOR) + CHANGE) > 0:
                COLOR = COLORS[COLORS.index(COLOR) + CHANGE]
            else:
                CHANGE *= -1
                COLOR = COLORS[COLORS.index(COLOR) + CHANGE]
            adjacent.get(step).state = True
            visited.append(adjacent.get(step))
            step.drawz(COLOR)
            stack.append(step)
            visited.append(step)
            counter =0
        else:
            counter += 1
            step = random.choice(stack)
            if (COLORS.index(COLOR) + CHANGE) < len(COLORS) and (COLORS.index(COLOR) + CHANGE) > 0:
                COLOR = COLORS[COLORS.index(COLOR) + CHANGE]
            else:
                CHANGE *= -1
                COLOR = COLORS[COLORS.index(COLOR) + CHANGE]
    print("done " +" prims")
    end = visited[-1]
    return visited,end

def ColorfulMaze3(nap=0,counter=0):
    CHANGE = 2
    cell = [[Cell(r,c,WIDTH,screen,row,column) for c in range(column)]for r in range(row)]
    step = random.choice(random.choice(cell))
    step.state = True
    step.rainbowDraw(CHANGE)
    stack = [step]
    visited = []
    while len(stack) > 0:
        previous = step
        time.sleep(nap)
        adjacent = step.neighbors(cell,step)
        possibleofnotvisited = [a for a in adjacent.keys() if not a.state]
        if len(possibleofnotvisited) >= 1:
            step = random.choice(possibleofnotvisited)
            step.state = True
            if CHANGE <= 10 and CHANGE > 0:
                adjacent.get(step).rainbowDraw(CHANGE)
                adjacent.get(step).state = True
                visited.append(adjacent.get(step))
                step.rainbowDraw(CHANGE)
                CHANGE += 2
            else:
                CHANGE *= -1
                adjacent.get(step).rainbowDraw(CHANGE)
                adjacent.get(step).state = True
                visited.append(adjacent.get(step))
                step.rainbowDraw(CHANGE)
            stack.append(step)
            visited.append(step)
            counter =0
        else:
            counter += 1
            step = stack.pop()

    print("done " +" prims")
    end = visited[-1]
    return visited,end


def TwoPlayer():
    r = random.randint(0,2)
    maze = rbacktracker() if r == 0 else prims()
    active_cells = maze[0]
    end = maze[1]
    p = random.choice(active_cells)
    playerOne = Player(p.row,p.column,p.width,screen)

    p = random.choice(active_cells)
    playerTwo = Player(p.row,p.column,p.width,screen)
    counter = 0
    start = time.time()
    timealloted = 100
    while True:
        gc.collect()
        for cells in active_cells:
            cells.drawz(white,mode=False)
        playerOne.checkmove()
        playerTwo.checkmove(mode="none")
        end.drawz(blue)
        if playerOne.row == end.row and playerOne.column == end.column:
            print("time spent: " + str(time.time()-start))
            r = random.randint(0,1)
            playerOne.drawmove()
            screen.fill(black)
            pygame.display.update()
            pygame.event.pump()
            DrawText("time spent: " + str(time.time()-start))
            screen.fill(black)
            DrawText("player One WON" + str(time.time()-start))
            pygame.display.update()
            counter += 1
            screen.fill(black)

            maze = rbacktracker() if r == 1 else prims()

            active_cells = maze[0]
            end = maze[1]
            p = random.choice(active_cells)
            playerOne = Player(p.row,p.column,p.width,screen)

            p = random.choice(active_cells)
            playerTwo = Player(p.row,p.column,p.width,screen)
        if playerTwo.row == end.row and playerTwo.column == end.column:
            print("time spent: " + str(time.time()-start))
            r = random.randint(0,1)
            playerTwo.drawmove(mode="n")
            screen.fill(black)
            pygame.display.update()
            pygame.event.pump()
            DrawText("time spent: " + str(time.time()-start))
            screen.fill(black)
            DrawText("player Two WON" + str(time.time()-start))
            pygame.display.update()
            counter += 1
            screen.fill(black)

            maze = rbacktracker() if r == 1 else prims()

            active_cells = maze[0]
            end = maze[1]
            p = random.choice(active_cells)
            playerOne = Player(p.row,p.column,p.width,screen)

            p = random.choice(active_cells)
            playerTwo = Player(p.row,p.column,p.width,screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

if rules["function"] == 0:
    Infinite()

if rules["function"] == 1:
    prims()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

if rules["function"] == 2:
    rbacktracker()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


if rules["function"] == 3:
    ColorfulMaze()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


if rules["function"] == 4:
    ColorfulMaze2()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

if rules["function"] == 5:
    TwoPlayer()
