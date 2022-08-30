
import settings
from random import seed
from random import random 
import random
import math

def x(a):
	return 1*math.cos(a)

def y(a):
	return 1*math.sin(a)

def mutate():
	seed()
	for v in range(len(settings.coords)):
		def mutate_run(rounded=False, eliminate=False, nucleus=False, exile=False, fix=False):
			def roundDown(vv,ranx, rany):
				if (vv>0 and vv<629):
					ogx=settings.coords[vv][0]
					ogy=settings.coords[vv][1]
					settings.coords[vv][0]=(ogx+(ogx+ ranx))/2
					settings.coords[vv][1]=(ogy+(ogy+ rany))/2
				#else:
					#ogx=settings.coords[len(settings.coords)-1][0]
					#ogy=settings.coords[len(settings.coords)-1][1]
					#settings.coords[len(settings.coords)-1][0]=(ogx+(ogx+ ranx))/2
					#settings.coords[len(settings.coords)-1][1]=(ogy+(ogy+ rany))/2

			def roundUp(vv,ranx,rany):
				if (vv<len(settings.coords)-1):
					ogx=settings.coords[vv][0]
					ogy=settings.coords[vv][1]
					settings.coords[vv][0]=(ogx+(ogx+ ranx))/2
					settings.coords[vv][1]=(ogy+(ogy+ rany))/2
				#else:
					#ogx=settings.coords[0][0]
					#ogy=settings.coords[0][1]
					#settings.coords[0][0]=(ogx+(ogx+ ranx))/2
					#settings.coords[0][1]=(ogy+(ogy+ rany))/2

			settings.mutations += 1
			if (nucleus):
				settings.coords[v][0]=settings.coords[v][0]*.7009
				settings.coords[v][1]=settings.coords[v][1]*.7009
			elif (exile):
				settings.coords[v][0]=settings.coords[v][0]*1.2
				settings.coords[v][1]=settings.coords[v][1]*1.2
			elif (fix):
				for a in range(10): 
					settings.coords.append([x(a),y(a)]) #get the coordinates for each angle
			else:
				zx= random.randint(-25,25)/1000
				zy= random.randint(-25,25)/1000
				settings.coords[v][0]=settings.coords[v][0]+ zx
				settings.coords[v][1]=settings.coords[v][1]+ zy

			if (eliminate):
				print("eliminate!")
				if (v > len(settings.coords)-1):
					settings.coords.pop(v)
				if (v > len(settings.coords)-1):
					settings.coords.pop(v)
				if (v > len(settings.coords)-1):
					settings.coords.pop(v)
				if (v > len(settings.coords)-1):
					settings.coords.pop(v)
				if (v > len(settings.coords)-1):
					settings.coords.pop(v)
				if (v > len(settings.coords)-1):
					settings.coords.pop(v)
			if(rounded):  #decide whether to edit the point or not
				roundUp(v+1,zx,zy)
				roundUp(v+2,zx,zy)
				roundUp(v+3,zx/1.5,zy/1.5)
				roundUp(v+4,zx/1.5,zy/1.5)
				roundDown(v-1,zx,zy)
				roundDown(v-2,zx,zy)
				roundDown(v-3,zx/1.5,zy/1.5)
				roundDown(v-4,zx/1.5,zy/1.5)

		rand = random.randint(0,500)
		if(rand%33==1):
			mutate_run(eliminate=True)
		elif (rand==2):
			mutate_run(rounded=True)
		elif (rand==3):
			mutate_run()
		elif (rand==4 and random.randint(0,50)==1):
			mutate_run(nucleus=True)
		elif (rand==5 and random.randint(0,50)==1):
			mutate_run(exile=True)
		elif (rand==6):
			print("FIX")
			mutate_run(fix=True)
			