from turtle import Turtle, Screen
import time
import random
from player import Player
from roadmarks import RoadMarks
from car_manager import CarManager
from scoreboard import Scoreboard
from gameover import GameOver
screen = Screen() 
screen.setup(width=800,height=600)
screen.bgcolor('gray')
screen.title('Turtle Crossing Game')
screen.tracer(0)

player = Player() 
scoreboard=Scoreboard()
gameov= GameOver()

for xgiven in range(-360,380,100): 
    for ygiven in range(-250,310, 80): 
        road = RoadMarks(xgiven,ygiven) 



screen.listen()
screen.onkeypress(player.up,'Up')
screen.onkeypress(player.down,'Down')
screen.onkeypress(player.left, 'Left')
screen.onkeypress(player.right, 'Right')
carlist=[]
game_is_on = True 

counter = 0 
divisor = 10
sleepset = 0.1
while game_is_on:

    time.sleep(sleepset)
    screen.update()
    if counter%divisor == 0: 
        for num in range(random.randint(1,6)): 
            car = CarManager()
            car.create_car()
            carlist.append(car)
        
    
    for car in carlist:
        car.move_car()
        if player.distance(car) < 25: 
            gameov.gameover() 
            scoreboard.mid_score()
            scoreboard.to_front() 
            game_is_on = False 

    counter +=1 

    if player.ycor() > 292: 
        scoreboard.score += 1 
        scoreboard.update_score()
        player.goto(0,-280)  
        sleepset *= 0.8
        divisor = divisor-1 # decrease regeneration rate 
        counter = 0 

while not game_is_on: 
    screen.update() 



screen.exitonclick()