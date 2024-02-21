from turtle import Screen
import random
from player import Player
from bullet import Bullet
from enemy import Enemy
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
game_on = True

player = Player()
bullet = Bullet()
enemies = [Enemy() for _ in range(30)]
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(lambda: bullet.fire(player), "space")

while game_on:
    for enemy in enemies:
        enemy.move()
        if bullet.isvisible() and bullet.distance(enemy) < 20:
            bullet.setposition(0, -400)
            enemy.setposition(random.randint(-200, 200), random.randint(100, 250))
            scoreboard.increase_score()

        if player.distance(enemy) < 20:
            player.reduce_life()
            if player.lives == 0:
                game_on = False
                scoreboard.game_over()

    bullet.move()
    screen.update()

screen.mainloop()



