from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}                 High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            self.score = 0
            self.update_score()

    def game_over_words(self):
        self.goto(x=0, y=0)
        self.write("Game Over! Better luck next Time 🙃", align=ALIGNMENT, font=FONT)

    def score_card(self):
        self.score += 1
        self.update_score()
