import time
from tkinter import *

root = Tk()
root.title('InfectionTime')
root.geometry('600x600')

label = Label(root, text="myPython")
label.pack(pady = 20)

root.mainloop()


# def theTimeInterval():
#         start_time = time.time()
#         s = 0
#         for i in range (1, n + 1):
#             s = s + i 
#         end_time = time.time()
#         return s, end_time-start_time
# n = 5
# print(theTimeInterval())
    