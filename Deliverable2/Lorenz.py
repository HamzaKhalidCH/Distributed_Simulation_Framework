
from pyfmi import load_fmu

lorenz_fmu = load_fmu('Lorenz.fmu')

Tstart = 0.5  # The start time.
Tend = 3.0  # The final simulation time.

lorenz_fmu.time = Tstart

lorenz_fmu.initialize()

x = lorenz_fmu.get_
print(x)
