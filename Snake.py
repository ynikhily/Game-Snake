# This file contains the definition of our snake object and functions that enables it move across our screen.
from turtle import Turtle


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for snake_pos in range(0, -60, -20):
            self.add_segment((snake_pos, 0))

    def add_segment(self, position):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.speed(0)
        snake.penup()
        snake.goto(position)
        self.segment.append(snake)

    def extend_snake(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for snake_index in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[snake_index - 1].xcor()
            new_y = self.segment[snake_index - 1].ycor()
            self.segment[snake_index].goto(new_x, new_y)
        self.head.forward(20)

    def reset_snake(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
