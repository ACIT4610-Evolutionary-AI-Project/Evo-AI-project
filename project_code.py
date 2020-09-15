from tkinter import *
import tkinter as tk
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import json
import networkx as nx

plt.style.use('seaborn')

data = json.load(open('data.json'))

root = Tk()

root.geometry("780x600")
root.title('ACIT4160 - Project')
a = tk.Label(root, text="Modeling the pandemic of COVID-19")
a.pack()
frame = Frame(root)
frame.pack()


def plot():


    x = [8, 9, 7, 9, 10, 8, 9, 10, 8, 4, 2, 6, 7, 9, 12, 6]
    y = [3, 2, 4, 8, 10, 4, 8, 4, 2, 3, 7, 10, 2, 3, 7, 9]
    colors = [7, 5, 2, 7, 5, 2, 7, 5, 2, 7, 4, 2, 2, 1, 9, 1]
    plt.scatter(x, y, s=200, c=colors, edgecolors='black', linewidths=1, alpha=0.75)

    # girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
    # boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
    # grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # fig = plt.figure()
    # ax = fig.add_axes([0, 0, 1, 1])
    # ax.scatter(grades_range, girls_grades, color='r')
    # ax.scatter(grades_range, boys_grades, color='b')
    # ax.set_xlabel('Grades Range')
    # ax.set_ylabel('Grades Scored')
    # ax.set_title('scatter plot')
    plt.tight_layout()
    plt.show()


# menubar = Menu(root)
# menubar.add_command(label="File", command=plot)
# menubar.add_command(label="Quit", command=root.quit)
# root.config(menu=menubar)


button = tk.Button(root, text="Network of Cells", fg="black", command=plot)
button.pack(side=tk.BOTTOM, padx=5, pady=5)


root.mainloop()
