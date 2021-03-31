#from pyFMI import MyFMU
import turtle
import math
import random
#from pyFMI import load_fmu
"""
bouncing_fmu = load_fmu()

Tstart = 0.5 #The start time.
Tend   = 3.0 #The final simulation time.

bouncing_fmu.time = Tstart  #Set the start time before the initialization.

bouncing_fmu.initialize()

# Get Continuous States
x = bouncing_fmu.continuous_states

"""


class Ball:

    def __init__(self):
        self.Ball = ''
        self.dx = 0
        self.dy = 0

width = 500
height = 500

wn = turtle.Screen()
wn.screensize(canvwidth=width,canvheight=height)
wn.setup(width=width,height=height)

wn.bgcolor("black")
wn.title("Ball Simulation")
wn.tracer(0)

totalBalls = 8

balls = []
colors = ['red','green','blue','pink','white','grey','purple','yellow']
cord = [[0.5,0.9],[-0.5,0.4]]

for u in range(totalBalls):
    turtleObj = turtle.Turtle()
    turtleObj.shape('circle')
    turtleObj.color(colors[u])
    obj = Ball()
    obj.Ball = turtleObj
    #obj.dx,obj.dy = cord[u]
    obj.dx = (random.uniform(-0.2,3.8))
    obj.dy = (random.uniform(-0.7, 1.9))
    balls.append(obj)

for ball in balls:
    ball.Ball.penup()
    ball.Ball.goto(random.randint(0,200),random.randint(0,200))

while True:
    for index in range(len(balls)):
        wn.update()

        balls[index].Ball.penup()

        if balls[index].Ball.ycor() < -250:
            balls[index].dy *= -1

        if balls[index].Ball.xcor() < -250:
            balls[index].dx *= -1

        if balls[index].Ball.ycor() > 250:
            balls[index].dy *= -1

        if balls[index].Ball.xcor() > 250:
            balls[index].dx *= -1

        balls[index].Ball.setx(balls[index].Ball.xcor()+balls[index].dx)
        balls[index].Ball.sety(balls[index].Ball.ycor()+balls[index].dy)
        print("x = ", balls[index].Ball.xcor(), "y = ", balls[index].Ball.ycor())

    for index in range(len(balls)):
        for i in range(index+1,len(balls)):
            if (math.sqrt((balls[i].Ball.xcor() - balls[index].Ball.xcor())**2
                          +(balls[i].Ball.ycor() - balls[index].Ball.ycor())**2))<20:
              
                velX = balls[i].dx
                velY = balls[i].dy

                balls[i].dx = (balls[index].dx)
                balls[i].dy = (balls[index].dy)

                balls[index].dx = velX
                balls[index].dy = velY

                print('After Swap')
                print('balls[i].x = ',velX," balls[i].y = ",velY)

               # print('balls[i].x = ', tempX, " balls[i].y = ", tempY)