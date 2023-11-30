from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=10)
        self.penup()
        self.goto(position)

    def move_right(self):
        x = self.xcor() + 50
        self.goto(x, self.ycor())

    def move_left(self):
        x = self.xcor() - 50
        self.goto(x, self.ycor())
