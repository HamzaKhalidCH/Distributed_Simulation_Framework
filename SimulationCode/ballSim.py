from FMU import MyFMU,Ball
import turtle
import math
import random

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
                """"
                tempX = balls[i].Ball.xcor()
                tempY = balls[i].Ball.ycor()

                balls[i].Ball.setx(balls[index].Ball.xcor())
                balls[i].Ball.sety(balls[index].Ball.ycor())

                balls[index].Ball.setx(tempX)
                balls[index].Ball.sety(tempY)
               """
                velX = balls[i].dx
                velY = balls[i].dy

                balls[i].dx = (balls[index].dx)
                balls[i].dy = (balls[index].dy)

                balls[index].dx = velX
                balls[index].dy = velY

                print('After Swap')
                print('balls[i].x = ',velX," balls[i].y = ",velY)
               # print('balls[i].x = ', tempX, " balls[i].y = ", tempY)

"""        

while True:

    wn.update()
    ball1.shape("circle")
    ball1.color("blue")
    ball1.penup()

    ball2.shape("circle")
    ball2.color("red")
    ball2.penup()

    if ball1.ycor() < -250:
        dy *= -1

    if ball1.xcor() < -250:
        dx *= -1

    if ball1.ycor() > 250:
        dy *= -1

    if ball1.xcor() > 250:
        dx *= -1

    if ball2.ycor() < -250:
        dy2 *= -1

    if ball2.xcor() < -250:
        dx2 *= -1

    if ball2.ycor() > 250:
        dy2 *= -1

    if ball2.xcor() > 250:
        dx2 *= -1

    ball1.setx(ball1.xcor()+dx)
    ball1.sety(ball1.ycor()+dy)

    ball2.setx(ball2.xcor()+dx2)
    ball2.sety(ball2.ycor()+dy2)


    print("x = ",ball1.xcor(),"y = ",ball1.ycor())

"""
