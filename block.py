import random
from turtle import Turtle

colors = ["red", "orange", "yellow", "blue"]


class Block(Turtle):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.block = Turtle()
        self.hideturtle()
        self.block.shape('square')
        self.block.shapesize(stretch_wid=height, stretch_len=width)
        self.block.color(random.choice(colors))
        self.block.penup()
        self.block.goto(x, y)
        
        