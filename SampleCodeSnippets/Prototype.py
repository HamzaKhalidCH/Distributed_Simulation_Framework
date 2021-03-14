import turtle
from mpi4py import MPI
# from vpython import *
import time
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()


def runSim():
    if rank == 0:
        print("Master is Existing......")

        timeStart = 0
        timeEnd = 11
        dt = 1
        time = timeStart
        cord = []
        f = open("logs.txt", "w")

        while time < timeEnd:
            comm.send(time, dest=1, tag=100)
            cord = comm.recv(source=1, tag=200)
            f.write("{t} {x} {y} \n".format(t=time, x=cord[0], y=cord[1]))
            time += dt

        comm.send("Exit", dest=1, tag=100)

        message = comm.recv(source=1, tag=400)

        f.close()

    elif rank == 1:
        sys.stdout.write("Child is Stimulating.....")

        # ball.goto(0,200)

        dy = -2
        dx = 2

        yCord = 0
        xCord = 0

        direction = 1

        while True:

            time = comm.recv(source=0, tag=100)

            if time == "Exit":
                break

            if yCord <= -250:
                direction *= -1
                dy *= -1

            if yCord >= 250:
                direction *= -1
                dy *= -1

            yCord = 2 * (time % 250) * direction

            comm.send((xCord, yCord), dest=0, tag=200)

        comm.send("Finished", dest=0, tag=400)


if __name__ == "__main__":
    runSim()
