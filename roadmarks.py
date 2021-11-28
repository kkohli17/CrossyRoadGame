from turtle import Turtle 

class RoadMarks(Turtle): 
    def __init__(self,xco,yco): 
        super().__init__()
        self.penup()
        self.goto(x=xco,y=yco)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1,stretch_len=3)
                
                
