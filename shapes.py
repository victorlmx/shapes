#ideas
#generate unique shapes using names
#generate multiple shapes
#change color
#paint shapes dot by dot. DONE

import math
import chart
import settings
import mutations

def initialize():
	def x(a):
		return 1*math.cos(a)

	def y(a):
		return 1*math.sin(a)

	angles = []
	for i in range(math.floor(round(2*math.pi,3)*settings.circleComplexity)): #change the line if you want more points in the circles
		angles.append(i/settings.circleComplexity)


	for a in angles: 
		settings.coords.append([x(a),y(a)]) #get the coordinates for each angle

	settings.coords.append(settings.coords[0]) #close the circle
	chart.cleanAndPrint()


settings.init()
initialize()

for d in range(settings.mutationCycles):
	mutations.mutate()
	settings.coords.append(settings.coords[0]) #close the circle
	if (len(settings.coords)<settings.circleComplexity):
		print("Ending the mutations due to too many points lost")
		break
	if(d%10==0): #display all mutations?
		chart.cleanAndPrint()

print("Process complete")

settings.coords.append(settings.coords[0]) #close the circle

chart.cleanAndPrint()
chart.cleanAndPrint()

