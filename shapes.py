import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
from random import seed
from random import random 
import random
import matplotlib.animation as animation

coords=[]
angles = []
maxPoints = 100

def x(a):
  return 1*math.cos(a)

def y(a):
  return 1*math.sin(a)

def showGraph(arr):
	xs, ys = zip(*arr) 
	plt.figure()
	plt.plot(xs,ys, 'black') 
	plt.xlim(-1.5, 1.5)
	plt.ylim(-1.5, 1.5)
	plt.gca().set_aspect('equal', adjustable='box')
	ax = plt.gca()
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

def mainFunction(coords_local, angles_local):
	seed()
	for _ in range(maxPoints):
		value = random.randrange(6200)/1000
		angles_local.append(value)
	angles_local.sort()
	
	for a in angles_local: 
		coords_local.append([x(a),y(a)])
	coords_local.append(coords_local[0])
	#showGraph(coords_local)

def mutate(coords_local):
	print(angles)
	seed()
	for _ in range(len(angles)):
		value = random.randint(1,maxPoints)  #select random points to modify them
		z= random.randint(-1,1)/100
		coords_local[value][0]=coords_local[value][0]+ z
		z= random.randint(-1,1)/100
		coords_local[value][1]=coords_local[value][1]+ z

		if (value>0):
			coords_local[value-1][0]=coords_local[value-1][0]+ z/2
			coords_local[value-1][1]=coords_local[value-1][1]+ z/2
		else:
			coords_local[len(coords_local)][0]=coords_local[value-1][0]+ z/2
			coords_local[len(coords_local)][1]=coords_local[value-1][1]+ z/2


		if (value<maxPoints):
			coords_local[value+1][0]=coords_local[value+1][0]+ z/2
			coords_local[value+1][1]=coords_local[value+1][1]+ z/2
		else:
			coords_local[0][0]=coords_local[value-1][0]+ z/2
			coords_local[0][1]=coords_local[value-1][1]+ z/2
	showGraph(coords)

mainFunction(coords, angles)

for _ in range(10):
	mutate(coords)


plt.show()
