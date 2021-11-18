# Python Class 2344
# Lesson 7 Problem 5 Part (b)
# Author: Phoenixcrusher (357011)

import turtle
from tkinter import *
class SuperAwesomeTurtle(turtle.Turtle):
    '''a super awesome turtle!'''
    def __init__(self):
        '''init(self) -> initalizes the keys to the function
        and sets speed to 0'''
        turtle.Turtle.__init__(self)
        
        #initalize speed
        self.speed = 0
        
        #set the keys to the functions
        self.getscreen().onkey(self.stop_moving, "s")
        self.getscreen().onkey(self.quit, "q")
        self.getscreen().onkey(self.go_faster, "Up")
        self.getscreen().onkey(self.go_slower, "Down")
        self.getscreen().onkey(self.go_left, "Left")
        self.getscreen().onkey(self.go_right, "Right")
        
        #calls go forward to make it go forward by a continuous amount
        self.go_forward()

    def stop_moving(self):
        '''stop_moving(self) -> makes the turtle stop moving'''
        self.speed = 0
    def quit(self):
        '''quit(self) -> deletes the tab and exits the program'''
        self.getscreen().bye()
    def go_faster(self):
        '''go_faster(self) -> makes the speed go faster by 25
        and makes it go forward by the speed'''
        self.speed += 25
    def go_slower(self):
        '''go_slower(self) -> makes the speed go slower by 25 and go forward by
        the speed'''
        self.speed -= 25
    def go_left(self):
        '''go_left(self) -> makes the turtle go left by 90 degrees'''
        turtle.Turtle.left(self,90)
    def go_right(self):
        '''go_right(self) -> makes the turtle go right by 90 degrees'''
        turtle.Turtle.right(self,90)
    def go_forward(self):
        '''go_forward(self) -> goes forward by the speed divided by 25 then loops it using ontimer'''
        self.forward(self.speed/25)
        self.getscreen().ontimer(self.go_forward, 40)
        

wn = turtle.Screen()
pete = SuperAwesomeTurtle()
wn.listen()
wn.mainloop()
