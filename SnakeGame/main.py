from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard


import time

# Press the green button in the gutter to run the script.

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer()

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


gameIsOn = True
while gameIsOn:
    time.sleep(0.01)
    screen.update()

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreBoard.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        scoreBoard.reset()
        snake.reset()

    for segement in snake.segements:
        if segement == snake.head:
            pass
        elif  snake.head.distance(segement) < 10:
            scoreBoard.reset()
            snake.reset()







screen.exitonclick()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
