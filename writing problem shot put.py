# Python Class 2344
# Lesson 8 Problem 2
# Author: Phoenixcrusher (357011)

from tkinter import *
import random

class GUIDie(Canvas):
    '''6-sided Die class for GUI'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
        '''GUIDie(master,[valueList,colorList]) -> GUIDie
        creates a GUI 6-sided die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self,master,width=60,height=60,bg='white',\
                        bd=5,relief=GROOVE)
        # store the valuelist and colorlist
        self.valueList = valueList
        self.colorList = colorList
        # initialize the top value
        self.top = 1

    def get_top(self):
        '''GUIDie.get_top() -> int
        returns the value on the die'''
        return self.valueList[self.top-1]

    def roll(self):
        '''GUIDie.roll()
        rolls the die'''
        self.top = random.randrange(1,7)
        self.draw()

    def draw(self):
        '''GUIDie.draw()
        draws the pips on the die'''
        # clear old pips first
        self.erase()
        # location of which pips should be drawn
        pipList = [[(1,1)],
                   [(0,0),(2,2)],
                   [(0,0),(1,1),(2,2)],
                   [(0,0),(0,2),(2,0),(2,2)],
                   [(0,0),(0,2),(1,1),(2,0),(2,2)],
                   [(0,0),(0,2),(1,0),(1,2),(2,0),(2,2)]]
        for location in pipList[self.top-1]:
            self.draw_pip(location,self.colorList[self.top-1])

    def draw_pip(self,location,color):
        '''GUIDie.draw_pip(location,color)
        draws a pip at (row,col) given by location, with given color'''
        (centerx,centery) = (17+20*location[1],17+20*location[0])  # center
        self.create_oval(centerx-5,centery-5,centerx+5,centery+5,fill=color)

    def erase(self):
        '''GUIDie.erase()
        erases all the pips'''
        pipList = self.find_all()
        for pip in pipList:
            self.delete(pip)

class Decath400MFrame(Frame):
    '''frame for a game of 400 Meters'''

    def __init__(self,master,name):
        '''Decath400MFrame(master,name) -> Decath400MFrame
        creates a new 400 Meters frame
        name is the name of the player'''
        # set up Frame object
        Frame.__init__(self,master)
        self.grid()
        # label for player's name
        Label(self,text=name,font=('Arial',18)).grid(columnspan=3,sticky=W)
        # set up score and high score
        self.scoreLabel = Label(self,text='Attempts: 1 | Score: 0',font=('Arial',18))
        self.scoreLabel.grid(row=0,column=2,columnspan=3)
        self.highLabel = Label(self,text='Highscore: 0',font=('Arial',18))
        self.highLabel.grid(row=0,column=5,columnspan=3,sticky=E)
        # initialize game data
        self.score = 0
        self.attempt = 1
        self.gameround = 0
        self.highScore = 0
        # set up dice
        self.dice = []
        for n in range(8):
            self.dice.append(GUIDie(self,[1,2,3,4,5,6],['red']+['black']*5))
            self.dice[n].grid(row=1,column=n)
        # set up buttons
        self.rollButton = Button(self,text='Roll',command=self.roll)
        self.rollButton.grid(row=2,columnspan=2)
        self.stopButton = Button(self,text='Stop',state=ACTIVE,command=self.stop)
        self.stopButton.grid(row=3,columnspan=2)

    def roll(self):
        '''Decath400MFrame.roll()
        handler method for the roll button click'''
        # roll one die
        self.dice[self.gameround].roll()
        
        #foul ball
        if self.dice[self.gameround].get_top() ==1:
            self.score = 0
            self.rollButton['state'] = DISABLED
            self.stopButton['text'] = "Foul"
            self.stopButton['fg'] = 'red'
        else: #not foul
            self.score += self.dice[self.gameround].get_top() 
            self.gameround += 1
            self.scoreLabel['text'] = 'Attempts: '+ str(self.attempt) +' | ' +'Score: '+str(self.score)
            self.rollButton.grid(row=2,column=self.gameround,columnspan=1)
            self.stopButton.grid(row=3,column=self.gameround,columnspan=1)

        if self.gameround == 8:
            self.stop()
            
    def stop(self):
        #add 1 attempt
        self.attempt += 1
        #set new high score
        if self.score > self.highScore:
            self.highScore = self.score
            self.highLabel['text'] = "High Score: " + str(self.highScore)
            
        if self.attempt > 3:  # game over
            self.stopButton.grid_remove()
            self.rollButton.grid_remove()
            self.scoreLabel['text'] = 'Game over'
        else :
            #set score and gameround to 0
            self.score=0
            self.gameround =0                   
            # reset dice
            self.dice = []
            #get the dies
            for n in range(8):
                self.dice.append(GUIDie(self,[1,2,3,4,5,6],['red']+['black']*5))
                self.dice[n].grid(row=1,column=n)

            #sets the text back to stop and color to black. Also sets button labels.
            self.stopButton['text'] = "Stop"
            self.stopButton['fg'] = 'black'
            self.rollButton['state'] = ACTIVE
            self.scoreLabel['text']  = 'Attempts: '+ str(self.attempt) +' | ' +'Score: '+str(self.score)
            self.rollButton.grid(row=2,column=self.gameround,columnspan=1)
            self.stopButton.grid(row=3,column=self.gameround,columnspan=1)


       
        
        

# play the game
name = input("Enter your name: ")
root = Tk()
root.title('400 Meters')
game = Decath400MFrame(root,name)
game.mainloop()
