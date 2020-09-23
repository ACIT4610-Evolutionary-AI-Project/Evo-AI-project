from tkinter import *
import tkinter as tk
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import networkx as nx
import json


data = json.load(open('data.json'))

plt.style.use('seaborn')

root = Tk()

root.geometry("780x600")
root.title('ACIT4160 - Project')
a = tk.Label(root, text="Modeling the pandemic of COVID-19", font=20)
a.pack(padx=10, pady=10)
frame = Frame(root)
frame.pack()


def objects():

 
    for i in data['nodes']:
        print(i)
    print('------------')
    for j in data['edges']:
        print(j)
    print('------------')
    for k in data['path']:
        print(k)
            
    
    # x = [8, 9, 7, 9, 10, 8, 9, 10, 8, 4, 2, 6, 7, 9, 12, 6]
    # y = [3, 2, 4, 8, 10, 4, 8, 4, 2, 3, 7, 10, 2, 3, 7, 9]
    # colors = [7, 5, 2, 7, 5, 2, 7, 5, 2, 7, 4, 2, 2, 1, 9, 1]

    # plt.scatter(x, y,  s=100, c=colors, edgecolors='green', linewidths=1, alpha=0.75)

    # plt.tight_layout()
    # plt.show()

# def observeRelation():
#     print('do')
    

button = tk.Button(root, text="Click to see the objects", fg="black", font=20, command=objects)
button.pack(side=tk.BOTTOM, padx=15, pady=15)

# button = tk.Button(root, text='Clicke to observe the objects and relationship between them', fg="black", font=20, command=observeRelation)
# button.pack(side=tk.BOTTOM, padx=17, pady=17)


root.mainloop()
