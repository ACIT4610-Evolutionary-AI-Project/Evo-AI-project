from tkinter import *
import tkinter as tk

root = Tk()


root.geometry("780x600")
root.title('ACIT4160 - Project')
a = tk.Label(root, text="Modeling the pandemic of COVID-19 through AI")
a.pack()
frame = Frame(root)
frame.pack()


def slogan():
    print("print button")


# button = tk.Button(root, text="Show", fg="black", command=slogan)
# button.pack(side=tk.BOTTOM, padx=5, pady=5)
#
# slogan = tk.Button(root, text="Hello", command=slogan)
# slogan.pack(side=tk.BOTTOM, padx=5, pady=5)


btnSubmit = Button(frame, text="submit", fg="red", activebackground="red")
btnSubmit.pack(side=LEFT, padx=5, pady=5)

btnRemove = Button(frame, text="remove", fg="green", activebackground="green")
btnRemove.pack(side=RIGHT, padx=5, pady=5)

leftFrame = Frame(root)
leftFrame.pack(side=LEFT)

rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)



root.mainloop()
