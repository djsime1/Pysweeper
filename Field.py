"""Field file, can technically run
   standalone. Contains all (very
   messy) code that runs the game."""

import graphics as gr
import random as rand
import Menus
import time
from Hardcore import *

settings = [] #Replaced with game settings
colors = [gr.color_rgb(66,66,66),gr.color_rgb(41,121,255),gr.color_rgb(0,230,118),gr.color_rgb(244,67,54),gr.color_rgb(156,39,176),gr.color_rgb(197,17,98),gr.color_rgb(77,182,172),gr.color_rgb(0,0,0),gr.color_rgb(255,255,255)]
# ^ Stores colors of numbers on the minefield
tick = 0 #Used to display timer
status = 0 #0 = pre-game, 1 = in-game, 2 = post-game
rflags = 0 #Number of remaining flags

class Field(object): #Essentially a 2D table, stores Tile and Bomb objects.
    """2D Table to store Tile/Bomb objects."""
    def __init__(self,w,h):
        """Width and height."""
        self.w = h
        self.h = w
        self.t = [[0]*h for i in range(w)]

    def write(self,x,y,v=None): #Accepts 1D or 2D position
        """Writes to table, accepts 1D position and data or 2D position and data."""
        if v == None:
            v = y
            y = x%self.w
            x = x//self.w
        self.t[x][y] = v
    
    def read(self,x,y=None): #Accepts 1D or 2D position
        """Reads from table, accepts 1D position or 2D position and returns data."""
        if y == None:
            y = x%self.w
            x = x//self.w
        return self.t[x][y]

    def convert(self,x,y=None): #Converts between 1D and 2D coordinates
        """Converts 1D coordinates to 2D coordinates and vice-versa."""
        if y != None:
            return (x*self.w)+y
        else:
            return (x//self.w,x%self.w)

class Tile(object): #Basic tile object
    """Main tile object, contains functions used to run the game."""
    def __init__(self,x,y):
        """X and Y position on field."""
        self.x = x
        self.y = y
        self.flag = False #Has the tile been flagged?
        self.sweeped = False #Has the tile been revealed?
        self.gr = [] #Stores graphic elements, tile background and flag icon.
        self.gr.append(gr.Rectangle(gr.Point((40*x)+0,(40*y)+40),gr.Point((40*x)+39,(40*y)+79))) #Background tile
        self.gr[0].setFill(gr.color_rgb(33,33,33))
        self.gr[0].setOutline(gr.color_rgb(250,250,250))
        self.gr[0].setWidth(1)
        self.gr.append(gr.Image(gr.Point((40*x)+20,(40*y)+60),"img/Flag.png")) #Flag icon

    def getTotal(self,t,lw): #Gets total number of mines within surrounding 8 tiles, also reveals other blank tiles.
        """Returns number of surrounding bombs, as well as reveals surrounding blank tiles."""
        total = 0
        for i in (-1,0,1):
            if self.x+i != -1 and self.x+i != t.h:
                for x in (-1,0,1):
                    if self.y+x != -1 and self.y+x != t.w:
                        b = t.read(self.x+i,self.y+x)
                        if b.isBomb():
                            total += 1
        if total == 0:
            for i in (-1,0,1):
                if self.x+i != -1 and self.x+i != t.h:
                    for x in (-1,0,1):
                        if self.y+x != -1 and self.y+x != t.w:
                            b = t.read(self.x+i,self.y+x)
                            if not b.isBomb() and not b.sweeped:
                                b.sweep(t,lw).draw(lw)
        return total

    def sweep(self,t,lw): #Function that reveals the tile and displays number of surrounding mines.
        """Reveals if tile is safe or not, returns graphics object."""
        self.sweeped = True
        self.gr[0].setFill(gr.color_rgb(66,66,66))
        total = self.getTotal(t,lw)
        self.l = gr.Text(gr.Point((40*self.x)+20,(40*self.y)+60),str(total))
        self.l.setSize(20)
        self.l.setFill(colors[total])
        return self.l
        

    def isBomb(self): #It's a tile, not a mine.
        """Returns true if mine, false if not."""
        return False

class Bomb(Tile): #INHERITS FROM TILE OBJECT!! But this time, it's explosive.
    """Inherits from tile class, but this one goes boom!"""
    def sweep(self,t,lw): #Shows bomb icon
        """Reveals if tile is safe or not, returns graphics object."""
        self.sweeped = True
        self.gr[0].setFill(gr.color_rgb(66,66,66))
        self.l = gr.Image(gr.Point((40*self.x)+20,(40*self.y)+60),"img/Bomb.png")
        return self.l
        
    def isBomb(self): #Yes this one goes boom.
        """Returns true if mine, false if not."""
        return True

def inrange(pos,min,max=None): #Checks if point is within set of points/rectangle
    """Pos is point, min/max can be supplied OR a rectangle object"""
    if not max: #If object is provided, set min/max values automagically
        max = min.getP2()
        min = min.getP1()
    if (pos.x >= min.x and pos.x <= max.x) and (pos.y >= min.y and pos.y <= max.y):
        return True
    else:
        return False

def pConv(p): #Converts point to tile location
    """Convert point object to tile location on field."""
    x = p.getX()
    y = p.getY()
    y -= 40
    return (int(x//40),int(y//40))

def showField(): #Generates window and basic objects
    """Generates window and basic objects, returns window and object list."""
    if settings[3]: #Hardcore setting
        lw = gr.GraphWin("Pysweeper | HARDCORE Game",settings[0]*40,(settings[1]*40)+40,False)
    else:
        lw = gr.GraphWin("Pysweeper | Game",settings[0]*40,(settings[1]*40)+40,False)
    lw.setBackground(gr.color_rgb(33,33,33))
    li = []
    # 0: Top bar background
    # 1: Remaining flags
    # 2: Timer
    # 3: Reset icon

    li.append(gr.Rectangle(gr.Point(0, 0),gr.Point(lw.width, 40)))
    li[0].setWidth(0)
    li[0].setFill(gr.color_rgb(66,66,66))

    li.append(gr.Text(gr.Point(30,20),"000"))
    li[1].setSize(20)
    li[1].setFill(gr.color_rgb(250,250,250))

    li.append(gr.Text(gr.Point(lw.width-30,20),"000"))
    li[2].setSize(20)
    li[2].setFill(gr.color_rgb(250,250,250))

    li.append(gr.Image(gr.Point(lw.width/2, 20),"img/Reset.png"))
    li[1].setText((3-len(str(rflags)))*"0"+str(rflags))

    for i in li:
        i.draw(lw)

    lw.flush()
    return lw,li

def initialize(sett): #The thing that does all the things!
    """Parameter is list of settings (Width, Height, Mine count, and Hardcore mode.)"""
    global settings
    global tick
    global rflags
    global status
    settings = sett
    rflags = settings[2]
    lw,li = showField()
    tick = 0
    status = 0
    bombs = rand.sample(range(1,settings[0]*settings[1]), settings[2]) #Determines which tiles will contain bombs, Tile 0 is reserved.
    f = Field(settings[0],settings[1]) #Makes a field object of width and height according to settings.
    for i in range(settings[0]*settings[1]): #For all possible tiles,
        if i in bombs: #If the tile is within the bomb list,
            x = Bomb(f.convert(i)[0],f.convert(i)[1]) #Make it a mine,
        else: #Otherwise,
            x = Tile(f.convert(i)[0],f.convert(i)[1]) #Make it a regular tile.
        x.gr[0].draw(lw) #Draw background graphic.
        f.write(i,x) #Write to field object.

    while status != 4: #Never got this working properly, supposed to return to Launcher if game is closed.
        if not lw.isClosed() and status != 4: #Even a secondary check fails to work!
            lw.flush()
            mp = lw.getCurrentMouseLocation()
            ml = lw.checkMouse()
            mr = lw.checkMouseRight()

            time.sleep(1/60)
            if status == 1:
                tick += 1 #Count clock if game is in progress.
            li[2].setText((3-len(str(int(tick//60))))*"0"+str(int(tick//60))) #Update clock.

            if ml: #Stuff to do on left click.
                if mp.getY() > 40 and status != 2: #Makes sure you click within the minefield while game isn't over.
                    p = pConv(mp) #Get tile location,
                    t = f.read(p[0],p[1]) #Read the tile,
                    if status == 0: #If it's the first click,
                        status = 1 #Start the game/timer.
                        if t.isBomb(): #If first click is on a bomb,
                            f.read(0,0).gr[0].undraw() #Delete tile at position 0,0
                            t.gr[0].undraw() #Delete bomb at cursor position,
                            f.write(0,Bomb(0,0)) #Write a new bomb to position 0,0
                            f.read(0,0).gr[0].draw(lw) #Draw it's graphic,
                            t = Tile(p[0],p[1]) #Make a new regular tile at cursor position,
                            t.gr[0].draw(lw) #Draw it,
                            f.write(p[0],p[1],t) #Write it to field.
                    if not t.flag and not t.sweeped: #If tile is not flagged and not sweeped,
                        t.sweep(f,lw).draw(lw) #Reveal it.
                        if t.isBomb(): #If it explodes,
                            status = 2 #End game.
                            for i in range(settings[0]*settings[1]): #For each tile,
                                b = f.read(i) #Read it.
                                b.gr[0].setOutline(gr.color_rgb(244,67,54)) #Set outline to red (grid becomes red)
                                if not b.sweeped and b.isBomb(): #If it's a bomb that isn't already revealed,
                                    b.sweep(f,lw).draw(lw) #Reveal it.
                            if settings[3]: #If hardcore,
                                lw.flush() #Update the screen because we won't get any further.
                                time.sleep(2) #Let you realize your mistake for 2 seconds.
                                execute_order(66) #Hardcore.py
                        else: #If it's not a bomb,
                            win = True #Assume player has won, but check.
                            for i in range(settings[0]*settings[1]): #For each tile,
                                b = f.read(i) #Read it,
                                if not b.sweeped and not b.isBomb(): #If it's not a bomb and isn't revealed,
                                    win = False #You haven't won yet.
                            if win: #Once you have won,
                                status = 2 #End the game,
                                for i in range(settings[0]*settings[1]): #For each tile,
                                    b = f.read(i) #Read it.
                                    b.gr[0].setOutline(gr.color_rgb(0,230,118)) #Make outline green (grid becomes green)

                else: #If you click above the field.
                    if inrange(mp,gr.Point((lw.width/2)-20,0),gr.Point((lw.width/2)+20,40)): #If you click restart icon,
                        lw.close() #Close the game,
                        initialize(settings) #Go back to square one.
                
            if mr: #Stuff to do on right click.
                if mp.getY() > 40 and status != 2: #Makes sure you click within the minefield while game isn't over.
                    p = pConv(mp) #Get tile location,
                    t = f.read(p[0],p[1]) #Read the tile,
                    if not t.sweeped: #If it's not revealed,
                        if t.flag: #If it's flagged,
                            t.gr[1].undraw() #Hide the flag,
                            t.flag = False #Set as not flagged,
                            rflags += 1 #Add 1 to flag count,
                            li[1].setText((3-len(str(rflags)))*"0"+str(rflags)) #Update flag count.
                        elif rflags != 0: #Otherwise if you have any flags remaining,
                            t.gr[1].draw(lw) #Draw the flag
                            t.flag = True #Set as flagged,
                            rflags -= 1 #Subtract 1 from flag count,
                            li[1].setText((3-len(str(rflags)))*"0"+str(rflags)) #Update flag count.
                else: #If you click above the field.
                    if inrange(mp,gr.Point((lw.width/2)-20,0),gr.Point((lw.width/2)+20,40)): #If you right-click reset icon,
                        flags = False #Assume you're not clearing flags
                        for i in range(settings[0]*settings[1]): #For each tile,
                            t = f.read(i) #Read it.
                            if t.flag: #If its flagged,
                                flags = True #You're clearing flags.
                                rflags = settings[2] #Reset number of remaining flags to bomb count,
                                t.gr[1].undraw() #Hide the flag icon,
                                t.flag = False #Set as not flagged.
                        li[1].setText((3-len(str(rflags)))*"0"+str(rflags)) #Update flag count.
                        if not flags and not settings[3]: #If you're not clearing flags, (Intended for development purposes.)
                            status = 2 #End the game
                            for i in range(settings[0]*settings[1]): #For each tile,
                                t = f.read(i) #Read it,
                                if not t.sweeped: #If it's not revealed,
                                    t.sweep(f,lw).draw(lw) #Reveal it.
        else: #Supposed to run if you close the window, but it doesn't work.
            status = 4 #Set status to post-post-game
            lw.close() #Close the window that is already closed???
            lw,li = Menus.showLauncher() #Show launcher

if __name__ == "__main__": #Yoinked from graphics
    import Launcher #Run launcher if script is executed directly
    #initialize([8,8,4]) #I used this to quickly launch an easy version of the game.