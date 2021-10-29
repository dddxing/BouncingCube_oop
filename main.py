from vpython import *
import math
import random
import datetime
import time

g = -9.8        # in m/s^2
dt = 0.001      # in s
t = 0           # in s


class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Cube:
    def __init__(self, position, length):
        self.length = length
        self.position = Position(position[0], position[1], position[2])

    def create(self):

        corners = [(self.position.x, self.position.y, self.position.z),
                   (self.position.x + self.length, self.position.y, self.position.z),
                   (self.position.x, self.position.y + self.length, self.position.z),
                   (self.position.x, self.position.y, self.position.z + self.length),
                   (self.position.x + self.length, self.position.y + self.length, self.position.z),
                   (self.position.x + self.length, self.position.y, self.position.z + self.length),
                   (self.position.x, self.position.y + self.length, self.position.z + self.length),
                   (self.position.x + self.length, self.position.y + self.length, self.position.z + self.length)
                   ]
        cor_objs = []
        edges = []

        for corner in corners:
            cor_obj = sphere(pos=vector(corner[0], corner[1], corner[2]), radius=0.3, color=color.red)
            cor_objs.append(cor_obj)

        for i in range(len(cor_objs)):
            for j in range(i, len(cor_objs)):
                line = curve(vector(cor_objs[i].pos), vector(cor_objs[j].pos))
                edges.append(line)


cube1 = Cube(position=(0, 10, 0), length=1)
cube1.create()

cube2 = Cube(position=(0, 5, 0), length=2)
cube2.create()

floor = box(pos=vector(0, 0, 0), size=vector(10, 0.5, 10), color=color.green)
