STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):  
        super().__init__()
        self.create_turtle() 

    def create_turtle(self): 
        self.penup()
        self.setpos(STARTING_POSITION)
        self.shape('turtle')
        self.color('black')
        self.shapesize(1.3,1.3)
        self.setheading(90)

    def clear_turtle(self): 
        self.clear() 


    def up(self): 
        self.forward(MOVE_DISTANCE)

    def down(self): 
        self.backward(MOVE_DISTANCE)
        
    def left(self): 
        currentx = self.xcor()
        currenty = self.ycor() 
        self.goto(currentx - 10, currenty)

    def right(self): 
        currentx = self.xcor()
        currenty = self.ycor() 
        self.goto(currentx + 10, currenty)

