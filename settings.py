from random import seed
from random import random 
import random
import math

def init():
	global maxPrints
	global circleComplexity
	global mutationCycles
	global mutations
	global coords
	global minimumDots
	global rangeElimintate
	global rangeRound
	global rangeNucleus
	global rangeExile
	global rangeFix
	global rangeSharp

	maxPrints = 60
	circleComplexity = 100 # 10, 100, 1000
	mutationCycles=900
	mutations = 0
	coords=[]
	minimumDots = random.randint(100,500)
	rangeElimintate = random.randint(1,10)
	rangeRound = random.randint(1,100)
	rangeNucleus = random.randint(1,100)
	rangeExile = random.randint(1,100)
	rangeSharp = random.randint(1,100)
	rangeFix = random.randint(1,100)