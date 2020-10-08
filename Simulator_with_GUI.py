# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:48:21 2020

@author: Nima
"""

# import pycxsimulator
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
#---------------------------------------------------------------------
root = Tk()
root.title('Simulator')
root.geometry('900x900')
Font = font.Font(size=15)
#---------------------------------------------------------------------
ttk.Label(root, text="Time", font=("Helvectia", 20)).pack()  
#-----Create Panedwindow
# panedwindow = ttk.Panedwindow(root, orient=HORIZONTAL)
# panedwindow.pack(fill = BOTH, expand=True)
#-----Create Frames
# fram1=ttk.Frame(panedwindow, width=100, height=300, relief=SUNKEN)
# fram2=ttk.Frame(panedwindow, width=400, height=400, relief=SUNKEN)
# panedwindow.add(fram1, weight=1)
# panedwindow.add(fram2, weight=1)
#------------------
def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")
    my_label.config(text=hour + ":" + minute + ":" + second + "" + " " + am_pm)
    my_label.after(1000, clock)
    
    my_label2.config(text=day)
    
def update_clock():
    my_label.config(text = "New Text")
    
my_label = Label(root, text="", font=("Helvectia", 25), fg = "grey")
my_label.pack(side = TOP, padx=2, pady=20)

my_label2 = Label(root, text="", font=("Helvectia", 14), fg = "grey")
my_label.pack(side = TOP, padx=2, pady=10)

clock()
#---------------------------------------------------------------------  
label = Label(root, text="Population : " + str(populationSize), font=("Helvectia", 15), fg = "orange")
# label.config(text = populationSize)
label.pack(side = TOP, padx=1,  pady=1 )
#---------------------------------------------------------------------  
# label = Label(root, text="Link Probability : " + str(linkProbability), font=("Helvectia", 15), fg="black")
# label.pack(side = TOP, padx=1,  pady=1 )
# #---------------------------------------------------------------------  
# label = Label(root, text="Initial Infected Ratio : " + str(initialInfectedRatio), font=("Helvectia", 15), fg="blue")
# label.pack(side = TOP, padx=1,  pady=1 )
#---------------------------------------------------------------------  
label = Label(root, text="Infection Probability : " + str(infectionProb), font=("Helvectia", 15), fg="grey")
label.pack(side = TOP, padx=1,  pady=1 )
#---------------------------------------------------------------------  
label = Label(root, text="Recovery Probability : " + str(recoveryProb), font=("Helvectia", 15), fg="green")
label.pack(side = TOP, padx=1,  pady=1 )
#---------------------------------------------------------------------  
label = Label(root, text="Infection Time : " + str(recoveryProb), font=("Helvectia", 15), fg="dark blue")
label.pack(side = TOP, padx=1,  pady=1 )
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

#---------------------------------------------------------------------
def optimize():
    messagebox.showinfo("Information","under construction")

Btn = Button(text = "Optimization through evolutionary algorithm",  command = optimize)
Btn.pack(padx = 10, pady = 20)
Btn['font'] = Font
#---------------------------------------------------------------------
# Progress bar widget
cpu_progress_bar = Progressbar(root, orient = HORIZONTAL, length = 200, mode = 'determinate')
cpu_progress_bar['maximum'] = 100
cpu_progress_bar['value'] = 30
cpu_progress_bar.pack(pady = 40)
cpu_label = Label(root, text='CPU usage')
cpu_label.pack()

memory_progress_bar = Progressbar(root, orient = HORIZONTAL, length = 200, mode = 'determinate')
memory_progress_bar['maximum'] = 100
memory_progress_bar['value'] = 50
memory_progress_bar.pack(pady = 10)
memory_label = Label(root, text='Memory usage')
memory_label.pack()
#---------------------------------------------------------------------
# Cpu and Memory usage to monitor system performance 
def tick():

    INTERVAL = 500

    cpu_usage = psutil.cpu_percent()
    cpu_progress_bar['value'] = cpu_usage
    cpu_label['text'] = 'CPU usage when update nodes: ' + str(cpu_usage) + ' % '

    memory_usage = psutil.virtual_memory()._asdict()['percent']
    memory_progress_bar['value'] = memory_usage
    memory_label['text'] = 'Memory usage when update nodes: ' + str(memory_usage) + ' % '

    root.after(INTERVAL, tick)

tick()
#---------------------------------------------------------------------
#StatusBar
status = Label(root, text="COVID-19 Simulator for ACIT 4610",
                      bd=10, bg="grey", relief=GROOVE, font=15)
status.pack(side=BOTTOM, fill=X, padx=10, pady=20)
#---------------------------------------------------------------------
#pycxsimulator.GUI().start(func=[initialize, observe, update])
root.mainloop()