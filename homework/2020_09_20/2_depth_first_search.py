# 22p21i0098-อดุลวิทย์
# https://github.com/adulgun/adul

import numpy as np
import sys
import os

import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import more_itertools
from more_itertools import locate

def depth_first_search(graph, source):
    path = []
    stack = [source]
    while(len(stack) != 0):
        s = stack.pop()
        if s not in path:
            path.append(s)
        if s not in graph:
            continue
        for neighbor in graph[s]:
            stack.append(neighbor)
    return path


graph = {"A": ["D", "C", "B"],
         "B": ["E"],
         "C": ["G", "F"],
         "D": ["H"],
         "E": ["I"],
         "F": ["J"]}
DFS_path = depth_first_search(graph, "A")
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
