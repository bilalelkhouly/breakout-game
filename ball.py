from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('#808080')
        self.penup()
        self.goto(0, 0)
        self.x_speed = 8
        self.y_speed = 8
        self.moving_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1
