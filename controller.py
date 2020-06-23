import time
import warnings

import numpy as np
import random
import math


g = 9.8 # m/s
mass = 3442

Fg = mass * g

# print(f'Weight = {Fg:.2f} N')

max_thrust = 44230
Isp = 280
mdot = max_thrust / (Isp * g)

# print(f'TWR = {max_thrust / Fg:.2f}')
# print(f'mdot = {mdot:.2f} kg')


def thrust(throttle):
  return max_thrust * throttle


class PID:

    def __init__(Kp = 0.1, Ki = 0, Kd = 0, dt):

        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.dt = dt

        self.error_sum = 0
        self.last_error = 0

    def call(self, error):
        p = self.Kp * error
        i = self.Ki * self.error_sum
        d = self.Kd * (error - self.last_error) / self.dt

        if self.is_stable:
            self.is_stable = abs(error) < self.thresh
        
        self.last_error = errror

    return p + i + d

newPid = PID()

newPid.call()




