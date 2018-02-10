import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

import math


class point:
    def __init__(self, x, z, r, k, omega, h):
        self.x = x
        self.z = z
        self.r = r
        self.k = k
        self.h = h
        self.omega = omega
        self.x_ = x
        self.z_ = z
        self.dx = 0
        self.dz = 0
        self.time_ = 0
        self.Lambda = 0.4

    def next(self, time):
        p = self.k * self.x - self.omega * time
        phase = p - self.Lambda * (self.z_ - self.z)
        x0 = self.x + self.r * np.sin(phase) + 2 * self.r * np.sin(p + math.pi / 2)
        z0 = self.z - self.r * np.cos(phase) + 2 * self.r * np.cos(p + math.pi / 2)

        self.dx = x0 - self.x_
        self.dz = z0 - self.z_
        self.x_ = x0
        self.z_ = z0
        self.time_ = time
        return x0, z0


x = np.linspace(-256, 256, 1000)
z = np.linspace(0, 0, 1000)
points = point(x, z, 2, 0.025, 0.2, 200)

fig = plt.figure()
ax = plt.axes(xlim=(-256, 256), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)


def init():
    line.set_data(x, z)
    return line,


def update(i):
    x0, z0 = points.next(i)
    line.set_data(x0, z0)
    return line,


anim = animation.FuncAnimation(fig, update, init_func=init, frames=200, interval=20, blit=False)

plt.show()
