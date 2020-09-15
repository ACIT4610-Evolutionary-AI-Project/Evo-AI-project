# import pycxsimulator
from pylab import *

import networkx as nx

n = 100  # size of space: n x n
p = 0.24 # probability of initially panicky individuals


def initialize():

    global config, nextconfig
    config = zeros([n, n])
    for x in range(n):
        for y in range(n):
            config[x, y] = 1 if random() < p else 0
    nextconfig = zeros([n, n])
