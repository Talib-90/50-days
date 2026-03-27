from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("SnakeGame/data.txt") as data:
            self.highScore = int(data.read())
        # self.highScore = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.highScore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("SnakeGame/data.txt", "w") as data:
                data.write(f"{self.highScore}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()