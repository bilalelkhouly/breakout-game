import random
from turtle import Turtle

colors = ["red", "orange", "yellow", "blue"]


class Block(Turtle):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=height, stretch_len=width)
        self.color(random.choice(colors))
        self.penup()
        self.goto(x, y)
        
        