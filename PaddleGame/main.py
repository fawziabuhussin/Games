from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup( width=800, height=600)
screen.title("Pong")
screen.tracer(0)


paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()


game_is_on = True



screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collison.
    if ball.ycor() > 280 or ball.ycor() < -280 :
        #need to bouce.
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 \
            or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

        #detect if paddle missed the ball:
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.left_score()

    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.right_score()





screen.exitonclick()