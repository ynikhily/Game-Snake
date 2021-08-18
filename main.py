from turtle import Screen
import time
from Snake import Snake
from Food import Food
from score import ScoreBoard

# ------------------------------------- CREATE A SCREEN INSTANCE------------------------------------------
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

# ----------------------------- INITIATE A SNAKE, FOOD AND SCOREBOARD OBJECT-----------------------------
snake = Snake()
food = Food()
user_score = ScoreBoard()

# --------------------- ASSIGN KEYS FOR THE MOVEMENT FUNCTIONS OF YOUR SNAKE OBJECT------------------------
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

# -----------------------------------------GAME FLOW BEGINS-------------------------------------------------
game_on = True

while game_on:
    screen.update()
    time.sleep(0.01)
    snake.move()

# CONDITION FOR SNAKE EATS THE FOOD.
    if snake.head.distance(food) <= 15:
        food.refresh()
        user_score.scored()
        snake.extend_snake()

# CONDITION FOR SNAKE'S COLLISION WITH SCREEN OR WITH ITSELF
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        user_score.refresh_game()
        snake.reset_snake()

# ELONGATES THE SNAKE'S BODY
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            user_score.refresh_game()
            snake.reset_snake()

screen.exitonclick()
