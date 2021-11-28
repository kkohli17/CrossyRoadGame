FONT = ("Courier", 12, "normal")
from turtle import Turtle

class Scoreboard(Turtle): 
    def __init__(self): 
        super().__init__() 
        self.score = 0 
        self.update_score() 

    def update_score(self): 
        self.clear() 
        self.color('white')
        self.penup() 
        self.hideturtle() 
        self.goto(x=-370,y=250)
        self.write(f" Level : {self.score}",align='left',font=FONT)

    def mid_score(self): 
        self.color('black')
        self.penup() 
        self.hideturtle() 
        self.goto(x=0,y=-40)
        self.write(f" You reached Level : {self.score}",align='center',font=FONT)

    def to_front(self): 
        self.forward(0)

        



