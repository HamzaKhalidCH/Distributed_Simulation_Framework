from FMU import MyFMU
import turtle


width = 100
height = 100

wn = turtle.Screen()
wn.screensize(canvwidth=width,canvheight=height)
wn.setup(width=500,height=500)
wn.bgcolor("black")
wn.title("Ball Simulation")
dx = 5
dy = -12

dx2 = 8
dy2 = 10

ball1 = turtle.Turtle()
ball2 = turtle.Turtle()
ball2.goto(0,100)
while True:

    wn.update()
    ball1.shape("circle")
    ball1.color("blue")
    ball1.penup()
    ball1.speed(0)

    ball2.shape("circle")
    ball2.color("red")
    ball2.penup()
    ball2.speed(0)

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

