import settings
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def showGraph(show, arr):
    xs, ys = zip(*arr)
    plt.figure(1, figsize=(10, 10))
    plt.subplot()
    plt.plot(xs,ys, color='black',  label='shape')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
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
        if (printSteps and d%80==0):  #how many steps to display at once
            showGraph(1, copy)
    copy.append(copy[0])
    showGraph(1,copy)
    
