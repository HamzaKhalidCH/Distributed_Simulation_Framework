import sys
from fyFmu import Ball_FMU

def runSlave(comm):

    sys.stdout.write("Child is Stimulating.....")
    comm.send("Child Ready",dest=0,tag=1)
    command = comm.recv(source=0,tag=2)
    message= 'error'
    bouncing_fmu = ''
    if(command == "initialize"):
         bouncing_fmu = Ball_FMU()
    comm.send(message, dest=0, tag=3)

    x = bouncing_fmu.getStates()

    while True:

        time = comm.recv(source=0,tag=11)

        if time == '-999':
            break

        bouncing_fmu.update(time=time)

        event_id = bouncing_fmu.getEventIndicator()

        bouncing_fmu.completed_Integrator_Step(event_id)

        comm.send(bouncing_fmu.getStates()+250, dest=0, tag=12)

    bouncing_fmu.finish()