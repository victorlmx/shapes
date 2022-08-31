
import settings
from random import seed
from random import random 
import random
import math

def mutate(v, rounded=False, eliminate=False, nucleus=False, exile=False, fix=False):
	def roundDown(vv,ranx, rany):
		if (vv>0 and vv<629):
			ogx=settings.coords[vv][0]
			ogy=settings.coords[vv][1]
			settings.coords[vv][0]=(ogx+(ogx+ ranx))/2
			settings.coords[vv][1]=(ogy+(ogy+ rany))/2

	def roundUp(vv,ranx,rany):
		if (vv<len(settings.coords)-1):
			ogx=settings.coords[vv][0]
			ogy=settings.coords[vv][1]
			settings.coords[vv][0]=(ogx+(ogx+ ranx))/2
			settings.coords[vv][1]=(ogy+(ogy+ rany))/2

	settings.mutations += 1
	if (nucleus):
		settings.coords[v][0]=settings.coords[v][0]*.9009
		settings.coords[v][1]=settings.coords[v][1]*.9009
	elif (exile):
		settings.coords[v][0]=settings.coords[v][0]*1.2
		settings.coords[v][1]=settings.coords[v][1]*1.2
	elif (fix):
		for a in range(1,20):
			settings.coords[a]=[1*math.cos(a/100),1*math.sin(a/100)]
	elif (eliminate):
		if (v>0 and v<len(settings.coords)-2):
			settings.coords.pop(v)
		if (v>0 and v<len(settings.coords)-2):
			settings.coords.pop(v)
		if settings.coords[v]!=settings.coords[0]:
			settings.coords.append(settings.coords[0])

	else:
		zx= random.randint(-25,25)/1000
		zy= random.randint(-25,25)/1000
		settings.coords[v][0]=settings.coords[v][0]+ zx
		settings.coords[v][1]=settings.coords[v][1]+ zy
	if(rounded): 
		roundUp(v+1,zx,zy)
		roundUp(v+2,zx,zy)
		roundUp(v+3,zx/1.5,zy/1.5)
		roundUp(v+4,zx/1.5,zy/1.5)
		roundDown(v-1,zx,zy)
		roundDown(v-2,zx,zy)
		roundDown(v-3,zx/1.5,zy/1.5)
		roundDown(v-4,zx/1.5,zy/1.5)

    #this looks sick:
	#if (settings.coords[v][0]>1): settings.coords[v][0]=1
	#if (settings.coords[v][1]<0): settings.coords[v][1]=0

def run():
	v=0
	while (v < len(settings.coords)-1 and len(settings.coords) > settings.minimumDots):
		#print(len(settings.coords))
		rand = random.randint(0,500)
		if(rand==1 and random.randint(0,settings.rangeElimintate)==1):
			mutate(v, eliminate=True)
		elif (rand==2 and random.randint(0,settings.rangeRound)==1):
			mutate(v, rounded=True)
		elif (rand%100==0 and random.randint(0,settings.rangeSharp)==1):
			mutate(v)
		elif (rand==4 and random.randint(0,settings.rangeNucleus)==1):
			mutate(v,nucleus=True)
		elif (rand==5 and random.randint(0,settings.rangeExile)==1):
			mutate(v,exile=True)
		elif (rand==6 and random.randint(0,settings.rangeFix)==1):
			mutate(v,fix=True)
		v += 1



