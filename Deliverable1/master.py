import sys
import math
import matplotlib.pyplot as plt
import turtle

radius = 20
numOfSlaves = 3
def checkEvent(sol,vel):

   events = {1:0 , 2:0 ,3:0}
   for i in range(1,numOfSlaves):
       for j in range(i+1,numOfSlaves+1):
          if (math.sqrt((sol[i][-1][0] - sol[j][-1][0]) ** 2
               + (sol[i][-1][1] - sol[j][-1][1]) ** 2)) < radius:
                  print("--------- Collision True --------")
                  print("For Ball 1 x = {}  y = {}".format(sol[i][-1][0],sol[i][-1][1]))
                  print("For Ball 1 x = {}  y = {}".format(sol[j][-1][0], sol[j][-1][1]))

                  events[i] = vel[j]
                  events[j] = vel[i]

   return events


def runMaster(comm):


    for i in range(numOfSlaves):
        message = comm.recv(source=i+1, tag=1)
        comm.send("initialize",dest=i+1,tag=2)
        message = comm.recv(source=i+1, tag=3)

    Tstart = 0.5  # The start time.
    Tend = 100000  # End time

    time = Tstart
    dt = 0.5

    t_sol = {1:[],2:[],3:[]}
    t_time = []

    t_vel = {1:[],2:[],3:[]}

    count = 0

    while time < Tend:
        time = time + dt
        for i in range(1,numOfSlaves+1):
            comm.send(time,dest=i,tag = 4)
        for i in range(1,numOfSlaves+1):
            #rec = comm.recv(source=i,tag = 5)
            t_sol[i].append(comm.recv(source=i,tag = 5))
            t_vel[i] = comm.recv(source=i,tag=6)

        events = checkEvent(t_sol,t_vel)

        for i in range(1,len(events)+1):
            if(events[i]==0):
                comm.send(-1,dest=i ,tag = 8)
            else:
                count += 1
                # print("Collision Occured at")
                # print("For Ball ",i)
                # print("Velocity : ",events[i][0],' ',events[i][1])

                comm.send(1,dest=i ,tag = 8)
                comm.send(events[i][0],dest=i, tag = 9)      #dx
                comm.send(events[i][1],dest=i, tag = 10)     #dy

        t_time.append(time)

    for i in range(1,numOfSlaves+1):
        comm.send('-999', dest=i, tag=4)

    width = 500
    height = 500

    print("Counts = ",count)

    wn = turtle.Screen()
    wn.screensize(canvwidth=width, canvheight=height)
    wn.setup(width=width, height=height)

    wn.bgcolor("black")
    wn.title("Ball Simulation")
    wn.tracer(0)

    turtleObj1 = turtle.Turtle()
    turtleObj1.shape('circle')
    turtleObj2 = turtle.Turtle()
    turtleObj2.shape('circle')
    turtleObj3 = turtle.Turtle()
    turtleObj3.shape('circle')
    turtleObj1.color('green')
    turtleObj2.color('blue')
    turtleObj3.color('red')

    turtleObj1.penup()
    turtleObj2.penup()
    turtleObj3.penup()


    for i in range(1, 100000, 1):
        #plt.figure(figsize=(500, 500))
        #plt.xlim(0, 500)
        #plt.ylim(0, 500)
        #plt.scatter(t_sol[1][i][0] , t_sol[1][i][1] , s=100, c='green')
        #plt.scatter(t_sol[2][i][0] , t_sol[2][i][1] , s=100, c='blue')
        turtleObj1.setx(t_sol[1][i][0]-250)
        turtleObj1.sety(t_sol[1][i][1]-250)
        turtleObj2.setx(t_sol[2][i][0]-250)
        turtleObj2.sety(t_sol[2][i][1]-250)
        turtleObj3.setx(t_sol[3][i][0] - 250)
        turtleObj3.sety(t_sol[3][i][1] - 250)
        wn.update()
        #plt.show()

    turtle.bye()

""""
    Tstart = 0.5  # The start time.
    Tend = 10000    #End time

    time = Tstart
    dt = 1

    t_sol  = []
    t_time =  []
    while time < Tend:
        time = time + dt
        comm.send(time,dest=1,tag=11)
        t_sol.append(comm.recv(source=1, tag=12))
        t_time.append(time)
    comm.send('-999', dest=1, tag=11)


    for i in range(1,10000,1000):
        plt.figure(figsize=(500,500))
        plt.xlim(0,500)
        plt.ylim(0,500)
        plt.scatter(t_sol[i][0]+250, t_sol[i][1]+250, s=100, c='green')
        plt.show()
        # P.figure(1)
        # P.plot(t_sol[:][0], t_sol[:][1])
        # P.ylabel('Y (m)')
        # P.xlabel('X (s)')
        # P.show()
"""


