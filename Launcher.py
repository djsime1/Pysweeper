"""Launcher file; allows modification of settings, opens 
   info webpage, and most importantly, starts the game."""

import graphics as gr
import random as rand
import time
import Menus as ui
import Field as game
import webbrowser

def inrange(pos,min,max=None):
    """Pos is point, min/max can be supplied OR a rectangle object"""
    if not max: #If object is provided, set min/max values automagically
        max = min.getP2()
        min = min.getP1()
    if (pos.x >= min.x and pos.x <= max.x) and (pos.y >= min.y and pos.y <= max.y):
        return True
    else:
        return False

screen = 1 #1=Launcher, 2=Settings, 3=How to play, 4=Notice, 5=Something else
seenalt = 0 #Flag, set if user visits settings/how to play
settings = [8,8,10,False] #Width, Height, Number of mines, Hardcore mode
tmphc = None #Temp hardcore mode, for settings menu
lw,li = ui.showLauncher() #All the UI setup is in a separate file as to not clutter this file

while screen != 5: #Screen 5 = game
    if screen == 1: #Main launcher
        if not lw.isClosed():
            lw.flush()
            mp = lw.getCurrentMouseLocation()
            ml = lw.checkMouse()

            if inrange(mp,li[4]): #Start
                li[4].setOutline(gr.color_rgb(0,230,118))
                li[4].setWidth(4)
            else:
                li[4].setOutline(gr.color_rgb(66,66,66))
                li[4].setWidth(2)

            if inrange(mp,li[6]): #Settings
                li[6].setOutline(gr.color_rgb(255,234,0))
                li[6].setWidth(4)
            else:
                li[6].setOutline(gr.color_rgb(66,66,66))
                li[6].setWidth(2)

            if inrange(mp,li[8]): #How to play
                li[8].setOutline(gr.color_rgb(41,121,255))
                li[8].setWidth(4)
            else:
                li[8].setOutline(gr.color_rgb(66,66,66))
                li[8].setWidth(2)

            if ml:
                #print("Yee haw")
                if inrange(ml,li[4]): #Start
                    if not seenalt: #Notice message
                        seenalt = 1
                        screen = 4
                        lw.close()
                        lw,li = ui.showNotice()
                    else: #Start game
                        screen = 5
                        lw.close()
                        game.initialize(settings)

                elif inrange(ml,li[6]): #Settings
                    seenalt = 1
                    screen = 2
                    tmphc = settings[3]
                    lw.close()
                    lw,li = ui.showSettings(settings)

                elif inrange(ml,li[8]): #Info
                    seenalt = 1
                    #screen = 3
                    #lw.close()
                    #lw,li = ui.showInfo()
                    webbrowser.open("https://dj.je/pysweeper",0,True)
                    lw.close()
                    time.sleep(2)
                    lw,li = ui.showLauncher()
        else:
            exit() #Goodbye

    elif screen == 2: #Settings
        if not lw.isClosed():
            mp = lw.getCurrentMouseLocation()
            ml = lw.checkMouse()
            
            if inrange(mp,li[9]): #Save
                li[9].setOutline(gr.color_rgb(0,230,118))
                li[9].setWidth(4)
            else:
                li[9].setOutline(gr.color_rgb(66,66,66))
                li[9].setWidth(2)
            
            valid = True #Assume settings are valid, but preform checks
            for i in range(3): #Reset all borders
                li[5+i].setOutline(gr.color_rgb(66,66,66))
                li[5+i].setWidth(2)
            if not str.isdigit(li[18].getText()) or li[18].getText() == "0": #Width is non-zero number
                valid = False
                li[5].setOutline(gr.color_rgb(244,67,54))
                li[5].setWidth(4)
            if not str.isdigit(li[19].getText()) or li[19].getText() == "0": #Height is non-zero number
                valid = False
                li[6].setOutline(gr.color_rgb(244,67,54))
                li[6].setWidth(4)
            if li[18].getText() == "1" and li[19].getText() == "1": #Width and height are not 1 at the same time
                valid = False
                li[5].setOutline(gr.color_rgb(244,67,54))
                li[5].setWidth(4)
                li[6].setOutline(gr.color_rgb(244,67,54))
                li[6].setWidth(4)
            if not str.isdigit(li[20].getText()) or li[20].getText() == "0": #Number of mines is non-zero number
                valid = False
                li[7].setOutline(gr.color_rgb(244,67,54))
                li[7].setWidth(4)
            elif valid and int(li[20].getText()) > (int(li[18].getText())*int(li[19].getText()))-1: #Number of mines is between 1 and (W*H)-1
                valid = False
                li[7].setOutline(gr.color_rgb(244,67,54))
                li[7].setWidth(4)

            if ml:
                if inrange(mp,li[8]): #Hardcore
                    li[21].undraw()
                    tmphc = not tmphc
                    li[21] = gr.Image(gr.Point(400,362.5),"img/"+str(tmphc)+".png")
                    li[21].draw(lw)
                    if tmphc:
                        li[8].setOutline(gr.color_rgb(41,121,255))
                        li[8].setWidth(4)
                    else:
                        li[8].setOutline(gr.color_rgb(66,66,66))
                        li[8].setWidth(2)
                
                if inrange(mp,li[9]): #Save
                    if valid:
                        settings = [int(li[18].getText()),int(li[19].getText()),int(li[20].getText()),tmphc]
                        screen = 1
                        lw.close()
                        lw,li = ui.showLauncher()
        else:
            screen = 1
            lw.close()
            lw,li = ui.showLauncher()
    
    elif screen == 3: #Unused, was going to be info screen.
        if not lw.isClosed():
            mp = lw.getCurrentMouseLocation()
            ml = lw.checkMouse()
        else:
            screen = 1
            lw.close()
            lw,li = ui.showLauncher()

    elif screen == 4: #Notice message
        if not lw.isClosed():
            lw.flush()
            mp = lw.getCurrentMouseLocation()
            ml = lw.checkMouse()

            if inrange(mp,li[3]): #Back
                li[3].setOutline(gr.color_rgb(244,67,54))
                li[3].setWidth(4)
            else:
                li[3].setOutline(gr.color_rgb(66,66,66))
                li[3].setWidth(2)

            if inrange(mp,li[5]): #Continue
                li[5].setOutline(gr.color_rgb(0,230,118))
                li[5].setWidth(4)
            else:
                li[5].setOutline(gr.color_rgb(66,66,66))
                li[5].setWidth(2)

            if ml:
                if inrange(ml,li[3]):
                    screen = 1
                    lw.close()
                    lw,li = ui.showLauncher()
                elif inrange(ml,li[5]):
                    screen = 5
                    lw.close()
                    game.initialize(settings)
        else:
            screen = 1
            lw.close()
            lw,li = ui.showLauncher()