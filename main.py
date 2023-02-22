import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    car.make_car()
    car.move_car()

    for s in car.all_cars:
        if player.distance(s) < 21:
            game_is_on = False
            scoreboard.end_game()
    
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.update()

screen.exitonclick()
    