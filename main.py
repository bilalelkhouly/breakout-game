import time
from turtle import Screen, Turtle
from paddle import Paddle
from block import Block
from ball import Ball

PADDLE_POSITION = (0, -250)
BACKGROUND_COLOR = '#202020'

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor(BACKGROUND_COLOR)
screen.title("Breakout Game")
screen.tracer(0)

blocks = []
game_is_on = True

paddle = Paddle(PADDLE_POSITION)
ball = Ball()

for y in range(280, 105, -35):
    for x in range(-345, 340, 85):
        block = Block(width=4, height=1.5, x=x, y=y)
        blocks.append(block)


screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

while game_is_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()

    # Detect collision with horizontal walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with vertical walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.bounce_y()

    # Detect collision with blocks
    for block in blocks:
        if ball.distance(block) < 30:
            blocks.remove(block)
            block.hideturtle()