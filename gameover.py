FONT = ("Courier", 40, "normal")
from turtle import Turtle
from scoreboard import Scoreboard

class GameOver(Turtle): 
    def __init__(self): 
        super().__init__()
        self.hideturtle()

    def gameover(self):  
        self.hideturtle() 
        self.color('black')
        self.penup() 
        self.goto(x=0,y=-10)
        self.write("Game Over",align='center',font=FONT)