import turtle
from mpi4py import MPI
# from vpython import *
import time
import sys
from datetime import datetime

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def runSim():

    if rank == 0:

        # sphere()
        print("Master is Existing......")
        data = " "
        for i in range(2):
            data = comm.recv(source=1, tag=1)
            sys.stdout.write(data)
            print(datetime.now().time())
            data = "Received"
            comm.send(data, dest=1, tag=2)

            # print(data+"{num}".format(num=i))

        # req = comm.irecv(source=1,tag=22)
        # data = req.Wait()
        # print(data)

    elif rank == 1:

        sys.stdout.write("Child is Stimulating.....")

        wn = turtle.Screen()
        wn.bgcolor("black")
        wn.title("Ball Simulation")
        # wn.tracer(10)

        ball = turtle.Turtle()
        ball.shape("circle")
        ball.color("green")
        ball.penup()
        ball.speed(0)
        # ball.goto(0,200)

        ball.dy = -2
        ball.dx = 2
        while True:

            f = open("myfile.txt", "a")
            f.write(" coordinates {x} {y} \n".format(x=ball.dx, y=ball.dy))
            f.close()

            wn.update()
            ball.sety(ball.ycor() + ball.dy)

            if ball.ycor() < -250:
                ball.dy *= -1

                data = "Shawty hit the floor"
                comm.send(data, dest=0, tag=1)
                data = comm.recv(source=0, tag=2)

            if ball.ycor() > 250:
                ball.dy *= -1
                data = "Just Hit the Roof"
                comm.send(data, dest=0, tag=1)
                break

if __name__ == "__main__":
    runSim()