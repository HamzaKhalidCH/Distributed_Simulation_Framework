import sys
import pylab as P
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

def runMaster(comm):

    message = comm.recv(source=1, tag=1)

    comm.send("initialize",dest=1,tag=2)
    message = comm.recv(source=1, tag=3)

    Tstart = 0.5  # The start time.
    Tend = 100    #End time

    time = Tstart
    dt = 0.1

    t_sol  = []
    t_time =  []
    while time < Tend:
        time = time + dt
        comm.send(time,dest=1,tag=11)
        t_sol.append(comm.recv(source=1, tag=12))
        t_time.append(time)
    comm.send('-999', dest=1, tag=11)

    print(t_sol[500][0],t_sol[500][1])

    plt.scatter(t_sol[500][0], t_sol[500][1], s=100, c='green')
    plt.show()
    # P.figure(1)
    # P.plot(t_sol[:][0], t_sol[:][1])
    # P.ylabel('Y (m)')
    # P.xlabel('X (s)')
    # P.show()



