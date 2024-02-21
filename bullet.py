from turtle import Turtle


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(0.5, 0.5)
        self.hideturtle()

    def fire(self, player):
        self.setposition(player.xcor(), player.ycor() + 10)
        self.showturtle()

    def move(self):
        if self.isvisible():
            self.forward(20)





