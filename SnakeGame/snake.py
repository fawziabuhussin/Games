from turtle import  Turtle
import time

POSES = [(0,0) , (-20,0), (-40,0)]
MOVE_DISTACE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180






class Snake:

    def __init__(self):
        self.segements = []
        self.create_snake()
        self.head = self.segements[0]

    def create_snake(self):
        for pos in POSES:
            self.add_segement(pos)

    def reset(self):
        for seg in self.segements:
            seg.goto(500,500)
        self.segements.clear()
        self.create_snake()
        self.head = self.segements[0]


    def extend(self):
        self.add_segement(self.segements[-1].position())

    def add_segement(self, position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.speed("fastest")
        new_seg.penup()
        new_seg.goto(position)
        self.segements.append(new_seg)


    def move(self):
        time.sleep(0.1)
        for seg in range(len(self.segements) - 1, 0, -1):
            new_x = self.segements[seg - 1].xcor()
            new_y = self.segements[seg - 1].ycor()
            self.segements[seg].goto(new_x, new_y)
        self.segements[0].forward(MOVE_DISTACE)


    def up(self):
        if self.head.heading() != DOWN:
            self.segements[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segements[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.segements[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segements[0].setheading(LEFT)

