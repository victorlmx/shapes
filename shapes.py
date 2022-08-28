import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
from random import seed
from random import random 
import random
import matplotlib.animation as animation


maxPrints = 10

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
	print("Printing plot..")
	plt.show()
	global maxPrints
	maxPrints -= 1
	if (maxPrints<0):
		print("max number of prints, exiting..")
		exit()


def initialize(coords_local):
	def x(a):
		return 1*math.cos(a)

	def y(a):
		return 1*math.sin(a)

	seed()
	angles = []
	for i in range(math.floor(round(2*math.pi,3)*100)): #change the line if you want more points in the circle
		angles.append(i/100)

		
	print("Your circle has these many points",len(angles))
	
	for a in angles: 
		coords_local.append([x(a),y(a)]) #get the coordinates for each angle

	coords_local.append(coords_local[0]) #close the circle
	showGraph(coords) #paint the circle prior to changing it


def mutate(coords_local):
	seed()
	for v in range(len(coords_local)):
		def mutate_run():
			print("Running mutate for v: ", v)
			zx= random.randint(-1,1)/10
			zy= random.randint(-1,1)/10
			print("zx ", zx, "zy ", zy)
			print("Original values:")
			print(coords_local[v])
			coords_local[v][0]=coords_local[v][0]+ zx
			coords_local[v][1]=coords_local[v][1]+ zy
			print("Changed values:")
			print(coords_local[v])

			def roundDown(vv,i):
				print("runDown..", vv)
				print("zx ", zx, "zy ", zy)
				if (vv-1>0 and vv-1<629):
					print("Original values:")
					print(coords_local[vv-1])
					coords_local[vv-1][0]=coords_local[vv-1][0]+ zx/i
					coords_local[vv-1][1]=coords_local[vv-1][1]+ zy/i
					print("After:")
					print(coords_local[vv-1])
				else:
					print("Original values:")
					print(coords_local[len(coords_local)-1])
					coords_local[len(coords_local)-1][0]=coords_local[len(coords_local)-1][0]+ zx/i
					coords_local[len(coords_local)-1][1]=coords_local[len(coords_local)-1][1]+ zy/i
					print("After:")
					print(coords_local[len(coords_local)-1])
				showGraph(coords)

			def roundUp(vv,i):
				print("runUp..", vv)
				print("zx ", zx, "zy ", zy)
				if (vv+1<len(coords_local)-1):
					print("Original values:")
					print(coords_local[vv+1])
					coords_local[vv+1][0]=coords_local[vv+1][0]+ zx/i
					coords_local[vv+1][1]=coords_local[vv+1][1]+ zy/i
					print("After:")
					print(coords_local[vv+1])
				else:
					print("Original values:")
					print(coords_local[0])
					coords_local[0][0]=coords_local[0][0]+ zx/i
					coords_local[0][1]=coords_local[0][1]+ zy/i
					print("After:")
					print(coords_local[0])
				showGraph(coords)

			roundUp(v+1,2)
			roundUp(v+2,4)
			roundUp(v+3,8)
			roundDown(v-1,2)
			roundDown(v-2,4)
			roundDown(v-3,8)

		print("Check if v will mutate.. : ", v)
		if(random.randint(0,15)==0):  #decide whether to edit the point or not
			mutate_run()


coords=[]
edits=1

initialize(coords)

for _ in range(edits):
	mutate(coords)
	showGraph(coords)



