from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import json
import networkx as nx

data = json.load(open('data.json'))
node_1 = ''
node_2 = ''


root = Tk()


root.geometry("780x600")
root.title('ACIT4160 - Project')
a = tk.Label(root, text="Modeling the pandemic of COVID-19 through AI")
a.pack()
frame = Frame(root)
frame.pack()


def slogan():
    print("print button")


menubar = Menu(root)
menubar.add_command(label="File", command=slogan)
menubar.add_command(label="Quit", command=root.quit)
root.config(menu=menubar)

w = Label(root, text="right click to see the result", width=50, height=25)
w.pack()

popup = Menu(root, tearoff=0)
popup.add_command(labe="Pause")
popup.add_command(label="Copy")

popup.add_separator()

popup.add_command(label="Home")

# def do_popup(event):
#
#     try:
#         popup.tk_popup(event.x_root, event.y_root,0)
#     finally:
#         popup.grab_release()


# Plot preview
def plot_preview():

    nodes = data.data['Switches'] + data.data['Hosts']
    path = data.data['Path']
    labels = {}
    edges_all = []
    edges_path = []
    G = nx.DiGraph()

    for link in data.data['Links']:
        for A, B in link.items():
            A_name = A.split('-')[0]
            A_if = A.split('-')[1]
            B_name = B.split('-')[0]
            B_if = B.split('-')[1]
            edges_all.append([A_name, B_name])
            labels[(A_name, B_name)] = A_if
            labels[(B_name, A_name)] = B_if

    for i in range(0, len(path) - 1):
        edges_path.append([path[i], path[i + 1]])

    G.add_nodes_from(nodes)
    G.add_edges_from(edges_all)

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, node_color='orange')
    nx.draw_networkx_labels(G, pos, node_size=800, font_size=10, with_labels=True)
    nx.draw_networkx_edges(G, pos, arrows=False)
    nx.draw_networkx_edges(G, pos, edges_path, edge_color='#00FF00', arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, labels, 0.8)
    plt.title('Topology graph based on "Links" dictionary in JSON file')
    plt.axis('on')
    plt.show()


# w.bind("<Button-3>", do_popup)
# b = Button(root, text="quit", command=root.destroy)
# b.pack()


button = tk.Button(root, text="Network of Cells", fg="black", command=plot_preview)
button.pack(side=tk.BOTTOM, padx=5, pady=5)

slogan = tk.Button(root, text="Hello", command=slogan)
slogan.pack(side=tk.BOTTOM, padx=5, pady=5)


# btnSubmit = Button(frame, text="submit", fg="red", activebackground="red")
# btnSubmit.pack(side=LEFT, padx=5, pady=5)
#
# btnRemove = Button(frame, text="remove", fg="green", activebackground="green")
# btnRemove.pack(side=RIGHT, padx=5, pady=5)

leftFrame = Frame(root)
leftFrame.pack(side=LEFT)

rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)


root.mainloop()
