import turtle
import random

class Ball_FMU:

    Ball = ''
    dx = 0
    dy = 0
    x  = 0
    y  = 0

    def __init__(self):
        self.Ball = turtle.Turtle()
        self.Ball.shape('circle')
        self.Ball.setx(random.uniform(-0.2, 3.8))
        self.Ball.sety(random.uniform(-0.7, 1.9))
        self.x = self.Ball.xcor()
        self.y = self.Ball.ycor()

    def getStates(self):
       return self.Ball.xcor(),self.Ball.ycor()

    def getDerivative(self):
        return

    def getEvent(self):
        pass