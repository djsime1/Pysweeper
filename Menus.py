"""Menus file, contains code to create all 
   windows excluding the actual game window.
   All graphics objects are stored in a list."""

import graphics as gr
import random as rand
import time

def showLauncher():
    """Displays the launcher, returns window and object list."""
    lw = gr.GraphWin("Pysweeper | Launcher",300,400,False)
    lw.setBackground(gr.color_rgb(33,33,33))
    li = []
    # 0: Top bar background
    # 1: Title BG
    # 2: Title FG
    # 3: Author name
    # 4: Start BG
    # 5: Start text
    # 6: Settings BG
    # 7: Settings text
    # 8: About BG
    # 9: About text

    li.append(gr.Rectangle(gr.Point(0, 0),gr.Point(300, 100)))
    li[0].setWidth(0)
    li[0].setFill(gr.color_rgb(66,66,66))
    li.append(gr.Text(gr.Point(150,33),"PYSWEEPER"))
    li[1].setSize(26)
    li[1].setStyle("bold")
    li[1].setFill(gr.color_rgb(244,67,54))
    li.append(gr.Text(gr.Point(150,33),"PYSWEEPER"))
    li[2].setSize(25)
    li[2].setStyle("bold")
    li[2].setFill(gr.color_rgb(250,250,250))
    li.append(gr.Text(gr.Point(150,66),"By David S."))
    li[3].setSize(20)
    li[3].setFill(gr.color_rgb(250,250,250))

    li.append(gr.RoundedRectangle(gr.Point(50,125),gr.Point(250,175),25))
    li[4].setFill(gr.color_rgb(33,33,33))
    li[4].setOutline(gr.color_rgb(66,66,66))
    li.append(gr.Text(gr.Point(150,150),"Start"))
    li[5].setSize(25)
    li[5].setFill(gr.color_rgb(250,250,250))
    li[5].setStyle("bold")

    li.append(gr.RoundedRectangle(gr.Point(50,225),gr.Point(250,275),25))
    li[6].setFill(gr.color_rgb(33,33,33))
    li[6].setOutline(gr.color_rgb(66,66,66))
    li.append(gr.Text(gr.Point(150,250),"Settings"))
    li[7].setSize(25)
    li[7].setFill(gr.color_rgb(250,250,250))

    li.append(gr.RoundedRectangle(gr.Point(50,325),gr.Point(250,375),25))
    li[8].setFill(gr.color_rgb(33,33,33))
    li[8].setOutline(gr.color_rgb(66,66,66))
    li.append(gr.Text(gr.Point(150,350),"Info/Guide"))
    li[9].setSize(25)
    li[9].setFill(gr.color_rgb(250,250,250))

    for i in li:
        i.draw(lw)

    lw.flush()
    return lw,li

def showSettings(s):
    """Displays the settings menu, returns window and object list."""
    lw = gr.GraphWin("Pysweeper | Settings",600,425,False)
    lw.setBackground(gr.color_rgb(33,33,33))
    li = []
    # 0: Top bar background
    # 1: Title BG
    # 2: Title FG
    # 3: Author name
    # 4: Window name

    li.append(gr.Rectangle(gr.Point(0, 0),gr.Point(600, 100)))
    li[0].setWidth(0)
    li[0].setFill(gr.color_rgb(66,66,66))
    li.append(gr.Text(gr.Point(150,33),"PYSWEEPER"))
    li[1].setSize(26)
    li[1].setStyle("bold")
    li[1].setFill(gr.color_rgb(244,67,54))
    li.append(gr.Text(gr.Point(150,33),"PYSWEEPER"))
    li[2].setSize(25)
    li[2].setStyle("bold")
    li[2].setFill(gr.color_rgb(250,250,250))
    li.append(gr.Text(gr.Point(150,66),"By David S."))
    li[3].setSize(20)
    li[3].setFill(gr.color_rgb(250,250,250))
    li.append(gr.Text(gr.Point(450,50),"Settings"))
    li[4].setSize(30)
    li[4].setFill(gr.color_rgb(250,250,250))
    li[4].setStyle("italic")

    li.append(gr.RoundedRectangle(gr.Point(25,125),gr.Point(287.5,200),25))
    li[5].setFill(gr.color_rgb(33,33,33))
    li[5].setOutline(gr.color_rgb(66,66,66))
    li[5].setWidth(2)

    li.append(gr.RoundedRectangle(gr.Point(312.5,125),gr.Point(575,200),25))
    li[6].setFill(gr.color_rgb(33,33,33))
    li[6].setOutline(gr.color_rgb(66,66,66))
    li[6].setWidth(2)

    li.append(gr.RoundedRectangle(gr.Point(25,225),gr.Point(475,300),25))
    li[7].setFill(gr.color_rgb(33,33,33))
    li[7].setOutline(gr.color_rgb(66,66,66))
    li[7].setWidth(2)

    li.append(gr.RoundedRectangle(gr.Point(25,325),gr.Point(475,400),25))
    li[8].setFill(gr.color_rgb(33,33,33))
    li[8].setWidth(2)
    if s[3]:
        li[8].setOutline(gr.color_rgb(41,121,255))
        li[8].setWidth(4)
    else:
        li[8].setOutline(gr.color_rgb(66,66,66))
        li[8].setWidth(2)

    li.append(gr.RoundedRectangle(gr.Point(500,225),gr.Point(575,400),25))
    li[9].setFill(gr.color_rgb(33,33,33))
    li[9].setOutline(gr.color_rgb(66,66,66))
    li[9].setWidth(2)

    li.append(gr.Text(gr.Point(75,162.5),"Width"))
    li[10].setSize(20)
    li[10].setFill(gr.color_rgb(250,250,250))

    li.append(gr.Text(gr.Point(362.5,162.5),"Height"))
    li[11].setSize(20)
    li[11].setFill(gr.color_rgb(250,250,250))

    li.append(gr.Text(gr.Point(150,262.5),"Number of mines"))
    li[12].setSize(20)
    li[12].setFill(gr.color_rgb(250,250,250))

    li.append(gr.Text(gr.Point(150,362.5),"Hardcore mode"))
    li[13].setSize(20)
    li[13].setFill(gr.color_rgb(250,250,250))

    li.append(gr.Text(gr.Point(537.5,225+(1*(175/5))),"S"))
    li[14].setSize(25)
    li[14].setFill(gr.color_rgb(250,250,250))
    li[14].setStyle("bold")

    li.append(gr.Text(gr.Point(537.5,225+(2*(175/5))),"A"))
    li[15].setSize(25)
    li[15].setFill(gr.color_rgb(250,250,250))
    li[15].setStyle("bold")

    li.append(gr.Text(gr.Point(537.5,225+(3*(175/5))),"V"))
    li[16].setSize(25)
    li[16].setFill(gr.color_rgb(250,250,250))
    li[16].setStyle("bold")

    li.append(gr.Text(gr.Point(537.5,225+(4*(175/5))),"E"))
    li[17].setSize(25)
    li[17].setFill(gr.color_rgb(250,250,250))
    li[17].setStyle("bold")

    li.append(gr.Entry(gr.Point(212.5,162.5),6))
    li[18].setSize(15)
    li[18].setFill(gr.color_rgb(250,250,250))
    li[18].setText(str(s[0]))

    li.append(gr.Entry(gr.Point(500,162.5),6))
    li[19].setSize(15)
    li[19].setFill(gr.color_rgb(250,250,250))
    li[19].setText(str(s[1]))

    li.append(gr.Entry(gr.Point(400,262.5),6))
    li[20].setSize(15)
    li[20].setFill(gr.color_rgb(250,250,250))
    li[20].setText(str(s[2]))

    li.append(gr.Image(gr.Point(400,362.5),"img/"+str(s[3])+".png"))

    for i in li:
        i.draw(lw)

    lw.flush()
    return lw,li

def showInfo(): #Replaced with webpage
    """! OBSOLETE ! Displays the info page, returns window and object list."""
    """
    lw = gr.GraphWin("Pysweeper | How to play",600,400,False)
    lw.setBackground(gr.color_rgb(33,33,33))
    li = []
    # 0: Top bar background
    # 1: Title BG
    # 2: Title FG
    # 3: Author name
    # 4: Window name

    li.append(gr.Rectangle(gr.Point(0, 0),gr.Point(600, 100)))
    li[0].setWidth(0)
    li[0].setFill(gr.color_rgb(66,66,66))
    li.append(gr.Text(gr.Point(150,33),"PYSWEEPER"))
    li[1].setSize(26)
    li[1].setStyle("bold")
    li[1].setFill(gr.color_rgb(244,67,54))
    li.append(gr.Text(gr.Point(150,33),"PYSWEEPER"))
    li[2].setSize(25)
    li[2].setStyle("bold")
    li[2].setFill(gr.color_rgb(250,250,250))
    li.append(gr.Text(gr.Point(150,66),"By David S."))
    li[3].setSize(20)
    li[3].setFill(gr.color_rgb(250,250,250))
    li.append(gr.Text(gr.Point(450,50),"How to play"))
    li[4].setSize(30)
    li[4].setFill(gr.color_rgb(250,250,250))
    li[4].setStyle("italic")

    for i in li:
        i.draw(lw)

    lw.flush()
    return lw,li
    """
    #Moved to webpage

def showNotice():
    """Displays the notice box, returns window and object list."""
    lw = gr.GraphWin("Pysweeper | Notice",400,200,False)
    lw.setBackground(gr.color_rgb(33,33,33))
    li = []
    # 0: Line 1
    # 1: Line 2
    # 2: Line 3
    # 3: Back BG
    # 4: Back Text
    # 5: Continue BG
    # 6: Continue Text

    li.append(gr.Text(gr.Point(200,25),"Are you sure you want to start"))
    li[0].setSize(20)
    li[0].setFill(gr.color_rgb(250,250,250))
    li.append(gr.Text(gr.Point(200,50),"without checking the settings"))
    li[1].setSize(20)
    li[1].setFill(gr.color_rgb(250,250,250))
    li.append(gr.Text(gr.Point(200,75),"or reading the guide?"))
    li[2].setSize(20)
    li[2].setFill(gr.color_rgb(250,250,250))

    li.append(gr.RoundedRectangle(gr.Point(25,125),gr.Point(175,175),25))
    li[3].setFill(gr.color_rgb(33,33,33))
    li[3].setOutline(gr.color_rgb(66,66,66))
    li.append(gr.Text(gr.Point(100,150),"Back"))
    li[4].setSize(25)
    li[4].setFill(gr.color_rgb(250,250,250))

    li.append(gr.RoundedRectangle(gr.Point(225,125),gr.Point(375,175),25))
    li[5].setFill(gr.color_rgb(33,33,33))
    li[5].setOutline(gr.color_rgb(66,66,66))
    li.append(gr.Text(gr.Point(300,150),"Continue"))
    li[6].setSize(25)
    li[6].setFill(gr.color_rgb(250,250,250))

    for i in li:
        i.draw(lw)

    lw.flush()
    return lw,li

if __name__ == "__main__": #Yoinked from graphics
    import Launcher #Run launcher if script is executed directly