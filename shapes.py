import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
from random import seed
from random import random 
import random
import matplotlib.animation as animation


def x(a):
  return 1*math.cos(a)

def y(a):
  return 1*math.sin(a)

def showGraph(arr):
	xs, ys = zip(*arr) 
	plt.figure()
	plt.plot(xs,ys, 'black') 
	plt.xlim(-1, 1)
	plt.ylim(-1, 1)
	plt.gca().set_aspect('equal', adjustable='box')
	#get current axes
	ax = plt.gca()
	#hide x-axis
	ax.get_xaxis().set_visible(False)
	#hide y-axis 
	ax.get_yaxis().set_visible(False)
	plt.show()

def mainFunction():
	coords=[]
	angles = []
	##### list of all angles we want to use
	seed(1)
	for _ in range(100):
		value = random.randrange(62)/10
		angles.append(value)
	#angles.sort()
	
	for a in angles: 
		coords.append([x(a),y(a)])
		coords.append(coords[0])
	showGraph(coords)

mainFunction()
   


