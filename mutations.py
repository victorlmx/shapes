
import settings
from random import seed
from random import random 
import random

def mutate():
	seed()
	for v in range(len(settings.coords)):
		def mutate_run():
			settings.mutations += 1
			zx= random.randint(-50,50)/1000
			zy= random.randint(-50,50)/1000
			settings.coords[v][0]=settings.coords[v][0]+ zx
			settings.coords[v][1]=settings.coords[v][1]+ zy

			def roundDown(vv,ranx, rany):
				if (vv>0 and vv<629):
					ogx=settings.coords[vv][0]
					ogy=settings.coords[vv][1]
					settings.coords[vv][0]=(ogx+(ogx+ ranx))/2
					settings.coords[vv][1]=(ogy+(ogy+ rany))/2
				else:
					ogx=settings.coords[len(settings.coords)-1][0]
					ogy=settings.coords[len(settings.coords)-1][1]
					settings.coords[len(settings.coords)-1][0]=(ogx+(ogx+ ranx))/2
					settings.coords[len(settings.coords)-1][1]=(ogy+(ogy+ rany))/2

			def roundUp(vv,ranx,rany):
				if (vv<len(settings.coords)-1):
					ogx=settings.coords[vv][0]
					ogy=settings.coords[vv][1]
					settings.coords[vv][0]=(ogx+(ogx+ ranx))/2
					settings.coords[vv][1]=(ogy+(ogy+ rany))/2
				else:
					ogx=settings.coords[0][0]
					ogy=settings.coords[0][1]
					settings.coords[0][0]=(ogx+(ogx+ ranx))/2
					settings.coords[0][1]=(ogy+(ogy+ rany))/2

			if(random.randint(0,60)<50):  #decide whether to edit the point or not
				roundUp(v+1,zx,zy)
				roundUp(v+2,zx,zy)
				roundUp(v+3,zx/1.5,zy/1.5)
				roundUp(v+4,zx/1.5,zy/1.5)
				roundDown(v-1,zx,zy)
				roundDown(v-2,zx,zy)
				roundDown(v-3,zx/1.5,zy/1.5)
				roundDown(v-4,zx/1.5,zy/1.5)

		if (v > len(settings.coords)-1):
			break
		if(random.randint(0,60)==0):  #decide whether to edit the point or not
			mutate_run()
		else:
			if(random.randint(0,150)==0): 
				settings.coords.pop(v)