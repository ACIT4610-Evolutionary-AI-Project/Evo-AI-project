import networkx as nx
from pylab import *
import matplotlib.pyplot as plt

g = nx.karate_club_graph()
nx.draw(g)
show()