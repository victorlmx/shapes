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

def makeWeirdShape():
	for a in range(0,630): 
		settings.coords.append([2*math.cos(a/100)+math.sin(2*a/100)*math.cos(60*a/100),math.sin(2*a/100)+math.sin(60*a/100)]) #get the coordinates for each angle
	chart.cleanAndPrint()


settings.init()
print("Random configs:")
print("minimumDots",settings.minimumDots)
print("rangeElimintate",settings.rangeElimintate)
print("rangeRound",settings.rangeRound)
print("rangeNucleus",settings.rangeNucleus)
print("rangeExile",settings.rangeExile)
print("rangeSharp",settings.rangeSharp)
print("rangeFix",settings.rangeSharp)

makeCircle()
#makeWeirdShape()

for d in range(settings.mutationCycles):
	if (len(settings.coords) < settings.minimumDots):
		print("Ending the mutations due to too many points lost")
		break

	mutations.run()
	if(d%20==0): #change this value to skip displaying some mutations
		chart.cleanAndPrint()

print("Size:", len(settings.coords))
print("Process complete")
chart.cleanAndPrint()
exit()	

