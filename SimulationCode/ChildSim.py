import time
import sys
from datetime import datetime

def runChild(comm, bouncing_fmu):

    bouncing_fmu.time = 0.5

    sys.stdout.write("Child is Stimulating.....")

    comm.send("Child Ready",dest=0,tag=1)

    command = comm.recv(source=0,tag=2)

    message= 'error'
    if(command == "initialize"):
        bouncing_fmu.initialize()
        message = "initialized"

    comm.send(message, dest=0, tag=3)

    vref = [bouncing_fmu.get_variable_valueref('h')] + [bouncing_fmu.get_variable_valueref('v')]

    comm.send([bouncing_fmu.get_real(vref)],dest=0,tag=102)

    Tstart = 0.5  # The start time.
    Tend = 3.0

    time = Tstart
    Tnext = Tend  # Used for time events
    dt = 0.01  #

    x = bouncing_fmu.continuous_states

    event_ind = bouncing_fmu.get_event_indicators()

    vref = [bouncing_fmu.get_variable_valueref('h')] + [bouncing_fmu.get_variable_valueref('v')]

    while True:

        # Compute the derivative
        dx = bouncing_fmu.get_derivatives()
        # Advance
        h = min(dt, Tnext - time)
        # Set the time
        bouncing_fmu.time = time

        time = comm.recv(source = 0,tag=11)  

        if time is None:
            break

        # Set the inputs at the current time (if any)
        # bouncing_fmu.set_real,set_integer,set_boolean,set_string (valueref, values)

        # Set the states at t = time (Perform the step)
        x = x + h * dx
        bouncing_fmu.continuous_states = x

        # Get the event indicators at t = time
        event_ind_new = bouncing_fmu.get_event_indicators()

        # Inform the model about an accepted step and check for step events
        step_event = bouncing_fmu.completed_integrator_step()

        # Check for time and state events
        time_event = abs(time - Tnext) <= 1.e-10
        state_event = True if True in ((event_ind_new > 0.0) != (event_ind > 0.0)) else False

        # Event handling
        if step_event or time_event or state_event:

            eInfo = bouncing_fmu.get_event_info()
            eInfo.iterationConverged = False

            # Event iteration
            while eInfo.iterationConverged == False:
                bouncing_fmu.event_update(intermediateResult=True)  # Stops after each event iteration
                eInfo = bouncing_fmu.get_event_info()

                # Retrieve solutions (if needed)
                if eInfo.iterationConverged == False:
                    # bouncing_fmu.get_real, get_integer, get_boolean,
                    # get_string(valueref)
                    pass

            # Check if the event affected the state values and if so sets them
            if eInfo.stateValuesChanged:
                x = bouncing_fmu.continuous_states

            # Get new nominal values.
            if eInfo.stateValueReferencesChanged:
                atol = 0.01 * rtol * bouncing_fmu.nominal_continuous_states

            # Check for new time event
            if eInfo.upcomingTimeEvent:
                Tnext = min(eInfo.nextEventTime, Tend)
            else:
                Tnext = Tend

        event_ind = event_ind_new

        comm.send(Tnext,dest=0,tag=10)
        comm.send([bouncing_fmu.get_real(vref)], dest=0, tag=12)