# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:48:21 2020

@author: Nima
"""

# import pycxsimulator
from pylab import *
import time
from tkinter import *
import tkinter.font as font
import networkx as nx
import matplotlib.pyplot as plt
import psutil


populationSize = 50
edges = 0.05
initialInfectedRatio = 0.5
infectionProb = 0.6
recoveryProb = 0.4
#isolationProb = 0.8

#change from 0 for sus to gray & from 1 for infected to r
#should this represent the state not the number because below we start to initialize the population and assign the state randomly
#susceptible = 'gray'
#infected = 'r'

susceptible = 'gray'
infected = 'r'
recovered = 'g'
# mitigation policies
#---------------------------------------------------------------------
root = Tk()
root.title('Simulator')
root.geometry('600x600')
Font = font.Font(size=20)
#---------------------------------------------------------------------
def theTimeInterval():
        start_time = time.time()
        s = 0
        for i in range (1, n + 1):
            s = s + i 
        end_time = time.time()
        return s, end_time-start_time
n = 10
print(theTimeInterval())
    
#---------------------------------------------------------------------
def initialize():
    global time, network, positions, nextNetwork, infectionTime
    time = 0
    infectionTime = 0
    #Returns a random graph & it takes (no.of nodes and prob. for edge creation)
    network = nx.erdos_renyi_graph(populationSize, edges)
    positions = nx.random_layout(network)
    
#need to check the probabilities -> lessthan or equal 
    for i in network.nodes:
        #add a new element to nodes 
        network.nodes[i]['inf_t'] = infectionTime
       
        #lessthan or equal
        if random() < initialInfectedRatio:
            network.nodes[i]['state'] = infected 
        else:
            network.nodes[i]['state'] = susceptible
    nextNetwork = network.copy()

Btn = Button(text = "initialize",  command = initialize)
Btn.pack(padx = 10, pady = 40)
Btn['font'] = Font
#---------------------------------------------------------------------
def observe():
    cla()

    nx.draw(network,
            pos = positions,
            node_color = [network.nodes[i]['state'] for i in network.nodes],
            node_size = 250,
           )
    axis('image')
    title('time = ' + str(time))
    plt.axis('on')
    plt.show()
#---------------------------------------------------------------------
Btn = Button(text = "observe",  command = observe)
Btn.pack(padx = 10, pady = 40)
Btn['font'] = Font
#---------------------------------------------------------------------
def update():
    global time, network, nextNetwork, infectionTime

    time += 1
 #  infectionTime +=1
    #print(infctionTime)
    
    for i in network.nodes:
        
        if network.nodes[i]['state'] == susceptible:
            nextNetwork.nodes[i]['state'] = susceptible
            for j in network.neighbors(i):
                if network.nodes[j]['state'] == infected:
                    if random() < infectionProb:
                        nextNetwork.nodes[i]['state'] = infected
                        nextNetwork.nodes[i]['inf_t'] = nextNetwork.nodes[i]['inf_t'] + 1
                        break
        elif network.nodes[i]['state'] == infected:
             nextNetwork.nodes[i]['inf_t'] = nextNetwork.nodes[i]['inf_t'] + 1
           
             if random() < recoveryProb and nextNetwork.nodes[i]['inf_t']>=3:
                #print(nextNetwork.nodes[i]['inf_t'])
                nextNetwork.nodes[i]['state'] = recovered
                for j in network.neighbors(i):
                   if network.nodes[j]['state'] == susceptible:
                      if random() < infectionProb:
                        nextNetwork.nodes[j]['state'] = infected
                        nextNetwork.nodes[i]['inf_t'] = nextNetwork.nodes[i]['inf_t'] + 1
                        break
    del network
    network = nextNetwork.copy()
    
Btn = Button(text = "update",  command = update)
Btn.pack(padx = 10, pady = 40)
Btn['font'] = Font

label = Label(root, text="Infection Time : ")
label.pack(side = LEFT, padx=10,  pady=20 )
label['font'] = Font

#---------------------------------------------------------------------
# StatusBar
status = Label(root, text="COVID-19 Simulator for ACIT 4610",
                     bd=2, bg="deepskyblue", relief=GROOVE, )
status.pack(side=BOTTOM, fill=X, padx=10, pady=20)

#---------------------------------------------------------------------
#pycxsimulator.GUI().start(func=[initialize, observe, update])
root.mainloop()