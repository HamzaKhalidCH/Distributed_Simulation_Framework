from mpi4py import MPI
import time
import sys
from datetime import datetime
from MasterSim import runMaster
from ChildSim import runChild

import os as O

import pylab as P
import numpy as N

from pyfmi import load_fmu

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

bouncing_fmu = None

path_to_fmus = '../files/FMUs'
path_to_fmus_me1 = path_to_fmus+'/ME1.0'
path_to_fmus_cs1 = path_to_fmus+'/CS1.0'

def run_MPI():

    if rank == 0:

        comm.send("bouncingBall.fmu",dest=1,tag=101)
        runMaster(comm)

    elif rank == 1:

        fmuName = comm.recv(source=0,tag=101)
        bouncing_fmu = load_fmu(fmuName, path_to_fmus_me1)
        runChild(comm,bouncing_fmu)

if __name__ == "__main__":
    run_MPI()


