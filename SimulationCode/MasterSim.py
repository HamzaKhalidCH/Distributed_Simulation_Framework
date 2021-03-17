from datetime import datetime

import os as O

import pylab as P
import numpy as N

from pyfmi import load_fmu

path_to_fmus = '../files/FMUs'
path_to_fmus_me1 = path_to_fmus+'/ME1.0'
path_to_fmus_cs1 = path_to_fmus+'/CS1.0'

with_plots = True

def runMaster(comm):

    print("Master is Existing......")
    message = comm.recv(source=1,tag=1)
    print(message)

    comm.send("initialize",dest=1,tag=2)
    message = comm.recv(source=1, tag=3)

    Tstart = 0.5  # The start time.
    Tend = 3.0

    time = Tstart
    Tnext = Tend  # Used for time events
    dt = 0.01  #

    t_sol = [Tstart]

    sol = comm.recv(source=1,tag=102)

    while time < Tend:
        h = min(dt, Tnext - time)
        time = time + h

        comm.send(time, dest=1, tag=11)
        Tnext = comm.recv(source=1,tag=10)
        t_sol += [time]
        sol += comm.recv(source=1,tag=12)

    comm.send(None, dest=1, tag=11)

    if with_plots:
        # Plot the height
        P.figure(1)
        P.plot(t_sol, N.array(sol)[:, 0])
        P.title("Sample")
        P.ylabel('Height (m)')
        P.xlabel('Time (s)')
        # Plot the velocity
        P.figure(2)
        P.plot(t_sol, N.array(sol)[:, 1])
        P.title("Sample")
        P.ylabel('Velocity (m/s)')
        P.xlabel('Time (s)')
        P.show()

