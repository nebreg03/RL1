import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import time

fig, ax = plt.subplots()
image = None

def init(graella, personatge):
    global image
    image = ax.imshow(np.zeros((len(graella), len(graella[0]))), cmap='viridis', interpolation='nearest')
    plt.xlim(0, len(graella[0]))
    plt.ylim(0, len(graella))
    plt.title("Grid Visualization")
    return image,

def update(frame, graella, personatge):
    global image
    for i in range(len(graella)):
        for j in range(len(graella[0])):
            color = 'white'
            if graella[i][j].propietats['fisica'] == 'prohibit':
                color = 'black'
            elif graella[i][j].propietats['fisica'] == 'final':
                color = 'green'
            elif graella[i][j] == personatge.estat_actual:
                color = 'red'

            ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, color=color))

    plt.xlim(0, len(graella[0]))
    plt.ylim(0, len(graella))
    plt.title("Grid Visualization")
    return image,
