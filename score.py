from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")
GAME_OVER_FONT = ("Arial", 30, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score_board()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score} ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.score_board()