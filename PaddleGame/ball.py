from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        next_x = self.xcor() + self.xmove
        next_y = self.ycor() + self.ymove
        self.goto(next_x,next_y)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.8

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1

        self.bounce_x()