from turtle import Turtle
import random

class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        self.setposition(x, y)
        self.speed = 2

    def move(self):
        self.setx(self.xcor() + self.speed)

        if self.xcor() > 270 or self.xcor() < -270:
            self.sety(self.ycor() - 40)
            self.speed *= -1
