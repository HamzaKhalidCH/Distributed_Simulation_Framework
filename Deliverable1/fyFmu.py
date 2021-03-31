import turtle
import random

class Ball_FMU:

    Ball = '' #(x,y)
    dx = 0.05
    dy = -0.05

    def __init__(self):
        width = 500
        height = 500

        self.wn = turtle.Screen()
        self.wn.screensize(canvwidth=width, canvheight=height)
        self.wn.setup(width=width, height=height)

        self.wn.bgcolor("black")
        self.wn.title("Ball Simulation")
        self.wn.tracer(0)

        self.Ball = turtle.Turtle()
        self.Ball.shape('circle')
        self.Ball.setx(random.uniform(-100, 100))
        self.Ball.sety(random.uniform(-100, 100))
        self.Ball.color('green')
        self.Ball.penup()

    def getStates(self):
       return [self.Ball.xcor(),self.Ball.ycor()]

    def update(self,time):
         self.wn.update()
         self.Ball.setx(self.Ball.xcor() + self.dx)
         self.Ball.sety(self.Ball.ycor() + self.dy)
         self.Ball.penup()


    def getDerivative(self):
        return

    def getEventIndicator(self):

        if self.Ball.ycor() < -250:
            #self.dy *= -1
            return 1

        if self.Ball.xcor() < -250:
            #self.dx *= -1
            return 2

        if self.Ball.ycor() > 250:
            #self.dy *= -1
            return 3

        if self.Ball.xcor() > 250:
            #self.dx *= -1
            return 4

    def completed_Integrator_Step(self,id):

        if id == 1:
            self.dy *= -1

        if id == 2:
            self.dx *= -1

        if id == 3:
            self.dy *= -1

        if id == 4:
            self.dx *= -1

    def finish(self):
        self.wn.bye()
