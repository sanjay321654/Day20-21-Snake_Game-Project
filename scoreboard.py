from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over_words(self):
        self.goto(x=0, y=0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)


    def score_card(self):
        self.score += 1
        self.clear()
        self.update_score()
