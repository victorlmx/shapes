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
	plt.xlim(-2, 2)
	plt.ylim(-2, 2)
	plt.gca().set_aspect('equal', adjustable='box')
	#get current axes
	ax = plt.gca()
	#hide x-axis
	ax.get_xaxis().set_visible(False)
	#hide y-axis 
	ax.get_yaxis().set_visible(False)

def mainFunction(coords_local, angles_local):
	seed(1)
	for _ in range(100):
		value = random.randrange(6200)/1000
		angles_local.append(value)
	print(angles_local)
	angles_local.sort()
	
	for a in angles_local: 
		coords_local.append([x(a),y(a)])
	coords_local.append(coords_local[0])
	#showGraph(coords_local)

def mutate(coords_local):
	seed(1)
	for _ in range(180):
		value = random.randint(1,62)  #select random points to modify them
		coords_local[value][0]=coords_local[value][0]+random.randint(1,10)/10000
		coords_local[value][0]=coords_local[value][0]-random.randint(1,10)/10000

coords=[]
angles = []
mainFunction(coords, angles)

print("start mutating")

for _ in range(100):
	seed(4)
	mutate(coords)

showGraph(coords)

plt.show()
print("end")
