#ideas
#generate unique shapes using names
#generate multiple shapes
#change color
#paint shapes dot by dot. DONE


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
from random import seed
from random import random 
import random
import matplotlib.animation as animation


maxPrints = 100
mutationCycles=200
mutations = 0
coords=[]

def showGraph(show=0, arr=coords):
	global coords
	xs, ys = zip(*arr) 
	plt.figure()
	plt.plot(xs,ys, 'black') 
	plt.xlim(-1.5, 1.5)
	plt.ylim(-1.5, 1.5)
	plt.gca().set_aspect('equal', adjustable='box')
	ax = plt.gca()
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
	global maxPrints
	if(show==1):
		plt.show()
		maxPrints -= 1
	if (maxPrints<0):
		exit()

def cleanAndPrint():
	copy=[]
	for d in range(len(coords)-1):
		copy.append(coords[d])
		if (d%50==0):
			showGraph(1,copy)
	copy.append(copy[0])
	showGraph(1,copy)
	


def initialize():
	global coords
	def x(a):
		return 1*math.cos(a)

	def y(a):
		return 1*math.sin(a)

	seed()
	angles = []
	for i in range(math.floor(round(2*math.pi,3)*100)): #change the line if you want more points in the circles
		angles.append(i/100)

		
	print("###Your circle has these many points",len(angles))
	#printDebug(angles)
	for a in angles: 
		coords.append([x(a),y(a)]) #get the coordinates for each angle

	coords.append(coords[0]) #close the circle


def mutate():
	global coords
	seed()
	for v in range(len(coords)):
		def mutate_run():
			global mutations
			mutations += 1
			zx= random.randint(-50,50)/1000
			zy= random.randint(-50,50)/1000
			coords[v][0]=coords[v][0]+ zx
			coords[v][1]=coords[v][1]+ zy

			def roundDown(vv,ranx, rany):
				if (vv>0 and vv<629):
					ogx=coords[vv][0]
					ogy=coords[vv][1]
					coords[vv][0]=(ogx+(ogx+ ranx))/2
					coords[vv][1]=(ogy+(ogy+ rany))/2
				else:
					ogx=coords[len(coords)-1][0]
					ogy=coords[len(coords)-1][1]
					coords[len(coords)-1][0]=(ogx+(ogx+ ranx))/2
					coords[len(coords)-1][1]=(ogy+(ogy+ rany))/2

			def roundUp(vv,ranx,rany):
				if (vv<len(coords)-1):
					ogx=coords[vv][0]
					ogy=coords[vv][1]
					coords[vv][0]=(ogx+(ogx+ ranx))/2
					coords[vv][1]=(ogy+(ogy+ rany))/2
				else:
					ogx=coords[0][0]
					ogy=coords[0][1]
					coords[0][0]=(ogx+(ogx+ ranx))/2
					coords[0][1]=(ogy+(ogy+ rany))/2

			if(random.randint(0,60)<50):  #decide whether to edit the point or not
				roundUp(v+1,zx,zy)
				roundUp(v+2,zx,zy)
				roundUp(v+3,zx/1.5,zy/1.5)
				roundUp(v+4,zx/1.5,zy/1.5)
				roundDown(v-1,zx,zy)
				roundDown(v-2,zx,zy)
				roundDown(v-3,zx/1.5,zy/1.5)
				roundDown(v-4,zx/1.5,zy/1.5)

		if (v > len(coords)-1):
			break
		if(random.randint(0,60)==0):  #decide whether to edit the point or not
			mutate_run()
		else:
			if(random.randint(0,150)==0): 
				coords.pop(v)

initialize()

for d in range(mutationCycles):
	mutate()
	coords.append(coords[0]) #close the circle
	if (len(coords)<60):
		break
	if(d%50==0):
		cleanAndPrint()

coords.append(coords[0]) #close the circle
print("###Your circle only has these many points now",len(coords))




cleanAndPrint()

