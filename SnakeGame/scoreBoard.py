ALIGMENT = "center"
FONT = ("Arial", 15, "normal")
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        #C:\Users\Fawzi\Desktop\PycharmProjects\SnakeGame\scoreBoard.py
        with open("../../store.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score_board()



    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGMENT, font=FONT)


    def  reset(self):
        if self.score > self.highscore :
            self.highscore = self.score
            with open("/Users/Fawzi/Desktop/store.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score_board()


    def increase_score(self):
        self.score += 1
        self.update_score_board()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", align=ALIGMENT, font=FONT)



