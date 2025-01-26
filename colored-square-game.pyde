import random
import sys

#Global variables
rounds=0
xsize=800
ysize=800
bluesquares=0
redsquares=0
redscore=0
bluescore=0
bluewin=False
tie=False
colours=[color(255, 51, 51), color(51, 51, 255)]

class squares(): 
    #Square class with its appropriate values
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.w=(12*xsize)/160
        self.h=(12*ysize)/160
        self.fillcolor=color(255)
    def setsqcolour(self, colour):
        self.fillcolor=colour
    def drawsquare(self):
        strokeWeight(2)
        stroke(224, 224, 224)
        fill(self.fillcolor)
        rect(self.x,self.y,self.w,self.h)
   
    
class rectangle():
    #Rectangle class that stores its appropriate properties
    def __init__(self,x, y, w, h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.fillcolor=color(255)
        self.weight = random.randint(1,4)
        self.checked = False
    def drawrect(self):
        strokeWeight(2)
        stroke(224, 224, 224)
        fill(self.fillcolor)
        rect(self.x,self.y,self.w,self.h)
        fill(0)
        if self in game.verticalbars:
            textSize(15)
            text(self.weight,self.x-10,self.y+(16*xsize)/320+5)
        if self in game.horizontalbars:
            textSize(15)
            text(self.weight,self.x+(16*xsize)/320, self.y-3)
        
    def setcolour(self, colour):
        self.fillcolor=colour
    

class dots():
    #dot class
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def drawdot(self):
        strokeWeight(1)
        stroke(76, 151, 0)
        fill(0, 255, 0)
        ellipse(self.x,self.y,(3*xsize)/140,(3*ysize)/140)
        
class Game():
    #Game class that containes the rectangles and squares
    def __init__(self):
        self.squares=[]
        self.rectangles=[]
        for j in range(40):
            self.rectangles.append(rectangle((4*xsize)/320, (3*ysize)/320, (16*xsize)/160, (3*ysize)/160))
        ycordcircles=xsize/4
        u=0
        while ysize/4 <= ycordcircles <= (ysize*3)/4:
            for i in range (xsize/4,(6*xsize)/8,xsize/8):
                rect1=rectangle(i+(4*xsize)/320, ycordcircles-(3*ysize)/320, (16*xsize)/160, (3*ysize)/160)
                rect1.index=u
                self.rectangles[u]=rect1
                u+=1
            u+=5
            ycordcircles+=ysize/8
        ycordcircles=xsize/4
        u=4
        while ysize/4 <= ycordcircles < (ysize*3)/4:
            for i in range (xsize/4,(7*xsize)/8,xsize/8):
                rect2=rectangle( i-(3*xsize)/320,ycordcircles+(4*ysize)/320, (3*ysize)/160, (16*xsize)/160)
                rect2.index=u
                self.rectangles[u]=rect2
                u+=1
            u+=4
            ycordcircles+=ysize/8
    
        self.horizontalbars=[self.rectangles[0], self.rectangles[1], self.rectangles[2], self.rectangles[3], self.rectangles[9], self.rectangles[10], self.rectangles[11], self.rectangles[12], self.rectangles[18], self.rectangles[19], self.rectangles[20], self.rectangles[21], self.rectangles[27], self.rectangles[28], self.rectangles[29], self.rectangles[30], self.rectangles[36], self.rectangles[37], self.rectangles[38], self.rectangles[39]] 
        self.verticalbars=[self.rectangles[4], self.rectangles[5], self.rectangles[6], self.rectangles[7], self.rectangles[8], self.rectangles[13], self.rectangles[14], self.rectangles[15], self.rectangles[16], self.rectangles[17], self.rectangles[22], self.rectangles[23], self.rectangles[24], self.rectangles[25], self.rectangles[26], self.rectangles[31], self.rectangles[32], self.rectangles[33], self.rectangles[34], self.rectangles[35]] 
    #Draw game function that runs whenever the game has not ended
    def drawgame(self):
        for i in range(len(self.rectangles)):
            self.rectangles[i].drawrect()
        ycordcircles=xsize/4
        while ysize/4 <= ycordcircles <= (ysize*3)/4:
            for i in range (xsize/4,(7*xsize)/8,xsize/8):
                dot1=dots(i, ycordcircles)
                dot1.drawdot()
            ycordcircles+=ysize/8
        textSize(25)
        fill(0)
        text("Blue Score: ",xsize-150,20)
        text(bluescore,xsize-30,20)
        textSize(25)
        fill(0)
        text("Red Score: ",xsize-150,50)
        text(redscore,xsize-30,50)
        for square in game.squares:
            square.drawsquare()
        
        
        
      
        
            
            
            
        
game=Game()    

def setup():
    size (xsize,ysize)
    background(255)

def draw():
    global gameover
    global tie
    if gameover:
        background(0)
        fill(255)
        textSize(40)
        text("Game Over!", xsize/2-100,ysize/2)
        if tie:
            text("Tie!", xsize/2-50,ysize/2+50)
        
        elif bluewin:
            text("Blue wins!", xsize/2-82,ysize/2+50)
        else:
            text("Red wins!", xsize/2-80,ysize/2+50)
    else:
        background(255)
        game.drawgame()
        
gameover=False

def keyPressed():
    global gameover
    if gameover:
        if key=='q' or key=='x' or key=='X' or key=='Q':
            exit()




def mouseClicked():
    global rounds
    global bluesquares
    global redsquares
    global bluescore
    global redscore
    global gameover
    global game
    global xsize
    global ysize
    global bluewin
    global colours
    global tie
    #restarting the game
    if gameover:
        rounds=0
        xsize=800
        ysize=800
        bluesquares=0
        redsquares=0
        redscore=0
        bluescore=0
        bluewin=False
        colours=[color(255, 51, 51), color(51, 51, 255)]
        game=Game()
        gameover=False
    #checking for clicks within rectangles and setting colors approratiely
    for i in game.rectangles:
        if (i.x<mouseX<i.x+i.w and i.y<mouseY<i.y+i.h):
            if i.fillcolor!=color(255, 51, 51) and i.fillcolor!=color(51, 51, 255):
                rounds+=1
                if rounds%2==0:
                    i.setcolour(colours[0])
                else:
                    i.setcolour(colours[1])
                
                current_index = i.index   
                
                #This segment of the code checks for the creation of a possible square whenever a turn is made. The code checks for 4 possible patterns that can form a square.
                #In case a square is form, the weights are calculated and added to the total score of the color
            
                #Pattern 1
                nocolor=0
                samecolor=0
                temporary_weight=0
                if 5<=current_index<=8 or 14<=current_index<=17 or 23<=current_index<=26 or  32<=current_index<=35:
                    # print(game.rectangles.index(game.rectangles[current_index+4]))
                    for e in [game.rectangles[current_index+4],game.rectangles[current_index-1],game.rectangles[current_index-5]]:
                        if e.fillcolor==i.fillcolor:
                            if e.checked==False:
                                temporary_weight+=e.weight
                            samecolor+=1
                        if e.fillcolor==color(255):
                            nocolor+=1
                    if 1<=samecolor and nocolor==0:
                        for u in [game.rectangles[current_index+4],game.rectangles[current_index-1],game.rectangles[current_index-5],game.rectangles[current_index]]:
                            u.checked=True
                        temporary_weight+=i.weight
                        sq1=squares(i.x-72, i.y+10)
                        sq1.setsqcolour(i.fillcolor)
                        sq1.drawsquare()
                        game.squares.append(sq1)
                        if sq1.fillcolor==color(255,51,51):
                            redscore+=temporary_weight
                            redsquares+=1
                        elif sq1.fillcolor==color(51, 51, 255):
                            bluescore+=temporary_weight
                            bluesquares+=1
                            
                
                #Pattern 2
                temporary_weight=0
                nocolor=0    
                samecolor=0
                if 4<=current_index<=7 or 13<=current_index<=16 or 22<=current_index<=25 or  31<=current_index<=34:
                    for t in [game.rectangles[current_index-4],game.rectangles[current_index+1],game.rectangles[current_index+5]]:
                        if t.fillcolor==i.fillcolor:
                            samecolor+=1
                            if t.checked==False:
                                temporary_weight+=t.weight
                        if t.fillcolor==color(255):
                            nocolor+=1
                    if 1<=samecolor and nocolor==0:
                        for u in [game.rectangles[current_index-4],game.rectangles[current_index+1],game.rectangles[current_index+5],game.rectangles[current_index]]:
                            u.checked=True
                        temporary_weight+=i.weight
                        sq1=squares(i.x+27, i.y+10)
                        sq1.setsqcolour(i.fillcolor)
                        sq1.drawsquare()
                        game.squares.append(sq1)
                        if sq1.fillcolor==color(255,51,51):
                            redscore+=temporary_weight
                            redsquares+=1
                        elif sq1.fillcolor==color(51, 51, 255):
                            bluescore+=temporary_weight
                            bluesquares+=1
                
                #Pattern 3
                temporary_weight=0
                nocolor=0    
                samecolor=0
                
                if current_index%9==0 or (current_index-1)%9==0 or (current_index-2)%9==0 or (current_index-3)%9==0:
                    for t in [game.rectangles[current_index-4],game.rectangles[current_index-5],game.rectangles[current_index-9]]:
                        if t.fillcolor==i.fillcolor:
                            if t.checked==False:
                                temporary_weight+=t.weight
                            samecolor+=1
                        if t.fillcolor==color(255):
                            nocolor+=1
                    if 1<=samecolor and nocolor==0:
                        for u in [game.rectangles[current_index-4],game.rectangles[current_index-5],game.rectangles[current_index-9],game.rectangles[current_index]]:
                            u.checked=True
                        temporary_weight+=i.weight
                        sq1=squares(i.x+10, i.y-73)
                        sq1.setsqcolour(i.fillcolor)
                        sq1.drawsquare()
                        game.squares.append(sq1)
                        if sq1.fillcolor==color(255,51,51):
                            redscore+=temporary_weight
                            redsquares+=1
                        elif sq1.fillcolor==color(51, 51, 255):
                            bluescore+=temporary_weight
                            bluesquares+=1
                #Pattern 4
                temporary_weight=0
                nocolor=0    
                samecolor=0
                if (current_index%9==0 and current_index!=36) or ((current_index-1)%9==0 and current_index!=37) or ((current_index-2)%9==0 and current_index!=38) or ((current_index-3)%9==0 and current_index!=39) or 0<=current_index<=3:
                    for t in [game.rectangles[current_index+4],game.rectangles[current_index+5],game.rectangles[current_index+9]]:
                        if t.fillcolor==i.fillcolor:
                            if t.checked==False:
                                temporary_weight+=t.weight
                            samecolor+=1
                        if t.fillcolor==color(255):
                            nocolor+=1
            
                    if 1<=samecolor and nocolor==0:
                        for u in [game.rectangles[current_index+4],game.rectangles[current_index+5],game.rectangles[current_index+9],game.rectangles[current_index]]:
                            u.checked=True
                        temporary_weight+=i.weight
                        sq1=squares(i.x+10, i.y+27)
                        sq1.setsqcolour(i.fillcolor)
                        sq1.drawsquare()
                        game.squares.append(sq1)
                        if sq1.fillcolor==color(255,51,51):
                            redscore+=temporary_weight
                            redsquares+=1
                        elif sq1.fillcolor==color(51, 51, 255):
                            bluescore+=temporary_weight
                            bluesquares+=1
                print("blue: ",bluescore)
                print("red: ",redscore)
                
                # Game end check when rounds hit 40, it checks for scores and appropriately sets booleans for game end screen in the draw function
                if rounds==40:
                    if bluescore>redscore:
                        gameover=True
                        print("BLUE WINSS")
                        bluewin=True
                    elif redscore>bluescore:
                        gameover=True
                        print("RED WINSS")
                        bluewin=False
                    elif bluescore==redscore:
                        print("Draw")
                        tie=True
                        gameover=True
    

        
    
    
    
