from SimulationCode import Dimensions
from ball_Fmu import Ball_FMU

class MyFMU:

    ball = ''
    continuous_states = []
    time = 0
    dt = 0.03

    def __init__(self):
        self.ball = Ball_FMU()
        pass

    def load_fmu(self):
        pass

    def initialize(self):
        self.continuous_states = self.ball.getStates()

    def get_event_indicators(self):
        self.ball


def load_fmu():
    return MyFMU()







