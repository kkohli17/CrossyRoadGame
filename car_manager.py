from turtle import Turtle
import random

from player import MOVE_DISTANCE 


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
YLOCATIONS = list(range(-210,310,80))
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 30

class CarManager(Turtle): 
    def __init__(self): 
        super().__init__()  

    def create_car(self): 
        self.penup()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.shapesize(stretch_len=2.5,stretch_wid = 1.2)
        self.goto(x=360,y=random.choice(YLOCATIONS))

    def move_car(self): 
        self.goto(self.xcor() - MOVE_INCREMENT,self.ycor())