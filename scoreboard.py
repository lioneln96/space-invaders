from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-290, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=("Arial", 14, "normal"))

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
        self.goto(0, -30)
        self.write(f"Final Score: {self.score}", align="center", font=("Arial", 18, "normal"))

