from tkinter import *
import tkinter as tk

root = Tk()

root.geometry("780x600")
root.title('Modeling of COVID-19 project')
# a = tk.Label(root, text="COVID-19")
# a.pack()
var = StringVar()
label = Label(root, textvariable=var, relief=RAISED)
var.set("COVID-19")
label.pack()


def slogan():
    print("print button")

button = tk.Button(root, text="Show", fg="black", command=slogan)
button.pack(side=tk.BOTTOM, padx=5, pady=5)

slogan = tk.Button(root, text="Hello", command=slogan)
slogan.pack(side=tk.BOTTOM, padx=5, pady=5)

root.mainloop()
