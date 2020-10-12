# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:48:21 2020

@author: Nima
"""

# import pycxsimulator
import numpy as np
from scipy.integrate import odeint
from abc import ABC, abstractmethod
from pylab import *
import time
from tkinter import *
from tkinter import ttk
import tkinter.font as font
import networkx as nx
import matplotlib.pyplot as plt
from tkinter.ttk import Progressbar
import psutil

populationSize = 150
linkProbability = 0.06
initialInfectedRatio = 0.5
infectionProb = 0.6
recoveryProb = 0.4
#isolationProb = 0.8

#change from 0 for sus to gray & from 1 for infected to r
#should this represent the state not the number because below we start to initialize the population and assign the state randomly
#susceptible = 'gray'
#infected = 'r'

susceptible = "Orange"
infected = "Red"
recovered = 'Green'
# mitigation policies
#--------------------------------------------------------------------- Variables for drwaing a plot shows SIR---------.
# Total population, N.
N = 1000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.2, 1./10 
# A grid of time points (in days)
t = np.linspace(0, 160, 160)
#---------------------------------------------------------------------
root = Tk()
root.title('Simulator')
root.geometry('900x900')
Font = font.Font(size=15)
#-------------------------------------------------------------------- SIR model function in differential equations.
def plot(y, t, N, beta, gamma):
    S, I, R = y
    ds_dt = -beta * S * I / N
    dI_dt = beta * S * I / N - gamma * I
    dR_dt = gamma * I
    return ds_dt, dI_dt, dR_dt

#------------------------------Initial conditions vector.
    y0 = S0, I0, R0
    #------------------------------Integrate the SIR equitions over the time grif, t.
    ret = odeint(plot, y0, t, args=(N, beta, gamma))
    S, I, R = ret.T     
    #------------------------------Plot the data on three separate curves for S(t), I(t) and R(t)
    figure = plt.figure(facecolor='w')
    ax = figure.add_subplot(111, facecolor = '#dddddd', axisbelow=True)
    ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label = "Susceptible")
    ax.plot(t, I/100, 'r', alpha=0.5, lw=2, label='Infected')
    ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label="Recovered")
    ax.set_xlabel('Time/days')
    ax.set_ylabel('Number (1000s)')
    ax.set_ylim(0, 1.4)
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.3)
    
    for i in ('top', 'right', 'bottom', 'left'):
        ax.spines[i].set_visible(False)
    plt.show()
             
Btn = Button(text = "Click to show SIR in a Plot",  command = plot)
Btn.pack(padx = 10, pady = 20)
Btn['font'] = Font
#---------------------------------------------------------------------  
label = Label(root, text="Population : " + str(populationSize), font=("Helvectia", 15), fg = "orange")
# label.config(text = populationSize)
label.pack(side = TOP, padx=1,  pady=20 )
#---------------------------------------------------------------------  
label = Label(root, text="Infection Probability : " + str(infectionProb), font=("Helvectia", 15), fg="grey")
label.pack(side = TOP, padx=1,  pady=20 )
#---------------------------------------------------------------------  
label = Label(root, text="Recovery Probability : " + str(recoveryProb), font=("Helvectia", 15), fg="green")
label.pack(side = TOP, padx=1,  pady=20 )
#---------------------------------------------------------------------  
label = Label(root, text="Infection Time : " + str(recoveryProb), font=("Helvectia", 15), fg="dark blue")
label.pack(side = TOP, padx=1,  pady=20 )
#---------------------------------------------------------------------
def initialize():
    messagebox.showinfo("Information","Initialization has been completed")
          
    global time, network, positions, nextNetwork, infectionTime
    time = 0
    infectionTime = 0
    # Returns a random graph & it takes (no.of nodes and prob. for edge creation)
    network = nx.erdos_renyi_graph(populationSize, linkProbability)
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
       

Btn = Button(text = "Click for initialization  ",  command = initialize)
Btn.pack(padx = 10, pady = 20)
Btn['font'] = Font
#---------------------------------------------------------------------
def observe():
           
    cla()

    nx.draw(network,
            pos = positions,
            node_color = [network.nodes[i]['state'] for i in network.nodes],
            cmap = cm.Wistia,
            vmin=0,
            vmax=1,
            node_size = 150,
            )
    axis('image')
    title('time = ' + str(time))
    plt.axis('on')
    plt.show()
#---------------------------------------------------------------------
Btn = Button(text = " Click to observe the network",  command = observe)
Btn.pack(padx = 10, pady = 20)
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
            # The random() generates the initial population randomely. 
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
 
 
Btn = Button(text = "Click to update nodes in time interval",  command = update)
Btn.pack(padx = 10, pady = 20)
Btn['font'] = Font

#---------------------------------------------------------------------class individual-------------.
# class indiv(ABC):
    
#     def __init__(self, value=None, initial_params=None):
        
#         if value is not None:
#             self.value = value
#         else:
#             self.value = self._random_init(initial_params)
            
#     @abstractmethod # anotations uses to define abstract class.
#     def pair(self, other, pair_params):
#         pass
    
#     @abstractmethid
#     def mutate(self, mutate_params):
#         pass
    
#     @abstractmethod
#     def _random_init(self, initial_params):
#         pass
    
# class Optimazation(indiv):
#     def pair(self, other, pair_params):
#         return Optimization(pair_params['alpha'] * self.value + (1 - pair_params['alpha']) * other.value)
    
#     # def mutate(self, mutate_params):
        

# class Population():
    
#     def __init__(self, size, fitness, individual_class, initial_params):
#         self.fitness = fitness
#         self.individuals = [individual_class(initial_params = initial_params)]
        

            
#-------------------------------------------------------------------

def optimization():
    messagebox.showinfo("Information","under construction")

Btn = Button(text = "Optimization through evolutionary algorithm",  command = optimization)
Btn.pack(padx = 10, pady = 20)
Btn['font'] = Font

#-------------------------------------------------------------------------------------------------.
#StatusBar
status = Label(root, text="COVID-19 Simulator for ACIT 4610",
                      bd=10, bg="grey", relief=GROOVE, font=15)
status.pack(side=BOTTOM, fill=X, padx=10, pady=20)
#---------------------------------------------------------------------
#pycxsimulator.GUI().start(func=[initialize, observe, update])
root.mainloop()