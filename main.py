from copyreg import constructor
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scorebeard import Scorebeard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


scorebeard = Scorebeard()

continuar = True
food = Food()
while continuar:
    snake = Snake()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.listen()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

        ## detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scorebeard.update_score()

        ## detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scorebeard.game_over()

        ## Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scorebeard.game_over()
    ##
    continuar = screen.textinput("Snake", "New Game? (S/N)").upper() == "S"
    scorebeard.game_new()
    snake.game_new()
    food.refresh()
screen.exitonclick()