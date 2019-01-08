import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal,rand
import time

plt.ion()
while True:
    x=rand(100)
    y=rand(100)
    plt.scatter(x,y)
    plt.draw()
    plt.pause(0.00001)
    plt.clf()