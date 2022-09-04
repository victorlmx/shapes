import settings
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def showGraph(show, arr):
    xs, ys = zip(*arr)
    plt.figure(1, figsize=(7, 7))
    plt.subplot()
    plt.plot(xs,ys, color='black',  label='shape')
    plt.xlim(-5.5, 5.5)
    plt.ylim(-5.5, 5.5)
    plt.gca().set_aspect('equal', adjustable='box')
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    if(show==1):
        plt.show()
    settings.maxPrints -= 1
    if (settings.maxPrints<0):
        print("Exiting due to too many printing")
        exit()

def cleanAndPrint(printSteps=False):
    copy=[]
    for d in range(len(settings.coords)-1): #shows the process of painting the shape
        copy.append(settings.coords[d])
    copy.append(copy[0])
    showGraph(1,copy)
    
