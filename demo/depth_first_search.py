import numpy as np
import sys
import os

import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import more_itertools
from more_itertools import locate

sys.path.append(os.path.abspath(os.path.join('..')))
from super_ai.homework import *

hw = Homework()

graph = {"A": ["D", "C", "B"],
         "B": ["E"],
         "C": ["G", "F"],
         "D": ["H"],
         "E": ["I"],
         "F": ["J"]}
DFS_path = hw.depth_first_search(graph, "A")
G = nx.Graph(graph)
list_G = list(G.nodes)
lenght_G = len(list_G)
pos = nx.spring_layout(G)
fig, ax = plt.subplots()
run_color = 0

def update(frame):
    global run_color
    ax.clear()
    color_map = ['green'] * lenght_G
    index_change = list(locate(list_G, lambda a: a == DFS_path[run_color]))[0]
    color_map[index_change] = 'red'
    nx.draw(G, node_color=color_map, pos=pos, with_labels=True)
    run_color += 1
    if run_color == lenght_G:
        run_color = 0


ani = matplotlib.animation.FuncAnimation(
    fig, update, interval=1000, repeat=True)
plt.show()
