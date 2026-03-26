from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def increaseScore(self):
        self.score += 1
        self.updateScoreBoard()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)