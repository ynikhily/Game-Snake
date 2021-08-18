# This file defines the Scoreboard object of the game.
from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.speed(0)
        self.goto(0, 280)
        self.update_score()

    def scored(self):
        self.score += 1
        self.update_score()

    def refresh_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER!!', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}\tHigh Score: {self.high_score} ", move=False, align=ALIGNMENT, font=FONT)
