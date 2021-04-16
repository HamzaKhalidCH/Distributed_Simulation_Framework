from mpi4py import MPI

from master import runMaster
from slave import runSlave
from slave2 import runSlave2

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

bouncing_fmu = None

def run_MPI():

    if rank == 0:
        runMaster(comm)

    elif rank == 1:
        runSlave(comm)

    elif rank == 2:
        runSlave(comm)

    elif rank == 3:
        runSlave(comm)

if __name__ == "__main__":
    run_MPI()

#  AWS cloudDK  python script to create infrastructure