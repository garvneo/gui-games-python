from turtle import Turtle

ALIGNMENT = "center"
FONTSTYLE = ("Times", 15, "bold")


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = self.fetch_highscore()
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(0, 320)
        self.refresh()

    def refresh(self):
        self.score += 1
        self.update_scorecard()

    def update_scorecard(self):
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONTSTYLE,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_highscore()
        self.score = 0
        self.update_scorecard()

    def game_over(self):
        self.goto(0, 0)
        self.color("White")
        self.write(" Game Over!", align=ALIGNMENT, font=FONTSTYLE)

    def fetch_highscore(self):
        with open("data") as file:
            hs = int(file.read())
            return hs

    def set_highscore(self):
        with open("data", mode="w") as file:
            file.write(str(self.high_score))
