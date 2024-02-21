from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.setposition(0, -250)
        self.setheading(90)
        self.speed = 15
        self.lives = 3

    def move_left(self):
        x = self.xcor()
        x -= self.speed
        if x < -280:
            x = -280
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += self.speed
        if x > 280:
            x = 280
        self.setx(x)

    def reduce_life(self):
        self.lives -= 1