#ideas
#idea: generate unique shapes using names
#idea: pick the probability of each mutation randomly

import math
import chart
import settings
import mutations

def makeCircle():
	angles = []
	for i in range(math.floor(round(2*math.pi,3)*settings.circleComplexity)): #change the line if you want more points in the circles
		angles.append(i/settings.circleComplexity)

	for a in angles: 
		settings.coords.append([1*math.cos(a),1*math.sin(a)]) #get the coordinates for each angle

	settings.coords.append(settings.coords[0]) #close the circle
	chart.cleanAndPrint()


settings.init()
makeCircle()

for d in range(settings.mutationCycles):
	mutations.run()

	if (len(settings.coords) < settings.minimumDots):
		print("Ending the mutations due to too many points lost")
		break
	if(d%20==0): #change this value to skip displaying some mutations
		chart.cleanAndPrint()


print("Process complete")
chart.cleanAndPrint()

