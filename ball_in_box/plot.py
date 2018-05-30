# -*- coding: utf-8 -*-  
from matplotlib.patches import Circle
import matplotlib.pyplot as plt


def answer(circles,blockers):    
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111)
    for block in blockers:
        ax.scatter(block[0],block[1], c='k')
    for circle in circles:
        x = circle[0]
        y = circle[1]
        r = circle[2]    
        cir = Circle(xy = (x, y), radius=r, alpha=0.4)
        ax.add_patch(cir)
    plt.xlim(-1.0, 1.0)
    plt.ylim(-1.0, 1.0)
    plt.show()